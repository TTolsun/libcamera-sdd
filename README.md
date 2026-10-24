# libcamera 설계 문서 검증

**For Vendor는 연동·구현 담당자, For Developer는 신입·타팀 개발자를 위한 경로입니다.** [처음 읽는 순서](https://ttolsun.github.io/libcamera-sdd/)에서 시작하세요.

Developer는 [시스템 개요](https://ttolsun.github.io/libcamera-sdd/overview.html)에서 첫 파일과 진입점 → 요청 제출·완료 → 증상별 확인 코드 → 수정 전 수명·동기화 조건을 찾습니다. Vendor는 [하드웨어 지원 구조와 구현 개요](https://ttolsun.github.io/libcamera-sdd/vendor-overview.html)에서 구현 계약을 확인합니다. [영어판](https://ttolsun.github.io/libcamera-sdd/en/)도 같은 읽기 경로와 근거를 제공합니다.

근거는 **문단 근거 N개**와 **절 전체 근거 N개**를 펼쳐 확인합니다. 휴대폰에서는 넓은 표가 열 이름을 가진 행별 묶음으로 표시됩니다.

## 생성과 검증

- 소스는 공식 upstream `2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f`, 생성기는 `4932912bbb41c12c628363b4543f87ccc920978e`입니다. upstream에 새 커밋은 없었으며 처음 읽는 개발자 안내의 누락을 보완했습니다.
- 전체 빌드 facts(TU 300개, 클래스 1,513개)와 원고 16편을 재사용하고 시스템 개요를 다시 생성했습니다. 개요는 에이전트가 실제 소스를 대조해 설정에 작성한 계약이며 `source-bound-contract`로 표시합니다. Vendor 개요의 기존 LLM 생성 이력은 유지합니다.
- 생성기 통합 테스트 725개 통과, 1개 건너뜀. 한영 사이트 38페이지에서 내부 링크 오류 0과 manifest 일치를 확인했고, 같은 원고·카탈로그의 반복 빌드에서 산출물 88개와 manifest가 같았습니다.
- 첫 진입점 링크, 근거 Enter·Space 접기와 영어 모바일 메뉴를 브라우저에서 확인했습니다. 최신 main 통합 후에도 390px 화면에서 가로 넘침이 없었습니다.
- 현재 작성 에이전트의 의미 대조이며 새 독립 에이전트나 실제 신입·타팀 독자의 이해도 시험은 아닙니다. 한국어·영어는 사람 검토 전이며 사내 Camera HAL·실기기·ADHD 독자의 이해도는 검증하지 않았습니다.

[배포 기록](run.json), [산출물 해시](docs/site-manifest.json), [생성기 변경 #78](https://github.com/TTolsun/camera-hal-sdd-generator/pull/78)을 확인하세요.

## 동기화와 배포

`upstream/master`는 공식 소스 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 환경에는 정기 예약을 설치하지 않습니다. 생성기 작업과 함께 upstream 확인·문서 보완·검증·배포를 수행합니다.

생성 HTML을 직접 수정하지 않습니다. 공개 libcamera 산출물만 배포하며 사내 Camera HAL 소스와 파생 facts·프롬프트·문서·로그는 올리지 않습니다.
