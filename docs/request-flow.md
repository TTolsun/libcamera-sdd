# 요청 흐름과 핵심 개념

요청을 만들고 제출하는 쪽에서 시작해 버퍼 완료, 요청 반환, 정지 뒤 취소 상태까지 따라가세요.

## 요청 생성과 소유권

`Camera::createRequest(cookie)`의 `cookie`는 애플리케이션이 사용하는 불투명한 입력입니다. 이 값은 요청에 저장되며 `Request::cookie()`로 언제든 읽을 수 있고, `libcamera` 관점에서는 완전히 불투명합니다. 애플리케이션은 보통 요청 완료 핸들러에서 요청을 외부 리소스에 연결하는 데 이 값을 사용합니다. `Camera::createRequest()`는 카메라가 `Configured` 또는 `Running` 상태일 때만 호출할 수 있으며, 오류가 발생하면 `nullptr`을 반환합니다.

### 요청 생성과 소유권의 관계와 경계

```mermaid
flowchart TB
%% sdd:translations {"Camera::createRequest는 <br/>Configured 또는 Running <br/>상태에서만 호출할 수 <br/>있으며, 빈 요청을 반환하고 <br/>오류가 나면 nullptr를 <br/>반환합니다.": "Camera::createRequest <br/>creates an empty request in <br/>Configured or Running and <br/>returns nullptr on error.", "Request::reuse의 flags가 <br/>버퍼 재사용 여부를 <br/>나타냅니다.": "The flags of Request::reuse <br/>indicate whether to reuse <br/>buffers.", "ReuseBuffers를 지정하면 <br/>기존 버퍼를 다시 <br/>연결합니다. #91;true#93;": "With ReuseBuffers, the <br/>existing buffers are <br/>associated again. #91;true#93;", "ReuseBuffers를 지정하지 <br/>않으면 버퍼 맵을 비웁니다. <br/>#91;false#93;": "Without ReuseBuffers, the <br/>buffer map is cleared. <br/>#91;false#93;", "bufferMap#95;을 비워 이전 버퍼 <br/>연결을 제거합니다.": "bufferMap#95; is cleared, <br/>removing the previous <br/>buffer associations.", "flags로 버퍼 재사용 여부를 <br/>선택합니다. 펜스를 사용하면 <br/>ReuseBuffers를 피합니다.": "Flags choose buffer reuse. <br/>Avoid ReuseBuffers when <br/>using fences.", "각 기존 buffer에 요청을 <br/>설정하고 pending#95;에 <br/>넣습니다. 모든 항목을 <br/>처리하면 반복이 끝납니다.": "Each existing buffer gets <br/>the request and enters <br/>pending#95;; the loop then <br/>ends.", "버퍼 처리 뒤 상태를 <br/>RequestPending으로 바꾸고 <br/>제어와 메타데이터를 <br/>비웁니다.": "After buffer handling, set <br/>RequestPending and clear <br/>controls and metadata.", "버퍼 처리를 마친 뒤 <br/>초기화합니다.": "Reset after buffer handling.", "요청을 반환하면 소유권이 <br/>호출자에게 넘어갑니다.": "The returned request#39;s <br/>ownership passes to the <br/>caller.", "요청을 재사용하려면 다시 <br/>제출하기 전에 <br/>Request::reuse를 호출합니다.": "Call Request::reuse before <br/>queueing the request again.", "호출자는 반환된 요청을 <br/>소유하며 삭제할 책임이 <br/>있습니다. 완료 핸들러에서 <br/>삭제하거나 상태를 초기화한 <br/>뒤 재사용할 수 있습니다.": "The caller owns and must <br/>delete the request; it may <br/>delete it on completion or <br/>reset and reuse it.", "호출자는 삭제하는 대신 <br/>상태를 초기화해 재사용할 수 <br/>있습니다.": "The caller may reset and <br/>reuse the request instead <br/>of deleting it."}
  v_create["Camera::createRequest는 <br/>Configured 또는 Running <br/>상태에서만 호출할 수 <br/>있으며, 빈 요청을 반환하고 <br/>오류가 나면 nullptr를 <br/>반환합니다."]
  v_caller["호출자는 반환된 요청을 <br/>소유하며 삭제할 책임이 <br/>있습니다. 완료 핸들러에서 <br/>삭제하거나 상태를 초기화한 <br/>뒤 재사용할 수 있습니다."]
  v_reuse["요청을 재사용하려면 다시 <br/>제출하기 전에 <br/>Request::reuse를 호출합니다."]
  v_flags{"flags로 버퍼 재사용 여부를 <br/>선택합니다. 펜스를 사용하면 <br/>ReuseBuffers를 피합니다."}
  v_buffer["각 기존 buffer에 요청을 <br/>설정하고 pending#95;에 <br/>넣습니다. 모든 항목을 <br/>처리하면 반복이 끝납니다."]
  v_map["bufferMap#95;을 비워 이전 버퍼 <br/>연결을 제거합니다."]
  v_reset["버퍼 처리 뒤 상태를 <br/>RequestPending으로 바꾸고 <br/>제어와 메타데이터를 <br/>비웁니다."]
  v_create -->|"요청을 반환하면 소유권이 <br/>호출자에게 넘어갑니다."| v_caller
  v_caller -->|"호출자는 삭제하는 대신 <br/>상태를 초기화해 재사용할 수 <br/>있습니다."| v_reuse
  v_reuse -->|"Request::reuse의 flags가 <br/>버퍼 재사용 여부를 <br/>나타냅니다."| v_flags
  v_flags -->|"ReuseBuffers를 지정하면 <br/>기존 버퍼를 다시 <br/>연결합니다. #91;true#93;"| v_buffer
  v_flags -->|"ReuseBuffers를 지정하지 <br/>않으면 버퍼 맵을 비웁니다. <br/>#91;false#93;"| v_map
  v_buffer -->|"버퍼 처리를 마친 뒤 <br/>초기화합니다."| v_reset
  v_map -->|"버퍼 처리를 마친 뒤 <br/>초기화합니다."| v_reset
```

Mermaid 원문

<details open>
<summary>그림 근거와 확인 범위</summary>

호출자는 요청을 어떻게 생성·소유·삭제하거나 재사용하며, ReuseBuffers 지정 여부에 따라 버퍼는 어떻게 되나요?

소스 연결 해석 · 자동 연결 검사만 통과 · 의미와 기기 실행은 검증 전

