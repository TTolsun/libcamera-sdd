#!/bin/bash
set -euo pipefail
TASK_NATIVE_ROOT=/home/baboess/.cache/sdd-141-6b6c
TASK_BUILD="$TASK_NATIVE_ROOT/libcamera/build/full-coverage-141-deps"
TASK_LOG="$TASK_NATIVE_ROOT/full-coverage-141-build.log"
TASK_DEST=/mnt/c/Users/baboe/.codex/worktrees/6b6c/camera-hal-sdd-generator/build/issue141/full-coverage
test -f "$TASK_BUILD/build.ninja"
trap 'cp "$TASK_LOG" "$TASK_DEST/build.log"; tail -40 "$TASK_LOG"' EXIT
ninja -C "$TASK_BUILD" -j4 > "$TASK_LOG" 2>&1
cp "$TASK_BUILD/compile_commands.json" "$TASK_DEST/meson-compile-commands.json"
cp "$TASK_BUILD/meson-info/intro-buildoptions.json" "$TASK_DEST/meson-buildoptions.json"
