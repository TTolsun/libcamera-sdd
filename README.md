# libcamera 설계 문서 검증

**Vendor는 [하드웨어 지원 구조와 구현 개요](https://ttolsun.github.io/libcamera-sdd/vendor-overview.html)에서 시작하세요.** 장치 연결, 설정, 요청 처리, IPA 선택, 종료와 구현 후 확인할 계약을 살핀 뒤 상세 문서로 이동합니다. 이 개요의 설명은 소스 발췌를 입력으로 받은 로컬 LLM이 생성했습니다. [영어판](https://ttolsun.github.io/libcamera-sdd/en/vendor-overview.html)과 [용어집](https://ttolsun.github.io/libcamera-sdd/glossary.html)도 제공합니다.

**본문에서 밑줄이 그어진 용어를 누르면 그 자리에서 뜻이 보입니다.** 용어는 문서 찾기와 [용어집](https://ttolsun.github.io/libcamera-sdd/glossary.html)에서도 찾을 수 있습니다.

## 재현 기준과 확인 결과

- 공식 upstream에 새 커밋은 없습니다. 분석 기준은 `2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f`, 생성기는 `4db414cab9fc3783af6e3c4f7d6de9c9e5d915e2`입니다.
- 같은 커밋의 전체 빌드 facts(TU 300개, 클래스 1,513개)를 재사용하고 현재 설정의 근거를 다시 발췌했습니다. 소스 위치 8,539개를 대조했으며 잘못된 위치는 없습니다. 이번 작업에서 전체 빌드의 증분 빌드도 확인했습니다.
- `ollama/qwen3.5:9b`가 6개 질문의 설명을 생성했습니다. 질문·근거 연결, 원문 구절, 입력·본문 지문을 검사하며, 근거나 질문이 바뀌면 재생성이 필요합니다. 본문을 설정에 미리 작성하지 않습니다.
- 원고 17편에서 한국어·영어 각 19페이지를 생성했습니다. 내부 링크와 manifest 검사를 통과했고 반복 빌드 결과가 같습니다.
- 생성기 테스트 660개와 Windows/Linux의 Python 3.11·3.14 CI가 통과했습니다. 기존 상세 가이드·독자 계약·Vendor 개요를 유지했습니다.
- 용어 표시가 본문을 첫 화면 밖으로 밀어내지 않는지 휴대폰(375px)과 데스크톱(1366px)에서 측정했습니다. IPA 문서의 본문은 데스크톱 405px, 휴대폰 596px에서 시작합니다.
- 사람의 내용 승인과 사내 Camera HAL·실기기 검증은 수행하지 않았습니다. 자동 검사는 설명의 의미를 승인하지 않으며 영어 번역도 사람 검토 전입니다.

[배포 기록](run.json)과 [산출물 해시](docs/site-manifest.json)를 확인할 수 있습니다. 생성기 변경은 [#68](https://github.com/TTolsun/camera-hal-sdd-generator/pull/68)과 [#70](https://github.com/TTolsun/camera-hal-sdd-generator/pull/70)에 있습니다.

## 동기화와 배포

`upstream/master`는 공식 소스 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 환경에는 정기 예약을 설치하지 않으며 생성기 작업과 함께 upstream 확인·문서 보완·검증·배포를 수행합니다.

생성 HTML을 직접 수정하지 않습니다. 이 저장소에는 공개 libcamera 산출물만 배포하며 사내 Camera HAL 소스와 파생 facts·프롬프트·문서·로그는 올리지 않습니다.
