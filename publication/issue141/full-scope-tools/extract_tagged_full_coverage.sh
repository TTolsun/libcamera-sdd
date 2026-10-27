#!/bin/bash
set -euo pipefail
export TASK_NATIVE_ROOT=/home/baboess/.cache/sdd-141-6b6c
TASK_SOURCE="$TASK_NATIVE_ROOT/libcamera"
TASK_BUILD="$TASK_SOURCE/build/full-coverage-141-deps"
TASK_RUN="$TASK_NATIVE_ROOT/run-full-coverage-tagged-141"
TASK_DEST=/mnt/c/Users/baboe/.codex/worktrees/6b6c/camera-hal-sdd-generator/build/issue141/full-coverage-tagged
test "$(git -C "$TASK_SOURCE" rev-parse HEAD)" = 182307a772ebebf173ee84911906da707718485f
test "$(git -C "$TASK_SOURCE" rev-parse --is-shallow-repository)" = false
git -C "$TASK_SOURCE" describe --tags --match 'v[0-9]*'
test ! -e "$TASK_RUN"
test ! -e "$TASK_DEST"
mkdir "$TASK_DEST"
meson setup --reconfigure "$TASK_BUILD" "$TASK_SOURCE" > "$TASK_DEST/reconfigure.log" 2>&1
ninja -C "$TASK_BUILD" -j4 > "$TASK_DEST/rebuild.log" 2>&1
cd "$TASK_NATIVE_ROOT/generator"
git diff --quiet
test "$(git rev-parse HEAD)" = 87ae42f448a5d825c026f2dec058cee0927feedf
mkdir "$TASK_RUN"
.venv/bin/python examples/libcamera/prepare_compdb.py --build-dir "$TASK_BUILD" --out "$TASK_RUN/compile_commands.json"
.venv/bin/python - <<'PY'
import hashlib,json,os,subprocess
from pathlib import Path
from sdd.config import load
from sdd.trial_workspace import clone_config,write_snapshot
r=Path(os.environ['TASK_NATIVE_ROOT']);out=r/'run-full-coverage-tagged-141'
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
meta={'generator_commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'source_commit':subprocess.check_output(['git','-C',str(cfg.source_root),'rev-parse','HEAD'],text=True).strip(),'source_describe':subprocess.check_output(['git','-C',str(cfg.source_root),'describe','--tags','--match','v[0-9]*'],text=True).strip(),'source_is_shallow':False,'source_exclude_loaded_from_merged_YAML':actual.exclude,'compile_commands_sha256':hashlib.sha256(cfg.compile_commands.read_bytes()).hexdigest(),'normalized_TUs':len(entries),'compiler_diagnostic_normalization':'-Wno-c99-designator: GCC-accepted array designators; same as original trial','model_calls':0,'selected_agent':{'kind':actual.agent.kind,'runner':actual.agent.runner,'model':actual.agent.model,'args':actual.agent.args},'build_scope':'all10 pipelines/all7 IPA modules/cam/lc-compliance/GStreamer/V4L2;no qcam/test/Android'}
(out/'execution.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8');print(json.dumps(meta),flush=True)
PY
PYTHONUNBUFFERED=1 .venv/bin/sdd --config "$TASK_RUN/sdd.claude.yaml" extract > "$TASK_DEST/extraction.log" 2>&1
mkdir "$TASK_DEST/facts"
cp "$TASK_RUN/facts/facts.json" "$TASK_DEST/facts/facts.json"
cp "$TASK_RUN/compile_commands.json" "$TASK_DEST/compile_commands.json"
cp "$TASK_RUN/sdd.claude.yaml" "$TASK_DEST/sdd.claude.yaml"
cp "$TASK_RUN/sdd.claude.local.yaml" "$TASK_DEST/sdd.claude.local.yaml"
cp "$TASK_RUN/execution.json" "$TASK_DEST/execution.json"
cp "$TASK_BUILD/compile_commands.json" "$TASK_DEST/meson-compile-commands.json"
cp "$TASK_BUILD/meson-info/intro-buildoptions.json" "$TASK_DEST/meson-buildoptions.json"
tail -12 "$TASK_DEST/extraction.log"
