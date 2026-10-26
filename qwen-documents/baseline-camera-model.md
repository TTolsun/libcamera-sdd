---
generated_at: 2026-10-26T10:07:28+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: camera-model
generation_method: facts-and-llm
evidence_fingerprint: a96af74b999444db178c70bedba0faa5b926ada3745f201729217f17461e8002
semantic_review: human-review-required
agent: ollama/qwen3.5:9b
generated_design: {"schema": 1, "input_fingerprint": "a96af74b999444db178c70bedba0faa5b926ada3745f201729217f17461e8002", "answers": {"responsibility": [{"text": "`CameraManager` 는 시스템 내 모든 카메라 장치를 열거하고 연결하며, 애플리케이션이 libcamera 와 상호작용할 때의 진입점 역할을 합니다. 이 관리자는 생성된 모든 `Camera` 객체의 소유권을 가지며, 장치의 플러그인/언플러그인 시나리오에서 카메라의 수명 주기를 관리합니다.", "covers": ["responsibility"], "kind": "behavior", "quote": "\\class CameraManager\n * \\brief Provide access and manage all cameras in the system\n *\n * The camera manager is the entry point to libcamera. It enumerates devices,\n * associates them with pipeline managers, and provides access to the cameras\n * in the system to applications. The manager owns all Camera objects and\n * handles hot-plugging and hot-unplugging to manage the lifetime of cameras.\n *\n * To interact with libcamera, an application starts by creating a camera\n * manager instance. Only a single instance of the camera manager may exist at\n * a time. Attempting to create a second instance without first deleting the\n * existing instance results in undefined behaviour.\n *\n * The manager is initially stopped, and shall be started with start(). This\n * will enumerate all the cameras present in the system, which can then be\n * listed with list() and retrieved with get().\n *\n * Cameras are shared through std::shared_ptr<>, ensuring that a camera will\n * stay valid until the last reference is released without requiring any special\n * action from the application. Once the application has released all the\n * references it held to cameras, the camera manager can be stopped with\n * stop().\n */", "evidence": ["manager"]}, {"text": "`CameraManager` 는 초기에는 정지된 상태로 시작되며, start() 함수를 호출하여 시스템에 존재하는 모든 카메라를 열거해야 합니다. 애플리케이션은 list() 로 열거한 후 get() 를 사용하여 특정 카메라를 가져올 수 있습니다.", "covers": ["responsibility"], "kind": "behavior", "quote": "\\class CameraManager\n * \\brief Provide access and manage all cameras in the system\n *\n * The camera manager is the entry point to libcamera. It enumerates devices,\n * associates them with pipeline managers, and provides access to the cameras\n * in the system to applications. The manager owns all Camera objects and\n * handles hot-plugging and hot-unplugging to manage the lifetime of cameras.\n *\n * To interact with libcamera, an application starts by creating a camera\n * manager instance. Only a single instance of the camera manager may exist at\n * a time. Attempting to create a second instance without first deleting the\n * existing instance results in undefined behaviour.\n *\n * The manager is initially stopped, and shall be started with start(). This\n * will enumerate all the cameras present in the system, which can then be\n * listed with list() and retrieved with get().\n *\n * Cameras are shared through std::shared_ptr<>, ensuring that a camera will\n * stay valid until the last reference is released without requiring any special\n * action from the application. Once the application has released all the\n * references it held to cameras, the camera manager can be stopped with\n * stop().\n */", "evidence": ["manager"]}, {"text": "`CameraManager` 는 `Camera` 객체를 std::shared_ptr< > 을 통해 공유하므로, 애플리케이션이 마지막 참조를 해제할 때까지 카메라가 유효하게 유지됩니다. 애플리케이션이 모든 카메라 참조를 해제한 후에는 stop() 함수를 호출하여 `CameraManager` 를 정지할 수 있습니다.", "covers": ["responsibility"], "kind": "behavior", "quote": "\\class CameraManager\n * \\brief Provide access and manage all cameras in the system\n *\n * The camera manager is the entry point to libcamera. It enumerates devices,\n * associates them with pipeline managers, and provides access to the cameras\n * in the system to applications. The manager owns all Camera objects and\n * handles hot-plugging and hot-unplugging to manage the lifetime of cameras.\n *\n * To interact with libcamera, an application starts by creating a camera\n * manager instance. Only a single instance of the camera manager may exist at\n * a time. Attempting to create a second instance without first deleting the\n * existing instance results in undefined behaviour.\n *\n * The manager is initially stopped, and shall be started with start(). This\n * will enumerate all the cameras present in the system, which can then be\n * listed with list() and retrieved with get().\n *\n * Cameras are shared through std::shared_ptr<>, ensuring that a camera will\n * stay valid until the last reference is released without requiring any special\n * action from the application. Once the application has released all the\n * references it held to cameras, the camera manager can be stopped with\n * stop().\n */", "evidence": ["manager"]}, {"text": "`Camera` 객체는 단일 이미지 소스에서 하나 이상의 이미지 스트림을 생성할 수 있는 장치를 모델링하며, libcamera 가 제공하는 중앙 객체입니다. `Camera` 인스턴스는 create() 함수를 사용하여 반환되는 shared pointer 로 생성해야 하며, 직접적인 생성자와 파괴자는 비공개로 정의되어 있습니다.", "covers": ["responsibility"], "kind": "behavior", "quote": "The Camera class models a camera capable of producing one or more image\n * streams from a single image source. It provides the main interface to\n * configuring and controlling the device, and capturing image streams. It is\n * the central object exposed by libcamera.\n *\n * To support the central nature of Camera objects, libcamera manages the\n * lifetime of camera instances with std::shared_ptr<>. Instances shall be\n * created with the create() function which returns a shared pointer. The\n * Camera constructors and destructor are private, to prevent instances from\n * being constructed and destroyed manually.\n *\n * \\section camera_operation", "evidence": ["camera"]}, {"text": "`Camera` 인스턴스는 std::shared_ptr< > 을 사용하여 수명 주기를 관리하므로, 애플리케이션은 명시적인 추가 작업 없이 참조를 해제하면 자동으로 처리됩니다. `Camera` 객체의 생성과 파괴는 libcamera 내부에서 제어되므로 수동으로 조작해서는 안 됩니다.", "covers": ["responsibility"], "kind": "behavior", "quote": "The Camera class models a camera capable of producing one or more image\n * streams from a single image source. It provides the main interface to\n * configuring and controlling the device, and capturing image streams. It is\n * the central object exposed by libcamera.\n *\n * To support the central nature of Camera objects, libcamera manages the\n * lifetime of camera instances with std::shared_ptr<>. Instances shall be\n * created with the create() function which returns a shared pointer. The\n * Camera constructors and destructor are private, to prevent instances from\n * being constructed and destroyed manually.\n *\n * \\section camera_operation", "evidence": ["camera"]}, {"text": "`Request` 는 프레임 캡처 요청을 나타내며, 애플리케이션이 각 프레임별로 버퍼와 컨트롤을 연결하여 카메라 장치에 처리를 위해 대기열에 넣을 수 있게 합니다. `Request` 객체는 `Camera` 를 통해 생성되며, 생성 시점에는 opaque cookie 가 저장되어 애플리케이션에서 요청 완료 핸들러에서 외부 리소스와 매핑하는 데 사용됩니다.", "covers": ["responsibility"], "kind": "behavior", "quote": "\\class Request\n * \\brief A frame capture request\n *\n * A Request allows an application to associate buffers and controls on a\n * per-frame basis to be queued to the camera device for processing.\n */", "evidence": ["request"]}, {"text": "`Request` 는 `Camera` *camera 와 uint64_t cookie 를 인자로 받는 생성자를 통해 생성되며, 이 cookie 는 요청 내내 접근 가능한 불투명한 식별자입니다. 애플리케이션은 요청 완료 핸들러에서 이 cookie 를 사용하여 외부 리소스와 매핑할 수 있지만, libcamera 에서는 완전히 불투명하게 처리됩니다.", "covers": ["responsibility"], "kind": "behavior", "quote": "/**\n * \\brief Create a capture request for a camera\n * \\param[in] camera The camera that creates the request\n * \\param[in] cookie Opaque cookie for application use\n *\n * The \\a cookie is stored in the request and is accessible through the\n * cookie() function at any time. It is typically used by applications to map\n * the request to an external resource in the request completion handler, and is\n * completely opaque to libcamera.\n */\nRequest::Request(Camera *camera, uint64_t cookie)", "evidence": ["request"]}], "state": [{"text": "카메라는 `release()`를 호출하면 `Available` 상태로, `acquire()`를 호출하면 `Acquired` 상태로 전이합니다. `Acquired` 상태에서는 `release()`로 다시 `Available` 상태로 되돌아가거나, `configure()`를 호출하여 `Configured` 상태로 넘어갈 수 있습니다.", "covers": ["state"], "kind": "behavior", "quote": "\\section camera_operation Operating the Camera\n *\n * An application needs to perform a sequence of operations on a camera before\n * it is ready to process requests. The camera needs to be acquired and\n * configured to prepare the camera for capture. Once started the camera can\n * process requests until it is stopped. When an application is done with a\n * camera, the camera needs to be released.\n *\n * An application may start and stop a camera multiple times as long as it is\n * not released. The camera may also be reconfigured.\n *\n * Functions that affect the camera state as defined below are generally not\n * synchronized with each other by the Camera class. The caller is responsible\n * for ensuring their synchronization if necessary.\n *\n * \\subsection Camera States\n *\n * To help manage the sequence of operations needed to control the camera a set\n * of states are defined. Each state describes which operations may be performed\n * on the camera. Performing an operation not allowed in the camera state\n * results in undefined behaviour. Operations not listed at all in the state\n * diagram are allowed in all states.\n *\n * \\dot\n * digraph camera_state_machine {\n *   node [shape = doublecircle ]; Available;\n *   node [shape = circle ]; Acquired;\n *   node [shape = circle ]; Configured;\n *   node [shape = circle ]; Stopping;\n *   node [shape = circle ]; Running;\n *\n *   Available -> Available [label = \"release()\"];\n *   Available -> Acquired [label = \"acquire()\"];\n *\n *   Acquired -> Available [label = \"release()\"];\n *   Acquired -> Configured [label = \"configure()\"];\n *\n *   Configured -> Available [label = \"release()\"];\n *   Configured -> Configured [label = \"configure(), createRequest()\"];\n *   Configured -> Running [label = \"start()\"];\n *\n *   Running -> Stopping [label = \"stop()\"];\n *   Stopping -> Configured;\n *   Running -> Running [label = \"createRequest(), queueRequest()\"];\n * }\n * \\enddot", "evidence": ["states"]}, {"text": "`Configured` 상태에서는 `release()`로 `Available` 상태로 되돌아가거나, `configure()` 또는 `createRequest()`를 호출하여 같은 상태를 유지할 수 있으며, `start()`를 호출하면 `Running` 상태로 전이합니다.", "covers": ["state"], "kind": "behavior", "quote": "\\section camera_operation Operating the Camera\n *\n * An application needs to perform a sequence of operations on a camera before\n * it is ready to process requests. The camera needs to be acquired and\n * configured to prepare the camera for capture. Once started the camera can\n * process requests until it is stopped. When an application is done with a\n * camera, the camera needs to be released.\n *\n * An application may start and stop a camera multiple times as long as it is\n * not released. The camera may also be reconfigured.\n *\n * Functions that affect the camera state as defined below are generally not\n * synchronized with each other by the Camera class. The caller is responsible\n * for ensuring their synchronization if necessary.\n *\n * \\subsection Camera States\n *\n * To help manage the sequence of operations needed to control the camera a set\n * of states are defined. Each state describes which operations may be performed\n * on the camera. Performing an operation not allowed in the camera state\n * results in undefined behaviour. Operations not listed at all in the state\n * diagram are allowed in all states.\n *\n * \\dot\n * digraph camera_state_machine {\n *   node [shape = doublecircle ]; Available;\n *   node [shape = circle ]; Acquired;\n *   node [shape = circle ]; Configured;\n *   node [shape = circle ]; Stopping;\n *   node [shape = circle ]; Running;\n *\n *   Available -> Available [label = \"release()\"];\n *   Available -> Acquired [label = \"acquire()\"];\n *\n *   Acquired -> Available [label = \"release()\"];\n *   Acquired -> Configured [label = \"configure()\"];\n *\n *   Configured -> Available [label = \"release()\"];\n *   Configured -> Configured [label = \"configure(), createRequest()\"];\n *   Configured -> Running [label = \"start()\"];\n *\n *   Running -> Stopping [label = \"stop()\"];\n *   Stopping -> Configured;\n *   Running -> Running [label = \"createRequest(), queueRequest()\"];\n * }\n * \\enddot", "evidence": ["states"]}, {"text": "`Running` 상태에서는 `stop()`를 호출하여 `Stopping` 상태로 전이하고, `createRequest()` 또는 `queueRequest()`를 호출하여 같은 상태를 유지할 수 있습니다. `Stopping` 상태는 자동으로 `Configured` 상태로 전이합니다.", "covers": ["state"], "kind": "behavior", "quote": "\\section camera_operation Operating the Camera\n *\n * An application needs to perform a sequence of operations on a camera before\n * it is ready to process requests. The camera needs to be acquired and\n * configured to prepare the camera for capture. Once started the camera can\n * process requests until it is stopped. When an application is done with a\n * camera, the camera needs to be released.\n *\n * An application may start and stop a camera multiple times as long as it is\n * not released. The camera may also be reconfigured.\n *\n * Functions that affect the camera state as defined below are generally not\n * synchronized with each other by the Camera class. The caller is responsible\n * for ensuring their synchronization if necessary.\n *\n * \\subsection Camera States\n *\n * To help manage the sequence of operations needed to control the camera a set\n * of states are defined. Each state describes which operations may be performed\n * on the camera. Performing an operation not allowed in the camera state\n * results in undefined behaviour. Operations not listed at all in the state\n * diagram are allowed in all states.\n *\n * \\dot\n * digraph camera_state_machine {\n *   node [shape = doublecircle ]; Available;\n *   node [shape = circle ]; Acquired;\n *   node [shape = circle ]; Configured;\n *   node [shape = circle ]; Stopping;\n *   node [shape = circle ]; Running;\n *\n *   Available -> Available [label = \"release()\"];\n *   Available -> Acquired [label = \"acquire()\"];\n *\n *   Acquired -> Available [label = \"release()\"];\n *   Acquired -> Configured [label = \"configure()\"];\n *\n *   Configured -> Available [label = \"release()\"];\n *   Configured -> Configured [label = \"configure(), createRequest()\"];\n *   Configured -> Running [label = \"start()\"];\n *\n *   Running -> Stopping [label = \"stop()\"];\n *   Stopping -> Configured;\n *   Running -> Running [label = \"createRequest(), queueRequest()\"];\n * }\n * \\enddot", "evidence": ["states"]}, {"text": "`createRequest()`와 `queueRequest()`는 `Configured` 상태에서는 허용되지만, `Running` 상태에서도 허용됩니다. 그러나 `start()`는 오직 `Configured` 상태에서만 호출할 수 있습니다.", "covers": ["state"], "kind": "behavior", "quote": "\\brief Start capture from camera\n * \\param[in] controls Controls to be applied before starting the Camera\n *\n * Start the camera capture session, optionally providing a list of controls to\n * apply before starting. Once the camera is started the application can queue\n * requests to the camera to process and return to the application until the\n * capture session is terminated with \\a stop().\n *\n * \\context This function may only be called when the camera is in the\n * Configured state as defined in \\ref camera_operation, and shall be\n * synchronized by the caller with other functions that affect the camera\n * state.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not in a state where it can be started\n */\nint Camera::start(const ControlList *controls)", "evidence": ["start"]}, {"text": "`Camera::start()` 함수는 호출자가 다른 카메라 상태 변경 함수와 동기화해야 하며, `Camera` 클래스는 일반적으로 이러한 동기화를 보장하지 않습니다. 따라서 호출자는 필요한 경우 스스로 동기화를 담당해야 합니다.", "covers": ["state"], "kind": "behavior", "quote": "\\brief Start capture from camera\n * \\param[in] controls Controls to be applied before starting the Camera\n *\n * Start the camera capture session, optionally providing a list of controls to\n * apply before starting. Once the camera is started the application can queue\n * requests to the camera to process and return to the application until the\n * capture session is terminated with \\a stop().\n *\n * \\context This function may only be called when the camera is in the\n * Configured state as defined in \\ref camera_operation, and shall be\n * synchronized by the caller with other functions that affect the camera\n * state.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not in a state where it can be started\n */\nint Camera::start(const ControlList *controls)", "evidence": ["start"]}], "request": [{"text": "응용 프로그램은 먼저 `Camera::createRequest()` 함수를 호출하여 빈 요청 객체를 생성해야 합니다. 이 함수는 요청의 소유권을 호출자에게 넘기며, 호출자는 완료 핸들러에서 삭제하거나 상태 초기화를 통해 재사용할 책임이 있습니다.", "covers": ["request"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest(uint64_t cookie)", "evidence": ["create"]}, {"text": "생성된 요청은 버퍼가 없으면 유효하지 않으므로, `Request::addBuffer()` 함수를 호출하여 각 스트림에 하나 이상의 캡처 버퍼를 추가해야 합니다. 같은 스트림에 이미 버퍼가 있으면 `-EEXIST` 오류를 반환합니다.", "covers": ["request"], "kind": "behavior", "quote": "\\brief Add a FrameBuffer with its associated Stream to the Request\n * \\param[in] stream The stream the buffer belongs to\n * \\param[in] buffer The FrameBuffer to add to the request\n * \\param[in] fence The optional fence\n *\n * A reference to the buffer is stored in the request. The caller is responsible\n * for ensuring that the buffer will remain valid until the request complete\n * callback is called.\n *\n * A request can only contain one buffer per stream. If a buffer has already\n * been added to the request for the same stream, this function returns -EEXIST.\n *\n * A Fence can be optionally associated with the \\a buffer.\n *\n * When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.\n *\n * If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request. Attempting to add a buffer that still\n * contains a fence to a request will result in this function returning -EEXIST.\n *\n * \\sa FrameBuffer::releaseFence()\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -EEXIST The request already contains a buffer for the stream\n *  or the buffer still references a fence\n * \\retval -EINVAL The buffer does not reference a valid Stream\n */\nint Request::addBuffer(const Stream *stream, FrameBuffer *buffer,", "evidence": ["buffer"]}, {"text": "버퍼 연결이 완료되면 카메라 상태가 `Running`인지 확인하고, 요청이 해당 카메라에서 생성되었는지 검증한 뒤 `Camera::queueRequest()` 함수를 호출하여 요청을 큐에 넣습니다.", "covers": ["request"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();", "evidence": ["queue"]}, {"text": "`Camera::queueRequest()` 내부에서는 요청 상태가 `RequestPending`인지, 버퍼가 비어있지 않은지, 스트림이 활성화되었는지 등 여러 가지 조건을 검사합니다. 모든 조건이 충족되면 요청은 파이프라인 핸들러로 전달되어 처리됩니다.", "covers": ["request"], "kind": "behavior", "quote": "if (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}", "evidence": ["queue"]}, {"text": "요청이 큐에 성공적으로 추가되면 카메라는 `requestCompleted` 신호를 통해 완료 통지를 보냅니다. 응용 프로그램은 이 신호를 처리하여 요청을 삭제하거나 재사용할 수 있습니다.", "covers": ["request"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();", "evidence": ["queue"]}], "lifetime": [{"text": "`Camera::createRequest()` 함수는 요청 객체의 소유권을 호출자에게 넘겨주며, 호출자는 해당 요청을 삭제할 책임이 있습니다.", "covers": ["lifetime"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest(uint64_t cookie)", "evidence": ["create"]}, {"text": "요청이 완료된 후 콜백에서 요청을 삭제하거나, `Request::reuse()` 를 호출하여 상태를 초기화한 뒤 재사용할 수 있습니다.", "covers": ["lifetime"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest(uint64_t cookie)", "evidence": ["create"]}, {"text": "`Request::addBuffer()` 함수는 요청이 완료될 콜백까지 버퍼가 유효하게 유지되도록 보장해야 합니다.", "covers": ["lifetime"], "kind": "behavior", "quote": "\\brief Add a FrameBuffer with its associated Stream to the Request\n * \\param[in] stream The stream the buffer belongs to\n * \\param[in] buffer The FrameBuffer to add to the request\n * \\param[in] fence The optional fence\n *\n * A reference to the buffer is stored in the request. The caller is responsible\n * for ensuring that the buffer will remain valid until the request complete\n * callback is called.\n *\n * A request can only contain one buffer per stream. If a buffer has already\n * been added to the request for the same stream, this function returns -EEXIST.\n *\n * A Fence can be optionally associated with the \\a buffer.\n *\n * When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.\n *\n * If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request. Attempting to add a buffer that still\n * contains a fence to a request will result in this function returning -EEXIST.\n *\n * \\sa FrameBuffer::releaseFence()\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -EEXIST The request already contains a buffer for the stream\n *  or the buffer still references a fence\n * \\retval -EINVAL The buffer does not reference a valid Stream\n */\nint Request::addBuffer(const Stream *stream, FrameBuffer *buffer,", "evidence": ["buffer"]}, {"text": "addBuffer() 함수는 동일한 스트림에 이미 버퍼가 추가된 경우 또는 버퍼에 펜스가 남아있는 경우 -EEXIST 오류를 반환합니다.", "covers": ["lifetime"], "kind": "behavior", "quote": "\\brief Add a FrameBuffer with its associated Stream to the Request\n * \\param[in] stream The stream the buffer belongs to\n * \\param[in] buffer The FrameBuffer to add to the request\n * \\param[in] fence The optional fence\n *\n * A reference to the buffer is stored in the request. The caller is responsible\n * for ensuring that the buffer will remain valid until the request complete\n * callback is called.\n *\n * A request can only contain one buffer per stream. If a buffer has already\n * been added to the request for the same stream, this function returns -EEXIST.\n *\n * A Fence can be optionally associated with the \\a buffer.\n *\n * When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.\n *\n * If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request. Attempting to add a buffer that still\n * contains a fence to a request will result in this function returning -EEXIST.\n *\n * \\sa FrameBuffer::releaseFence()\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -EEXIST The request already contains a buffer for the stream\n *  or the buffer still references a fence\n * \\retval -EINVAL The buffer does not reference a valid Stream\n */\nint Request::addBuffer(const Stream *stream, FrameBuffer *buffer,", "evidence": ["buffer"]}, {"text": "`Request::reuse`(ReuseBuffers) 를 호출하면 이전에 addBuffer() 로 추가된 버퍼들이 다시 요청에 연결됩니다.", "covers": ["lifetime"], "kind": "behavior", "quote": "if (flags & ReuseBuffers) {\n\t\tfor (const auto &[stream, buffer] : bufferMap_) {\n\t\t\tbuffer->_d()->setRequest(this);\n\t\t\t_d()->pending_.insert(buffer);\n\t\t}\n\t} else {\n\t\tbufferMap_.clear();\n\t}", "evidence": ["reuse"]}, {"text": "ReuseBuffers 플래그를 사용하지 않으면 bufferMap_ 가 비워지고, 기존 버퍼는 더 이상 요청과 연결되지 않습니다.", "covers": ["lifetime"], "kind": "behavior", "quote": "if (flags & ReuseBuffers) {\n\t\tfor (const auto &[stream, buffer] : bufferMap_) {\n\t\t\tbuffer->_d()->setRequest(this);\n\t\t\t_d()->pending_.insert(buffer);\n\t\t}\n\t} else {\n\t\tbufferMap_.clear();\n\t}", "evidence": ["reuse"]}, {"text": "ReuseBuffers 플래그를 설정할 경우 펜스가 사용된 상태라면 이 플래그를 사용하지 않아야 합니다.", "covers": ["lifetime"], "kind": "limitation", "quote": "\\enum Request::ReuseFlag\n * Flags to control the behavior of Request::reuse()\n * \\var Request::Default\n * Don't reuse buffers\n * \\var Request::ReuseBuffers\n * Reuse the buffers that were previously added by addBuffer()\n *\n * \\note Fences associated with the buffers are not reused.\n *  This flag should not be used if fences are used.\n */", "evidence": ["reuse-flags"]}, {"text": "addBuffer() 함수에 유효한 펜스가 전달되면 성공 시 해당 펜스는 버퍼로 이동되어 요청이 큐에 추가될 때까지 신호가 기다려집니다.", "covers": ["lifetime"], "kind": "behavior", "quote": "\\brief Add a FrameBuffer with its associated Stream to the Request\n * \\param[in] stream The stream the buffer belongs to\n * \\param[in] buffer The FrameBuffer to add to the request\n * \\param[in] fence The optional fence\n *\n * A reference to the buffer is stored in the request. The caller is responsible\n * for ensuring that the buffer will remain valid until the request complete\n * callback is called.\n *\n * A request can only contain one buffer per stream. If a buffer has already\n * been added to the request for the same stream, this function returns -EEXIST.\n *\n * A Fence can be optionally associated with the \\a buffer.\n *\n * When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.\n *\n * If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request. Attempting to add a buffer that still\n * contains a fence to a request will result in this function returning -EEXIST.\n *\n * \\sa FrameBuffer::releaseFence()\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -EEXIST The request already contains a buffer for the stream\n *  or the buffer still references a fence\n * \\retval -EINVAL The buffer does not reference a valid Stream\n */\nint Request::addBuffer(const Stream *stream, FrameBuffer *buffer,", "evidence": ["buffer"]}], "shutdown": [{"text": "`Camera::queueRequest()` 함수는 요청을 카메라에 대기열에 넣기 전에 여러 가지 오류 조건을 검사합니다. 먼저 카메라가 실행 중이 아닌 경우 `-EACCES` 오류를 반환하며, 요청이 해당 카메라에서 생성되지 않은 경우 `-EXDEV` 오류를 반환합니다. 또한 요청의 상태가 `RequestPending`이 아니면 `-EINVAL` 오류를 반환하고, 요청에 포함된 제어 목록 정보가 카메라의 현재 정보 맵과 일치하지 않으면 `-EINVAL` 오류를 반환합니다. 마지막으로 요청에 버퍼가 하나도 포함되지 않았거나 활성 스트림 목록에 해당 스트림이 존재하지 않는 경우에도 `-EINVAL` 오류를 반환하여 요청을 대기열에 추가하지 않습니다.", "covers": ["shutdown"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();", "evidence": ["queue"]}, {"text": "`Camera::stop()` 함수는 카메라가 실행 중이 아닌 경우 실제로 아무 작업도 수행하지 않고 즉시 `0`을 반환합니다. 이 함수는 카메라 상태가 실행 중이 아닐 때 호출되더라도 무조건 성공으로 처리되며, 실행 중인 상태에서만 접근 권한 검사와 상태 전환 및 동기화 작업을 진행합니다.", "covers": ["shutdown"], "kind": "behavior", "quote": "/*\n\t * \\todo Make calling stop() when not in 'Running' part of the state\n\t * machine rather than take this shortcut\n\t */\n\tif (!d->isRunning())\n\t\treturn 0;", "evidence": ["stop"]}, {"text": "`Camera::stop()` 함수는 카메라가 실행 중일 때 먼저 상태를 `CameraStopping`으로 전환한 후, `PipelineHandler::stop` 메서드를 `ConnectionTypeBlocking` 타입으로 호출하여 동기적으로 처리합니다. 이후 모든 대기 중인 요청이 취소되고 완료된 것을 확인한 뒤 상태를 다시 `CameraConfigured`로 되돌립니다.", "covers": ["shutdown"], "kind": "behavior", "quote": "d->pipe_->invokeMethod(&PipelineHandler::stop, ConnectionTypeBlocking,\n\t\t\t       this);", "evidence": ["stop"]}, {"text": "`Camera::queueRequest()` 함수는 요청이 완료되면 `requestCompleted` 신호를 통해 애플리케이션에 알림을 보냅니다. 반면 `Camera::stop()` 함수는 실행 중일 때 호출되면 모든 대기 중인 요청을 즉시 취소하고 오류 상태로 동기적으로 완료시킵니다.", "covers": ["shutdown"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();", "evidence": ["queue"]}], "concurrency": [{"text": "`Camera::createRequest()` 함수는 카메라 상태가 `Configured` 또는 `Running`일 때 호출할 수 있으며, 이 함수는 스레드 안전합니다. 반환된 요청의 소유권은 호출자에게 넘어가므로 호출자가 이를 삭제하거나 재사용해야 합니다.", "covers": ["concurrency"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest(uint64_t cookie)", "evidence": ["create"]}, {"text": "`Camera::queueRequest()` 함수는 카메라 상태가 `Running`일 때만 호출할 수 있으며, 이 함수도 스레드 안전합니다. 요청에 버퍼가 하나 이상 포함되어 있어야 하며, 요청은 해당 카메라에서 생성된 것만 큐잉됩니다.", "covers": ["concurrency"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();", "evidence": ["queue"]}, {"text": "`Camera::start()` 함수는 카메라 상태가 `Configured`일 때 호출되며, 호출자는 다른 상태 변경 함수와 동기화해야 합니다. 성공 시 0을 반환하고 실패 시 음수 오류 코드를 반환합니다.", "covers": ["concurrency"], "kind": "behavior", "quote": "\\brief Start capture from camera\n * \\param[in] controls Controls to be applied before starting the Camera\n *\n * Start the camera capture session, optionally providing a list of controls to\n * apply before starting. Once the camera is started the application can queue\n * requests to the camera to process and return to the application until the\n * capture session is terminated with \\a stop().\n *\n * \\context This function may only be called when the camera is in the\n * Configured state as defined in \\ref camera_operation, and shall be\n * synchronized by the caller with other functions that affect the camera\n * state.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not in a state where it can be started\n */\nint Camera::start(const ControlList *controls)", "evidence": ["start"]}, {"text": "`Camera::stop()` 함수는 어떤 카메라 상태에서도 호출할 수 있으며, 실행 중이 아닌 경우 무작동입니다. 호출자는 다른 상태 변경 함수와 동기화해야 하며, 성공 시 0을 반환합니다.", "covers": ["concurrency"], "kind": "behavior", "quote": "\\brief Stop capture from camera\n *\n * This function stops capturing and processing requests immediately. All\n * pending requests are cancelled and complete synchronously in an error state.\n *\n * \\context This function may be called in any camera state as defined in \\ref\n * camera_operation, and shall be synchronized by the caller with other\n * functions that affect the camera state. If called when the camera isn't\n * running, it is a no-op.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so can't be stopped\n */\nint Camera::stop()\n{\n\tPrivate *const d = _d();", "evidence": ["stop"]}, {"text": "`PipelineHandler::completeBuffer()` 함수는 `CameraManager` 스레드에서 호출되어야 하며, 버퍼 완료를 애플리케이션에 알리고 요청의 내부 버퍼 추적을 업데이트합니다.", "covers": ["concurrency"], "kind": "behavior", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}", "evidence": ["completion"]}, {"text": "`PipelineHandler::completeRequest()` 함수는 `CameraManager` 스레드에서 호출되어야 하며, 요청이 완료되었음을 카메라에 알립니다. 이 함수가 반환되면 파이프라인 핸들러는 더 이상 해당 요청을 관리하지 않습니다.", "covers": ["concurrency"], "kind": "behavior", "quote": "/**\n * \\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();", "evidence": ["completion"]}, {"text": "`PipelineHandler::cancelRequest()` 함수는 요청을 취소하고 완료하며, `completeRequest()`의 규칙이 동일하게 적용됩니다. 이 함수도 `CameraManager` 스레드에서 호출되어야 합니다.", "covers": ["concurrency"], "kind": "behavior", "quote": "/**\n * \\brief Cancel request and signal its completion\n * \\param[in] request The request to cancel\n *\n * This function cancels and completes the request. The same rules as for\n * completeRequest() apply.\n */\nvoid PipelineHandler::cancelRequest(Request *request)\n{\n\trequest->_d()->cancel();\n\tcompleteRequest(request);\n}", "evidence": ["completion"]}, {"text": "`Camera::bufferCompleted` 신호는 버퍼 완료를 애플리케이션에 알리기 위해 사용되며, `PipelineHandler::completeBuffer()`를 통해 호출됩니다. 이 신호는 애플리케이션이 완료된 버퍼를 처리하는 데 사용됩니다.", "covers": ["concurrency"], "kind": "behavior", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}", "evidence": ["completion"]}], "disconnection": [{"text": "if (currentState >= low && currentState <= high) 조건식이 참일 경우, 즉 현재 상태가 허용된 범위 내라면 함수는 0 을 반환합니다.", "covers": ["disconnection"], "kind": "behavior", "quote": "if (currentState >= low && currentState <= high)\n\t\treturn 0;\n\n\tASSERT(static_cast<unsigned int>(low) < std::size(camera_state_names) &&\n\t       static_cast<unsigned int>(high) < std::size(camera_state_names));\n\n\tLOG(Camera, Error) << \"Camera in \" << camera_state_names[currentState]\n\t\t\t   << \" state trying \" << from\n\t\t\t   << \"() requiring state between \"\n\t\t\t   << camera_state_names[low] << \" and \"\n\t\t\t   << camera_state_names[high];\n\n\treturn -EACCES;\n}\n\nvoid Camera::Private::disconnect()", "evidence": ["state-return"], "part_id": "access-state"}, {"text": "상태 범위를 벗어나 이 경로에 도달했을 때 마지막 return 문이 반환하는 오류 식별자는 -EACCES 입니다.", "covers": ["disconnection"], "kind": "behavior", "quote": "ASSERT(static_cast<unsigned int>(low) < std::size(camera_state_names) &&\n\t       static_cast<unsigned int>(high) < std::size(camera_state_names));\n\n\tLOG(Camera, Error) << \"Camera in \" << camera_state_names[currentState]\n\t\t\t   << \" state trying \" << from\n\t\t\t   << \"() requiring state between \"\n\t\t\t   << camera_state_names[low] << \" and \"\n\t\t\t   << camera_state_names[high];\n\n\treturn -EACCES;\n}", "evidence": ["state-failure"], "part_id": "state-failure"}, {"text": "if (!allowDisconnected && disconnected_) 조건식이 참일 경우 -ENODEV 값을 반환합니다.", "covers": ["disconnection"], "kind": "behavior", "quote": "if (!allowDisconnected && disconnected_)\n\t\treturn -ENODEV;", "evidence": ["disconnected-check"], "part_id": "access-disconnected"}, {"text": "`Private::disconnect` 함수는 카메라가 실행 중일 때 하드웨어가 제거된 경우 상태 변경을 수행하며, 이때 state_의 현재 값이 `Private::CameraRunning` 이라면 상태를 `Private::CameraConfigured` 로 변경하고, disconnected_ 변수에는 true 를 대입합니다.", "covers": ["disconnection"], "kind": "behavior", "quote": "void Camera::Private::disconnect()\n{\n\t/*\n\t * If the camera was running when the hardware was removed force the\n\t * state to Configured state to allow applications to free resources\n\t * and call release() before deleting the camera.\n\t */\n\tif (state_.load(std::memory_order_acquire) == Private::CameraRunning)\n\t\tstate_.store(Private::CameraConfigured, std::memory_order_release);\n\n\tdisconnected_ = true;\n}\n\nvoid Camera::Private::setState(State state)", "evidence": ["private-disconnect"], "part_id": "disconnect-state"}, {"text": "`Camera::disconnect` 함수는 먼저 _d() 객체의 disconnect 메서드를 호출한 후, disconnected 신호를 방출합니다.", "covers": ["disconnection"], "kind": "behavior", "quote": "void Camera::disconnect()\n{\n\tLOG(Camera, Debug) << \"Disconnecting camera \" << id();\n\n\t_d()->disconnect();\n\tdisconnected.emit();\n}\n\nint Camera::exportFrameBuffers(Stream *stream,", "evidence": ["notify-body"], "part_id": "notification"}, {"text": "카메라가 실행 중 상태일 때 연결이 끊기는 경우 처리해야 할 대기 중인 요청에 대해 대응해야 합니다.", "covers": ["disconnection"], "kind": "behavior", "quote": "\\todo Deal with pending requests if the camera is disconnected in a\n * running state.\n */", "evidence": ["notification"], "part_id": "pending"}]}, "topic_inputs": {"responsibility": "54d2abcd8bbf6adc701b26b13c667815e040a5da52569864f1a8512a038dbf58", "state": "8c06461f86c2e18b9affcc363863359e9d60e56f1b152f4d95beb8f92a42b2e7", "request": "2e22ffd2d08db53ea031d24c2098b957155a9f8e01728bda634c8174d986d3aa", "lifetime": "e03d8a7c9c2958f2efe2f88cf7a2ac514ba994221ea7d88bebf67b142e4a25be", "shutdown": "19c02fa1f0c347fa143fbc47fcb7085e860942647a99aa95acf5250ab1bb13ae", "concurrency": "64877e1f65825d3ec4293ff9a1c63d7933186898d076653cbbdd89ea5e3fd0d3", "disconnection": "d28911b21b2423f8671c9db00e5779bd90cf9be950723a837660ae359a78ba15"}, "reused_topics": [], "generated_topics": ["responsibility", "state", "request", "lifetime", "shutdown", "concurrency", "disconnection"], "topic_agents": {"responsibility": "ollama/qwen3.5:9b", "state": "ollama/qwen3.5:9b", "request": "ollama/qwen3.5:9b", "lifetime": "ollama/qwen3.5:9b", "shutdown": "ollama/qwen3.5:9b", "concurrency": "ollama/qwen3.5:9b", "disconnection": "ollama/qwen3.5:9b"}, "body_sha256": "043cfcb6d13de898f80ca7cfda7a9f4fdbc9526a03bab00243bc1a16d9112ce6"}
---

# 카메라와 요청 모델

**클래스의 책임, 요청과 버퍼의 수명, 상태 전이와 종료·동기화 계약을 코드 근거로 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 클래스별 책임 절을 확인합니다. | [클래스별 책임](#클래스별-책임) |
| 상태와 허용 호출 절을 확인합니다. | [상태와 허용 호출](#상태와-허용-호출) |
| 요청 생성과 완료 절을 확인합니다. | [요청 생성과 완료](#요청-생성과-완료) |
| 소유권과 재사용 절을 확인합니다. | [소유권과 재사용](#소유권과-재사용) |
| 오류와 종료 절을 확인합니다. | [오류와 종료](#오류와-종료) |
| 동시성과 실행 확인 절을 확인합니다. | [동시성과 실행 확인](#동시성과-실행-확인) |

## 클래스별 책임

`CameraManager` 는 시스템 내 모든 카메라 장치를 열거하고 연결하며, 애플리케이션이 libcamera 와 상호작용할 때의 진입점 역할을 합니다. 이 관리자는 생성된 모든 `Camera` 객체의 소유권을 가지며, 장치의 플러그인/언플러그인 시나리오에서 카메라의 수명 주기를 관리합니다. `src/libcamera/camera_manager.cpp:280`

`CameraManager` 는 초기에는 정지된 상태로 시작되며, start() 함수를 호출하여 시스템에 존재하는 모든 카메라를 열거해야 합니다. 애플리케이션은 list() 로 열거한 후 get() 를 사용하여 특정 카메라를 가져올 수 있습니다. `src/libcamera/camera_manager.cpp:280`

`CameraManager` 는 `Camera` 객체를 std::shared_ptr< > 을 통해 공유하므로, 애플리케이션이 마지막 참조를 해제할 때까지 카메라가 유효하게 유지됩니다. 애플리케이션이 모든 카메라 참조를 해제한 후에는 stop() 함수를 호출하여 `CameraManager` 를 정지할 수 있습니다. `src/libcamera/camera_manager.cpp:280`

`Camera` 객체는 단일 이미지 소스에서 하나 이상의 이미지 스트림을 생성할 수 있는 장치를 모델링하며, libcamera 가 제공하는 중앙 객체입니다. `Camera` 인스턴스는 create() 함수를 사용하여 반환되는 shared pointer 로 생성해야 하며, 직접적인 생성자와 파괴자는 비공개로 정의되어 있습니다. `src/libcamera/camera.cpp:758`

`Camera` 인스턴스는 std::shared_ptr< > 을 사용하여 수명 주기를 관리하므로, 애플리케이션은 명시적인 추가 작업 없이 참조를 해제하면 자동으로 처리됩니다. `Camera` 객체의 생성과 파괴는 libcamera 내부에서 제어되므로 수동으로 조작해서는 안 됩니다. `src/libcamera/camera.cpp:758`

`Request` 는 프레임 캡처 요청을 나타내며, 애플리케이션이 각 프레임별로 버퍼와 컨트롤을 연결하여 카메라 장치에 처리를 위해 대기열에 넣을 수 있게 합니다. `Request` 객체는 `Camera` 를 통해 생성되며, 생성 시점에는 opaque cookie 가 저장되어 애플리케이션에서 요청 완료 핸들러에서 외부 리소스와 매핑하는 데 사용됩니다. `src/libcamera/request.cpp:343`

`Request` 는 `Camera` *camera 와 uint64_t cookie 를 인자로 받는 생성자를 통해 생성되며, 이 cookie 는 요청 내내 접근 가능한 불투명한 식별자입니다. 애플리케이션은 요청 완료 핸들러에서 이 cookie 를 사용하여 외부 리소스와 매핑할 수 있지만, libcamera 에서는 완전히 불투명하게 처리됩니다. `src/libcamera/request.cpp:343`

근거 원문: [src/libcamera/camera_manager.cpp:280](#source-fbcf3effd2584b79) · [src/libcamera/camera.cpp:758](#source-6c066281dcce33d6) · [src/libcamera/request.cpp:343](#source-abce7dd469896527)

## 상태와 허용 호출

카메라는 `release()`를 호출하면 `Available` 상태로, `acquire()`를 호출하면 `Acquired` 상태로 전이합니다. `Acquired` 상태에서는 `release()`로 다시 `Available` 상태로 되돌아가거나, `configure()`를 호출하여 `Configured` 상태로 넘어갈 수 있습니다. `src/libcamera/camera.cpp:769`

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

`Configured` 상태에서는 `release()`로 `Available` 상태로 되돌아가거나, `configure()` 또는 `createRequest()`를 호출하여 같은 상태를 유지할 수 있으며, `start()`를 호출하면 `Running` 상태로 전이합니다. `src/libcamera/camera.cpp:769`

`Running` 상태에서는 `stop()`를 호출하여 `Stopping` 상태로 전이하고, `createRequest()` 또는 `queueRequest()`를 호출하여 같은 상태를 유지할 수 있습니다. `Stopping` 상태는 자동으로 `Configured` 상태로 전이합니다. `src/libcamera/camera.cpp:769`

`createRequest()`와 `queueRequest()`는 `Configured` 상태에서는 허용되지만, `Running` 상태에서도 허용됩니다. 그러나 `start()`는 오직 `Configured` 상태에서만 호출할 수 있습니다. `src/libcamera/camera.cpp:1383`

`Camera::start()` 함수는 호출자가 다른 카메라 상태 변경 함수와 동기화해야 하며, `Camera` 클래스는 일반적으로 이러한 동기화를 보장하지 않습니다. 따라서 호출자는 필요한 경우 스스로 동기화를 담당해야 합니다. `src/libcamera/camera.cpp:1383`

근거 원문: [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d) · [src/libcamera/camera.cpp:1383](#source-617d53c4c7de2c0c)

## 요청 생성과 완료

응용 프로그램은 먼저 `Camera::createRequest()` 함수를 호출하여 빈 요청 객체를 생성해야 합니다. 이 함수는 요청의 소유권을 호출자에게 넘기며, 호출자는 완료 핸들러에서 삭제하거나 상태 초기화를 통해 재사용할 책임이 있습니다. `src/libcamera/camera.cpp:1243`

생성된 요청은 버퍼가 없으면 유효하지 않으므로, `Request::addBuffer()` 함수를 호출하여 각 스트림에 하나 이상의 캡처 버퍼를 추가해야 합니다. 같은 스트림에 이미 버퍼가 있으면 `-EEXIST` 오류를 반환합니다. `src/libcamera/request.cpp:442`

버퍼 연결이 완료되면 카메라 상태가 `Running`인지 확인하고, 요청이 해당 카메라에서 생성되었는지 검증한 뒤 `Camera::queueRequest()` 함수를 호출하여 요청을 큐에 넣습니다. `src/libcamera/camera.cpp:1308`

`Camera::queueRequest()` 내부에서는 요청 상태가 `RequestPending`인지, 버퍼가 비어있지 않은지, 스트림이 활성화되었는지 등 여러 가지 조건을 검사합니다. 모든 조건이 충족되면 요청은 파이프라인 핸들러로 전달되어 처리됩니다. `src/libcamera/camera.cpp:1308`

요청이 큐에 성공적으로 추가되면 카메라는 `requestCompleted` 신호를 통해 완료 통지를 보냅니다. 응용 프로그램은 이 신호를 처리하여 요청을 삭제하거나 재사용할 수 있습니다. `src/libcamera/camera.cpp:1308`

근거 원문: [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) · [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1)

## 소유권과 재사용

`Camera::createRequest()` 함수는 요청 객체의 소유권을 호출자에게 넘겨주며, 호출자는 해당 요청을 삭제할 책임이 있습니다. `src/libcamera/camera.cpp:1243`

<!-- sdd:visual:request-ownership -->
### 요청과 버퍼를 유지할 기간

요청의 소유권은 호출자에게 있습니다. 버퍼 참조를 연결해도 호출자의 버퍼 유지 책임은 계속됩니다.

```mermaid
flowchart TB
%% sdd:translations {"Request가 버퍼를 참조": "Request references buffer", "addBuffer()": "addBuffer()", "reuse() 후 다시 제출": "Reset before requeue", "완료 핸들러에서 삭제 가능": "May delete in completion <br/>handler", "요청 삭제": "Delete request", "요청 완료 콜백": "Request completion callback", "이 시점까지 버퍼를 유효하게 <br/>유지": "Keep buffer valid until <br/>this point", "재사용 전 상태 초기화": "Reset state before reuse", "호출자가 Request를 소유": "Caller owns Request"}
  v_caller["호출자가 Request를 소유"]
  v_buffer["Request가 버퍼를 참조"]
  v_callback["요청 완료 콜백"]
  v_delete["요청 삭제"]
  v_reuse["reuse() 후 다시 제출"]
  v_caller -->|"addBuffer()"| v_buffer
  v_buffer -->|"이 시점까지 버퍼를 유효하게 <br/>유지"| v_callback
  v_callback -->|"완료 핸들러에서 삭제 가능"| v_delete
  v_callback -->|"재사용 전 상태 초기화"| v_reuse
```

[Mermaid 원문](camera-model.request-ownership.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | 호출자가 Request를 소유 | [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) |
    | Request가 버퍼를 참조 | [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) |
    | 요청 완료 콜백 | [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) |
    | 요청 삭제 | [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) |
    | reuse() 후 다시 제출 | [src/libcamera/request.cpp:376](#source-38494771cb29cc8c) |
    | addBuffer() | [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) |
    | 이 시점까지 버퍼를 유효하게 유지 | [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) |
    | 완료 핸들러에서 삭제 가능 | [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) |
    | 재사용 전 상태 초기화 | [src/libcamera/request.cpp:376](#source-38494771cb29cc8c) |
<!-- /sdd:visual:request-ownership -->

요청이 완료된 후 콜백에서 요청을 삭제하거나, `Request::reuse()` 를 호출하여 상태를 초기화한 뒤 재사용할 수 있습니다. `src/libcamera/camera.cpp:1243`

`Request::addBuffer()` 함수는 요청이 완료될 콜백까지 버퍼가 유효하게 유지되도록 보장해야 합니다. `src/libcamera/request.cpp:442`

addBuffer() 함수는 동일한 스트림에 이미 버퍼가 추가된 경우 또는 버퍼에 펜스가 남아있는 경우 -EEXIST 오류를 반환합니다. `src/libcamera/request.cpp:442`

`Request::reuse`(ReuseBuffers) 를 호출하면 이전에 addBuffer() 로 추가된 버퍼들이 다시 요청에 연결됩니다. `src/libcamera/request.cpp:376`

ReuseBuffers 플래그를 사용하지 않으면 bufferMap_ 가 비워지고, 기존 버퍼는 더 이상 요청과 연결되지 않습니다. `src/libcamera/request.cpp:376`

실행 확인 항목: ReuseBuffers 플래그를 설정할 경우 펜스가 사용된 상태라면 이 플래그를 사용하지 않아야 합니다. `src/libcamera/request.cpp:326`

addBuffer() 함수에 유효한 펜스가 전달되면 성공 시 해당 펜스는 버퍼로 이동되어 요청이 큐에 추가될 때까지 신호가 기다려집니다. `src/libcamera/request.cpp:442`

근거 원문: [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) · [src/libcamera/request.cpp:376](#source-38494771cb29cc8c) · [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) · [src/libcamera/request.cpp:326](#source-447804db33308244)

## 오류와 종료

`Camera::queueRequest()` 함수는 요청을 카메라에 대기열에 넣기 전에 여러 가지 오류 조건을 검사합니다. 먼저 카메라가 실행 중이 아닌 경우 `-EACCES` 오류를 반환하며, 요청이 해당 카메라에서 생성되지 않은 경우 `-EXDEV` 오류를 반환합니다. 또한 요청의 상태가 `RequestPending`이 아니면 `-EINVAL` 오류를 반환하고, 요청에 포함된 제어 목록 정보가 카메라의 현재 정보 맵과 일치하지 않으면 `-EINVAL` 오류를 반환합니다. 마지막으로 요청에 버퍼가 하나도 포함되지 않았거나 활성 스트림 목록에 해당 스트림이 존재하지 않는 경우에도 `-EINVAL` 오류를 반환하여 요청을 대기열에 추가하지 않습니다. `src/libcamera/camera.cpp:1308`

`Camera::stop()` 함수는 카메라가 실행 중이 아닌 경우 실제로 아무 작업도 수행하지 않고 즉시 `0`을 반환합니다. 이 함수는 카메라 상태가 실행 중이 아닐 때 호출되더라도 무조건 성공으로 처리되며, 실행 중인 상태에서만 접근 권한 검사와 상태 전환 및 동기화 작업을 진행합니다. `src/libcamera/camera.cpp:1431`

`Camera::stop()` 함수는 카메라가 실행 중일 때 먼저 상태를 `CameraStopping`으로 전환한 후, `PipelineHandler::stop` 메서드를 `ConnectionTypeBlocking` 타입으로 호출하여 동기적으로 처리합니다. 이후 모든 대기 중인 요청이 취소되고 완료된 것을 확인한 뒤 상태를 다시 `CameraConfigured`로 되돌립니다. `src/libcamera/camera.cpp:1431`

`Camera::queueRequest()` 함수는 요청이 완료되면 `requestCompleted` 신호를 통해 애플리케이션에 알림을 보냅니다. 반면 `Camera::stop()` 함수는 실행 중일 때 호출되면 모든 대기 중인 요청을 즉시 취소하고 오류 상태로 동기적으로 완료시킵니다. `src/libcamera/camera.cpp:1308`

근거 원문: [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/camera.cpp:1431](#source-e09324743def3f09)

## 동시성과 실행 확인

`Camera::createRequest()` 함수는 카메라 상태가 `Configured` 또는 `Running`일 때 호출할 수 있으며, 이 함수는 스레드 안전합니다. 반환된 요청의 소유권은 호출자에게 넘어가므로 호출자가 이를 삭제하거나 재사용해야 합니다. `src/libcamera/camera.cpp:1243`

`Camera::queueRequest()` 함수는 카메라 상태가 `Running`일 때만 호출할 수 있으며, 이 함수도 스레드 안전합니다. 요청에 버퍼가 하나 이상 포함되어 있어야 하며, 요청은 해당 카메라에서 생성된 것만 큐잉됩니다. `src/libcamera/camera.cpp:1308`

`Camera::start()` 함수는 카메라 상태가 `Configured`일 때 호출되며, 호출자는 다른 상태 변경 함수와 동기화해야 합니다. 성공 시 0을 반환하고 실패 시 음수 오류 코드를 반환합니다. `src/libcamera/camera.cpp:1383`

`Camera::stop()` 함수는 어떤 카메라 상태에서도 호출할 수 있으며, 실행 중이 아닌 경우 무작동입니다. 호출자는 다른 상태 변경 함수와 동기화해야 하며, 성공 시 0을 반환합니다. `src/libcamera/camera.cpp:1431`

`PipelineHandler::completeBuffer()` 함수는 `CameraManager` 스레드에서 호출되어야 하며, 버퍼 완료를 애플리케이션에 알리고 요청의 내부 버퍼 추적을 업데이트합니다. `src/libcamera/pipeline_handler.cpp:547`

`PipelineHandler::completeRequest()` 함수는 `CameraManager` 스레드에서 호출되어야 하며, 요청이 완료되었음을 카메라에 알립니다. 이 함수가 반환되면 파이프라인 핸들러는 더 이상 해당 요청을 관리하지 않습니다. `src/libcamera/pipeline_handler.cpp:547`

`PipelineHandler::cancelRequest()` 함수는 요청을 취소하고 완료하며, `completeRequest()`의 규칙이 동일하게 적용됩니다. 이 함수도 `CameraManager` 스레드에서 호출되어야 합니다. `src/libcamera/pipeline_handler.cpp:547`

`Camera::bufferCompleted` 신호는 버퍼 완료를 애플리케이션에 알리기 위해 사용되며, `PipelineHandler::completeBuffer()`를 통해 호출됩니다. 이 신호는 애플리케이션이 완료된 버퍼를 처리하는 데 사용됩니다. `src/libcamera/pipeline_handler.cpp:547`

근거 원문: [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) · [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/camera.cpp:1383](#source-617d53c4c7de2c0c) · [src/libcamera/camera.cpp:1431](#source-e09324743def3f09) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a)

## 연결 해제와 대기 요청

if (currentState >= low && currentState <= high) 조건식이 참일 경우, 즉 현재 상태가 허용된 범위 내라면 함수는 0 을 반환합니다. `src/libcamera/camera.cpp:717`

상태 범위를 벗어나 이 경로에 도달했을 때 마지막 return 문이 반환하는 오류 식별자는 -EACCES 입니다. `src/libcamera/camera.cpp:720`

if (!allowDisconnected && disconnected_) 조건식이 참일 경우 -ENODEV 값을 반환합니다. `src/libcamera/camera.cpp:713`

`Private::disconnect` 함수는 카메라가 실행 중일 때 하드웨어가 제거된 경우 상태 변경을 수행하며, 이때 state_의 현재 값이 `Private::CameraRunning` 이라면 상태를 `Private::CameraConfigured` 로 변경하고, disconnected_ 변수에는 true 를 대입합니다. `src/libcamera/camera.cpp:732`

`Camera::disconnect` 함수는 먼저 _d() 객체의 disconnect 메서드를 호출한 후, disconnected 신호를 방출합니다. `src/libcamera/camera.cpp:955`

카메라가 실행 중 상태일 때 연결이 끊기는 경우 처리해야 할 대기 중인 요청에 대해 대응해야 합니다. `src/libcamera/camera.cpp:952`

근거 원문: [src/libcamera/camera.cpp:952](#source-6a5f4b06e439be31) · [src/libcamera/camera.cpp:717](#source-2bd61734262b0f97) · [src/libcamera/camera.cpp:732](#source-6d8cd0929b722770) · [src/libcamera/camera.cpp:955](#source-e663d38465c31ba8) · [src/libcamera/camera.cpp:713](#source-788f31dc88936e2c) · [src/libcamera/camera.cpp:720](#source-04d54618fa3d3171)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | CameraManager, Camera, Request의 책임과 객체 수명은 어떻게 나뉩니까? | [클래스별 책임](#클래스별-책임) | 코드 근거와 설명 연결 |
    | 상태별 허용 호출과 동기화 책임은 어떻게 나뉩니까? | [상태와 허용 호출](#상태와-허용-호출) | 코드 근거와 설명 연결 |
    | 요청 생성부터 완료 통지까지 객체 수명과 호출 순서는 무엇입니까? | [요청 생성과 완료](#요청-생성과-완료) | 코드 근거와 설명 연결 |
    | 요청이 진행 중일 때와 완료된 뒤의 소유권, ReuseBuffers와 fence 규칙은 무엇입니까? | [소유권과 재사용](#소유권과-재사용) | 코드 근거와 설명 연결 · 실행 확인 항목 별도 |
    | queueRequest의 실패 조건과 stop의 취소·완료·반환 상태는 무엇입니까? | [오류와 종료](#오류와-종료) | 코드 근거와 설명 연결 |
    | threadsafe 보장, 호출자의 동기화 책임과 파이프라인의 완료 통지 계약을 구분하세요. 애플리케이션 콜백 전달 방식과 실기기 검증은 별도로 확인하세요. | [동시성과 실행 확인](#동시성과-실행-확인) | 코드 근거와 설명 연결 |
    | 카메라 연결이 끊어지면 상태·API 접근·대기 요청에 어떤 변화와 확인 한계가 있습니까? | [연결 해제와 대기 요청](#연결-해제와-대기-요청) | 코드 근거와 설명 연결 |

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

<a id="source-95ae69eeb085e3b1"></a>

??? note "소스 근거: src/libcamera/request.cpp:442"
    `src/libcamera/request.cpp:442`에서 시작하는 발췌입니다. 종료 줄은 475이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `65cd8b0501b7f6545dd10eaaec4a4fe46c52a096a3bbd94ea6b4813e4a670876`
    
    ```text
    \brief Add a FrameBuffer with its associated Stream to the Request
     * \param[in] stream The stream the buffer belongs to
     * \param[in] buffer The FrameBuffer to add to the request
     * \param[in] fence The optional fence
     *
     * A reference to the buffer is stored in the request. The caller is responsible
     * for ensuring that the buffer will remain valid until the request complete
     * callback is called.
     *
     * A request can only contain one buffer per stream. If a buffer has already
     * been added to the request for the same stream, this function returns -EEXIST.
     *
     * A Fence can be optionally associated with the \a buffer.
     *
     * When a valid Fence is provided to this function, \a fence is moved to \a
     * buffer and this Request will only be queued to the device once the
     * fences of all its buffers have been correctly signalled. Ownership of the
     * fence will only be taken in case of success, otherwise the fence will
     * be left unmodified.
     *
     * If the \a fence associated with \a buffer isn't signalled, the request will
     * fail after a timeout. The buffer will still contain the fence, which
     * applications must retrieve with FrameBuffer::releaseFence() before the buffer
     * can be reused in another request. Attempting to add a buffer that still
     * contains a fence to a request will result in this function returning -EEXIST.
     *
     * \sa FrameBuffer::releaseFence()
     *
     * \return 0 on success or a negative error code otherwise
     * \retval -EEXIST The request already contains a buffer for the stream
     *  or the buffer still references a fence
     * \retval -EINVAL The buffer does not reference a valid Stream
     */
    int Request::addBuffer(const Stream *stream, FrameBuffer *buffer,
    ```

<a id="source-38494771cb29cc8c"></a>

??? note "소스 근거: src/libcamera/request.cpp:376"
    `src/libcamera/request.cpp:376`에서 시작하는 발췌입니다. 종료 줄은 407이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `22294a6809bd4c6655824af9603fb3879603cec256c6845e00d3d2a0e6bf7679`
    
    ```text
    \brief Reset the request for reuse
     * \param[in] flags Indicate whether or not to reuse the buffers
     *
     * Reset the status and controls associated with the request, to allow it to
     * be reused and requeued without destruction. This function shall be called
     * prior to queueing the request to the camera, in lieu of constructing a new
     * request. The application can reuse the buffers that were previously added
     * to the request via addBuffer() by setting \a flags to ReuseBuffers.
     */
    void Request::reuse(ReuseFlag flags)
    {
    	LIBCAMERA_TRACEPOINT(request_reuse, this);
    
    	_d()->reset();
    
    	if (flags & ReuseBuffers) {
    		for (const auto &[stream, buffer] : bufferMap_) {
    			buffer->_d()->setRequest(this);
    			_d()->pending_.insert(buffer);
    		}
    	} else {
    		bufferMap_.clear();
    	}
    
    	status_ = RequestPending;
    
    	controls_.clear();
    	_d()->metadata_.clear();
    }
    
    /**
     * \fn Request::controls()
    ```

<a id="source-447804db33308244"></a>

??? note "소스 근거: src/libcamera/request.cpp:326"
    `src/libcamera/request.cpp:326`에서 시작하는 발췌입니다. 종료 줄은 338이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `9e55d8335a38080c0af78cf267bac78c573636447425e25d394e5b206217e7fe`
    
    ```text
    \enum Request::ReuseFlag
     * Flags to control the behavior of Request::reuse()
     * \var Request::Default
     * Don't reuse buffers
     * \var Request::ReuseBuffers
     * Reuse the buffers that were previously added by addBuffer()
     *
     * \note Fences associated with the buffers are not reused.
     *  This flag should not be used if fences are used.
     */
    
    /**
     * \typedef Request::BufferMap
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

<a id="source-6a5f4b06e439be31"></a>

??? note "소스 근거: src/libcamera/camera.cpp:952"
    `src/libcamera/camera.cpp:952`에서 시작하는 발췌입니다. 종료 줄은 954이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `21ad02a52ecffea6a1eeebcc2336982670d59110ec6ca1481c5d631877953715`
    
    ```text
    \todo Deal with pending requests if the camera is disconnected in a
     * running state.
     */
    ```

<a id="source-2bd61734262b0f97"></a>

??? note "소스 근거: src/libcamera/camera.cpp:717"
    `src/libcamera/camera.cpp:717`에서 시작하는 발췌입니다. 종료 줄은 732이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `61511adef3e69f6c8f9c59805bfe7acab9b8719e23c69909bb8505046390a5c3`
    
    ```text
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
    ```

<a id="source-6d8cd0929b722770"></a>

??? note "소스 근거: src/libcamera/camera.cpp:732"
    `src/libcamera/camera.cpp:732`에서 시작하는 발췌입니다. 종료 줄은 745이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `5ba21c3c07a431acb932184449d6248b686805bf778cd50106880dfdfb393a1a`
    
    ```text
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

<a id="source-e663d38465c31ba8"></a>

??? note "소스 근거: src/libcamera/camera.cpp:955"
    `src/libcamera/camera.cpp:955`에서 시작하는 발췌입니다. 종료 줄은 963이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `05c69afe50e8cce3fc2089bbee618a14232dcc24942c99d61cb7083122919a30`
    
    ```text
    void Camera::disconnect()
    {
    	LOG(Camera, Debug) << "Disconnecting camera " << id();
    
    	_d()->disconnect();
    	disconnected.emit();
    }
    
    int Camera::exportFrameBuffers(Stream *stream,
    ```

<a id="source-788f31dc88936e2c"></a>

??? note "소스 근거: src/libcamera/camera.cpp:713"
    `src/libcamera/camera.cpp:713`에서 시작하는 발췌입니다. 종료 줄은 714이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `ce414db71a2d33cc2353d142b1ae6cd28523b052f83a35caf06819d389756594`
    
    ```text
    if (!allowDisconnected && disconnected_)
    		return -ENODEV;
    ```

<a id="source-04d54618fa3d3171"></a>

??? note "소스 근거: src/libcamera/camera.cpp:720"
    `src/libcamera/camera.cpp:720`에서 시작하는 발췌입니다. 종료 줄은 730이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `248c1ec90da12c583c88083544a5c4d43253f4cd2bff4a6cbd05340a3b0acd34`
    
    ```text
    ASSERT(static_cast<unsigned int>(low) < std::size(camera_state_names) &&
    	       static_cast<unsigned int>(high) < std::size(camera_state_names));
    
    	LOG(Camera, Error) << "Camera in " << camera_state_names[currentState]
    			   << " state trying " << from
    			   << "() requiring state between "
    			   << camera_state_names[low] << " and "
    			   << camera_state_names[high];
    
    	return -EACCES;
    }
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
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `2c4b67c079`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-26 · 사람 검토 전

다음 단계: [Pipeline Handler](pipeline-handler.md)
