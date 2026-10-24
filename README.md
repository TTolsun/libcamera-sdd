# libcamera 설계 문서 검증

**Developer는 [시스템 개요](https://ttolsun.github.io/libcamera-sdd/overview.html), Vendor는 [하드웨어 지원 구조와 구현 개요](https://ttolsun.github.io/libcamera-sdd/vendor-overview.html)에서 시작하세요.** 두 개요 모두 현재 소스 발췌를 근거로 LLM이 설명을 생성합니다. 질문이나 근거가 바뀌면 기존 답변을 그대로 게시하지 않고 재생성을 요구합니다.

시스템 개요는 컴포넌트 책임, 탐색, 요청 소유권, 캡처 수명주기, 제출·완료, 동기화와 확인 한계를 다룹니다. [영어판](https://ttolsun.github.io/libcamera-sdd/en/overview.html)에서도 같은 절과 원문 근거를 확인할 수 있습니다.

문단 끝의 긴 근거는 **문단 근거 N개**, 절의 전체 목록은 **절 전체 근거 N개**를 펼쳐 확인하세요. 파일별 줄 번호를 묶었으며, 원고와 근거 위치·발췌·해시는 그대로 유지합니다.

## 재현 기준과 확인 결과

- 공식 upstream에 새 커밋은 없습니다. 소스는 `2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f`, 생성기는 `a044ef55f2fab125912521b1d6ff6b01da752dad`입니다.
- 같은 커밋의 전체 빌드 facts(TU 300개, 클래스 1,513개)와 원고 17편을 재사용했습니다. 이번에는 표시만 개선했으며 LLM 재생성과 소스 변경은 없습니다.
- 기존 시스템 개요의 8개 질문은 `ollama/qwen3.5:9b`의 실제 응답으로 작성되었습니다. 이번 표시 개선에서는 그 원고와 생성 이력을 보존했습니다. 설정에는 설명 본문을 고정하지 않습니다.
- 원고 17편에서 한국어·영어 각 19페이지를 생성했습니다. 내부 링크와 manifest 검사를 통과했고 반복 빌드 결과가 같습니다.
- 생성기 테스트 686개(1개 건너뜀)와 Windows/Linux Python 3.11·3.14 CI가 통과했습니다. 새 에이전트가 한영 38페이지를 대조해 근거 링크 손실 0건, 발췌·해시 164건 보존과 원고 바이트 동일성을 확인했습니다. 모바일·키보드·근거 이동·그림 조작도 브라우저에서 확인했습니다.
- 자동 검사는 사람의 내용 승인이 아닙니다. 한국어와 영어는 사람 검토 전이며 사내 Camera HAL·실기기 검증은 수행하지 않았습니다.

[배포 기록](run.json)과 [산출물 해시](docs/site-manifest.json)를 확인할 수 있습니다. 이번 생성기 변경은 [#74](https://github.com/TTolsun/camera-hal-sdd-generator/pull/74)에 있습니다.

## 동기화와 배포

`upstream/master`는 공식 소스 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 환경에는 정기 예약을 설치하지 않으며 생성기 작업과 함께 upstream 확인·문서 보완·검증·배포를 수행합니다.

생성 HTML을 직접 수정하지 않습니다. 이 저장소에는 공개 libcamera 산출물만 배포하며 사내 Camera HAL 소스와 파생 facts·프롬프트·문서·로그는 올리지 않습니다.
