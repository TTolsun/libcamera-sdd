# Checking the first libcamera frame · Whole document

1 pages

- **Analyzed source commit**: `adfa719f8ed67d18fd8a0739fc088a1f8b9e7252`
- **Source site**: [https://ttolsun.github.io/libcamera-sdd/validation/first-capture/en/](https://ttolsun.github.io/libcamera-sdd/validation/first-capture/en/)

This file combines every page of the site into one copy. Code and documents changed after it was made are not included, so check the analyzed source commit. Automated checks such as citation checks are not human review approval. Each page ends with its generation and review record.

## Contents

1. For Vendor

   1. [Checking the virtual camera's first frame](#doc-1)

<a id="doc-1"></a>

For Vendor

# Checking the virtual camera's first frame

Before human reviewCitation check not recordedAuthorship: Method not recorded[Status description ↓](#d1-page-evidence)

English translation · human review pending. Review states below refer to the Korean source.

Capture the first frame from `Virtual2` in a Linux shell. If it stops, find the last step that passed and where to check next in `$OUT/serial.log`. This test covers the libcamera virtual pipeline and does not validate a physical camera or the in-house Camera HAL.

## Environment setup

The record is current as of 2026-11-21 KST. The observed host was Ubuntu 26.04 LTS x86_64 on WSL2 on Windows 11 Home build 26300. The tests used QEMU 10.2.1 TCG and GDB, publicly available tools extracted separately. The full process of installing from scratch using the public packages below was not verified.

1. Use the Ubuntu system Python that matches the distribution's GDB and install the standard packages.

```
sudo apt update
sudo apt install build-essential git meson ninja-build pkg-config python3 python3-yaml python3-jinja2 python3-ply libyaml-dev libgnutls28-dev libudev-dev libevent-dev libdrm-dev libyuv-dev openssl qemu-system-x86 seabios busybox-static cpio gdb bc bison flex libelf-dev libssl-dev dwarves
```

1. Specify absolute paths without spaces. `$GENERATOR` is this repository, which has already been cloned, and the rest are paths that do not yet exist. The runner creates `$OUT` itself.

```
export GENERATOR=/absolute/path/to/camera-hal-sdd-generator
export LIBCAMERA=/absolute/path/to/new-libcamera
export KERNEL=/absolute/path/to/new-kernel
export BUILD=/absolute/path/to/new-build
export OUT=/absolute/path/to/new-output
```

1. Pin the official libcamera source and create a debug build.

```
git clone https://gitlab.freedesktop.org/camera/libcamera.git "$LIBCAMERA"
git -C "$LIBCAMERA" checkout --detach adfa719f8ed67d18fd8a0739fc088a1f8b9e7252
meson setup "$BUILD" "$LIBCAMERA" --buildtype=debug -Dpipelines=virtual '-Dipas=[]' -Dcam=enabled -Dqcam=disabled -Dtest=false -Ddocumentation=disabled -Dgstreamer=disabled -Dpycamera=disabled -Dv4l2=disabled -Dlc-compliance=disabled
ninja -C "$BUILD" -j6
```

1. Pin the kernel and build with [Archived test.config](https://github.com/TTolsun/camera-hal-sdd-generator/blob/main/examples/libcamera/validation/issue211/runs/20261031-kernel-config/test.config).

```
git clone https://github.com/microsoft/WSL2-Linux-Kernel "$KERNEL"
git -C "$KERNEL" checkout --detach linux-msft-wsl-6.18.33.2
test "$(git -C "$KERNEL" rev-parse HEAD)" = c21a03b2943d147c280bdf32530d4fe6badfd6bd
cp "$GENERATOR/examples/libcamera/validation/issue211/runs/20261031-kernel-config/test.config" "$KERNEL/.config"
make -C "$KERNEL" olddefconfig
make -C "$KERNEL" -j6 bzImage
```

## Run the first frame

1. Run [Runner](https://github.com/TTolsun/camera-hal-sdd-generator/blob/main/examples/libcamera/runtime/run_first_capture_vm.sh) as a regular user.

```
bash "$GENERATOR/examples/libcamera/runtime/run_first_capture_vm.sh" "$KERNEL/arch/x86/boot/bzImage" "$LIBCAMERA" "$BUILD" "$OUT"
```

1. Read `$OUT/serial.log`. The runner first saves frames to a file without instrumentation, then observes request return values and callbacks with GDB during a separate second capture. Check the file and exit code from the first run, and the callbacks and buffer status from the second run.

The guest is isolated, and root privileges are used only inside the guest. There is no NIC or hardware passthrough, and the host WSL settings are not changed. At the end, the runner hides only the guest's `/dev/udmabuf` to test for a missing allocator. In this case, camera configuration must succeed, but buffer allocation must fail.

## Find the first failure

Check in order and stop at the first failed row. Compare the observed value with that row, then move to the next check.

| Verification steps | Observed success | Where to check if it fails |
| --- | --- | --- |
| Device enumeration | `Virtual2` appears in `Available cameras:`. | Check `cam --list`, the virtual pipeline, and provider errors. |
| Settings | `configuring streams: (0) 400x300-NV12/SMPTE170M` is displayed. | Checks the request format, [Configuration diagnostics](https://ttolsun.github.io/libcamera-sdd/request-diagnosis.html#구성-실패를-좁히는-순서), and [Capture start code](https://gitlab.freedesktop.org/camera/libcamera/-/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/apps/cam/camera_session.cpp#L365). |
| Allocation | Reaching the submission breakpoint for the first request means that buffer allocation, which runs before it, succeeded. | Check `Could not open any dma-buf provider`, `Can't allocate buffers`, the guest's access permissions for `/dev/udmabuf`, and the kernel configuration. If the configuration uses a DMA-BUF heap, also check `/dev/dma_heap`. Check [Allocator code](https://gitlab.freedesktop.org/camera/libcamera/-/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/dma_buf_allocator.cpp#L119). |
| Submit request | The first call observed by GDB returns `0`. | The return value of [queueRequest](https://gitlab.freedesktop.org/camera/libcamera/-/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/apps/cam/camera_session.cpp#L453) and the capture limit branch are checked. |
| Callback | `RequestComplete` appears in `CALLBACK`. | Check the delivery and completion of the same request in [requestComplete](https://gitlab.freedesktop.org/camera/libcamera/-/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/apps/cam/camera_session.cpp#L467) and [Completion notification diagnostics](https://ttolsun.github.io/libcamera-sdd/request-diagnosis.html#실패-위치별-확인-순서). |
| Valid frame | The `FRAME` for the same request pointer shows sequence `0` and `FrameSuccess`. In the frame output from the same run, the two planes are `120000/60000` bytes. | Check the buffer status and the bytes used in each plane in [Completion handling](https://gitlab.freedesktop.org/camera/libcamera/-/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/apps/cam/camera_session.cpp#L479). |

In the second capture of [Measured VM logs](https://github.com/TTolsun/camera-hal-sdd-generator/blob/main/examples/libcamera/runtime/issue337-vm.log), the request pointers at the `queueRequest` breakpoint and in `CALLBACK` and `FRAME` match. The submission return value, completion notification, and buffer status are checked separately.

```
Value returned is $1 = 0
CALLBACK request=0x5555556790d0 status=libcamera::Request::RequestComplete
FRAME request=0x5555556790d0 sequence=0 status=libcamera::FrameMetadata::FrameSuccess
cam0-stream0 seq: 000000 bytesused: 120000/60000
```

The first capture's exit code was `0`, and `/tmp/frame.bin` was 180,000 bytes. In the missing-allocator test, allocator warnings appeared during enumeration, but `Virtual2` appeared in the list and execution proceeded through stream configuration. The first failure was buffer allocation.

```
Can't allocate buffers
Failed to start camera session
negative_capture_exit=1
TRIAL_FINISHED
```

## Execution evidence

[Current default WSL execution log](https://github.com/TTolsun/camera-hal-sdd-generator/blob/main/examples/libcamera/runtime/issue337-wsl-baseline.log) shows that `CONFIG_UDMABUF` and `CONFIG_DMABUF_HEAPS` are disabled in the default kernel and that both provider paths are absent. The test kernel required by the linked earlier run instructions in the published #211 was also absent from the host running at the time. Separately from those missing prerequisites, a time-limited WSL diagnostic command was run, and device discovery and stream configuration succeeded. The first failure was buffer allocation, and the capture exit code was `1`. This log records a run using a different libcamera commit, `293d751a814e0d4c34e85ad457ccd9d5eefd1a61`.

The #211 record from 2026-10-31 is a past observation of a successful 3×3 test with a modified WSL boot. After checking three runs of three frames each on the test kernel, the default kernel was restored.

[VM measurement log](https://github.com/TTolsun/camera-hal-sdd-generator/blob/main/examples/libcamera/runtime/issue337-vm.log) records the SHA-256 of the kernel image used. It does not guarantee that a rebuilt image will be bit-for-bit identical. Next, check [OFFICIAL_CAM.md](https://github.com/TTolsun/camera-hal-sdd-generator/blob/main/examples/libcamera/runtime/OFFICIAL_CAM.md).

## <a id="d1-page-evidence"></a>Document generation and review information

- **Generation method**: Generation method not recorded
- **Verification scope**: The existing manuscript did not record how it was generated. It will be displayed when regenerated.
- **Citation check**: Not recorded (`unrecorded`). Only the presence of the cited code locations in the analysis results was checked. A person checks whether the description is correct.
- **Human review**: Before human review
- **Commit used for analysis**: `adfa719f8ed67d18fd8a0739fc088a1f8b9e7252`

[Original Markdown ↗](https://ttolsun.github.io/libcamera-sdd/validation/first-capture/index.md)
