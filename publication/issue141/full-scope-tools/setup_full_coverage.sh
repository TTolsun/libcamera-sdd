#!/bin/bash
set -euo pipefail
TASK_NATIVE_ROOT=/home/baboess/.cache/sdd-141-6b6c
TASK_SOURCE="$TASK_NATIVE_ROOT/libcamera"
TASK_BUILD="$TASK_SOURCE/build/full-coverage-141"
TASK_LOG="$TASK_NATIVE_ROOT/full-coverage-141-setup.log"
TASK_DEST=/mnt/c/Users/baboe/.codex/worktrees/6b6c/camera-hal-sdd-generator/build/issue141/full-coverage
test "$(git -C "$TASK_SOURCE" rev-parse HEAD)" = 182307a772ebebf173ee84911906da707718485f
git -C "$TASK_SOURCE" diff --quiet
test ! -e "$TASK_BUILD"
mkdir -p "$TASK_DEST"
trap 'cp "$TASK_LOG" "$TASK_DEST/setup.log"; tail -65 "$TASK_LOG"' EXIT
meson setup "$TASK_BUILD" "$TASK_SOURCE" \
  -Dpipelines=all \
  -Dipas=ipu3,mali-c55,rkisp1,rpi/pisp,rpi/vc4,softisp,vimc \
  -Dcam=enabled -Dqcam=disabled -Dtest=false -Ddocumentation=disabled \
  --wrap-mode=nofallback > "$TASK_LOG" 2>&1
