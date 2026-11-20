제공된 시험 조건에서는 **A는 요청 완료 호출에 도달하지 않은 경우**, **B는 요청 완료 상태가 되었지만 앞선 요청 때문에 반환이 지연되는 경우**로 구분합니다. 둘 다 실제 기기에서 측정한 결과는 아닙니다.

`completeBuffer()`의 `true`는 **그 요청에 포함된 모든 버퍼의 완료 처리**를 뜻합니다. 요청은 자동으로 완료되지 않습니다. 제공된 [완료 처리 소스 발췌](https://ttolsun.github.io/libcamera-sdd/pipeline-requests.html#source-01ad7c6605c3296a)는 `bufferCompleted.emit()` 다음에 내부 버퍼 추적을 갱신하고, 핸들러가 `completeRequest()`를 명시적으로 호출해야 한다고 보여 줍니다.

## 사례 A: 완료 호출에 진입하지 않음

시험 입력대로 같은 제출 건을 제출부터 추적했고 관련 경로 전체를 빠짐없이 관측했다면, 관측 구간 동안 **대상 요청의 `completeRequest()` 진입이 없었다**고 판단할 수 있습니다. 필요한 후처리가 끝난 뒤에도 호출이 없다면 핸들러의 요청 완료 누락이 가능한 원인입니다. 반대로 후처리가 아직 진행 중이거나 그 이후 호출을 기다리는 구간이라면, 현재 정보만으로 영구 누락이나 코드 결함을 확정할 수 없습니다.

다음에는 대상 파이프라인 핸들러의 기존 버퍼 완료 경로에서 다음을 확인하겠습니다.

1. 마지막 `completeBuffer(request, buffer)`의 인자와 `true` 반환을 제출 회차에 연결합니다.
2. 그 반환 뒤 필요한 추가 작업, 조건 분기, 오류·취소 경로와 `completeRequest(request)`에 이르는 호출 지점을 추적합니다. 취소 경로의 `cancelRequest()`도 내부에서 `completeRequest()`를 호출하므로 함께 살핍니다.
3. 후처리가 끝났는데 정상 완료 호출이 빠져 있다면, 모든 버퍼가 각각 완료된 것을 확인한 뒤 **CameraManager 스레드에서** 명시적으로 완료하도록 구현을 검토합니다. 조사만을 위해 상태 변경 함수를 다시 호출하지는 않습니다.

참고로 제공된 공개 [UVC 예제 발췌](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#source-bfa0db3a4bc7970d)는 `imageBufferReady()`에서 `completeBuffer()` 다음에 `completeRequest()`를 호출합니다. 이는 선택된 UVC 경로의 예이며, 시험 대상이 UVC이거나 다른 핸들러도 같은 호출 구조라는 증거는 아닙니다.

## 사례 B: 앞선 Pending 요청에 의한 반환 지연

시험 입력에서는 대상 제출의 `completeRequest()` 진입과 상태 변경을 확인했고, 이어진 큐 검사에서 **앞서 제출된 다른 요청이 선두이며 `RequestPending`**입니다. 따라서 그 검사에서 반환 루프는 `break`하고, 뒤의 대상 요청에는 도달하지 않습니다. 이것은 해당 시점의 통지 지연을 설명하는 소스상 원인입니다. 선두 요청이 왜 Pending인지는 아직 미확인입니다.

[큐 반환 소스](https://ttolsun.github.io/libcamera-sdd/pipeline-requests.html#source-236c920e906cb6fd)에서 `completeRequest(request)`는 먼저 **전달받은 요청**의 상태를 갱신한 다음, `queuedRequests_.front()`의 **별도 변수 `req`**를 검사합니다. 선두가 Pending이 아니면 대기 버퍼가 없음을 단언하고 제거한 뒤 `camera->requestComplete(req)`를 호출합니다. 한 `completeRequest` 진입과 한 통지 호출을 일대일로 가정해서는 안 됩니다.

다음에는 선두 요청의 제출 ID를 확보하고 그 요청의 버퍼 완료, 남은 버퍼, 추가 처리와 `completeRequest` 또는 취소 경로를 추적하겠습니다. 선두가 완료된 뒤에도 대상 사이에 다른 Pending 요청이 있으면 거기서 다시 멈출 수 있으므로, **대상에 도달할 때까지 각 선두 상태와 실제 `requestComplete(req)` 인자**를 확인합니다. 대상의 상태가 `RequestComplete`인지 `RequestCancelled`인지는 `cancelled_`와 실제 상태 대입을 보고 구분합니다. 버퍼가 모두 끝났다는 사실만으로 촬영 성공이나 비취소 상태를 단정할 수 없습니다. [상태 대입 발췌](https://ttolsun.github.io/libcamera-sdd/pipeline-requests.html#source-0626196def047e5c)

## 같은 제출인지 확인하는 방법

실제 조사에서는 카메라 ID와 실행 ID에 더해, **앱의 `queueRequest()` 호출마다 고유한 제출 회차 ID와 재사용 세대**를 만들겠습니다. 공통 시각과 스레드 ID를 함께 기록하고, 유효한 시점에 `Request *`, cookie, 할당된 요청 `sequence_`, 버퍼 식별자를 회차 ID에 연결합니다.

`Request *`와 cookie는 재사용될 수 있고, `sequence_`는 나중에 `doQueueRequest()`에서 부여되며 정지 때 초기화될 수 있으므로 각각만으로 회차를 식별하지 않습니다. 프레임 메타데이터의 sequence도 요청 sequence와 같은 키로 취급하지 않습니다. 동시 제출에서는 API 호출 시작 순서와 실제 게시·큐 등록 순서를 따로 기록합니다. [제출 회차 및 순서 조사](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#준비-대기와-재진입을-좁히기), [큐 등록 소스](https://ttolsun.github.io/libcamera-sdd/pipeline-requests.html#source-789eafedfaa7f3c5)

핸들러는 `completeRequest()` 또는 `cancelRequest()`가 반환된 뒤 해당 요청에 접근하면 안 됩니다. 통지 후 비교에는 미리 확보한 기록을 사용합니다. 버퍼는 요청 완료 콜백까지 유효해야 하며, 별도 Queued 수신자가 포인터를 더 오래 사용한다면 그 마지막 사용도 동기화해야 합니다. [요청과 버퍼 수명](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#요청버퍼fence의-수명)

## 관측이 불완전하거나 앱 진입이 없을 때

호출 기록이 없다는 것만으로 호출이 없었다고 확정하지 않습니다. 마지막으로 확인한 지점, 처음 미관찰된 지점, 활성 계측, 관측 구간과 손실 건수, 제출 회차 연결의 확실성을 기록합니다. 특히 버퍼 완료 **신호만** 봤다면 내부 추적 갱신과 `completeBuffer()` 반환은 별도로 확인해야 합니다. Direct 수신자는 내부 갱신 전에 실행될 수 있습니다. [버퍼 알림의 내부 경계](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#버퍼-알림과-요청-반환의-내부-경계)

대상 요청이 큐에서 나간 뒤에도 경계를 나눠 봅니다.

- `Camera::requestComplete(req)`가 **대상 회차로 실제 호출됐는지** 확인합니다. 호출됐다면 그 호출의 `isAccessAllowed(CameraStopping, CameraRunning, true)`에서 읽은 상태와 결과를 기록합니다. 범위 밖이면 Fatal 경계이며 정상 신호 발생을 가정하지 않습니다. [Camera 소스 발췌](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#source-a8b87568e9f33e81)
- 상태 검사를 통과한 뒤 **`requestCompleted.emit` 발생**과 **같은 회차의 앱 핸들러 진입**을 따로 기록합니다. emit을 관찰해도 특정 앱 수신자의 실행을 증명하지는 않습니다.
- 앱 진입이 미관찰이면 실제 슬롯 연결과 수신 객체 수명, 연결 방식, 발신·수신 스레드, 이벤트 루프와 메시지 소비, 관측 손실을 확인합니다. `Auto`는 같은 스레드면 Direct, 다르면 Queued를 선택합니다. Direct는 즉시 동기 호출하고 Queued는 게시 후 수신 완료를 기다리지 않습니다. [연결 방식 소스 발췌](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#source-bfdfed92f905633d)

## 자료 확인 기록과 막힌 지점

네트워크 방문이나 도구 검색은 하지 않았습니다. 아래는 **사용자가 제공한 사본에서 확인한 페이지와 정확한 앵커**이며, 검색어는 실제 도구에 입력한 이력이 아니라 사본을 살필 때의 확인어입니다.

| 사본의 페이지·앵커 | 확인 내용 |
|---|---|
| [vendor-integration: 요청을 장치에 전달하고 반환하기](https://ttolsun.github.io/libcamera-sdd/vendor-integration.html#요청을-장치에-전달하고-반환하기) | 버퍼 완료와 명시적 요청 완료의 책임 |
| [pipeline-requests: 버퍼 완료와 요청 반환](https://ttolsun.github.io/libcamera-sdd/pipeline-requests.html#버퍼-완료와-요청-반환) | `completeBuffer`, `completeRequest`, 선두 Pending 분기 |
| [request-diagnosis: 실패 위치별 확인 순서](https://ttolsun.github.io/libcamera-sdd/request-diagnosis.html#실패-위치별-확인-순서) | 미관측 값과 조사 메모, 완료 경계 |
| [request-lifecycle: 콜백의 스레드와 재진입](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#콜백의-스레드와-재진입을-구분하기) | 신호 발생과 수신 실행의 구분 |
| [request-lifecycle: 실제 UVC 장치에서 같은 요청의 완료 기록을 대조하는 절차](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#실제-uvc-장치에서-같은-요청의-완료-기록을-대조하는-절차) | 제출 세대, 큐 선두, 상태 검사 및 앱 진입의 조사 계획 |

사본에 실제 코드가 펼쳐져 있는 발췌 중에서는 `pipeline_handler.cpp:547~620`, `request.cpp:125~139`, `camera.cpp:1475~1491`, `bound_method.cpp:22~110`과 위 UVC 발췌를 대조했습니다. 확인어는 `completeBuffer`, `completeRequest`, `RequestPending`, `queuedRequests_`, `requestCompleted`, `ConnectionTypeQueued`, `reuse`, `sequence_`입니다.

**미발견·미확인:** 대상 벤더 핸들러의 실제 구현, A의 후처리 진행 상태, B의 선두 요청이 Pending인 원인, 실제 앱 연결과 이벤트 루프 상태, 실기기 로그 및 실행 결과는 제공 자료에 없습니다. 따라서 어느 사례도 실제 제품의 근본 원인이나 수정 완료로 판정할 수 없습니다.