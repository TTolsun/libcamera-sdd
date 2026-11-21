# #347 공개 libcamera 독자 경로

첫 화면에서 libcamera가 장치별 제어를 공통 API로 제공하는 이유와 코드 근거를 소개합니다. 두 역할은 서로 다른 질문으로 시작해 #346의 같은 정지·완료 절을 엽니다. #346에서 게시한 설명과 그림의 파일 해시를 보존했습니다.

## For Vendor

홈에서 “우리 장치에서 무엇을 검증해야 하는가?”를 고르고, 정지 뒤 완료 알림 절의 근거를 엽니다. 정상 촬영과 미완료 요청이 있는 정지를 비교하고, 제출 회차별로 콜백 횟수·요청 상태·버퍼별 상태를 기록합니다. `PipelineHandler::stop()`의 소스에서 장치 정지와 대기 요청 처리를 확인할 수 있습니다. [홈의 검증 안내](https://ttolsun.github.io/libcamera-sdd/#vendor가-먼저-확인할-내용) · [정지 코드 발췌](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#source-eefd1bbecb1aad0a)

## For Developer

홈에서 “취소 상태를 어느 코드에서 확인하는가?”를 고르고, 같은 절의 상태 판정과 코드를 엽니다. 앱의 `Camera::requestCompleted` 콜백에서 `Request::status()`의 `RequestCancelled` 분기를 찾습니다. 영상을 사용하기 전에 버퍼별 `FrameBuffer::metadata().status`가 `FrameSuccess`인지 확인합니다. `Request::Private::complete()`에 상태 판정 코드가 있습니다. [홈의 코드 안내](https://ttolsun.github.io/libcamera-sdd/#처음-읽는-개발자의-순서) · [상태 판정 코드 발췌](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#source-db7f21585c4c2708)

## 확인 범위

- 기준 소스는 `adfa719f8ed67d18fd8a0739fc088a1f8b9e7252`입니다. 한영 홈으로 시작해서 1440px와 390px에서 두 역할 경로를 총 8번 검증했습니다. 390px에서는 첫 화면에 두 역할 링크가 모두 표시됐습니다. 8번 모두 같은 절과 11개 노드 그림에 도달했고, 코드 발췌와 해당 커밋의 전체 소스를 대조했습니다. [영문 홈](https://ttolsun.github.io/libcamera-sdd/en/) · [영문 공통 절](https://ttolsun.github.io/libcamera-sdd/en/request-lifecycle.html#정지와-연결-해제를-구분하기) · [로컬 Chrome 기록](browser-local.json)
- 생성기 CI와 링크·해시 검사, 독립 Codex CLI의 홈 항목 24개 판정을 기록했습니다. 실제 독자 평가와 대상 장치 시험은 미실시 상태입니다. [생성기 PR](https://github.com/TTolsun/camera-hal-sdd-generator/pull/349) · [공개 빌드 기록](release.json)
