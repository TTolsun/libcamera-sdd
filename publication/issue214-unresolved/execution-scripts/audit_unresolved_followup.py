from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,wait,FIRST_COMPLETED
import json,copy
from sdd.config import load
from sdd.facts.model import KnowledgeModel
from sdd.consistency import groups,request,batches,review_store,validate,audit
from sdd.validation_stage import stage
from sdd.execution_lock import lease
from sdd.generation_run import Execution
from sdd.cli_checkpoint import Capture
from sdd.llm import Agent
R=Path('build/issue214/unresolved-followup');cfg=load(R/'independent-review.yaml');model=KnowledgeModel.load(cfg.facts_path);pending=[];reused=0
with stage() as inputs:
 inputs.pin(cfg,model)
 for group in groups(cfg):
  for index,batch in enumerate(batches(request(cfg,model,group),max_input_chars=cfg.agent.max_input_chars)):
   store,_=review_store(cfg,batch)
   if store.read() is None:pending.append((f"consistency_{group['id']}_{index}",batch))
   else:reused+=1
print(dict(stage='contract-review',fresh_remaining=len(pending),completed_checkpoint_reuse=reused,concurrent_cli_workers=2,reason='Only canonical changed batches; original validation and provenance unchanged.'),flush=True)
def run(item):
 key,batch=item;local=copy.deepcopy(cfg);e=Execution(local,Agent(local.agent,local.build_dir/'prompts'))
 with e.track('changed-contract-batch'),e.document('consistency',[key]),stage() as inputs:
  inputs.pin(local,model);e.unit(key,'running');store,data=review_store(local,batch);cached=store.read()
  if cached:
   checked=validate(batch,cached[0]['raw']);assert checked==cached[0]['statements'];e.unit(key,'checkpoint-revalidated');return key,'revalidated'
  capture=Capture(e);raw=capture.chat(**data,tag=key);checked=validate(batch,raw);store.write(raw,checked,capture);assert capture.receipts;e.unit(key,'completed');return key,'completed'
with lease(cfg,'consistency'):
 with ThreadPoolExecutor(max_workers=2) as pool:
  remaining=iter(pending);active={}
  for _ in range(min(2,len(pending))):
   item=next(remaining);active[pool.submit(run,item)]=item[0]
  completed=0
  while active:
   done,_=wait(active,timeout=30,return_when=FIRST_COMPLETED)
   if not done:print(dict(status='running',current=list(active.values()),completed=completed,planned=len(pending),restarted=False),flush=True);continue
   for future in done:
    active.pop(future);print(future.result(),flush=True);completed+=1
   for _ in done:
    item=next(remaining,None)
    if item:active[pool.submit(run,item)]=item[0]
# Run the ordinary audit over every canonical batch. It must revalidate all
# prewarmed receipts and existing verdicts, not substitute a custom approval.
result=audit(cfg,model,Agent(cfg.agent,cfg.build_dir/'prompts'))
print(dict(status=result['status'],fresh_batches=result['fresh_batches'],reused_batches=result['reused_batches'],unresolved=len(result['unresolved'])),flush=True)
