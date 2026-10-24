# libcamera 설계 문서 검증

**Vendor는 [요청 처리와 문제 진단](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html), 아키텍처 개발자는 [시스템 개요](https://ttolsun.github.io/libcamera-sdd/overview.html)에서 시작하세요.** [용어집](https://ttolsun.github.io/libcamera-sdd/glossary.html)과 [영어판](https://ttolsun.github.io/libcamera-sdd/en/)도 제공합니다.

## 이번 검증

- 공식 upstream은 `2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f`이며 새 커밋은 없습니다. 생성기는 `e111adc8fccda05a04618b2c416e5e465495afd8`입니다.
- [생성기 #71](https://github.com/TTolsun/camera-hal-sdd-generator/pull/71)에서 사내 에이전트의 설정·계약 작성·검증 가이드와 스킬을 정리했습니다. 검증 중 발견한 소스 탐색 링크의 중복 오탐도 수정했습니다. 실제 설명의 중복 검사는 유지합니다.
- [직전 배포 #18](https://github.com/TTolsun/libcamera-sdd/pull/18)의 facts와 원고 16편을 재사용해 문서·사이트 검사를 수행했습니다. 한국어·영어 각 18페이지와 자산을 포함한 81개 파일 해시는 이전과 같습니다. 검증기 변경으로 manifest 지문과 이 배포 기록만 갱신했습니다.
- 내부 링크 오류는 0개이며 반복 빌드 결과가 같습니다. 화면 검증은 동일한 HTML·자산을 사용한 직전 배포의 결과를 유지합니다.
- 생성기 테스트 633개와 Windows/Linux의 Python 3.11·3.14 CI가 통과했습니다. 별도 공개 mini HAL에서 6개 시나리오·두 독자의 질문 10개, 발췌 후 계약 작성 경로, 반복 빌드, 필수 답변 누락 차단과 출력 보존·복구를 확인했습니다.

이번 변경은 검증기와 사내 적용 지침의 보완이며, 새 libcamera 설계 내용을 추가한 작업은 아닙니다. 사내 소스·파생 자료는 포함하지 않았습니다. 사람의 내용 승인, 실제 독자의 이해도 시험, 사내 HAL과 실기기 검증은 수행하지 않았습니다. 영어 번역도 사람 검토 전입니다.

## 재현 입력과 배포

재사용한 공개 입력은 TU 300개, 클래스 1,513개, 파싱 오류 0개, 시나리오 진입점 누락 0개이며 소스 위치 8,536개를 대조한 facts입니다. 모든 파이프라인·IPA와 cam·lc-compliance·GStreamer 빌드 구성을 사용했고, cam의 SDL 출력은 libsdl2가 없어 제외했습니다. 이번에 추출이나 네이티브 빌드를 다시 수행한 것은 아닙니다.

[배포 기록](run.json)과 [산출물 해시](docs/site-manifest.json)를 확인하세요. `upstream/master`는 공식 소스 이력을 보관하며 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 환경에는 정기 예약을 설치하지 않습니다.

생성 HTML을 직접 수정하지 않습니다. 생성기에서 만든 공개 libcamera 산출물만 배포하며 사내 Camera HAL 소스와 파생 설정·facts·프롬프트·문서·로그는 올리지 않습니다.
