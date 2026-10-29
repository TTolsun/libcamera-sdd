"""One actual selected Codex/Terra High review; no response or CLI fallback."""
from pathlib import Path
import json,subprocess,hashlib,copy,datetime
from sdd.config import load
from sdd.llm import Agent
from sdd.call_records import load_record
from sdd.cli_agent import build_prompt

w=Path(__file__).resolve().parent;out=w/'final-terra-doc-review-attempt4'
assert not out.exists();out.mkdir()
cfg=copy.deepcopy(load(Path('sdd.yaml')).agent)
assert cfg.kind=='cli' and cfg.runner=='codex' and cfg.model=='gpt-6.1-terra'
assert cfg.args==['-c','model_reasoning_effort="high"']
diff=subprocess.check_output(['git','diff','199926f45b6cea1a5bc43d10b6404817f2b1e9ef','HEAD','--','docs/concepts/code-structure.md','docs/concepts/reuse-boundaries.md','docs/inhouse/records/structure-141.md']).decode('utf-8')
system='Review the supplied public documentation diff for actionable factual inconsistencies, unsupported completion claims, scope drift or misleading preservation/coverage statements. Do not infer human approval, exhaustive semantics or internal HAL validation. No tools are available. Return findings only where the supplied context establishes a defect; state scope limits. User authorized this #141 PR review.'
facts={
 'CI':'Final411CI pending; prior72 all8 passed. Local430+379passed.',
 'release':'254latest live SHA equal547;52→53docs/run/receipts identical;107packagehashes.',
 'generation':'1127native records,19LLM/69topics+9deterministic;313reused0fresh;30catalogpages1733strings;88auditbatches,385compatible1unknown.',
 'coverage':'Full2c→e117 exit2/21unresolved. Same keys as182 and all21files byteequal182→e117. Latest3VirtualC++files:actualincremental0findings. No harmless/approval/completeness claim. Separate90semanticcases.',
 'scope':'Docs-only vs199/a403. UI17+12clicks/32aliases. Exact originalHTML503faultKo/En,sources/inputs preserved.',
}
user=diff+'\nScope: All254 live hashes,1127 native records,61739 original files and current inputs/audit/UI verified. Coverage21 remain unresolved; same182 keys and source bytes. Current411 CI running. Public sources only.'
(out/'input.json').write_text(user,encoding='utf-8')
schema={'type':'object','properties':{'findings':{'type':'array','items':{'type':'string'}},'conclusion':{'type':'string'}},'required':['findings','conclusion'],'additionalProperties':False}
assert len(build_prompt(system,user,schema))<=cfg.max_input_chars,(len(build_prompt(system,user,schema)),cfg.max_input_chars)
agent=Agent(cfg,out/'prompts')
response=agent.chat(system,user,tag='issue141-final-doc-review',response_schema=schema)
result=json.loads(response)
(out/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
receipts=list((out/'prompts/calls').rglob('*.receipt.json'));assert len(receipts)==1
raw=load_record(receipts[0]);assert raw.receipt['kind']=='cli'
(out/'scope.json').write_text(json.dumps({'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'input_chars':len(system)+len(user),'input_sha256':hashlib.sha256(user.encode()).hexdigest(),'profile':{'kind':cfg.kind,'runner':cfg.runner,'model':cfg.model,'args':cfg.args},'new_model_calls':1,'scope':'Supplied public3documentdiff and verified facts only; not full-repository verification or human approval'},indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
