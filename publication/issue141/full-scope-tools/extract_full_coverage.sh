#!/bin/bash
set -euo pipefail
export TASK_NATIVE_ROOT=/home/baboess/.cache/sdd-141-6b6c
TASK_RUN="$TASK_NATIVE_ROOT/run-full-coverage-141"
TASK_BUILD="$TASK_NATIVE_ROOT/libcamera/build/full-coverage-141-deps"
TASK_LOG="$TASK_NATIVE_ROOT/full-coverage-141-extract.log"
TASK_DEST=/mnt/c/Users/baboe/.codex/worktrees/6b6c/camera-hal-sdd-generator/build/issue141/full-coverage
cd "$TASK_NATIVE_ROOT/generator"
git diff --quiet
test -z "$(git ls-files --others --exclude-standard)"
test ! -e "$TASK_RUN"
git fetch origin main
git checkout --detach origin/main
export UV_CACHE_DIR="$TASK_NATIVE_ROOT/cache"
"$TASK_NATIVE_ROOT/bootstrap/bin/uv" sync --frozen --extra dev --python /usr/bin/python3
mkdir "$TASK_RUN"
.venv/bin/python examples/libcamera/prepare_compdb.py --build-dir "$TASK_BUILD" --out "$TASK_RUN/compile_commands.json"
.venv/bin/python - <<'PY'
import hashlib,json,os,subprocess
from pathlib import Path
from sdd.config import load
from sdd.trial_workspace import clone_config,write_snapshot
r=Path(os.environ['TASK_NATIVE_ROOT']);out=r/'run-full-coverage-141'
cfg=clone_config(load(Path('examples/libcamera/sdd.yaml')),out)
cfg.source_root=r/'libcamera';cfg.compile_commands=out/'compile_commands.json'
assert cfg.exclude==['subprojects/**','test/**','build/**']
entries=json.loads(cfg.compile_commands.read_text())
for entry in entries:entry['arguments'].append('-Wno-c99-designator')
cfg.compile_commands.write_text(json.dumps(entries,ensure_ascii=False,indent=1)+'\n',encoding='utf-8')
write_snapshot(cfg,out/'sdd.claude.yaml')
(out/'sdd.claude.local.yaml').write_text('agent:\n  kind: cli\n  runner: claude\n  model: claude-haiku-5-5\n  args: [--effort, high]\n',encoding='utf-8')
actual=load(out/'sdd.claude.yaml')
assert (actual.agent.kind,actual.agent.runner,actual.agent.model,actual.agent.args)==('cli','claude','claude-haiku-5-5',['--effort','high'])
meta={'generator_commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'source_commit':subprocess.check_output(['git','-C',str(cfg.source_root),'rev-parse','HEAD'],text=True).strip(),'source_exclude_loaded_from_merged_YAML':actual.exclude,'compile_commands_sha256':hashlib.sha256(cfg.compile_commands.read_bytes()).hexdigest(),'normalized_TUs':len(entries),'compiler_diagnostic_normalization':'-Wno-c99-designator: GCC-accepted array designators, same normalization as earlier trial','model_calls':0,'selected_agent':{'kind':actual.agent.kind,'runner':actual.agent.runner,'model':actual.agent.model,'args':actual.agent.args},'build_scope':'all10 pipelines,all7 IPA modules,cam,lc-compliance,GStreamer,V4L2;no qcam/test/Android','subproject_libpisp_commit':subprocess.check_output(['git','-C',str(r/'libcamera/subprojects/libpisp'),'rev-parse','HEAD'],text=True).strip()}
(out/'execution.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8');print(json.dumps(meta),flush=True)
PY
trap 'cp "$TASK_LOG" "$TASK_DEST/extraction.log"; tail -40 "$TASK_LOG"' EXIT
PYTHONUNBUFFERED=1 .venv/bin/sdd --config "$TASK_RUN/sdd.claude.yaml" extract > "$TASK_LOG" 2>&1
mkdir -p "$TASK_DEST/facts"
cp "$TASK_RUN/facts/facts.json" "$TASK_DEST/facts/facts.json"
cp "$TASK_RUN/sdd.claude.yaml" "$TASK_DEST/sdd.claude.yaml"
cp "$TASK_RUN/sdd.claude.local.yaml" "$TASK_DEST/sdd.claude.local.yaml"
cp "$TASK_RUN/execution.json" "$TASK_DEST/execution.json"
cp "$TASK_RUN/compile_commands.json" "$TASK_DEST/compile_commands.json"
