# libcamera SDD

- [공개 시작 화면](https://ttolsun.github.io/libcamera-sdd/) · [English](https://ttolsun.github.io/libcamera-sdd/en/) · [장치 검증과 취소 코드 경로](publication/issue347-reader-entries/README.md)

- [실제 UVC 장치에서 요청을 대조하는 절차](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#실제-uvc-장치에서-같은-요청의-완료-기록을-대조하는-절차) · [English field procedure](https://ttolsun.github.io/libcamera-sdd/en/request-lifecycle.html#실제-uvc-장치에서-같은-요청의-완료-기록을-대조하는-절차) · [검증 기록](publication/uvc-device-request-observation/README.md)

- [연결 해제와 요청 완료 상태](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#연결-해제와-요청-완료-상태) · [English](https://ttolsun.github.io/libcamera-sdd/en/request-lifecycle.html#연결-해제와-요청-완료-상태) · [Publication evidence](publication/disconnect-completion-state/README.md)

- [UVC 정지 중 특정 버퍼가 돌아오지 않을 때](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#uvc-정지-중-버퍼-하나가-돌아오지-않을-때) · [English](https://ttolsun.github.io/libcamera-sdd/en/request-lifecycle.html#uvc-정지-중-버퍼-하나가-돌아오지-않을-때) · [Publication evidence](publication/uvc-stop-diagnosis/README.md)

- [#323 excerpt and figure-note labels: render-time label replacement, contract audit and figure-review carryover](publication/issue323-labels/README.md)
- [Supplied-fence condition and pretranslation/pre-merge validation evidence](publication/publication-preflight/README.md)

Public source-bound design documents and generator validation evidence.

- [Public site](https://ttolsun.github.io/libcamera-sdd/)
- [Upstream ColourTemperature supplement and first-run evidence](publication/issue304/README.md)
- [Issue214 release evidence](publication/issue214/README.md)
- [Seven automatic findings: source review and minimal correction](publication/issue214-unresolved/README.md)
- [Original official cam reader/runtime evidence](publication/issue211-reader/README.md)

The earlier contract review used analysis source `be7e83e91348250c015aad6d6f59f1468555bae8` and upstream mirror `c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78`. The four source files for this contract review are byte-identical across those commits. The configured build was extracted again across 294 translation units, with no parsing errors. LC-compliance test-tool units were excluded; the resulting class inventory is 1,403 rather than the previous 1,412. Original virtual CPU trials remain at 293d751a814e0d4c34e85ad457ccd9d5eefd1a61 and were not rerun. Automatic checks remain separate from human approval and hardware/internal HAL validation.

- [Request submission diagnosis evidence](publication/submission-diagnosis/README.md)
- [Issue242: receipt-linked reuse decisions, native CLI sample and publication verification](publication/issue242/README.md)
- [Issue241: preserved publication contract, bilingual addBuffer validation and actual execution evidence](publication/issue241/README.md)
- [Issue243: causal repair, native evidence and publication checkpoint](publication/issue243/README.md)

- [Reader task and resumption study — human evaluation pending](publication/issue248/README.md)

- [요청을 보내고 완료 알림을 받기까지](https://ttolsun.github.io/libcamera-sdd/validation/reader-first-prose/capture.html) · 미리보기와 저장 버퍼가 함께 있는 촬영 요청을 세 문단으로 설명합니다.

공통 근거에서 작업·의사결정을 찾는 공개 사례와 대리 평가·사람 평가의 경계는 [#250 검증 기록](publication/issue250/README.md)에 있습니다.

- [Issue242 follow-up: verified source defaults and defined probe terms](publication/review-followup-242/README.md)
- [Conditional completion, ownership and reuse decisions — representative automatic evaluation](publication/issue249/README.md)

- [Issue243 followup: parameter association and access-default evidence](publication/issue243-followup/README.md)

- [Issue250 follow-up: conditions, direct navigation and ordered search — agent proxy evaluation; human evaluation unverified](publication/issue250-followup/README.md)

- [Public request contract corrections and verification](publication/contract-ambiguities/README.md)
