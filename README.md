# libcamera SDD

Public source-bound design documents and generator validation evidence.

- [Public site](https://ttolsun.github.io/libcamera-sdd/)
- [Issue214 release evidence](publication/issue214/README.md)
- [Seven automatic findings: source review and minimal correction](publication/issue214-unresolved/README.md)
- [Original official cam reader/runtime evidence](publication/issue211-reader/README.md)

Configured source analysis and official upstream mirror:be7e83e91348250c015aad6d6f59f1468555bae8. The configured build was extracted again across 294 translation units, with no parsing errors. LC-compliance test-tool units were excluded; the resulting class inventory is 1,403 rather than the previous 1,412. Original virtual CPU trials remain at 293d751a814e0d4c34e85ad457ccd9d5eefd1a61 and were not rerun. Automatic checks remain separate from human approval and hardware/internal HAL validation.

- [Request submission diagnosis evidence](publication/submission-diagnosis/README.md)
- [Issue242: receipt-linked reuse decisions, native CLI sample and publication verification](publication/issue242/README.md)
- [Issue241: preserved publication contract, bilingual addBuffer validation and actual execution evidence](publication/issue241/README.md)
- [Issue243: causal repair, native evidence and publication checkpoint](publication/issue243/README.md)

- [Reader task and resumption study — human evaluation pending](publication/issue248/README.md)

공통 근거에서 작업·의사결정을 찾는 공개 사례와 대리 평가·사람 평가의 경계는 [#250 검증 기록](publication/issue250/README.md)에 있습니다.

- [Issue242 follow-up: verified source defaults and defined probe terms](publication/review-followup-242/README.md)
- [Conditional completion, ownership and reuse decisions — representative automatic evaluation](publication/issue249/README.md)
