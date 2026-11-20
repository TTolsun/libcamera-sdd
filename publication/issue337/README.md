# First public Virtual2 frame

This validation site accompanies [generator issue #337](https://github.com/TTolsun/camera-hal-sdd-generator/issues/337). It is generated from the runtime guide and focused facts for the synchronized official libcamera commit `adfa719f8ed67d18fd8a0739fc088a1f8b9e7252`. The virtual capture and the allocator-missing path both ran in the same isolated QEMU guest. The default WSL run and the historical #211 WSL run are recorded separately in the [source guide and raw logs](https://github.com/TTolsun/camera-hal-sdd-generator/pull/341).

- [한국어](https://ttolsun.github.io/libcamera-sdd/validation/first-capture/#first-frame)
- [English](https://ttolsun.github.io/libcamera-sdd/validation/first-capture/en/#first-frame)
- Validation build `1e76b148438bc76f2c720e25fe182e65e567c21b852ef59de754e4a1c174504a` contains 13 outputs. Both repeated exports produced the same manifest. The four HTML pages passed internal link validation.
- The entry baseline was the main site's Pages build `d1069be92ef26b1085c3dad1dfebc3b9721325d5b78f57e9eb9cf258d82d7ca0` at source `da6a6ed33ed0ab305f10b6f8b44736150d39cef4`. This focused validation has a dedicated manifest. Human review remains pending.
