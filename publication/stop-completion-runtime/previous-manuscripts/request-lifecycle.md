---
generated_at: 2026-10-30T16:56:15+00:00
source_commit: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61
status: ok
section: request-lifecycle
generation_method: facts-and-llm
evidence_fingerprint: 22ef7a0e84b2b8f54b26a5a100e3491a5a6f347d08ca6385e8e255e78d691661
semantic_review: human-review-required
agent: cli/claude/claude-haiku-5-5
generated_design: {"schema": 1, "input_fingerprint": "22ef7a0e84b2b8f54b26a5a100e3491a5a6f347d08ca6385e8e255e78d691661", "answers": {"journey": [{"text": "createRequest의 반환 타입은 `std::unique_ptr<Request>`입니다. 반환되는 객체는 애플리케이션이 버퍼와 파라미터를 채우고 캡처용으로 큐에 넣기 위한 빈 `Request` 객체입니다. 오류가 발생하면 반환값은 nullptr입니다.", "evidence": ["create"], "covers": ["journey"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest(uint64_t cookie)", "part_id": "create"}, {"text": "`Request::addBuffer`는 `FrameBuffer`를 그 버퍼가 속한 `Stream`과 함께 `Request`에 추가하는 API입니다. 첫 번째 인자 stream이 버퍼가 속하는 스트림이며, 한 요청에는 스트림당 하나의 버퍼만 담을 수 있습니다. 같은 스트림에 이미 버퍼가 추가되어 있거나 버퍼가 아직 fence를 참조하고 있으면 -EEXIST가 반환되고, 버퍼가 유효한 `Stream`을 참조하지 않으면 -EINVAL이 반환됩니다.", "evidence": ["buffer"], "covers": ["journey"], "kind": "behavior", "quote": "\\brief Add a FrameBuffer with its associated Stream to the Request\n * \\param[in] stream The stream the buffer belongs to\n * \\param[in] buffer The FrameBuffer to add to the request\n * \\param[in] fence The optional fence\n *\n * A reference to the buffer is stored in the request. The caller is responsible\n * for ensuring that the buffer will remain valid until the request complete\n * callback is called.\n *\n * A request can only contain one buffer per stream. If a buffer has already\n * been added to the request for the same stream, this function returns -EEXIST.\n *\n * A Fence can be optionally associated with the \\a buffer.\n *\n * When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.\n *\n * If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request. Attempting to add a buffer that still\n * contains a fence to a request will result in this function returning -EEXIST.\n *\n * \\sa FrameBuffer::releaseFence()\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -EEXIST The request already contains a buffer for the stream\n *  or the buffer still references a fence\n * \\retval -EINVAL The buffer does not reference a valid Stream\n */\nint Request::addBuffer(const Stream *stream, FrameBuffer *buffer,", "part_id": "buffer"}, {"text": "`Camera::queueRequest`가 0을 반환하면 요청이 카메라 캡처를 위해 큐에 놓였다는 뜻입니다. 이 반환값은 캡처가 완료되었음을 의미하지 않습니다. 요청이 큐에 놓인 뒤 카메라의 완료는 requestCompleted 시그널을 통해 통지됩니다.", "evidence": ["queue"], "covers": ["journey"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();\n\n\tint ret = d->isAccessAllowed(Private::CameraRunning);\n\tif (ret < 0)\n\t\treturn ret;\n\n\t/* Requests can only be queued to the camera that created them. */\n\tif (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;\n\t}\n\n\tif (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}\n\n\t/* Make sure the Request has a valid control list. */\n\tif (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * The camera state may change until the end of the function. No locking\n\t * is however needed as PipelineHandler::queueRequest() will handle\n\t * this.\n\t */\n\n\tif (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}\n\n\t/* Pre-process AeEnable. */\n\tpatchControlList(request->controls());\n\n\td->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;\n}\n\n/**\n * \\brief Start capture from camera", "part_id": "submission"}, {"text": "`waitingRequests_`의 선두 요청에서 `prepared_`가 거짓이면 doQueueRequests()가 반복을 중단하므로, 뒤에 쌓인 요청도 장치로 전달되지 않습니다. 반면 `queuedRequests_`의 크기가 `maxQueuedRequestsDevice_`에 도달하면 반복이 중단되며, 이 크기 검사가 먼저 실행되므로 선두 요청의 상태와는 무관합니다.", "evidence": ["waiting-prepared", "device-queue"], "covers": ["journey"], "kind": "behavior", "quote": "Request *request = data->waitingRequests_.front();\n\t\tif (!request->_d()->prepared_)\n\t\t\tbreak;", "part_id": "waiting"}, {"text": "doQueueRequest는 void 함수이므로 호출자에게 반환하는 값이 없습니다. 함수는 먼저 request를 camera의 `queuedRequests_`에 `push_back`하고 `sequence_`를 부여한 뒤, request->`_d()`->`cancelled_`가 참이면 completeRequest(request)를 호출하고 return하여 queueRequestDevice 호출을 건너뜁니다. `cancelled_`가 거짓이면 queueRequestDevice(camera, request)를 호출하고, 그 결과 ret이 0이 아니면 cancelRequest(request)를 호출합니다.", "evidence": ["dispatch"], "covers": ["journey"], "kind": "behavior", "quote": "void PipelineHandler::doQueueRequest(Request *request)\n{\n\tLIBCAMERA_TRACEPOINT(request_device_queue, request);\n\n\tCamera *camera = request->_d()->camera();\n\tCamera::Private *data = camera->_d();\n\tdata->queuedRequests_.push_back(request);\n\n\trequest->_d()->sequence_ = data->requestSequence_++;\n\n\tif (request->_d()->cancelled_) {\n\t\tcompleteRequest(request);\n\t\treturn;\n\t}\n\n\tint ret = queueRequestDevice(camera, request);\n\tif (ret)\n\t\tcancelRequest(request);\n}", "part_id": "dispatch"}, {"text": "`PipelineHandler::queueRequestDevice()` 함수는 장치에 캡처 요청을 큐에 넣는 함수입니다. 이 함수는 성공하면 0을 반환하고, 오류가 발생하면 음수 오류 코드를 반환합니다.", "evidence": ["device-contract"], "covers": ["journey"], "kind": "behavior", "quote": "\\fn PipelineHandler::queueRequestDevice()\n * \\brief Queue a request to the device\n * \\param[in] camera The camera to queue the request to\n * \\param[in] request The request to queue\n *\n * This function queues a capture request to the device for processing. The\n * request contains a set of buffers associated with streams and a set of\n * parameters. The pipeline handler shall program the device to ensure that the\n * parameters will be applied to the frames captured in the buffers provided in\n * the request.\n *\n * \\context This function is called from the CameraManager thread.\n *\n * \\return 0 on success or a negative error code otherwise\n */", "part_id": "device-result"}, {"text": "파이프라인 핸들러는 버퍼 완료를 알릴 때 `CameraManager` 스레드에서 completeBuffer를 호출해야 합니다. 마지막 버퍼가 완료되어도 요청은 자동으로 완료되지 않으므로, 핸들러는 completeRequest를 별도로 명시 호출해야 합니다.", "evidence": ["buffer-notice", "request-duty", "completion"], "covers": ["journey"], "kind": "behavior", "quote": "The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().", "part_id": "buffer-complete"}, {"text": "completeRequest는 camera의 `queuedRequests_` 앞쪽부터 요청을 확인하며, 요청의 status()가 `Request::RequestPending`이면 반복을 중단합니다. 그 밖의 경우에는 ASSERT로 hasPendingBuffers()가 거짓임을 확인한 뒤 큐 앞에서 요청을 제거하고 requestComplete(req)로 애플리케이션에 반환하므로 제출 순서가 유지됩니다.", "evidence": ["completed-head", "request-notice"], "covers": ["journey"], "kind": "behavior", "quote": "if (req->status() == Request::RequestPending)\n\t\t\tbreak;", "part_id": "request-complete"}], "resources": [{"text": "`createRequest`가 반환한 요청의 소유권은 호출자에게 넘어가며, 요청을 삭제할 책임도 호출자에게 있습니다. 요청은 완료 핸들러에서 삭제될 수 있고, `Request::reuse()`로 상태를 초기화한 뒤 다시 사용할 수도 있습니다. 문서는 `Request::reuse()`를 큐에 넣기 전에 호출하는 방식으로 설명하며, 애플리케이션은 `ReuseBuffers` 플래그로 이전에 `addBuffer()`로 추가한 버퍼를 재사용할 수 있다고 적습니다.", "evidence": ["create", "reuse"], "covers": ["resources"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest(uint64_t cookie)", "part_id": "request-owner"}, {"text": "`Request::addBuffer`는 전달받은 버퍼의 참조를 요청에 저장합니다. 호출자는 요청 완료 콜백이 호출될 때까지 버퍼가 유효하게 남아 있도록 해야 합니다.", "evidence": ["buffer-duty", "buffer"], "covers": ["resources"], "kind": "behavior", "quote": "A reference to the buffer is stored in the request. The caller is responsible\n * for ensuring that the buffer will remain valid until the request complete\n * callback is called.", "part_id": "buffer-validity"}, {"text": "`addBuffer`에 유효한 `Fence`가 전달되면 그 `Fence`는 `buffer` 인자의 `FrameBuffer` 버퍼로 이동합니다. `Fence` 소유권은 `addBuffer`가 성공한 경우에만 넘어가며, 실패하면 `Fence`는 수정되지 않은 상태로 남습니다. 따라서 `Fence` 소유권의 이동 대상은 요청에 추가되는 `buffer` 버퍼 객체입니다.", "evidence": ["fence-move"], "covers": ["resources"], "kind": "behavior", "quote": "When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.", "part_id": "fence-transfer"}, {"text": "`Request::addBuffer()`가 실패하면 전달받은 fence는 수정되지 않고 그대로 남습니다. 소스 주석에 따르면 fence의 소유권은 성공한 경우에만 가져가며, 실패하면 fence는 변경 없이 유지됩니다. 실패 사례로 buffer가 아직 fence를 참조하고 있으면 `-EEXIST`가 반환됩니다.", "evidence": ["fence-move"], "covers": ["resources"], "kind": "behavior", "quote": "When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.", "part_id": "fence-failure"}, {"text": "펜스가 신호되지 않으면 요청은 타임아웃 후 실패합니다. 이때 버퍼에는 펜스가 그대로 남아 있습니다. 애플리케이션은 이 버퍼를 다른 요청에 재사용하기 전에 `FrameBuffer::releaseFence()`로 펜스를 회수해야 합니다.", "evidence": ["fence-expiry"], "covers": ["resources"], "kind": "behavior", "quote": "If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request.", "part_id": "fence-timeout"}, {"text": "`Request::ReuseBuffers` 플래그는 `Request::reuse()`의 동작을 제어하며, 이 플래그를 쓰면 `addBuffer()`로 이전에 추가된 버퍼를 유지하여 다시 사용합니다. 다만 버퍼에 연결된 펜스(fence)는 재사용되지 않습니다. 원문은 펜스를 사용하는 경우 이 플래그를 피하도록 권고하므로, 펜스를 사용할 때에는 `Request::ReuseBuffers`를 피하는 것이 바람직합니다.", "evidence": ["reuse-flags", "reuse-advice"], "covers": ["resources"], "kind": "behavior", "quote": "\\enum Request::ReuseFlag\n * Flags to control the behavior of Request::reuse()\n * \\var Request::Default\n * Don't reuse buffers\n * \\var Request::ReuseBuffers\n * Reuse the buffers that were previously added by addBuffer()\n *\n * \\note Fences associated with the buffers are not reused.\n *  This flag should not be used if fences are used.\n */", "part_id": "reuse-fences"}, {"text": "`PipelineHandler::completeRequest()`는 파이프라인 핸들러가 요청 완료를 `Camera`에 알릴 때 호출해야 하며, 이 함수가 반환된 뒤에는 파이프라인 핸들러가 해당 요청에 접근해서는 안 됩니다. `cancelRequest()`는 요청을 `_d()->cancel()`로 취소한 뒤 `completeRequest()`를 호출하고, 문서상 `completeRequest()`와 같은 규칙이 적용됩니다. 따라서 이 규칙의 주체는 `cancelRequest()`를 호출한 파이프라인 핸들러이며, 시점은 `cancelRequest()` 반환 이후입니다.", "evidence": ["complete-access", "completion", "cancel-rules"], "covers": ["resources"], "kind": "behavior", "quote": "The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.", "part_id": "handler-access"}], "stopping": [{"text": "조사 계획으로 `Camera::stop`에서 `d->isRunning()`이 거짓이면 `0`을 반환하는 경로와, `d->isAccessAllowed(Private::CameraRunning)`이 음수를 반환하면 그 값을 그대로 돌려주는 경로를 구분해 관찰합니다. 두 검사를 통과하면 `Private::CameraStopping` 상태 설정 뒤 `ConnectionTypeBlocking`으로 `PipelineHandler::stop`을 호출하는 진입 시점과 호출에서 복귀하는 시점을 로그 `Stopping capture`와 함께 확인합니다. 복귀 후 `ASSERT(!d->pipe_->hasPendingRequests(this))`의 pending 요청 여부, `Private::CameraConfigured`로 설정되는 상태, 마지막 `return 0`을 기록하되 이는 실행한 테스트나 시간 측정이 아니며 상태 변경 함수를 다시 호출하지 않습니다.", "evidence": ["stop", "stopping-call"], "covers": ["stopping"], "kind": "behavior", "quote": "d->setState(Private::CameraStopping);\n\n\td->pipe_->invokeMethod(&PipelineHandler::stop, ConnectionTypeBlocking,\n\t\t\t       this);", "part_id": "camera-entry"}, {"text": "이 내용은 실행 결과가 아닌 조사 계획입니다. `PipelineHandler::stop`에서 `data->waitingRequests_`를 로컬 큐와 `swap`으로 분리한 직후의 값을 기록하고, `stopDevice(camera)` 진입 시점과 복귀 시점을 함께 기록하면 장치 내부에서 멎은 경우와 반환한 경우를 구분할 수 있습니다.", "evidence": ["device-stop"], "covers": ["stopping"], "kind": "behavior", "quote": "\\brief Stop capturing from all running streams and cancel pending requests\n * \\param[in] camera The camera to stop\n *\n * This function stops capturing and processing requests immediately. All\n * pending requests are cancelled and complete immediately in an error state.\n *\n * \\context This function is called from the CameraManager thread.\n */\nvoid PipelineHandler::stop(Camera *camera)\n{\n\t/*\n\t * Take all waiting requests so that they are not requeued in response\n\t * to completeRequest() being called inside stopDevice(). Cancel them\n\t * after the device to keep them in order.\n\t */\n\tCamera::Private *data = camera->_d();\n\tstd::queue<Request *> waitingRequests;\n\twaitingRequests.swap(data->waitingRequests_);", "part_id": "device-entry"}, {"text": "이 발췌는 `PipelineHandler::stop()`의 대기 요청 취소 루프에서 `doQueueRequest`가 어떤 `request` 인자로 호출되는지 확인하기 위한 조사 계획입니다. 이 계획은 실행한 테스트나 시간 측정이 아니며, 정지 경로의 전체 함수를 나열하지 않습니다. 관찰 대상은 `waitingRequests` 지역 큐에서 꺼낸 `request` 변수, `request->_d()->cancel()` 호출 뒤 `doQueueRequest(request);`에 전달되는 값, 루프 종료 뒤 두 `ASSERT` 조건입니다. 상태를 바꾸는 `stop()`이나 `doQueueRequest()`를 다시 호출해서 관찰하지 않고, 발췌 코드에 있는 변수와 분기만 기록합니다.", "evidence": ["pending-requeue"], "covers": ["stopping"], "kind": "behavior", "quote": "doQueueRequest(request);", "part_id": "pending"}, {"text": "이 항목은 실행 결과가 아닌 조사 계획입니다. `PipelineHandler::stop()` 끝의 두 `ASSERT(data->queuedRequests_.empty())`와 `ASSERT(data->waitingRequests_.empty())`가 검사하는 `queuedRequests_`와 `waitingRequests_`의 빈 상태를, 두 `ASSERT` 줄 직전 지점에서 변수 값으로 관찰할 수 있습니다. 두 검사 뒤에는 `data->requestSequence_ = 0;`이 실행되므로, 관찰 대상에 이 줄 이후의 `requestSequence_` 값을 포함할 수 있습니다. 관찰하려고 상태를 바꾸는 `stop()`을 다시 호출하지 않습니다.", "evidence": ["stop-assertions"], "covers": ["stopping"], "kind": "behavior", "quote": "ASSERT(data->queuedRequests_.empty());\n\tASSERT(data->waitingRequests_.empty());", "part_id": "queue-assertions"}, {"text": "파이프라인 핸들러는 `completeRequest()`를 `CameraManager` 스레드에서 호출해야 하며, 이 함수는 요청이 제출 순서대로 애플리케이션에 반환되도록 합니다. 함수가 반환된 뒤에는 핸들러가 해당 요청을 더 이상 관리하지 않으므로 그 요청에 접근해서는 안 됩니다.", "evidence": ["completion"], "covers": ["stopping"], "kind": "behavior", "quote": "/**\n * \\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();", "part_id": "completion"}, {"text": "아직 실행하지 않은 조사 계획으로, 애플리케이션 콜백의 진입·복귀 시점과 실행 스레드를 `completeRequest` 호출 문맥과 구분해 콜백 내부 로그로 기록하고, 상태를 바꾸는 함수는 다시 호출하지 않고 관측합니다. `completeRequest`는 `CameraManager thread`에서 호출해야 하는 파이프라인 핸들러의 의무이며, 콜백 실행 결과는 아직 검증 전이므로 이 계획만으로 콜백 스레드나 시점이 같다고 확인되지 않습니다.", "evidence": ["completion"], "covers": ["stopping"], "kind": "limitation", "quote": "/**\n * \\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();", "part_id": "callback-observation"}, {"text": "`Camera::disconnect()`는 `_d()->disconnect()`를 먼저 호출하고, 그 호출이 끝난 뒤 `disconnected.emit()`을 실행합니다. 따라서 `_d()->disconnect()`의 처리는 `disconnected` 시그널 발생보다 앞선 순서로 실행됩니다. 제공된 소스에는 `_d()->disconnect()`의 본문이 없으므로, 이 내부 함수가 구체적으로 무엇을 처리하는지는 확인할 수 없습니다.", "evidence": ["disconnect-internal", "notification"], "covers": ["stopping"], "kind": "behavior", "quote": "_d()->disconnect();", "part_id": "disconnect"}, {"text": "`Camera::disconnect()` 함수 안의 `disconnected.emit();` 호출은 `disconnected` 신호를 발행합니다.", "evidence": ["disconnect-signal"], "covers": ["stopping"], "kind": "behavior", "quote": "disconnected.emit();", "part_id": "disconnect-signal"}, {"text": "`Camera::disconnect()` 함수의 설명 주석에 있는 `\\todo` 항목은 카메라가 실행 중(running state)일 때 연결이 해제되는 경우, 아직 처리하지 않은 대기 요청(pending requests)을 어떻게 다룰지가 남아 있음을 표시합니다.", "evidence": ["disconnect-todo-owner", "disconnect-todo"], "covers": ["stopping"], "kind": "behavior", "quote": "\\brief Notify camera disconnection\n *\n * This function is used to notify the camera instance that the underlying\n * hardware has been unplugged. In response to the disconnection the camera\n * instance notifies the application by emitting the #disconnected signal, and\n * ensures that all new calls to the application-facing Camera API return an\n * error immediately.\n *\n * \\todo Deal with pending requests if the camera is disconnected in a\n * running state.\n */\nvoid Camera::disconnect()", "part_id": "disconnect-todo"}], "review": [{"text": "`Camera::queueRequest` 호출마다 반환값을 그대로 기록하고, 기록 항목에서 성공 0과 실패 음수 오류 코드를 구분하는 조사 계획을 제안합니다.", "evidence": ["queue"], "covers": ["review"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();\n\n\tint ret = d->isAccessAllowed(Private::CameraRunning);\n\tif (ret < 0)\n\t\treturn ret;\n\n\t/* Requests can only be queued to the camera that created them. */\n\tif (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;\n\t}\n\n\tif (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}\n\n\t/* Make sure the Request has a valid control list. */\n\tif (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * The camera state may change until the end of the function. No locking\n\t * is however needed as PipelineHandler::queueRequest() will handle\n\t * this.\n\t */\n\n\tif (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}\n\n\t/* Pre-process AeEnable. */\n\tpatchControlList(request->controls());\n\n\td->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;\n}\n\n/**\n * \\brief Start capture from camera", "part_id": "submission-record"}, {"text": "대입 대상은 `status_`이며, 기록 항목은 `Request::reuse(ReuseFlag flags)` 안의 `status_ = RequestPending;` 대입 전후에 `status_`, `controls_`, `metadata_` 값을 남기는 것입니다. `controls_.clear();`와 `_d()->metadata_.clear();`는 대입 뒤에 놓여 있어 두 값이 대입 이후 비워지는 지점을 표시합니다. 이 항목은 제안이며, 실행된 테스트나 측정 결과가 아닙니다. 원문에 이 기록을 의무로 정한 문장은 없습니다.", "evidence": ["record-status", "record-controls", "record-metadata"], "covers": ["review"], "kind": "behavior", "quote": "status_ = RequestPending;", "part_id": "reuse-state-record"}, {"text": "선두 요청의 상태 조회식은 코드 그대로 `req->status() == Request::RequestPending`입니다. 이 식은 `data->queuedRequests_.front()`로 얻은 `req`에 대해 `status()`를 호출하고 그 결과를 `Request::RequestPending`과 비교합니다. 따라서 기록 항목으로 이 식의 평가 결과와 대상 `req`를 함께 남기는 것을 제안합니다. 이 항목은 소스가 기록을 요구하는 것이 아니라 선택적 관찰 계획이며, 실제 테스트 결과나 측정값이 아닙니다.", "evidence": ["record-head-status"], "covers": ["review"], "kind": "behavior", "quote": "if (req->status() == Request::RequestPending)\n\t\t\tbreak;", "part_id": "completion-record"}]}, "topic_inputs": {"journey": "c1367f4989476bd7713a267129396f5e0e1f5eb149255c52d47fc3f0a2dd5694", "resources": "fd506a9689ec5f62ce48742acd47cea5be5c66fb966c689fc83a8d88ad08ea5d", "stopping": "fa109e16d90d856bca975ce7b0a0fae70cb93e97803a911815cbf4cd439d285d", "review": "16aaf3e6061786ee7b729d9c349e95d7b8438e32fda3625ad29a61e2846f1cb9"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["journey", "resources", "stopping", "review"], "topic_agents": {"journey": "cli/claude/claude-haiku-5-5", "resources": "cli/claude/claude-haiku-5-5", "stopping": "cli/claude/claude-haiku-5-5", "review": "cli/claude/claude-haiku-5-5"}, "grounding_review": "not-run", "grounding_policy": null, "validation_policy": {"manuscript": "e0c429a5c80a01c34563ce00a616df89d8f75c735f8669bcbd1f75d84cce82a6", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "281d217a1d4a212dd56cdb3ce61e9fae7a4622099962c1beee847a57866e83e0", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "fecc4ee78a481139776e562c164c0da9a3e5edf0a64a72be1d1c8feddee3cd08", "answer_contracts": "1e0d24e0cf26ded53ecec2e5a6fbc51836bac6e17530318a9fa7cffaa936c00b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "9db4d42a710b4a71a7d2bb16f69db06926409281dc1a200c796e77d5deaa25a0", "design_response": "74ebb2d21768d6bdd4ef7611c1c539526a7e72e6a58604c82e8305003d24f8b7", "design_validation": "b8133c78a8eb42fd5194c2756bb649b396ec54b40c49b72544bdbbcaf3366c57"}, "validation_model": "6d7b40d6cf6b277e785cb3b10128faa4707edc543d8ca670138f358e37cf5bd9", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "f8fd5a3d8041c23fc68b93ff32b8727e98393383b5099032eb00ad0013e7611c"}, "checkpoint_units": [{"checkpoint": "91afb87718e0fb9de3047e41f822adac91c6dcfbdc021d1beabc9cbe508621b5.json", "topic": "journey", "part": "create", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/001.receipt.json"]}, {"checkpoint": "3b4b9efe76c4e64c9329c239083ece7ecafa11d517ce7736e4d1f694ed93e151.json", "topic": "journey", "part": "buffer", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/002.receipt.json"]}, {"checkpoint": "f9e8d903bfcd94aff509615d48d7a209a138987fcefc6dc13bc2f0001397bea4.json", "topic": "journey", "part": "submission", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/003.receipt.json"]}, {"checkpoint": "cce05e120902de18a434a793f5b23223e03ae57c807f28a171a145d81062e292.json", "topic": "journey", "part": "waiting", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/004.receipt.json"]}, {"checkpoint": "bd20ab7997813d6385948905f0a666be1919a5ad9af6c94a9235fa2df33d125c.json", "topic": "journey", "part": "dispatch", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/005.receipt.json"]}, {"checkpoint": "9cdcf9d7a196fa040c85e4f6ac81e5c951b746daf3c4b982dc9fd200d42a6892.json", "topic": "journey", "part": "device-result", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/006.receipt.json"]}, {"checkpoint": "1ea5c986e43d540a9524be6669dafc29289c31a87c0e48ad5eadc9c6e68ddd55.json", "topic": "journey", "part": "buffer-complete", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["599ffde9b144426e8753273befe0baeb/001.receipt.json"]}, {"checkpoint": "f62547a3137080cf9448b87953113b8a467122685701eacddb19e378cbf253e9.json", "topic": "journey", "part": "request-complete", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/008.receipt.json"]}, {"checkpoint": "9404119f9edabef653acf8dc916cdea855b13e814bdebcc7f0e6383b8093ad93.json", "topic": "resources", "part": "request-owner", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/009.receipt.json"]}, {"checkpoint": "335d4acc4627c9cb435f240742294430c5acc02a44c6cc9cd56e9469268a4d8d.json", "topic": "resources", "part": "buffer-validity", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/010.receipt.json"]}, {"checkpoint": "c0f5b30e2865816e7ba473d91c7104c204f26f48d59bbeee2ab99d29b76f4b04.json", "topic": "resources", "part": "fence-transfer", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/011.receipt.json"]}, {"checkpoint": "f12710f4a6c75b17889958849482f80dcc41b00f03428287847cc9ae0661f60d.json", "topic": "resources", "part": "fence-failure", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/012.receipt.json"]}, {"checkpoint": "e9b620f193bc6d3a65a1f8f9f1ea9e523704b08aaf3875b298edea3cdbfa2932.json", "topic": "resources", "part": "fence-timeout", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/013.receipt.json"]}, {"checkpoint": "e159d6cc70df887422ca6dc19a1f33622e7d0fc6afc5301984fe6480c70226d0.json", "topic": "resources", "part": "reuse-fences", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/014.receipt.json"]}, {"checkpoint": "cd4591d85947a7210170add057f24d608091e052fd7dd0fd8246aa1e124c219f.json", "topic": "resources", "part": "handler-access", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/015.receipt.json"]}, {"checkpoint": "c8cc3b4ba9564c15d0ac492bfb772701002cc0b58bbc4d0aeb6e40aef13ff891.json", "topic": "stopping", "part": "camera-entry", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/016.receipt.json"]}, {"checkpoint": "c37e54e48cfbf252636bfd190e5afb437e791566581dc03f093460229a728c4a.json", "topic": "stopping", "part": "device-entry", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/017.receipt.json"]}, {"checkpoint": "cff9ddb567faeb342aab52e685ee5b747d9bca58d6721d691ec8b67c98a51d7f.json", "topic": "stopping", "part": "pending", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/018.receipt.json"]}, {"checkpoint": "b1d4004dccf8d2c7d5c17ded367bbb027421331e4469055d4029f315005eb3f4.json", "topic": "stopping", "part": "queue-assertions", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/019.receipt.json"]}, {"checkpoint": "ae17f525c86695b9c3ac209e5621165d5df8151fe845933ad1fccfc729a3d0f4.json", "topic": "stopping", "part": "completion", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/020.receipt.json"]}, {"checkpoint": "9d946c2cc6479707120038c71881382ac1d3d6abd490d2bc3d0fdf4885488913.json", "topic": "stopping", "part": "callback-observation", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/021.receipt.json"]}, {"checkpoint": "769818a8ccffc0c90ede0eaa0464a13bc8fa1df9ab691a1504e90da1044b732a.json", "topic": "stopping", "part": "disconnect", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/022.receipt.json"]}, {"checkpoint": "792b3bd4c18ed0866bf81cab11461d01853ad07437d7c881d044a9196f2843e8.json", "topic": "stopping", "part": "disconnect-signal", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/023.receipt.json"]}, {"checkpoint": "cab512bf30872c19411cc6d584f97e0a2571d53cd1531b588c1a4e35bc404bdf.json", "topic": "stopping", "part": "disconnect-todo", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/024.receipt.json"]}, {"checkpoint": "efba55d065d1f2cc695fac53f70bd6240b0fc42730756de44f793cffd8533c77.json", "topic": "review", "part": "reuse-state-record", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/026.receipt.json"]}, {"checkpoint": "d6eb7ea10aa14fe26eb6003fe4c366d274d090ef8960b5b1a354061446d17d18.json", "topic": "review", "part": "completion-record", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["2b85735f892e4bbdb5a5c60d0b4e6ac4/027.receipt.json"]}], "body_sha256": "5be6b61e154cda9f37f57b9b6402f53481c510a20417d9fc74caeeedf79969d7"}
revalidated_from: 212c689fcf2450bbfbaab25c7472895ac277b5d6
---

# 요청 처리와 문제 진단

**요청의 제출 성공과 촬영 완료를 구분하고, 버퍼를 유지할 기간과 오류가 난 위치를 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| <a id="구성-실패를-좁히는-순서"></a>구성 실패를 좁히는 순서의 조건과 근거를 대조하세요. | [구성과 요청 오류 조사](request-diagnosis.md#구성-실패를-좁히는-순서) |
| 요청 제출과 완료의 연결을 확인합니다. | [제출에서 완료까지](#제출에서-완료까지) |
| 자원을 재사용하거나 해제할 시점을 확인합니다. | [요청·버퍼·fence의 수명](#요청버퍼fence의-수명) |
| <a id="실패-위치별-확인-순서"></a>실패 위치별 확인 순서의 조건과 근거를 대조하세요. | [구성과 요청 오류 조사](request-diagnosis.md#실패-위치별-확인-순서) |
| 정지와 연결 해제의 차이를 확인합니다. | [정지와 연결 해제를 구분하기](#정지와-연결-해제를-구분하기) |
| <a id="요청이-대기하거나-장치로-가는-조건"></a>“요청이 대기하거나 장치로 가는 조건” 그림을 확인하세요. | [구성과 요청 오류 조사](request-diagnosis.md#요청이-대기하거나-장치로-가는-조건) |
| <a id="구성-실패를-좁히는-분기"></a>“구성 실패를 좁히는 분기” 그림을 확인하세요. | [구성과 요청 오류 조사](request-diagnosis.md#구성-실패를-좁히는-분기) |

## 제출에서 완료까지

createRequest의 반환 타입은 `std::unique_ptr<Request>`입니다. 반환되는 객체는 애플리케이션이 버퍼와 파라미터를 채우고 캡처용으로 큐에 넣기 위한 빈 `Request` 객체입니다. 오류가 발생하면 반환값은 nullptr입니다. `src/libcamera/camera.cpp:1243`

<!-- sdd:visual:request-stages -->
### 제출·준비·장치 처리·완료의 연결

접수 성공 뒤에도 준비 대기와 장치 처리가 남습니다. 정상 촬영 경로의 계약을 연결한 그림이며 실제 실행 시간이나 전체 실패 경로를 나타내지 않습니다.

```mermaid
flowchart TB
%% sdd:translations {"Camera::queueRequest()": "Camera::queueRequest()", "completeBuffer()": "completeBuffer()", "completeRequest()": "completeRequest()", "queueRequestDevice()": "queueRequestDevice()", "대기열과 준비 단계": "Waiting queue and <br/>preparation", "버퍼 완료 알림": "Notify buffer completion", "버퍼 추적 상태 갱신": "Update buffer completion <br/>tracking", "선두 미완료 요청 뒤의 <br/>반환은 대기": "Wait behind an incomplete <br/>head request", "장치 구현자가 버퍼 완료 통지": "Device handler signals <br/>buffer completion", "제출 순서로 애플리케이션 <br/>반환": "Return to application in <br/>submission order", "준비·큐 한도 통과, 취소되지 <br/>않은 요청": "Prepared, within queue <br/>limit and not cancelled", "핸들러 호출을 큐에 예약": "Queue the handler invocation", "후처리 뒤 구현자가 <br/>명시적으로 호출": "Handler explicitly <br/>completes after remaining <br/>work"}
  v_queue["Camera::queueRequest()"]
  v_waiting["대기열과 준비 단계"]
  v_device["queueRequestDevice()"]
  v_buffer["completeBuffer()"]
  v_remaining["버퍼 추적 상태 갱신"]
  v_request["completeRequest()"]
  v_application["제출 순서로 애플리케이션 <br/>반환"]
  v_queue -->|"핸들러 호출을 큐에 예약"| v_waiting
  v_waiting -->|"준비·큐 한도 통과, 취소되지 <br/>않은 요청"| v_device
  v_device -->|"장치 구현자가 버퍼 완료 통지"| v_buffer
  v_buffer -->|"버퍼 완료 알림"| v_remaining
  v_remaining -->|"후처리 뒤 구현자가 <br/>명시적으로 호출"| v_request
  v_request -->|"선두 미완료 요청 뒤의 <br/>반환은 대기"| v_application
```

[Mermaid 원문](request-lifecycle.request-stages.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | Camera::queueRequest() | [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) |
    | 대기열과 준비 단계 | [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) |
    | queueRequestDevice() | [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) |
    | completeBuffer() | [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) |
    | 버퍼 추적 상태 갱신 | [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) |
    | completeRequest() | [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) |
    | 제출 순서로 애플리케이션 반환 | [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) |
    | 핸들러 호출을 큐에 예약 | [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) |
    | 준비·큐 한도 통과, 취소되지 않은 요청 | [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) |
    | 장치 구현자가 버퍼 완료 통지 | [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) |
    | 버퍼 완료 알림 | [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) |
    | 후처리 뒤 구현자가 명시적으로 호출 | [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) |
    | 선두 미완료 요청 뒤의 반환은 대기 | [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) |
<!-- /sdd:visual:request-stages -->

`Request::addBuffer`는 `FrameBuffer`를 그 버퍼가 속한 `Stream`과 함께 `Request`에 추가하는 API입니다. 첫 번째 인자 stream이 버퍼가 속하는 스트림이며, 한 요청에는 스트림당 하나의 버퍼만 담을 수 있습니다. 같은 스트림에 이미 버퍼가 추가되어 있거나 버퍼가 아직 fence를 참조하고 있으면 -EEXIST가 반환되고, 버퍼가 유효한 `Stream`을 참조하지 않으면 -EINVAL이 반환됩니다. `src/libcamera/request.cpp:442`

`Camera::queueRequest`가 0을 반환하면 요청이 카메라 캡처를 위해 큐에 놓였다는 뜻입니다. 이 반환값은 캡처가 완료되었음을 의미하지 않습니다. 요청이 큐에 놓인 뒤 카메라의 완료는 requestCompleted 시그널을 통해 통지됩니다. `src/libcamera/camera.cpp:1308`

`waitingRequests_`의 선두 요청에서 `prepared_`가 거짓이면 doQueueRequests()가 반복을 중단하므로, 뒤에 쌓인 요청도 장치로 전달되지 않습니다. 반면 `queuedRequests_`의 크기가 `maxQueuedRequestsDevice_`에 도달하면 반복이 중단되며, 이 크기 검사가 먼저 실행되므로 선두 요청의 상태와는 무관합니다. `src/libcamera/pipeline_handler.cpp:516`, `src/libcamera/pipeline_handler.cpp:428`

doQueueRequest는 void 함수이므로 호출자에게 반환하는 값이 없습니다. 함수는 먼저 request를 camera의 `queuedRequests_`에 `push_back`하고 `sequence_`를 부여한 뒤, request->`_d()`->`cancelled_`가 참이면 completeRequest(request)를 호출하고 return하여 queueRequestDevice 호출을 건너뜁니다. `cancelled_`가 거짓이면 queueRequestDevice(camera, request)를 호출하고, 그 결과 ret이 0이 아니면 cancelRequest(request)를 호출합니다. `src/libcamera/pipeline_handler.cpp:483`

`PipelineHandler::queueRequestDevice()` 함수는 장치에 캡처 요청을 큐에 넣는 함수입니다. 이 함수는 성공하면 0을 반환하고, 오류가 발생하면 음수 오류 코드를 반환합니다. 파이프라인 핸들러는 버퍼 완료를 알릴 때 `CameraManager` 스레드에서 completeBuffer를 호출해야 합니다. 마지막 버퍼가 완료되어도 요청은 자동으로 완료되지 않으므로, 핸들러는 completeRequest를 별도로 명시 호출해야 합니다. `src/libcamera/pipeline_handler.cpp:530`, `src/libcamera/pipeline_handler.cpp:547`, `src/libcamera/pipeline_handler.cpp:553`

completeRequest는 camera의 `queuedRequests_` 앞쪽부터 요청을 확인하며, 요청의 status()가 `Request::RequestPending`이면 반복을 중단합니다. 그 밖의 경우에는 ASSERT로 hasPendingBuffers()가 거짓임을 확인한 뒤 큐 앞에서 요청을 제거하고 requestComplete(req)로 애플리케이션에 반환하므로 제출 순서가 유지됩니다. `src/libcamera/pipeline_handler.cpp:594`, `src/libcamera/pipeline_handler.cpp:571`

근거 원문: [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) · [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) · [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) · [src/libcamera/pipeline_handler.cpp:483](#source-7348e9b4af985eb2) · [src/libcamera/pipeline_handler.cpp:530](#source-c05f8214908fe4fe) · [src/libcamera/pipeline_handler.cpp:547](#source-ab8710f8a8a7905d) · [src/libcamera/pipeline_handler.cpp:571](#source-236c920e906cb6fd) · [src/libcamera/pipeline_handler.cpp:516](#source-a637b7daf9acb7ac) · [src/libcamera/pipeline_handler.cpp:553](#source-5b0ae08604dff588) · [src/libcamera/pipeline_handler.cpp:594](#source-bae861ceef5e8406)

## 요청·버퍼·fence의 수명

`createRequest`가 반환한 요청의 소유권은 호출자에게 넘어가며, 요청을 삭제할 책임도 호출자에게 있습니다. 요청은 완료 핸들러에서 삭제될 수 있고, `Request::reuse()`로 상태를 초기화한 뒤 다시 사용할 수도 있습니다. 문서는 `Request::reuse()`를 큐에 넣기 전에 호출하는 방식으로 설명하며, 애플리케이션은 `ReuseBuffers` 플래그로 이전에 `addBuffer()`로 추가한 버퍼를 재사용할 수 있다고 적습니다. `src/libcamera/camera.cpp:1243`, `src/libcamera/request.cpp:376`

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

[Mermaid 원문](request-lifecycle.request-ownership.mmd)

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

`Request::addBuffer`는 전달받은 버퍼의 참조를 요청에 저장합니다. 호출자는 요청 완료 콜백이 호출될 때까지 버퍼가 유효하게 남아 있도록 해야 합니다. `src/libcamera/request.cpp:447`, `src/libcamera/request.cpp:442`

`addBuffer`에 유효한 `Fence`가 전달되면 그 `Fence`는 `buffer` 인자의 `FrameBuffer` 버퍼로 이동합니다. `Fence` 소유권은 `addBuffer`가 성공한 경우에만 넘어가며, 실패하면 `Fence`는 수정되지 않은 상태로 남습니다. 따라서 `Fence` 소유권의 이동 대상은 요청에 추가되는 `buffer` 버퍼 객체입니다. `src/libcamera/request.cpp:456`

`Request::addBuffer()`가 실패하면 전달받은 fence는 수정되지 않고 그대로 남습니다. 소스 주석에 따르면 fence의 소유권은 성공한 경우에만 가져가며, 실패하면 fence는 변경 없이 유지됩니다. 실패 사례로 buffer가 아직 fence를 참조하고 있으면 `-EEXIST`가 반환됩니다. `src/libcamera/request.cpp:456`

펜스가 신호되지 않으면 요청은 타임아웃 후 실패합니다. 이때 버퍼에는 펜스가 그대로 남아 있습니다. 애플리케이션은 이 버퍼를 다른 요청에 재사용하기 전에 `FrameBuffer::releaseFence()`로 펜스를 회수해야 합니다. `src/libcamera/request.cpp:462`

`Request::ReuseBuffers` 플래그는 `Request::reuse()`의 동작을 제어하며, 이 플래그를 쓰면 `addBuffer()`로 이전에 추가된 버퍼를 유지하여 다시 사용합니다. 다만 버퍼에 연결된 펜스(fence)는 재사용되지 않습니다. 원문은 펜스를 사용하는 경우 이 플래그를 피하도록 권고하므로, 펜스를 사용할 때에는 `Request::ReuseBuffers`를 피하는 것이 바람직합니다. `src/libcamera/request.cpp:326`, `src/libcamera/request.cpp:334`

`PipelineHandler::completeRequest()`는 파이프라인 핸들러가 요청 완료를 `Camera`에 알릴 때 호출해야 하며, 이 함수가 반환된 뒤에는 파이프라인 핸들러가 해당 요청에 접근해서는 안 됩니다. `cancelRequest()`는 요청을 `_d()->cancel()`로 취소한 뒤 `completeRequest()`를 호출하고, 문서상 `completeRequest()`와 같은 규칙이 적용됩니다. 따라서 이 규칙의 주체는 `cancelRequest()`를 호출한 파이프라인 핸들러이며, 시점은 `cancelRequest()` 반환 이후입니다. `src/libcamera/pipeline_handler.cpp:575`, `src/libcamera/pipeline_handler.cpp:547`, `src/libcamera/pipeline_handler.cpp:610`

근거 원문: [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) · [src/libcamera/request.cpp:376](#source-38494771cb29cc8c) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) · [src/libcamera/request.cpp:326](#source-447804db33308244) · [src/libcamera/request.cpp:456](#source-86a8d784a8348122) · [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) · [src/libcamera/request.cpp:447](#source-4cdce80c57526221) · [src/libcamera/pipeline_handler.cpp:575](#source-d93a02e9220fa760) · [src/libcamera/pipeline_handler.cpp:610](#source-52fb58c8956b1a91) · [src/libcamera/request.cpp:334](#source-d9944a69f2dd6758) · [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1)

## 정지와 연결 해제를 구분하기

조사 계획으로 `Camera::stop`에서 `d->isRunning()`이 거짓이면 `0`을 반환하는 경로와, `d->isAccessAllowed(Private::CameraRunning)`이 음수를 반환하면 그 값을 그대로 돌려주는 경로를 구분해 관찰합니다. 두 검사를 통과하면 `Private::CameraStopping` 상태 설정 뒤 `ConnectionTypeBlocking`으로 `PipelineHandler::stop`을 호출하는 진입 시점과 호출에서 복귀하는 시점을 로그 `Stopping capture`와 함께 확인합니다. 복귀 후 `ASSERT(!d->pipe_->hasPendingRequests(this))`의 pending 요청 여부, `Private::CameraConfigured`로 설정되는 상태, 마지막 `return 0`을 기록하되 이는 실행한 테스트나 시간 측정이 아니며 상태 변경 함수를 다시 호출하지 않습니다. `src/libcamera/camera.cpp:1431`, `src/libcamera/camera.cpp:1462`

<!-- sdd:visual:stop-order -->
### 정지할 때 대기 요청을 처리하는 순서

정상 정지 경로의 순서를 표시합니다. 연결 해제 알림의 미완료 요청 TODO를 이 정지 보장과 혼동하지 마세요.

```mermaid
flowchart TB
%% sdd:translations {"Configured로 복귀": "Return to Configured", "stopDevice()": "stopDevice()", "대기 요청 취소·완료": "Cancel and complete waiting <br/>requests", "대기열을 별도로 분리": "Detach waiting queue", "분리 후 장치 정지": "Stop device after detaching", "장치 요청 뒤 대기 요청 취소": "Cancel waiting requests <br/>after device requests", "핸들러 정지 호출이 반환한 뒤": "After handler stop returns"}
  v_detach["대기열을 별도로 분리"]
  v_stop["stopDevice()"]
  v_cancel["대기 요청 취소·완료"]
  v_configured["Configured로 복귀"]
  v_detach -->|"분리 후 장치 정지"| v_stop
  v_stop -->|"장치 요청 뒤 대기 요청 취소"| v_cancel
  v_cancel -->|"핸들러 정지 호출이 반환한 뒤"| v_configured
```

[Mermaid 원문](request-lifecycle.stop-order.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | 대기열을 별도로 분리 | [src/libcamera/pipeline_handler.cpp:359](#source-eefd1bbecb1aad0a) |
    | stopDevice() | [src/libcamera/pipeline_handler.cpp:359](#source-eefd1bbecb1aad0a) |
    | 대기 요청 취소·완료 | [src/libcamera/pipeline_handler.cpp:359](#source-eefd1bbecb1aad0a) |
    | Configured로 복귀 | [src/libcamera/camera.cpp:1431](#source-e09324743def3f09) |
    | 분리 후 장치 정지 | [src/libcamera/pipeline_handler.cpp:359](#source-eefd1bbecb1aad0a) |
    | 장치 요청 뒤 대기 요청 취소 | [src/libcamera/pipeline_handler.cpp:359](#source-eefd1bbecb1aad0a) |
    | 핸들러 정지 호출이 반환한 뒤 | [src/libcamera/camera.cpp:1431](#source-e09324743def3f09) |
<!-- /sdd:visual:stop-order -->

이 내용은 실행 결과가 아닌 조사 계획입니다. `PipelineHandler::stop`에서 `data->waitingRequests_`를 로컬 큐와 `swap`으로 분리한 직후의 값을 기록하고, `stopDevice(camera)` 진입 시점과 복귀 시점을 함께 기록하면 장치 내부에서 멎은 경우와 반환한 경우를 구분할 수 있습니다. `src/libcamera/pipeline_handler.cpp:359`

이 발췌는 `PipelineHandler::stop()`의 대기 요청 취소 루프에서 `doQueueRequest`가 어떤 `request` 인자로 호출되는지 확인하기 위한 조사 계획입니다. 이 계획은 실행한 테스트나 시간 측정이 아니며, 정지 경로의 전체 함수를 나열하지 않습니다. 관찰 대상은 `waitingRequests` 지역 큐에서 꺼낸 `request` 변수, `request->_d()->cancel()` 호출 뒤 `doQueueRequest(request);`에 전달되는 값, 루프 종료 뒤 두 `ASSERT` 조건입니다. 상태를 바꾸는 `stop()`이나 `doQueueRequest()`를 다시 호출해서 관찰하지 않고, 발췌 코드에 있는 변수와 분기만 기록합니다. `src/libcamera/pipeline_handler.cpp:394`

이 항목은 실행 결과가 아닌 조사 계획입니다. `PipelineHandler::stop()` 끝의 두 `ASSERT(data->queuedRequests_.empty())`와 `ASSERT(data->waitingRequests_.empty())`가 검사하는 `queuedRequests_`와 `waitingRequests_`의 빈 상태를, 두 `ASSERT` 줄 직전 지점에서 변수 값으로 관찰할 수 있습니다. 두 검사 뒤에는 `data->requestSequence_ = 0;`이 실행되므로, 관찰 대상에 이 줄 이후의 `requestSequence_` 값을 포함할 수 있습니다. 관찰하려고 상태를 바꾸는 `stop()`을 다시 호출하지 않습니다. `src/libcamera/pipeline_handler.cpp:398`

파이프라인 핸들러는 `completeRequest()`를 `CameraManager` 스레드에서 호출해야 하며, 이 함수는 요청이 제출 순서대로 애플리케이션에 반환되도록 합니다. 함수가 반환된 뒤에는 핸들러가 해당 요청을 더 이상 관리하지 않으므로 그 요청에 접근해서는 안 됩니다. `src/libcamera/pipeline_handler.cpp:547`

실행 확인 항목: 아직 실행하지 않은 조사 계획으로, 애플리케이션 콜백의 진입·복귀 시점과 실행 스레드를 `completeRequest` 호출 문맥과 구분해 콜백 내부 로그로 기록하고, 상태를 바꾸는 함수는 다시 호출하지 않고 관측합니다. `completeRequest`는 `CameraManager thread`에서 호출해야 하는 파이프라인 핸들러의 의무이며, 콜백 실행 결과는 아직 검증 전이므로 이 계획만으로 콜백 스레드나 시점이 같다고 확인되지 않습니다. `src/libcamera/pipeline_handler.cpp:547`

`Camera::disconnect()`는 `_d()->disconnect()`를 먼저 호출하고, 그 호출이 끝난 뒤 `disconnected.emit()`을 실행합니다. 따라서 `_d()->disconnect()`의 처리는 `disconnected` 시그널 발생보다 앞선 순서로 실행됩니다. 제공된 소스에는 `_d()->disconnect()`의 본문이 없으므로, 이 내부 함수가 구체적으로 무엇을 처리하는지는 확인할 수 없습니다. `Camera::disconnect()` 함수 안의 `disconnected.emit();` 호출은 `disconnected` 신호를 발행합니다. `src/libcamera/camera.cpp:959`, `src/libcamera/camera.cpp:944`, `src/libcamera/camera.cpp:960`

`Camera::disconnect()` 함수의 설명 주석에 있는 `\todo` 항목은 카메라가 실행 중(running state)일 때 연결이 해제되는 경우, 아직 처리하지 않은 대기 요청(pending requests)을 어떻게 다룰지가 남아 있음을 표시합니다. `src/libcamera/camera.cpp:944`, `src/libcamera/camera.cpp:952`

근거 원문: [src/libcamera/camera.cpp:1431](#source-e09324743def3f09) · [src/libcamera/pipeline_handler.cpp:359](#source-eefd1bbecb1aad0a) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) · [src/libcamera/camera.cpp:1462](#source-6191f91df6cbffa2) · [src/libcamera/pipeline_handler.cpp:398](#source-5e7914238ff81605) · [src/libcamera/camera.cpp:952](#source-1d583253fc11ef1c) · [src/libcamera/pipeline_handler.cpp:394](#source-fd5daba4aa44adfd) · [src/libcamera/camera.cpp:959](#source-56494d0aedf70c2d) · [src/libcamera/camera.cpp:960](#source-7d48ce2e18c8877c) · [src/libcamera/camera.cpp:944](#source-2758e9ddd31ad41d) · [src/libcamera/camera.cpp:944](#source-839140c350119dd1)

## 변경 검토와 실행 확인

`Camera::queueRequest` 호출마다 반환값을 그대로 기록하고, 기록 항목에서 성공 0과 실패 음수 오류 코드를 구분하는 조사 계획을 제안합니다. `src/libcamera/camera.cpp:1308`

대입 대상은 `status_`이며, 기록 항목은 `Request::reuse(ReuseFlag flags)` 안의 `status_ = RequestPending;` 대입 전후에 `status_`, `controls_`, `metadata_` 값을 남기는 것입니다. `controls_.clear();`와 `_d()->metadata_.clear();`는 대입 뒤에 놓여 있어 두 값이 대입 이후 비워지는 지점을 표시합니다. 이 항목은 제안이며, 실행된 테스트나 측정 결과가 아닙니다. 원문에 이 기록을 의무로 정한 문장은 없습니다. `src/libcamera/request.cpp:400`, `src/libcamera/request.cpp:402`, `src/libcamera/request.cpp:403`

선두 요청의 상태 조회식은 코드 그대로 `req->status() == Request::RequestPending`입니다. 이 식은 `data->queuedRequests_.front()`로 얻은 `req`에 대해 `status()`를 호출하고 그 결과를 `Request::RequestPending`과 비교합니다. 따라서 기록 항목으로 이 식의 평가 결과와 대상 `req`를 함께 남기는 것을 제안합니다. 이 항목은 소스가 기록을 요구하는 것이 아니라 선택적 관찰 계획이며, 실제 테스트 결과나 측정값이 아닙니다. `src/libcamera/pipeline_handler.cpp:594`

근거 원문: [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/request.cpp:400](#source-a98823fa5ec440a2) · [src/libcamera/request.cpp:402](#source-c8638489aa83cfd1) · [src/libcamera/request.cpp:403](#source-47569737e131b31a) · [src/libcamera/pipeline_handler.cpp:594](#source-bae861ceef5e8406)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 제출 성공 이후의 대기 조건과 완료 책임은 무엇입니까? | [제출에서 완료까지](#제출에서-완료까지) | 코드 근거와 설명 연결 |
    | 어떤 자원을 누가 유지하고 완료 후 무엇을 초기화해야 합니까? | [요청·버퍼·fence의 수명](#요청버퍼fence의-수명) | 코드 근거와 설명 연결 |
    | 정지 중 요청 반환과 연결 해제의 보장 범위는 어떻게 다릅니까? | [정지와 연결 해제를 구분하기](#정지와-연결-해제를-구분하기) | 코드 근거와 설명 연결 · 실행 확인 항목 별도 |
    | 문서를 읽고 어떤 질문에 답하고 어떤 실행 증거를 확보해야 합니까? | [변경 검토와 실행 확인](#변경-검토와-실행-확인) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

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

<a id="source-789eafedfaa7f3c5"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:428"
    `src/libcamera/pipeline_handler.cpp:428`에서 시작하는 발췌입니다. 종료 줄은 547이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `5a7a3397a6034a73fe348ae44eb1e2568d2823e95542fe43386e16359d627180`
    
    ```text
    \fn PipelineHandler::registerRequest()
     * \brief Register a request for use by the pipeline handler
     * \param[in] request The request to register
     *
     * This function is called when the request is created, and allows the pipeline
     * handler to perform any one-time initialization it requries for the request.
     */
    void PipelineHandler::registerRequest(Request *request)
    {
    	/*
    	 * Connect the request prepared signal to notify the pipeline handler
    	 * when a request is ready to be processed.
    	 */
    	request->_d()->prepared.connect(this, [this, request]() {
    		doQueueRequests(request->_d()->camera());
    	});
    }
    
    /**
     * \fn PipelineHandler::queueRequest()
     * \brief Queue a request
     * \param[in] request The request to queue
     *
     * This function queues a capture request to the pipeline handler for
     * processing. The request is first added to the internal list of waiting
     * requests which have to be prepared to make sure they are ready for being
     * queued to the pipeline handler.
     *
     * The queue of waiting requests is iterated and up to \a
     * maxQueuedRequestsDevice_ prepared requests are passed to the pipeline handler
     * in the same order they have been queued by calling this function.
     *
     * If a Request fails during the preparation phase or if the pipeline handler
     * fails in queuing the request to the hardware the request is cancelled.
     *
     * Keeping track of queued requests ensures automatic completion of all requests
     * when the pipeline handler is stopped with stop(). Request completion shall be
     * signalled by the pipeline handler using the completeRequest() function.
     *
     * \context This function is called from the CameraManager thread.
     */
    void PipelineHandler::queueRequest(Request *request)
    {
    	LIBCAMERA_TRACEPOINT(request_queue, request);
    
    	Camera *camera = request->_d()->camera();
    	Camera::Private *data = camera->_d();
    	data->waitingRequests_.push(request);
    
    	request->_d()->prepare(300ms);
    }
    
    /**
     * \brief Queue one requests to the device
     */
    void PipelineHandler::doQueueRequest(Request *request)
    {
    	LIBCAMERA_TRACEPOINT(request_device_queue, request);
    
    	Camera *camera = request->_d()->camera();
    	Camera::Private *data = camera->_d();
    	data->queuedRequests_.push_back(request);
    
    	request->_d()->sequence_ = data->requestSequence_++;
    
    	if (request->_d()->cancelled_) {
    		completeRequest(request);
    		return;
    	}
    
    	int ret = queueRequestDevice(camera, request);
    	if (ret)
    		cancelRequest(request);
    }
    
    /**
     * \brief Queue prepared requests to the device
     *
     * Iterate the list of waiting requests and queue them to the device one
     * by one if they have been prepared.
     */
    void PipelineHandler::doQueueRequests(Camera *camera)
    {
    	Camera::Private *data = camera->_d();
    	while (!data->waitingRequests_.empty()) {
    		if (data->queuedRequests_.size() == maxQueuedRequestsDevice_)
    			break;
    
    		Request *request = data->waitingRequests_.front();
    		if (!request->_d()->prepared_)
    			break;
    
    		/*
    		 * Pop the request first, in case doQueueRequests() is called
    		 * recursively from within doQueueRequest()
    		 */
    		data->waitingRequests_.pop();
    		doQueueRequest(request);
    	}
    }
    
    /**
     * \fn PipelineHandler::queueRequestDevice()
     * \brief Queue a request to the device
     * \param[in] camera The camera to queue the request to
     * \param[in] request The request to queue
     *
     * This function queues a capture request to the device for processing. The
     * request contains a set of buffers associated with streams and a set of
     * parameters. The pipeline handler shall program the device to ensure that the
     * parameters will be applied to the frames captured in the buffers provided in
     * the request.
     *
     * \context This function is called from the CameraManager thread.
     *
     * \return 0 on success or a negative error code otherwise
     */
    
    /**
     * \brief Complete a buffer for a request
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

<a id="source-7348e9b4af985eb2"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:483"
    `src/libcamera/pipeline_handler.cpp:483`에서 시작하는 발췌입니다. 종료 줄은 501이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `fbd3ed6fe295b1cdd82d6ce420a30695986e43199347f92ac2545fe0e7831da8`
    
    ```text
    void PipelineHandler::doQueueRequest(Request *request)
    {
    	LIBCAMERA_TRACEPOINT(request_device_queue, request);
    
    	Camera *camera = request->_d()->camera();
    	Camera::Private *data = camera->_d();
    	data->queuedRequests_.push_back(request);
    
    	request->_d()->sequence_ = data->requestSequence_++;
    
    	if (request->_d()->cancelled_) {
    		completeRequest(request);
    		return;
    	}
    
    	int ret = queueRequestDevice(camera, request);
    	if (ret)
    		cancelRequest(request);
    }
    ```

<a id="source-c05f8214908fe4fe"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:530"
    `src/libcamera/pipeline_handler.cpp:530`에서 시작하는 발췌입니다. 종료 줄은 544이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `18f697dba5bc979e14125471abadb8a7ecccef4de79e75e1f385e2c6ee044df2`
    
    ```text
    \fn PipelineHandler::queueRequestDevice()
     * \brief Queue a request to the device
     * \param[in] camera The camera to queue the request to
     * \param[in] request The request to queue
     *
     * This function queues a capture request to the device for processing. The
     * request contains a set of buffers associated with streams and a set of
     * parameters. The pipeline handler shall program the device to ensure that the
     * parameters will be applied to the frames captured in the buffers provided in
     * the request.
     *
     * \context This function is called from the CameraManager thread.
     *
     * \return 0 on success or a negative error code otherwise
     */
    ```

<a id="source-ab8710f8a8a7905d"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:547"
    `src/libcamera/pipeline_handler.cpp:547`에서 시작하는 발췌입니다. 종료 줄은 563이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `096784b4798b3156e88e3acf84577f60a27f0bf0e2422ae7850e44b081eb9d3a`
    
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
    ```

<a id="source-236c920e906cb6fd"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:571"
    `src/libcamera/pipeline_handler.cpp:571`에서 시작하는 발췌입니다. 종료 줄은 607이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `6ad80c6800e8b980c2a6146d7dcc5648de9db2b0ca408711a896c4e46a624684`
    
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
    ```

<a id="source-a637b7daf9acb7ac"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:516"
    `src/libcamera/pipeline_handler.cpp:516`에서 시작하는 발췌입니다. 종료 줄은 518이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `f655f79ce0ac9e9361d1759b2974e6f382b7fe1e9e3aa35b51952572af8d5a6f`
    
    ```text
    Request *request = data->waitingRequests_.front();
    		if (!request->_d()->prepared_)
    			break;
    ```

<a id="source-5b0ae08604dff588"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:553"
    `src/libcamera/pipeline_handler.cpp:553`에서 시작하는 발췌입니다. 종료 줄은 556이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `957ec8f5090b25e8e97e61a6390c77c799eb5e696028a5674ca4717473b6d42d`
    
    ```text
    The request
     * is not completed automatically when the last buffer completes to give
     * pipeline handlers a chance to perform any operation that may still be
     * needed. They shall complete requests explicitly with completeRequest().
    ```

<a id="source-bae861ceef5e8406"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:594"
    `src/libcamera/pipeline_handler.cpp:594`에서 시작하는 발췌입니다. 종료 줄은 595이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `103a09a61422ec5ef5b879512b00b4194d428eb70ce8bbe292ded0be5382caf6`
    
    ```text
    if (req->status() == Request::RequestPending)
    			break;
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

<a id="source-86a8d784a8348122"></a>

??? note "소스 근거: src/libcamera/request.cpp:456"
    `src/libcamera/request.cpp:456`에서 시작하는 발췌입니다. 종료 줄은 460이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e7cc6e59b5401c6d2ef2bef1cceef1090d9bdd058ea8ce00a74bc573f5e4fdc2`
    
    ```text
    When a valid Fence is provided to this function, \a fence is moved to \a
     * buffer and this Request will only be queued to the device once the
     * fences of all its buffers have been correctly signalled. Ownership of the
     * fence will only be taken in case of success, otherwise the fence will
     * be left unmodified.
    ```

<a id="source-d8cf34a75a4333a7"></a>

??? note "소스 근거: src/libcamera/request.cpp:462"
    `src/libcamera/request.cpp:462`에서 시작하는 발췌입니다. 종료 줄은 465이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `ebb24de716cdebb7c0c82cfddf05e91d7d2fb938eda24fe5027d3e9efcf62104`
    
    ```text
    If the \a fence associated with \a buffer isn't signalled, the request will
     * fail after a timeout. The buffer will still contain the fence, which
     * applications must retrieve with FrameBuffer::releaseFence() before the buffer
     * can be reused in another request.
    ```

<a id="source-4cdce80c57526221"></a>

??? note "소스 근거: src/libcamera/request.cpp:447"
    `src/libcamera/request.cpp:447`에서 시작하는 발췌입니다. 종료 줄은 449이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `996424643a0de2ec5fbd8b8491639ae1afea030ab989179410e7a1eaa48c1673`
    
    ```text
    A reference to the buffer is stored in the request. The caller is responsible
     * for ensuring that the buffer will remain valid until the request complete
     * callback is called.
    ```

<a id="source-d93a02e9220fa760"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:575"
    `src/libcamera/pipeline_handler.cpp:575`에서 시작하는 발췌입니다. 종료 줄은 576이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `d2c64999e07c4a9df08f21b514cd8480e6ccc091f1aeef3ebaf44522d8fb0961`
    
    ```text
    The request is no longer managed by the pipeline
     * handler and shall not be accessed once this function returns.
    ```

<a id="source-52fb58c8956b1a91"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:610"
    `src/libcamera/pipeline_handler.cpp:610`에서 시작하는 발췌입니다. 종료 줄은 611이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `048bc649f307f0f41b7702b59be24a5fba9f7a48ff6a266bfbe458df4a5bdc8d`
    
    ```text
    This function cancels and completes the request. The same rules as for
     * completeRequest() apply.
    ```

<a id="source-d9944a69f2dd6758"></a>

??? note "소스 근거: src/libcamera/request.cpp:334"
    `src/libcamera/request.cpp:334`에서 시작하는 발췌입니다. 종료 줄은 334이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `7b740fbb97fdbfb9b7d270aa48ba5e7902f04d691349b58981ea011f324282d5`
    
    ```text
    This flag should not be used if fences are used.
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

<a id="source-eefd1bbecb1aad0a"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:359"
    `src/libcamera/pipeline_handler.cpp:359`에서 시작하는 발췌입니다. 종료 줄은 414이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `108b1bea5a8314ba57213d15c1e3ba01abe2b3f8a9e0e1e1281864b5492c7304`
    
    ```text
    \brief Stop capturing from all running streams and cancel pending requests
     * \param[in] camera The camera to stop
     *
     * This function stops capturing and processing requests immediately. All
     * pending requests are cancelled and complete immediately in an error state.
     *
     * \context This function is called from the CameraManager thread.
     */
    void PipelineHandler::stop(Camera *camera)
    {
    	/*
    	 * Take all waiting requests so that they are not requeued in response
    	 * to completeRequest() being called inside stopDevice(). Cancel them
    	 * after the device to keep them in order.
    	 */
    	Camera::Private *data = camera->_d();
    	std::queue<Request *> waitingRequests;
    	waitingRequests.swap(data->waitingRequests_);
    
    	/* Stop the pipeline handler and let the queued requests complete. */
    	stopDevice(camera);
    
    	/* Cancel and signal as complete all waiting requests. */
    	while (!waitingRequests.empty()) {
    		Request *request = waitingRequests.front();
    		waitingRequests.pop();
    
    		/*
    		 * Cancel all requests by marking them as cancelled and calling
    		 * doQueueRequest() instead of cancelRequest(). This ensures
    		 * that the requests get a sequence number and are temporarily
    		 * added to queuedRequests_ so they can be properly completed in
    		 * completeRequest().
    		 */
    		request->_d()->cancel();
    		doQueueRequest(request);
    	}
    
    	/* Make sure no requests are pending. */
    	ASSERT(data->queuedRequests_.empty());
    	ASSERT(data->waitingRequests_.empty());
    
    	data->requestSequence_ = 0;
    }
    
    /**
     * \fn PipelineHandler::stopDevice()
     * \brief Stop capturing from all running streams
     * \param[in] camera The camera to stop
     *
     * This function stops capturing and processing requests immediately. All
     * pending requests are cancelled and complete immediately in an error state.
     */
    
    /**
     * \brief Determine if the camera has any requests pending
    ```

<a id="source-6191f91df6cbffa2"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1462"
    `src/libcamera/camera.cpp:1462`에서 시작하는 발췌입니다. 종료 줄은 1465이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `a75876cfb66d256185fe7085444cbe91f726b87bdceca83cb6b243514f03c1ed`
    
    ```text
    d->setState(Private::CameraStopping);
    
    	d->pipe_->invokeMethod(&PipelineHandler::stop, ConnectionTypeBlocking,
    			       this);
    ```

<a id="source-5e7914238ff81605"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:398"
    `src/libcamera/pipeline_handler.cpp:398`에서 시작하는 발췌입니다. 종료 줄은 399이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `d21508cce62c51c0c63a2a50ba2c452548a69a2be9d425d526f42ee04c86c7a1`
    
    ```text
    ASSERT(data->queuedRequests_.empty());
    	ASSERT(data->waitingRequests_.empty());
    ```

<a id="source-1d583253fc11ef1c"></a>

??? note "소스 근거: src/libcamera/camera.cpp:952"
    `src/libcamera/camera.cpp:952`에서 시작하는 발췌입니다. 종료 줄은 953이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `94a54591940109c4ab230abf56ac78e1d5821e1db9e35016cb50505c40b34e55`
    
    ```text
    \todo Deal with pending requests if the camera is disconnected in a
     * running state.
    ```

<a id="source-fd5daba4aa44adfd"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:394"
    `src/libcamera/pipeline_handler.cpp:394`에서 시작하는 발췌입니다. 종료 줄은 394이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `b7a285b9db4abdc209d166d80bdc9e1ef6658f4908d2b05274beddc1592943e1`
    
    ```text
    doQueueRequest(request);
    ```

<a id="source-56494d0aedf70c2d"></a>

??? note "소스 근거: src/libcamera/camera.cpp:959"
    `src/libcamera/camera.cpp:959`에서 시작하는 발췌입니다. 종료 줄은 959이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e90a232265587ca40e1236c80aa01d9e22649c8379b6b580fcab5dcccc5728c1`
    
    ```text
    _d()->disconnect();
    ```

<a id="source-7d48ce2e18c8877c"></a>

??? note "소스 근거: src/libcamera/camera.cpp:960"
    `src/libcamera/camera.cpp:960`에서 시작하는 발췌입니다. 종료 줄은 960이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `b9f19485d322f3dc7639a06e2f78ddb25a293c4f361a7c44e01a9b4fe971f974`
    
    ```text
    disconnected.emit();
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

<a id="source-839140c350119dd1"></a>

??? note "소스 근거: src/libcamera/camera.cpp:944"
    `src/libcamera/camera.cpp:944`에서 시작하는 발췌입니다. 종료 줄은 955이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `768781b1763c3413e3780132c987fb0733d6fff2cdf1d128a6be5bbd1aa50d71`
    
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
    ```

<a id="source-a98823fa5ec440a2"></a>

??? note "소스 근거: src/libcamera/request.cpp:400"
    `src/libcamera/request.cpp:400`에서 시작하는 발췌입니다. 종료 줄은 400이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `aaf5bc87fb8a4ce9c7fbee2875c9cd6f20a8eb982ace6a531236dbd558cc8fc4`
    
    ```text
    status_ = RequestPending;
    ```

<a id="source-c8638489aa83cfd1"></a>

??? note "소스 근거: src/libcamera/request.cpp:402"
    `src/libcamera/request.cpp:402`에서 시작하는 발췌입니다. 종료 줄은 402이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e0203f8fd7483c79c6b1a03e35cf952e3839dce41ea145adaa678eceb1382491`
    
    ```text
    controls_.clear();
    ```

<a id="source-47569737e131b31a"></a>

??? note "소스 근거: src/libcamera/request.cpp:403"
    `src/libcamera/request.cpp:403`에서 시작하는 발췌입니다. 종료 줄은 403이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `794ec4bc82f6076eb388d21eab25bd1409e880c0160e00c1fee50d822c8fa82d`
    
    ```text
    _d()->metadata_.clear();
    ```

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `include/libcamera/camera.h`, `include/libcamera/internal/pipeline_handler.h`, `include/libcamera/request.h`, `src/libcamera/camera.cpp`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/request.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `212c689fcf`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-31 · 사람 검토 전

다음 단계: [구성과 요청 오류 조사](request-diagnosis.md)
