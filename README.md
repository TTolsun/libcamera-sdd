# libcamera 설계 문서 검증

**Vendor는 [요청 처리와 문제 진단](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html), 아키텍처 개발자는 [시스템 개요](https://ttolsun.github.io/libcamera-sdd/overview.html)에서 시작하세요.** 소유권·완료 규칙의 기준 설명을 나누고, 같은 페이지의 소스 발췌 중복을 줄였습니다. [용어집](https://ttolsun.github.io/libcamera-sdd/glossary.html)과 [영어판](https://ttolsun.github.io/libcamera-sdd/en/)도 제공합니다.

## 재현 기준과 확인 결과

- 공식 upstream에 새 커밋은 없습니다. 분석 기준은 `2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f`, 생성기는 `e886c9ce7d22469344165588687deaa74f11c713`입니다.
- 기존 전체 빌드에서 TU 300개를 새로 추출하고 원고 16편을 재생성했습니다. 클래스 1,513개, 파싱 오류 0개, 시나리오 진입점 누락 0개이며 소스 위치 8,536개를 대조했습니다. 이번에 네이티브 빌드를 다시 수행한 것은 아닙니다.
- 빌드 구성은 모든 파이프라인·IPA와 cam·lc-compliance·GStreamer입니다. cam의 SDL 출력은 libsdl2가 없어 제외된 구성입니다.
- 한국어·영어 각 18페이지를 생성했습니다. 내부 링크 오류는 0개이며 반복 빌드의 manifest와 모든 산출물이 같습니다.
- 요청 진단 문서의 소스 발췌 패널을 22개에서 10개로 줄였습니다. 소유권·재사용의 상세 규칙은 객체 모델 문서에서, 장치 완료 구현은 Pipeline Handler 문서에서 관리합니다.
- 모바일 이동 안내는 가로 스크롤 없이 읽을 수 있습니다. 데스크톱·모바일, 근거 펼치기, 문서 검색, 그림 확대·요소 검색·닫기와 영어판 이동을 확인했습니다.
- 생성기 통합 테스트 584개와 Windows/Linux의 Python 3.11·3.14 CI가 통과했습니다. 사내 템플릿과 별도의 작은 HAL 예제도 같은 독자별 필수 질문·소스 근거·분량 검사를 사용합니다.
- 사람의 내용 승인, 실제 독자의 이해도 시험, 사내 Camera HAL과 실기기 동작 검증은 수행하지 않았습니다. 영어 번역도 사람 검토 전입니다.

[배포 기록](run.json)과 [산출물 해시](docs/site-manifest.json)를 확인할 수 있습니다. 생성기 변경은 [#69](https://github.com/TTolsun/camera-hal-sdd-generator/pull/69)에 있으며 [#67](https://github.com/TTolsun/camera-hal-sdd-generator/pull/67)의 용어집 기능을 유지합니다.

## 동기화와 배포

`upstream/master`는 공식 소스 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 환경에는 정기 예약을 설치하지 않으며 생성기 작업과 함께 upstream 확인·문서 보완·검증·배포를 수행합니다.

생성 HTML을 직접 수정하지 않습니다. 원고·설정·테마는 생성기에서 관리하며 이 저장소에는 공개 libcamera 산출물만 배포합니다. 사내 Camera HAL 소스와 파생 facts·프롬프트·문서·로그는 올리지 않습니다.
