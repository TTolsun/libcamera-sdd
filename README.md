# LLM 그림 자동화 검증

현재 생성기는 `4a47e73bedc0ec0970cd498fcbbbaeaad595524e`입니다. 질문별 그림과 긴 한영 레이블의 줄바꿈을 공통 생성기에서 구성합니다.

[지원 범위와 검증](https://ttolsun.github.io/libcamera-sdd/vendor-assurance.html)의 validate 반환 그림을 실제 Local Qwen으로 생성했습니다. 생성기가 소스 구절·조건·필수 심볼·한영 핵심 용어를 검사하고 설명 가까이에 배치합니다. 기존 문단 답변과 두 개요의 Qwen 생성 이력은 보존했습니다.

[그림·근거 검증](llm-visual-verification.json), [실제 libcamera HTTP 호출](llm-visuals/libcamera-call/), [반입 ZIP에서 실행한 두 커밋 재생성 시험](llm-visuals/import-replay/report.json)을 확인하세요. 생성기 변경은 [PR91](https://github.com/TTolsun/camera-hal-sdd-generator/pull/91), 사내 반입본은 [그림 자동화 릴리스](https://github.com/TTolsun/camera-hal-sdd-generator/releases/tag/inhouse-2026-10-25-visuals)에서 제공합니다.

공개 소스 시험이며 사내 HAL·사내 게이트웨이·실기기 검증이나 사람 승인이 아닙니다. 원문·번역·그림은 사람 검토 전입니다. 공개 정기 예약은 설치하지 않습니다.

## 두 개요의 이전 Qwen 검증

[Vendor 제품 개요](https://ttolsun.github.io/libcamera-sdd/vendor-overview.html)와 [Developer 시스템 개요](https://ttolsun.github.io/libcamera-sdd/overview.html)를 실제 로컬 Qwen으로 재생성했습니다. 별도 소스의 기본 요청 한도를 32 → 16 → 32로 바꾸고 운영용 `sdd update`가 두 문서를 갱신하는 경로도 실행했습니다. 공개 문서는 공식 소스의 값 32를 설명합니다.

[시험 기록과 검증 방법](qwen-overviews/README.md), [실제 요청·응답 및 단계별 증빙](qwen-overviews/proof.json), [배포 기록](run.json), [사이트 해시](docs/site-manifest.json)를 확인하세요. 생성기는 `e19a08ee565958033ad859e52050478744577789`이며 [변경 #84](https://github.com/TTolsun/camera-hal-sdd-generator/pull/84)에 구현과 검증 방법이 있습니다.

최신 Vendor 연동·지원 문서와 독자별 작업 메뉴는 보존했습니다. [영어판](https://ttolsun.github.io/libcamera-sdd/en/index.html)의 새 문장도 같은 로컬 Qwen으로 번역했습니다. 생성기 전체 회귀 828개와 최종 관련 검사 76개가 통과했고 1개는 건너뛰었습니다. 원문·번역은 사람 검토 전이며 사내 HAL·실기기는 검증하지 않았습니다.

이전 [EGL 자동 갱신 시험](qwen-replay/README.md)과 [Vendor 모델 평가](vendor-llm-retest/README.md)는 당시 기록으로 보존합니다. 기존 `generation-receipts.json`도 이전 배포의 응답 기록이며, 이번 두 개요의 출처는 `qwen-overviews/proof.json`입니다.

`upstream/master`는 공식 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 정기 예약은 설치하지 않습니다. HTML은 생성기에서 만들며 공개 libcamera 입력만 게시합니다.
