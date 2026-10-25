---
generated_at: 2026-10-25T08:20:43+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: overview
generation_method: facts-and-llm
evidence_fingerprint: e69c84c4875e665514c88bde5b0eca4b0cd3b73caf71d87423e27cfe28d54952
semantic_review: human-review-required
agent: response-bundle/codex-session
generated_design: {"schema": 1, "input_fingerprint": "e69c84c4875e665514c88bde5b0eca4b0cd3b73caf71d87423e27cfe28d54952", "answers": {"discovery": [{"text": "처음 읽을 진입점은 `CameraManager`입니다. 장치를 열거하고 파이프라인과 연결하며 애플리케이션에 카메라 접근을 제공합니다. 동시에 하나의 인스턴스만 허용하므로 기존 관리자를 남긴 채 두 번째 관리자를 만들면 안 됩니다.", "covers": ["discovery"], "kind": "behavior", "quote": "The camera manager is the entry point to libcamera. It enumerates devices,\n * associates them with pipeline managers, and provides access to the cameras\n * in the system to applications. The manager owns all Camera objects and\n * handles hot-plugging and hot-unplugging to manage the lifetime of cameras.\n *\n * To interact with libcamera, an application starts by creating a camera\n * manager instance. Only a single instance of the camera manager may exist at\n * a time. Attempting to create a second instance without first deleting the\n * existing instance results in undefined behaviour.\n *\n * The manager is initially stopped,", "evidence": ["manager"]}, {"text": "`CameraManager::start()`는 관리자를 시작하고 시스템의 장치를 열거합니다. 성공을 확인한 뒤 카메라를 조회하고 사용할 수 있으며, 반환값은 성공 시 0, 실패 시 음수 오류 코드입니다.", "covers": ["discovery"], "kind": "behavior", "quote": "\\brief Start the camera manager\n *\n * Start the camera manager and enumerate all devices in the system. Once\n * the start has been confirmed the user is free to list and otherwise\n * interact with cameras in the system until either the camera manager\n * is stopped or the camera is unplugged from the system.\n *\n * \\return 0 on success or a negative error code otherwise\n */\nint CameraManager::start()", "evidence": ["start"]}, {"text": "카메라 목록은 `cameras()`로 얻고 특정 ID는 `get()`으로 찾습니다. 두 함수 모두 스레드 안전성을 명시하지만, 호출자는 관리자가 실행 중임을 보장해야 합니다. `get()`은 해당 카메라를 찾지 못하면 null 포인터를 반환합니다.", "covers": ["discovery"], "kind": "behavior", "quote": "\\fn CameraManager::cameras()\n * \\brief Retrieve all available cameras\n *\n * Before calling this function the caller is responsible for ensuring that\n * the camera manager is running.\n *\n * \\context This function is \\threadsafe.\n *\n * \\return List of all available cameras\n */\nstd::vector<std::shared_ptr<Camera>> CameraManager::cameras() const\n{\n\tconst Private *const d = _d();", "evidence": ["access"]}, {"text": "하드웨어 쪽 진입점은 `PipelineHandler::match()`입니다. 필요한 미디어 장치를 확보하고 카메라를 생성해 관리자에 등록하는 책임을 가집니다. 성공 시 카메라를 내부에 저장하고 `true`를 반환하며, 필요한 장치를 확보하지 못했다면 이미 확보한 장치도 해제하고 `false`를 반환해야 합니다.", "covers": ["discovery"], "kind": "behavior", "quote": "\\fn PipelineHandler::match(DeviceEnumerator *enumerator)\n * \\brief Match media devices and create camera instances\n * \\param[in] enumerator The enumerator providing all media devices found in the\n * system\n *\n * This function is the main entry point of the pipeline handler. It is called\n * by the camera manager with the \\a enumerator passed as an argument. It shall\n * acquire from the \\a enumerator all the media devices it needs for a single\n * pipeline, create one or multiple Camera instances and register them with the\n * camera manager.\n *\n * If all media devices needed by the pipeline handler are found, they must all\n * be acquired by a call to MediaDevice::acquire(). This function shall then\n * create the corresponding Camera instances, store them internally, and return\n * true. Otherwise it shall not acquire any media device (or shall release all\n * the media devices is has acquired by calling MediaDevice::release()) and\n * return false.\n *\n * If multiple instances of a pipeline are available in the system, the\n * PipelineHandler class will be instantiated once per instance, and its match()\n * function called for every instance. Each call shall acquire media devices for\n * one pipeline instance, until all compatible media devices are exhausted.\n *\n * If this function returns true, a new instance of the pipeline handler will\n * be created and its match() function called.\n *\n * \\context This function is called from the CameraManager thread.\n *\n * \\return true if media devices have been acquired and camera instances\n * created, or false otherwise\n */", "evidence": ["match"]}], "responsibility": [{"text": "`Camera`는 하나의 영상 소스에서 나오는 하나 이상의 스트림을 구성하고, 장치를 제어하며 영상을 캡처하는 공개 객체입니다. 시스템에서 카메라를 찾은 뒤 실제 캡처 기능을 따라갈 중심 인터페이스입니다.", "covers": ["responsibility"], "kind": "behavior", "quote": "The Camera class models a camera capable of producing one or more image\n * streams from a single image source. It provides the main interface to\n * configuring and controlling the device, and capturing image streams. It is\n * the central object exposed by libcamera.\n *\n * To support the central nature of Camera objects, libcamera manages the\n * lifetime of camera instances with std::shared_ptr<>. Instances shall be\n * created with the create() function which returns a shared pointer. The\n * Camera constructors and destructor are private, to prevent instances from\n * being constructed and destroyed manually.\n *\n * \\section camera_operation", "evidence": ["camera"]}, {"text": "`Camera` 인스턴스 수명은 `std::shared_ptr`로 관리합니다. 생성은 공유 포인터를 반환하는 `create()` 경로를 사용하며, 생성자와 소멸자는 private이므로 직접 생성·파괴하지 않습니다.", "covers": ["responsibility"], "kind": "behavior", "quote": "The Camera class models a camera capable of producing one or more image\n * streams from a single image source. It provides the main interface to\n * configuring and controlling the device, and capturing image streams. It is\n * the central object exposed by libcamera.\n *\n * To support the central nature of Camera objects, libcamera manages the\n * lifetime of camera instances with std::shared_ptr<>. Instances shall be\n * created with the create() function which returns a shared pointer. The\n * Camera constructors and destructor are private, to prevent instances from\n * being constructed and destroyed manually.\n *\n * \\section camera_operation", "evidence": ["camera"]}], "creation": [{"text": "`Camera::createRequest()`는 버퍼와 파라미터를 채울 빈 요청을 만듭니다. `cookie`는 애플리케이션이 완료 요청과 외부 자원을 연결하는 데 사용하는 값이며 libcamera는 그 의미를 해석하지 않습니다. 함수는 스레드 안전하지만 `Configured` 또는 `Running`에서만 호출할 수 있고, 오류 시 null 포인터를 반환합니다.", "covers": ["creation"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest", "evidence": ["create"]}, {"text": "반환된 요청의 소유권은 호출자에게 있습니다. 애플리케이션은 완료 핸들러에서 요청을 정리하거나, `Request::reuse()`로 상태를 초기화한 뒤 다시 사용할 수 있습니다.", "covers": ["creation"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest", "evidence": ["create"]}], "lifecycle": [{"text": "캡처 준비는 카메라 획득과 구성에서 시작합니다. 그 뒤 카메라를 시작하면 정지할 때까지 요청을 처리할 수 있습니다. 정지는 캡처를 끝내는 단계이고, 카메라 사용 자체가 끝났다면 최종 해제까지 수행해야 합니다.", "covers": ["lifecycle"], "kind": "behavior", "quote": "\\section camera_operation Operating the Camera\n *\n * An application needs to perform a sequence of operations on a camera before\n * it is ready to process requests. The camera needs to be acquired and\n * configured to prepare the camera for capture. Once started the camera can\n * process requests until it is stopped. When an application is done with a\n * camera, the camera needs to be released.\n *\n * An application may start and stop a camera multiple times as long as it is\n * not released. The camera may also be reconfigured.\n *\n * Functions that affect the camera state", "evidence": ["state"]}, {"text": "카메라를 아직 해제하지 않았다면 시작과 정지를 여러 번 반복할 수 있으며 구성도 다시 바꿀 수 있습니다. 캡처 세션을 끝내는 것과 카메라를 더 이상 사용하지 않는 것을 구분하는 기준입니다.", "covers": ["lifecycle"], "kind": "behavior", "quote": "\\section camera_operation Operating the Camera\n *\n * An application needs to perform a sequence of operations on a camera before\n * it is ready to process requests. The camera needs to be acquired and\n * configured to prepare the camera for capture. Once started the camera can\n * process requests until it is stopped. When an application is done with a\n * camera, the camera needs to be released.\n *\n * An application may start and stop a camera multiple times as long as it is\n * not released. The camera may also be reconfigured.\n *\n * Functions that affect the camera state", "evidence": ["state"]}], "request": [{"text": "`Camera::queueRequest()`에 제출할 요청에는 캡처 버퍼가 하나 이상 연결돼 있어야 합니다. 버퍼가 없는 요청은 큐에 넣지 않고 거절합니다. 이 조건은 요청에 버퍼 객체를 연결하라는 뜻이며, 애플리케이션이 버퍼의 촬영 픽셀을 미리 채우라는 뜻은 아닙니다.", "covers": ["request"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest", "evidence": ["queue"]}, {"text": "`queueRequest()`는 스레드 안전하지만 실제 카메라가 `Running`일 때만 호출할 수 있습니다. 성공 반환과 완료 알림은 다르며, 제출한 요청의 완료는 `requestCompleted` 신호로 받습니다.", "covers": ["request"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest", "evidence": ["queue"]}], "completion": [{"text": "`PipelineHandler::completeBuffer()`는 애플리케이션에 버퍼 완료를 알리고 요청 안의 버퍼 추적 상태를 갱신합니다. 모든 버퍼가 끝나면 `true`를 반환하며, 아직 남아 있으면 `false`를 반환합니다.", "covers": ["completion"], "kind": "behavior", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer", "evidence": ["buffer"]}, {"text": "마지막 버퍼가 끝나더라도 요청은 자동 완료되지 않습니다. 파이프라인에 남은 후처리를 수행할 기회를 주기 위한 계약이며, 핸들러는 `completeRequest()`를 명시적으로 호출해 요청 완료를 알려야 합니다.", "covers": ["completion"], "kind": "behavior", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer", "evidence": ["buffer"]}], "boundary": [{"text": "카메라 상태를 바꾸는 함수들은 일반적으로 `Camera`가 서로 동기화하지 않습니다. 필요한 동기화는 호출자의 책임이므로, 개별 API의 스레드 안전성과 상태 전환 전체의 동기화는 구분해야 합니다.", "covers": ["boundary"], "kind": "behavior", "quote": "Functions that affect the camera state as defined below are generally not\n * synchronized with each other by the Camera class. The caller is responsible\n * for ensuring their synchronization if necessary.\n *\n * \\subsection Camera States", "evidence": ["synchronization"]}, {"text": "`PipelineHandler::completeRequest()`는 `CameraManager` 스레드에서 호출하는 계약입니다. 완료 요청의 호출 순서는 자유롭지만 애플리케이션에는 제출 순서대로 반환하며, 함수 반환 뒤 핸들러는 해당 요청에 접근하면 안 됩니다. 이 함수의 실행 문맥을 모든 콜백의 실행 스레드로 확대하면 안 됩니다.", "covers": ["boundary"], "kind": "behavior", "quote": "\\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest", "evidence": ["completion"]}], "verification": [{"text": "`Camera::start()`는 `Configured`에서 호출하며, 다른 상태 변경 함수와의 동기화는 호출자가 책임집니다. 선택적인 제어 목록을 시작 전에 적용할 수 있고, 성공 이후에는 `stop()`으로 세션을 끝낼 때까지 요청을 제출할 수 있습니다.", "covers": ["verification"], "kind": "behavior", "quote": "\\brief Start capture from camera\n * \\param[in] controls Controls to be applied before starting the Camera\n *\n * Start the camera capture session, optionally providing a list of controls to\n * apply before starting. Once the camera is started the application can queue\n * requests to the camera to process and return to the application until the\n * capture session is terminated with \\a stop().\n *\n * \\context This function may only be called when the camera is in the\n * Configured state as defined in \\ref camera_operation, and shall be\n * synchronized by the caller with other functions that affect the camera\n * state.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not in a state where it can be started\n */\nint Camera::start", "evidence": ["start"]}, {"text": "`Camera` 클래스 주석에는 시작 시점에 핸들러가 무엇을 해야 하는지 타이밍 문서를 보강하라는 TODO가 남아 있습니다. 이는 시작 타이밍 문서의 한계이며, 시작 기능 전체가 구현되지 않았다는 뜻은 아닙니다.", "covers": ["verification"], "kind": "limitation", "quote": "\\todo Add documentation for camera start timings. What exactly does the\n * camera expect the pipeline handler to do when start() is called?\n *\n * The Camera class models a camera", "evidence": ["timing"]}]}, "topic_inputs": {"discovery": "fccea5aab48ca68e1140d6de23b8305a9e81a487f82a08e8bd5ef6132b40977a", "responsibility": "71a5fee0f5bc0a1eb0b3211eefb100a245a9dbfebad96d46b29e2f6958780080", "creation": "9ac5c82d24b0c1132d8d5328f763557644ff27358f845c80098c6aea0aa0c6dc", "lifecycle": "5052e8bb7b19701b884ff2b721bb41f312be6323b067f55652873bcbf6d54dfe", "request": "89187c8e6122f75ed7ea19a4ff1725859cc6b8e9b02c87ccdbe6eba13f3c64b5", "completion": "142470276f7aa2e79788f6aa5cbb6f9e35617b7165f77dd02b259d4bdfc0d450", "boundary": "6ed25b7e273b61554cb1465ba24200a6ee23e0eb8fd3fe807bb14c056f245d81", "verification": "255f1b4f2890f24adab4dc2a091df5a50751882248423f84769efb7634defcc2"}, "reused_topics": ["discovery", "responsibility", "creation", "lifecycle", "request", "completion", "boundary", "verification"], "generated_topics": [], "topic_agents": {"discovery": "response-bundle/codex-session", "responsibility": "response-bundle/codex-session", "creation": "response-bundle/codex-session", "lifecycle": "response-bundle/codex-session", "request": "response-bundle/codex-session", "completion": "response-bundle/codex-session", "boundary": "response-bundle/codex-session", "verification": "response-bundle/codex-session"}, "body_sha256": "c2209db87de64a015297f19fa026005242b965dfdf7bd317fefb17db34adde6d"}
---

# 시스템 개요

**src/libcamera/camera_manager.cpp의 CameraManager에서 시작해 요청 제출과 완료를 따라가세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 처음 읽을 파일과 진입점을 찾습니다. | [탐색과 파이프라인 선택](#탐색과-파이프라인-선택) |
| 요청과 결과가 지나는 경계를 확인합니다. | [요청 제출과 완료](#요청-제출과-완료) |
| 구성 실패의 원인을 좁힙니다. | [요청 처리와 문제 진단](request-lifecycle.md#구성-실패를-좁히는-순서) |
| 완료가 오지 않는 요청을 조사합니다. | [요청 처리와 문제 진단](request-lifecycle.md) |
| 수정 전에 상태와 종료 순서를 확인합니다. | [캡처 세션의 상태와 자원](#캡처-세션의-상태와-자원) |
| 전체 클래스와 패키지를 찾습니다. | [구성 요소 색인](component-index.md) |

## 탐색과 파이프라인 선택

처음 읽을 진입점은 `CameraManager`입니다. 장치를 열거하고 파이프라인과 연결하며 애플리케이션에 카메라 접근을 제공합니다. 동시에 하나의 인스턴스만 허용하므로 기존 관리자를 남긴 채 두 번째 관리자를 만들면 안 됩니다. `src/libcamera/camera_manager.cpp:283`

<!-- sdd:visual:discovery-map -->
### 장치 탐색에서 Camera 접근까지

장치 매칭과 등록의 책임을 따라가세요. 그림은 책임 연결이며 전체 호출 순서나 실행 시간을 나타내지 않습니다.

```mermaid
flowchart TB
%% sdd:translations {"Camera 생성·등록": "Create and register Camera", "CameraManager 진입점": "CameraManager entry", "PipelineHandler::match()": "PipelineHandler::match()", "start()": "start()", "열거자를 전달해 장치를 매칭": "Pass enumerator to match devices", "장치 열거": "Enumerate devices", "필요한 장치를 확보한 경우": "When required devices are acquired"}
  v_manager["CameraManager 진입점"]
  v_enumerate["장치 열거"]
  v_handler["PipelineHandler::match()"]
  v_camera["Camera 생성·등록"]
  v_manager -->|"start()"| v_enumerate
  v_enumerate -->|"열거자를 전달해 장치를 매칭"| v_handler
  v_handler -->|"필요한 장치를 확보한 경우"| v_camera
```

[Mermaid 원문](overview.discovery-map.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | CameraManager 진입점 | [src/libcamera/camera_manager.cpp:283](#source-f75d22cf73f3402d) |
    | 장치 열거 | [src/libcamera/camera_manager.cpp:329](#source-f58d94d893e03971) |
    | PipelineHandler::match() | [src/libcamera/pipeline_handler.cpp:86](#source-5bbd41c1e725138c) |
    | Camera 생성·등록 | [src/libcamera/pipeline_handler.cpp:86](#source-5bbd41c1e725138c) |
    | start() | [src/libcamera/camera_manager.cpp:329](#source-f58d94d893e03971) |
    | 열거자를 전달해 장치를 매칭 | [src/libcamera/pipeline_handler.cpp:86](#source-5bbd41c1e725138c) |
    | 필요한 장치를 확보한 경우 | [src/libcamera/pipeline_handler.cpp:86](#source-5bbd41c1e725138c) |
<!-- /sdd:visual:discovery-map -->

`CameraManager::start()`는 관리자를 시작하고 시스템의 장치를 열거합니다. 성공을 확인한 뒤 카메라를 조회하고 사용할 수 있으며, 반환값은 성공 시 0, 실패 시 음수 오류 코드입니다. `src/libcamera/camera_manager.cpp:329`

카메라 목록은 `cameras()`로 얻고 특정 ID는 `get()`으로 찾습니다. 두 함수 모두 스레드 안전성을 명시하지만, 호출자는 관리자가 실행 중임을 보장해야 합니다. `get()`은 해당 카메라를 찾지 못하면 null 포인터를 반환합니다. `src/libcamera/camera_manager.cpp:368`

하드웨어 쪽 진입점은 `PipelineHandler::match()`입니다. 필요한 미디어 장치를 확보하고 카메라를 생성해 관리자에 등록하는 책임을 가집니다. 성공 시 카메라를 내부에 저장하고 `true`를 반환하며, 필요한 장치를 확보하지 못했다면 이미 확보한 장치도 해제하고 `false`를 반환해야 합니다. `src/libcamera/pipeline_handler.cpp:86`

근거 원문: [src/libcamera/camera_manager.cpp:283](#source-f75d22cf73f3402d) · [src/libcamera/camera_manager.cpp:329](#source-f58d94d893e03971) · [src/libcamera/camera_manager.cpp:368](#source-0c733673790ad84f) · [src/libcamera/pipeline_handler.cpp:86](#source-5bbd41c1e725138c)

## 컴포넌트별 책임

`Camera`는 하나의 영상 소스에서 나오는 하나 이상의 스트림을 구성하고, 장치를 제어하며 영상을 캡처하는 공개 객체입니다. 시스템에서 카메라를 찾은 뒤 실제 캡처 기능을 따라갈 중심 인터페이스입니다. `src/libcamera/camera.cpp:758`

`Camera` 인스턴스 수명은 `std::shared_ptr`로 관리합니다. 생성은 공유 포인터를 반환하는 `create()` 경로를 사용하며, 생성자와 소멸자는 private이므로 직접 생성·파괴하지 않습니다. `src/libcamera/camera.cpp:758`

근거 원문: [src/libcamera/camera.cpp:758](#source-6c066281dcce33d6)

## 요청 생성과 소유권

`Camera::createRequest()`는 버퍼와 파라미터를 채울 빈 요청을 만듭니다. `cookie`는 애플리케이션이 완료 요청과 외부 자원을 연결하는 데 사용하는 값이며 libcamera는 그 의미를 해석하지 않습니다. 함수는 스레드 안전하지만 `Configured` 또는 `Running`에서만 호출할 수 있고, 오류 시 null 포인터를 반환합니다. `src/libcamera/camera.cpp:1243`

반환된 요청의 소유권은 호출자에게 있습니다. 애플리케이션은 완료 핸들러에서 요청을 정리하거나, `Request::reuse()`로 상태를 초기화한 뒤 다시 사용할 수 있습니다. `src/libcamera/camera.cpp:1243`

근거 원문: [src/libcamera/camera.cpp:1243](#source-d61960ed2545ba78)

## 캡처 세션의 상태와 자원

캡처 준비는 카메라 획득과 구성에서 시작합니다. 그 뒤 카메라를 시작하면 정지할 때까지 요청을 처리할 수 있습니다. 정지는 캡처를 끝내는 단계이고, 카메라 사용 자체가 끝났다면 최종 해제까지 수행해야 합니다. `src/libcamera/camera.cpp:769`

카메라를 아직 해제하지 않았다면 시작과 정지를 여러 번 반복할 수 있으며 구성도 다시 바꿀 수 있습니다. 캡처 세션을 끝내는 것과 카메라를 더 이상 사용하지 않는 것을 구분하는 기준입니다. `src/libcamera/camera.cpp:769`

근거 원문: [src/libcamera/camera.cpp:769](#source-04f354bc331ec5c1)

## 요청 제출과 완료

`Camera::queueRequest()`에 제출할 요청에는 캡처 버퍼가 하나 이상 연결돼 있어야 합니다. 버퍼가 없는 요청은 큐에 넣지 않고 거절합니다. 이 조건은 요청에 버퍼 객체를 연결하라는 뜻이며, 애플리케이션이 버퍼의 촬영 픽셀을 미리 채우라는 뜻은 아닙니다. `src/libcamera/camera.cpp:1308`

<!-- sdd:visual:submission-completion -->
### 접수 성공과 촬영 완료는 다른 시점

queueRequest()의 0 반환은 접수 결과입니다. 요청 완료는 별도의 requestCompleted 신호로 확인합니다.

```mermaid
flowchart TB
%% sdd:translations {"0 반환: 접수 성공": "Return 0: submission accepted", "Running 상태에서 제출": "Submit in Running state", "queueRequest()": "queueRequest()", "requestCompleted 신호": "requestCompleted signal", "버퍼를 연결한 Request": "Request with capture buffers", "접수 결과를 반환": "Return submission result", "촬영 완료는 별도로 통지": "Notify completion separately"}
  v_request["버퍼를 연결한 Request"]
  v_queue["queueRequest()"]
  v_accepted["0 반환: 접수 성공"]
  v_signal["requestCompleted 신호"]
  v_request -->|"Running 상태에서 제출"| v_queue
  v_queue -->|"접수 결과를 반환"| v_accepted
  v_queue -->|"촬영 완료는 별도로 통지"| v_signal
```

[Mermaid 원문](overview.submission-completion.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | 버퍼를 연결한 Request | [src/libcamera/camera.cpp:1308](#source-2f880c124115c9c4) |
    | queueRequest() | [src/libcamera/camera.cpp:1308](#source-2f880c124115c9c4) |
    | 0 반환: 접수 성공 | [src/libcamera/camera.cpp:1308](#source-2f880c124115c9c4) |
    | requestCompleted 신호 | [src/libcamera/camera.cpp:1308](#source-2f880c124115c9c4) |
    | Running 상태에서 제출 | [src/libcamera/camera.cpp:1308](#source-2f880c124115c9c4) |
    | 접수 결과를 반환 | [src/libcamera/camera.cpp:1308](#source-2f880c124115c9c4) |
    | 촬영 완료는 별도로 통지 | [src/libcamera/camera.cpp:1308](#source-2f880c124115c9c4) |
<!-- /sdd:visual:submission-completion -->

`queueRequest()`는 스레드 안전하지만 실제 카메라가 `Running`일 때만 호출할 수 있습니다. 성공 반환과 완료 알림은 다르며, 제출한 요청의 완료는 `requestCompleted` 신호로 받습니다. `src/libcamera/camera.cpp:1308`

근거 원문: [src/libcamera/camera.cpp:1308](#source-2f880c124115c9c4)

## 버퍼 완료와 요청 완료

`PipelineHandler::completeBuffer()`는 애플리케이션에 버퍼 완료를 알리고 요청 안의 버퍼 추적 상태를 갱신합니다. 모든 버퍼가 끝나면 `true`를 반환하며, 아직 남아 있으면 `false`를 반환합니다. `src/libcamera/pipeline_handler.cpp:547`

마지막 버퍼가 끝나더라도 요청은 자동 완료되지 않습니다. 파이프라인에 남은 후처리를 수행할 기회를 주기 위한 계약이며, 핸들러는 `completeRequest()`를 명시적으로 호출해 요청 완료를 알려야 합니다. `src/libcamera/pipeline_handler.cpp:547`

근거 원문: [src/libcamera/pipeline_handler.cpp:547](#source-ca3f659653ce3f6a)

## 스레드 경계와 동기화

카메라 상태를 바꾸는 함수들은 일반적으로 `Camera`가 서로 동기화하지 않습니다. 필요한 동기화는 호출자의 책임이므로, 개별 API의 스레드 안전성과 상태 전환 전체의 동기화는 구분해야 합니다. `src/libcamera/camera.cpp:780`

`PipelineHandler::completeRequest()`는 `CameraManager` 스레드에서 호출하는 계약입니다. 완료 요청의 호출 순서는 자유롭지만 애플리케이션에는 제출 순서대로 반환하며, 함수 반환 뒤 핸들러는 해당 요청에 접근하면 안 됩니다. 이 함수의 실행 문맥을 모든 콜백의 실행 스레드로 확대하면 안 됩니다. `src/libcamera/pipeline_handler.cpp:571`

근거 원문: [src/libcamera/camera.cpp:780](#source-33ababe2a4780075) · [src/libcamera/pipeline_handler.cpp:571](#source-7ac40780a56ae3a9)

## 정적 근거의 확인 범위

`Camera::start()`는 `Configured`에서 호출하며, 다른 상태 변경 함수와의 동기화는 호출자가 책임집니다. 선택적인 제어 목록을 시작 전에 적용할 수 있고, 성공 이후에는 `stop()`으로 세션을 끝낼 때까지 요청을 제출할 수 있습니다. `src/libcamera/camera.cpp:1383`

실행 확인 항목: `Camera` 클래스 주석에는 시작 시점에 핸들러가 무엇을 해야 하는지 타이밍 문서를 보강하라는 TODO가 남아 있습니다. 이는 시작 타이밍 문서의 한계이며, 시작 기능 전체가 구현되지 않았다는 뜻은 아닙니다. `src/libcamera/camera.cpp:755`

근거 원문: [src/libcamera/camera.cpp:1383](#source-9fe53bb2bee0d8b7) · [src/libcamera/camera.cpp:755](#source-6874d2b69bd02915)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | Camera는 어떤 공개 기능과 객체 수명 계약을 제공합니까? | [컴포넌트별 책임](#컴포넌트별-책임) | 코드 근거와 설명 연결 |
    | 어느 파일과 진입점부터 읽고, 장치 탐색과 카메라 접근은 어떤 순서로 이어집니까? | [탐색과 파이프라인 선택](#탐색과-파이프라인-선택) | 코드 근거와 설명 연결 |
    | 요청 생성의 조건과 소유권·재사용 계약은 무엇입니까? | [요청 생성과 소유권](#요청-생성과-소유권) | 코드 근거와 설명 연결 |
    | 캡처를 준비하고 반복하고 끝내는 순서는 무엇입니까? | [캡처 세션의 상태와 자원](#캡처-세션의-상태와-자원) | 코드 근거와 설명 연결 |
    | 요청을 어떤 조건으로 제출하고 완료를 어떻게 통지받습니까? | [요청 제출과 완료](#요청-제출과-완료) | 코드 근거와 설명 연결 |
    | 버퍼 완료와 요청 완료는 어떻게 구분합니까? | [버퍼 완료와 요청 완료](#버퍼-완료와-요청-완료) | 코드 근거와 설명 연결 |
    | 상태 변경의 동기화 책임과 요청 완료의 실행 스레드는 무엇입니까? | [스레드 경계와 동기화](#스레드-경계와-동기화) | 코드 근거와 설명 연결 |
    | 시작 API의 명시된 계약과 아직 문서화되지 않은 타이밍은 무엇입니까? | [정적 근거의 확인 범위](#정적-근거의-확인-범위) | 코드 근거와 설명 연결 · 실행 확인 항목 별도 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-f75d22cf73f3402d"></a>

??? note "소스 근거: src/libcamera/camera_manager.cpp:283"
    `src/libcamera/camera_manager.cpp:283`에서 시작하는 발췌입니다. 종료 줄은 293이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `6c52c603a60f0faf8c931e6c1691d951484c4915ef9ab8ac67cc65d89acbb550`
    
    ```text
    The camera manager is the entry point to libcamera. It enumerates devices,
     * associates them with pipeline managers, and provides access to the cameras
     * in the system to applications. The manager owns all Camera objects and
     * handles hot-plugging and hot-unplugging to manage the lifetime of cameras.
     *
     * To interact with libcamera, an application starts by creating a camera
     * manager instance. Only a single instance of the camera manager may exist at
     * a time. Attempting to create a second instance without first deleting the
     * existing instance results in undefined behaviour.
     *
     * The manager is initially stopped,
    ```

<a id="source-f58d94d893e03971"></a>

??? note "소스 근거: src/libcamera/camera_manager.cpp:329"
    `src/libcamera/camera_manager.cpp:329`에서 시작하는 발췌입니다. 종료 줄은 338이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `5c647185035857e55de76a49cffad27bfac087260af8577a43cc2611196e3c17`
    
    ```text
    \brief Start the camera manager
     *
     * Start the camera manager and enumerate all devices in the system. Once
     * the start has been confirmed the user is free to list and otherwise
     * interact with cameras in the system until either the camera manager
     * is stopped or the camera is unplugged from the system.
     *
     * \return 0 on success or a negative error code otherwise
     */
    int CameraManager::start()
    ```

<a id="source-0c733673790ad84f"></a>

??? note "소스 근거: src/libcamera/camera_manager.cpp:368"
    `src/libcamera/camera_manager.cpp:368`에서 시작하는 발췌입니다. 종료 줄은 398이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `756e463ef09b825d17af3fc8b7d9912349d46cc84446a0e0c3e9c48fb22d56b6`
    
    ```text
    \fn CameraManager::cameras()
     * \brief Retrieve all available cameras
     *
     * Before calling this function the caller is responsible for ensuring that
     * the camera manager is running.
     *
     * \context This function is \threadsafe.
     *
     * \return List of all available cameras
     */
    std::vector<std::shared_ptr<Camera>> CameraManager::cameras() const
    {
    	const Private *const d = _d();
    
    	MutexLocker locker(d->mutex_);
    
    	return d->cameras_;
    }
    
    /**
     * \brief Get a camera based on ID
     * \param[in] id ID of camera to get
     *
     * Before calling this function the caller is responsible for ensuring that
     * the camera manager is running.
     *
     * \context This function is \threadsafe.
     *
     * \return Shared pointer to Camera object or nullptr if camera not found
     */
    std::shared_ptr<Camera> CameraManager::get(std::string_view id)
    ```

<a id="source-5bbd41c1e725138c"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:86"
    `src/libcamera/pipeline_handler.cpp:86`에서 시작하는 발췌입니다. 종료 줄은 119이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `7dde6563cf6bda32f38f4c1fb3ef0443502432236a0222d4f811b3fa71f3fc05`
    
    ```text
    \fn PipelineHandler::match(DeviceEnumerator *enumerator)
     * \brief Match media devices and create camera instances
     * \param[in] enumerator The enumerator providing all media devices found in the
     * system
     *
     * This function is the main entry point of the pipeline handler. It is called
     * by the camera manager with the \a enumerator passed as an argument. It shall
     * acquire from the \a enumerator all the media devices it needs for a single
     * pipeline, create one or multiple Camera instances and register them with the
     * camera manager.
     *
     * If all media devices needed by the pipeline handler are found, they must all
     * be acquired by a call to MediaDevice::acquire(). This function shall then
     * create the corresponding Camera instances, store them internally, and return
     * true. Otherwise it shall not acquire any media device (or shall release all
     * the media devices is has acquired by calling MediaDevice::release()) and
     * return false.
     *
     * If multiple instances of a pipeline are available in the system, the
     * PipelineHandler class will be instantiated once per instance, and its match()
     * function called for every instance. Each call shall acquire media devices for
     * one pipeline instance, until all compatible media devices are exhausted.
     *
     * If this function returns true, a new instance of the pipeline handler will
     * be created and its match() function called.
     *
     * \context This function is called from the CameraManager thread.
     *
     * \return true if media devices have been acquired and camera instances
     * created, or false otherwise
     */
    
    /**
     * \brief Search and acquire a MediaDevice
    ```

<a id="source-6c066281dcce33d6"></a>

??? note "소스 근거: src/libcamera/camera.cpp:758"
    `src/libcamera/camera.cpp:758`에서 시작하는 발췌입니다. 종료 줄은 769이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e77cee469b7c57430e4bd4b0f08493289c46b57549873521c476df388d591dc2`
    
    ```text
    The Camera class models a camera capable of producing one or more image
     * streams from a single image source. It provides the main interface to
     * configuring and controlling the device, and capturing image streams. It is
     * the central object exposed by libcamera.
     *
     * To support the central nature of Camera objects, libcamera manages the
     * lifetime of camera instances with std::shared_ptr<>. Instances shall be
     * created with the create() function which returns a shared pointer. The
     * Camera constructors and destructor are private, to prevent instances from
     * being constructed and destroyed manually.
     *
     * \section camera_operation
    ```

<a id="source-d61960ed2545ba78"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1243"
    `src/libcamera/camera.cpp:1243`에서 시작하는 발췌입니다. 종료 줄은 1263이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e71b8c0bea6263314881525ebf4714628591079745c9453624d3f4c3dffe31d0`
    
    ```text
    \brief Create a request object for the camera
     * \param[in] cookie Opaque cookie for application use
     *
     * This function creates an empty request for the application to fill with
     * buffers and parameters, and queue for capture.
     *
     * The \a cookie is stored in the request and is accessible through the
     * Request::cookie() function at any time. It is typically used by applications
     * to map the request to an external resource in the request completion
     * handler, and is completely opaque to libcamera.
     *
     * The ownership of the returned request is passed to the caller, which is
     * responsible for deleting it. The request may be deleted in the completion
     * handler, or reused after resetting its state with Request::reuse().
     *
     * \context This function is \threadsafe. It may only be called when the camera
     * is in the Configured or Running state as defined in \ref camera_operation.
     *
     * \return A pointer to the newly created request, or nullptr on error
     */
    std::unique_ptr<Request> Camera::createRequest
    ```

<a id="source-04f354bc331ec5c1"></a>

??? note "소스 근거: src/libcamera/camera.cpp:769"
    `src/libcamera/camera.cpp:769`에서 시작하는 발췌입니다. 종료 줄은 780이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `73164878543e86e16cf4e3197648ec4e79819beaad2f1c8754260715f65b8333`
    
    ```text
    \section camera_operation Operating the Camera
     *
     * An application needs to perform a sequence of operations on a camera before
     * it is ready to process requests. The camera needs to be acquired and
     * configured to prepare the camera for capture. Once started the camera can
     * process requests until it is stopped. When an application is done with a
     * camera, the camera needs to be released.
     *
     * An application may start and stop a camera multiple times as long as it is
     * not released. The camera may also be reconfigured.
     *
     * Functions that affect the camera state
    ```

<a id="source-2f880c124115c9c4"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1308"
    `src/libcamera/camera.cpp:1308`에서 시작하는 발췌입니다. 종료 줄은 1330이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `b24af43d2f808f81b527cf4ee8915451be675f43f877bac5e6edfe69ff3739d6`
    
    ```text
    \brief Queue a request to the camera
     * \param[in] request The request to queue to the camera
     *
     * This function queues a \a request to the camera for capture.
     *
     * After allocating the request with createRequest(), the application shall
     * fill it with at least one capture buffer before queuing it. Requests that
     * contain no buffers are invalid and are rejected without being queued.
     *
     * Once the request has been queued, the camera will notify its completion
     * through the \ref requestCompleted signal.
     *
     * \context This function is \threadsafe. It may only be called when the camera
     * is in the Running state as defined in \ref camera_operation.
     *
     * \return 0 on success or a negative error code otherwise
     * \retval -ENODEV The camera has been disconnected from the system
     * \retval -EACCES The camera is not running so requests can't be queued
     * \retval -EXDEV The request does not belong to this camera
     * \retval -EINVAL The request is invalid
     * \retval -ENOMEM No buffer memory was available to handle the request
     */
    int Camera::queueRequest
    ```

<a id="source-ca3f659653ce3f6a"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:547"
    `src/libcamera/pipeline_handler.cpp:547`에서 시작하는 발췌입니다. 종료 줄은 563이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `49b0139e3f0f620c0a3c044caf699179753dddf1b896d48de417c338bbae6a22`
    
    ```text
    \brief Complete a buffer for a request
     * \param[in] request The request the buffer belongs to
     * \param[in] buffer The buffer that has completed
     *
     * This function shall be called by pipeline handlers to signal completion of
     * the \a buffer part of the \a request. It notifies applications of buffer
     * completion and updates the request's internal buffer tracking. The request
     * is not completed automatically when the last buffer completes to give
     * pipeline handlers a chance to perform any operation that may still be
     * needed. They shall complete requests explicitly with completeRequest().
     *
     * \context This function shall be called from the CameraManager thread.
     *
     * \return True if all buffers contained in the request have completed, false
     * otherwise
     */
    bool PipelineHandler::completeBuffer
    ```

<a id="source-33ababe2a4780075"></a>

??? note "소스 근거: src/libcamera/camera.cpp:780"
    `src/libcamera/camera.cpp:780`에서 시작하는 발췌입니다. 종료 줄은 784이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `943831ed5cf08179455c41bd83a649d74d2a4a2d53f153cfa83dbeff179c2bf6`
    
    ```text
    Functions that affect the camera state as defined below are generally not
     * synchronized with each other by the Camera class. The caller is responsible
     * for ensuring their synchronization if necessary.
     *
     * \subsection Camera States
    ```

<a id="source-7ac40780a56ae3a9"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:571"
    `src/libcamera/pipeline_handler.cpp:571`에서 시작하는 발췌입니다. 종료 줄은 584이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `25903b4c6a305017b96bfe9117fe2b7b917b51fbeb2fd21139700b1fbf6a4fe2`
    
    ```text
    \brief Signal request completion
     * \param[in] request The request that has completed
     *
     * The pipeline handler shall call this function to notify the \a camera that
     * the request has completed. The request is no longer managed by the pipeline
     * handler and shall not be accessed once this function returns.
     *
     * This function ensures that requests will be returned to the application in
     * submission order, the pipeline handler may call it on any complete request
     * without any ordering constraint.
     *
     * \context This function shall be called from the CameraManager thread.
     */
    void PipelineHandler::completeRequest
    ```

<a id="source-9fe53bb2bee0d8b7"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1383"
    `src/libcamera/camera.cpp:1383`에서 시작하는 발췌입니다. 종료 줄은 1400이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `3b6dec3d3372dc891ac15cca8f5c578ab56f76a0321a113a64f10a25f830283d`
    
    ```text
    \brief Start capture from camera
     * \param[in] controls Controls to be applied before starting the Camera
     *
     * Start the camera capture session, optionally providing a list of controls to
     * apply before starting. Once the camera is started the application can queue
     * requests to the camera to process and return to the application until the
     * capture session is terminated with \a stop().
     *
     * \context This function may only be called when the camera is in the
     * Configured state as defined in \ref camera_operation, and shall be
     * synchronized by the caller with other functions that affect the camera
     * state.
     *
     * \return 0 on success or a negative error code otherwise
     * \retval -ENODEV The camera has been disconnected from the system
     * \retval -EACCES The camera is not in a state where it can be started
     */
    int Camera::start
    ```

<a id="source-6874d2b69bd02915"></a>

??? note "소스 근거: src/libcamera/camera.cpp:755"
    `src/libcamera/camera.cpp:755`에서 시작하는 발췌입니다. 종료 줄은 758이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `fe1cde84836279cf75402cca5392d528cc43c3eff36066e3beb4822b75329a46`
    
    ```text
    \todo Add documentation for camera start timings. What exactly does the
     * camera expect the pipeline handler to do when start() is called?
     *
     * The Camera class models a camera
    ```


<!-- sdd:class-diagram -->
## 클래스 관계

화살표의 글자는 추출한 관계를 나타내며, 점선은 상속입니다. 화살표는 참조 대상 또는 기반 클래스를 향합니다. 호출 순서를 뜻하지 않습니다.

```mermaid
flowchart LR
  c0["Camera"]
  c1["CameraManager"]
  c2["Extensible"]:::context
  c3["IPAManager"]
  c4["Object"]:::context
  c5["PipelineHandler"]
  c6["Request"]
  c0 -.->|상속| c2
  c0 -.->|상속| c4
  c1 -.->|상속| c2
  c1 -.->|상속| c4
  c3 -->|필드 참조| c1
  c5 -->|필드 참조| c0
  c5 -->|필드 참조| c1
  c5 -.->|상속| c4
  c6 -.->|상속| c2
  classDef context fill:#fafafa,stroke:#aaa,stroke-dasharray:4 3,color:#555
```
<!-- /sdd:class-diagram -->



## 선택한 시나리오의 코드 읽기 순서

1. 진입점 `Camera::queueRequest(Request *)`의 입력 검사와 반환 조건을 확인합니다.
2. [요청 제출 (Camera::queueRequest)](scenarios/queue_request.md)에서 주요 호출과 추적 경계를 확인합니다.
3. 예약된 호출과 완료 통지를 구분하고, 실행 스레드는 연결 코드와 대조합니다.

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `include/libcamera/camera.h`, `include/libcamera/camera_manager.h`, `include/libcamera/internal/ipa_manager.h`, `include/libcamera/internal/pipeline_handler.h`, `include/libcamera/request.h`, `src/libcamera/base/log.cpp`, `src/libcamera/camera.cpp`, `src/libcamera/camera_manager.cpp`, `src/libcamera/controls.cpp`, `src/libcamera/ipa_manager.cpp`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/request.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `2c4b67c079`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-25 · 사람 검토 전

다음 단계: [카메라와 요청 모델](camera-model.md)
