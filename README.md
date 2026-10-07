# libcamera 설계 문서 검증

**[요청 처리와 문제 진단](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html)**에서 요청 제출·완료·재사용·정지를 연결해서 읽을 수 있습니다.

요청 단계별 대기 조건, Request·FrameBuffer·fence의 수명, 오류별 확인 순서와 정지·연결 해제의 차이를 보강했습니다. 첫 화면에는 작업별 읽기 경로를 추가하고 IPU3 LSC에는 조건별 갱신 표를 추가했습니다. [영어판](https://ttolsun.github.io/libcamera-sdd/en/request-lifecycle.html)도 함께 제공합니다.

## 재현 기준과 확인 결과

- 공식 upstream 다섯 커밋을 동기화했습니다. 분석 기준은 `8103c3f29fba61dbd1d3bbf1a099280c5f3217e3`이며 생성기는 `2bb6ff30e7201288b5f28ebd2b4d92065ef6f155`입니다.
- WSL에서 IPU3·RKISP1·UVC와 GStreamer를 빌드하고 TU 171개를 다시 추출했습니다. 파싱 오류와 시나리오 진입점 누락은 0개입니다.
- 인용 위치 5,069개, 필수 설계 질문 32개와 소스 발췌 88개의 연결을 검사했습니다. 원고 14편에서 한국어·영어 각 15페이지를 생성했습니다.
- 내부 링크 오류는 0개이며 manifest와 반복 빌드 동일성을 확인했습니다. 데스크톱·모바일 표 표시와 영어 검색을 확인했습니다.
- 사람의 내용 승인, 특정 기기의 실행 순서·복구 검증과 사내 Camera HAL 검증은 수행하지 않았습니다. 공통 파이프라인의 정적 계약을 특정 하드웨어의 동작 보장으로 해석하지 않습니다.

[배포 기록](run.json)과 [산출물 해시](docs/site-manifest.json)를 확인할 수 있습니다. 생성기 변경은 [PR #51](https://github.com/TTolsun/camera-hal-sdd-generator/pull/51)에 있습니다.

## 동기화와 배포

`upstream/master`는 공식 소스 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 환경에는 정기 예약을 설치하지 않으며 생성기 작업과 함께 upstream 확인·문서 보완·검증·배포를 수행합니다.

생성 HTML을 직접 수정하지 않습니다. 원고·설정·테마는 생성기에서 관리하며 이 저장소에는 공개 libcamera 산출물만 배포합니다. 사내 Camera HAL 소스와 파생 facts·프롬프트·문서·로그는 올리지 않습니다. 영어 번역도 사람 검토 전이며 원문의 승인 상태를 상속하지 않습니다.
