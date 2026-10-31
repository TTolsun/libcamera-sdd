---
generated_at: 2026-10-30T22:41:11+00:00
source_commit: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61
status: ok
section: overview
generation_method: facts-and-llm
evidence_fingerprint: 48ee0ce3dd22bea8395731271af652cc0c47a27037d9f368d2969a5b2e6331fc
semantic_review: human-review-required
agent: cli/claude/claude-haiku-5-5
generated_design: {"schema": 1, "input_fingerprint": "48ee0ce3dd22bea8395731271af652cc0c47a27037d9f368d2969a5b2e6331fc", "answers": {"discovery": [{"text": "`CameraManager`는 libcamera의 진입점으로, 장치를 열거하고 애플리케이션에 시스템의 카메라 접근을 제공하는 역할을 합니다. 소개 주석에 따르면 `CameraManager`는 모든 `Camera` 객체를 소유하며, 핫플러그와 핫언플러그를 처리해 카메라의 수명을 관리합니다. `CameraManager::Private::pipelineFactoryMatch`는 주어진 팩토리로 `PipelineHandler`를 반복해서 생성하고, 각 객체의 `match(enumerator_.get())`가 참을 반환하는 동안 매칭되는 파이프라인을 가능한 한 많이 제공합니다. `match`가 거짓을 반환하면 반복을 멈추고, 매칭에 성공한 경우에만 `Debug` 로그를 남깁니다.", "evidence": ["manager", "manager-pipeline-implementation"], "covers": ["discovery"], "kind": "behavior", "quote": "The camera manager is the entry point to libcamera. It enumerates devices,\n * associates them with pipeline managers, and provides access to the cameras\n * in the system to applications. The manager owns all Camera objects and\n * handles hot-plugging and hot-unplugging to manage the lifetime of cameras.\n *\n * To interact with libcamera, an application starts by creating a camera\n * manager instance. Only a single instance of the camera manager may exist at\n * a time. Attempting to create a second instance without first deleting the\n * existing instance results in undefined behaviour.\n *\n * The manager is initially stopped,", "part_id": "entry"}, {"text": "동시에 존재할 수 있는 `CameraManager` 인스턴스는 하나뿐입니다.", "evidence": ["manager"], "covers": ["discovery"], "kind": "behavior", "quote": "The camera manager is the entry point to libcamera. It enumerates devices,\n * associates them with pipeline managers, and provides access to the cameras\n * in the system to applications. The manager owns all Camera objects and\n * handles hot-plugging and hot-unplugging to manage the lifetime of cameras.\n *\n * To interact with libcamera, an application starts by creating a camera\n * manager instance. Only a single instance of the camera manager may exist at\n * a time. Attempting to create a second instance without first deleting the\n * existing instance results in undefined behaviour.\n *\n * The manager is initially stopped,", "part_id": "singleton"}, {"text": "기존 인스턴스를 삭제하지 않은 상태에서 두 번째 `CameraManager` 인스턴스를 생성하면 정의되지 않은 동작(undefined behaviour)이 발생합니다. 따라서 호출하는 쪽은 새 인스턴스를 만들기 전에 기존 인스턴스를 먼저 삭제해야 합니다.", "evidence": ["manager"], "covers": ["discovery"], "kind": "limitation", "quote": "The camera manager is the entry point to libcamera. It enumerates devices,\n * associates them with pipeline managers, and provides access to the cameras\n * in the system to applications. The manager owns all Camera objects and\n * handles hot-plugging and hot-unplugging to manage the lifetime of cameras.\n *\n * To interact with libcamera, an application starts by creating a camera\n * manager instance. Only a single instance of the camera manager may exist at\n * a time. Attempting to create a second instance without first deleting the\n * existing instance results in undefined behaviour.\n *\n * The manager is initially stopped,", "part_id": "singleton"}, {"text": "`CameraManager::start()`가 성공하면 시작 과정에서 열거된 시스템의 카메라를 애플리케이션이 나열하고 사용할 수 있으며, 이 상태는 카메라 매니저가 중지되거나 카메라가 시스템에서 분리될 때까지 계속됩니다.", "evidence": ["start"], "covers": ["discovery"], "kind": "behavior", "quote": "\\brief Start the camera manager\n *\n * Start the camera manager and enumerate all devices in the system. Once\n * the start has been confirmed the user is free to list and otherwise\n * interact with cameras in the system until either the camera manager\n * is stopped or the camera is unplugged from the system.\n *\n * \\return 0 on success or a negative error code otherwise\n */\nint CameraManager::start()", "part_id": "start"}, {"text": "`CameraManager::cameras()`와 `CameraManager::get()`은 카메라 매니저가 실행 중인 상태에서 호출해야 하며, 이 상태를 확보할 책임은 호출하는 쪽에 있습니다.", "evidence": ["access"], "covers": ["discovery"], "kind": "behavior", "quote": "\\fn CameraManager::cameras()\n * \\brief Retrieve all available cameras\n *\n * Before calling this function the caller is responsible for ensuring that\n * the camera manager is running.\n *\n * \\context This function is \\threadsafe.\n *\n * \\return List of all available cameras\n */\nstd::vector<std::shared_ptr<Camera>> CameraManager::cameras() const\n{\n\tconst Private *const d = _d();", "part_id": "access"}, {"text": "`match()`를 구현하는 쪽은 필요한 장치를 모두 찾으면 `MediaDevice::acquire()`로 해당 장치를 모두 획득해야 합니다. 이어서 `Camera` 인스턴스를 생성해 내부에 저장하고 카메라 관리자에 등록한 뒤 `true`를 반환해야 합니다. 필요한 장치를 모두 찾지 못하면 어떤 장치도 획득하지 않거나, 이미 획득한 장치를 `MediaDevice::release()`로 모두 해제한 뒤 `false`를 반환해야 합니다.", "evidence": ["match"], "covers": ["discovery"], "kind": "behavior", "quote": "\\fn PipelineHandler::match(DeviceEnumerator *enumerator)\n * \\brief Match media devices and create camera instances\n * \\param[in] enumerator The enumerator providing all media devices found in the\n * system\n *\n * This function is the main entry point of the pipeline handler. It is called\n * by the camera manager with the \\a enumerator passed as an argument. It shall\n * acquire from the \\a enumerator all the media devices it needs for a single\n * pipeline, create one or multiple Camera instances and register them with the\n * camera manager.\n *\n * If all media devices needed by the pipeline handler are found, they must all\n * be acquired by a call to MediaDevice::acquire(). This function shall then\n * create the corresponding Camera instances, store them internally, and return\n * true. Otherwise it shall not acquire any media device (or shall release all\n * the media devices is has acquired by calling MediaDevice::release()) and\n * return false.\n *\n * If multiple instances of a pipeline are available in the system, the\n * PipelineHandler class will be instantiated once per instance, and its match()\n * function called for every instance. Each call shall acquire media devices for\n * one pipeline instance, until all compatible media devices are exhausted.\n *\n * If this function returns true, a new instance of the pipeline handler will\n * be created and its match() function called.\n *\n * \\context This function is called from the CameraManager thread.\n *\n * \\return true if media devices have been acquired and camera instances\n * created, or false otherwise\n */", "part_id": "match"}], "responsibility": [{"text": "`Camera` 클래스는 하나의 이미지 소스에서 하나 이상의 이미지 스트림을 만들 수 있는 카메라를 나타냅니다. 장치를 구성하고 제어하며 이미지 스트림을 캡처하는 주요 인터페이스를 제공하고, libcamera가 외부에 노출하는 중심 객체입니다.", "evidence": ["camera"], "covers": ["responsibility"], "kind": "behavior", "quote": "The Camera class models a camera capable of producing one or more image\n * streams from a single image source. It provides the main interface to\n * configuring and controlling the device, and capturing image streams. It is\n * the central object exposed by libcamera.\n *\n * To support the central nature of Camera objects, libcamera manages the\n * lifetime of camera instances with std::shared_ptr<>. Instances shall be\n * created with the create() function which returns a shared pointer. The\n * Camera constructors and destructor are private, to prevent instances from\n * being constructed and destroyed manually.\n *\n * \\section camera_operation", "part_id": "responsibility"}, {"text": "libcamera는 `Camera` 인스턴스의 수명을 `std::shared_ptr<>`로 관리합니다. 인스턴스는 `create()` 함수로 생성해야 하며, 이 함수는 공유 포인터를 반환합니다. `Camera`의 생성자와 소멸자는 private으로 선언되어 있어서, 인스턴스를 직접 생성하거나 파괴할 수 없습니다.", "evidence": ["camera"], "covers": ["responsibility"], "kind": "behavior", "quote": "The Camera class models a camera capable of producing one or more image\n * streams from a single image source. It provides the main interface to\n * configuring and controlling the device, and capturing image streams. It is\n * the central object exposed by libcamera.\n *\n * To support the central nature of Camera objects, libcamera manages the\n * lifetime of camera instances with std::shared_ptr<>. Instances shall be\n * created with the create() function which returns a shared pointer. The\n * Camera constructors and destructor are private, to prevent instances from\n * being constructed and destroyed manually.\n *\n * \\section camera_operation", "part_id": "responsibility"}], "creation": [{"text": "`Camera::createRequest`의 `cookie`는 애플리케이션용 불투명 입력 값입니다. 이 값은 생성된 요청에 저장되며, `Request::cookie()`로 언제든지 다시 읽을 수 있습니다. 소스 설명에 따르면 애플리케이션은 보통 완료 핸들러에서 이 값으로 요청을 외부 리소스와 연결하며, libcamera 입장에서 `cookie`는 completely opaque(완전히 불투명)한 값입니다.", "evidence": ["create"], "covers": ["creation"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest", "part_id": "cookie"}, {"text": "`Camera::createRequest()`는 카메라가 `Configured` 또는 `Running` 상태일 때만 호출할 수 있으며, 오류가 발생하면 `nullptr`을 반환합니다.", "evidence": ["create"], "covers": ["creation"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest", "part_id": "state"}, {"text": "`Camera::createRequest()`가 반환한 요청의 소유권은 호출자에게 넘어가며, 그 요청을 삭제할 책임도 호출자에게 있습니다.", "evidence": ["create"], "covers": ["creation"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest", "part_id": "ownership"}, {"text": "새 요청을 만드는 대신 같은 요청을 다시 큐에 넣으려면, 호출자는 큐에 넣기 전에 `Request::reuse()`를 호출해서 요청의 상태와 연결된 컨트롤을 초기화해야 합니다.", "evidence": ["reuse"], "covers": ["creation"], "kind": "behavior", "quote": "\\brief Reset the request for reuse\n * \\param[in] flags Indicate whether or not to reuse the buffers\n *\n * Reset the status and controls associated with the request, to allow it to\n * be reused and requeued without destruction. This function shall be called\n * prior to queueing the request to the camera, in lieu of constructing a new\n * request. The application can reuse the buffers that were previously added\n * to the request via addBuffer() by setting \\a flags to ReuseBuffers.\n */\nvoid Request::reuse(ReuseFlag flags)\n{\n\tLIBCAMERA_TRACEPOINT(request_reuse, this);", "part_id": "reuse"}, {"text": "`Request::reuse(ReuseFlag)`는 `flags & ReuseBuffers`가 참이면 `bufferMap_`의 각 버퍼에 `setRequest(this)`를 호출하고 `_d()->pending_`에 넣어, `addBuffer()`로 이미 추가한 버퍼를 유지한 채 재사용합니다. `ReuseBuffers`를 지정하지 않으면 `bufferMap_`을 비웁니다.", "evidence": ["reuse"], "covers": ["creation"], "kind": "behavior", "quote": "if (flags & ReuseBuffers) {\n\t\tfor (const auto &[stream, buffer] : bufferMap_) {\n\t\t\tbuffer->_d()->setRequest(this);\n\t\t\t_d()->pending_.insert(buffer);\n\t\t}\n\t} else {\n\t\tbufferMap_.clear();\n\t}", "part_id": "buffers"}], "lifecycle": [{"text": "캡처를 준비하려면 애플리케이션은 `acquire()`로 카메라를 획득한 뒤 `configure()`로 구성하고, 그다음 `start()`로 시작하는 순서로 진행해야 합니다.", "evidence": ["state"], "covers": ["lifecycle"], "kind": "behavior", "quote": "\\section camera_operation Operating the Camera\n *\n * An application needs to perform a sequence of operations on a camera before\n * it is ready to process requests. The camera needs to be acquired and\n * configured to prepare the camera for capture. Once started the camera can\n * process requests until it is stopped. When an application is done with a\n * camera, the camera needs to be released.\n *\n * An application may start and stop a camera multiple times as long as it is\n * not released. The camera may also be reconfigured.\n *\n * Functions that affect the camera state as defined below are generally not\n * synchronized with each other by the Camera class. The caller is responsible\n * for ensuring their synchronization if necessary.\n *\n * \\subsection Camera States\n *\n * To help manage the sequence of operations needed to control the camera a set\n * of states are defined. Each state describes which operations may be performed\n * on the camera. Performing an operation not allowed in the camera state\n * results in undefined behaviour. Operations not listed at all in the state\n * diagram are allowed in all states.\n *\n * \\dot\n * digraph camera_state_machine {\n *   node [shape = doublecircle ]; Available;\n *   node [shape = circle ]; Acquired;\n *   node [shape = circle ]; Configured;\n *   node [shape = circle ]; Stopping;\n *   node [shape = circle ]; Running;\n *\n *   Available -> Available [label = \"release()\"];\n *   Available -> Acquired [label = \"acquire()\"];\n *\n *   Acquired -> Available [label = \"release()\"];\n *   Acquired -> Configured [label = \"configure()\"];\n *\n *   Configured -> Available [label = \"release()\"];\n *   Configured -> Configured [label = \"configure(), createRequest()\"];\n *   Configured -> Running [label = \"start()\"];\n *\n *   Running -> Stopping [label = \"stop()\"];\n *   Stopping -> Configured;\n *   Running -> Running [label = \"createRequest(), queueRequest()\"];\n * }\n * \\enddot", "part_id": "prepare"}, {"text": "시작된 카메라는 정지되기 전까지 요청을 처리할 수 있으며, 이 구간이 `Running` 상태입니다. 완전히 끝내는 경로는 `Running`에서 `stop()`으로 `Stopping`을 거쳐 정지 후 `Configured`로 돌아가고, 이어서 `Configured`에서 `release()`로 `Available`로 해제하는 순서입니다.", "evidence": ["state"], "covers": ["lifecycle"], "kind": "behavior", "quote": "\\section camera_operation Operating the Camera\n *\n * An application needs to perform a sequence of operations on a camera before\n * it is ready to process requests. The camera needs to be acquired and\n * configured to prepare the camera for capture. Once started the camera can\n * process requests until it is stopped. When an application is done with a\n * camera, the camera needs to be released.\n *\n * An application may start and stop a camera multiple times as long as it is\n * not released. The camera may also be reconfigured.\n *\n * Functions that affect the camera state as defined below are generally not\n * synchronized with each other by the Camera class. The caller is responsible\n * for ensuring their synchronization if necessary.\n *\n * \\subsection Camera States\n *\n * To help manage the sequence of operations needed to control the camera a set\n * of states are defined. Each state describes which operations may be performed\n * on the camera. Performing an operation not allowed in the camera state\n * results in undefined behaviour. Operations not listed at all in the state\n * diagram are allowed in all states.\n *\n * \\dot\n * digraph camera_state_machine {\n *   node [shape = doublecircle ]; Available;\n *   node [shape = circle ]; Acquired;\n *   node [shape = circle ]; Configured;\n *   node [shape = circle ]; Stopping;\n *   node [shape = circle ]; Running;\n *\n *   Available -> Available [label = \"release()\"];\n *   Available -> Acquired [label = \"acquire()\"];\n *\n *   Acquired -> Available [label = \"release()\"];\n *   Acquired -> Configured [label = \"configure()\"];\n *\n *   Configured -> Available [label = \"release()\"];\n *   Configured -> Configured [label = \"configure(), createRequest()\"];\n *   Configured -> Running [label = \"start()\"];\n *\n *   Running -> Stopping [label = \"stop()\"];\n *   Stopping -> Configured;\n *   Running -> Running [label = \"createRequest(), queueRequest()\"];\n * }\n * \\enddot", "part_id": "finish"}, {"text": "카메라가 해제되지 않은 동안에는 애플리케이션이 시작과 정지를 여러 번 반복할 수 있으며, 카메라를 재구성하여 캡처 설정을 바꿀 수도 있습니다.", "evidence": ["state"], "covers": ["lifecycle"], "kind": "behavior", "quote": "\\section camera_operation Operating the Camera\n *\n * An application needs to perform a sequence of operations on a camera before\n * it is ready to process requests. The camera needs to be acquired and\n * configured to prepare the camera for capture. Once started the camera can\n * process requests until it is stopped. When an application is done with a\n * camera, the camera needs to be released.\n *\n * An application may start and stop a camera multiple times as long as it is\n * not released. The camera may also be reconfigured.\n *\n * Functions that affect the camera state as defined below are generally not\n * synchronized with each other by the Camera class. The caller is responsible\n * for ensuring their synchronization if necessary.\n *\n * \\subsection Camera States\n *\n * To help manage the sequence of operations needed to control the camera a set\n * of states are defined. Each state describes which operations may be performed\n * on the camera. Performing an operation not allowed in the camera state\n * results in undefined behaviour. Operations not listed at all in the state\n * diagram are allowed in all states.\n *\n * \\dot\n * digraph camera_state_machine {\n *   node [shape = doublecircle ]; Available;\n *   node [shape = circle ]; Acquired;\n *   node [shape = circle ]; Configured;\n *   node [shape = circle ]; Stopping;\n *   node [shape = circle ]; Running;\n *\n *   Available -> Available [label = \"release()\"];\n *   Available -> Acquired [label = \"acquire()\"];\n *\n *   Acquired -> Available [label = \"release()\"];\n *   Acquired -> Configured [label = \"configure()\"];\n *\n *   Configured -> Available [label = \"release()\"];\n *   Configured -> Configured [label = \"configure(), createRequest()\"];\n *   Configured -> Running [label = \"start()\"];\n *\n *   Running -> Stopping [label = \"stop()\"];\n *   Stopping -> Configured;\n *   Running -> Running [label = \"createRequest(), queueRequest()\"];\n * }\n * \\enddot", "part_id": "repeat"}], "request": [{"text": "애플리케이션은 `Camera::queueRequest()`로 제출하기 전에 `createRequest()`가 반환한 요청 객체에 캡처 버퍼를 최소 한 개 연결해야 합니다.", "evidence": ["queue"], "covers": ["request"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest", "part_id": "buffers"}, {"text": "`Camera::queueRequest()`로 제출한 요청이 처리를 마치면, 카메라는 `requestCompleted` 신호로 완료를 알립니다.", "evidence": ["queue"], "covers": ["request"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest", "part_id": "signal"}, {"text": "`Camera::queueRequest()`는 카메라가 `camera_operation`에 정의된 Running 상태일 때만 호출할 수 있습니다.", "evidence": ["queue"], "covers": ["request"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest", "part_id": "state"}], "completion": [{"text": "파이프라인 핸들러는 요청의 버퍼 한 개가 완료되었음을 알리기 위해 `PipelineHandler::completeBuffer()`를 호출해야 합니다. `completeBuffer()`는 애플리케이션에 버퍼 완료를 통지하고, 요청의 내부 버퍼 추적 상태를 갱신합니다. 요청에 포함된 모든 버퍼가 완료되었으면 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.", "evidence": ["buffer"], "covers": ["completion"], "kind": "behavior", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer", "part_id": "buffer"}, {"text": "마지막 버퍼가 완료된 뒤에도 파이프라인 핸들러는 `completeRequest()`를 명시적으로 호출해야 합니다.", "evidence": ["buffer"], "covers": ["completion"], "kind": "behavior", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer", "part_id": "request"}], "boundary": [{"text": "`Camera` 상태를 바꾸는 함수들은 `Camera` 클래스가 일반적으로 서로 동기화하지 않으므로, 필요한 경우 호출자가 이 함수들 사이의 동기화를 보장해야 합니다.", "evidence": ["synchronization"], "covers": ["boundary"], "kind": "behavior", "quote": "Functions that affect the camera state as defined below are generally not\n * synchronized with each other by the Camera class. The caller is responsible\n * for ensuring their synchronization if necessary.\n *\n * \\subsection Camera States", "part_id": "state"}, {"text": "`PipelineHandler::completeRequest()`의 호출 주체는 pipeline handler입니다. pipeline handler는 완료된 요청을 카메라에 알릴 때 이 함수를 호출해야 하며, 그 호출은 `CameraManager` 스레드에서 이루어져야 합니다.", "evidence": ["completion"], "covers": ["boundary"], "kind": "behavior", "quote": "\\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest", "part_id": "complete"}], "verification": [{"text": "`Camera::start()`는 `d->isAccessAllowed(Private::CameraConfigured)`로 카메라 상태를 검사하고 그 반환값을 `ret`에 저장합니다. `ret`가 음수이면(`ret < 0`) `start()`는 `return ret;`으로 그 값을 그대로 반환하며, 이 분기에서는 파이프라인 시작 호출과 `Private::CameraRunning` 상태 전환이 실행되지 않습니다. API 주석의 `-EACCES`는 카메라가 시작할 수 없는 상태를 뜻하지만, 이 코드 조각만으로는 `isAccessAllowed()`가 `-EACCES`를 반환하는지 확인할 수 없으므로 두 값을 같은 것으로 단정하지 않습니다.", "evidence": ["allowed-start-state", "start-api"], "covers": ["verification"], "kind": "behavior", "quote": "int ret = d->isAccessAllowed(Private::CameraConfigured);\n\tif (ret < 0)", "part_id": "contracts"}, {"text": "이 TODO 주석이 문서화를 요청한 대상은 카메라 시작 타이밍입니다.", "evidence": ["timing"], "covers": ["verification"], "kind": "behavior", "quote": "\\todo Add documentation for camera start timings.", "part_id": "timing"}]}, "topic_inputs": {"discovery": "74216ca939f7eee1f0c3d7aab49f43c686ec88b3535def0bc183c322eb55c678", "responsibility": "64eb3ae285a184be45c730e6163f29ebb63b53b8f89e1359d8bef2ba0512ef63", "creation": "393183cdeec1bcb25a03fd5af59f0204a22d8e558613fe1883f8a27879a79d7e", "lifecycle": "4b65e4120a7debd8695aac248a113c53fa11e45b72fbf96cbb3754222e08263f", "request": "451063d9ff4127e5fbf04c2a06460db16af935b8ac95b324f41c4d52c96015ab", "completion": "829e47aa3ba34dae8cd978975d8f006def049b5202ed19fe60afc7bf123afcb0", "boundary": "c6086439a20aca18c3ebf4a680c9eab01cfe861fc72b81c553399512e499bc05", "verification": "afc4879b963fb8f73a00e138f373a85b85c3535b9abef46f72c39c2c2499b62e"}, "reused_topics": ["discovery", "responsibility", "creation", "lifecycle", "request", "completion", "boundary", "verification"], "replayed_units": [], "generated_topics": [], "topic_agents": {"discovery": "cli/claude/claude-haiku-5-5", "responsibility": "cli/claude/claude-haiku-5-5", "creation": "cli/claude/claude-haiku-5-5", "lifecycle": "cli/claude/claude-haiku-5-5", "request": "cli/claude/claude-haiku-5-5", "completion": "cli/claude/claude-haiku-5-5", "boundary": "cli/claude/claude-haiku-5-5", "verification": "cli/claude/claude-haiku-5-5"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "reader_scope": {"revision": 1, "change_reason": "독자의 개요 과업을 고정하고 장치별 요청 수의 기본 한도는 기존 연동 상세로 이동합니다. 준비 실패·완료·소유권의 필수 조건과 예외는 유지합니다.", "tasks": [{"id": "onboarding", "goal": "신입사원이 전체 구조와 대표 흐름을 이해하고 첫 코드 탐색 순서를 찾습니다.", "completion": "책임·대표 요청 흐름·첫 파일·필수 예외와 확인 조건을 찾습니다.", "requirements": ["responsibility", "discovery", "creation", "lifecycle", "request", "completion", "boundary", "verification"]}], "optional": [{"id": "implementation-detail", "location": "scenarios/index.md", "reason": "내부 상세는 과업에 필요한 조건과 예외를 유지한 채 연결해서 읽습니다."}, {"id": "queue-limit-detail", "location": "pipeline-requests.md#장치-요청-한도와-대기-큐", "reason": "장치별 큐의 기본 수치는 연동 구현 상세에서 확인합니다. 개요의 요청 준비·실패·완료 조건은 유지합니다."}], "excluded": [{"id": "all-features", "reason": "전체 기능·모든 하드웨어 조합의 참조서는 이 개요의 목적이 아닙니다."}], "removed_requirements": ["queue-limit"]}, "validation_policy": {"manuscript": "e0c429a5c80a01c34563ce00a616df89d8f75c735f8669bcbd1f75d84cce82a6", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "c80b476cf38b78ab674977c3f39584d8db6961a914e8ed13ac9370e2fec6fa45", "answer_contracts": "1e0d24e0cf26ded53ecec2e5a6fbc51836bac6e17530318a9fa7cffaa936c00b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "9db4d42a710b4a71a7d2bb16f69db06926409281dc1a200c796e77d5deaa25a0", "design_response": "deb70dda7ad27f001267e4a9712c5b0dc1fe9fa67acd13bedbfefaaad0ad83c8", "design_validation": "946deebb694018f6361ee86669e1a7a26cd61dfffef11bb3a7de0a193639fabe"}, "validation_model": "2eb3bf27fc8fdca03721abcecc71d006bc0c9612049018fdc117931887213ef9", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "f8fd5a3d8041c23fc68b93ff32b8727e98393383b5099032eb00ad0013e7611c"}, "reuse_lineage": {"source_commit": "293d751a814e0d4c34e85ad457ccd9d5eefd1a61", "body_sha256": "a46c0e35d12042851abfa2c40e52bffabae848175058a452cfabda9167adebc4", "topics": ["discovery", "responsibility", "creation", "lifecycle", "request", "completion", "boundary", "verification"], "validation": "current source, contract and editorial checks; human review pending"}, "body_sha256": "a46c0e35d12042851abfa2c40e52bffabae848175058a452cfabda9167adebc4"}
---

# 시스템 개요

**src/libcamera/camera_manager.cpp의 CameraManager에서 시작해 요청 제출과 완료를 따라가세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 처음 읽을 파일과 진입점을 찾습니다. | [탐색과 파이프라인 선택](#탐색과-파이프라인-선택) |
| 요청과 결과가 지나는 경계를 확인합니다. | [요청 제출과 완료](#요청-제출과-완료) |
| 구성 실패의 원인을 좁힙니다. | [구성과 요청 오류 조사](request-diagnosis.md#구성-실패를-좁히는-순서) |
| 요청의 제출 성공과 촬영 완료를 구분하고, 버퍼를 유지할 기간과 오류가 난 위치를 확인하세요. | [요청 처리와 문제 진단](request-lifecycle.md) |
| 수정 전에 상태와 종료 순서를 확인합니다. | [캡처 세션의 상태와 자원](#캡처-세션의-상태와-자원) |
| 빌드한 모든 파이프라인·IPA·앱의 클래스와 함수를 패키지별로 찾으세요. 표는 추출 사실에서 만들었고 동작은 설명하지 않습니다. | [구성 요소 색인](component-index.md) |
| <a id="장치-요청-한도와-대기-큐"></a>장치 요청 수의 기본 한도와 대기 큐를 확인합니다. | [Pipeline 요청 제출과 완료](pipeline-requests.md#장치-요청-한도와-대기-큐) |

## 탐색과 파이프라인 선택

`CameraManager`는 libcamera의 진입점으로, 장치를 열거하고 애플리케이션에 시스템의 카메라 접근을 제공하는 역할을 합니다. 소개 주석에 따르면 `CameraManager`는 모든 `Camera` 객체를 소유하며, 핫플러그와 핫언플러그를 처리해 카메라의 수명을 관리합니다. `CameraManager::Private::pipelineFactoryMatch`는 주어진 팩토리로 `PipelineHandler`를 반복해서 생성하고, 각 객체의 `match(enumerator_.get())`가 참을 반환하는 동안 매칭되는 파이프라인을 가능한 한 많이 제공합니다. `match`가 거짓을 반환하면 반복을 멈추고, 매칭에 성공한 경우에만 `Debug` 로그를 남깁니다. `src/libcamera/camera_manager.cpp:283`, `src/libcamera/camera_manager.cpp:154`

<!-- sdd:visual:discovery-map -->
### 장치 탐색에서 Camera 접근까지

장치 매칭과 등록의 책임을 따라가세요. 그림은 책임 연결이며 전체 호출 순서나 실행 시간을 나타내지 않습니다.

```mermaid
flowchart TB
%% sdd:translations {"Camera 생성·등록": "Create and register Camera", "CameraManager 진입점": "CameraManager entry", "PipelineHandler::match()": "PipelineHandler::match()", "start()": "start()", "열거자를 전달해 장치를 매칭": "Pass enumerator to match <br/>devices", "장치 열거": "Enumerate devices", "필요한 장치를 확보한 경우": "When required devices are <br/>acquired"}
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

동시에 존재할 수 있는 `CameraManager` 인스턴스는 하나뿐입니다. `src/libcamera/camera_manager.cpp:283`

실행 확인 항목: 기존 인스턴스를 삭제하지 않은 상태에서 두 번째 `CameraManager` 인스턴스를 생성하면 정의되지 않은 동작(undefined behaviour)이 발생합니다. 따라서 호출하는 쪽은 새 인스턴스를 만들기 전에 기존 인스턴스를 먼저 삭제해야 합니다. `src/libcamera/camera_manager.cpp:283`

`CameraManager::start()`가 성공하면 시작 과정에서 열거된 시스템의 카메라를 애플리케이션이 나열하고 사용할 수 있으며, 이 상태는 카메라 매니저가 중지되거나 카메라가 시스템에서 분리될 때까지 계속됩니다. `CameraManager::cameras()`와 `CameraManager::get()`은 카메라 매니저가 실행 중인 상태에서 호출해야 하며, 이 상태를 확보할 책임은 호출하는 쪽에 있습니다. `src/libcamera/camera_manager.cpp:329`, `src/libcamera/camera_manager.cpp:368`

`match()`를 구현하는 쪽은 필요한 장치를 모두 찾으면 `MediaDevice::acquire()`로 해당 장치를 모두 획득해야 합니다. 이어서 `Camera` 인스턴스를 생성해 내부에 저장하고 카메라 관리자에 등록한 뒤 `true`를 반환해야 합니다. 필요한 장치를 모두 찾지 못하면 어떤 장치도 획득하지 않거나, 이미 획득한 장치를 `MediaDevice::release()`로 모두 해제한 뒤 `false`를 반환해야 합니다. `src/libcamera/pipeline_handler.cpp:86`

근거 원문: [src/libcamera/camera_manager.cpp:283](#source-f75d22cf73f3402d) · [src/libcamera/camera_manager.cpp:329](#source-f58d94d893e03971) · [src/libcamera/camera_manager.cpp:368](#source-0c733673790ad84f) · [src/libcamera/pipeline_handler.cpp:86](#source-5bbd41c1e725138c) · [src/libcamera/camera_manager.cpp:154](#source-0c01857bf49370e2)

## 컴포넌트별 책임

`Camera` 클래스는 하나의 이미지 소스에서 하나 이상의 이미지 스트림을 만들 수 있는 카메라를 나타냅니다. 장치를 구성하고 제어하며 이미지 스트림을 캡처하는 주요 인터페이스를 제공하고, libcamera가 외부에 노출하는 중심 객체입니다. `src/libcamera/camera.cpp:758`

libcamera는 `Camera` 인스턴스의 수명을 `std::shared_ptr<>`로 관리합니다. 인스턴스는 `create()` 함수로 생성해야 하며, 이 함수는 공유 포인터를 반환합니다. `Camera`의 생성자와 소멸자는 private으로 선언되어 있어서, 인스턴스를 직접 생성하거나 파괴할 수 없습니다. `src/libcamera/camera.cpp:758`

근거 원문: [src/libcamera/camera.cpp:758](#source-6c066281dcce33d6)

## 요청 생성과 소유권

`Camera::createRequest`의 `cookie`는 애플리케이션용 불투명 입력 값입니다. 이 값은 생성된 요청에 저장되며, `Request::cookie()`로 언제든지 다시 읽을 수 있습니다. 소스 설명에 따르면 애플리케이션은 보통 완료 핸들러에서 이 값으로 요청을 외부 리소스와 연결하며, libcamera 입장에서 `cookie`는 completely opaque(완전히 불투명)한 값입니다. `Camera::createRequest()`는 카메라가 `Configured` 또는 `Running` 상태일 때만 호출할 수 있으며, 오류가 발생하면 `nullptr`을 반환합니다. `src/libcamera/camera.cpp:1243`

`Camera::createRequest()`가 반환한 요청의 소유권은 호출자에게 넘어가며, 그 요청을 삭제할 책임도 호출자에게 있습니다. 새 요청을 만드는 대신 같은 요청을 다시 큐에 넣으려면, 호출자는 큐에 넣기 전에 `Request::reuse()`를 호출해서 요청의 상태와 연결된 컨트롤을 초기화해야 합니다. `Request::reuse(ReuseFlag)`는 `flags & ReuseBuffers`가 참이면 `bufferMap_`의 각 버퍼에 `setRequest(this)`를 호출하고 `_d()->pending_`에 넣어, `addBuffer()`로 이미 추가한 버퍼를 유지한 채 재사용합니다. `ReuseBuffers`를 지정하지 않으면 `bufferMap_`을 비웁니다. `src/libcamera/camera.cpp:1243`, `src/libcamera/request.cpp:376`

근거 원문: [src/libcamera/camera.cpp:1243](#source-d61960ed2545ba78) · [src/libcamera/request.cpp:376](#source-0556d5e91908d040)

## 캡처 세션의 상태와 자원

캡처를 준비하려면 애플리케이션은 `acquire()`로 카메라를 획득한 뒤 `configure()`로 구성하고, 그다음 `start()`로 시작하는 순서로 진행해야 합니다. 시작된 카메라는 정지되기 전까지 요청을 처리할 수 있으며, 이 구간이 `Running` 상태입니다. 완전히 끝내는 경로는 `Running`에서 `stop()`으로 `Stopping`을 거쳐 정지 후 `Configured`로 돌아가고, 이어서 `Configured`에서 `release()`로 `Available`로 해제하는 순서입니다. 카메라가 해제되지 않은 동안에는 애플리케이션이 시작과 정지를 여러 번 반복할 수 있으며, 카메라를 재구성하여 캡처 설정을 바꿀 수도 있습니다. `src/libcamera/camera.cpp:769`

근거 원문: [src/libcamera/camera.cpp:769](#source-4b17a07667f3a55d)

## 요청 제출과 완료

애플리케이션은 `Camera::queueRequest()`로 제출하기 전에 `createRequest()`가 반환한 요청 객체에 캡처 버퍼를 최소 한 개 연결해야 합니다. `Camera::queueRequest()`로 제출한 요청이 처리를 마치면, 카메라는 `requestCompleted` 신호로 완료를 알립니다. `Camera::queueRequest()`는 카메라가 `camera_operation`에 정의된 Running 상태일 때만 호출할 수 있습니다. `src/libcamera/camera.cpp:1308`

<!-- sdd:visual:submission-completion -->
### 접수 성공과 촬영 완료는 다른 시점

queueRequest()의 0 반환은 접수 결과입니다. 요청 완료는 별도의 requestCompleted 신호로 확인합니다.

```mermaid
flowchart TB
%% sdd:translations {"0 반환: 접수 성공": "Return 0: submission <br/>accepted", "Running 상태에서 제출": "Submit in Running state", "queueRequest()": "queueRequest()", "requestCompleted 신호": "requestCompleted signal", "버퍼를 연결한 Request": "Request with capture buffers", "접수 결과를 반환": "Return submission result", "촬영 완료는 별도로 통지": "Notify completion separately"}
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

근거 원문: [src/libcamera/camera.cpp:1308](#source-2f880c124115c9c4)

## 버퍼 완료와 요청 완료

파이프라인 핸들러는 요청의 버퍼 한 개가 완료되었음을 알리기 위해 `PipelineHandler::completeBuffer()`를 호출해야 합니다. `completeBuffer()`는 애플리케이션에 버퍼 완료를 통지하고, 요청의 내부 버퍼 추적 상태를 갱신합니다. 요청에 포함된 모든 버퍼가 완료되었으면 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다. 마지막 버퍼가 완료된 뒤에도 파이프라인 핸들러는 `completeRequest()`를 명시적으로 호출해야 합니다. `src/libcamera/pipeline_handler.cpp:547`

근거 원문: [src/libcamera/pipeline_handler.cpp:547](#source-ca3f659653ce3f6a)

## 스레드 경계와 동기화

`Camera` 상태를 바꾸는 함수들은 `Camera` 클래스가 일반적으로 서로 동기화하지 않으므로, 필요한 경우 호출자가 이 함수들 사이의 동기화를 보장해야 합니다. `PipelineHandler::completeRequest()`의 호출 주체는 pipeline handler입니다. pipeline handler는 완료된 요청을 카메라에 알릴 때 이 함수를 호출해야 하며, 그 호출은 `CameraManager` 스레드에서 이루어져야 합니다. `src/libcamera/camera.cpp:780`, `src/libcamera/pipeline_handler.cpp:571`

근거 원문: [src/libcamera/camera.cpp:780](#source-33ababe2a4780075) · [src/libcamera/pipeline_handler.cpp:571](#source-7ac40780a56ae3a9)

## 정적 근거의 확인 범위

`Camera::start()`는 `d->isAccessAllowed(Private::CameraConfigured)`로 카메라 상태를 검사하고 그 반환값을 `ret`에 저장합니다. `ret`가 음수이면(`ret < 0`) `start()`는 `return ret;`으로 그 값을 그대로 반환하며, 이 분기에서는 파이프라인 시작 호출과 `Private::CameraRunning` 상태 전환이 실행되지 않습니다. API 주석의 `-EACCES`는 카메라가 시작할 수 없는 상태를 뜻하지만, 이 코드 조각만으로는 `isAccessAllowed()`가 `-EACCES`를 반환하는지 확인할 수 없으므로 두 값을 같은 것으로 단정하지 않습니다. 이 TODO 주석이 문서화를 요청한 대상은 카메라 시작 타이밍입니다. `src/libcamera/camera.cpp:1404`, `src/libcamera/camera.cpp:1383`, `src/libcamera/camera.cpp:755`

근거 원문: [src/libcamera/camera.cpp:755](#source-2e73109154ae3a90) · [src/libcamera/camera.cpp:1404](#source-bf3cae669253cabe) · [src/libcamera/camera.cpp:1383](#source-1bb135021258e6a5)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | Camera는 어떤 공개 기능과 객체 수명 계약을 제공합니까? | [컴포넌트별 책임](#컴포넌트별-책임) | 코드 근거와 설명 연결 |
    | 어느 파일과 진입점부터 읽고, 장치 탐색과 카메라 접근은 어떤 순서로 이어집니까? | [탐색과 파이프라인 선택](#탐색과-파이프라인-선택) | 코드 근거와 설명 연결 · 실행 확인 항목 별도 |
    | 요청 생성의 조건과 소유권·재사용 계약은 무엇입니까? | [요청 생성과 소유권](#요청-생성과-소유권) | 코드 근거와 설명 연결 |
    | 캡처를 준비하고 반복하고 끝내는 순서는 무엇입니까? | [캡처 세션의 상태와 자원](#캡처-세션의-상태와-자원) | 코드 근거와 설명 연결 |
    | 요청을 어떤 조건으로 제출하고 완료를 어떻게 통지받습니까? | [요청 제출과 완료](#요청-제출과-완료) | 코드 근거와 설명 연결 |
    | 버퍼 완료와 요청 완료는 어떻게 구분합니까? | [버퍼 완료와 요청 완료](#버퍼-완료와-요청-완료) | 코드 근거와 설명 연결 |
    | 상태 변경의 동기화 책임과 요청 완료의 실행 스레드는 무엇입니까? | [스레드 경계와 동기화](#스레드-경계와-동기화) | 코드 근거와 설명 연결 |
    | Camera::start()의 허용 상태와 상태 검사 실패 시 음수 오류 반환을 behavior로 설명하고, 별도 limitation에서 Camera 클래스 주석의 시작 타이밍 문서화 TODO만 설명하세요. 호출자 동기화 의무는 boundary 절에서 한 번 설명하므로 여기서 되풀이하지 마세요. TODO로 전체 구현이 미정이라고 추정하지 마세요. | [정적 근거의 확인 범위](#정적-근거의-확인-범위) | 코드 근거와 설명 연결 |

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

<a id="source-0c01857bf49370e2"></a>

??? note "소스 근거: src/libcamera/camera_manager.cpp:154"
    `src/libcamera/camera_manager.cpp:154`에서 시작하는 발췌입니다. 종료 줄은 169이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `9d849533ca73d2d4d7b3a00c565fb4226d372e08d7001bde8bb3d18eb287f0f4`
    
    ```text
    void CameraManager::Private::pipelineFactoryMatch(const PipelineHandlerFactoryBase *factory)
    {
    	CameraManager *const o = LIBCAMERA_O_PTR();
    
    	/* Provide as many matching pipelines as possible. */
    	while (1) {
    		std::shared_ptr<PipelineHandler> pipe = factory->create(o);
    		if (!pipe->match(enumerator_.get()))
    			break;
    
    		LOG(Camera, Debug)
    			<< "Pipeline handler \"" << factory->name()
    			<< "\" matched";
    	}
    }
    
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

<a id="source-0556d5e91908d040"></a>

??? note "소스 근거: src/libcamera/request.cpp:376"
    `src/libcamera/request.cpp:376`에서 시작하는 발췌입니다. 종료 줄은 404이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `b8358f2f31eecf64aa785310854e8d8736615d7ad24816d0d1916db424b7f351`
    
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

<a id="source-2e73109154ae3a90"></a>

??? note "소스 근거: src/libcamera/camera.cpp:755"
    `src/libcamera/camera.cpp:755`에서 시작하는 발췌입니다. 종료 줄은 755이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `fa53c392eca3eb23fa113575f5efb5ed42ce1ea38f034199417d8365c3b79e01`
    
    ```text
    \todo Add documentation for camera start timings.
    ```

<a id="source-bf3cae669253cabe"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1404"
    `src/libcamera/camera.cpp:1404`에서 시작하는 발췌입니다. 종료 줄은 1405이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `604f18ec7863ac1636e2cf6bf73286d6cfa15a0c6eaad0782eb3c612d0aac4d4`
    
    ```text
    int ret = d->isAccessAllowed(Private::CameraConfigured);
    	if (ret < 0)
    ```

<a id="source-1bb135021258e6a5"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1383"
    `src/libcamera/camera.cpp:1383`에서 시작하는 발췌입니다. 종료 줄은 1399이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `9121c6f5bd2e73de134af571dd2a8a2089f052b08739b10519bdf9433ea1b2b9`
    
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
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `293d751a81`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-31 · 사람 검토 전

다음 단계: [카메라와 요청 모델](camera-model.md)
