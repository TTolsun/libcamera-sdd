# libcamera 설계 문서 검증

[공개 문서](https://ttolsun.github.io/libcamera-sdd/)의 나머지 설명 문서 8편을 실제 로컬 Qwen으로 재생성했습니다. 요청 재사용, fence 소유권, 취소·완료·정지의 조건을 혼동한 설명은 근거와 질문을 나눠 Qwen으로 다시 생성했습니다. 기준 생성 → 소스 변경 → 복원 → 공식 커밋 이월을 모두 실행하고, 채택된 HTTP 응답 331개와 원고·인용을 대조했습니다. 변경·복원마다 16개 주제를 다시 생성하고 27개 주제를 재검증해 이월했습니다. 같은 커밋의 재실행에서는 추가 모델 호출이 없었습니다.

[재현 증빙과 검증기](qwen-documents/README.md), [배포 기록](run.json), [문장별 출처](generation-receipts.json)를 확인하세요. 프레임 수, 대기 시간, 셀 크기 제한, 오류 코드, 계수 개수와 프록시 선택 조건을 바꾸고 복원했습니다. 클래스·필드·호출 변경은 구조 문서에서도 확인했습니다. 변경·복원 소스 각각 실제 WSL 빌드와 300개 번역 단위 추출을 수행했으며 파싱 오류는 0개였습니다. 같은 커밋의 생성 재시도에서는 해시가 검증된 실제 추출 결과를 재사용했습니다.

공개 원고는 공식 upstream `2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f` 기준입니다. 시험용 소스 변경은 배포하지 않았습니다. 기존 [개요 생성·소스 변경 시험](qwen-overviews/README.md), [Vendor 시험](qwen-vendor-guides/README.md), [자동 보완 시험](qwen-reader-loop/README.md)은 당시 기록으로 유지하며, 최신 원고의 출처는 이번 증빙에 연결합니다.

한영 42페이지의 링크 검사와 반복 빌드 139개 파일의 일치를 확인했습니다. 새 영어 문장도 실제 Qwen으로 번역했습니다. 자동 검사와 작성 세션의 소스 대조를 수행했으며, 사람 승인·사내 HAL·실기기 검증은 수행하지 않았습니다.

`upstream/master`는 공식 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 libcamera 입력만 사용하고 HTML은 생성기에서 만듭니다. 정기 예약은 설치하지 않았습니다. 소스 변경 처리는 생성기의 `sdd update --to <commit>` 경로로 실행합니다.


## CLI 실행 검증 (2026-10-26)

생성기의 기본 모델 실행 경로는 Hermes CLI입니다. 모델과 제공자는 선택한 CLI 설정을 사용하며, 사용자가 원하면 OpenCode 또는 Claude Code를 독립적으로 선택할 수 있습니다. [실제 Hermes → Qwen 두 커밋 시험](cli-runners/mini-hal/report.json)과 [CLI 증거 검증 요약](cli-runners/mini-hal/verification.json)을 함께 보관합니다. Claude Code는 OAuth 만료로 실패했고 OpenCode는 설치하지 않았습니다.

공식 upstream SHA는 바뀌지 않았습니다. 기존 IPA 범주의 [모듈 정보 검사와 서명 파일 누락 설명](https://ttolsun.github.io/libcamera-sdd/ipa-module-validation.html)을 Hermes로 보완했습니다. 기존 공개 300-TU facts를 같은 SHA에서 재사용했으며 새로운 추출이나 사내 HAL 검증으로 보고하지 않습니다. 원응답과 실패 후보는 cli-runners/libcamera/에 남기며 사람 승인은 아직 없습니다.