| 요소·전이 | 소스 근거 |
| --- | --- |
| Camera::createRequest는 Configured 또는 Running 상태에서만 호출할 수 있으며, 빈 요청을 반환하고 오류가 나면 nullptr를 반환합니다. | src/libcamera/camera.cpp:1243 |
| 호출자는 반환된 요청을 소유하며 삭제할 책임이 있습니다. 완료 핸들러에서 삭제하거나 상태를 초기화한 뒤 재사용할 수 있습니다. | src/libcamera/camera.cpp:1243 |
| 요청을 재사용하려면 다시 제출하기 전에 Request::reuse를 호출합니다. | src/libcamera/request.cpp:376 |
| flags로 버퍼 재사용 여부를 선택합니다. 펜스를 사용하면 ReuseBuffers를 피합니다. | src/libcamera/request.cpp:376 · src/libcamera/request.cpp:326 |
| 각 기존 buffer에 요청을 설정하고 pending\_에 넣습니다. 모든 항목을 처리하면 반복이 끝납니다. | src/libcamera/request.cpp:376 |
| bufferMap\_을 비워 이전 버퍼 연결을 제거합니다. | src/libcamera/request.cpp:376 |
| 버퍼 처리 뒤 상태를 RequestPending으로 바꾸고 제어와 메타데이터를 비웁니다. | src/libcamera/request.cpp:376 |
| 요청을 반환하면 소유권이 호출자에게 넘어갑니다. | src/libcamera/camera.cpp:1243 |
| 호출자는 삭제하는 대신 상태를 초기화해 재사용할 수 있습니다. | src/libcamera/camera.cpp:1243 |
| Request::reuse의 flags가 버퍼 재사용 여부를 나타냅니다. | src/libcamera/request.cpp:376 |
| ReuseBuffers를 지정하면 기존 버퍼를 다시 연결합니다. · flags & ReuseBuffers \[true\] | src/libcamera/request.cpp:376 |
| ReuseBuffers를 지정하지 않으면 버퍼 맵을 비웁니다. · flags & ReuseBuffers \[false\] | src/libcamera/request.cpp:376 |
| 버퍼 처리를 마친 뒤 초기화합니다. | src/libcamera/request.cpp:376 |
| 버퍼 처리를 마친 뒤 초기화합니다. | src/libcamera/request.cpp:376 |

</details>

`Camera::createRequest()`가 반환한 요청의 소유권은 호출자에게 넘어가며, 호출자는 요청을 삭제할 책임이 있습니다. 호출자는 새 요청을 만들지 않고 같은 요청을 다시 큐에 넣으려면 큐에 넣기 전에 `Request::reuse()`를 호출해 요청 상태와 연결된 컨트롤을 초기화해야 합니다. `Request::reuse()`는 `ReuseBuffers`를 지정하면 `addBuffer()`로 추가한 기존 버퍼를 요청에 다시 연결해 재사용하고 지정하지 않으면 `bufferMap_`을 비우며, 버퍼에 연결된 펜스는 재사용하지 않으므로 펜스를 사용할 때는 `ReuseBuffers`를 쓰지 않도록 권고합니다.

<details open>
<summary>절 전체 근거 3개</summary>

