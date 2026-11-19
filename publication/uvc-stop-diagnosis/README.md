# UVC stop diagnosis

Start at V4L2VideoDevice::streamOff() and look up the same submitted FrameBuffer in the same device’s queuedBuffers_. The Korean and English pages contain the decision diagram and its 16 source-linked observations and next checks.

- [UVC 정지 중 특정 버퍼가 돌아오지 않을 때](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#uvc-정지-중-버퍼-하나가-돌아오지-않을-때) · [English](https://ttolsun.github.io/libcamera-sdd/en/request-lifecycle.html#uvc-정지-중-버퍼-하나가-돌아오지-않을-때)

Source commit da6a6ed33ed0ab305f10b6f8b44736150d39cef4. Build 4c1167f54cb4ede87e935695f2b01105ec84aac889c5ff2894d441b614c85334. Static source analysis. Hardware execution and human review remain separate. The visual ledger and contract assessment record both new reviews and verified prior results.
