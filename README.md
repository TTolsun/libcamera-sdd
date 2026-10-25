# libcamera 설계 문서 검증

[Vendor 연동 가이드](https://ttolsun.github.io/libcamera-sdd/vendor-integration.html)와 [지원 범위와 검증](https://ttolsun.github.io/libcamera-sdd/vendor-assurance.html)을 실제 로컬 Qwen 응답으로 갱신했습니다. 원고의 47개 답변을 HTTP 원응답과 대조했고, 작성 세션에서 근거의 주체·조건·의무·반환·순서를 검토했습니다. 사람 승인과 사내 HAL·실기기 검증은 남아 있습니다.

[질문·근거·프롬프트 개선과 시험 증빙](qwen-vendor-guides/README.md), [배포 기록](run.json), [산출물 해시](docs/site-manifest.json)를 확인하세요. 공식 source는 `2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f`, 생성기는 `ae349a2b0fcda9cde3036a7ff2059539bc3a03bf`입니다. upstream 변경이 없어 300 TU·클래스 1,513개의 기존 전체 빌드 facts를 재사용하고 공개 근거를 다시 수집했습니다. 새 정기 예약은 설치하지 않았습니다.

PR #84의 [Vendor 제품 개요](https://ttolsun.github.io/libcamera-sdd/vendor-overview.html)와 [Developer 시스템 개요](https://ttolsun.github.io/libcamera-sdd/overview.html), 요청 한도 32 → 16 → 32의 [실제 소스 변경 시험](qwen-overviews/README.md)을 포함한 나머지 원고 17편을 그대로 보존했습니다. [이전 EGL 시험](qwen-replay/README.md)과 [이전 차단 중심 평가](vendor-llm-retest/README.md)도 당시 기록으로 유지합니다.

한영 42페이지의 링크 검사와 반복 빌드 138개 파일 일치를 확인했습니다. [영어판](https://ttolsun.github.io/libcamera-sdd/en/vendor-integration.html)의 새 문장도 Qwen으로 번역했습니다. 원문·번역은 사람 검토 전이며 코드 근거를 성능·지원·양산 보장으로 확대하지 않습니다.

`upstream/master`는 공식 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. HTML은 생성기에서 만들며 공개 libcamera 입력만 게시합니다. `generation-receipts.json`의 갱신한 두 Vendor 항목은 이번 HTTP 증빙에 연결되고, 다른 항목은 각 당시 배포 기록입니다. 최종 실행 방식은 verified-http-replay-and-live-repair입니다. 원응답 55회를 재사용하고 실제 HTTP 1회를 새로 호출한 보완 실행이며, 전체 신규 생성 시험과 구분합니다.