- `src/libcamera/camera.cpp``L1243` 발췌 · [전체 소스 `L1243`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L1243)
- `src/libcamera/request.cpp``L376` 발췌 · [전체 소스 `L376`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/request.cpp#L376) · `L326` 발췌 · [전체 소스 `L326`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/request.cpp#L326)

</details>

## 요청 제출과 완료

함께 확인: [버퍼 완료와 요청 전체 완료 구분](#completion) · [완료 호출자와 스레드 의무](#callback-thread)

애플리케이션은 `Camera::queueRequest()`로 제출하기 전에 `createRequest()`가 반환한 요청 객체에 캡처 버퍼를 최소 한 개 연결해야 합니다. 카메라는 `Camera::queueRequest()`로 큐에 넣은 요청의 처리가 끝나면 `requestCompleted` 신호로 애플리케이션에 완료를 알립니다. `Camera::queueRequest()`는 카메라가 `Running` 상태일 때만 호출해야 합니다.

### 요청 접수와 버퍼 완료, 요청 완료

```mermaid
flowchart TB
%% sdd:translations {"0 반환: 접수 성공": "Return 0: submission <br/>accepted", "Running 상태에서 제출": "Submit in Running state", "completeBuffer#40;#41;: 버퍼 완료 <br/>알림과 추적": "completeBuffer#40;#41;: buffer <br/>completion notification and <br/>tracking", "completeRequest#40;#41;: <br/>파이프라인 핸들러의 명시적 <br/>요청 완료": "completeRequest#40;#41;: explicit <br/>request completion by the <br/>pipeline handler", "queueRequest#40;#41;": "queueRequest#40;#41;", "requestCompleted 신호": "requestCompleted signal", "마지막 버퍼가 완료되어도 <br/>요청은 자동으로 완료되지 <br/>않으므로 핸들러가 별도로 <br/>완료해야 함": "Even the last buffer does <br/>not automatically complete <br/>the request; the handler <br/>must complete it separately", "버퍼를 연결한 Request": "Request with capture buffers", "음수 오류 반환. 빈 요청은 <br/>큐에 넣지 않음": "Negative error. Empty <br/>requests are not queued", "접수 성공": "Accepted", "제출 거부": "Rejected", "촬영 완료는 별도로 통지": "Notify completion separately"}
  v_request["버퍼를 연결한 Request"]
  v_queue["queueRequest#40;#41;"]
  v_accepted["0 반환: 접수 성공"]
  v_signal["requestCompleted 신호"]
  v_complete-buffer["completeBuffer#40;#41;: 버퍼 완료 <br/>알림과 추적"]
  v_complete-request["completeRequest#40;#41;: <br/>파이프라인 핸들러의 명시적 <br/>요청 완료"]
  v_rejected["음수 오류 반환. 빈 요청은 <br/>큐에 넣지 않음"]
  v_request -->|"Running 상태에서 제출"| v_queue
  v_queue -->|"접수 성공"| v_accepted
  v_accepted -->|"촬영 완료는 별도로 통지"| v_signal
  v_complete-buffer -->|"마지막 버퍼가 완료되어도 <br/>요청은 자동으로 완료되지 <br/>않으므로 핸들러가 별도로 <br/>완료해야 함"| v_complete-request
  v_queue -->|"제출 거부"| v_rejected
```

Mermaid 원문

<details open>
<summary>그림 근거와 확인 범위</summary>

queueRequest()의 반환값은 접수 결과입니다. completeBuffer()는 버퍼 완료를 알리고 추적하며, 파이프라인 핸들러는 completeRequest()로 요청을 별도로 완료해야 합니다. requestCompleted 신호는 요청 완료를 별도로 알립니다.

소스 연결 해석 · 자동 연결 검사만 통과 · 의미와 기기 실행은 검증 전

LLM 그림 초안 · 사람 검토 전

작성 모델: `cli/codex/gpt-6.1-terra`

| 요소·전이 | 소스 근거 |
| --- | --- |
| 버퍼를 연결한 Request | src/libcamera/camera.cpp:1308 |
| queueRequest() | src/libcamera/camera.cpp:1308 |
| 0 반환: 접수 성공 | src/libcamera/camera.cpp:1308 |
| requestCompleted 신호 | src/libcamera/camera.cpp:1308 |
| completeBuffer(): 버퍼 완료 알림과 추적 | src/libcamera/pipeline_handler.cpp:547 |
| completeRequest(): 파이프라인 핸들러의 명시적 요청 완료 | src/libcamera/pipeline_handler.cpp:547 |
| 음수 오류 반환. 빈 요청은 큐에 넣지 않음 | src/libcamera/camera.cpp:1308 |
| Running 상태에서 제출 | src/libcamera/camera.cpp:1308 |
| 접수 성공 | src/libcamera/camera.cpp:1308 |
| 촬영 완료는 별도로 통지 | src/libcamera/camera.cpp:1308 |
| 마지막 버퍼가 완료되어도 요청은 자동으로 완료되지 않으므로 핸들러가 별도로 완료해야 함 | src/libcamera/pipeline_handler.cpp:547 |
| 제출 거부 | src/libcamera/camera.cpp:1308 |

</details>

<details open>
<summary>절 전체 근거 1개</summary>

- `src/libcamera/camera.cpp``L1308` 발췌 · [전체 소스 `L1308`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L1308)

</details>

## 요청·버퍼·fence의 수명

### 소유권과 두 완료 경계

`Camera::createRequest()` 호출자는 반환된 `Request`의 소유권을 받으며 삭제할 책임이 있습니다. 호출자는 완료 핸들러에서 요청을 삭제하거나 `Request::reuse()`로 상태를 초기화한 뒤 재사용할 수 있습니다. `Request::addBuffer()`는 버퍼 참조를 요청에 저장하며, 호출자는 요청 완료 콜백이 호출될 때까지 버퍼가 유효하도록 해야 합니다. 파이프라인 핸들러는 `completeRequest()` 또는 `cancelRequest()`가 반환된 뒤 해당 요청에 접근해서는 안 됩니다.

#### 요청과 버퍼를 유지할 기간

```mermaid
flowchart TB
%% sdd:translations {"Queued 수신은 비동기이며 <br/>발신자는 완료를 기다리지 <br/>않습니다. Auto는 같은 <br/>스레드에서 Direct, 다른 <br/>스레드에서 Queued를 <br/>사용합니다.": "Queued delivery is <br/>asynchronous and the sender <br/>does not wait for <br/>completion. Auto uses <br/>Direct in the same thread <br/>and Queued in different <br/>threads.", "Signal::emit으로 포인터나 <br/>참조를 전달하는 발신자는 <br/>신호 발생 후에도 대상이 <br/>유효하도록 해야 합니다.": "An emitter passing a <br/>pointer or reference <br/>through Signal::emit must <br/>ensure that its target <br/>remains valid after <br/>emission.", "addBuffer 호출자는 요청에 <br/>참조로 저장된 버퍼가 요청 <br/>완료 콜백이 호출될 때까지 <br/>유효하도록 해야 합니다.": "The addBuffer caller must <br/>ensure that the buffer <br/>referenced by the request <br/>remains valid until the <br/>request completion callback <br/>is called.", "cancelRequest는 <br/>completeRequest를 호출하며 <br/>같은 완료 규칙을 따릅니다.": "cancelRequest calls <br/>completeRequest and follows <br/>the same completion rules.", "cancelRequest는 요청을 <br/>취소하고 완료합니다. 반환 <br/>후 접근 금지를 포함해 <br/>completeRequest와 같은 <br/>규칙이 적용됩니다.": "cancelRequest cancels and <br/>completes the request. The <br/>same rules as <br/>completeRequest apply, <br/>including the prohibition <br/>on access after return.", "createRequest 호출자는 <br/>반환된 요청의 소유권과 삭제 <br/>책임을 받습니다. 오류가 <br/>나면 nullptr가 반환됩니다.": "The createRequest caller <br/>receives ownership of the <br/>returned request and is <br/>responsible for deleting <br/>it. On error, nullptr is <br/>returned.", "reuse는 요청의 상태와 제어 <br/>값을 초기화합니다. 다시 <br/>큐에 넣기 전에 호출하며 <br/>ReuseBuffers로 이전 버퍼를 <br/>재사용할 수 있습니다.": "reuse resets the request <br/>status and controls. Call <br/>it before requeuing; <br/>ReuseBuffers can be used to <br/>reuse previously added <br/>buffers.", "반환된 요청은 완료 <br/>핸들러에서 삭제할 수 <br/>있습니다.": "The returned request may be <br/>deleted in the completion <br/>handler.", "별도 Queued 수신자가 <br/>포인터를 계속 쓰면 마지막 <br/>사용까지의 수명과 관계자 간 <br/>협의를 확인하세요. 완료 <br/>콜백 하나나 stop 반환이 <br/>모든 수신을 기다린다고 <br/>가정하지 마세요.": "If a separate Queued <br/>receiver continues to use a <br/>pointer, verify its <br/>lifetime through the last <br/>use and coordination <br/>between parties. Do not <br/>assume one completion <br/>callback or stop return <br/>waits for all receivers.", "삭제 대신 요청의 상태를 <br/>초기화한 뒤 재사용할 수 <br/>있습니다.": "As an alternative to <br/>deletion, the request may <br/>be reused after its state <br/>is reset.", "완료 핸들러에서 요청을 <br/>삭제하거나 상태를 초기화한 <br/>뒤 재사용할 수 있습니다. <br/>삭제와 재사용은 <br/>선택지입니다.": "The request may be deleted <br/>in the completion handler <br/>or reused after its state <br/>is reset. Deletion and <br/>reuse are alternatives.", "요청 완료 콜백은 addBuffer <br/>호출자가 버퍼를 유효하게 <br/>유지해야 하는 기한입니다.": "The request completion <br/>callback is the point until <br/>which the addBuffer caller <br/>must keep the buffer valid.", "파이프라인 핸들러는 <br/>completeRequest가 반환된 뒤 <br/>요청에 접근하면 안 됩니다. <br/>이는 완료 핸들러의 <br/>삭제·재사용 선택과 별도 <br/>경계입니다.": "The pipeline handler must <br/>not access the request <br/>after completeRequest <br/>returns. This is a separate <br/>boundary from the <br/>completion handler#39;s <br/>deletion or reuse choice.", "호출자는 요청 완료 콜백이 <br/>호출될 때까지 버퍼가 <br/>유효하도록 해야 합니다.": "The caller must ensure that <br/>the buffer remains valid <br/>until the request <br/>completion callback is <br/>called."}
  v_create["createRequest 호출자는 <br/>반환된 요청의 소유권과 삭제 <br/>책임을 받습니다. 오류가 <br/>나면 nullptr가 반환됩니다."]
  v_add["addBuffer 호출자는 요청에 <br/>참조로 저장된 버퍼가 요청 <br/>완료 콜백이 호출될 때까지 <br/>유효하도록 해야 합니다."]
  v_handler["완료 핸들러에서 요청을 <br/>삭제하거나 상태를 초기화한 <br/>뒤 재사용할 수 있습니다. <br/>삭제와 재사용은 <br/>선택지입니다."]
  v_callback["요청 완료 콜백은 addBuffer <br/>호출자가 버퍼를 유효하게 <br/>유지해야 하는 기한입니다."]
  v_reuse["reuse는 요청의 상태와 제어 <br/>값을 초기화합니다. 다시 <br/>큐에 넣기 전에 호출하며 <br/>ReuseBuffers로 이전 버퍼를 <br/>재사용할 수 있습니다."]
  v_complete["파이프라인 핸들러는 <br/>completeRequest가 반환된 뒤 <br/>요청에 접근하면 안 됩니다. <br/>이는 완료 핸들러의 <br/>삭제·재사용 선택과 별도 <br/>경계입니다."]
  v_cancel["cancelRequest는 요청을 <br/>취소하고 완료합니다. 반환 <br/>후 접근 금지를 포함해 <br/>completeRequest와 같은 <br/>규칙이 적용됩니다."]
  v_signal["Signal::emit으로 포인터나 <br/>참조를 전달하는 발신자는 <br/>신호 발생 후에도 대상이 <br/>유효하도록 해야 합니다."]
  v_queued["별도 Queued 수신자가 <br/>포인터를 계속 쓰면 마지막 <br/>사용까지의 수명과 관계자 간 <br/>협의를 확인하세요. 완료 <br/>콜백 하나나 stop 반환이 <br/>모든 수신을 기다린다고 <br/>가정하지 마세요."]
  v_create -->|"반환된 요청은 완료 <br/>핸들러에서 삭제할 수 <br/>있습니다."| v_handler
  v_handler -->|"삭제 대신 요청의 상태를 <br/>초기화한 뒤 재사용할 수 <br/>있습니다."| v_reuse
  v_add -->|"호출자는 요청 완료 콜백이 <br/>호출될 때까지 버퍼가 <br/>유효하도록 해야 합니다."| v_callback
  v_cancel -->|"cancelRequest는 <br/>completeRequest를 호출하며 <br/>같은 완료 규칙을 따릅니다."| v_complete
  v_signal -->|"Queued 수신은 비동기이며 <br/>발신자는 완료를 기다리지 <br/>않습니다. Auto는 같은 <br/>스레드에서 Direct, 다른 <br/>스레드에서 Queued를 <br/>사용합니다."| v_queued
```

Mermaid 원문

<details open>
<summary>그림 근거와 확인 범위</summary>

createRequest·addBuffer 호출자, 완료 핸들러의 삭제·재사용과 핸들러 접근 종료, 별도 Queued 수신자의 포인터 수명을 어떻게 구분합니까?

소스 연결 해석 · 자동 연결 검사만 통과 · 의미와 기기 실행은 검증 전

LLM 그림 초안 · 사람 검토 전

작성 모델: `cli/codex/gpt-6.1-terra`

| 요소·전이 | 소스 근거 |
| --- | --- |
| createRequest 호출자는 반환된 요청의 소유권과 삭제 책임을 받습니다. 오류가 나면 nullptr가 반환됩니다. | src/libcamera/camera.cpp:1243 |
| addBuffer 호출자는 요청에 참조로 저장된 버퍼가 요청 완료 콜백이 호출될 때까지 유효하도록 해야 합니다. | src/libcamera/request.cpp:442 |
| 완료 핸들러에서 요청을 삭제하거나 상태를 초기화한 뒤 재사용할 수 있습니다. 삭제와 재사용은 선택지입니다. | src/libcamera/camera.cpp:1243 |
| 요청 완료 콜백은 addBuffer 호출자가 버퍼를 유효하게 유지해야 하는 기한입니다. | src/libcamera/request.cpp:442 |
| reuse는 요청의 상태와 제어 값을 초기화합니다. 다시 큐에 넣기 전에 호출하며 ReuseBuffers로 이전 버퍼를 재사용할 수 있습니다. | src/libcamera/request.cpp:376 |
| 파이프라인 핸들러는 completeRequest가 반환된 뒤 요청에 접근하면 안 됩니다. 이는 완료 핸들러의 삭제·재사용 선택과 별도 경계입니다. | src/libcamera/pipeline_handler.cpp:547 · src/libcamera/camera.cpp:1243 |
| cancelRequest는 요청을 취소하고 완료합니다. 반환 후 접근 금지를 포함해 completeRequest와 같은 규칙이 적용됩니다. | src/libcamera/pipeline_handler.cpp:547 |
| Signal::emit으로 포인터나 참조를 전달하는 발신자는 신호 발생 후에도 대상이 유효하도록 해야 합니다. | src/libcamera/base/signal.cpp:73 |
| 별도 Queued 수신자가 포인터를 계속 쓰면 마지막 사용까지의 수명과 관계자 간 협의를 확인하세요. 완료 콜백 하나나 stop 반환이 모든 수신을 기다린다고 가정하지 마세요. | src/libcamera/base/signal.cpp:73 · src/libcamera/base/bound_method.cpp:22 |
| 반환된 요청은 완료 핸들러에서 삭제할 수 있습니다. | src/libcamera/camera.cpp:1243 |
| 삭제 대신 요청의 상태를 초기화한 뒤 재사용할 수 있습니다. | src/libcamera/camera.cpp:1243 |
| 호출자는 요청 완료 콜백이 호출될 때까지 버퍼가 유효하도록 해야 합니다. | src/libcamera/request.cpp:442 |
| cancelRequest는 completeRequest를 호출하며 같은 완료 규칙을 따릅니다. | src/libcamera/pipeline_handler.cpp:547 |
| Queued 수신은 비동기이며 발신자는 완료를 기다리지 않습니다. Auto는 같은 스레드에서 Direct, 다른 스레드에서 Queued를 사용합니다. | src/libcamera/base/bound_method.cpp:22 |

</details>

### 정상 완료와 다음 요청 준비

`completeBuffer`는 `bufferCompleted`를 emit한 뒤 요청 내부의 버퍼 추적을 갱신하고, 모든 버퍼가 완료되면 `true`, 남은 버퍼가 있으면 `false`를 반환합니다. 마지막 버퍼가 완료되어도 요청은 자동 완료되지 않으므로, 파이프라인 핸들러는 필요한 처리를 마친 뒤 `completeRequest`로 명시적으로 완료를 통지해야 합니다. 두 함수는 `CameraManager` 스레드에서 호출해야 하며, 실제 콜백 실행 스레드는 이 소스에서 확인되지 않습니다. `completeRequest`가 호출하는 내부 `complete`는 `cancelled_`가 `false`이면 `RequestComplete`, `true`이면 `RequestCancelled`를 선택합니다.

#### 버퍼 알림에서 요청 반환까지

```mermaid
flowchart TB
%% sdd:translations {"bufferCompleted 알림": "bufferCompleted notification", "emit 뒤 갱신": "Update after emit", "마지막 버퍼만으로 자동 <br/>완료되지 않음": "Last buffer does not <br/>automatically complete <br/>request", "명시적 completeRequest": "Explicit completeRequest", "완료된 선두부터 반환": "Return completed queue heads", "요청 내부 버퍼 추적 갱신": "Update internal buffer <br/>tracking", "제출 순서로 애플리케이션 <br/>반환": "Return to application in <br/>submission order"}
  v_notice["bufferCompleted 알림"]
  v_tracking["요청 내부 버퍼 추적 갱신"]
  v_complete["명시적 completeRequest"]
  v_return["제출 순서로 애플리케이션 <br/>반환"]
  v_notice -->|"emit 뒤 갱신"| v_tracking
  v_tracking -->|"마지막 버퍼만으로 자동 <br/>완료되지 않음"| v_complete
  v_complete -->|"완료된 선두부터 반환"| v_return
```

Mermaid 원문

<details open>
<summary>그림 근거와 확인 범위</summary>

정상 경로의 호출·추적 순서입니다. 모든 버퍼와 필요한 추가 처리가 끝난 뒤 요청 완료를 통지하며, 실제 실행 시간이나 애플리케이션 콜백 스레드를 나타내지 않습니다.

소스 연결 해석 · 자동 연결 검사만 통과 · 의미와 기기 실행은 검증 전

| 요소·전이 | 소스 근거 |
| --- | --- |
| bufferCompleted 알림 | src/libcamera/pipeline_handler.cpp:547 |
| 요청 내부 버퍼 추적 갱신 | src/libcamera/pipeline_handler.cpp:547 |
| 명시적 completeRequest | src/libcamera/pipeline_handler.cpp:547 |
| 제출 순서로 애플리케이션 반환 | src/libcamera/pipeline_handler.cpp:547 |
| emit 뒤 갱신 | src/libcamera/pipeline_handler.cpp:547 |
| 마지막 버퍼만으로 자동 완료되지 않음 | src/libcamera/pipeline_handler.cpp:547 |
| 완료된 선두부터 반환 | src/libcamera/pipeline_handler.cpp:547 |

</details>

마지막 버퍼 알림은 관찰했지만 요청 완료 콜백은 아직 관찰하지 못한 경우, 그 관측만으로 내부 추적 갱신이나 `completeRequest` 호출이 아직 남았다고 단정할 수 없습니다. 이 알림은 버퍼 유효성 유지 기한이 끝났다는 근거가 아니므로, 버퍼 유효성을 깨뜨리는 해제나 다른 요청에 연결하는 작업의 안전성을 알림만으로 판정할 수 없습니다. 모든 재사용이 일괄적으로 금지되는 것은 아니며, 다른 요청에 연결할 수 있는지는 적용되는 API와 동기화 계약 및 버퍼 유효성 유지를 별도로 대조해야 합니다.

소스 기반 조사 계획으로, 조사자는 기존 `completeBuffer` 호출의 반환값을 관찰합니다. 조사자는 `completeRequest` 호출 자체도 관찰합니다. 이어서 조사자는 제출 순서 때문에 완료된 요청의 반환이 지연되는지와 요청 완료 콜백이 발생하는지를 확인합니다.

## 타임아웃 뒤 펜스 회수

```mermaid
flowchart TB
%% sdd:translations {"다른 요청의 재사용에 필요한 <br/>회수 조건": "Required retrieval <br/>condition for reuse in <br/>another request", "버퍼에 펜스가 남음": "Buffer still contains its <br/>fence", "애플리케이션이 <br/>releaseFence#40;#41;로 회수": "Application retrieves with <br/>releaseFence#40;#41;", "요청 실패 뒤에도 유지": "Remains after request <br/>failure", "재사용 전 회수 의무": "Must retrieve before reuse", "펜스 미신호: 요청 타임아웃": "Unsignalled fence: request <br/>times out", "회수는 필요한 선행 조건": "Retrieval is a necessary <br/>precondition"}
  v_timeout["펜스 미신호: 요청 타임아웃"]
  v_retained["버퍼에 펜스가 남음"]
  v_retrieve["애플리케이션이 <br/>releaseFence#40;#41;로 회수"]
  v_reuse["다른 요청의 재사용에 필요한 <br/>회수 조건"]
  v_timeout -->|"요청 실패 뒤에도 유지"| v_retained
  v_retained -->|"재사용 전 회수 의무"| v_retrieve
  v_retrieve -->|"회수는 필요한 선행 조건"| v_reuse
```

Mermaid 원문

<details open>
<summary>그림 근거와 확인 범위</summary>

신호되지 않은 펜스로 타임아웃이 나면 다른 요청에 재사용하기 전에 무엇을 해야 합니까?

소스 연결 해석 · 자동 연결 검사만 통과 · 의미와 기기 실행은 검증 전

| 요소·전이 | 소스 근거 |
| --- | --- |
| 펜스 미신호: 요청 타임아웃 | src/libcamera/request.cpp:462 |
| 버퍼에 펜스가 남음 | src/libcamera/request.cpp:462 |
| 애플리케이션이 releaseFence()로 회수 | src/libcamera/request.cpp:462 |
| 다른 요청의 재사용에 필요한 회수 조건 | src/libcamera/request.cpp:462 |
| 요청 실패 뒤에도 유지 | src/libcamera/request.cpp:462 |
| 재사용 전 회수 의무 | src/libcamera/request.cpp:462 |
| 회수는 필요한 선행 조건 | src/libcamera/request.cpp:462 |

</details>

## <a id="completion"></a>버퍼 완료와 요청 완료

`PipelineHandler::completeBuffer()`는 요청에 속한 버퍼의 완료를 애플리케이션에 알림으로 전달하고, 요청 내부의 버퍼 추적 정보를 갱신합니다. 파이프라인 핸들러는 마지막 버퍼가 완료된 뒤에도 `completeRequest()`를 명시적으로 호출해야 합니다.

### 버퍼 완료와 요청 완료의 관계와 경계

```mermaid
flowchart TB
%% sdd:translations {"마지막 버퍼가 끝나도 요청을 <br/>별도로 완료해야 합니다.": "Even after the last buffer, <br/>the handler must complete <br/>the request explicitly.", "마지막 버퍼가 완료돼도 <br/>요청은 자동 완료되지 <br/>않으므로 핸들러는 <br/>completeRequest#40;#41;로 <br/>명시적으로 완료해야 합니다.": "The last buffer does not <br/>automatically complete the <br/>request; handlers must call <br/>completeRequest#40;#41;.", "모든 버퍼가 완료됐다면 <br/>True를 반환합니다.": "It returns True if all <br/>buffers have completed.", "모든 버퍼가 완료되지 <br/>않았다면 false를 반환합니다.": "It returns false if not all <br/>buffers have completed.", "반환값은 요청에 포함된 <br/>버퍼가 모두 완료됐는지 <br/>나타냅니다.": "The return value indicates <br/>whether all buffers in the <br/>request have completed.", "이 함수는 전체 버퍼의 완료 <br/>여부를 반환합니다.": "The function returns <br/>whether all buffers have <br/>completed.", "파이프라인 핸들러는 <br/>CameraManager 스레드에서 <br/>PipelineHandler::<br/>completeBuffer를 호출해 <br/>개별 버퍼 완료를 알리고 <br/>요청의 버퍼 추적 정보를 <br/>갱신해야 합니다.": "The handler must call <br/>completeBuffer on the <br/>CameraManager thread to <br/>notify and track buffer <br/>completion."}
  v_buffer_completion["파이프라인 핸들러는 <br/>CameraManager 스레드에서 <br/>PipelineHandler::<br/>completeBuffer를 호출해 <br/>개별 버퍼 완료를 알리고 <br/>요청의 버퍼 추적 정보를 <br/>갱신해야 합니다."]
  v_result{"반환값은 요청에 포함된 <br/>버퍼가 모두 완료됐는지 <br/>나타냅니다."}
  v_all_complete["모든 버퍼가 완료됐다면 <br/>True를 반환합니다."]
  v_buffers_remaining["모든 버퍼가 완료되지 <br/>않았다면 false를 반환합니다."]
  v_request_completion["마지막 버퍼가 완료돼도 <br/>요청은 자동 완료되지 <br/>않으므로 핸들러는 <br/>completeRequest#40;#41;로 <br/>명시적으로 완료해야 합니다."]
  v_buffer_completion -->|"이 함수는 전체 버퍼의 완료 <br/>여부를 반환합니다."| v_result
  v_result -->|"모든 버퍼가 완료됐다면 <br/>True를 반환합니다."| v_all_complete
  v_result -->|"모든 버퍼가 완료되지 <br/>않았다면 false를 반환합니다."| v_buffers_remaining
  v_all_complete -->|"마지막 버퍼가 끝나도 요청을 <br/>별도로 완료해야 합니다."| v_request_completion
```

Mermaid 원문

<details open>
<summary>그림 근거와 확인 범위</summary>

개별 버퍼 완료와 전체 버퍼 완료 여부는 명시적인 요청 완료 호출과 어떻게 구분되나요?

소스 연결 해석 · 자동 연결 검사만 통과 · 의미와 기기 실행은 검증 전

| 요소·전이 | 소스 근거 |
| --- | --- |
| 파이프라인 핸들러는 CameraManager 스레드에서 PipelineHandler::completeBuffer를 호출해 개별 버퍼 완료를 알리고 요청의 버퍼 추적 정보를 갱신해야 합니다. | src/libcamera/pipeline_handler.cpp:547 |
| 반환값은 요청에 포함된 버퍼가 모두 완료됐는지 나타냅니다. | src/libcamera/pipeline_handler.cpp:547 |
| 모든 버퍼가 완료됐다면 True를 반환합니다. | src/libcamera/pipeline_handler.cpp:547 |
| 모든 버퍼가 완료되지 않았다면 false를 반환합니다. | src/libcamera/pipeline_handler.cpp:547 |
| 마지막 버퍼가 완료돼도 요청은 자동 완료되지 않으므로 핸들러는 completeRequest()로 명시적으로 완료해야 합니다. | src/libcamera/pipeline_handler.cpp:547 |
| 이 함수는 전체 버퍼의 완료 여부를 반환합니다. | src/libcamera/pipeline_handler.cpp:547 |
| 모든 버퍼가 완료됐다면 True를 반환합니다. | src/libcamera/pipeline_handler.cpp:547 |
| 모든 버퍼가 완료되지 않았다면 false를 반환합니다. | src/libcamera/pipeline_handler.cpp:547 |
| 마지막 버퍼가 끝나도 요청을 별도로 완료해야 합니다. | src/libcamera/pipeline_handler.cpp:547 |

</details>

<details open>
<summary>절 전체 근거 1개</summary>

- `src/libcamera/pipeline_handler.cpp``L547` 발췌 · [전체 소스 `L547`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L547)

</details>

## <a id="callback-thread"></a>스레드 경계와 동기화

호출자는 `Camera` 상태에 영향을 주는 함수를 호출할 때 필요한 경우 함수 간 동기화를 보장해야 합니다. 파이프라인 핸들러는 `PipelineHandler::completeRequest()`를 `CameraManager` 스레드에서 호출해야 합니다.

<details open>
<summary>절 전체 근거 2개</summary>

- `src/libcamera/camera.cpp``L780` 발췌 · [전체 소스 `L780`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L780)
- `src/libcamera/pipeline_handler.cpp``L571` 발췌 · [전체 소스 `L571`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline_handler.cpp#L571)

</details>

## 정지와 연결 해제를 구분하기

UVC의 정상 버퍼 반환과 STREAMOFF 성공 시 남은 버퍼 취소는 `imageBufferReady`에서 `completeBuffer`와 `completeRequest`를 거쳐 같은 `requestCompleted` 알림으로 이어질 수 있습니다. Developer는 이 슬롯에서 `RequestComplete`와 `RequestCancelled`를 구별하고 버퍼별 `FrameSuccess`로 영상 사용 여부를 판단해야 하며, `RequestComplete`에도 `FrameError`가 있을 수 있고 취소된 버퍼는 `FrameCancelled`입니다. Vendor의 장치 검증 계획은 첫 실행에서 정상 촬영하고 둘째 실행에서 미완료 요청을 남긴 채 `stop()`을 호출하며, 수신 루프를 처리해 제출별 알림 횟수와 미수신 여부, 요청과 버퍼 상태를 기록하는 것입니다. 다른 스레드에 큐잉된 슬롯은 `stop()` 반환 뒤에도 실행될 수 있습니다.

### 촬영을 멈췄는데 왜 완료 알림이 오는가?

```mermaid
flowchart TB
%% sdd:translations {"Camera API: Running 또는 <br/>Stopping에서 <br/>requestCompleted 발행": "Camera API: emit <br/>requestCompleted in Running <br/>or Stopping", "Camera API가 <br/>CameraStopping으로 전환": "Camera API enters <br/>CameraStopping", "Pipeline Handler가 대기열을 <br/>분리하고 장치를 정지": "Pipeline Handler detaches <br/>the waiting queue and stops <br/>the device", "UVC 정지 중 장치에 남은 <br/>버퍼를 FrameCancelled로 반환": "During UVC stop, return <br/>buffers still queued on the <br/>device as FrameCancelled", "UVC 촬영 중 회수한 버퍼: <br/>FrameSuccess 또는 FrameError": "Buffer dequeued during UVC <br/>capture: FrameSuccess or <br/>FrameError", "UVC 핸들러가 버퍼 완료 뒤 <br/>요청 완료를 명시적으로 호출": "UVC handler explicitly <br/>completes the request after <br/>completing the buffer", "UVC의 VIDIOC#95;STREAMOFF 성공": "VIDIOC#95;STREAMOFF succeeds <br/>in UVC", "UVC의 VIDIOC#95;STREAMOFF 실패": "VIDIOC#95;STREAMOFF fails in <br/>UVC", "bufferReady → <br/>imageBufferReady": "bufferReady → <br/>imageBufferReady", "cancelled#95;에 따라 <br/>RequestCancelled 또는 <br/>RequestComplete": "cancelled#95; selects <br/>RequestCancelled or <br/>RequestComplete", "같은 bufferReady 신호": "Same bufferReady signal", "공통 핸들러가 분리했던 대기 <br/>요청을 취소해 완료": "Common handler cancels and <br/>completes the detached <br/>waiting requests", "버퍼 상태를 반영한 뒤 요청 <br/>완료": "Apply the buffer status, <br/>then complete the request", "블로킹 호출": "Blocking invocation", "실행 중이고 접근 검사 통과": "Running and access check <br/>passes", "앱에서 Camera::stop#40;#41; 호출": "App calls Camera::stop#40;#41;", "앱이 요청 상태와 버퍼별 <br/>FrameSuccess 여부를 확인": "App checks request status <br/>and whether each buffer <br/>reports FrameSuccess", "장치 버퍼 반환 루프를 <br/>건너뛰고 오류 반환": "Return an error before the <br/>device-buffer return loop", "장치 정지 호출이 반환한 뒤": "After the device stop call <br/>returns", "제출 순서대로 반환, 선두가 <br/>Pending이면 대기": "Return in submission order; <br/>wait if the head is pending", "취소 표시 후 소프트웨어 <br/>큐에서 완료": "Complete in the software <br/>queue after marking <br/>cancelled", "큐에 들어간 슬롯은 stop#40;#41; <br/>반환 뒤에도 실행 가능": "A queued slot may run after <br/>stop#40;#41; returns"}
  v_app-stop["앱에서 Camera::stop#40;#41; 호출"]
  v_camera-stop["Camera API가 <br/>CameraStopping으로 전환"]
  v_pipe-stop["Pipeline Handler가 대기열을 <br/>분리하고 장치를 정지"]
  v_device-frame["UVC 촬영 중 회수한 버퍼: <br/>FrameSuccess 또는 FrameError"]
  v_streamoff-error["장치 버퍼 반환 루프를 <br/>건너뛰고 오류 반환"]
  v_device-cancel["UVC 정지 중 장치에 남은 <br/>버퍼를 FrameCancelled로 반환"]
  v_uvc-ready["UVC 핸들러가 버퍼 완료 뒤 <br/>요청 완료를 명시적으로 호출"]
  v_waiting-cancel["공통 핸들러가 분리했던 대기 <br/>요청을 취소해 완료"]
  v_request-result["cancelled#95;에 따라 <br/>RequestCancelled 또는 <br/>RequestComplete"]
  v_camera-notify["Camera API: Running 또는 <br/>Stopping에서 <br/>requestCompleted 발행"]
  v_app-result["앱이 요청 상태와 버퍼별 <br/>FrameSuccess 여부를 확인"]
  v_app-stop -->|"실행 중이고 접근 검사 통과"| v_camera-stop
  v_camera-stop -->|"블로킹 호출"| v_pipe-stop
  v_pipe-stop -->|"UVC의 VIDIOC#95;STREAMOFF 성공"| v_device-cancel
  v_pipe-stop -->|"장치 정지 호출이 반환한 뒤"| v_waiting-cancel
  v_pipe-stop -->|"UVC의 VIDIOC#95;STREAMOFF 실패"| v_streamoff-error
  v_device-frame -->|"bufferReady → <br/>imageBufferReady"| v_uvc-ready
  v_device-cancel -->|"같은 bufferReady 신호"| v_uvc-ready
  v_uvc-ready -->|"버퍼 상태를 반영한 뒤 요청 <br/>완료"| v_request-result
  v_waiting-cancel -->|"취소 표시 후 소프트웨어 <br/>큐에서 완료"| v_request-result
  v_request-result -->|"제출 순서대로 반환, 선두가 <br/>Pending이면 대기"| v_camera-notify
  v_camera-notify -->|"큐에 들어간 슬롯은 stop#40;#41; <br/>반환 뒤에도 실행 가능"| v_app-result
```

완료 시 상태 검사는 연결 해제도 허용합니다. Running과 Stopping 범위를 벗어나면 Fatal 로그 경로에 들어갑니다. [`camera.cpp:1483`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L1483) · [`camera.cpp:1486`](https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L1486)

Mermaid 원문

<details open>
<summary>그림 근거와 확인 범위</summary>

정상 촬영과 정지 중 취소가 어떤 경로를 거쳐 같은 완료 신호로 앱에 전달됩니까?

소스 연결 해석 · 자동 연결 검사만 통과 · 의미와 기기 실행은 검증 전

| 요소·전이 | 소스 근거 |
| --- | --- |
| 앱에서 Camera::stop() 호출 | src/libcamera/camera.cpp:1431 |
| Camera API가 CameraStopping으로 전환 | src/libcamera/camera.cpp:1431 |
| Pipeline Handler가 대기열을 분리하고 장치를 정지 | src/libcamera/pipeline_handler.cpp:359 |
| UVC 촬영 중 회수한 버퍼: FrameSuccess 또는 FrameError | src/libcamera/v4l2_videodevice.cpp:1814 |
| 장치 버퍼 반환 루프를 건너뛰고 오류 반환 | src/libcamera/v4l2_videodevice.cpp:2023 |
| UVC 정지 중 장치에 남은 버퍼를 FrameCancelled로 반환 | src/libcamera/v4l2_videodevice.cpp:2023 · include/libcamera/internal/framebuffer.h:36 |
| UVC 핸들러가 버퍼 완료 뒤 요청 완료를 명시적으로 호출 | src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:893 |
| 공통 핸들러가 분리했던 대기 요청을 취소해 완료 | src/libcamera/pipeline_handler.cpp:359 · src/libcamera/pipeline_handler.cpp:483 |
| cancelled\_에 따라 RequestCancelled 또는 RequestComplete | src/libcamera/request.cpp:103 |
| Camera API: Running 또는 Stopping에서 requestCompleted 발행 | src/libcamera/camera.cpp:1481 |
| 앱이 요청 상태와 버퍼별 FrameSuccess 여부를 확인 | src/libcamera/camera.cpp:1481 · src/libcamera/request.cpp:103 · src/libcamera/framebuffer.cpp:40 |
| 실행 중이고 접근 검사 통과 | src/libcamera/camera.cpp:1431 |
| 블로킹 호출 | src/libcamera/camera.cpp:1462 |
| UVC의 VIDIOC_STREAMOFF 성공 | src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:320 · src/libcamera/v4l2_videodevice.cpp:2023 |
| 장치 정지 호출이 반환한 뒤 | src/libcamera/pipeline_handler.cpp:359 |
| UVC의 VIDIOC_STREAMOFF 실패 | src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:320 · src/libcamera/v4l2_videodevice.cpp:2023 |
| bufferReady → imageBufferReady | src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:535 |
| 같은 bufferReady 신호 | src/libcamera/v4l2_videodevice.cpp:2023 · src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:535 |
| 버퍼 상태를 반영한 뒤 요청 완료 | src/libcamera/request.cpp:103 · src/libcamera/pipeline_handler.cpp:547 |
| 취소 표시 후 소프트웨어 큐에서 완료 | src/libcamera/pipeline_handler.cpp:483 |
| 제출 순서대로 반환, 선두가 Pending이면 대기 | src/libcamera/pipeline_handler.cpp:547 |
| 큐에 들어간 슬롯은 stop() 반환 뒤에도 실행 가능 | src/libcamera/camera.cpp:1481 · src/libcamera/base/bound_method.cpp:68 · src/libcamera/camera.cpp:1462 |

</details>

### 정지 API 계약과 연결 해제 TODO

```mermaid
flowchart TB
%% sdd:translations {"Camera::disconnect 알림": "Camera::disconnect <br/>notification", "PipelineHandler::stop 계약": "PipelineHandler::stop <br/>contract", "Running 중 연결 해제 시 <br/>대기 요청 처리: TODO": "Pending requests on <br/>disconnection while <br/>Running: TODO", "계약: 모든 대기 요청 <br/>취소·즉시 오류 완료": "Contract: cancel all <br/>pending requests; <br/>immediately complete in <br/>error", "미완료 TODO를 구분": "Distinguish unfinished TODO", "선택된 핸들러 원문의 계약": "Contract in the selected <br/>handler source"}
  v_stop["PipelineHandler::stop 계약"]
  v_complete["계약: 모든 대기 요청 <br/>취소·즉시 오류 완료"]
  v_disconnect["Camera::disconnect 알림"]
  v_todo["Running 중 연결 해제 시 <br/>대기 요청 처리: TODO"]
  v_stop -->|"선택된 핸들러 원문의 계약"| v_complete
  v_disconnect -->|"미완료 TODO를 구분"| v_todo
```

Mermaid 원문

<details open>
<summary>그림 근거와 확인 범위</summary>

PipelineHandler::stop과 Camera::disconnect의 선택된 두 원문은 대기 요청 처리를 어떻게 다르게 명시합니까?

소스 연결 해석 · 자동 연결 검사만 통과 · 의미와 기기 실행은 검증 전

| 요소·전이 | 소스 근거 |
| --- | --- |
| PipelineHandler::stop 계약 | src/libcamera/pipeline_handler.cpp:359 |
| 계약: 모든 대기 요청 취소·즉시 오류 완료 | src/libcamera/pipeline_handler.cpp:359 |
| Camera::disconnect 알림 | src/libcamera/camera.cpp:944 |
| Running 중 연결 해제 시 대기 요청 처리: TODO | src/libcamera/camera.cpp:944 |
| 선택된 핸들러 원문의 계약 | src/libcamera/pipeline_handler.cpp:359 |
| 미완료 TODO를 구분 | src/libcamera/camera.cpp:944 |

</details>

## 원고와 검토 기록

<details open>
<summary>시스템 개요</summary>

- **생성 방식**: 추출 사실과 LLM 설명
- **검증 범위**: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
- **자동 검사**: 통과 (`ok`). 검사한 항목은 검증 범위에 적혀 있습니다. 설명 내용이 맞는지는 사람이 확인합니다.
- **사람 검토**: 사람 검토 전
- **분석 기준 커밋**: `adfa719f8ed67d18fd8a0739fc088a1f8b9e7252`
- **문서 생성 시각**: `2026-11-20 17:39:13+00:00`
- **문장 생성 모델**: `cli/codex/gpt-6.1-terra`
- **문서 간 계약**: 자동 대조 보고서 · 사람 검토 전
- **독자 범위**: 과업별 답변과 미검토 범위

<details open>
<summary>원고 작성 당시 기록</summary>

원고에 저장된 당시 기록입니다. 현재 문서의 기준과 다를 수 있습니다.

- 근거 파일: `include/libcamera/camera.h`, `include/libcamera/camera_manager.h`, `include/libcamera/internal/ipa_manager.h`, `include/libcamera/internal/pipeline_handler.h`, `include/libcamera/request.h`, `src/libcamera/base/log.cpp`, `src/libcamera/camera.cpp`, `src/libcamera/camera_manager.cpp`, `src/libcamera/controls.cpp`, `src/libcamera/ipa_manager.cpp`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/request.cpp`
- 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `adfa719f8e`)
- 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
- 검토 상태 기록일: 2026-11-21 · 사람 검토 전

</details>

Markdown 원문 ↗ Mermaid 원문 ↗

이전 주소의 상세 내용 열기

</details>

<details open>
<summary>요청 처리와 문제 진단</summary>

- **생성 방식**: 추출 사실과 LLM 설명
- **검증 범위**: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
- **자동 검사**: 통과 (`ok`). 검사한 항목은 검증 범위에 적혀 있습니다. 설명 내용이 맞는지는 사람이 확인합니다.
- **사람 검토**: 사람 검토 전
- **분석 기준 커밋**: `adfa719f8ed67d18fd8a0739fc088a1f8b9e7252`
- **문서 생성 시각**: `2026-11-21 13:28:40+00:00`
- **문장 생성 모델**: `cli/codex/gpt-6.1-terra`
- **문서 간 계약**: 자동 대조 보고서 · 사람 검토 전
- **제품 설명 입력**: 적용 범위·조건·자료

<details open>
<summary>원고 작성 당시 기록</summary>

원고에 저장된 당시 기록입니다. 현재 문서의 기준과 다를 수 있습니다.

- 근거 파일: `Documentation/thread-safety.dox`, `include/libcamera/base/bound_method.h`, `include/libcamera/base/object.h`, `include/libcamera/base/signal.h`, `include/libcamera/base/utils.h`, `include/libcamera/camera.h`, `include/libcamera/internal/camera.h`, `include/libcamera/internal/framebuffer.h`, `include/libcamera/internal/pipeline_handler.h`, `include/libcamera/internal/request.h`, `include/libcamera/request.h`, `product-evidence/libcamera-callback-probe/callback-run.txt`, `src/libcamera/base/bound_method.cpp`, `src/libcamera/base/event_dispatcher_poll.cpp`, `src/libcamera/base/message.cpp`, `src/libcamera/base/object.cpp`, `src/libcamera/base/signal.cpp`, `src/libcamera/base/thread.cpp`, `src/libcamera/base/timer.cpp`, `src/libcamera/camera.cpp`, `src/libcamera/framebuffer.cpp`, `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/request.cpp`, `src/libcamera/v4l2_device.cpp`, `src/libcamera/v4l2_videodevice.cpp`
- 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `adfa719f8e`)
- 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
- 검토 상태 기록일: 2026-11-21 · 사람 검토 전

</details>

Markdown 원문 ↗

이전 주소의 상세 내용 열기

</details>

이 페이지 Markdown 받기 · 독자용 문서의 원본 위치
