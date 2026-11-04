from pathlib import Path
import copy,json,hashlib
from sdd.config import load
from sdd.facts.model import KnowledgeModel
from sdd.document_metadata import split_frontmatter
from sdd.design_request import prepare_requests,_design_units,_unit_tag
from sdd.design_execution import _request_unit
from sdd.design_response import validate_answers
from sdd.design_types import DesignResult
from sdd.evidence import fingerprint
from sdd.llm import Agent
from sdd.generation_run import Execution
from sdd.validation_stage import stage
from sdd.execution_lock import lease
from sdd.generate import Generator
from sdd.generated_design import verify

R=Path('build/issue214/draft-v1');O=Path('build/issue214/unresolved-followup');cfg=load(O/'generation.yaml');model=KnowledgeModel.load(cfg.facts_path);sec=next(s for s in cfg.sections() if s['id']=='scenario-queue_request');path=cfg.sdd_dir/'scenarios/queue_request.md';previous=(R/'run/manuscripts/scenarios/queue_request.md').read_text(encoding='utf-8');meta,_=split_frontmatter(previous);old=meta['generated_design'];unit=next(u for u in _design_units(sec,{}) if u['id']=='acceptance')
assert cfg.agent.runner=='claude' and cfg.agent.model=='claude-haiku-5-5' and cfg.agent.args==['--effort','high','--setting-sources','project,local']
plan_record=dict(schema=1,status='planned',stage='single-unit-generation',new_draft_units=['scenario-queue_request/acceptance/answer'],new_internal_grounding_units=['scenario-queue_request/acceptance/answer'],historical_carryover=['scenario-queue_request/dispatch/transfer','scenario-queue_request/dispatch/device'],reason='Full-section planner correctly cannot claim exact drafting-profile compatibility for older unchanged dispatch units. Do not fabricate compatible identities or redraft them. Use the existing unit generation API for the selected acceptance unit and the normal deterministic validator/materializer for explicit historical carryover, preserving their original topic inputs, agents and grounding policy.',source_commit=model.meta['source_commit'],human_review='pending');(O/'single-unit-plan.json').write_text(json.dumps(plan_record,indent=2)+'\n',encoding='utf-8')
e=Execution(cfg,Agent(cfg.agent,cfg.build_dir/'prompts'))
with lease(cfg,'generation'),e.track('single-unit-generation'),e.document(sec['id'],[_unit_tag(sec,unit)]):
 with stage() as inputs:
  inputs.pin(cfg,model);plan=prepare_requests(cfg,model,sec,previous);answers=copy.deepcopy(old['answers']);answers.pop('acceptance')
  statements,checkpoint=_request_unit(cfg,model,e,sec,unit,plan.prompts['acceptance'],plan.policy['design_grounding'],None,answers)
  assert [a['text'] for a in statements[1:]]==[a['text'] for a in old['answers']['acceptance'][1:]],'Unnecessary paragraph changes rejected'
  answers['acceptance']=statements;pinned,resolved,report=validate_answers(model,sec,answers)
  artifact=copy.deepcopy(old);artifact.update(answers=answers,input_fingerprint=fingerprint(model,sec),generated_topics=['acceptance'],reused_topics=['dispatch']);artifact['topic_inputs']['acceptance']=plan.inputs['acceptance']
  artifact['followup_generation']=dict(selected_unit='acceptance/answer',native_checkpoint=checkpoint,current_grounding_policy=plan.policy.get('grounding_policy'),historical_dispatch='Original topic_inputs, agent and grounding_policy retained; source/contract revalidated, not new generation or human approval.')
  inputs.verify()
 g=Generator(cfg,model,e);g.generated_designs[sec['id']]=DesignResult(pinned,resolved,report,artifact);g._prose(sec);verify(model,sec,path.read_text(encoding='utf-8'),cfg=cfg)
 e.unit(_unit_tag(sec,unit),'completed')
after,_=split_frontmatter(path.read_text(encoding='utf-8'));assert after['generated_design']['answers']['dispatch']==old['answers']['dispatch'];assert after['generated_design']['topic_inputs']['dispatch']==old['topic_inputs']['dispatch']
record=dict(schema=1,status='generated',source_commit=model.meta['source_commit'],changed_document='scenarios/queue_request.md',new_draft_units=1,new_grounding_units=1,unchanged_dispatch_statements=len(old['answers']['dispatch']),other_acceptance_paragraphs_verbatim=True,old_first=old['answers']['acceptance'][0]['text'],new_first=statements[0]['text'],native_checkpoint=checkpoint,human_review='pending');(O/'generation-result.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(record,ensure_ascii=False,indent=2),flush=True)
