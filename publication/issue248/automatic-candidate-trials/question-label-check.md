# 질문 안내와 B2 자동 회귀 확인

## 범위와 식별

2026-11-04 20:29:32 UTC에 내용 조회 전에 `candidate/site-manifest.json`을 확인했습니다. build_id는 지정값 `0f150c6b2d03e800a227ac1726d7d016108c5cd1107994d5a2a2a670e3bdfa76`와 일치했습니다. 이후 내용은 `build/issue248/candidate/scenarios/queue_request.html`과 그 안의 발췌만 읽었습니다. 코드·작성 이력·정답표나 다른 후보 페이지는 읽지 않았습니다.

같은 자동 에이전트가 같은 페이지와 과업을 세 번째로 접했습니다. 이전 노출의 학습 효과가 있으며 이번 결과는 변경을 확인하는 자동 회귀입니다. 독립 첫 독자나 사람 평가가 아니며, 사람의 부담·이해도·흥미·기억 또는 성과 점수를 만들지 않았습니다. 브라우저 화면과 그림 렌더링도 평가하지 않았습니다. 범위는 B2와 상단 질문 안내에 한정했습니다.

## 상단 질문 안내의 실제 원문

두 문장은 다음과 같습니다.

> Camera::queueRequest()의 요청 조건을 확인하고 반환값과 완료 알림을 어떻게 구분합니까?

> 접수된 요청은 언제 장치로 전달되며, 대기·취소·큐잉 실패는 어떻게 처리됩니까?

첫 질문은 `#요청을-제출하기-전에-갖출-조건`, 둘째 질문은 `#큐로-전달된-요청의-준비와-실패`에 연결됩니다. 두 문장은 독자가 문서에서 답을 찾을 의문문으로 표시됩니다. 이 안내에서는 ‘한 번 설명하세요’, ‘조건별로 설명하세요’, ‘다시 요약하지 마세요’, ‘세 문단 이내로 작성하세요’, ‘소스 한 줄마다 문단을 만들지 마세요’라는 작성 지시를 찾지 못했습니다. 같은 HTML의 텍스트에서도 이 다섯 문자열이 없는 것을 추가로 확인했습니다. 상단의 ‘시작된 카메라에 유효한 요청을 제출하고 완료 알림은 별도로 확인하세요’는 독자의 작업 안내로 읽히며 원고 작성 지시는 아닙니다.

안내가 짧아진 사실만으로 조건·예외·근거의 충족을 판정하지 않았습니다. 아래 본문과 발췌를 직접 대조했습니다. 변경 이유나 작성 의도는 추측하지 않았습니다.

## B2 실제 답과 근거 대조

요청 전달 대상은 `PipelineHandler::queueRequest()`입니다. `Camera::queueRequest()`는 이를 `invokeMethod()`의 메서드 인자로 전달하며, 호출부에 `ConnectionTypeQueued`를 지정합니다. 본문의 연결 방식 설명과 L1373~1380 발췌가 대응합니다. 예약 호출 표시는 인자로 전달된 메서드 대상을 뜻하며 그 표시 자체가 비동기 실행을 보증하지 않습니다. 실제 연결 방식과 동기화 계약을 확인해야 합니다.

준비와 큐 한도도 본문과 발췌에서 확인했습니다. `PipelineHandler::queueRequest()`는 요청을 waitingRequests_에 넣고 `prepare(300ms)`를 호출하며, 이 함수의 주석은 CameraManager 스레드에서 호출된다고 설명합니다. 준비된 요청을 제출 순서로 최대 maxQueuedRequestsDevice_까지 넘깁니다. `doQueueRequests()`는 queuedRequests_.size()가 maxQueuedRequestsDevice_와 같으면 중단하고, 선두 요청의 prepared_가 거짓이어도 중단합니다. 조건을 통과한 요청을 먼저 pop한 후 doQueueRequest에 넘기는 순서도 발췌에 있습니다.

