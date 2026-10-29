---
generated_at: 2026-10-29T20:32:14+00:00
source_commit: 212c689fcf2450bbfbaab25c7472895ac277b5d6
status: ok
section: camera-model
generation_method: facts-and-llm
evidence_fingerprint: 304cbaa27c6fb771a0d3b02507f627ef6dd702a58c713e5af9ce170a85f2bb82
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "304cbaa27c6fb771a0d3b02507f627ef6dd702a58c713e5af9ce170a85f2bb82", "answers": {"responsibility": [{"text": "`CameraManager`는 libcamera의 진입점으로, 장치를 열거하고 파이프라인 관리자와 연결하며 애플리케이션에 카메라를 제공합니다. 관리자는 모든 `Camera` 객체를 소유하고 핫플러그와 핫언플러그를 처리해 카메라의 수명을 관리합니다. 애플리케이션은 관리자 인스턴스를 만들고 `start()`를 호출해야 합니다. 관리자는 처음에 정지 상태이며, 시작하면 시스템의 카메라를 열거하여 `list()`와 `get()`으로 접근할 수 있습니다.", "evidence": ["manager"], "covers": ["responsibility"], "kind": "behavior", "quote": "\\class CameraManager\n * \\brief Provide access and manage all cameras in the system\n *\n * The camera manager is the entry point to libcamera. It enumerates devices,\n * associates them with pipeline managers, and provides access to the cameras\n * in the system to applications. The manager owns all Camera objects and\n * handles hot-plugging and hot-unplugging to manage the lifetime of cameras.\n *\n * To interact with libcamera, an application starts by creating a camera\n * manager instance. Only a single instance of the camera manager may exist at\n * a time. Attempting to create a second instance without first deleting the\n * existing instance results in undefined behaviour.\n *\n * The manager is initially stopped, and shall be started with start(). This\n * will enumerate all the cameras present in the system, which can then be\n * listed with list() and retrieved with get().\n *\n * Cameras are shared through std::shared_ptr<>, ensuring that a camera will\n * stay valid until the last reference is released without requiring any special\n * action from the application. Once the application has released all the\n * references it held to cameras, the camera manager can be stopped with\n * stop().\n */"}, {"text": "한 번에 `CameraManager` 인스턴스는 하나만 존재할 수 있으며, 기존 인스턴스를 삭제하기 전에 두 번째 인스턴스를 만들면 동작이 정의되지 않습니다. 카메라는 `std::shared_ptr<>`로 공유되며 마지막 참조가 해제될 때까지 유효합니다. 애플리케이션이 보유한 모든 카메라 참조를 해제한 뒤에는 `stop()`으로 관리자를 정지할 수 있습니다.", "evidence": ["manager"], "covers": ["responsibility"], "kind": "behavior", "quote": "\\class CameraManager\n * \\brief Provide access and manage all cameras in the system\n *\n * The camera manager is the entry point to libcamera. It enumerates devices,\n * associates them with pipeline managers, and provides access to the cameras\n * in the system to applications. The manager owns all Camera objects and\n * handles hot-plugging and hot-unplugging to manage the lifetime of cameras.\n *\n * To interact with libcamera, an application starts by creating a camera\n * manager instance. Only a single instance of the camera manager may exist at\n * a time. Attempting to create a second instance without first deleting the\n * existing instance results in undefined behaviour.\n *\n * The manager is initially stopped, and shall be started with start(). This\n * will enumerate all the cameras present in the system, which can then be\n * listed with list() and retrieved with get().\n *\n * Cameras are shared through std::shared_ptr<>, ensuring that a camera will\n * stay valid until the last reference is released without requiring any special\n * action from the application. Once the application has released all the\n * references it held to cameras, the camera manager can be stopped with\n * stop().\n */"}, {"text": "`Camera`는 단일 이미지 소스에서 하나 이상의 이미지 스트림을 생성하는 카메라를 나타내며, 장치 설정과 제어 및 이미지 스트림 캡처의 주 인터페이스를 제공합니다. libcamera는 `std::shared_ptr<>`로 카메라 인스턴스의 수명을 관리하며, 인스턴스는 공유 포인터를 반환하는 `create()`로 생성해야 합니다. `Camera` 생성자와 소멸자는 비공개이므로 인스턴스를 직접 생성하거나 파괴할 수 없습니다.", "evidence": ["camera"], "covers": ["responsibility"], "kind": "behavior", "quote": "The Camera class models a camera capable of producing one or more image\n * streams from a single image source. It provides the main interface to\n * configuring and controlling the device, and capturing image streams. It is\n * the central object exposed by libcamera.\n *\n * To support the central nature of Camera objects, libcamera manages the\n * lifetime of camera instances with std::shared_ptr<>. Instances shall be\n * created with the create() function which returns a shared pointer. The\n * Camera constructors and destructor are private, to prevent instances from\n * being constructed and destroyed manually.\n *\n * \\section camera_operation"}, {"text": "`Request`는 애플리케이션이 프레임마다 버퍼와 제어 값을 연결하여 카메라 장치의 처리를 위해 대기열에 넣을 수 있게 합니다. `Request::Request()`는 애플리케이션용 `cookie`를 요청에 저장하며, 애플리케이션은 언제든 `cookie()`로 이 값을 읽을 수 있습니다. 애플리케이션은 일반적으로 요청 완료 핸들러에서 이 값을 사용해 요청을 외부 리소스에 연결하며, libcamera는 이 값을 불투명한 값으로 취급합니다.", "evidence": ["request"], "covers": ["responsibility"], "kind": "behavior", "quote": "/**\n * \\brief Create a capture request for a camera\n * \\param[in] camera The camera that creates the request\n * \\param[in] cookie Opaque cookie for application use\n *\n * The \\a cookie is stored in the request and is accessible through the\n * cookie() function at any time. It is typically used by applications to map\n * the request to an external resource in the request completion handler, and is\n * completely opaque to libcamera.\n */\nRequest::Request(Camera *camera, uint64_t cookie)"}], "state": [{"text": "`Available` 상태에서 `acquire()`가 성공하면 카메라는 `Acquired` 상태가 됩니다.", "evidence": ["states"], "covers": ["state"], "kind": "behavior", "quote": "\\section camera_operation Operating the Camera\n *\n * An application needs to perform a sequence of operations on a camera before\n * it is ready to process requests. The camera needs to be acquired and\n * configured to prepare the camera for capture. Once started the camera can\n * process requests until it is stopped. When an application is done with a\n * camera, the camera needs to be released.\n *\n * An application may start and stop a camera multiple times as long as it is\n * not released. The camera may also be reconfigured.\n *\n * Functions that affect the camera state as defined below are generally not\n * synchronized with each other by the Camera class. The caller is responsible\n * for ensuring their synchronization if necessary.\n *\n * \\subsection Camera States\n *\n * To help manage the sequence of operations needed to control the camera a set\n * of states are defined. Each state describes which operations may be performed\n * on the camera. Performing an operation not allowed in the camera state\n * results in undefined behaviour. Operations not listed at all in the state\n * diagram are allowed in all states.\n *\n * \\dot\n * digraph camera_state_machine {\n *   node [shape = doublecircle ]; Available;\n *   node [shape = circle ]; Acquired;\n *   node [shape = circle ]; Configured;\n *   node [shape = circle ]; Stopping;\n *   node [shape = circle ]; Running;\n *\n *   Available -> Available [label = \"release()\"];\n *   Available -> Acquired [label = \"acquire()\"];\n *\n *   Acquired -> Available [label = \"release()\"];\n *   Acquired -> Configured [label = \"configure()\"];\n *\n *   Configured -> Available [label = \"release()\"];\n *   Configured -> Configured [label = \"configure(), createRequest()\"];\n *   Configured -> Running [label = \"start()\"];\n *\n *   Running -> Stopping [label = \"stop()\"];\n *   Stopping -> Configured;\n *   Running -> Running [label = \"createRequest(), queueRequest()\"];\n * }\n * \\enddot", "part_id": "transition-acquire"}, {"text": "상태도에서 `configure()`는 `Acquired` 또는 `Configured` 상태를 `Configured` 상태로 전환합니다. `Camera::configure()` 구현은 접근 검사, 설정 검증, 파이프라인 설정 호출과 각 스트림 확인을 통과하면 상태를 `Private::CameraConfigured`로 설정한 뒤 `0`을 반환합니다. 접근 검사가 실패하면 해당 음수 값을 반환하고, 설정이 유효하지 않거나 스트림이 없으면 `-EINVAL`을 반환하며, 파이프라인 설정 호출이 0이 아닌 값을 반환하면 그 값을 그대로 반환합니다.", "evidence": ["configure-state-result", "states"], "covers": ["state"], "kind": "behavior", "quote": "d->setState(Private::CameraConfigured);\n\n\treturn 0;", "part_id": "transition-configure"}, {"text": "카메라가 `Configured` 상태에서 `start()`를 호출하면 `Running` 상태로 전환합니다.", "evidence": ["states"], "covers": ["state"], "kind": "behavior", "quote": "\\section camera_operation Operating the Camera\n *\n * An application needs to perform a sequence of operations on a camera before\n * it is ready to process requests. The camera needs to be acquired and\n * configured to prepare the camera for capture. Once started the camera can\n * process requests until it is stopped. When an application is done with a\n * camera, the camera needs to be released.\n *\n * An application may start and stop a camera multiple times as long as it is\n * not released. The camera may also be reconfigured.\n *\n * Functions that affect the camera state as defined below are generally not\n * synchronized with each other by the Camera class. The caller is responsible\n * for ensuring their synchronization if necessary.\n *\n * \\subsection Camera States\n *\n * To help manage the sequence of operations needed to control the camera a set\n * of states are defined. Each state describes which operations may be performed\n * on the camera. Performing an operation not allowed in the camera state\n * results in undefined behaviour. Operations not listed at all in the state\n * diagram are allowed in all states.\n *\n * \\dot\n * digraph camera_state_machine {\n *   node [shape = doublecircle ]; Available;\n *   node [shape = circle ]; Acquired;\n *   node [shape = circle ]; Configured;\n *   node [shape = circle ]; Stopping;\n *   node [shape = circle ]; Running;\n *\n *   Available -> Available [label = \"release()\"];\n *   Available -> Acquired [label = \"acquire()\"];\n *\n *   Acquired -> Available [label = \"release()\"];\n *   Acquired -> Configured [label = \"configure()\"];\n *\n *   Configured -> Available [label = \"release()\"];\n *   Configured -> Configured [label = \"configure(), createRequest()\"];\n *   Configured -> Running [label = \"start()\"];\n *\n *   Running -> Stopping [label = \"stop()\"];\n *   Stopping -> Configured;\n *   Running -> Running [label = \"createRequest(), queueRequest()\"];\n * }\n * \\enddot", "part_id": "transition-start"}, {"text": "`Running` 상태에서 `stop()`을 호출하면 `Stopping` 상태로 전이합니다.", "evidence": ["states"], "covers": ["state"], "kind": "behavior", "quote": "\\section camera_operation Operating the Camera\n *\n * An application needs to perform a sequence of operations on a camera before\n * it is ready to process requests. The camera needs to be acquired and\n * configured to prepare the camera for capture. Once started the camera can\n * process requests until it is stopped. When an application is done with a\n * camera, the camera needs to be released.\n *\n * An application may start and stop a camera multiple times as long as it is\n * not released. The camera may also be reconfigured.\n *\n * Functions that affect the camera state as defined below are generally not\n * synchronized with each other by the Camera class. The caller is responsible\n * for ensuring their synchronization if necessary.\n *\n * \\subsection Camera States\n *\n * To help manage the sequence of operations needed to control the camera a set\n * of states are defined. Each state describes which operations may be performed\n * on the camera. Performing an operation not allowed in the camera state\n * results in undefined behaviour. Operations not listed at all in the state\n * diagram are allowed in all states.\n *\n * \\dot\n * digraph camera_state_machine {\n *   node [shape = doublecircle ]; Available;\n *   node [shape = circle ]; Acquired;\n *   node [shape = circle ]; Configured;\n *   node [shape = circle ]; Stopping;\n *   node [shape = circle ]; Running;\n *\n *   Available -> Available [label = \"release()\"];\n *   Available -> Acquired [label = \"acquire()\"];\n *\n *   Acquired -> Available [label = \"release()\"];\n *   Acquired -> Configured [label = \"configure()\"];\n *\n *   Configured -> Available [label = \"release()\"];\n *   Configured -> Configured [label = \"configure(), createRequest()\"];\n *   Configured -> Running [label = \"start()\"];\n *\n *   Running -> Stopping [label = \"stop()\"];\n *   Stopping -> Configured;\n *   Running -> Running [label = \"createRequest(), queueRequest()\"];\n * }\n * \\enddot", "part_id": "transition-stop-entry"}, {"text": "카메라는 `Stopping` 상태에서 정지 처리를 마치면 `Configured` 상태로 돌아갑니다.", "evidence": ["states"], "covers": ["state"], "kind": "behavior", "quote": "\\section camera_operation Operating the Camera\n *\n * An application needs to perform a sequence of operations on a camera before\n * it is ready to process requests. The camera needs to be acquired and\n * configured to prepare the camera for capture. Once started the camera can\n * process requests until it is stopped. When an application is done with a\n * camera, the camera needs to be released.\n *\n * An application may start and stop a camera multiple times as long as it is\n * not released. The camera may also be reconfigured.\n *\n * Functions that affect the camera state as defined below are generally not\n * synchronized with each other by the Camera class. The caller is responsible\n * for ensuring their synchronization if necessary.\n *\n * \\subsection Camera States\n *\n * To help manage the sequence of operations needed to control the camera a set\n * of states are defined. Each state describes which operations may be performed\n * on the camera. Performing an operation not allowed in the camera state\n * results in undefined behaviour. Operations not listed at all in the state\n * diagram are allowed in all states.\n *\n * \\dot\n * digraph camera_state_machine {\n *   node [shape = doublecircle ]; Available;\n *   node [shape = circle ]; Acquired;\n *   node [shape = circle ]; Configured;\n *   node [shape = circle ]; Stopping;\n *   node [shape = circle ]; Running;\n *\n *   Available -> Available [label = \"release()\"];\n *   Available -> Acquired [label = \"acquire()\"];\n *\n *   Acquired -> Available [label = \"release()\"];\n *   Acquired -> Configured [label = \"configure()\"];\n *\n *   Configured -> Available [label = \"release()\"];\n *   Configured -> Configured [label = \"configure(), createRequest()\"];\n *   Configured -> Running [label = \"start()\"];\n *\n *   Running -> Stopping [label = \"stop()\"];\n *   Stopping -> Configured;\n *   Running -> Running [label = \"createRequest(), queueRequest()\"];\n * }\n * \\enddot", "part_id": "transition-stop-return"}, {"text": "`release()` 후 카메라는 `Available` 상태입니다. 상태도에서 `Available` 상태의 `release()`는 `Available`에 머물고, `Acquired` 또는 `Configured` 상태의 `release()`는 `Available`로 전환합니다.", "evidence": ["states"], "covers": ["state"], "kind": "behavior", "quote": "\\section camera_operation Operating the Camera\n *\n * An application needs to perform a sequence of operations on a camera before\n * it is ready to process requests. The camera needs to be acquired and\n * configured to prepare the camera for capture. Once started the camera can\n * process requests until it is stopped. When an application is done with a\n * camera, the camera needs to be released.\n *\n * An application may start and stop a camera multiple times as long as it is\n * not released. The camera may also be reconfigured.\n *\n * Functions that affect the camera state as defined below are generally not\n * synchronized with each other by the Camera class. The caller is responsible\n * for ensuring their synchronization if necessary.\n *\n * \\subsection Camera States\n *\n * To help manage the sequence of operations needed to control the camera a set\n * of states are defined. Each state describes which operations may be performed\n * on the camera. Performing an operation not allowed in the camera state\n * results in undefined behaviour. Operations not listed at all in the state\n * diagram are allowed in all states.\n *\n * \\dot\n * digraph camera_state_machine {\n *   node [shape = doublecircle ]; Available;\n *   node [shape = circle ]; Acquired;\n *   node [shape = circle ]; Configured;\n *   node [shape = circle ]; Stopping;\n *   node [shape = circle ]; Running;\n *\n *   Available -> Available [label = \"release()\"];\n *   Available -> Acquired [label = \"acquire()\"];\n *\n *   Acquired -> Available [label = \"release()\"];\n *   Acquired -> Configured [label = \"configure()\"];\n *\n *   Configured -> Available [label = \"release()\"];\n *   Configured -> Configured [label = \"configure(), createRequest()\"];\n *   Configured -> Running [label = \"start()\"];\n *\n *   Running -> Stopping [label = \"stop()\"];\n *   Stopping -> Configured;\n *   Running -> Running [label = \"createRequest(), queueRequest()\"];\n * }\n * \\enddot", "part_id": "transition-release"}, {"text": "`Camera::createRequest`는 카메라가 `Configured` 또는 `Running` 상태일 때만 호출할 수 있습니다.", "evidence": ["create-state"], "covers": ["state"], "kind": "behavior", "quote": "\\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest(uint64_t cookie)", "part_id": "create-state"}, {"text": "호출자는 카메라가 `Running` 상태일 때만 `Camera::queueRequest`를 호출할 수 있습니다.", "evidence": ["queue-state"], "covers": ["state"], "kind": "behavior", "quote": "\\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)", "part_id": "queue-state"}, {"text": "호출자는 카메라가 `Configured` 상태일 때만 `Camera::start`를 호출할 수 있습니다.", "evidence": ["start"], "covers": ["state"], "kind": "behavior", "quote": "\\brief Start capture from camera\n * \\param[in] controls Controls to be applied before starting the Camera\n *\n * Start the camera capture session, optionally providing a list of controls to\n * apply before starting. Once the camera is started the application can queue\n * requests to the camera to process and return to the application until the\n * capture session is terminated with \\a stop().\n *\n * \\context This function may only be called when the camera is in the\n * Configured state as defined in \\ref camera_operation, and shall be\n * synchronized by the caller with other functions that affect the camera\n * state.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not in a state where it can be started\n */\nint Camera::start(const ControlList *controls)", "part_id": "start-state"}, {"text": "카메라 상태에 영향을 주는 함수들은 일반적으로 `Camera` 클래스에서 서로 동기화하지 않습니다. 호출자는 필요한 경우 이 함수들을 동기화해야 합니다.", "evidence": ["synchronization"], "covers": ["state"], "kind": "behavior", "quote": "Functions that affect the camera state as defined below are generally not\n * synchronized with each other by the Camera class. The caller is responsible\n * for ensuring their synchronization if necessary.", "part_id": "state-synchronization"}], "shutdown": [{"text": "`Camera::queueRequest()`는 성공하면 0을 반환하고, 그 밖에는 음수 오류 코드를 반환합니다. 카메라 연결이 끊어지면 `-ENODEV`, 카메라가 실행 중이 아니면 `-EACCES`, 요청이 이 카메라에 속하지 않으면 `-EXDEV`, 요청이 유효하지 않으면 `-EINVAL`, 요청을 처리할 버퍼 메모리가 없으면 `-ENOMEM`을 반환합니다.", "evidence": ["queue"], "covers": ["shutdown"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();"}, {"text": "`Camera::queueRequest()`는 실행 상태 접근 검사에서 음수가 나오면 그 값을 반환합니다. 요청을 만든 카메라가 현재 카메라가 아니면 `-EXDEV`를 반환합니다. 요청 상태가 `Request::RequestPending`이 아니거나 `request->controls().infoMap()`이 카메라의 `controls()` 주소와 다르면 `-EINVAL`을 반환합니다.", "evidence": ["queue"], "covers": ["shutdown"], "kind": "behavior", "quote": "if (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}"}, {"text": "`Camera::queueRequest()`는 요청에 버퍼가 없거나 버퍼에 연결된 스트림 중 활성 스트림이 아닌 것이 있으면 `-EINVAL`을 반환합니다. 이 검사를 통과하면 `patchControlList()`를 호출한 뒤 `PipelineHandler::queueRequest()`를 `ConnectionTypeQueued`로 호출하고 0을 반환합니다.", "evidence": ["queue"], "covers": ["shutdown"], "kind": "behavior", "quote": "for (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}"}, {"text": "`Camera::stop()`은 카메라가 실행 중이 아니면 실제 구현에서 아무 작업 없이 0을 반환합니다. 실행 중이면 접근 검사를 하고, 검사 결과가 음수일 때 그 값을 반환합니다.", "evidence": ["stop"], "covers": ["shutdown"], "kind": "behavior", "quote": "/*\n\t * \\todo Make calling stop() when not in 'Running' part of the state\n\t * machine rather than take this shortcut\n\t */\n\tif (!d->isRunning())\n\t\treturn 0;"}, {"text": "`Camera::stop()`은 접근 검사를 통과하면 상태를 `CameraStopping`으로 바꾸고 `PipelineHandler::stop()`을 `ConnectionTypeBlocking`으로 호출합니다. 이후 대기 중인 요청이 없다는 assertion을 확인하고 상태를 `CameraConfigured`로 바꾼 뒤 0을 반환합니다. 문서에 따르면 이 함수는 촬영과 요청 처리를 즉시 중단하며, 대기 중인 모든 요청은 취소되어 오류 상태로 동기적으로 완료됩니다.", "evidence": ["stop"], "covers": ["shutdown"], "kind": "behavior", "quote": "d->pipe_->invokeMethod(&PipelineHandler::stop, ConnectionTypeBlocking,\n\t\t\t       this);"}], "concurrency": [{"text": "`Camera::createRequest()`는 스레드 안전 함수입니다.", "evidence": ["create"], "covers": ["concurrency"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest(uint64_t cookie)", "part_id": "create-thread"}, {"text": "`Camera::queueRequest()`는 스레드 안전 함수입니다. 이 함수는 카메라가 `Running` 상태일 때만 호출할 수 있습니다.", "evidence": ["queue"], "covers": ["concurrency"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();", "part_id": "queue-thread"}, {"text": "호출자는 `Camera::start`와 `Camera::stop`을 각각 카메라 상태에 영향을 주는 다른 함수와 동기화해야 합니다.", "evidence": ["start", "stop"], "covers": ["concurrency"], "kind": "behavior", "quote": "\\brief Start capture from camera\n * \\param[in] controls Controls to be applied before starting the Camera\n *\n * Start the camera capture session, optionally providing a list of controls to\n * apply before starting. Once the camera is started the application can queue\n * requests to the camera to process and return to the application until the\n * capture session is terminated with \\a stop().\n *\n * \\context This function may only be called when the camera is in the\n * Configured state as defined in \\ref camera_operation, and shall be\n * synchronized by the caller with other functions that affect the camera\n * state.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not in a state where it can be started\n */\nint Camera::start(const ControlList *controls)", "part_id": "state-synchronization"}, {"text": "파이프라인 핸들러는 `completeBuffer()`와 `completeRequest()`를 `CameraManager` 스레드에서 호출해야 합니다. `cancelRequest()`에는 `completeRequest()`와 같은 규칙이 적용됩니다.", "evidence": ["completion"], "covers": ["concurrency"], "kind": "behavior", "quote": "/**\n * \\brief Cancel request and signal its completion\n * \\param[in] request The request to cancel\n *\n * This function cancels and completes the request. The same rules as for\n * completeRequest() apply.\n */\nvoid PipelineHandler::cancelRequest(Request *request)\n{\n\trequest->_d()->cancel();\n\tcompleteRequest(request);\n}", "part_id": "completion-context"}, {"text": "파이프라인 핸들러는 요청이 완료되면 `Camera::requestComplete`를 호출해 카메라에 알립니다. `Camera::requestComplete`는 `requestCompleted.emit(request)`를 호출해 완료된 요청을 애플리케이션에 알리는 신호를 발행합니다.", "evidence": ["callback-signal"], "covers": ["concurrency"], "kind": "behavior", "quote": "\\brief Handle request completion and notify application\n * \\param[in] request The request that has completed\n *\n * This function is called by the pipeline handler to notify the camera that\n * the request has completed. It emits the requestCompleted signal.\n */\nvoid Camera::requestComplete(Request *request)\n{\n\t/* Disconnected cameras are still able to complete requests. */\n\tif (_d()->isAccessAllowed(Private::CameraStopping, Private::CameraRunning,\n\t\t\t\t  true))\n\t\tLOG(Camera, Fatal) << \"Trying to complete a request when stopped\";", "part_id": "callback-signal"}], "disconnection": [{"text": "`Camera::disconnect()`는 내부 `disconnect()`를 호출한 뒤 `disconnected` 신호를 발생시켜 애플리케이션에 연결 해제를 알립니다. 내부 `Camera::Private::disconnect()`는 현재 상태가 `CameraRunning`이면 `CameraConfigured`로 바꾸고, 그다음 `disconnected_`를 `true`로 설정합니다.", "evidence": ["notification", "access"], "covers": ["disconnection"], "kind": "behavior", "quote": "_d()->disconnect();\n\tdisconnected.emit();\n}"}, {"text": "`Camera::disconnect()`의 문서는 연결 해제 후 애플리케이션에 공개된 `Camera` API에 대한 모든 새 호출이 즉시 오류를 반환한다고 설명합니다. 두 `isAccessAllowed()` 오버로드는 `allowDisconnected`가 거짓이고 `disconnected_`가 참이면 상태를 확인하기 전에 `-ENODEV`를 반환합니다. 그렇지 않으면 현재 상태가 지정된 상태와 같거나 지정된 범위의 양 끝을 포함해 그 안에 있을 때 `0`을 반환하고, 일치하지 않으면 오류를 기록한 뒤 `-EACCES`를 반환합니다.", "evidence": ["access", "notification"], "covers": ["disconnection"], "kind": "behavior", "quote": "int Camera::Private::isAccessAllowed(State state, bool allowDisconnected,\n\t\t\t\t     const char *from) const\n{\n\tif (!allowDisconnected && disconnected_)\n\t\treturn -ENODEV;"}, {"text": "`Camera::disconnect()`의 문서는 실행 중 연결이 해제된 경우 대기 중인 요청을 처리하는 일을 `TODO`로 남겨 둡니다.", "evidence": ["notification"], "covers": ["disconnection"], "kind": "limitation", "quote": "\\brief Notify camera disconnection\n *\n * This function is used to notify the camera instance that the underlying\n * hardware has been unplugged. In response to the disconnection the camera\n * instance notifies the application by emitting the #disconnected signal, and\n * ensures that all new calls to the application-facing Camera API return an\n * error immediately.\n *\n * \\todo Deal with pending requests if the camera is disconnected in a\n * running state.\n */\nvoid Camera::disconnect()\n{\n\tLOG(Camera, Debug) << \"Disconnecting camera \" << id();"}]}, "topic_inputs": {"responsibility": "e720401a6f8f1bcd6607e697d62ca2a7ff16922e8ad71988578103bf27ca5b41", "state": "cada78ad3f58e59a205e5b0704a5bf6a4ea1aec2a753aba468ec9f64b5ea9b77", "shutdown": "774ceade6a7a6466d4378e9b37e72936815d10bad7f0f790ceeb605c59cd2bbf", "concurrency": "06893f5454e0251cdafc278f4f4ae73b6c224268d943b6e3794c93d0a9015181", "disconnection": "b3645e0ea3c375914d543e8b000e77b3feda107bab5a14973b257938d3b79874"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["responsibility", "state", "shutdown", "concurrency", "disconnection"], "topic_agents": {"responsibility": "cli/codex/gpt-6.1-terra", "state": "cli/codex/gpt-6.1-terra", "shutdown": "cli/codex/gpt-6.1-terra", "concurrency": "cli/codex/gpt-6.1-terra", "disconnection": "cli/codex/gpt-6.1-terra"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "e0c429a5c80a01c34563ce00a616df89d8f75c735f8669bcbd1f75d84cce82a6", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "d4af3d834d8b1c99a6c9311612712a64112c30fa4621b375904d172f361285b8", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "fecc4ee78a481139776e562c164c0da9a3e5edf0a64a72be1d1c8feddee3cd08", "answer_contracts": "1e0d24e0cf26ded53ecec2e5a6fbc51836bac6e17530318a9fa7cffaa936c00b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "9db4d42a710b4a71a7d2bb16f69db06926409281dc1a200c796e77d5deaa25a0", "design_response": "74ebb2d21768d6bdd4ef7611c1c539526a7e72e6a58604c82e8305003d24f8b7", "design_validation": "b8133c78a8eb42fd5194c2756bb649b396ec54b40c49b72544bdbbcaf3366c57"}, "validation_model": "44197615786b818e4d9150110e74bef6772ea4f261a58d27ac12f379abaeb439", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "f8fd5a3d8041c23fc68b93ff32b8727e98393383b5099032eb00ad0013e7611c"}, "checkpoint_units": [{"checkpoint": "e34fdc061a88dbed043301a3a652759a187be16e5c8478ae4e30a6be66a9154c.json", "topic": "responsibility", "part": null, "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/395.receipt.json", "60b1bf48442840808eecd0e46851648e/396.receipt.json"]}, {"checkpoint": "f3234531fd7993843e62beaecc6b85e36299d378313d1e6afed65d965473fc36.json", "topic": "state", "part": "transition-acquire", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/397.receipt.json", "60b1bf48442840808eecd0e46851648e/398.receipt.json"]}, {"checkpoint": "2f4de625d4eded3f7bd00a04f15e18d9e837dd83832ee21fdd98cc93618fa3f9.json", "topic": "state", "part": "transition-configure", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/399.receipt.json", "60b1bf48442840808eecd0e46851648e/400.receipt.json"]}, {"checkpoint": "71cbdfa97fb8a4f18e2b1c37730eab5bf0260d0199bfeb5f5e353e7efb8242d1.json", "topic": "state", "part": "transition-start", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/401.receipt.json", "60b1bf48442840808eecd0e46851648e/402.receipt.json"]}, {"checkpoint": "a75ce3fbae532fe94bf50f8ddbc2c9b4593e980865bf27ea194655e32e38bad0.json", "topic": "state", "part": "transition-stop-entry", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/403.receipt.json", "60b1bf48442840808eecd0e46851648e/404.receipt.json"]}, {"checkpoint": "6bfa8eb8aeb6632a6890c39f8fb25c8a029ff22df874fcfb4bbac7bebdd342ca.json", "topic": "state", "part": "transition-stop-return", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/405.receipt.json", "60b1bf48442840808eecd0e46851648e/406.receipt.json", "60b1bf48442840808eecd0e46851648e/407.receipt.json"]}, {"checkpoint": "e026ccecdf003d38badd79456f1c6453232eb794991f1e6de7ccf2ef9d40e3ea.json", "topic": "state", "part": "transition-release", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/408.receipt.json", "60b1bf48442840808eecd0e46851648e/409.receipt.json"]}, {"checkpoint": "1b6a6ef0a5984e1e2a272f76915fe76ad70aad2d52321206191a980d972bf7d4.json", "topic": "state", "part": "create-state", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/410.receipt.json", "60b1bf48442840808eecd0e46851648e/411.receipt.json"]}, {"checkpoint": "e834d9f0335fbc16c70cab436a26b3294c2821d35666ae8ad3439631135f3a51.json", "topic": "state", "part": "queue-state", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/412.receipt.json", "60b1bf48442840808eecd0e46851648e/413.receipt.json"]}, {"checkpoint": "0bc0e7d30bc0db350e0eb6bdc5f2ac5fc7866a19f96f75bb034466eae6d21756.json", "topic": "state", "part": "start-state", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/414.receipt.json", "60b1bf48442840808eecd0e46851648e/415.receipt.json"]}, {"checkpoint": "1174e41910cb5d1f9fc39e53b12efad7c2d3b0ba91ce6417502a210fe8ac6d55.json", "topic": "state", "part": "state-synchronization", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/416.receipt.json", "60b1bf48442840808eecd0e46851648e/417.receipt.json"]}, {"checkpoint": "ef91d2fe4d683ea9fbb502e14feeba272715ae9022c4f753d03cb71ac5f269f5.json", "topic": "shutdown", "part": null, "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/418.receipt.json", "60b1bf48442840808eecd0e46851648e/419.receipt.json"]}, {"checkpoint": "bd4a26efa87f7fd80efd5b316ed4cd831831c542ee85da8e7b0d24a0f813f31e.json", "topic": "concurrency", "part": "create-thread", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/420.receipt.json", "60b1bf48442840808eecd0e46851648e/421.receipt.json"]}, {"checkpoint": "8f8b6155c49612a0596cfb0f671b861053986b903cacc1db661dfc108d7a8150.json", "topic": "concurrency", "part": "queue-thread", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/422.receipt.json", "60b1bf48442840808eecd0e46851648e/423.receipt.json"]}, {"checkpoint": "1be46db3326ac6979f2999a7288c744e88ae0da435d9616a26a8eb167ddb669e.json", "topic": "concurrency", "part": "state-synchronization", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/424.receipt.json", "60b1bf48442840808eecd0e46851648e/425.receipt.json"]}, {"checkpoint": "5f2345459fe50042043e3f2bc0efaffd9947abad94465f7c828f4a50eb2e17db.json", "topic": "concurrency", "part": "completion-context", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/426.receipt.json", "60b1bf48442840808eecd0e46851648e/427.receipt.json"]}, {"checkpoint": "bb5377fe2bbd82a38111f732d001b144fc01bb0c008c9e037d36d773ad0b7d8c.json", "topic": "concurrency", "part": "callback-signal", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/428.receipt.json", "60b1bf48442840808eecd0e46851648e/429.receipt.json"]}, {"checkpoint": "de5692c3d618d8f87c41f9a3a4ffa6c3d65af3eb94b2c92e988bb8b3e4e894c5.json", "topic": "disconnection", "part": null, "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/430.receipt.json", "60b1bf48442840808eecd0e46851648e/431.receipt.json"]}], "body_sha256": "88708451033f33926b4167efe35b6d5cce5a0dc3b4bc1653d78d30c9891672f5"}
---

