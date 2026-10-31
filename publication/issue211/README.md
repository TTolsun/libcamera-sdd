## Result

- Status: `observed-wsl-virtual-only`. Camera: Virtual2, applied configuration `(0) 400x300-NV12/SMPTE170M`.
- Trial kernel: `6.18.33.2-microsoft-standard-WSL2-issue211`.
- Three independent final processes (pids 434, 449, 464) each completed 3 frames (buffer sequences 0, 1, 2), made 4 udmabuf allocations, had zero observed cancelled callbacks, and exited with code 0.
- Observed TIDs: [434, 437], [449, 452], [464, 467]. These are the observed main-processing and callback roles in each process; other process threads may exist.

## Callback and processing threads

- Callback entry (`CameraSession::requestComplete`) ran on callback TIDs 437, 452, and 467.
- Frame processing (`CameraSession::processRequest`, immediately before `captureCount_++`, `camera_session.cpp:535`) ran on main TIDs 434, 449, and 464. At this measured processing point, it was not observed on the callback thread.
- Buffer metadata was read after `FrameMetadata` at `camera_session.cpp:503`.

## udmabuf lifecycle (CPU read/write, not hardware DMA)

1. Open `/dev/udmabuf`.
2. Allocate a 4096-byte dmabuf (backing_fd 4, dmabuf_fd 5).
3. `mmap`.
4. `sync-start` (flags 3).
5. CPU access: 4096 bytes, checksum 522240.
6. `sync-end` (flags 7).
7. `munmap`, then close dmabuf, backing, and provider. All return 0.

## Environment during the trial

- The default kernel `6.18.33.2-microsoft-standard-WSL2` is restored, and `.wslconfig` is absent after restore.
- Kernel tag `linux-msft-wsl-6.18.33.2` (commit `c21a03b2943d147c280bdf32530d4fe6badfd6bd`). The compiler and config diff is preserved in full: GCC 13.2 to Ubuntu GCC 15.2, binutils 2.41 to 2.46, pahole 1.25 to 1.31.
- Matching modules are not installed. Docker was stopped during the trial. The user authorized the kernel trial.
- `/dev/udmabuf` is root-only. Permissions are unchanged. The unprivileged run failed with errno 13.

## Limits

- GDB breakpoints affect timing. The run does not prove callback return or performance.
- No callback-return instruction was observed.
- The cancellation branch was not exercised dynamically. The observed count of 0 was not forced.
- Timeout probe (0.5 s) timed out with exit code 1. Cleanup returned 0 for `sync-end`, `munmap`, and all closes, and the process group was absent.
- Negative probes: absent provider errno 2, unsupported ioctl errno 25, exit code 1.
- Not validated: hardware DMA (`not-validated`), physical camera (`not-run`), production application (`not-run`), internal HAL (`not-run`). Human review is `pending`.

## Generation

- Writer and translation: native CLI `claude-haiku-5-5` with `--effort high --setting-sources project,local`.
- New-document review: a separate Codex run, `gpt-6.1-terra` with `-c 'model_reasoning_effort="high"'`.
- The historical issue193/PR69 selected-Claude contract audit keeps its actual historical identity. It is not relabeled as Terra.
- The renderer's original Codex visual identity is used for authentication only and invokes no model.
- PR69 latest corrected source-identical request documents are preserved.
- The official upstream is unchanged, so this is not a trivial rebuild. A new reader task closes the missing evidence for actual WSL allocator and callback behavior.

## Evidence and files

- Raw runs: https://github.com/TTolsun/camera-hal-sdd-generator/tree/main/examples/libcamera/validation/issue211/runs/20261031-wsl-cam-3
- Runbook: https://github.com/TTolsun/camera-hal-sdd-generator/blob/main/examples/libcamera/runtime/OFFICIAL_CAM.md
- Reproduction script: https://github.com/TTolsun/camera-hal-sdd-generator/blob/main/examples/libcamera/runtime/run_cam.py
- Source commit `293d751a814e0d4c34e85ad457ccd9d5eefd1a61` is tracked clean and unmodified.
- Package contents: `config/`, `manuscripts/`, `facts293.json.gz`, `english.json`, `profiles/`, `reviews/`, `build-validation.json`, `consistency-review.json`, `cli-evidence.zip`, `evidence-index.json`, `previous-release/`.
- Pending: the postmerge Pages check and live output-hash proof, to be recorded in issue211.
