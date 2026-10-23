# libcamera 설계 문서 검증

**[구성 요소 색인](https://ttolsun.github.io/libcamera-sdd/component-index.html)이 추가되었습니다.** 빌드한 모든 파이프라인 10종·IPA 7종·앱의 클래스와 함수를 패키지별로 찾을 수 있습니다. [영어판](https://ttolsun.github.io/libcamera-sdd/en/component-index.html)도 함께 제공합니다.

## 재현 기준과 확인 결과

- 공식 upstream의 새 커밋 23개 중 8개를 `sdd update`로 하나씩 처리했습니다. `7a25b42`(IPA 튜닝 YAML 변경, LLM 판정 '문서 추가 필요')에서 사람의 범위 판단을 기다리며 멈췄고, 그 뒤 커밋은 아직 반영하지 않았습니다. 분석 기준은 `4eb2378f21b81b02b2814bde7be86d34f3297de8`이며 생성기는 `92ea02b4b83153f39df3ad6e0371139e9a00882e`입니다.
- WSL에서 모든 파이프라인·IPA와 cam·lc-compliance·GStreamer를 빌드하고 TU 299개를 추출했습니다. 파싱 오류와 시나리오 진입점 누락은 0개입니다. cam의 SDL 출력은 libsdl2가 없어 빌드하지 않았습니다.
- 커밋마다 문서가 다루지 않는 변경을 검사했습니다. 주석·공백·`#include`만 바뀐 파일과 빌드 밖 파일 11개는 자동 분류했고, 남은 항목은 LLM(qwen3.5:9b)이 판정했습니다. 게시한 커밋 중 LLM 판정만으로 관문을 통과한 것은 없습니다. 판정은 사람 검토 전입니다.
- 원고 16편에서 한국어·영어 각 17페이지를 생성했습니다. 내부 링크 오류는 0개이며 manifest를 검증했습니다.
- 생성기 테스트 519개와 Windows/Linux의 Python 3.11·3.14 CI가 통과했습니다.
- 사람의 내용 승인과 사내 Camera HAL 검증은 수행하지 않았습니다. 영어 번역도 사람 검토 전입니다.

[배포 기록](run.json)과 [산출물 해시](docs/site-manifest.json)를 확인할 수 있습니다. 생성기 변경은 [#55](https://github.com/TTolsun/camera-hal-sdd-generator/pull/55), [#56](https://github.com/TTolsun/camera-hal-sdd-generator/pull/56), [#57](https://github.com/TTolsun/camera-hal-sdd-generator/pull/57), [#59](https://github.com/TTolsun/camera-hal-sdd-generator/pull/59), [#60](https://github.com/TTolsun/camera-hal-sdd-generator/pull/60)에 있습니다.

## 동기화와 배포

`upstream/master`는 공식 소스 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 환경에는 정기 예약을 설치하지 않으며 생성기 작업과 함께 upstream 확인·문서 보완·검증·배포를 수행합니다.

생성 HTML을 직접 수정하지 않습니다. 원고·설정·테마는 생성기에서 관리하며 이 저장소에는 공개 libcamera 산출물만 배포합니다. 사내 Camera HAL 소스와 파생 facts·프롬프트·문서·로그는 올리지 않습니다.