취소·실패 분기도 직접 확인했습니다. L447~478 주석은 준비 실패 또는 하드웨어 큐잉 실패 때 요청이 취소된다고 설명합니다. L483~501 구현은 소프트웨어 queuedRequests_에 요청을 추가하고 sequence_를 부여한 뒤, cancelled_가 참이면 completeRequest를 호출하고 바로 반환해 장치 큐잉을 건너뜁니다. 거짓이면 queueRequestDevice를 호출하고 결과 ret가 0이 아닐 때 cancelRequest를 호출합니다. doQueueRequest 자체는 void 함수입니다.

정적 추적의 경계는 본문의 ‘주요 확인 지점’, ‘주요 호출 관계’, ‘추적 범위와 경계’에서 확인했습니다. 나열 순서나 기록 번호는 실행 순서가 아닙니다. 화살표는 시간 순서나 모든 경로의 실행을 뜻하지 않습니다. 조건 분기·반복 횟수·실제 실행 스레드는 이 호출 목록만으로 확정할 수 없고, 가상 호출 후보는 실제 객체에 따라 달라집니다. 예약된 호출 1개라는 통계도 실제 비동기 실행이나 모든 경로의 실행을 보장하지 않습니다.

확인한 후보 앵커와 공개 대응 주소는 다음과 같습니다. 공개 대응 주소는 후보의 배포 완료를 뜻하지 않습니다.

- [큐로 전달된 요청의 준비와 실패](https://ttolsun.github.io/libcamera-sdd/scenarios/queue_request.html#큐로-전달된-요청의-준비와-실패)
- [ConnectionTypeQueued 호출부, L1373~1380](https://ttolsun.github.io/libcamera-sdd/scenarios/queue_request.html#source-997ecce495182b6b)
- [준비·순서·실패 계약과 prepare, L447~478](https://ttolsun.github.io/libcamera-sdd/scenarios/queue_request.html#source-5493b66ef420047f)
- [큐 한도와 선두 prepared_, L509~527](https://ttolsun.github.io/libcamera-sdd/scenarios/queue_request.html#source-9bef16708cb3efe3)
- [취소와 장치 반환 오류 분기, L483~501](https://ttolsun.github.io/libcamera-sdd/scenarios/queue_request.html#source-7348e9b4af985eb2)
- [주요 확인 지점](https://ttolsun.github.io/libcamera-sdd/scenarios/queue_request.html#주요-확인-지점)
- [주요 호출 관계](https://ttolsun.github.io/libcamera-sdd/scenarios/queue_request.html#주요-호출-관계)
- [추적 범위와 경계](https://ttolsun.github.io/libcamera-sdd/scenarios/queue_request.html#추적-범위와-경계)

## 실제 경로와 한계

실제 조회 경로는 후보 `scenarios/queue_request.html` 상단 질문 안내 → `#요청을-제출하기-전에-갖출-조건` → `#큐로-전달된-요청의-준비와-실패` → `#주요-확인-지점` → `#주요-호출-관계` → `#추적-범위와-경계` → `#source-997ecce495182b6b` → `#source-5493b66ef420047f` → `#source-9bef16708cb3efe3` → `#source-7348e9b4af985eb2`입니다. HTML을 파싱한 순서이며 브라우저 클릭이나 뒤로 가기 동작이 아닙니다. 20:29:47 UTC에 본문과 발췌 대조를 마쳤습니다. 과업별 순수 독해 시간은 미측정입니다. 막힌 점은 없었습니다. 이번 제한 범위에서는 추가 편집 문제를 찾지 못했으며, 이를 전체 페이지나 전체 사이트의 독자 품질 승인으로 확장하지 않습니다.

## 종료 식별

종료 시 manifest build_id는 `0f150c6b2d03e800a227ac1726d7d016108c5cd1107994d5a2a2a670e3bdfa76`로 시작과 같았습니다. 요청 제출 HTML의 시작·종료 SHA-256도 모두 `ad8a82eeb31e1d47e6169e5f0a11f42879fefb58f1f0891e79d995b396490845`로 같았습니다. 다른 build 내용을 섞지 않았습니다. 이 결과 파일만 작성했으며 코드·문서는 수정하지 않았습니다.
