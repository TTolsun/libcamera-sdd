"""Run the selected Hermes CLI with a fresh, hashed per-run provider profile."""
from pathlib import Path
import argparse,hashlib,json,os,runpy,sys
from unittest.mock import patch
from sdd import cli_agent
from sdd.cli import main

parser=argparse.ArgumentParser()
parser.add_argument('--hermes-home',type=Path,required=True)
parser.add_argument('--audit',type=Path,required=True)
parser.add_argument('--script',type=Path)
args,rest=parser.parse_known_args()
if rest[:1]==['--']: rest=rest[1:]
base=Path(__file__).resolve().parent
home=args.hermes_home.resolve(); audit=args.audit.resolve()
assert home.parent.name=='profiles' and home.is_relative_to(base) and audit.is_relative_to(base)
assert not audit.exists(), 'Audit must be a fresh file; existing inputs and evidence are never overwritten'
assert not audit.is_relative_to(home), 'Audit must be outside the private Hermes profile'
profile=home/'config.yaml'
profile_sha=hashlib.sha256(profile.read_bytes()).hexdigest()
original=cli_agent.run
rows=[]
def save(status):
 audit.parent.mkdir(parents=True,exist_ok=True)
 audit.write_text(json.dumps({'schema':1,'status':status,'hermes_profile_sha256':profile_sha,
  'hermes_profile':profile.relative_to(base).as_posix(),'parent_environment_unchanged':True,
  'scope':'Actual child CLI environment and unmodified transport prompt/output hashes; no model-weight attestation',
  'calls':rows},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def execute(argv,*,cwd,prompt,timeout,env=None):
 assert Path(argv[0]).name.lower() in {'hermes','hermes.exe'}
 child_env=dict(os.environ if env is None else env)
 child_env['HERMES_HOME']=str(home)
 assert hashlib.sha256(profile.read_bytes()).hexdigest()==profile_sha
 inference='chat' in argv
 if inference:
  assert argv.count('--model')==1 and argv[argv.index('--model')+1]=='qwen3.5:9b-ctx64k'
  assert argv.count('--reasoning')==1 and argv[argv.index('--reasoning')+1]=='high'
  assert argv.count('--provider')==1 and argv[argv.index('--provider')+1]=='custom'
 row={'argv':[Path(argv[0]).name,*argv[1:]],'profile_sha256':profile_sha,
      'prompt_sha256':hashlib.sha256(prompt.encode()).hexdigest(),'inference':inference,
      'child_hermes_home_matches_profile':True}
 try:
  result=original(argv,cwd=cwd,prompt=prompt,timeout=timeout,env=child_env)
 except Exception as exc:
  row.update(status='transport-failed',error_type=type(exc).__name__);rows.append(row);save('failed');raise
 row.update(status='completed',exit_code=result.returncode,
  stdout_sha256=hashlib.sha256(result.stdout.encode()).hexdigest(),
  stderr_sha256=hashlib.sha256(result.stderr.encode()).hexdigest())
 if hashlib.sha256(profile.read_bytes()).hexdigest()!=profile_sha:
  row['status']='profile-changed-after-transport'
  rows.append(row);save('failed')
  raise AssertionError('Hermes profile changed during the call; output was not adopted')
 rows.append(row);save('running')
 return result
save('started')
try:
 with patch('sdd.cli_agent.run',execute):
  if args.script:
   sys.argv=[str(args.script),*rest]
   runpy.run_path(str(args.script),run_name='__main__')
   code=0
  else: code=main(rest)
 save('completed' if code==0 else 'failed')
except BaseException:
 save('failed');raise
raise SystemExit(code)
