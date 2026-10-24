# libcamera 설계 문서 검증

**[IPA 문서](https://ttolsun.github.io/libcamera-sdd/ipa.html)에 보정 전 튜닝 파일과 소프트웨어 ISP 렌즈 음영 보정 설명이 추가되었습니다.** 빌드한 모든 클래스와 함수는 [구성 요소 색인](https://ttolsun.github.io/libcamera-sdd/component-index.html)에서 패키지별로 찾을 수 있습니다. [영어판](https://ttolsun.github.io/libcamera-sdd/en/)도 함께 제공합니다.

## 재현 기준과 확인 결과

- 공식 upstream의 새 커밋 24개를 모두 `sdd update`로 하나씩 처리했습니다. 분석 기준은 `2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f`이며 생성기는 `3080f2e39155115ed20633a38cfc8c2b62b90fbd`입니다.
- WSL에서 모든 파이프라인·IPA와 cam·lc-compliance·GStreamer를 빌드하고 TU 300개를 추출했습니다. 파싱 오류와 시나리오 진입점 누락은 0개입니다. cam의 SDL 출력은 libsdl2가 없어 빌드하지 않았습니다.
- 커밋마다 문서가 다루지 않는 변경을 검사했습니다. 주석·공백·`#include`만 바뀐 파일, 빌드 밖 파일, 설계 근거가 파일 전체를 고정한 파일, 효과가 분석한 빌드에서 모두 검사된 빌드 파일 18개는 자동 분류했습니다. 남은 항목은 LLM(qwen3.5:9b)이 판정했고, LLM 판정만으로 관문을 통과한 커밋은 없습니다. 판정은 사람 검토 전입니다.
- 코드가 아닌 파일 때문에 멈춘 커밋(튜닝 YAML, 셰이더, mojom)은 승인으로 넘기지 않고 IPA 문서에 소스 근거가 있는 설명을 추가해 해결했습니다. 설명은 사람 검토 전입니다.
- 원고 16편에서 한국어·영어 각 17페이지를 생성했습니다. 내부 링크 오류는 0개이며 manifest를 검증했습니다.
- 생성기 테스트 544개와 Windows/Linux의 Python 3.11·3.14 CI가 통과했습니다.
- 사람의 내용 승인과 사내 Camera HAL 검증은 수행하지 않았습니다. 영어 번역도 사람 검토 전입니다.

[배포 기록](run.json)과 [산출물 해시](docs/site-manifest.json)를 확인할 수 있습니다. 생성기 변경은 [#55](https://github.com/TTolsun/camera-hal-sdd-generator/pull/55), [#56](https://github.com/TTolsun/camera-hal-sdd-generator/pull/56), [#57](https://github.com/TTolsun/camera-hal-sdd-generator/pull/57), [#59](https://github.com/TTolsun/camera-hal-sdd-generator/pull/59), [#60](https://github.com/TTolsun/camera-hal-sdd-generator/pull/60), [#61](https://github.com/TTolsun/camera-hal-sdd-generator/pull/61), [#62](https://github.com/TTolsun/camera-hal-sdd-generator/pull/62), [#63](https://github.com/TTolsun/camera-hal-sdd-generator/pull/63), [#64](https://github.com/TTolsun/camera-hal-sdd-generator/pull/64), [#65](https://github.com/TTolsun/camera-hal-sdd-generator/pull/65), [#66](https://github.com/TTolsun/camera-hal-sdd-generator/pull/66)에 있습니다.

## 동기화와 배포

`upstream/master`는 공식 소스 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 환경에는 정기 예약을 설치하지 않으며 생성기 작업과 함께 upstream 확인·문서 보완·검증·배포를 수행합니다.

생성 HTML을 직접 수정하지 않습니다. 원고·설정·테마는 생성기에서 관리하며 이 저장소에는 공개 libcamera 산출물만 배포합니다. 사내 Camera HAL 소스와 파생 facts·프롬프트·문서·로그는 올리지 않습니다.
