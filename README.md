# libcamera 설계 문서 검증

**For Vendor는 연동·구현 담당자, For Developer는 신입·타팀 개발자를 위한 경로입니다.** [처음 읽는 순서](https://ttolsun.github.io/libcamera-sdd/)에서 시작하세요.

Developer는 [시스템 개요](https://ttolsun.github.io/libcamera-sdd/overview.html)에서 첫 파일과 진입점 → 요청 제출·완료 → 증상별 확인 코드 → 수정 전 수명·동기화 조건을 찾습니다. Vendor는 [하드웨어 지원 구조와 구현 개요](https://ttolsun.github.io/libcamera-sdd/vendor-overview.html)에서 구현 계약을 확인합니다. [영어판](https://ttolsun.github.io/libcamera-sdd/en/)도 같은 읽기 경로와 근거를 제공합니다.

근거는 **문단 근거 N개**와 **절 전체 근거 N개**를 펼쳐 확인합니다. 휴대폰에서는 넓은 표가 열 이름을 가진 행별 묶음으로 표시됩니다.

## 생성과 검증

- 소스는 공식 upstream `2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f`, 생성기는 `8dc830e7c616927ca0592d371c21fa8b6257f90f`입니다. upstream에 새 커밋은 없었으며, 고정 설명의 생성·갱신 경로를 보완했습니다.
- 전체 빌드 facts(TU 300개, 클래스 1,513개)를 재사용했습니다. 상세 문서 6편과 Developer 시스템 개요의 40개 주제·154개 설명 문단을 LLM 응답으로 다시 생성했습니다. 기존 Vendor LLM 개요를 포함한 설계 문서 8편 모두 질문·소스 선택자만 설정하며 답변을 고정하지 않습니다.
- 이번 7편의 작성 주체는 **Codex 세션**입니다. 소스를 대조한 응답을 입력 해시에 연결한 `response-bundle`로 가져왔으며, Qwen의 실패한 설명은 게시하지 않았습니다. 이 파일 경로는 모델을 직접 호출하지 않습니다. 입력이 바뀌면 새 응답이 필요하며, 연결된 모델의 자동 호출은 `ollama`·`openai-compatible` 경로를 사용합니다.
- 회귀 테스트 합계 740개 통과, 1개 건너뜀. 소스 인용 8,545곳·563개 파일에 잘못된 위치가 없었습니다. 한영 38페이지의 내부 링크 오류는 0이며 산출물 88개와 manifest가 반복 빌드에서 같았습니다.
- 한국어 Pipeline Handler 본문·문단 근거 펼치기와 영어 Developer 첫 파일·진단 안내를 브라우저에서 확인했습니다. 390px 영어 개요 화면에서 가로 넘침이 없었으며 기존 모바일 표·탐색 디자인을 유지합니다.
- 한국어·영어와 기술 해석은 사람 검토 전입니다. 사내 Camera HAL과 실기기 동작은 검증하지 않았습니다.

[배포 기록](run.json), [요청·응답 해시 기록](generation-receipts.json), [산출물 해시](docs/site-manifest.json), [생성기 변경 #75](https://github.com/TTolsun/camera-hal-sdd-generator/pull/75)을 확인하세요.

## 동기화와 배포

`upstream/master`는 공식 소스 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 환경에는 정기 예약을 설치하지 않습니다. 생성기 작업과 함께 upstream 확인·문서 보완·검증·배포를 수행합니다.

생성 HTML을 직접 수정하지 않습니다. 공개 libcamera 산출물만 배포하며 사내 Camera HAL 소스와 파생 facts·프롬프트·문서·로그는 올리지 않습니다.
