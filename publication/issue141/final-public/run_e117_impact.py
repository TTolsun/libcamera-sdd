"""Independent deterministic upstream impact; never generation or human acceptance."""
import copy
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from sdd.config import load
from sdd.trial_workspace import clone_config, write_snapshot

root = Path.cwd()
w = root/'build/issue141'
out = w/(sys.argv[1] if len(sys.argv)>1 else 'e117-impact-main160')
assert out.resolve().parent == w.resolve()
assert not out.exists(), 'Preserve prior runs; use a fresh isolated output'
merged = 'a40341568df71c77d780a047f7d56cbcf07c8993'
base, head = '2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f', 'e117198c015057761bb0bbaa85f963c41ce412d7'
subprocess.run(['git', 'diff', '--quiet', merged, 'HEAD', '--', 'src/sdd'], check=True)
example = load(root/'examples/libcamera/sdd.yaml')
selected = load(root/'sdd.yaml').agent
assert selected.kind == 'cli' and selected.runner == 'codex' and selected.model == 'gpt-6.1-terra'
assert selected.args == ['-c', 'model_reasoning_effort="high"']
assert not example.review.triage_options().get('enabled', False)
out.mkdir()
cfg = clone_config(example, out)
cfg.agent = copy.deepcopy(selected)
cfg.source_root = (w/'current-e117/source').resolve()
cfg.compile_commands = (w/'current-e117/compile_commands.json').resolve()
cfg.facts_dir = (w/'current-e117/facts').resolve()
cfg.build_dir.mkdir(parents=True)
snapshot = write_snapshot(cfg, out/'sdd.codex.yaml')
restored = load(snapshot)
assert not restored.review.triage_options().get('enabled', False)
facts_before = cfg.facts_path.read_bytes()
assert json.loads(facts_before)['meta']['source_commit'] == head
base_facts = w/'public-sdd/qwen-full/publication/facts.json'
assert json.loads(base_facts.read_bytes())['meta']['source_commit'] == base
command = [sys.executable, '-X', 'utf8', '-m', 'sdd.cli', '--config', str(snapshot),
           'impact', '--base', base, '--head', head, '--base-facts', str(base_facts),
           '--fail-on-coverage-gap']
process = subprocess.run(command, capture_output=True,
    env={**os.environ, 'PYTHONUTF8':'1', 'PYTHONIOENCODING':'utf-8'})
(out/'stdout.log').write_bytes(process.stdout)
(out/'stderr.log').write_bytes(process.stderr)
assert cfg.facts_path.read_bytes() == facts_before
data = dict(checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    command=command, native_exit_code=process.returncode, merged_runtime_code=merged,
    observed_worktree_head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
    source_code_identical_to_merged_main=True, base_source=base, current_source=head,
    current_facts_sha256=hashlib.sha256(facts_before).hexdigest(),
    base_facts_sha256=hashlib.sha256(base_facts.read_bytes()).hexdigest(), facts_unchanged=True,
    coverage_triage_enabled=False, new_model_calls=0, human_acceptances_recorded=0,
    scope='Actual generator impact CLI on independent e117 facts and merged source code; not native Codex execution, manuscript generation, final publisher input equivalence, coverage approval or deployment')
report_file = cfg.build_dir/'impact.json'
(out/'execution.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
if report_file.exists():
    report = json.loads(report_file.read_bytes())
    assert set(report) == {'base','head','changed_files','changed_classes','sections','scenarios','packages','coverage'}
    assert report['base'] == base and report['head'] == head
    data.update(schema_contract=1, explicit_schema_version_field=False,
        report_sha256=hashlib.sha256(report_file.read_bytes()).hexdigest(),
        changed_files=len(report['changed_files']), sections=sorted(report['sections']),
        coverage_status=report['coverage']['status'], coverage_findings=len(report['coverage']['findings']),
        coverage_gate_passed=process.returncode == 0)
assert not (cfg.sdd_dir/'approvals.json').exists()
assert not list(out.rglob('*.receipt.json'))
(out/'execution.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(process.stdout.decode('utf-8'))
print(json.dumps(data,ensure_ascii=False,indent=2))
if process.returncode not in (0,2):
    print(process.stderr.decode('utf-8'))
    raise SystemExit(process.returncode)
