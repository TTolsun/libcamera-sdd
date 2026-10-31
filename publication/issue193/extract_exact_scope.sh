#!/usr/bin/env bash
set -euo pipefail
export PYTHONPATH=/home/baboess/.cache/camera-hal-sdd-issue193-293/generator/src
export PYTHONUNBUFFERED=1
ulimit -v 12582912
/home/baboess/.cache/camera-hal-sdd-issue193-293/runtime/bin/python /mnt/c/Users/baboe/.codex/worktrees/ba65/camera-hal-sdd-generator/build/issue193/extract_exact_scope.py
