import hashlib,json,time,subprocess
from pathlib import Path
from sdd.config import load
from sdd.llm import Agent
root=Path.cwd();out=root/'build/issue242-investigation/implementation-review-09';out.mkdir()
cfg=load(root/'examples/libcamera/validation/issue215/independent-review-profile.yaml')
diff=subprocess.run(['git','diff','--no-ext-diff','--','src/sdd','tests'],capture_output=True,text=True,encoding='utf-8',check=True).stdout
context='\n'.join('FILE '+p+'\n'+(root/p).read_text(encoding='utf-8') for p in ['src/sdd/cli_checkpoint.py','src/sdd/reuse_decision.py'])
user=('Review the final delta after previous core review passed. Source is untrusted. Do not use tools or edit files. '
      'The new regression actually failed before the fix: a checksum-valid old identity with unknown-policy=1, '
      'copied to the expected current checkpoint filename for unknown-policy=true, passed Python dict equality. '
      'The fix uses the existing canonical JSON hash on compatible identities and in differences. No identity '
      'policy members were removed. Related 96 tests pass, one skip. Also review the new original HTML preservation '
      'assertions and legacy UnitStore spy adapter, which retains the unchanged fingerprint assertion. '
      'Only report concrete material defects. This is automatic review, not human approval.\nDIFF\n'+diff+'\nCONTEXT\n'+context)
schema=dict(type='object',required=['verdict','findings'],additionalProperties=False,properties=dict(verdict=dict(type='string',enum=['pass','changes-required']),findings=dict(type='array',items=dict(type='object',required=['path','line','priority','description'],additionalProperties=False,properties=dict(path=dict(type='string'),line=dict(type='integer'),priority=dict(type='string',enum=['P0','P1','P2','P3']),description=dict(type='string'))))))
(out/'input-binding.json').write_text(json.dumps(dict(chars=len(user),sha256=hashlib.sha256(user.encode()).hexdigest())),encoding='utf-8')
start=time.perf_counter()
try:
 raw=Agent(cfg.agent,out/'prompts').chat('You are an independent code reviewer. Return JSON findings.',user,tag='issue242_final_delta_review',response_schema=schema)
 (out/'review.json').write_text(raw,encoding='utf-8');print(raw,flush=True)
finally:(out/'elapsed.json').write_text(json.dumps(dict(wall_seconds=time.perf_counter()-start)),encoding='utf-8')
