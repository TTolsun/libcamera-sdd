# libcamera 설계 문서 검증

**[공개 설계 문서 열기](https://ttolsun.github.io/libcamera-sdd/)**

이번 갱신은 공식 upstream에 새 커밋이 없음을 확인한 뒤 기존 공개 facts로 문서 13편을 다시 생성했습니다. 요청 제출·재사용 설명을 쉬운 단어와 짧은 문장으로 고치고, 재사용 시 상태와 완료 대기 버퍼를 복원하는 동작을 소스 근거로 보완했습니다. 앞선 배포의 요청 거부 조건 설명도 유지합니다. facts를 재추출하거나 기기 실행을 검증한 것은 아닙니다.

- [캡처 종료 요청](docs/scenarios/camera_stop.md): Camera::stop()의 상태 검사·종료 호출 대상·대기 요청 확인과 정적 추적 경계를 설명합니다.
- [카메라와 요청 모델](docs/camera-model.md): 연결 해제의 상태 변화·API 접근 제한과 대기 요청 처리의 확인 한계를 소스 근거에 연결합니다.
- [Pipeline Handler](docs/pipeline-handler.md): 대기 큐 분리, 장치 정지, 취소와 완료 계약을 확인할 수 있습니다.

문서 13편과 HTML 14페이지를 생성했습니다. 시나리오 6개의 전체 호출 기록 507개를 보존하며, 설계 질문 27개와 소스 발췌 66개의 연결을 검사했습니다. 사람의 내용 승인과 실제 장치 동작 검증은 별도입니다.

## 재현 기준

- 공식 소스: [libcamera](https://gitlab.freedesktop.org/camera/libcamera), `0f0450158f4eaa37de633520822a9c4a1c25c5ea`
- 생성기: [camera-hal-sdd-generator](https://github.com/TTolsun/camera-hal-sdd-generator), `16aee63f1ba07f22e1c05fe6729ba2e954f85cab`
- 앞선 WSL Meson/Ninja 빌드에서 전체 추출·검증한 TU 171개의 facts를 같은 소스 커밋에서 재사용했습니다. 해당 추출의 파싱 오류와 시나리오 진입점 누락은 0개입니다.
- 빌드 범위는 IPU3·RKISP1·UVC와 GStreamer입니다. Raspberry Pi·software ISP 변경 이력도 보관하지만 해당 하드웨어의 빌드·동작 검증을 뜻하지 않습니다.
- [배포 기록](run.json)과 [입력·산출물 해시](docs/site-manifest.json)를 확인할 수 있습니다.

[4B·9B 동일 입력 비교](https://github.com/TTolsun/camera-hal-sdd-generator/blob/main/docs/model-comparison.md)에서는 두 모델 모두 의미 오류나 조건 누락이 남았습니다. 기본 모델을 유지하며 비교 원고는 공개 설계 설명으로 채택하지 않았습니다. 생성 페이지는 사실·소스 계약에서 만들며 사람의 승인으로 표시하지 않습니다.

## 동기화와 배포

`upstream/master`는 공식 원본 이력을 보관합니다. [동기화 워크플로](.github/workflows/sync-upstream.yml)는 수동 실행만 지원하며 force push는 하지 않습니다. 공개 환경에는 정기 예약을 두지 않습니다.

`main`은 문서와 배포 기록을 관리하고 GitHub Pages는 `docs/`를 게시합니다. 생성기 저장소에서 작업할 때 공식 upstream을 확인·동기화하고 문서 갱신·PR 병합·배포 확인까지 함께 수행합니다. 새 커밋이 없으면 기존 카테고리에서 근거가 있는 누락을 보완합니다. 매일 21시 등의 정기 예약은 사내 운영을 위한 공통 실행기 기능이며 이 공개 환경에서는 사용하지 않습니다.

생성 HTML을 직접 수정하지 않습니다. 원고·설정·테마는 생성기에서 관리하고 이 저장소에는 공개 libcamera 산출물만 배포합니다. 사내 Camera HAL의 소스·facts·문서·프롬프트·로그를 올리지 않습니다.
