import shutil
import sys
from pathlib import Path
from sdd.config import load
from sdd.trial_workspace import clone_config, write_snapshot

root=Path.cwd();variant=sys.argv[1] if len(sys.argv)>1 else 'full-coverage';out=root/'build/issue141'/(sys.argv[2] if len(sys.argv)>2 else 'full-coverage-impact')
out.mkdir()
cfg=clone_config(load(root/'examples/libcamera/sdd.yaml'),out)
cfg.source_root=root/'build/issue141/libcamera-full'
cfg.facts_dir.mkdir()
shutil.copyfile(root/'build/issue141'/variant/'facts/facts.json',cfg.facts_path)
write_snapshot(cfg,out/'sdd.claude.yaml')
(out/'sdd.claude.local.yaml').write_text('agent:\n  kind: cli\n  runner: claude\n  model: claude-haiku-5-5\n  args: [--effort, high]\n',encoding='utf-8')
actual=load(out/'sdd.claude.yaml')
assert not actual.review.triage_options().get('enabled')
print('Prepared source-only impact with actual selected CLI profile; optional LLM triage disabled by existing default; no acceptance ledger')
