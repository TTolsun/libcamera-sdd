from pathlib import Path
import json,yaml,subprocess,resource,shutil,hashlib
from sdd import compdb
from sdd.config import load
from sdd.extract import run
w=Path(__file__).resolve().parent
prior=Path('/mnt/c/Users/baboe/.codex/worktrees/d9d0/camera-hal-sdd-generator/build/issues-162-163/native-extraction-v2/sdd-linux.yaml')
old=yaml.safe_load(prior.read_text(encoding='utf-8'))
data=yaml.safe_load((w/'latest293/extraction-merged-linux.yaml').read_text(encoding='utf-8'))
data['source']['exclude']=old['source']['exclude']
profile=w/'latest293/extraction-exact-scope-linux.yaml'
profile.write_text(yaml.safe_dump(data,allow_unicode=True,sort_keys=False),encoding='utf-8')
cfg=load(profile)
trial=w/'latest293/trial-generated-headers-included';trial.mkdir(exist_ok=True)
if not (trial/'facts.json').exists():shutil.copyfile(cfg.facts_path,trial/'facts.json')
rows=compdb.normalize(compdb.load_entries(cfg.source_root/'build-followup/compile_commands.json'),compdb.clang_resource_dir('clang'))
assert len(rows)==300
cfg.compile_commands.write_text(json.dumps(rows,indent=1),encoding='utf-8')
print('source',subprocess.check_output(['git','rev-parse','HEAD'],cwd=cfg.source_root,text=True).strip(),flush=True)
print('actual prior exclusions',data['source']['exclude'],'TU count',len(rows),flush=True)
print('prior profile SHA256',hashlib.sha256(prior.read_bytes()).hexdigest(),flush=True)
print('task-only memory limit',resource.getrlimit(resource.RLIMIT_AS),flush=True)
m=run(cfg)
print('final extracted source',m.meta['source_commit'],'comments',m.meta['comments'],flush=True)
