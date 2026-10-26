---
generated_at: 2026-10-26T14:23:28+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: request-lifecycle
generation_method: facts-and-llm
evidence_fingerprint: 26e9dd4d3890bf3acc2ea9e184ba4168a9e6352c49d050693e3b32c553c1de9d
semantic_review: human-review-required
agent: ollama/qwen3.5:9b
generated_design: {"schema": 1, "input_fingerprint": "26e9dd4d3890bf3acc2ea9e184ba4168a9e6352c49d050693e3b32c553c1de9d", "answers": {"configuration-failure": [{"text": "`Camera::configure` 함수 내부에서 `d->isAccessAllowed(Private::CameraAcquired, Private::CameraConfigured)` 호출의 반환값을 변수 `ret`에 저장한 뒤, 이 값이 음수인지 확인하여 실패 시 즉시 반환하는 로직을 관찰해야 합니다.", "evidence": ["configure-access"], "covers": ["configuration-failure"], "kind": "behavior", "quote": "int ret = d->isAccessAllowed(Private::CameraAcquired,\n\t\t\t\t     Private::CameraConfigured);\n\tif (ret < 0)\n\t\treturn ret;", "part_id": "entry"}, {"text": "`isAccessAllowed` 함수는 `allowDisconnected` 가 거짓이고 `disconnected_` 가 참인 경우에만 `-ENODEV` 를 반환합니다.", "evidence": ["access"], "covers": ["configuration-failure"], "kind": "behavior", "quote": "int Camera::Private::isAccessAllowed(State low, State high,\n\t\t\t\t     bool allowDisconnected,\n\t\t\t\t     const char *from) const\n{\n\tif (!allowDisconnected && disconnected_)\n\t\treturn -ENODEV;", "part_id": "access"}, {"text": "`isAccessAllowed` 함수는 현재 카메라 상태를 `currentState`로 로드한 후, 요청된 상태 범위인 `low`와 `high`가 `currentState`를 포함하는지 확인합니다. 이 과정에서 `currentState >= low && currentState <= high` 조건이 참이면 접근을 허용하고 거짓이면 `-EACCES` 오류를 반환하며, 로그에 현재 상태와 요구되는 상태 범위를 기록합니다.", "evidence": ["state-range"], "covers": ["configuration-failure"], "kind": "behavior", "quote": "State currentState = state_.load(std::memory_order_acquire);\n\tif (currentState >= low && currentState <= high)\n\t\treturn 0;\n\n\tASSERT(static_cast<unsigned int>(low) < std::size(camera_state_names) &&\n\t       static_cast<unsigned int>(high) < std::size(camera_state_names));\n\n\tLOG(Camera, Error) << \"Camera in \" << camera_state_names[currentState]\n\t\t\t   << \" state trying \" << from\n\t\t\t   << \"() requiring state between \"\n\t\t\t   << camera_state_names[low] << \" and \"\n\t\t\t   << camera_state_names[high];\n\n\treturn -EACCES;", "part_id": "access-state"}, {"text": "`CameraConfiguration::validate()` 함수가 `CameraConfiguration::Adjusted` 상태를 반환하면, 해당 스트림의 파라미터 값이 변경되었을 수도 있고, 스트림 구성 자체가 제거되었을 수 있습니다.", "evidence": ["validation-changes"], "covers": ["configuration-failure"], "kind": "behavior", "quote": "Parameters may have changed for any stream, and stream\n * configurations may have been removed.", "part_id": "validation-effects"}, {"text": "`CameraConfiguration::Adjusted`를 반환하는 호출자는 반드시 해당 구성을 신중하게 확인해야 합니다.", "evidence": ["validation-caller"], "covers": ["configuration-failure"], "kind": "behavior", "quote": "The caller shall check the\n * configuration carefully.", "part_id": "validation-caller"}, {"text": "`Camera::configure` 함수 내부에서 `config->validate()` 호출의 반환값이 `CameraConfiguration::Valid`와 일치하지 않을 경우, 해당 비교 대상 상태 이름은 코드 흐름상 `-EINVAL` 오류 코드가 반환되기 직전의 조건 분기에서 관찰됩니다.", "evidence": ["validation-check"], "covers": ["configuration-failure"], "kind": "behavior", "quote": "if (config->validate() != CameraConfiguration::Valid) {\n\t\tLOG(Camera, Error)\n\t\t\t<< \"Can't configure camera with invalid configuration\";\n\t\treturn -EINVAL;", "part_id": "validation-result"}, {"text": "`Camera::configure` 함수가 `config->validate()` 호출 결과가 유효하지 않은 값일 때, 즉 비교 조건이 참이면 해당 함수는 오류 로그를 출력한 뒤 `-EINVAL` 코드를 반환합니다.", "evidence": ["validation-check"], "covers": ["configuration-failure"], "kind": "behavior", "quote": "if (config->validate() != CameraConfiguration::Valid) {\n\t\tLOG(Camera, Error)\n\t\t\t<< \"Can't configure camera with invalid configuration\";\n\t\treturn -EINVAL;", "part_id": "validation-error"}, {"text": "`Camera::configure` 함수는 상태 검증이 통과한 뒤 `d->pipe_->invokeMethod(&PipelineHandler::configure, ...)` 호출의 반환값을 확인하여 실패 위치를 파악해야 합니다.", "evidence": ["configure-code"], "covers": ["configuration-failure"], "kind": "behavior", "quote": "ret = d->pipe_->invokeMethod(&PipelineHandler::configure,\n\t\t\t\t     ConnectionTypeBlocking, this, config);\n\tif (ret)\n\t\treturn ret;", "part_id": "device-configure"}, {"text": "`Camera::configure` 함수 내부에서 `cfg.stream()` 호출 결과를 확인하고, 만약 스트림 포인터가 null 이라면 파이프라인 핸들러가 스트림 구성을 업데이트하는 데 실패했다는_fatal 로그를 출력하며 `-EINVAL` 오류 코드를 반환합니다.", "evidence": ["stream-check"], "covers": ["configuration-failure"], "kind": "behavior", "quote": "Stream *stream = cfg.stream();\n\t\tif (!stream) {\n\t\t\tLOG(Camera, Fatal)\n\t\t\t\t<< \"Pipeline handler failed to update stream configuration\";\n\t\t\td->activeStreams_.clear();\n\t\t\treturn -EINVAL;", "part_id": "stream-link"}], "journey": [{"text": "`Camera::createRequest()` 함수는 애플리케이션이 버퍼와 매개변수로 채우고 캡처를 대기하도록 할 빈 요청을 생성하며, 생성된 요청의 소유권은 호출자에게 전달되어 호출자가 이를 삭제할 책임이 있습니다.", "evidence": ["create"], "covers": ["journey"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest(uint64_t cookie)", "part_id": "create"}, {"text": "버퍼를 요청의 특정 스트림에 연결하는 API는 `Request::addBuffer()` 함수이며, 이 함수는 `Stream` 포인터와 `FrameBuffer` 포인터를 인자로 받아 버퍼를 요청에 추가합니다.", "evidence": ["buffer"], "covers": ["journey"], "kind": "behavior", "quote": "\\brief Add a FrameBuffer with its associated Stream to the Request\n * \\param[in] stream The stream the buffer belongs to\n * \\param[in] buffer The FrameBuffer to add to the request\n * \\param[in] fence The optional fence\n *\n * A reference to the buffer is stored in the request. The caller is responsible\n * for ensuring that the buffer will remain valid until the request complete\n * callback is called.\n *\n * A request can only contain one buffer per stream. If a buffer has already\n * been added to the request for the same stream, this function returns -EEXIST.\n *\n * A Fence can be optionally associated with the \\a buffer.\n *\n * When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.\n *\n * If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request. Attempting to add a buffer that still\n * contains a fence to a request will result in this function returning -EEXIST.\n *\n * \\sa FrameBuffer::releaseFence()\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -EEXIST The request already contains a buffer for the stream\n *  or the buffer still references a fence\n * \\retval -EINVAL The buffer does not reference a valid Stream\n */\nint Request::addBuffer(const Stream *stream, FrameBuffer *buffer,", "part_id": "buffer"}, {"text": "`Camera::queueRequest` 함수는 성공 시 0 을 반환하며, 요청이 큐에 등록된 후 카메라는 requestCompleted 신호를 통해 완료 통지를 합니다.", "evidence": ["queue"], "covers": ["journey"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();\n\n\tint ret = d->isAccessAllowed(Private::CameraRunning);\n\tif (ret < 0)\n\t\treturn ret;\n\n\t/* Requests can only be queued to the camera that created them. */\n\tif (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;\n\t}\n\n\tif (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}\n\n\t/* Make sure the Request has a valid control list. */\n\tif (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * The camera state may change until the end of the function. No locking\n\t * is however needed as PipelineHandler::queueRequest() will handle\n\t * this.\n\t */\n\n\tif (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}\n\n\t/* Pre-process AeEnable. */\n\tpatchControlList(request->controls());\n\n\td->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;\n}\n\n/**\n * \\brief Start capture from camera", "part_id": "submission"}, {"text": "대기 큐와 장치 큐 한도로 요청 전달을 제한하는 두 변수는 각각 data->`waitingRequests_` 와 `maxQueuedRequestsDevice_` 입니다.", "evidence": ["device-queue"], "covers": ["journey"], "kind": "behavior", "quote": "\\fn PipelineHandler::registerRequest()\n * \\brief Register a request for use by the pipeline handler\n * \\param[in] request The request to register\n *\n * This function is called when the request is created, and allows the pipeline\n * handler to perform any one-time initialization it requries for the request.\n */\nvoid PipelineHandler::registerRequest(Request *request)\n{\n\t/*\n\t * Connect the request prepared signal to notify the pipeline handler\n\t * when a request is ready to be processed.\n\t */\n\trequest->_d()->prepared.connect(this, [this, request]() {\n\t\tdoQueueRequests(request->_d()->camera());\n\t});\n}\n\n/**\n * \\fn PipelineHandler::queueRequest()\n * \\brief Queue a request\n * \\param[in] request The request to queue\n *\n * This function queues a capture request to the pipeline handler for\n * processing. The request is first added to the internal list of waiting\n * requests which have to be prepared to make sure they are ready for being\n * queued to the pipeline handler.\n *\n * The queue of waiting requests is iterated and up to \\a\n * maxQueuedRequestsDevice_ prepared requests are passed to the pipeline handler\n * in the same order they have been queued by calling this function.\n *\n * If a Request fails during the preparation phase or if the pipeline handler\n * fails in queuing the request to the hardware the request is cancelled.\n *\n * Keeping track of queued requests ensures automatic completion of all requests\n * when the pipeline handler is stopped with stop(). Request completion shall be\n * signalled by the pipeline handler using the completeRequest() function.\n *\n * \\context This function is called from the CameraManager thread.\n */\nvoid PipelineHandler::queueRequest(Request *request)\n{\n\tLIBCAMERA_TRACEPOINT(request_queue, request);\n\n\tCamera *camera = request->_d()->camera();\n\tCamera::Private *data = camera->_d();\n\tdata->waitingRequests_.push(request);\n\n\trequest->_d()->prepare(300ms);\n}\n\n/**\n * \\brief Queue one requests to the device\n */\nvoid PipelineHandler::doQueueRequest(Request *request)\n{\n\tLIBCAMERA_TRACEPOINT(request_device_queue, request);\n\n\tCamera *camera = request->_d()->camera();\n\tCamera::Private *data = camera->_d();\n\tdata->queuedRequests_.push_back(request);\n\n\trequest->_d()->sequence_ = data->requestSequence_++;\n\n\tif (request->_d()->cancelled_) {\n\t\tcompleteRequest(request);\n\t\treturn;\n\t}\n\n\tint ret = queueRequestDevice(camera, request);\n\tif (ret)\n\t\tcancelRequest(request);\n}\n\n/**\n * \\brief Queue prepared requests to the device\n *\n * Iterate the list of waiting requests and queue them to the device one\n * by one if they have been prepared.\n */\nvoid PipelineHandler::doQueueRequests(Camera *camera)\n{\n\tCamera::Private *data = camera->_d();\n\twhile (!data->waitingRequests_.empty()) {\n\t\tif (data->queuedRequests_.size() == maxQueuedRequestsDevice_)\n\t\t\tbreak;\n\n\t\tRequest *request = data->waitingRequests_.front();\n\t\tif (!request->_d()->prepared_)\n\t\t\tbreak;\n\n\t\t/*\n\t\t * Pop the request first, in case doQueueRequests() is called\n\t\t * recursively from within doQueueRequest()\n\t\t */\n\t\tdata->waitingRequests_.pop();\n\t\tdoQueueRequest(request);\n\t}\n}\n\n/**\n * \\fn PipelineHandler::queueRequestDevice()\n * \\brief Queue a request to the device\n * \\param[in] camera The camera to queue the request to\n * \\param[in] request The request to queue\n *\n * This function queues a capture request to the device for processing. The\n * request contains a set of buffers associated with streams and a set of\n * parameters. The pipeline handler shall program the device to ensure that the\n * parameters will be applied to the frames captured in the buffers provided in\n * the request.\n *\n * \\context This function is called from the CameraManager thread.\n *\n * \\return 0 on success or a negative error code otherwise\n */\n\n/**\n * \\brief Complete a buffer for a request", "part_id": "waiting"}, {"text": "코드에서 선두 요청이 준비되었는지 확인하는 멤버는 `prepared_` 입니다.", "evidence": ["waiting-prepared"], "covers": ["journey"], "kind": "behavior", "quote": "Request *request = data->waitingRequests_.front();\n\t\tif (!request->_d()->prepared_)\n\t\t\tbreak;", "part_id": "waiting-prepared"}, {"text": "void `PipelineHandler::doQueueRequest` 함수는 요청을 큐에 추가한 후, 해당 요청이 취소되었는지(`cancelled_`)를 확인하여 분기합니다. 만약 요청이 취소된 경우라면 completeRequest 를 호출하고 함수를 종료하며, 취소되지 않은 경우 queueRequestDevice 를 호출한 뒤 그 반환값(ret)이 0 이 아닌 경우 cancelRequest 를 호출합니다.", "evidence": ["dispatch"], "covers": ["journey"], "kind": "behavior", "quote": "void PipelineHandler::doQueueRequest(Request *request)\n{\n\tLIBCAMERA_TRACEPOINT(request_device_queue, request);\n\n\tCamera *camera = request->_d()->camera();\n\tCamera::Private *data = camera->_d();\n\tdata->queuedRequests_.push_back(request);\n\n\trequest->_d()->sequence_ = data->requestSequence_++;\n\n\tif (request->_d()->cancelled_) {\n\t\tcompleteRequest(request);\n\t\treturn;\n\t}\n\n\tint ret = queueRequestDevice(camera, request);\n\tif (ret)\n\t\tcancelRequest(request);\n}", "part_id": "dispatch"}, {"text": "함수의 이름은 `PipelineHandler::queueRequestDevice()`이며, 성공 시 0 을 반환합니다.", "evidence": ["device-contract"], "covers": ["journey"], "kind": "behavior", "quote": "\\fn PipelineHandler::queueRequestDevice()\n * \\brief Queue a request to the device\n * \\param[in] camera The camera to queue the request to\n * \\param[in] request The request to queue\n *\n * This function queues a capture request to the device for processing. The\n * request contains a set of buffers associated with streams and a set of\n * parameters. The pipeline handler shall program the device to ensure that the\n * parameters will be applied to the frames captured in the buffers provided in\n * the request.\n *\n * \\context This function is called from the CameraManager thread.\n *\n * \\return 0 on success or a negative error code otherwise\n */", "part_id": "device-result"}, {"text": "이 함수는 성공 시 0 을 반환하며, 오류가 발생하면 음수인 오류 코드를 반환합니다.", "evidence": ["device-contract"], "covers": ["journey"], "kind": "behavior", "quote": "\\fn PipelineHandler::queueRequestDevice()\n * \\brief Queue a request to the device\n * \\param[in] camera The camera to queue the request to\n * \\param[in] request The request to queue\n *\n * This function queues a capture request to the device for processing. The\n * request contains a set of buffers associated with streams and a set of\n * parameters. The pipeline handler shall program the device to ensure that the\n * parameters will be applied to the frames captured in the buffers provided in\n * the request.\n *\n * \\context This function is called from the CameraManager thread.\n *\n * \\return 0 on success or a negative error code otherwise\n */", "part_id": "device-error"}, {"text": "버퍼 완료를 알릴 때 파이프라인 핸들러는 completeBuffer() 함수를 호출해야 하며, 이 함수는 요청의 버퍼 부분 완료를 신호로 보내고 애플리케이션에 완료를 통보하며 요청의 내부 버퍼 추적을 업데이트해야 합니다.", "evidence": ["buffer-notice"], "covers": ["journey"], "kind": "behavior", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)", "part_id": "buffer-complete"}, {"text": "마지막 버퍼가 완료된 후에도 요청이 자동으로 완료되지 않으며, 파이프라인 핸들러가 여전히 수행해야 할 작업을 위해 명시적으로 completeRequest() 함수를 호출하여 요청을 완료해야 합니다.", "evidence": ["request-duty"], "covers": ["journey"], "kind": "behavior", "quote": "The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().", "part_id": "request-duty"}, {"text": "`PipelineHandler::completeRequest` 함수는 요청이 완료되었을 때 애플리케이션에 요청을 제출 순서(submission order)로 반환하도록 보장합니다.", "evidence": ["request-notice"], "covers": ["journey"], "kind": "behavior", "quote": "\\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}\n\n/**\n * \\brief Cancel request and signal its completion", "part_id": "request-complete"}, {"text": "이 분기는 요청의 상태가 `Request::RequestPending` 인지를 판단합니다.", "evidence": ["completed-head"], "covers": ["journey"], "kind": "behavior", "quote": "if (req->status() == Request::RequestPending)\n\t\t\tbreak;", "part_id": "request-head"}], "resources": [{"text": "`Camera::createRequest` 함수는 새로 생성된 요청 객체의 소유권을 호출자에게 넘깁니다.", "evidence": ["create"], "covers": ["resources"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest(uint64_t cookie)", "part_id": "request-owner"}, {"text": "`Request::addBuffer` 함수를 호출한 호출자는 요청의 완료 콜백이 호출될 때까지 버퍼가 유효하게 유지되도록 해야 합니다.", "evidence": ["buffer-duty"], "covers": ["resources"], "kind": "behavior", "quote": "A reference to the buffer is stored in the request. The caller is responsible\n * for ensuring that the buffer will remain valid until the request complete\n * callback is called.", "part_id": "buffer-validity"}, {"text": "`addBuffer` 함수가 성공적으로 호출되고 유효한 펜스가 제공되면, 그 펜스의 소유권이 `buffer` 객체로 이동합니다.", "evidence": ["fence-move"], "covers": ["resources"], "kind": "behavior", "quote": "When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.", "part_id": "fence-transfer"}, {"text": "`addBuffer` 함수가 실패할 경우, 전달받은 `fence` 는 수정되지 않고 원래 상태로 유지됩니다.", "evidence": ["fence-move"], "covers": ["resources"], "kind": "behavior", "quote": "When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.", "part_id": "fence-failure"}, {"text": "요청 (`Request`) 이 프레임 버퍼에 연결된 펜스 신호를 받지 못하면 요청은 지정된 시간 이후 타임아웃으로 실패합니다.", "evidence": ["fence-expiry"], "covers": ["resources"], "kind": "behavior", "quote": "If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request.", "part_id": "fence-timeout"}, {"text": "타임아웃으로 인해 요청이 실패한 후 버퍼를 재사용하려면 호출자는 `FrameBuffer::releaseFence()` 함수를 반드시 호출해야 합니다.", "evidence": ["fence-expiry"], "covers": ["resources"], "kind": "behavior", "quote": "If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request.", "part_id": "release-fence"}, {"text": "`Request::reuse` 함수의 실행 흐름에서 `ReuseBuffers` 분기 조건이 충족되면 내부적으로 `buffer->_d()->setRequest(this)` 호출이 수행되어 기존 버퍼를 현재 요청에 연결합니다.", "evidence": ["reuse-link-call"], "covers": ["resources"], "kind": "behavior", "quote": "buffer->_d()->setRequest(this);", "part_id": "reset-buffer-link"}, {"text": "`Request::reuse` 함수에서 `ReuseBuffers` 플래그가 설정된 경우, 버퍼 맵에 있는 모든 버퍼를 순회하며 각 버퍼의 `_d()` 를 통해 `setRequest(this)` 호출로 현재 요청과 연동하고, 그 다음 `_d()->pending_` 집합에 해당 버퍼를 추가합니다.", "evidence": ["reuse-buffers"], "covers": ["resources"], "kind": "behavior", "quote": "if (flags & ReuseBuffers) {\n\t\tfor (const auto &[stream, buffer] : bufferMap_) {\n\t\t\tbuffer->_d()->setRequest(this);\n\t\t\t_d()->pending_.insert(buffer);\n\t\t}\n\t} else {\n\t\tbufferMap_.clear();\n\t}\n\n\tstatus_ = RequestPending;", "part_id": "reset-pending"}, {"text": "`Request::reuse()` 함수의 `ReuseBuffers` 플래그가 없는 else 분기에서는 `bufferMap_`를 비웁니다.", "evidence": ["reuse-buffers"], "covers": ["resources"], "kind": "behavior", "quote": "if (flags & ReuseBuffers) {\n\t\tfor (const auto &[stream, buffer] : bufferMap_) {\n\t\t\tbuffer->_d()->setRequest(this);\n\t\t\t_d()->pending_.insert(buffer);\n\t\t}\n\t} else {\n\t\tbufferMap_.clear();\n\t}\n\n\tstatus_ = RequestPending;", "part_id": "reset-buffer-clear"}, {"text": "`Request::reuse` 함수 내부에서 `status_` 변수에 `RequestPending` 값을 대입하는 것은 요청이 재사용 준비 상태로 설정됨을 나타냅니다.", "evidence": ["reuse-status"], "covers": ["resources"], "kind": "behavior", "quote": "status_ = RequestPending;", "part_id": "reset"}, {"text": "`Request::reuse` 함수 내부에서 `controls_` 멤버 변수에 대한 호출은 해당 벡터를 비우는 초기화 작업만 수행합니다.", "evidence": ["reuse-controls"], "covers": ["resources"], "kind": "behavior", "quote": "controls_.clear();", "part_id": "reset-controls"}, {"text": "`Request::reuse` 함수 내부에서 `_d()->metadata_.clear()` 호출은 `metadata_` 멤버 변수에 저장된 모든 메타데이터 항목을 제거하여 초기화 상태를 만듭니다.", "evidence": ["reuse-metadata"], "covers": ["resources"], "kind": "behavior", "quote": "_d()->metadata_.clear();", "part_id": "reset-metadata"}, {"text": "`Request::ReuseBuffers` 플래그는 `addBuffer()` 함수를 통해 이전에 추가된 버퍼들을 재사용하도록 요청합니다.", "evidence": ["reuse-flags"], "covers": ["resources"], "kind": "behavior", "quote": "\\enum Request::ReuseFlag\n * Flags to control the behavior of Request::reuse()\n * \\var Request::Default\n * Don't reuse buffers\n * \\var Request::ReuseBuffers\n * Reuse the buffers that were previously added by addBuffer()\n *\n * \\note Fences associated with the buffers are not reused.\n *  This flag should not be used if fences are used.\n */", "part_id": "reuse-fences"}, {"text": "`Request::ReuseBuffers` 플래그를 사용하면 `addBuffer()` 로 추가된 버퍼만 재사용되지만, 해당 버퍼에 연결된 펜스 (`Fence`) 는 재사용되지 않습니다.", "evidence": ["reuse-flags"], "covers": ["resources"], "kind": "behavior", "quote": "\\enum Request::ReuseFlag\n * Flags to control the behavior of Request::reuse()\n * \\var Request::Default\n * Don't reuse buffers\n * \\var Request::ReuseBuffers\n * Reuse the buffers that were previously added by addBuffer()\n *\n * \\note Fences associated with the buffers are not reused.\n *  This flag should not be used if fences are used.\n */", "part_id": "fence-reuse-caution"}, {"text": "`Request::ReuseFlag` 플래그는 펜스 (fence) 가 사용될 경우 사용하지 않는 것이 좋습니다.", "evidence": ["reuse-advice"], "covers": ["resources"], "kind": "behavior", "quote": "This flag should not be used if fences are used.", "part_id": "reuse-advice"}, {"text": "`PipelineHandler::completeRequest()` 함수가 반환하면 해당 요청은 더 이상 파이프라인 핸들러에 의해 관리되지 않으며, 이 함수가 돌아온 이후에는 해당 요청을 접근해서는 안 됩니다.", "evidence": ["completion"], "covers": ["resources"], "kind": "behavior", "quote": "/**\n * \\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();", "part_id": "handler-access"}, {"text": "`cancelRequest` 함수가 반환되면 해당 요청은 파이프라인 핸들러에 의해 더 이상 관리되지 않으며, 이 함수가 돌아온 이후에는 요청을 접근해서는 안 됩니다.", "evidence": ["cancel-rules"], "covers": ["resources"], "kind": "behavior", "quote": "This function cancels and completes the request. The same rules as for\n * completeRequest() apply.", "part_id": "cancel-access"}], "diagnosis": [{"text": "`Camera::queueRequest` 함수는 요청을 카메라에 대기열로 등록할 때 반환하는 값을 확인해야 합니다. 이 함수는 호출 성공 시 0 을 반환하고, 실패 시 음수 오류 코드를 반환합니다.", "evidence": ["queue"], "covers": ["diagnosis"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();", "part_id": "submission"}, {"text": "`Request::addBuffer` 함수를 호출할 때 `-EEXIST` 오류 코드가 반환되면, 이는 요청에 이미 해당 스트림의 버퍼가 추가되었거나 버퍼에 아직 해제되지 않은 펜스가 남아있기 때문입니다.", "evidence": ["buffer"], "covers": ["diagnosis"], "kind": "behavior", "quote": "\\brief Add a FrameBuffer with its associated Stream to the Request\n * \\param[in] stream The stream the buffer belongs to\n * \\param[in] buffer The FrameBuffer to add to the request\n * \\param[in] fence The optional fence\n *\n * A reference to the buffer is stored in the request. The caller is responsible\n * for ensuring that the buffer will remain valid until the request complete\n * callback is called.\n *\n * A request can only contain one buffer per stream. If a buffer has already\n * been added to the request for the same stream, this function returns -EEXIST.\n *\n * A Fence can be optionally associated with the \\a buffer.\n *\n * When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.\n *\n * If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request. Attempting to add a buffer that still\n * contains a fence to a request will result in this function returning -EEXIST.\n *\n * \\sa FrameBuffer::releaseFence()\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -EEXIST The request already contains a buffer for the stream\n *  or the buffer still references a fence\n * \\retval -EINVAL The buffer does not reference a valid Stream\n */\nint Request::addBuffer(const Stream *stream, FrameBuffer *buffer,", "part_id": "buffer-error"}, {"text": "`doQueueRequests` 함수는 `waitingRequests_` 대기열에서 요청을 꺼내 처리하기 전에, 현재 제출된 요청 수인 `queuedRequests_.size()`가 한도 값인 `maxQueuedRequestsDevice_`와 같으면 순회를 멈춥니다.", "evidence": ["device-queue"], "covers": ["diagnosis"], "kind": "behavior", "quote": "/**\n * \\brief Queue prepared requests to the device\n *\n * Iterate the list of waiting requests and queue them to the device one\n * by one if they have been prepared.\n */\nvoid PipelineHandler::doQueueRequests(Camera *camera)\n{\n\tCamera::Private *data = camera->_d();\n\twhile (!data->waitingRequests_.empty()) {\n\t\tif (data->queuedRequests_.size() == maxQueuedRequestsDevice_)\n\t\t\tbreak;", "part_id": "capacity"}, {"text": "`PipelineHandler::doQueueRequests` 함수 내부에서 `data->waitingRequests_.front()`로 선두 요청을 가져온 후, 바로 `_d()` 메서드를 호출하여 접근한 뒤 그 결과의 `prepared_` 멤버 변수 값을 확인하는 위치가 관찰 대상입니다.", "evidence": ["prepared-branch"], "covers": ["diagnosis"], "kind": "behavior", "quote": "Request *request = data->waitingRequests_.front();\n\t\tif (!request->_d()->prepared_)\n\t\t\tbreak;", "part_id": "preparation"}, {"text": "`PipelineHandler::doQueueRequests` 함수가 `data->waitingRequests_`의 첫 번째 요청을 가져온 후, 해당 요청의 `_d()`를 통해 접근한 `prepared_` 멤버 변수가 거짓이면 루프를 중단합니다.", "evidence": ["prepared-branch"], "covers": ["diagnosis"], "kind": "behavior", "quote": "Request *request = data->waitingRequests_.front();\n\t\tif (!request->_d()->prepared_)\n\t\t\tbreak;", "part_id": "preparation-break"}, {"text": "`PipelineHandler::doQueueRequest` 함수 내부에서 요청의 취소 상태를 확인하는 위치는 `request->_d()->cancelled_` 조건문입니다. 이 식이 참이면 요청을 즉시 완료하고 함수를 종료합니다.", "evidence": ["cancelled-branch"], "covers": ["diagnosis"], "kind": "behavior", "quote": "if (request->_d()->cancelled_) {\n\t\tcompleteRequest(request);\n\t\treturn;", "part_id": "cancelled"}, {"text": "`PipelineHandler::doQueueRequest` 함수 내부에서 `request->_d()->cancelled_` 조건이 참일 경우, 해당 요청을 즉시 완료 처리하기 위해 `completeRequest(request)` 함수를 호출합니다.", "evidence": ["cancelled-branch"], "covers": ["diagnosis"], "kind": "behavior", "quote": "if (request->_d()->cancelled_) {\n\t\tcompleteRequest(request);\n\t\treturn;", "part_id": "cancelled-completion"}, {"text": "`PipelineHandler::doQueueRequest` 함수 내에서 `queueRequestDevice` 호출 직후의 반환값을 관찰할 수 있습니다.", "evidence": ["device-result-branch"], "covers": ["diagnosis"], "kind": "behavior", "quote": "int ret = queueRequestDevice(camera, request);\n\tif (ret)\n\t\tcancelRequest(request);", "part_id": "device-result"}, {"text": "`PipelineHandler::doQueueRequest` 함수 내에서 `queueRequestDevice` 가 오류를 반환하면 바로 다음 줄에서 `cancelRequest` 함수가 호출됩니다.", "evidence": ["device-result-branch"], "covers": ["diagnosis"], "kind": "behavior", "quote": "int ret = queueRequestDevice(camera, request);\n\tif (ret)\n\t\tcancelRequest(request);", "part_id": "device-cancel"}, {"text": "`PipelineHandler::completeBuffer` 함수는 요청의 내부 버퍼 추적을 업데이트하고 애플리케이션에 완료를 알립니다. 이 함수가 호출되면 마지막 버퍼가 완료되었더라도 요청이 자동으로 완료되지 않으며, 파이프라인 핸들러가 추가 작업을 수행할 기회를 주기 위해 명시적으로 `completeRequest()` 를 호출해야 합니다.", "evidence": ["completion"], "covers": ["diagnosis"], "kind": "behavior", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}", "part_id": "buffer-completion"}, {"text": "`PipelineHandler::completeRequest` 함수 내부에서 `data->queuedRequests_`의 선두 요청이 `RequestPending` 상태인지 확인하는 분기가 존재하며, 이 조건이 참일 경우 루프를 중단합니다.", "evidence": ["completion"], "covers": ["diagnosis"], "kind": "behavior", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;", "part_id": "pending-head"}], "stopping": [{"text": "`Camera::stop` 함수를 호출할 때 카메라가 실행 중이 아닌 상태라면, `_d()->isRunning()` 조건에서 `false`로 판정되어 즉시 0 을 반환합니다.", "evidence": ["stop"], "covers": ["stopping"], "kind": "behavior", "quote": "/*\n\t * \\todo Make calling stop() when not in 'Running' part of the state\n\t * machine rather than take this shortcut\n\t */\n\tif (!d->isRunning())\n\t\treturn 0;", "part_id": "camera-entry"}, {"text": "`Camera::stop()` 함수가 실행될 때 내부적으로 `d->setState(Private::CameraStopping)` 호출을 통해 카메라 상태를 `Private::CameraStopping`으로 변경합니다.", "evidence": ["stopping-call"], "covers": ["stopping"], "kind": "behavior", "quote": "d->setState(Private::CameraStopping);\n\n\td->pipe_->invokeMethod(&PipelineHandler::stop, ConnectionTypeBlocking,\n\t\t\t       this);", "part_id": "blocking"}, {"text": "`Camera::stop()` 함수는 `d->pipe_->invokeMethod(&PipelineHandler::stop, ConnectionTypeBlocking, this)`를 호출하여 `PipelineHandler::stop`에 대한 메서드 호출을 시작합니다.", "evidence": ["stopping-call"], "covers": ["stopping"], "kind": "behavior", "quote": "d->setState(Private::CameraStopping);\n\n\td->pipe_->invokeMethod(&PipelineHandler::stop, ConnectionTypeBlocking,\n\t\t\t       this);", "part_id": "blocking-call"}, {"text": "`PipelineHandler::stop` 함수는 `stopDevice` 를 호출하기 전에 `data->waitingRequests_` 큐에 대기 중인 모든 요청을 `waitingRequests`라는 임시 변수로 분리합니다.", "evidence": ["device-stop"], "covers": ["stopping"], "kind": "behavior", "quote": "\\brief Stop capturing from all running streams and cancel pending requests\n * \\param[in] camera The camera to stop\n *\n * This function stops capturing and processing requests immediately. All\n * pending requests are cancelled and complete immediately in an error state.\n *\n * \\context This function is called from the CameraManager thread.\n */\nvoid PipelineHandler::stop(Camera *camera)\n{\n\t/*\n\t * Take all waiting requests so that they are not requeued in response\n\t * to completeRequest() being called inside stopDevice(). Cancel them\n\t * after the device to keep them in order.\n\t */\n\tCamera::Private *data = camera->_d();\n\tstd::queue<Request *> waitingRequests;\n\twaitingRequests.swap(data->waitingRequests_);", "part_id": "device-entry"}, {"text": "`doQueueRequest`라는 함수 호출이 요청 인자를 전달하며, 이 호출은 캡처를 중지하거나 대기 중인 요청을 취소하는 경로의 일부로 관찰됩니다.", "evidence": ["pending-requeue"], "covers": ["stopping"], "kind": "behavior", "quote": "doQueueRequest(request);", "part_id": "pending"}, {"text": "`PipelineHandler::stop` 함수 내부에서 `data->queuedRequests_.empty()`와 `data->waitingRequests_.empty()` 두 가지 ASSERT 문은 해당 큐가 비어있음을 확인합니다.", "evidence": ["stop-assertions"], "covers": ["stopping"], "kind": "behavior", "quote": "ASSERT(data->queuedRequests_.empty());\n\tASSERT(data->waitingRequests_.empty());", "part_id": "queue-assertions"}, {"text": "`PipelineHandler::completeRequest` 함수는 요청이 완료되었음을 카메라에 알리기 위해 호출되며, 이 함수는 반드시 `CameraManager` 스레드에서 실행되어야 합니다.", "evidence": ["completion"], "covers": ["stopping"], "kind": "behavior", "quote": "/**\n * \\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();", "part_id": "completion"}, {"text": "`Camera::disconnect()` 함수는 카메라 인스턴스가 연결된 하드웨어가 뽑혔음을 알리기 위해 내부적으로 `_d()->disconnect()`를 호출합니다.", "evidence": ["notification"], "covers": ["stopping"], "kind": "behavior", "quote": "\\brief Notify camera disconnection\n *\n * This function is used to notify the camera instance that the underlying\n * hardware has been unplugged. In response to the disconnection the camera\n * instance notifies the application by emitting the #disconnected signal, and\n * ensures that all new calls to the application-facing Camera API return an\n * error immediately.\n *\n * \\todo Deal with pending requests if the camera is disconnected in a\n * running state.\n */\nvoid Camera::disconnect()\n{\n\tLOG(Camera, Debug) << \"Disconnecting camera \" << id();", "part_id": "disconnect"}, {"text": "`disconnected.emit()` 호출은 `Camera::disconnect()` 함수 내부에서 발생하며, 이 호출은 `disconnected`라는 이름의 신호를 발행합니다.", "evidence": ["disconnect-signal"], "covers": ["stopping"], "kind": "behavior", "quote": "disconnected.emit();", "part_id": "disconnect-signal"}, {"text": "`Camera::disconnect()` 함수가 카메라가 실행 중인 상태에서 연결이 끊길 때 처리해야 할 미해결 요청을 명시적으로 언급하고 있습니다.", "evidence": ["disconnect-todo"], "covers": ["stopping"], "kind": "behavior", "quote": "\\todo Deal with pending requests if the camera is disconnected in a\n * running state.", "part_id": "disconnect-todo"}, {"text": "`Camera::disconnect` 함수는 하드웨어가 뽑혀 나간 상황을 카메라 인스턴스에 알리는 역할을 합니다.", "evidence": ["disconnect-todo-owner"], "covers": ["stopping"], "kind": "behavior", "quote": "\\brief Notify camera disconnection\n *\n * This function is used to notify the camera instance that the underlying\n * hardware has been unplugged. In response to the disconnection the camera\n * instance notifies the application by emitting the #disconnected signal, and\n * ensures that all new calls to the application-facing Camera API return an\n * error immediately.\n *\n * \\todo Deal with pending requests if the camera is disconnected in a\n * running state.\n */\nvoid Camera::disconnect()", "part_id": "disconnect-todo-owner"}], "review": [{"text": "함수 queueRequest 의 반환값 항목은 성공 시 0 이나 실패 시 음수 오류 코드 (-ENODEV, -EACCES, -EXDEV, -EINVAL, -ENOMEM) 를 기록할 수 있습니다.", "evidence": ["queue"], "covers": ["review"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();\n\n\tint ret = d->isAccessAllowed(Private::CameraRunning);\n\tif (ret < 0)\n\t\treturn ret;\n\n\t/* Requests can only be queued to the camera that created them. */\n\tif (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;\n\t}\n\n\tif (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}\n\n\t/* Make sure the Request has a valid control list. */\n\tif (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * The camera state may change until the end of the function. No locking\n\t * is however needed as PipelineHandler::queueRequest() will handle\n\t * this.\n\t */\n\n\tif (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}\n\n\t/* Pre-process AeEnable. */\n\tpatchControlList(request->controls());\n\n\td->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;\n}\n\n/**\n * \\brief Start capture from camera", "part_id": "submission-record"}, {"text": "소스 기반 조사 기록을 위해 제안하는 대입문의 대상 변수 이름은 '`status_`'이며, 이 변수에 할당되는 기록 항목의 값은 'RequestPending'입니다.", "evidence": ["record-status"], "covers": ["review"], "kind": "behavior", "quote": "status_ = RequestPending;", "part_id": "reuse-state-record"}, {"text": "소스 기반 조사에서 '`controls_`.clear()' 호출에 대한 기록 항목으로 제안할 변수는 소스 코드에 명시된 '`controls_`'입니다.", "evidence": ["record-controls"], "covers": ["review"], "kind": "behavior", "quote": "controls_.clear();", "part_id": "reuse-data-record"}, {"text": "소스 기반 조사에서 `_d()`->`metadata_` 변수를 기록 항목으로 제안합니다.", "evidence": ["record-metadata"], "covers": ["review"], "kind": "behavior", "quote": "_d()->metadata_.clear();", "part_id": "reuse-metadata-record"}, {"text": "소스 기반 조사 기록에 넣을 선두 요청의 상태 조회식은 'if (req->status() == `Request::RequestPending`)'이며, 이는 `PipelineHandler::completeRequest` 함수 내에서 req 객체의 상태를 확인하는 코드 구절로 제안됩니다.", "evidence": ["record-head-status"], "covers": ["review"], "kind": "behavior", "quote": "if (req->status() == Request::RequestPending)\n\t\t\tbreak;", "part_id": "completion-record"}, {"text": "`PipelineHandler::stop` 함수 내부에서 stopDevice(camera) 호출이 수행되는지 여부를 기록합니다.", "evidence": ["record-device"], "covers": ["review"], "kind": "behavior", "quote": "stopDevice(camera);", "part_id": "stop-record"}, {"text": "제안하는 조사 계획에서 기록 항목으로 '`queuedRequests_`'라는 식과 해당 큐가 비어 있는지 여부를 포함해야 하며, 이는 void `PipelineHandler::stop`(`Camera` *camera) 함수의 시작점과 끝점을 사이에 두고 ASSERT(data->`queuedRequests_`.empty()) 문장이 검사하는 내용을 반영한 것입니다.", "evidence": ["record-queued"], "covers": ["review"], "kind": "behavior", "quote": "ASSERT(data->queuedRequests_.empty());", "part_id": "stop-queued-record"}, {"text": "제안하는 조사 계획에서 기록 항목은 함수 'void `PipelineHandler::stop`(`Camera` *camera)'이 종료될 때 실행되는 ASSERT(data->`waitingRequests_`.empty())가 검사하는 큐의 상태, 즉 `waitingRequests_`라는 식을 가진 큐가 비어있는지 여부를 포함해야 하며, 이 ASSERT는 호출 시점에 큐가 비어있음을 보장하지 않고 함수 종료 시점의 상태 확인에 해당하므로 기록 항목은 해당 시점의 큐 비어 여부만을 반영해야 합니다.", "evidence": ["record-waiting"], "covers": ["review"], "kind": "behavior", "quote": "ASSERT(data->waitingRequests_.empty());", "part_id": "stop-waiting-record"}]}, "topic_inputs": {"configuration-failure": "eeb2420ae54b8cebe127a1706833ced63c83fbd44bd45e1a9de71d80aec14874", "journey": "12d71b18b59834c52d82d65499e6592c7bb53993b3eb910866147ab655c16414", "resources": "6c31818dd2785f4e979433f661fab23c49a04a628c1b6ddab3da9180c592a79a", "diagnosis": "e8a4c77dd0dcb751358edfbea1233bdd2749e819952576ffe487a23ab31b84fe", "stopping": "e292bf92ce1588f934721f1e156940792e0b3fced8e8a05eed99cd9a8bf8feb9", "review": "3187eb6bcd60d06f0e386186d175838f51e871c2995e6e88cc832df80e8d2d58"}, "reused_topics": ["configuration-failure", "journey", "resources", "diagnosis", "stopping", "review"], "replayed_units": [], "generated_topics": [], "topic_agents": {"configuration-failure": "ollama/qwen3.5:9b", "journey": "ollama/qwen3.5:9b", "resources": "ollama/qwen3.5:9b", "diagnosis": "ollama/qwen3.5:9b", "stopping": "ollama/qwen3.5:9b", "review": "ollama/qwen3.5:9b"}, "grounding_review": "passed", "grounding_policy": "c54006f7c90cb2af955e1ede18b761c7feb22dffa3bc37a885c019508348eba0", "body_sha256": "0b9658d38d3c3708320f7483566fa2263b28625252fc485a9d3bc45f43422733"}
---

# 요청 처리와 문제 진단

**요청의 제출 성공과 촬영 완료를 구분하고, 버퍼를 유지할 기간과 오류가 난 위치를 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 구성 실패의 반환값과 분기를 확인합니다. | [구성 실패를 좁히는 순서](#구성-실패를-좁히는-순서) |
| 요청 제출과 완료의 연결을 확인합니다. | [제출에서 완료까지](#제출에서-완료까지) |
| 자원을 재사용하거나 해제할 시점을 확인합니다. | [요청·버퍼·fence의 수명](#요청버퍼fence의-수명) |
| 완료 누락의 관측 지점을 찾습니다. | [실패 위치별 확인 순서](#실패-위치별-확인-순서) |
| 정지와 연결 해제의 차이를 확인합니다. | [정지와 연결 해제를 구분하기](#정지와-연결-해제를-구분하기) |

## 구성 실패를 좁히는 순서

`Camera::configure` 함수 내부에서 `d->isAccessAllowed(Private::CameraAcquired, Private::CameraConfigured)` 호출의 반환값을 변수 `ret`에 저장한 뒤, 이 값이 음수인지 확인하여 실패 시 즉시 반환하는 로직을 관찰해야 합니다. `src/libcamera/camera.cpp:1195`

<!-- sdd:visual:configure-failures -->
### 구성 실패를 좁히는 분기

입력 검사와 장치 구현 실패를 순서대로 구분하세요. 아래 그림의 성공 경로에서도 스트림 연결 검사가 남습니다.

```mermaid
flowchart TB
%% sdd:translations {"-EINVAL 반환": "Return -EINVAL", "0이 아니면 즉시 반환": "Return immediately when <br/>nonzero", "PipelineHandler::configure()": "PipelineHandler::configure()", "validate() == Valid인가?": "Does validate() return <br/>Valid?", "상태·접근이 허용되는가?": "State and access allowed?", "아니오": "No", "아니오: Adjusted도 거절": "No: Adjusted is also <br/>rejected", "예: 입력 검사": "Yes: validate input", "예: 장치 구성": "Yes: configure device", "장치 반환값을 확인": "Inspect device return value", "접근 오류 반환": "Return access error"}
  v_access{"상태·접근이 허용되는가?"}
  v_accesserror["접근 오류 반환"]
  v_valid{"validate() == Valid인가?"}
  v_invalid["-EINVAL 반환"]
  v_device["PipelineHandler::configure()"]
  v_ret["장치 반환값을 확인"]
  v_access -->|"아니오"| v_accesserror
  v_access -->|"예: 입력 검사"| v_valid
  v_valid -->|"아니오: Adjusted도 거절"| v_invalid
  v_valid -->|"예: 장치 구성"| v_device
  v_device -->|"0이 아니면 즉시 반환"| v_ret
```

[Mermaid 원문](request-lifecycle.configure-failures.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | 상태·접근이 허용되는가? | [src/libcamera/camera.cpp:1163](#source-4e218db5e20840dc) |
    | 접근 오류 반환 | [src/libcamera/camera.cpp:1163](#source-4e218db5e20840dc) |
    | validate() == Valid인가? | [src/libcamera/camera.cpp:1163](#source-4e218db5e20840dc) |
    | -EINVAL 반환 | [src/libcamera/camera.cpp:1163](#source-4e218db5e20840dc) |
    | PipelineHandler::configure() | [src/libcamera/camera.cpp:1163](#source-4e218db5e20840dc) |
    | 장치 반환값을 확인 | [src/libcamera/camera.cpp:1163](#source-4e218db5e20840dc) |
    | 아니오 | [src/libcamera/camera.cpp:1163](#source-4e218db5e20840dc) |
    | 예: 입력 검사 | [src/libcamera/camera.cpp:1163](#source-4e218db5e20840dc) |
    | 아니오: Adjusted도 거절 | [src/libcamera/camera.cpp:1163](#source-4e218db5e20840dc) |
    | 예: 장치 구성 | [src/libcamera/camera.cpp:1163](#source-4e218db5e20840dc) |
    | 0이 아니면 즉시 반환 | [src/libcamera/camera.cpp:1163](#source-4e218db5e20840dc) |
<!-- /sdd:visual:configure-failures -->

`isAccessAllowed` 함수는 `allowDisconnected` 가 거짓이고 `disconnected_` 가 참인 경우에만 `-ENODEV` 를 반환합니다. `src/libcamera/camera.cpp:709`

`isAccessAllowed` 함수는 현재 카메라 상태를 `currentState`로 로드한 후, 요청된 상태 범위인 `low`와 `high`가 `currentState`를 포함하는지 확인합니다. 이 과정에서 `currentState >= low && currentState <= high` 조건이 참이면 접근을 허용하고 거짓이면 `-EACCES` 오류를 반환하며, 로그에 현재 상태와 요구되는 상태 범위를 기록합니다. `src/libcamera/camera.cpp:716`

`CameraConfiguration::validate()` 함수가 `CameraConfiguration::Adjusted` 상태를 반환하면, 해당 스트림의 파라미터 값이 변경되었을 수도 있고, 스트림 구성 자체가 제거되었을 수 있습니다. `src/libcamera/camera.cpp:342`

`CameraConfiguration::Adjusted`를 반환하는 호출자는 반드시 해당 구성을 신중하게 확인해야 합니다. `src/libcamera/camera.cpp:343`

`Camera::configure` 함수 내부에서 `config->validate()` 호출의 반환값이 `CameraConfiguration::Valid`와 일치하지 않을 경우, 해당 비교 대상 상태 이름은 코드 흐름상 `-EINVAL` 오류 코드가 반환되기 직전의 조건 분기에서 관찰됩니다. `src/libcamera/camera.cpp:1203`

`Camera::configure` 함수가 `config->validate()` 호출 결과가 유효하지 않은 값일 때, 즉 비교 조건이 참이면 해당 함수는 오류 로그를 출력한 뒤 `-EINVAL` 코드를 반환합니다. `src/libcamera/camera.cpp:1203`

`Camera::configure` 함수는 상태 검증이 통과한 뒤 `d->pipe_->invokeMethod(&PipelineHandler::configure, ...)` 호출의 반환값을 확인하여 실패 위치를 파악해야 합니다. `src/libcamera/camera.cpp:1191`

`Camera::configure` 함수 내부에서 `cfg.stream()` 호출 결과를 확인하고, 만약 스트림 포인터가 null 이라면 파이프라인 핸들러가 스트림 구성을 업데이트하는 데 실패했다는_fatal 로그를 출력하며 `-EINVAL` 오류 코드를 반환합니다. `src/libcamera/camera.cpp:1225`

근거 원문: [src/libcamera/camera.cpp:1163](#source-4e218db5e20840dc) · [src/libcamera/camera.cpp:709](#source-1e64f4ece8808997) · [src/libcamera/camera.cpp:323](#source-cb5242e98ac1e72c) · [src/libcamera/camera.cpp:1191](#source-846c5a830281fa6a) · [src/libcamera/camera.cpp:716](#source-9328b9e82bc716a1) · [src/libcamera/camera.cpp:342](#source-e13fede0aa40ada1) · [src/libcamera/camera.cpp:343](#source-e5758fc43bf244cd) · [src/libcamera/camera.cpp:1203](#source-fcc2510602fe412b) · [src/libcamera/camera.cpp:1225](#source-fa2c87e2c2f4e322) · [src/libcamera/camera.cpp:1195](#source-2da795dd561f56ec)

## 제출에서 완료까지

`Camera::createRequest()` 함수는 애플리케이션이 버퍼와 매개변수로 채우고 캡처를 대기하도록 할 빈 요청을 생성하며, 생성된 요청의 소유권은 호출자에게 전달되어 호출자가 이를 삭제할 책임이 있습니다. `src/libcamera/camera.cpp:1243`

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

버퍼를 요청의 특정 스트림에 연결하는 API는 `Request::addBuffer()` 함수이며, 이 함수는 `Stream` 포인터와 `FrameBuffer` 포인터를 인자로 받아 버퍼를 요청에 추가합니다. `src/libcamera/request.cpp:442`

`Camera::queueRequest` 함수는 성공 시 0 을 반환하며, 요청이 큐에 등록된 후 카메라는 requestCompleted 신호를 통해 완료 통지를 합니다. `src/libcamera/camera.cpp:1308`

대기 큐와 장치 큐 한도로 요청 전달을 제한하는 두 변수는 각각 data->`waitingRequests_` 와 `maxQueuedRequestsDevice_` 입니다. `src/libcamera/pipeline_handler.cpp:428`

코드에서 선두 요청이 준비되었는지 확인하는 멤버는 `prepared_` 입니다. `src/libcamera/pipeline_handler.cpp:516`

void `PipelineHandler::doQueueRequest` 함수는 요청을 큐에 추가한 후, 해당 요청이 취소되었는지(`cancelled_`)를 확인하여 분기합니다. 만약 요청이 취소된 경우라면 completeRequest 를 호출하고 함수를 종료하며, 취소되지 않은 경우 queueRequestDevice 를 호출한 뒤 그 반환값(ret)이 0 이 아닌 경우 cancelRequest 를 호출합니다. `src/libcamera/pipeline_handler.cpp:483`

함수의 이름은 `PipelineHandler::queueRequestDevice()`이며, 성공 시 0 을 반환합니다. `src/libcamera/pipeline_handler.cpp:530`

이 함수는 성공 시 0 을 반환하며, 오류가 발생하면 음수인 오류 코드를 반환합니다. `src/libcamera/pipeline_handler.cpp:530`

버퍼 완료를 알릴 때 파이프라인 핸들러는 completeBuffer() 함수를 호출해야 하며, 이 함수는 요청의 버퍼 부분 완료를 신호로 보내고 애플리케이션에 완료를 통보하며 요청의 내부 버퍼 추적을 업데이트해야 합니다. `src/libcamera/pipeline_handler.cpp:547`

마지막 버퍼가 완료된 후에도 요청이 자동으로 완료되지 않으며, 파이프라인 핸들러가 여전히 수행해야 할 작업을 위해 명시적으로 completeRequest() 함수를 호출하여 요청을 완료해야 합니다. `src/libcamera/pipeline_handler.cpp:553`

`PipelineHandler::completeRequest` 함수는 요청이 완료되었을 때 애플리케이션에 요청을 제출 순서(submission order)로 반환하도록 보장합니다. `src/libcamera/pipeline_handler.cpp:571`

이 분기는 요청의 상태가 `Request::RequestPending` 인지를 판단합니다. `src/libcamera/pipeline_handler.cpp:594`

근거 원문: [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) · [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) · [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) · [src/libcamera/pipeline_handler.cpp:483](#source-7348e9b4af985eb2) · [src/libcamera/pipeline_handler.cpp:530](#source-c05f8214908fe4fe) · [src/libcamera/pipeline_handler.cpp:547](#source-ab8710f8a8a7905d) · [src/libcamera/pipeline_handler.cpp:571](#source-236c920e906cb6fd) · [src/libcamera/pipeline_handler.cpp:516](#source-a637b7daf9acb7ac) · [src/libcamera/pipeline_handler.cpp:553](#source-5b0ae08604dff588) · [src/libcamera/pipeline_handler.cpp:594](#source-bae861ceef5e8406)

## 요청·버퍼·fence의 수명

`Camera::createRequest` 함수는 새로 생성된 요청 객체의 소유권을 호출자에게 넘깁니다. `src/libcamera/camera.cpp:1243`

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

`Request::addBuffer` 함수를 호출한 호출자는 요청의 완료 콜백이 호출될 때까지 버퍼가 유효하게 유지되도록 해야 합니다. `src/libcamera/request.cpp:447`

`addBuffer` 함수가 성공적으로 호출되고 유효한 펜스가 제공되면, 그 펜스의 소유권이 `buffer` 객체로 이동합니다. `src/libcamera/request.cpp:456`

`addBuffer` 함수가 실패할 경우, 전달받은 `fence` 는 수정되지 않고 원래 상태로 유지됩니다. `src/libcamera/request.cpp:456`

요청 (`Request`) 이 프레임 버퍼에 연결된 펜스 신호를 받지 못하면 요청은 지정된 시간 이후 타임아웃으로 실패합니다. `src/libcamera/request.cpp:462`

타임아웃으로 인해 요청이 실패한 후 버퍼를 재사용하려면 호출자는 `FrameBuffer::releaseFence()` 함수를 반드시 호출해야 합니다. `src/libcamera/request.cpp:462`

`Request::reuse` 함수의 실행 흐름에서 `ReuseBuffers` 분기 조건이 충족되면 내부적으로 `buffer->_d()->setRequest(this)` 호출이 수행되어 기존 버퍼를 현재 요청에 연결합니다. `src/libcamera/request.cpp:393`

`Request::reuse` 함수에서 `ReuseBuffers` 플래그가 설정된 경우, 버퍼 맵에 있는 모든 버퍼를 순회하며 각 버퍼의 `_d()` 를 통해 `setRequest(this)` 호출로 현재 요청과 연동하고, 그 다음 `_d()->pending_` 집합에 해당 버퍼를 추가합니다. `src/libcamera/request.cpp:391`

`Request::reuse()` 함수의 `ReuseBuffers` 플래그가 없는 else 분기에서는 `bufferMap_`를 비웁니다. `src/libcamera/request.cpp:391`

`Request::reuse` 함수 내부에서 `status_` 변수에 `RequestPending` 값을 대입하는 것은 요청이 재사용 준비 상태로 설정됨을 나타냅니다. `src/libcamera/request.cpp:400`

`Request::reuse` 함수 내부에서 `controls_` 멤버 변수에 대한 호출은 해당 벡터를 비우는 초기화 작업만 수행합니다. `src/libcamera/request.cpp:402`

`Request::reuse` 함수 내부에서 `_d()->metadata_.clear()` 호출은 `metadata_` 멤버 변수에 저장된 모든 메타데이터 항목을 제거하여 초기화 상태를 만듭니다. `src/libcamera/request.cpp:403`

`Request::ReuseBuffers` 플래그는 `addBuffer()` 함수를 통해 이전에 추가된 버퍼들을 재사용하도록 요청합니다. `src/libcamera/request.cpp:326`

`Request::ReuseBuffers` 플래그를 사용하면 `addBuffer()` 로 추가된 버퍼만 재사용되지만, 해당 버퍼에 연결된 펜스 (`Fence`) 는 재사용되지 않습니다. `src/libcamera/request.cpp:326`

`Request::ReuseFlag` 플래그는 펜스 (fence) 가 사용될 경우 사용하지 않는 것이 좋습니다. `src/libcamera/request.cpp:334`

`PipelineHandler::completeRequest()` 함수가 반환하면 해당 요청은 더 이상 파이프라인 핸들러에 의해 관리되지 않으며, 이 함수가 돌아온 이후에는 해당 요청을 접근해서는 안 됩니다. `src/libcamera/pipeline_handler.cpp:547`

`cancelRequest` 함수가 반환되면 해당 요청은 파이프라인 핸들러에 의해 더 이상 관리되지 않으며, 이 함수가 돌아온 이후에는 요청을 접근해서는 안 됩니다. `src/libcamera/pipeline_handler.cpp:610`

근거 원문: [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) · [src/libcamera/request.cpp:376](#source-38494771cb29cc8c) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) · [src/libcamera/request.cpp:326](#source-447804db33308244) · [src/libcamera/request.cpp:456](#source-86a8d784a8348122) · [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) · [src/libcamera/request.cpp:400](#source-a98823fa5ec440a2) · [src/libcamera/request.cpp:402](#source-c8638489aa83cfd1) · [src/libcamera/request.cpp:403](#source-47569737e131b31a) · [src/libcamera/request.cpp:391](#source-e41b7fa688c1de2e) · [src/libcamera/request.cpp:447](#source-4cdce80c57526221) · [src/libcamera/pipeline_handler.cpp:575](#source-d93a02e9220fa760) · [src/libcamera/pipeline_handler.cpp:610](#source-52fb58c8956b1a91) · [src/libcamera/request.cpp:334](#source-d9944a69f2dd6758) · [src/libcamera/request.cpp:393](#source-bf1ee390b8473e16) · [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1)

## 실패 위치별 확인 순서

`Camera::queueRequest` 함수는 요청을 카메라에 대기열로 등록할 때 반환하는 값을 확인해야 합니다. 이 함수는 호출 성공 시 0 을 반환하고, 실패 시 음수 오류 코드를 반환합니다. `src/libcamera/camera.cpp:1308`

<!-- sdd:visual:queue-gates -->
### 요청이 대기하거나 장치로 가는 조건

준비 대기와 장치 큐 한도를 구분하세요. 준비 실패와 장치 제출 실패는 취소 경로로 이어집니다.

```mermaid
flowchart TB
%% sdd:translations {"doQueueRequests()에서 확인": "Check in doQueueRequests()", "queueRequestDevice()": "queueRequestDevice()", "waitingRequests_": "waitingRequests_", "대기열에 유지": "Stay in waiting queue", "선두 요청이 prepared_인가?": "Is the front request <br/>prepared?", "아니오: 선두 요청 확인": "No: inspect front request", "아니오: 준비를 기다림": "No: wait for preparation", "예: 새 요청을 전달하지 않음": "Yes: stop forwarding", "예: 준비 실패로 취소되지 <br/>않은 요청": "Yes: unless cancelled <br/>during preparation", "장치 제출 실패": "Device queue failure", "장치 큐 한도에 도달했는가?": "Device queue at its limit?", "준비 중 취소된 요청은 장치 <br/>제출 생략": "Skip device for cancelled <br/>request", "취소·완료 경로": "Cancellation and completion"}
  v_wait["waitingRequests_"]
  v_ready{"선두 요청이 prepared_인가?"}
  v_limit{"장치 큐 한도에 도달했는가?"}
  v_hold["대기열에 유지"]
  v_device["queueRequestDevice()"]
  v_cancel["취소·완료 경로"]
  v_wait -->|"doQueueRequests()에서 확인"| v_limit
  v_limit -->|"예: 새 요청을 전달하지 않음"| v_hold
  v_limit -->|"아니오: 선두 요청 확인"| v_ready
  v_ready -->|"아니오: 준비를 기다림"| v_hold
  v_ready -->|"예: 준비 실패로 취소되지 <br/>않은 요청"| v_device
  v_device -->|"장치 제출 실패"| v_cancel
  v_ready -->|"준비 중 취소된 요청은 장치 <br/>제출 생략"| v_cancel
```

[Mermaid 원문](request-lifecycle.queue-gates.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | waitingRequests_ | [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) |
    | 선두 요청이 prepared_인가? | [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) |
    | 장치 큐 한도에 도달했는가? | [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) |
    | 대기열에 유지 | [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) |
    | queueRequestDevice() | [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) |
    | 취소·완료 경로 | [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) |
    | doQueueRequests()에서 확인 | [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) |
    | 예: 새 요청을 전달하지 않음 | [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) |
    | 아니오: 선두 요청 확인 | [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) |
    | 아니오: 준비를 기다림 | [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) |
    | 예: 준비 실패로 취소되지 않은 요청 | [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) |
    | 장치 제출 실패 | [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) |
    | 준비 중 취소된 요청은 장치 제출 생략 | [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) |
<!-- /sdd:visual:queue-gates -->

`Request::addBuffer` 함수를 호출할 때 `-EEXIST` 오류 코드가 반환되면, 이는 요청에 이미 해당 스트림의 버퍼가 추가되었거나 버퍼에 아직 해제되지 않은 펜스가 남아있기 때문입니다. `src/libcamera/request.cpp:442`

`doQueueRequests` 함수는 `waitingRequests_` 대기열에서 요청을 꺼내 처리하기 전에, 현재 제출된 요청 수인 `queuedRequests_.size()`가 한도 값인 `maxQueuedRequestsDevice_`와 같으면 순회를 멈춥니다. `src/libcamera/pipeline_handler.cpp:428`

`PipelineHandler::doQueueRequests` 함수 내부에서 `data->waitingRequests_.front()`로 선두 요청을 가져온 후, 바로 `_d()` 메서드를 호출하여 접근한 뒤 그 결과의 `prepared_` 멤버 변수 값을 확인하는 위치가 관찰 대상입니다. `src/libcamera/pipeline_handler.cpp:516`

`PipelineHandler::doQueueRequests` 함수가 `data->waitingRequests_`의 첫 번째 요청을 가져온 후, 해당 요청의 `_d()`를 통해 접근한 `prepared_` 멤버 변수가 거짓이면 루프를 중단합니다. `src/libcamera/pipeline_handler.cpp:516`

`PipelineHandler::doQueueRequest` 함수 내부에서 요청의 취소 상태를 확인하는 위치는 `request->_d()->cancelled_` 조건문입니다. 이 식이 참이면 요청을 즉시 완료하고 함수를 종료합니다. `src/libcamera/pipeline_handler.cpp:493`

`PipelineHandler::doQueueRequest` 함수 내부에서 `request->_d()->cancelled_` 조건이 참일 경우, 해당 요청을 즉시 완료 처리하기 위해 `completeRequest(request)` 함수를 호출합니다. `src/libcamera/pipeline_handler.cpp:493`

`PipelineHandler::doQueueRequest` 함수 내에서 `queueRequestDevice` 호출 직후의 반환값을 관찰할 수 있습니다. `src/libcamera/pipeline_handler.cpp:498`

`PipelineHandler::doQueueRequest` 함수 내에서 `queueRequestDevice` 가 오류를 반환하면 바로 다음 줄에서 `cancelRequest` 함수가 호출됩니다. `src/libcamera/pipeline_handler.cpp:498`

`PipelineHandler::completeBuffer` 함수는 요청의 내부 버퍼 추적을 업데이트하고 애플리케이션에 완료를 알립니다. 이 함수가 호출되면 마지막 버퍼가 완료되었더라도 요청이 자동으로 완료되지 않으며, 파이프라인 핸들러가 추가 작업을 수행할 기회를 주기 위해 명시적으로 `completeRequest()` 를 호출해야 합니다. `src/libcamera/pipeline_handler.cpp:547`

`PipelineHandler::completeRequest` 함수 내부에서 `data->queuedRequests_`의 선두 요청이 `RequestPending` 상태인지 확인하는 분기가 존재하며, 이 조건이 참일 경우 루프를 중단합니다. `src/libcamera/pipeline_handler.cpp:547`

근거 원문: [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) · [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) · [src/libcamera/pipeline_handler.cpp:516](#source-a637b7daf9acb7ac) · [src/libcamera/pipeline_handler.cpp:493](#source-0bb6ebc961be6e80) · [src/libcamera/pipeline_handler.cpp:498](#source-1e06e477d10056b7)

## 정지와 연결 해제를 구분하기

`Camera::stop` 함수를 호출할 때 카메라가 실행 중이 아닌 상태라면, `_d()->isRunning()` 조건에서 `false`로 판정되어 즉시 0 을 반환합니다. `src/libcamera/camera.cpp:1431`

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

`Camera::stop()` 함수가 실행될 때 내부적으로 `d->setState(Private::CameraStopping)` 호출을 통해 카메라 상태를 `Private::CameraStopping`으로 변경합니다. `src/libcamera/camera.cpp:1462`

`Camera::stop()` 함수는 `d->pipe_->invokeMethod(&PipelineHandler::stop, ConnectionTypeBlocking, this)`를 호출하여 `PipelineHandler::stop`에 대한 메서드 호출을 시작합니다. `src/libcamera/camera.cpp:1462`

`PipelineHandler::stop` 함수는 `stopDevice` 를 호출하기 전에 `data->waitingRequests_` 큐에 대기 중인 모든 요청을 `waitingRequests`라는 임시 변수로 분리합니다. `src/libcamera/pipeline_handler.cpp:359`

`doQueueRequest`라는 함수 호출이 요청 인자를 전달하며, 이 호출은 캡처를 중지하거나 대기 중인 요청을 취소하는 경로의 일부로 관찰됩니다. `src/libcamera/pipeline_handler.cpp:394`

`PipelineHandler::stop` 함수 내부에서 `data->queuedRequests_.empty()`와 `data->waitingRequests_.empty()` 두 가지 ASSERT 문은 해당 큐가 비어있음을 확인합니다. `src/libcamera/pipeline_handler.cpp:398`

`PipelineHandler::completeRequest` 함수는 요청이 완료되었음을 카메라에 알리기 위해 호출되며, 이 함수는 반드시 `CameraManager` 스레드에서 실행되어야 합니다. `src/libcamera/pipeline_handler.cpp:547`

`Camera::disconnect()` 함수는 카메라 인스턴스가 연결된 하드웨어가 뽑혔음을 알리기 위해 내부적으로 `_d()->disconnect()`를 호출합니다. `src/libcamera/camera.cpp:944`

`disconnected.emit()` 호출은 `Camera::disconnect()` 함수 내부에서 발생하며, 이 호출은 `disconnected`라는 이름의 신호를 발행합니다. `src/libcamera/camera.cpp:960`

`Camera::disconnect()` 함수가 카메라가 실행 중인 상태에서 연결이 끊길 때 처리해야 할 미해결 요청을 명시적으로 언급하고 있습니다. `src/libcamera/camera.cpp:952`

`Camera::disconnect` 함수는 하드웨어가 뽑혀 나간 상황을 카메라 인스턴스에 알리는 역할을 합니다. `src/libcamera/camera.cpp:944`

근거 원문: [src/libcamera/camera.cpp:1431](#source-e09324743def3f09) · [src/libcamera/pipeline_handler.cpp:359](#source-eefd1bbecb1aad0a) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) · [src/libcamera/camera.cpp:1462](#source-6191f91df6cbffa2) · [src/libcamera/pipeline_handler.cpp:398](#source-5e7914238ff81605) · [src/libcamera/camera.cpp:952](#source-1d583253fc11ef1c) · [src/libcamera/pipeline_handler.cpp:394](#source-fd5daba4aa44adfd) · [src/libcamera/camera.cpp:959](#source-56494d0aedf70c2d) · [src/libcamera/camera.cpp:960](#source-7d48ce2e18c8877c) · [src/libcamera/camera.cpp:944](#source-2758e9ddd31ad41d) · [src/libcamera/camera.cpp:944](#source-839140c350119dd1)

## 변경 검토와 실행 확인

함수 queueRequest 의 반환값 항목은 성공 시 0 이나 실패 시 음수 오류 코드 (-ENODEV, -EACCES, -EXDEV, -EINVAL, -ENOMEM) 를 기록할 수 있습니다. `src/libcamera/camera.cpp:1308`

소스 기반 조사 기록을 위해 제안하는 대입문의 대상 변수 이름은 '`status_`'이며, 이 변수에 할당되는 기록 항목의 값은 'RequestPending'입니다. `src/libcamera/request.cpp:400`

소스 기반 조사에서 '`controls_`.clear()' 호출에 대한 기록 항목으로 제안할 변수는 소스 코드에 명시된 '`controls_`'입니다. `src/libcamera/request.cpp:402`

소스 기반 조사에서 `_d()`->`metadata_` 변수를 기록 항목으로 제안합니다. `src/libcamera/request.cpp:403`

소스 기반 조사 기록에 넣을 선두 요청의 상태 조회식은 'if (req->status() == `Request::RequestPending`)'이며, 이는 `PipelineHandler::completeRequest` 함수 내에서 req 객체의 상태를 확인하는 코드 구절로 제안됩니다. `src/libcamera/pipeline_handler.cpp:594`

`PipelineHandler::stop` 함수 내부에서 stopDevice(camera) 호출이 수행되는지 여부를 기록합니다. `src/libcamera/pipeline_handler.cpp:379`

제안하는 조사 계획에서 기록 항목으로 '`queuedRequests_`'라는 식과 해당 큐가 비어 있는지 여부를 포함해야 하며, 이는 void `PipelineHandler::stop`(`Camera` *camera) 함수의 시작점과 끝점을 사이에 두고 ASSERT(data->`queuedRequests_`.empty()) 문장이 검사하는 내용을 반영한 것입니다. `src/libcamera/pipeline_handler.cpp:398`

제안하는 조사 계획에서 기록 항목은 함수 'void `PipelineHandler::stop`(`Camera` *camera)'이 종료될 때 실행되는 ASSERT(data->`waitingRequests_`.empty())가 검사하는 큐의 상태, 즉 `waitingRequests_`라는 식을 가진 큐가 비어있는지 여부를 포함해야 하며, 이 ASSERT는 호출 시점에 큐가 비어있음을 보장하지 않고 함수 종료 시점의 상태 확인에 해당하므로 기록 항목은 해당 시점의 큐 비어 여부만을 반영해야 합니다. `src/libcamera/pipeline_handler.cpp:399`

근거 원문: [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/request.cpp:400](#source-a98823fa5ec440a2) · [src/libcamera/request.cpp:402](#source-c8638489aa83cfd1) · [src/libcamera/request.cpp:403](#source-47569737e131b31a) · [src/libcamera/pipeline_handler.cpp:594](#source-bae861ceef5e8406) · [src/libcamera/pipeline_handler.cpp:379](#source-1bc6b7c1710b9de4) · [src/libcamera/pipeline_handler.cpp:398](#source-22bd3eab4afc5389) · [src/libcamera/pipeline_handler.cpp:399](#source-8a8099ed4a95531d)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 제출 성공 이후의 대기 조건과 완료 책임은 무엇입니까? | [제출에서 완료까지](#제출에서-완료까지) | 코드 근거와 설명 연결 |
    | 어떤 자원을 누가 유지하고 완료 후 무엇을 초기화해야 합니까? | [요청·버퍼·fence의 수명](#요청버퍼fence의-수명) | 코드 근거와 설명 연결 |
    | 제출 실패와 제출 후 완료 지연을 어떻게 구분합니까? | [실패 위치별 확인 순서](#실패-위치별-확인-순서) | 코드 근거와 설명 연결 |
    | 정지 중 요청 반환과 연결 해제의 보장 범위는 어떻게 다릅니까? | [정지와 연결 해제를 구분하기](#정지와-연결-해제를-구분하기) | 코드 근거와 설명 연결 |
    | 문서를 읽고 어떤 질문에 답하고 어떤 실행 증거를 확보해야 합니까? | [변경 검토와 실행 확인](#변경-검토와-실행-확인) | 코드 근거와 설명 연결 |
    | 구성 실패를 상태 검사·구성 검증·장치 구성·스트림 연결 중 어디로 좁히며 어떤 값을 관찰합니까? | [구성 실패를 좁히는 순서](#구성-실패를-좁히는-순서) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-4e218db5e20840dc"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1163"
    `src/libcamera/camera.cpp:1163`에서 시작하는 발췌입니다. 종료 줄은 1243이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `5892a108abafcaf7266fb5798b70facc498e62efce52f04e773156c01471b509`
    
    ```text
    \brief Configure the camera prior to capture
     * \param[in] config The camera configurations to setup
     *
     * Prior to starting capture, the camera must be configured to select a
     * group of streams to be involved in the capture and their configuration.
     * The caller specifies which streams are to be involved and their configuration
     * by populating \a config.
     *
     * The configuration is created by generateConfiguration(), and adjusted by the
     * caller with CameraConfiguration::validate(). This function only accepts fully
     * valid configurations and returns an error if \a config is not valid.
     *
     * Exclusive access to the camera shall be ensured by a call to acquire() prior
     * to calling this function, otherwise an -EACCES error will be returned.
     *
     * \context This function may only be called when the camera is in the Acquired
     * or Configured state as defined in \ref camera_operation, and shall be
     * synchronized by the caller with other functions that affect the camera
     * state.
     *
     * Upon return the StreamConfiguration entries in \a config are associated with
     * Stream instances which can be retrieved with StreamConfiguration::stream().
     *
     * \return 0 on success or a negative error code otherwise
     * \retval -ENODEV The camera has been disconnected from the system
     * \retval -EACCES The camera is not in a state where it can be configured
     * \retval -EINVAL The configuration is not valid
     */
    int Camera::configure(CameraConfiguration *config)
    {
    	Private *const d = _d();
    
    	int ret = d->isAccessAllowed(Private::CameraAcquired,
    				     Private::CameraConfigured);
    	if (ret < 0)
    		return ret;
    
    	for (auto &cfg : *config)
    		cfg.setStream(nullptr);
    
    	if (config->validate() != CameraConfiguration::Valid) {
    		LOG(Camera, Error)
    			<< "Can't configure camera with invalid configuration";
    		return -EINVAL;
    	}
    
    	std::ostringstream msg("configuring streams:", std::ios_base::ate);
    
    	for (unsigned int index = 0; index < config->size(); ++index) {
    		StreamConfiguration &cfg = config->at(index);
    		msg << " (" << index << ") " << cfg.toString();
    	}
    
    	LOG(Camera, Info) << msg.str();
    
    	ret = d->pipe_->invokeMethod(&PipelineHandler::configure,
    				     ConnectionTypeBlocking, this, config);
    	if (ret)
    		return ret;
    
    	d->activeStreams_.clear();
    	for (const StreamConfiguration &cfg : *config) {
    		Stream *stream = cfg.stream();
    		if (!stream) {
    			LOG(Camera, Fatal)
    				<< "Pipeline handler failed to update stream configuration";
    			d->activeStreams_.clear();
    			return -EINVAL;
    		}
    
    		stream->configuration_ = cfg;
    		d->activeStreams_.insert(stream);
    	}
    
    	d->setState(Private::CameraConfigured);
    
    	return 0;
    }
    
    /**
     * \brief Create a request object for the camera
    ```

<a id="source-1e64f4ece8808997"></a>

??? note "소스 근거: src/libcamera/camera.cpp:709"
    `src/libcamera/camera.cpp:709`에서 시작하는 발췌입니다. 종료 줄은 732이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `4652821b0f8cfd78a0a4b8ec372fe45eb5ed2fc9b2280a765c3dc47bcc13767b`
    
    ```text
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
    ```

<a id="source-cb5242e98ac1e72c"></a>

??? note "소스 근거: src/libcamera/camera.cpp:323"
    `src/libcamera/camera.cpp:323`에서 시작하는 발췌입니다. 종료 줄은 350이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `a6c84f68e53cafd0f2721ee7eee586981059b62a93378a48235f86ffaa0a8fce`
    
    ```text
    \fn CameraConfiguration::validate()
     * \brief Validate and possibly adjust the camera configuration
     *
     * This function adjusts the camera configuration to the closest valid
     * configuration and returns the validation status.
     *
     * \todo Define exactly when to return each status code. Should stream
     * parameters set to 0 by the caller be adjusted without returning Adjusted ?
     * This would potentially be useful for applications but would get in the way
     * in Camera::configure(). Do we need an extra status code to signal this ?
     *
     * \todo Handle validation of buffers count when refactoring the buffers API.
     *
     * \return A CameraConfiguration::Status value that describes the validation
     * status.
     * \retval CameraConfiguration::Invalid The configuration is invalid and can't
     * be adjusted. This may only occur in extreme cases such as when the
     * configuration is empty.
     * \retval CameraConfiguration::Adjusted The configuration has been adjusted
     * and is now valid. Parameters may have changed for any stream, and stream
     * configurations may have been removed. The caller shall check the
     * configuration carefully.
     * \retval CameraConfiguration::Valid The configuration was already valid and
     * hasn't been adjusted.
     */
    
    /**
     * \brief Retrieve a reference to a stream configuration
    ```

<a id="source-846c5a830281fa6a"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1191"
    `src/libcamera/camera.cpp:1191`에서 시작하는 발췌입니다. 종료 줄은 1243이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e6185ee35674c441653590c65d2de1bc40d13b5a9d8ef8dc083936c54cb7f470`
    
    ```text
    int Camera::configure(CameraConfiguration *config)
    {
    	Private *const d = _d();
    
    	int ret = d->isAccessAllowed(Private::CameraAcquired,
    				     Private::CameraConfigured);
    	if (ret < 0)
    		return ret;
    
    	for (auto &cfg : *config)
    		cfg.setStream(nullptr);
    
    	if (config->validate() != CameraConfiguration::Valid) {
    		LOG(Camera, Error)
    			<< "Can't configure camera with invalid configuration";
    		return -EINVAL;
    	}
    
    	std::ostringstream msg("configuring streams:", std::ios_base::ate);
    
    	for (unsigned int index = 0; index < config->size(); ++index) {
    		StreamConfiguration &cfg = config->at(index);
    		msg << " (" << index << ") " << cfg.toString();
    	}
    
    	LOG(Camera, Info) << msg.str();
    
    	ret = d->pipe_->invokeMethod(&PipelineHandler::configure,
    				     ConnectionTypeBlocking, this, config);
    	if (ret)
    		return ret;
    
    	d->activeStreams_.clear();
    	for (const StreamConfiguration &cfg : *config) {
    		Stream *stream = cfg.stream();
    		if (!stream) {
    			LOG(Camera, Fatal)
    				<< "Pipeline handler failed to update stream configuration";
    			d->activeStreams_.clear();
    			return -EINVAL;
    		}
    
    		stream->configuration_ = cfg;
    		d->activeStreams_.insert(stream);
    	}
    
    	d->setState(Private::CameraConfigured);
    
    	return 0;
    }
    
    /**
     * \brief Create a request object for the camera
    ```

<a id="source-9328b9e82bc716a1"></a>

??? note "소스 근거: src/libcamera/camera.cpp:716"
    `src/libcamera/camera.cpp:716`에서 시작하는 발췌입니다. 종료 줄은 729이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `5ab79ef3ca49ade8dd11511db4c512b99c2857d6eeb73c27919f3d972c2e78cc`
    
    ```text
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
    ```

<a id="source-e13fede0aa40ada1"></a>

??? note "소스 근거: src/libcamera/camera.cpp:342"
    `src/libcamera/camera.cpp:342`에서 시작하는 발췌입니다. 종료 줄은 343이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `7c0debb896b6072c0bc59cf3589fbc49b607f915d96f30182d4e02038b94c156`
    
    ```text
    Parameters may have changed for any stream, and stream
     * configurations may have been removed.
    ```

<a id="source-e5758fc43bf244cd"></a>

??? note "소스 근거: src/libcamera/camera.cpp:343"
    `src/libcamera/camera.cpp:343`에서 시작하는 발췌입니다. 종료 줄은 344이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `f2efdb13d4f1bd8dd432fb0badb987eab0cc484fe8ecb30b7ea9d47c0126590c`
    
    ```text
    The caller shall check the
     * configuration carefully.
    ```

<a id="source-fcc2510602fe412b"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1203"
    `src/libcamera/camera.cpp:1203`에서 시작하는 발췌입니다. 종료 줄은 1206이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `5ee265dc6e41d87b5c011c9621dca0bbee5126a9fdc4633d198adaa12a4f910e`
    
    ```text
    if (config->validate() != CameraConfiguration::Valid) {
    		LOG(Camera, Error)
    			<< "Can't configure camera with invalid configuration";
    		return -EINVAL;
    ```

<a id="source-fa2c87e2c2f4e322"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1225"
    `src/libcamera/camera.cpp:1225`에서 시작하는 발췌입니다. 종료 줄은 1230이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `7cb269c9ced475fe50b39132fab5bd1f830e388d0875c1a3b8ce3f6bad2b573f`
    
    ```text
    Stream *stream = cfg.stream();
    		if (!stream) {
    			LOG(Camera, Fatal)
    				<< "Pipeline handler failed to update stream configuration";
    			d->activeStreams_.clear();
    			return -EINVAL;
    ```

<a id="source-2da795dd561f56ec"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1195"
    `src/libcamera/camera.cpp:1195`에서 시작하는 발췌입니다. 종료 줄은 1198이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `2ca01ecac48b645d4b85b91e1263ca63f344077b66afd74a31ef47b4c6ad17bd`
    
    ```text
    int ret = d->isAccessAllowed(Private::CameraAcquired,
    				     Private::CameraConfigured);
    	if (ret < 0)
    		return ret;
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

<a id="source-e41b7fa688c1de2e"></a>

??? note "소스 근거: src/libcamera/request.cpp:391"
    `src/libcamera/request.cpp:391`에서 시작하는 발췌입니다. 종료 줄은 400이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `2b47b341a1707d21d16d2589f40203968308f0b9b7c9b0ac59d62b3ed792e533`
    
    ```text
    if (flags & ReuseBuffers) {
    		for (const auto &[stream, buffer] : bufferMap_) {
    			buffer->_d()->setRequest(this);
    			_d()->pending_.insert(buffer);
    		}
    	} else {
    		bufferMap_.clear();
    	}
    
    	status_ = RequestPending;
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

<a id="source-bf1ee390b8473e16"></a>

??? note "소스 근거: src/libcamera/request.cpp:393"
    `src/libcamera/request.cpp:393`에서 시작하는 발췌입니다. 종료 줄은 393이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `ede3bfeddecbdb89f3d76930ab26a1c4c232bab0eb12712ce122ad99e600af8c`
    
    ```text
    buffer->_d()->setRequest(this);
    ```

<a id="source-0bb6ebc961be6e80"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:493"
    `src/libcamera/pipeline_handler.cpp:493`에서 시작하는 발췌입니다. 종료 줄은 495이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `1ebc4d56b99218bfb196cf7548aa7167a251392ddb7bf53af9ef4963cc24636b`
    
    ```text
    if (request->_d()->cancelled_) {
    		completeRequest(request);
    		return;
    ```

<a id="source-1e06e477d10056b7"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:498"
    `src/libcamera/pipeline_handler.cpp:498`에서 시작하는 발췌입니다. 종료 줄은 500이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `474a449d8915b2098739e2f25079a56e132930340a353c2538de1f3ca84c3a1e`
    
    ```text
    int ret = queueRequestDevice(camera, request);
    	if (ret)
    		cancelRequest(request);
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

<a id="source-1bc6b7c1710b9de4"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:379"
    `src/libcamera/pipeline_handler.cpp:379`에서 시작하는 발췌입니다. 종료 줄은 379이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `13a940eeb5b83ef63ec2a570d4e1c8357bea011b71722f96e6b7e45daa2342a6`
    
    ```text
    stopDevice(camera);
    ```

<a id="source-22bd3eab4afc5389"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:398"
    `src/libcamera/pipeline_handler.cpp:398`에서 시작하는 발췌입니다. 종료 줄은 398이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `9cbe2a4b7e545083b0e86f981bfaf9ab5c32cb87b85551b89bbe523e48caec33`
    
    ```text
    ASSERT(data->queuedRequests_.empty());
    ```

<a id="source-8a8099ed4a95531d"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:399"
    `src/libcamera/pipeline_handler.cpp:399`에서 시작하는 발췌입니다. 종료 줄은 399이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `b3d10c004fa9f1aa04f0ad8c7edf6647d531f7ccc4569d7596a58cb88d50473a`
    
    ```text
    ASSERT(data->waitingRequests_.empty());
    ```

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `include/libcamera/camera.h`, `include/libcamera/internal/pipeline_handler.h`, `include/libcamera/request.h`, `src/libcamera/camera.cpp`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/request.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `2c4b67c079`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-26 · 사람 검토 전

다음 단계: [Pipeline Handler](pipeline-handler.md)
