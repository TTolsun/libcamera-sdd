# libcamera 설계 문서 검증

Vendor 문서는 [libcamera 제품 개요](https://ttolsun.github.io/libcamera-sdd/vendor-overview.html), [연동 가이드](https://ttolsun.github.io/libcamera-sdd/vendor-integration.html), [지원 범위와 검증](https://ttolsun.github.io/libcamera-sdd/vendor-assurance.html)으로 나누었습니다. [영어판](https://ttolsun.github.io/libcamera-sdd/en/vendor-overview.html)도 같은 구성과 근거를 제공합니다. 신입·타팀 개발자는 [시스템 개요](https://ttolsun.github.io/libcamera-sdd/overview.html)에서 시작합니다.

제공 기능과 공통 요청 관리의 강점을 소개하고, 장치 구현자의 책임과 지원 조건을 설명합니다. 코드 계약과 측정 결과를 구분하며 성능 우위나 모든 하드웨어 지원을 주장하지 않습니다. 고객 구매·제품 홍보 자료로 확정하려면 실제 제품 사양·지원 조합·시험 결과와 공개 승인이 필요합니다.

## 생성과 검증

- 공식 upstream `2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f`, 생성기 `d3ded865198a5603011916f337722044e17cb12e`를 사용했습니다. 공식 upstream에 새 커밋이 없어 공개 근거의 설명 누락을 보완했습니다.
- 전체 빌드 facts(TU 300개, 클래스 1,513개)를 재사용하고 124개 발췌를 재수집했습니다. Codex 세션의 근거 대조 답변으로 3개 문서·12개 주제를 생성하고 나머지 최신 원고 16편은 유지했습니다. 이전 배포의 [Qwen EGL 갱신 근거](qwen-update-proof.json)와 [재현 기록](qwen-replay/README.md)도 보존했습니다. 구조 재추출은 하지 않았습니다.
- 최신 main과 병합한 전체 회귀 771개 통과, 1개 건너뜀. 관련 검사 64개 통과. 한영 42페이지의 내부 링크 오류가 없으며 manifest와 반복 빌드 98개 파일의 일치를 확인했습니다.
- 실제 로컬 qwen3.5:9b 시험에서는 2개 문서가 자동 검사를 통과했고 1개는 실패했습니다. 통과한 문서에도 의미 오류가 있어 초안을 채택하지 않았습니다. 이 결과는 사내 모델·HAL의 자동 게시 준비 완료를 뜻하지 않습니다.
- 공통 프로필·평가 명령·사내 템플릿을 제공합니다. 실제 사내 HAL·실기기·Vendor 읽기 시험은 수행하지 않았으며 원문·번역은 사람 검토 전입니다.

[배포 기록](run.json), [응답 해시](generation-receipts.json), [산출물 해시](docs/site-manifest.json), [생성기 변경 #82](https://github.com/TTolsun/camera-hal-sdd-generator/pull/82)을 확인하세요.

## 동기화와 배포

`upstream/master`는 공식 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 정기 예약은 설치하지 않습니다. 생성기 작업과 함께 upstream 확인·누락 보완·검증·배포를 수행합니다.

HTML은 직접 수정하지 않습니다. 공개 libcamera 입력만 배포하며 사내 소스와 파생 facts·문서·프롬프트·로그는 올리지 않습니다.
