# libcamera 설계 문서 검증

**[처음 읽는 순서](https://ttolsun.github.io/libcamera-sdd/)에서 시작하세요.** For Vendor는 연동·구현 담당자, For Developer는 신입·타팀 개발자를 위한 경로입니다.

처음 소스를 연다면 [시스템 개요](https://ttolsun.github.io/libcamera-sdd/overview.html)를, 장애를 조사한다면 [요청 처리와 문제 진단](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html)을 읽으세요. 구성 실패·완료 누락·정지 문제별로 파일·함수·관측값·다음 분기를 안내합니다. 진단 절차는 소스 기반 조사 계획이며 실기기 시험 결과가 아닙니다.

문단 근거에서 **발췌**를 누르면 문서 안의 코드가 펼쳐집니다. **전체 소스**는 분석 커밋의 코드 저장소로 연결됩니다. 낯선 fence·Pending·컨트롤 정보 맵·활성 스트림은 용어집에서 확인할 수 있습니다. [영어판](https://ttolsun.github.io/libcamera-sdd/en/)도 같은 구조와 근거를 제공합니다.

## 생성과 검증

- 공식 소스는 `2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f`, 생성기는 `3066527e44f5ee843acb0f192cc7505afdc16c9e`입니다. 새 upstream 커밋은 없었습니다.
- 전체 빌드 facts(TU 300개, 클래스 1,513개)와 최신 상세 원고를 유지했습니다. 요청 진단과 개요를 입력 해시에 묶인 Codex 세션 LLM 응답으로 다시 생성했습니다. 고정 설계 답변을 설정에 추가하지 않았습니다.
- 공개 문서만 읽은 새 에이전트가 구성 실패·진단·근거 탐색 장애를 발견했습니다. 수정 후 별도 새 에이전트는 첫 코드·흐름·완료 누락·구성 실패·정지 문제의 필수 과제를 모두 통과했습니다. 시험 빌드와 후속 수정 범위는 배포 기록에 구분했습니다.
- 고유 회귀 테스트 742개 통과, 1개 건너뜀. 최종 관련 테스트 45개 통과. 한영 38페이지에서 링크 오류 0, manifest 검증 성공, 같은 입력의 89개 파일 반복 일치를 확인했습니다.
- 문단 근거의 로컬 발췌 이동과 390px 화면을 확인했습니다. 사내 반입 후보 ZIP 263개 파일의 무결성과 별도 경로에서 공개 mini HAL 생성·검증 4단계를 확인했습니다.
- 한국어·영어와 기술 해석은 사람 검토 전입니다. 사내 Camera HAL·실기기·실제 ADHD 독자의 이해도는 검증하지 않았습니다.

[배포 기록](run.json), [요청·응답 해시](generation-receipts.json), [산출물 해시](docs/site-manifest.json), [생성기 변경 #79](https://github.com/TTolsun/camera-hal-sdd-generator/pull/79)을 확인하세요.

## 동기화와 배포

`upstream/master`는 공식 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 정기 예약은 설치하지 않습니다. 생성기 작업과 함께 upstream 확인·누락 보완·검증·배포를 수행합니다.

생성 HTML은 직접 수정하지 않습니다. 공개 libcamera 입력만 배포하며 사내 소스와 파생 facts·문서·프롬프트·로그는 올리지 않습니다.
