# Camera state at completion after disconnect

The camera state sampled at disconnect and the state sampled by the completion guard are separate observations. The table follows the actual queued request through FIFO handoff and the guard. Device arrival, state at the guard, signal emission and application receipt remain distinct observation points.

[한국어](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#연결-해제와-요청-완료-상태) · [English](https://ttolsun.github.io/libcamera-sdd/en/request-lifecycle.html#연결-해제와-요청-완료-상태)

Static source reference at `da6a6ed33ed0ab305f10b6f8b44736150d39cef4`. See summary.json for scope and validation.