# 카메라와 요청 모델

**클래스의 책임, 요청과 버퍼의 수명, 상태 전이와 종료·동기화 계약을 코드 근거로 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| <a id="요청-생성과-완료"></a>요청 생성과 완료의 조건과 근거를 대조하세요. | [요청 객체와 버퍼 수명](camera-requests.md#요청-생성과-완료) |
| <a id="소유권과-재사용"></a>소유권과 재사용의 조건과 근거를 대조하세요. | [요청 객체와 버퍼 수명](camera-requests.md#소유권과-재사용) |
| <a id="요청과-버퍼를-유지할-기간"></a>“요청과 버퍼를 유지할 기간” 그림을 확인하세요. | [요청 객체와 버퍼 수명](camera-requests.md#요청과-버퍼를-유지할-기간) |

## 클래스별 책임

`CameraManager`는 libcamera의 진입점으로, 장치를 열거하고 파이프라인 관리자와 연결하며 애플리케이션에 카메라를 제공합니다. 관리자는 모든 `Camera` 객체를 소유하고 핫플러그와 핫언플러그를 처리해 카메라의 수명을 관리합니다. 애플리케이션은 관리자 인스턴스를 만들고 `start()`를 호출해야 합니다. 관리자는 처음에 정지 상태이며, 시작하면 시스템의 카메라를 열거하여 `list()`와 `get()`으로 접근할 수 있습니다. `src/libcamera/camera_manager.cpp:280`

한 번에 `CameraManager` 인스턴스는 하나만 존재할 수 있으며, 기존 인스턴스를 삭제하기 전에 두 번째 인스턴스를 만들면 동작이 정의되지 않습니다. 카메라는 `std::shared_ptr<>`로 공유되며 마지막 참조가 해제될 때까지 유효합니다. 애플리케이션이 보유한 모든 카메라 참조를 해제한 뒤에는 `stop()`으로 관리자를 정지할 수 있습니다. `src/libcamera/camera_manager.cpp:280`

`Camera`는 단일 이미지 소스에서 하나 이상의 이미지 스트림을 생성하는 카메라를 나타내며, 장치 설정과 제어 및 이미지 스트림 캡처의 주 인터페이스를 제공합니다. libcamera는 `std::shared_ptr<>`로 카메라 인스턴스의 수명을 관리하며, 인스턴스는 공유 포인터를 반환하는 `create()`로 생성해야 합니다. `Camera` 생성자와 소멸자는 비공개이므로 인스턴스를 직접 생성하거나 파괴할 수 없습니다. `src/libcamera/camera.cpp:758`

`Request`는 애플리케이션이 프레임마다 버퍼와 제어 값을 연결하여 카메라 장치의 처리를 위해 대기열에 넣을 수 있게 합니다. `Request::Request()`는 애플리케이션용 `cookie`를 요청에 저장하며, 애플리케이션은 언제든 `cookie()`로 이 값을 읽을 수 있습니다. 애플리케이션은 일반적으로 요청 완료 핸들러에서 이 값을 사용해 요청을 외부 리소스에 연결하며, libcamera는 이 값을 불투명한 값으로 취급합니다. `src/libcamera/request.cpp:343`

근거 원문: [src/libcamera/camera_manager.cpp:280](#source-fbcf3effd2584b79) · [src/libcamera/camera.cpp:758](#source-6c066281dcce33d6) · [src/libcamera/request.cpp:343](#source-abce7dd469896527)

## 상태와 허용 호출

`Available` 상태에서 `acquire()`가 성공하면 카메라는 `Acquired` 상태가 됩니다. 상태도에서 `configure()`는 `Acquired` 또는 `Configured` 상태를 `Configured` 상태로 전환합니다. `Camera::configure()` 구현은 접근 검사, 설정 검증, 파이프라인 설정 호출과 각 스트림 확인을 통과하면 상태를 `Private::CameraConfigured`로 설정한 뒤 `0`을 반환합니다. 접근 검사가 실패하면 해당 음수 값을 반환하고, 설정이 유효하지 않거나 스트림이 없으면 `-EINVAL`을 반환하며, 파이프라인 설정 호출이 0이 아닌 값을 반환하면 그 값을 그대로 반환합니다. `src/libcamera/camera.cpp:769`, `src/libcamera/camera.cpp:1237`

<!-- sdd:visual:camera-states -->
### 카메라 상태와 허용 호출

성공한 상태 전이와 상태를 유지하는 호출을 구분하세요. 상태 변경 함수의 동기화는 호출자가 책임집니다.

```mermaid
flowchart TB
%% sdd:translations {"Acquired": "Acquired", "Available": "Available", "Configured": "Configured", "Running": "Running", "Stopping": "Stopping", "acquire()": "acquire()", "configure()": "configure()", "configure(), createRequest()": "configure(), createRequest()", "createRequest(), <br/>queueRequest()": "createRequest(), <br/>queueRequest()", "release()": "release()", "start()": "start()", "stop()": "stop()", "정지 처리 종료": "stop finished"}
  v_available["Available"]
  v_acquired["Acquired"]
  v_configured["Configured"]
  v_running["Running"]
  v_stopping["Stopping"]
  v_available -->|"release()"| v_available
  v_available -->|"acquire()"| v_acquired
  v_acquired -->|"release()"| v_available
  v_acquired -->|"configure()"| v_configured
  v_configured -->|"release()"| v_available
  v_configured -->|"configure(), createRequest()"| v_configured
  v_configured -->|"start()"| v_running
  v_running -->|"stop()"| v_stopping
  v_stopping -->|"정지 처리 종료"| v_configured
  v_running -->|"createRequest(), <br/>queueRequest()"| v_running
```

[Mermaid 원문](camera-model.camera-states.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | Available | [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d) |
    | Acquired | [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d) |
    | Configured | [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d) |
    | Running | [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d) |
    | Stopping | [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d) |
    | release() | [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d) |
    | acquire() | [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d) |
    | release() | [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d) |
    | configure() | [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d) |
    | release() | [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d) |
    | configure(), createRequest() | [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d) |
    | start() | [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d) |
    | stop() | [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d) |
    | 정지 처리 종료 | [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d) |
    | createRequest(), queueRequest() | [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d) |
<!-- /sdd:visual:camera-states -->

카메라가 `Configured` 상태에서 `start()`를 호출하면 `Running` 상태로 전환합니다. `Running` 상태에서 `stop()`을 호출하면 `Stopping` 상태로 전이합니다. 카메라는 `Stopping` 상태에서 정지 처리를 마치면 `Configured` 상태로 돌아갑니다. `src/libcamera/camera.cpp:769`

`release()` 후 카메라는 `Available` 상태입니다. 상태도에서 `Available` 상태의 `release()`는 `Available`에 머물고, `Acquired` 또는 `Configured` 상태의 `release()`는 `Available`로 전환합니다. `Camera::createRequest`는 카메라가 `Configured` 또는 `Running` 상태일 때만 호출할 수 있습니다. 호출자는 카메라가 `Running` 상태일 때만 `Camera::queueRequest`를 호출할 수 있습니다. `src/libcamera/camera.cpp:769`, `src/libcamera/camera.cpp:1258`, `src/libcamera/camera.cpp:1320`

호출자는 카메라가 `Configured` 상태일 때만 `Camera::start`를 호출할 수 있습니다. 카메라 상태에 영향을 주는 함수들은 일반적으로 `Camera` 클래스에서 서로 동기화하지 않습니다. 호출자는 필요한 경우 이 함수들을 동기화해야 합니다. `src/libcamera/camera.cpp:1383`, `src/libcamera/camera.cpp:780`

근거 원문: [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d) · [src/libcamera/camera.cpp:1383](#source-617d53c4c7de2c0c) · [src/libcamera/camera.cpp:1258](#source-8f791427a31c3313) · [src/libcamera/camera.cpp:1320](#source-e0caa8c16f728202) · [src/libcamera/camera.cpp:780](#source-cc6c66b57cf028e6) · [src/libcamera/camera.cpp:1237](#source-077fcae46087aee0)

## 오류와 종료

`Camera::queueRequest()`는 성공하면 0을 반환하고, 그 밖에는 음수 오류 코드를 반환합니다. 카메라 연결이 끊어지면 `-ENODEV`, 카메라가 실행 중이 아니면 `-EACCES`, 요청이 이 카메라에 속하지 않으면 `-EXDEV`, 요청이 유효하지 않으면 `-EINVAL`, 요청을 처리할 버퍼 메모리가 없으면 `-ENOMEM`을 반환합니다. `src/libcamera/camera.cpp:1308`

`Camera::queueRequest()`는 실행 상태 접근 검사에서 음수가 나오면 그 값을 반환합니다. 요청을 만든 카메라가 현재 카메라가 아니면 `-EXDEV`를 반환합니다. 요청 상태가 `Request::RequestPending`이 아니거나 `request->controls().infoMap()`이 카메라의 `controls()` 주소와 다르면 `-EINVAL`을 반환합니다. `src/libcamera/camera.cpp:1308`

`Camera::queueRequest()`는 요청에 버퍼가 없거나 버퍼에 연결된 스트림 중 활성 스트림이 아닌 것이 있으면 `-EINVAL`을 반환합니다. 이 검사를 통과하면 `patchControlList()`를 호출한 뒤 `PipelineHandler::queueRequest()`를 `ConnectionTypeQueued`로 호출하고 0을 반환합니다. `Camera::stop()`은 카메라가 실행 중이 아니면 실제 구현에서 아무 작업 없이 0을 반환합니다. 실행 중이면 접근 검사를 하고, 검사 결과가 음수일 때 그 값을 반환합니다. `src/libcamera/camera.cpp:1308`, `src/libcamera/camera.cpp:1431`

`Camera::stop()`은 접근 검사를 통과하면 상태를 `CameraStopping`으로 바꾸고 `PipelineHandler::stop()`을 `ConnectionTypeBlocking`으로 호출합니다. 이후 대기 중인 요청이 없다는 assertion을 확인하고 상태를 `CameraConfigured`로 바꾼 뒤 0을 반환합니다. 문서에 따르면 이 함수는 촬영과 요청 처리를 즉시 중단하며, 대기 중인 모든 요청은 취소되어 오류 상태로 동기적으로 완료됩니다. `src/libcamera/camera.cpp:1431`

근거 원문: [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/camera.cpp:1431](#source-e09324743def3f09)

## 동시성과 실행 확인

`Camera::createRequest()`는 스레드 안전 함수입니다. `Camera::queueRequest()`는 스레드 안전 함수입니다. 이 함수는 카메라가 `Running` 상태일 때만 호출할 수 있습니다. 호출자는 `Camera::start`와 `Camera::stop`을 각각 카메라 상태에 영향을 주는 다른 함수와 동기화해야 합니다. `src/libcamera/camera.cpp:1243`, `src/libcamera/camera.cpp:1308`, `src/libcamera/camera.cpp:1383`, `src/libcamera/camera.cpp:1431`

파이프라인 핸들러는 `completeBuffer()`와 `completeRequest()`를 `CameraManager` 스레드에서 호출해야 합니다. `cancelRequest()`에는 `completeRequest()`와 같은 규칙이 적용됩니다. 파이프라인 핸들러는 요청이 완료되면 `Camera::requestComplete`를 호출해 카메라에 알립니다. `Camera::requestComplete`는 `requestCompleted.emit(request)`를 호출해 완료된 요청을 애플리케이션에 알리는 신호를 발행합니다. `src/libcamera/pipeline_handler.cpp:547`, `src/libcamera/camera.cpp:1475`

근거 원문: [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) · [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/camera.cpp:1383](#source-617d53c4c7de2c0c) · [src/libcamera/camera.cpp:1431](#source-e09324743def3f09) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) · [src/libcamera/camera.cpp:1475](#source-8e6389a7d7864907)

## 연결 해제와 대기 요청

`Camera::disconnect()`는 내부 `disconnect()`를 호출한 뒤 `disconnected` 신호를 발생시켜 애플리케이션에 연결 해제를 알립니다. 내부 `Camera::Private::disconnect()`는 현재 상태가 `CameraRunning`이면 `CameraConfigured`로 바꾸고, 그다음 `disconnected_`를 `true`로 설정합니다. `src/libcamera/camera.cpp:944`, `src/libcamera/camera.cpp:690`

`Camera::disconnect()`의 문서는 연결 해제 후 애플리케이션에 공개된 `Camera` API에 대한 모든 새 호출이 즉시 오류를 반환한다고 설명합니다. 두 `isAccessAllowed()` 오버로드는 `allowDisconnected`가 거짓이고 `disconnected_`가 참이면 상태를 확인하기 전에 `-ENODEV`를 반환합니다. 그렇지 않으면 현재 상태가 지정된 상태와 같거나 지정된 범위의 양 끝을 포함해 그 안에 있을 때 `0`을 반환하고, 일치하지 않으면 오류를 기록한 뒤 `-EACCES`를 반환합니다. `src/libcamera/camera.cpp:690`, `src/libcamera/camera.cpp:944`

실행 확인 항목: `Camera::disconnect()`의 문서는 실행 중 연결이 해제된 경우 대기 중인 요청을 처리하는 일을 `TODO`로 남겨 둡니다. `src/libcamera/camera.cpp:944`

근거 원문: [src/libcamera/camera.cpp:690](#source-ac8ee83f828fe269) · [src/libcamera/camera.cpp:944](#source-2758e9ddd31ad41d)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | CameraManager, Camera, Request의 책임과 객체 수명은 어떻게 나뉩니까? | [클래스별 책임](#클래스별-책임) | 코드 근거와 설명 연결 |
    | 상태별 허용 호출과 동기화 책임은 어떻게 나뉩니까? | [상태와 허용 호출](#상태와-허용-호출) | 코드 근거와 설명 연결 |
    | queueRequest의 실패 조건과 stop의 취소·완료·반환 상태는 무엇입니까? | [오류와 종료](#오류와-종료) | 코드 근거와 설명 연결 |
    | threadsafe 보장, 호출자의 동기화 책임과 파이프라인의 완료 통지 계약을 구분하세요. 애플리케이션 콜백 전달 방식과 실기기 검증은 별도로 확인하세요. | [동시성과 실행 확인](#동시성과-실행-확인) | 코드 근거와 설명 연결 |
    | 카메라 연결이 끊어지면 상태·API 접근·대기 요청에 어떤 변화와 확인 한계가 있습니까? | [연결 해제와 대기 요청](#연결-해제와-대기-요청) | 코드 근거와 설명 연결 · 실행 확인 항목 별도 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-fbcf3effd2584b79"></a>

??? note "소스 근거: src/libcamera/camera_manager.cpp:280"
    `src/libcamera/camera_manager.cpp:280`에서 시작하는 발췌입니다. 종료 줄은 304이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `adcd6d49b0c989ec78a81cacece7f6c871a8e0ddf3aa52e42648fae2760a6e84`
    
    ```text
    \class CameraManager
     * \brief Provide access and manage all cameras in the system
     *
     * The camera manager is the entry point to libcamera. It enumerates devices,
     * associates them with pipeline managers, and provides access to the cameras
     * in the system to applications. The manager owns all Camera objects and
     * handles hot-plugging and hot-unplugging to manage the lifetime of cameras.
     *
     * To interact with libcamera, an application starts by creating a camera
     * manager instance. Only a single instance of the camera manager may exist at
     * a time. Attempting to create a second instance without first deleting the
     * existing instance results in undefined behaviour.
     *
     * The manager is initially stopped, and shall be started with start(). This
     * will enumerate all the cameras present in the system, which can then be
     * listed with list() and retrieved with get().
     *
     * Cameras are shared through std::shared_ptr<>, ensuring that a camera will
     * stay valid until the last reference is released without requiring any special
     * action from the application. Once the application has released all the
     * references it held to cameras, the camera manager can be stopped with
     * stop().
     */
    
    CameraManager *CameraManager::self_
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

<a id="source-abce7dd469896527"></a>

??? note "소스 근거: src/libcamera/request.cpp:343"
    `src/libcamera/request.cpp:343`에서 시작하는 발췌입니다. 종료 줄은 360이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `948968e35cb0d98957bc63aa2d6b613d2a8203e66855db23974f035e9d679764`
    
    ```text
    \class Request
     * \brief A frame capture request
     *
     * A Request allows an application to associate buffers and controls on a
     * per-frame basis to be queued to the camera device for processing.
     */
    
    /**
     * \brief Create a capture request for a camera
     * \param[in] camera The camera that creates the request
     * \param[in] cookie Opaque cookie for application use
     *
     * The \a cookie is stored in the request and is accessible through the
     * cookie() function at any time. It is typically used by applications to map
     * the request to an external resource in the request completion handler, and is
     * completely opaque to libcamera.
     */
    Request::Request(Camera *camera, uint64_t cookie)
    ```

<a id="source-4b17a07667f3a55d"></a>

??? note "소스 근거: src/libcamera/camera.cpp:769"
    `src/libcamera/camera.cpp:769`에서 시작하는 발췌입니다. 종료 줄은 814이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e85796df194551ecbd587ba1a7bb356a1409fa1d606762865e7eb989c92d2f72`
    
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
     * Functions that affect the camera state as defined below are generally not
     * synchronized with each other by the Camera class. The caller is responsible
     * for ensuring their synchronization if necessary.
     *
     * \subsection Camera States
     *
     * To help manage the sequence of operations needed to control the camera a set
     * of states are defined. Each state describes which operations may be performed
     * on the camera. Performing an operation not allowed in the camera state
     * results in undefined behaviour. Operations not listed at all in the state
     * diagram are allowed in all states.
     *
     * \dot
     * digraph camera_state_machine {
     *   node [shape = doublecircle ]; Available;
     *   node [shape = circle ]; Acquired;
     *   node [shape = circle ]; Configured;
     *   node [shape = circle ]; Stopping;
     *   node [shape = circle ]; Running;
     *
     *   Available -> Available [label = "release()"];
     *   Available -> Acquired [label = "acquire()"];
     *
     *   Acquired -> Available [label = "release()"];
     *   Acquired -> Configured [label = "configure()"];
     *
     *   Configured -> Available [label = "release()"];
     *   Configured -> Configured [label = "configure(), createRequest()"];
     *   Configured -> Running [label = "start()"];
     *
     *   Running -> Stopping [label = "stop()"];
     *   Stopping -> Configured;
     *   Running -> Running [label = "createRequest(), queueRequest()"];
     * }
     * \enddot
    ```

<a id="source-617d53c4c7de2c0c"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1383"
    `src/libcamera/camera.cpp:1383`에서 시작하는 발췌입니다. 종료 줄은 1400이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e0abda64dc6b1bdd78d1326c8dd8651e842c03181dcf28e3b8b7eac1a4c70fcf`
    
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
    int Camera::start(const ControlList *controls)
    ```

<a id="source-8f791427a31c3313"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1258"
    `src/libcamera/camera.cpp:1258`에서 시작하는 발췌입니다. 종료 줄은 1263이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `fd7dc6ea02f64424f17322fff027c34131ac5a3fb64d69d83aa6fa55ca9f826a`
    
    ```text
    \context This function is \threadsafe. It may only be called when the camera
     * is in the Configured or Running state as defined in \ref camera_operation.
     *
     * \return A pointer to the newly created request, or nullptr on error
     */
    std::unique_ptr<Request> Camera::createRequest(uint64_t cookie)
    ```

<a id="source-e0caa8c16f728202"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1320"
    `src/libcamera/camera.cpp:1320`에서 시작하는 발췌입니다. 종료 줄은 1330이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `b9de90acc07617b489b367e116e41ecc8bc712180c6f445763b58658ff1bc649`
    
    ```text
    \context This function is \threadsafe. It may only be called when the camera
     * is in the Running state as defined in \ref camera_operation.
     *
     * \return 0 on success or a negative error code otherwise
     * \retval -ENODEV The camera has been disconnected from the system
     * \retval -EACCES The camera is not running so requests can't be queued
     * \retval -EXDEV The request does not belong to this camera
     * \retval -EINVAL The request is invalid
     * \retval -ENOMEM No buffer memory was available to handle the request
     */
    int Camera::queueRequest(Request *request)
    ```

<a id="source-cc6c66b57cf028e6"></a>

??? note "소스 근거: src/libcamera/camera.cpp:780"
    `src/libcamera/camera.cpp:780`에서 시작하는 발췌입니다. 종료 줄은 782이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `de3ba7a26c3bbaf6bbb33d1749b99829fdc58e13718068d149c849d0b2c43388`
    
    ```text
    Functions that affect the camera state as defined below are generally not
     * synchronized with each other by the Camera class. The caller is responsible
     * for ensuring their synchronization if necessary.
    ```

<a id="source-077fcae46087aee0"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1237"
    `src/libcamera/camera.cpp:1237`에서 시작하는 발췌입니다. 종료 줄은 1239이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `c286717b62d3b69c9dd97f324bb16930edb27f32da54c40916bef758fbca20da`
    
    ```text
    d->setState(Private::CameraConfigured);
    
    	return 0;
    ```

<a id="source-28d007de6ad1a8a5"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1308"
    `src/libcamera/camera.cpp:1308`에서 시작하는 발췌입니다. 종료 줄은 1383이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `96db61baeb32065c966b20942f97518ddbd3a43b36b64e8083eb29a90ecb7f4b`
    
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
    int Camera::queueRequest(Request *request)
    {
    	Private *const d = _d();
    
    	int ret = d->isAccessAllowed(Private::CameraRunning);
    	if (ret < 0)
    		return ret;
    
    	/* Requests can only be queued to the camera that created them. */
    	if (request->_d()->camera() != this) {
    		LOG(Camera, Error) << "Request was not created by this camera";
    		return -EXDEV;
    	}
    
    	if (request->status() != Request::RequestPending) {
    		LOG(Camera, Error) << request->toString() << " is not valid";
    		return -EINVAL;
    	}
    
    	/* Make sure the Request has a valid control list. */
    	if (request->controls().infoMap() != &controls()) {
    		LOG(Camera, Error) << "Overwriting Request::controls() is not allowed";
    		return -EINVAL;
    	}
    
    	/*
    	 * The camera state may change until the end of the function. No locking
    	 * is however needed as PipelineHandler::queueRequest() will handle
    	 * this.
    	 */
    
    	if (request->buffers().empty()) {
    		LOG(Camera, Error) << "Request contains no buffers";
    		return -EINVAL;
    	}
    
    	for (const auto &[stream, buffer] : request->buffers()) {
    		if (d->activeStreams_.find(stream) == d->activeStreams_.end()) {
    			LOG(Camera, Error) << "Invalid request";
    			return -EINVAL;
    		}
    	}
    
    	/* Pre-process AeEnable. */
    	patchControlList(request->controls());
    
    	d->pipe_->invokeMethod(&PipelineHandler::queueRequest,
    			       ConnectionTypeQueued, request);
    
    	return 0;
    }
    
    /**
     * \brief Start capture from camera
    ```

<a id="source-e09324743def3f09"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1431"
    `src/libcamera/camera.cpp:1431`에서 시작하는 발췌입니다. 종료 줄은 1475이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `0009c665993b995489738e48affc81643a7159d82b5326e5f182e30fe11e4901`
    
    ```text
    \brief Stop capture from camera
     *
     * This function stops capturing and processing requests immediately. All
     * pending requests are cancelled and complete synchronously in an error state.
     *
     * \context This function may be called in any camera state as defined in \ref
     * camera_operation, and shall be synchronized by the caller with other
     * functions that affect the camera state. If called when the camera isn't
     * running, it is a no-op.
     *
     * \return 0 on success or a negative error code otherwise
     * \retval -ENODEV The camera has been disconnected from the system
     * \retval -EACCES The camera is not running so can't be stopped
     */
    int Camera::stop()
    {
    	Private *const d = _d();
    
    	/*
    	 * \todo Make calling stop() when not in 'Running' part of the state
    	 * machine rather than take this shortcut
    	 */
    	if (!d->isRunning())
    		return 0;
    
    	int ret = d->isAccessAllowed(Private::CameraRunning);
    	if (ret < 0)
    		return ret;
    
    	LOG(Camera, Debug) << "Stopping capture";
    
    	d->setState(Private::CameraStopping);
    
    	d->pipe_->invokeMethod(&PipelineHandler::stop, ConnectionTypeBlocking,
    			       this);
    
    	ASSERT(!d->pipe_->hasPendingRequests(this));
    
    	d->setState(Private::CameraConfigured);
    
    	return 0;
    }
    
    /**
     * \brief Handle request completion and notify application
    ```

<a id="source-0ae00d77839f61cb"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1243"
    `src/libcamera/camera.cpp:1243`에서 시작하는 발췌입니다. 종료 줄은 1263이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `9f251ecf5ba569606e9753d3619b88e1aef5a4ce15f816ae97efd283e34b823b`
    
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
    std::unique_ptr<Request> Camera::createRequest(uint64_t cookie)
    ```

<a id="source-01ad7c6605c3296a"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:547"
    `src/libcamera/pipeline_handler.cpp:547`에서 시작하는 발췌입니다. 종료 줄은 620이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `514288cc958de9ff5fd19d46393cec3bb3088f4f08486528d4559071138638c9`
    
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
    bool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)
    {
    	Camera *camera = request->_d()->camera();
    	camera->bufferCompleted.emit(request, buffer);
    	return request->_d()->completeBuffer(buffer);
    }
    
    /**
     * \brief Signal request completion
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
    void PipelineHandler::completeRequest(Request *request)
    {
    	Camera *camera = request->_d()->camera();
    
    	request->_d()->complete();
    
    	Camera::Private *data = camera->_d();
    
    	while (!data->queuedRequests_.empty()) {
    		Request *req = data->queuedRequests_.front();
    		if (req->status() == Request::RequestPending)
    			break;
    
    		ASSERT(!req->hasPendingBuffers());
    		data->queuedRequests_.pop_front();
    		camera->requestComplete(req);
    	}
    
    	/* Allow any waiting requests to be queued to the pipeline. */
    	doQueueRequests(camera);
    }
    
    /**
     * \brief Cancel request and signal its completion
     * \param[in] request The request to cancel
     *
     * This function cancels and completes the request. The same rules as for
     * completeRequest() apply.
     */
    void PipelineHandler::cancelRequest(Request *request)
    {
    	request->_d()->cancel();
    	completeRequest(request);
    }
    
    /**
     * \brief Retrieve the absolute path to a platform configuration file
    ```

<a id="source-8e6389a7d7864907"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1475"
    `src/libcamera/camera.cpp:1475`에서 시작하는 발췌입니다. 종료 줄은 1490이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `69fcc9cae7f7590799771bd304b13feeca21ebe9eed7032ea7562d3ab737db6e`
    
    ```text
    \brief Handle request completion and notify application
     * \param[in] request The request that has completed
     *
     * This function is called by the pipeline handler to notify the camera that
     * the request has completed. It emits the requestCompleted signal.
     */
    void Camera::requestComplete(Request *request)
    {
    	/* Disconnected cameras are still able to complete requests. */
    	if (_d()->isAccessAllowed(Private::CameraStopping, Private::CameraRunning,
    				  true))
    		LOG(Camera, Fatal) << "Trying to complete a request when stopped";
    
    	requestCompleted.emit(request);
    }
    
    ```

<a id="source-ac8ee83f828fe269"></a>

??? note "소스 근거: src/libcamera/camera.cpp:690"
    `src/libcamera/camera.cpp:690`에서 시작하는 발췌입니다. 종료 줄은 745이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `1e0ac0e45422136580c0722ca5a356f17a7c0b8ae18dbb64090f7734afdbfaae`
    
    ```text
    int Camera::Private::isAccessAllowed(State state, bool allowDisconnected,
    				     const char *from) const
    {
    	if (!allowDisconnected && disconnected_)
    		return -ENODEV;
    
    	State currentState = state_.load(std::memory_order_acquire);
    	if (currentState == state)
    		return 0;
    
    	ASSERT(static_cast<unsigned int>(state) < std::size(camera_state_names));
    
    	LOG(Camera, Error) << "Camera in " << camera_state_names[currentState]
    			   << " state trying " << from << "() requiring state "
    			   << camera_state_names[state];
    
    	return -EACCES;
    }
    
    int Camera::Private::isAccessAllowed(State low, State high,
    				     bool allowDisconnected,
    				     const char *from) const
    {
    	if (!allowDisconnected && disconnected_)
    		return -ENODEV;
    
    	State currentState = state_.load(std::memory_order_acquire);
    	if (currentState >= low && currentState <= high)
    		return 0;
    
    	ASSERT(static_cast<unsigned int>(low) < std::size(camera_state_names) &&
    	       static_cast<unsigned int>(high) < std::size(camera_state_names));
    
    	LOG(Camera, Error) << "Camera in " << camera_state_names[currentState]
    			   << " state trying " << from
    			   << "() requiring state between "
    			   << camera_state_names[low] << " and "
    			   << camera_state_names[high];
    
    	return -EACCES;
    }
    
    void Camera::Private::disconnect()
    {
    	/*
    	 * If the camera was running when the hardware was removed force the
    	 * state to Configured state to allow applications to free resources
    	 * and call release() before deleting the camera.
    	 */
    	if (state_.load(std::memory_order_acquire) == Private::CameraRunning)
    		state_.store(Private::CameraConfigured, std::memory_order_release);
    
    	disconnected_ = true;
    }
    
    void Camera::Private::setState(State state)
    ```

<a id="source-2758e9ddd31ad41d"></a>

??? note "소스 근거: src/libcamera/camera.cpp:944"
    `src/libcamera/camera.cpp:944`에서 시작하는 발췌입니다. 종료 줄은 963이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `cbc12aaba21898e519c8599faec5e998b408162912a507880b162ee6787cf8b0`
    
    ```text
    \brief Notify camera disconnection
     *
     * This function is used to notify the camera instance that the underlying
     * hardware has been unplugged. In response to the disconnection the camera
     * instance notifies the application by emitting the #disconnected signal, and
     * ensures that all new calls to the application-facing Camera API return an
     * error immediately.
     *
     * \todo Deal with pending requests if the camera is disconnected in a
     * running state.
     */
    void Camera::disconnect()
    {
    	LOG(Camera, Debug) << "Disconnecting camera " << id();
    
    	_d()->disconnect();
    	disconnected.emit();
    }
    
    int Camera::exportFrameBuffers(Stream *stream,
    ```


<!-- sdd:class-diagram -->
## 클래스 관계

화살표의 글자는 추출한 관계를 나타내며, 점선은 상속입니다. 화살표는 참조 대상 또는 기반 클래스를 향합니다. 호출 순서를 뜻하지 않습니다.

```mermaid
flowchart LR
  c0["Camera"]
  c1["CameraManager"]
  c2["Extensible"]:::context
  c3["Object"]:::context
  c4["Request"]
  c0 -.->|상속| c2
  c0 -.->|상속| c3
  c1 -.->|상속| c2
  c1 -.->|상속| c3
  c4 -.->|상속| c2
  classDef context fill:#fafafa,stroke:#aaa,stroke-dasharray:4 3,color:#555
```
<!-- /sdd:class-diagram -->



## 관련 클래스

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::Camera` | `include/libcamera/camera.h:114` | `libcamera::Object`, `libcamera::Extensible` | Camera device |
| `libcamera::CameraManager` | `include/libcamera/camera_manager.h:24` | `libcamera::Object`, `libcamera::Extensible` | Provide access and manage all cameras in the system |
| `libcamera::Request` | `include/libcamera/request.h:29` | `libcamera::Extensible` | A frame capture request |

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `include/libcamera/camera.h`, `include/libcamera/camera_manager.h`, `include/libcamera/request.h`, `src/libcamera/camera.cpp`, `src/libcamera/camera_manager.cpp`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/request.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `212c689fcf`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-30 · 사람 검토 전

다음 단계: [요청 객체와 버퍼 수명](camera-requests.md)
