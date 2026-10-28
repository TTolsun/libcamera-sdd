"""Frozen published PR51 comparison; never invoke a model or edit manuscripts."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import sys

root = Path.cwd()
base = root / 'build/issue141'
out = base / 'fixed-public-pr51'
published = base / 'current-public-8f936'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

if len(sys.argv) > 1:
    from sdd.config import load
    from sdd.export_site import export_site
    from sdd.site_build import verify_site
    from sdd.llm import Agent
    Agent.chat = lambda *a, **kw: (_ for _ in ()).throw(AssertionError('No model in frozen render'))
    cfg = load(out / 'sdd.yaml')
    result = verify_site(export_site(cfg, out / sys.argv[1]))
    (out / (sys.argv[1] + '-verification.json')).write_text(json.dumps(result) + '\n')
    print(json.dumps(result))
    raise SystemExit(0)

from sdd.config import load
from sdd.trial_workspace import clone_config, write_snapshot
assert not out.exists()
out.mkdir()
original = load(base / 'fixed-public-latest/sdd.yaml')
cfg = clone_config(original, out)
shutil.copytree(original.sdd_dir, cfg.sdd_dir)
cfg.facts_dir.mkdir()
shutil.copyfile(original.facts_path, cfg.facts_path)
for path in (published / 'publication/issue107-claude-part2/manuscripts').glob('*.md'):
    shutil.copyfile(path, cfg.sdd_dir / path.name)
catalog = out / 'english.json'
shutil.copyfile(published / 'publication/issue107-claude-part2/english.json', catalog)
cfg.raw['site']['english_catalog'] = str(catalog)
write_snapshot(cfg, out / 'sdd.yaml')
inputs = [cfg.facts_path, catalog, out / 'sdd.yaml', *sorted(cfg.sdd_dir.rglob('*'))]
before_inputs = {str(p.relative_to(out)): digest(p) for p in inputs if p.is_file()}
for mode, generator in [('before', base / 'baseline'), ('after', base / 'fault-render-generator')]:
    env = dict(os.environ, PYTHONPATH=str(generator / 'src'), PYTHONUTF8='1')
    with (out / (mode + '.log')).open('wb') as log:
        result = subprocess.run([sys.executable, __file__, mode], env=env,
                                stdout=log, stderr=subprocess.STDOUT)
    print(mode, 'native_exit', result.returncode, flush=True)
    result.check_returncode()
assert before_inputs == {str(p.relative_to(out)): digest(p) for p in inputs if p.is_file()}
before = json.loads((out / 'before/site-manifest.json').read_text())
after = json.loads((out / 'after/site-manifest.json').read_text())
actual = json.loads((published / 'docs/site-manifest.json').read_text())
assert before['inputs'] == after['inputs']
assert before['outputs'] == after['outputs']
assert after['outputs'] == actual['outputs']
report = dict(public_sha='8f936663f82f71c729baaf34f0259b6580edd6b7',
              source_commit='2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f',
              before_generator='45609e46c6d76806003e9dd75702a8b7ddab9e5e',
              after_generator='350a9d344e6170d37124774f5f290ec13bc04d0b',
              outputs=len(after['outputs']), inputs_unchanged=True,
              inputs_identical=True, before_after_bytes_identical=True,
              matches_current_public=True, model_calls=0,
              before_build_id=before['build_id'], after_build_id=after['build_id'],
              public_build_id=actual['build_id'],
              scope='Frozen old-source preservation including newly published3PR51manuscripts;not new upstream generation')
(out / 'comparison.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report))
