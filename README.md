# libcamera 설계 문서 검증

[공개 문서](https://ttolsun.github.io/libcamera-sdd/index.html)의 왼쪽 메뉴를 **독자 → 수행할 작업 → 문서** 순서로 정리했습니다. For Vendor는 도입 판단·연동 구현·장치별 기능 구현으로, For Developer는 구조 이해·동작 추적과 문제 진단·코드 탐색으로 나눕니다. 요청 처리와 문제 진단은 Developer의 작업 안에서 찾을 수 있습니다. [영어판](https://ttolsun.github.io/libcamera-sdd/en/index.html)도 같은 구조입니다.

## 생성과 검증

- 공식 upstream과 미러는 `2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f`로 일치합니다. 생성기는 `045f409a41bba126eaaa665a13f8cc2dc938b0f6`입니다.
- 새 upstream 커밋이 없어 기존 카테고리의 탐색 누락을 보완했습니다. 전체 빌드 facts(TU 300개, 클래스 1,513개)와 최신 원고 19편을 재사용했습니다. 문서 주소·제목·설계 본문·근거·검토 상태를 유지했고, 홈페이지의 작업별 안내와 메뉴를 갱신했습니다. 구조 재추출과 LLM 재생성은 하지 않았습니다.
- 전체 회귀 773개 통과, 1개 건너뜀. 한국어·영어 42페이지의 링크 오류가 없으며 manifest와 반복 빌드가 일치합니다. 데스크톱 메뉴·시나리오 접기·검색·그림 확대와 요소 검색, 390px 모바일 영어 메뉴를 확인했습니다.
- 이전 배포의 [Qwen EGL 갱신 근거](qwen-update-proof.json), [재현 기록](qwen-replay/README.md), [원고 생성 응답 해시](generation-receipts.json)는 보존했습니다. 원문과 번역은 사람 검토 전이며 실제 사내 HAL·실기기는 검증하지 않았습니다.

[배포 기록](run.json), [산출물 해시](docs/site-manifest.json), [생성기 변경 #85](https://github.com/TTolsun/camera-hal-sdd-generator/pull/85)를 확인하세요.

## 동기화와 배포

`upstream/master`는 공식 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 정기 예약은 설치하지 않습니다. 생성기 작업과 함께 upstream 확인·누락 보완·검증·배포를 수행합니다.

HTML은 생성기에서 다시 만듭니다. 공개 libcamera 입력만 배포하며 사내 소스와 파생 facts·문서·프롬프트·로그는 올리지 않습니다.
