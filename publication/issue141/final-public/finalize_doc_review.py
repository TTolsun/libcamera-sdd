"""Verify the completed call after recording-helper error; do not run a model again."""
from pathlib import Path
import json,datetime,hashlib,subprocess
from sdd.call_records import load_record
from sdd.cli_provenance import verify_cli_receipt
from sdd.cli_agent import build_prompt
from sdd.config import load
w=Path(__file__).resolve().parent;out=w/'final-terra-doc-review-attempt4'
paths=list((out/'prompts/calls').rglob('*.receipt.json'));assert len(paths)==1
cfg=load(Path('sdd.yaml')).agent
r=load_record(paths[0]);assert r.receipt['transport']=='cli'
checked=verify_cli_receipt(r.request,r.raw,r.receipt,out/'prompts/calls',cfg)
assert checked['arguments_verified']
result=json.loads(r.raw);assert result==json.loads((out/'result.json').read_bytes())
assert len(result['findings'])==1
for name in ('publication157-final-ci.json','publication157-final-push-ci.json'):
 c=json.loads((w/name).read_bytes());assert c['headSha']=='411a74ac434c2ba0f39f3cd610335d5d4d9268b2' and c['conclusion']=='success' and len(c['jobs'])==4 and all(j['conclusion']=='success' for j in c['jobs'])
scope={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':'411a74ac434c2ba0f39f3cd610335d5d4d9268b2','profile':{'kind':cfg.kind,'runner':cfg.runner,'model':cfg.model,'args':cfg.args},'native_receipts_verified':1,'new_model_calls':1,'scope':'Entire own3documentdiff plus stated facts; not full repository verification or human approval','preflight_attempts':{'attempt1':'local raw-input length precheck; no model invocation','attempt2':'production CLI schema-inclusive size precheck refused before invocation','attempt3':'local full-prompt length precheck; no invocation'},'post_call_helper_error':'The call completed and result/receipt were preserved, then private recorder incorrectly looked for receipt.kind; correct field transport checked without another call','findings_disposition':[{'original':result['findings'][0],'status':'resolved by current authoritative CI evidence, no document claim broadened','evidence':['publication157-final-ci.json','publication157-final-push-ci.json'],'reason':'Review input said head411 CI pending.411a74a is a commit prefix, not PR411. The document points to PR157 current-head results without asserting pending jobs passed. Both same-head runs are now completed with all8 jobs successful; final PR body/comment record actual1945Ubuntu/1944+1Windows counts. Historical72 results remain explicitly historical.'}]}
(out/'scope.json').write_text(json.dumps(scope,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'native_record_verified':True,'model':cfg.model,'review_findings':1,'resolved_with_actual_same_head_CI':True}))
