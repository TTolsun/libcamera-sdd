"""One isolated native build/extract of official e117; no LLM invocation."""
from pathlib import Path
import datetime
import hashlib
import importlib.metadata
import json
import os
import platform
import shutil
import subprocess
import sys

base = Path('/home/baboess/.cache/sdd-141-6b6c')
source = base / 'libcamera-e117'
generator = base / 'generator-5474ac7'
run_dir = base / 'run-e117-141'
host = Path(__file__).resolve().parent
build = source / 'build/full-coverage-141'
source_sha = 'e117198c015057761bb0bbaa85f963c41ce412d7'
generator_sha = '5474ac75c282517a4d10666d8f5b887911bdc029'

def output(args, cwd=None):
    return subprocess.check_output(args, cwd=cwd, text=True).strip()

assert output(['git', 'rev-parse', 'HEAD'], source) == source_sha
assert output(['git', 'rev-parse', 'HEAD'], generator) == generator_sha
assert output(['git', 'rev-parse', '--is-shallow-repository'], source) == 'false'
assert not run_dir.exists() or (
    '--retry-empty-startup' in sys.argv and not any(run_dir.iterdir())
), 'Inspect the existing run before any explicit retry'
run_dir.mkdir(exist_ok=True)
metadata = dict(started_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                generator_commit=generator_sha, source_commit=source_sha,
                source_describe=output(['git', 'describe', '--tags', '--always'], source),
                source_tree=output(['git', 'rev-parse', 'HEAD^{tree}'], source),
                python=platform.python_version(),
                libclang=importlib.metadata.version('libclang'),
                meson=output(['meson', '--version']), ninja=output(['ninja', '--version']),
                model_calls=0, status='running', commands=[])

def save():
    (host / 'execution.json').write_text(json.dumps(metadata, indent=2) + '\n')

def command(args, label, cwd=None):
    metadata['phase'] = label
    save()
    with (host / (label + '.log')).open('wb') as log:
        result = subprocess.run([str(a) for a in args], cwd=cwd, stdout=log,
                                stderr=subprocess.STDOUT)
    metadata['commands'].append(dict(phase=label, command=[str(a) for a in args],
                                     native_exit=result.returncode))
    save()
    result.check_returncode()
    print(label + ': exit0', flush=True)

try:
    command(['meson', 'setup', build, source, '-Dpipelines=all',
             '-Dipas=ipu3,mali-c55,rkisp1,rpi/pisp,rpi/vc4,softisp,vimc',
             '-Dcam=enabled', '-Dqcam=disabled', '-Dandroid=disabled', '-Dtest=false',
             '-Dgstreamer=enabled', '-Dlc-compliance=enabled', '-Dv4l2=enabled'], 'setup')
    options = output(['meson', 'introspect', build, '--buildoptions'])
    (host / 'meson-buildoptions.json').write_text(options + '\n')
    command(['ninja', '-C', build, '-j', '4'], 'compile')
    command([sys.executable, generator / 'examples/libcamera/prepare_compdb.py',
             '--build-dir', build, '--out', run_dir / 'compile_commands.json'], 'prepare-compdb')
    database = json.loads((run_dir / 'compile_commands.json').read_text())
    assert len(database) >= 300
    for row in database:
        row['arguments'].append('-Wno-c99-designator')
    (run_dir / 'compile_commands.json').write_text(json.dumps(database, indent=2) + '\n')
    shutil.copyfile(build / 'compile_commands.json', host / 'meson-compile_commands.json')
    shutil.copyfile(run_dir / 'compile_commands.json', host / 'compile_commands.json')

    sys.path.insert(0, str(generator / 'src'))
    from sdd.config import load
    from sdd.trial_workspace import clone_config, write_snapshot
    default = load(generator / 'examples/libcamera/sdd.yaml')
    assert default.agent.kind == 'cli' and default.agent.runner == 'hermes'
    assert default.agent.model == 'qwen3.5:9b-ctx64k'
    assert default.agent.args == ['--provider', 'custom', '--reasoning', 'high']
    cfg = clone_config(default, run_dir)
    cfg.source_root = source
    cfg.compile_commands = run_dir / 'compile_commands.json'
    config_path = run_dir / 'sdd.claude.yaml'
    write_snapshot(cfg, config_path)
    (run_dir / 'sdd.claude.local.yaml').write_text(
        'agent:\n  kind: cli\n  runner: claude\n  model: claude-haiku-5-5\n'
        '  args: [--effort, high]\n')
    actual = load(config_path)
    assert (actual.agent.kind, actual.agent.runner, actual.agent.model, actual.agent.args) == (
        'cli', 'claude', 'claude-haiku-5-5', ['--effort', 'high'])
    assert actual.exclude == ['subprojects/**', 'test/**', 'build/**']
    for name in ('sdd.claude.yaml', 'sdd.claude.local.yaml'):
        shutil.copyfile(run_dir / name, host / name)
    command([sys.executable, generator / 'tools/run_sdd.py', '--config', config_path,
             'extract'], 'extract', generator)
    shutil.copytree(run_dir / 'facts', host / 'facts')
    facts = json.loads((host / 'facts/facts.json').read_text())
    assert facts['meta']['source_commit'] == source_sha
    assert facts['meta']['translation_units'] == len(database)
    assert facts['meta']['comments']['errors'] == 0
    metadata.update(status='completed', translation_units=len(database),
                    classes=len(facts['classes']), functions=len(facts['functions']),
                    scenarios=len(facts['scenarios']),
                    source_exclude_loaded=actual.exclude,
                    selected_agent=dict(kind=actual.agent.kind, runner=actual.agent.runner,
                                        model=actual.agent.model, args=actual.agent.args),
                    facts_sha256=hashlib.sha256((host / 'facts/facts.json').read_bytes()).hexdigest(),
                    completed_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
    save()
    print(json.dumps(metadata), flush=True)
except Exception as exc:
    metadata.update(status='failed', error=repr(exc))
    save()
    raise
