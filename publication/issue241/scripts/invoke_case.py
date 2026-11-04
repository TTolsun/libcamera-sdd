"""Capture command wall time separately from existing generation-run accounting."""
from pathlib import Path
import hashlib,json,os,subprocess,sys,time
root=Path.cwd(); work=root/'build/issue241/public-case-02'
name,action=sys.argv[1:3]
if action=='generate':
    command=[sys.executable,'-m','sdd.cli','--config',str(work/'sdd.yaml'),'generate','--sections','camera-requests']
elif action=='translate':
    command=[sys.executable,'-c','from sdd.localization_cli import main; main()','--config',str(work/'sdd.yaml'),'--out',str(work/'english.json'),'--translate']
elif action=='audit':
    command=[sys.executable,'-m','sdd.cli','--config',str(work/'sdd.yaml'),'audit-consistency']
elif action=='export':
    command=[sys.executable,'-m','sdd.cli','--config',str(work/'sdd.yaml'),'export-site','--out',str(work/'site')]
elif action=='diagram-review':
    command=[sys.executable,str(root/'build/issue241/review_diagram.py')]
elif action=='plan':
    command=[sys.executable,'-c','import sys; from pathlib import Path; from sdd.config import load; from sdd.facts.model import KnowledgeModel; from sdd.publication_plan import prepare; cfg=load(Path(sys.argv[1])); prepare(cfg, KnowledgeModel.load(cfg.facts_path))',str(work/'sdd.yaml')]
elif action=='verify-site':
    command=[sys.executable,'-m','sdd.cli','--config',str(work/'sdd.yaml'),'verify-site','--out',str(work/'site')]
else:
    raise ValueError(action)
folder=work/'invocations';folder.mkdir(exist_ok=True)
path=folder/(name+'.json');log=folder/(name+'.log')
if path.exists() or log.exists():raise ValueError('Preserve the old invocation; use a new name')
record=dict(command=command,cwd=str(root),started_at=time.time(),status='running',generator_commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip())
record['inputs']={n:hashlib.sha256((work/n).read_bytes()).hexdigest() for n in
                  ('sdd.yaml','sections.yaml','scenarios.yaml','operation.json','visuals.yaml','contracts.yaml')}
path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
started=time.monotonic()
with log.open('wb') as stream:
    code=subprocess.run(command,stdout=stream,stderr=subprocess.STDOUT,env={**os.environ,'PYTHONPATH':str(root/'src'),'PYTHONDONTWRITEBYTECODE':'1','PYTHONIOENCODING':'utf-8'}).returncode
record.update(status='completed' if code==0 else 'failed',exit_code=code,finished_at=time.time(),wall_seconds=time.monotonic()-started)
path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,ensure_ascii=False))
print(log.read_text(encoding='utf-8',errors='replace')[-8000:])
raise SystemExit(code)
