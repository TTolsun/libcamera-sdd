# libcamera 설계 문서 검증

[공개 문서](https://ttolsun.github.io/libcamera-sdd/index.html)의 10개 문서에 핵심 질문을 설명하는 그림 20개를 추가했습니다. [카메라 상태 전이](https://ttolsun.github.io/libcamera-sdd/camera-model.html), [요청 흐름·소유권·실패 분기](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html), IPA 실행 경계와 장치별 보정 흐름을 설명 가까이에서 볼 수 있습니다. [영어판](https://ttolsun.github.io/libcamera-sdd/en/index.html)은 같은 연결을 유지합니다.

## 생성과 검증

- 공식 upstream과 미러는 `2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f`로 일치합니다. 생성기는 `3ad601c94d3bbf40333581cfb4a30cc04ccc86eb`이며 [변경 PR #88](https://github.com/TTolsun/camera-hal-sdd-generator/pull/88)을 사용합니다.
- 전체 빌드 facts(TU 300개, 클래스 1,513개)를 재사용하고 현재 설정으로 발췌를 수집했습니다. 최신 Vendor 답변 검증·원고와 기존 설명을 보존했으며 구조 재추출이나 새 LLM 설명 호출은 하지 않았습니다.
- 노드 99개·화살표 96개의 발췌 33개를 실제 Git 원문 9개 파일과 대조했습니다. 그림 아래에서 요소별 원문을 펼치거나 Mermaid 원문을 내려받을 수 있습니다. 해시 연결 검사는 작성한 해석의 의미 승인이나 실행 검증이 아닙니다.
- 통합 회귀 816개 통과·1개 건너뜀, 최종 관련 검사 61개 통과. 한영 42페이지의 링크 오류는 0개이고 manifest·반복 빌드가 일치합니다. 데스크톱 한영 렌더링을 확인했지만 Windows UI 자동화 중단으로 모바일과 확대·검색·Escape 수동 재검증은 완료하지 못했습니다.
- [Vendor 실제 9B 재시험](vendor-llm-retest/README.md), [이전 Qwen EGL 갱신 근거](qwen-update-proof.json), [원고 생성 응답 해시](generation-receipts.json)는 보존했습니다. 사람 의미 승인·독립 독자 평가·사내 HAL·실기기는 검증하지 않았습니다.

[배포 기록](run.json), [그림 근거 대조](visualization-verification.json), [산출물 해시](docs/site-manifest.json)를 확인하세요.

## 동기화와 배포

`upstream/master`는 공식 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 정기 예약은 설치하지 않습니다. 생성기 작업과 함께 upstream 확인·누락 보완·검증·배포를 수행합니다.

HTML은 생성기에서 다시 만듭니다. 공개 libcamera 입력만 배포하며 사내 소스와 파생 facts·문서·프롬프트·로그는 올리지 않습니다.
