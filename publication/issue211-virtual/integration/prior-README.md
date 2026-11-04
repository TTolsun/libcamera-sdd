# Virtual principle update (issue211-virtual)

This update adds a virtual-principle section and a source-bound diagram to the public libcamera developer SDD. It is based on source inspection and documentation only.

- Korean: https://ttolsun.github.io/libcamera-sdd/official-cam-validation.html
- English: https://ttolsun.github.io/libcamera-sdd/en/official-cam-validation.html

## Changes
- The diagram covers Virtual2 lines-pattern generation, DMA-BUF buffers with queued requests, CPU NV12 writes, and completion connected to the cam callback.
- The cam processing name is now CameraSession::processRequest, distinct from VirtualCameraData::processRequest.
- The allocator conclusion, callback follow-up, and reproduction conditions are retained. The existing wording has changed, and the reproduction conditions are split into separate tasks.

## Pins
- Baseline manuscript, facts, and original runtime: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61.
- Upstream recorded separately: df8e348d64b4932a0676256ed24f0da3ee9438bc. The two are not identical because unchanged is false.
- The only changed path is meson.build, a libcamera v0.8.0 version declaration. The virtual pipeline and cam implementation are unchanged.
- No latest-SHA runtime or regeneration is claimed.

## Limits
- Automatic checks are not human approval.
- Hardware, sensor, ISP, physical DMA, product-app, and internal-HAL validation are not established.
- Final review and post-merge Pages and live hash proof will be recorded in the publication PR.
- No scheduling, app, global, or default-profile changes.
