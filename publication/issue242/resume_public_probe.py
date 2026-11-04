import hashlib,json,time
from pathlib import Path
from sdd.config import load
from sdd.facts.model import KnowledgeModel
from sdd.generate import Generator
from sdd.export_site import export_site
from sdd.site_build import verify_site
from sdd.llm import Agent

root=Path.cwd();out=root/'build/issue242-publication/actual-probe-02'
cfg=load(out/'sdd.yaml');model=KnowledgeModel.load(cfg.facts_path)
before=set((cfg.build_dir/'generation-runs').glob('*.json'))
archives={p:hashlib.sha256(p.read_bytes()).hexdigest() for parent in ('calls','cli')
          for p in (cfg.build_dir/'prompts'/parent).rglob('*') if p.is_file()}
start=time.perf_counter()
Generator(cfg,model,Agent(cfg.agent,cfg.build_dir/'prompts')).run()
site=export_site(cfg)
runs=[json.loads(p.read_bytes()) for p in set((cfg.build_dir/'generation-runs').glob('*.json'))-before]
calls=[c for r in runs for c in r['calls']]
if calls:raise ValueError('Final candidate unexpectedly called the selected CLI')
if any(hashlib.sha256(p.read_bytes()).hexdigest()!=sha for p,sha in archives.items()):
    raise ValueError('Original CLI archive changed')
result=dict(status='passed',wall_seconds=time.perf_counter()-start,new_calls=0,
            quality=verify_site(site),original_files_preserved=len(archives),
            decisions=[d for r in runs for d in r.get('decisions',[])])
(out/'final-code-resume.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='decisions'},ensure_ascii=False))
