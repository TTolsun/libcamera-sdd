# libcamera 설계 문서 검증

**공개 libcamera 소스에 근거한 검토용 설계 문서입니다.**

[웹 문서 열기](https://ttolsun.github.io/libcamera-sdd/)

| 문서 | 생성 방식 |
|---|---|
| [시스템 개요](docs/overview.md) | 탐색·요청 생성·캡처 상태·스레드 경계 설명을 소스 발췌 해시에 연결합니다. |
| [핵심 시나리오](docs/scenarios/index.md) | facts로 주요 호출 관계와 추적 경계를 구성하고 전체 호출 기록을 보존합니다. |
| [카메라와 요청 모델](docs/camera-model.md) | 책임·상태·요청·소유권·종료·동시성의 여섯 설계 계약을 소스 발췌 해시에 연결합니다. |
| [Pipeline Handler](docs/pipeline-handler.md) | 구성·요청 준비·완료 순서·접근 수명·정지 계약을 소스 발췌 해시에 연결합니다. |
| [IPA 관리와 구현 진입점](docs/ipa.md) | 모듈 선택·실행 경계·입출력·수명·IPC 실패 설명을 소스 발췌 해시에 연결합니다. |
| [IPU3 LSC와 상태 연결](docs/ipu3-lsc.md) | 직접 상속과 필드 참조를 facts에서 문장과 그림으로 생성합니다. |
| [IPU3 LSC의 설정과 프레임 처리](docs/ipu3-lsc-flow.md) | 초기화·요청 처리·파라미터 갱신 설명을 소스 발췌 해시에 연결합니다. |

문서 12편의 자동 검사가 통과했으며, 설계 질문 26개와 소스 발췌 64개의 연결을 확인했습니다. 다섯 시나리오의 추적 기록 474개를 모두 보존합니다. 사람의 내용 검토와 실제 콜백·하드웨어 종료 검증은 별도입니다. 전체 문서 범위 검사는 이번 배포에서 다시 실행하지 않았으며, 사내 Camera HAL의 검증 결과가 아닙니다.

각 페이지에서 생성 방식과 검증 범위를 구분하고, 설계 설명 아래의 원문을 펼쳐 대조할 수 있습니다. 메뉴는 스크롤바 공간을 미리 확보해 하위 문서를 펼쳐도 다른 제목의 줄바꿈이 바뀌지 않습니다. CSS 원본은 생성기의 `src/sdd/site_assets/reading.css`이며, 이 저장소의 `docs/assets/reading.css`는 생성기가 복사한 배포 산출물입니다.

## 소스와 생성기

- 원본: [libcamera upstream](https://gitlab.freedesktop.org/camera/libcamera)
- 분석 커밋: `279d355ef8f7a4f98bb0a3004c0f788387814506`
- 생성기: [camera-hal-sdd-generator](https://github.com/TTolsun/camera-hal-sdd-generator), 커밋 `960297dee346f57b22bb1e0559ab48f3fdd51859`
- [이번 생성기 개선과 검증 범위](https://github.com/TTolsun/camera-hal-sdd-generator/blob/960297dee346f57b22bb1e0559ab48f3fdd51859/docs/generator-quality-validation.md)
- [LSC 문서 보강과 범위 검토 기록](https://github.com/TTolsun/camera-hal-sdd-generator/blob/6887f0b3a9feda91e7824e6e64751539068429d0/docs/libcamera-lsc-followup.md)
- [A/B 검증 기록](https://github.com/TTolsun/camera-hal-sdd-generator/blob/main/docs/libcamera-design-validation.md)
- [배포 기록](run.json)과 [입력·산출물 해시](docs/site-manifest.json)

기존에 빌드와 구조 추출을 검증한 facts를 사용하고 동일한 커밋에서 소스 발췌를 다시 대조했습니다. 이번 문서 생성은 LLM을 호출하지 않았으며, libcamera를 다시 빌드하거나 전체 추출하지 않았습니다. 생성·검증 기술은 camera-hal-sdd-generator에서 관리하고 이 저장소에는 공개 libcamera 문서와 정적 산출물만 배포합니다.

## 브랜치와 게시

`main`은 문서와 배포 기록을 관리하며 GitHub Pages는 `docs/`를 게시합니다. `upstream/master`는 libcamera 원본 이력을 보존합니다. 문서는 작업 브랜치와 PR로 갱신하며 원본 브랜치에는 문서 커밋이나 force push를 하지 않습니다.

생성 HTML을 직접 수정하지 않습니다. 생성기의 원고·설정·테마를 수정한 뒤 export-site와 verify-site를 실행합니다. 사이트 안내 원고는 [site-intro.md](site-intro.md)에 보관합니다. 자동 문서 갱신과 예약 작업은 아직 연결하지 않았습니다.
