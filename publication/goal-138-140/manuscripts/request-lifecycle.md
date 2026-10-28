---
generated_at: 2026-10-28T23:09:52+00:00
source_commit: e117198c015057761bb0bbaa85f963c41ce412d7
status: ok
section: request-lifecycle
generation_method: facts-and-llm
evidence_fingerprint: 1cb65eb7b499ba8cef7c361f3edb8c3857adaa291c5ebb92f2cce41b929137bf
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "1cb65eb7b499ba8cef7c361f3edb8c3857adaa291c5ebb92f2cce41b929137bf", "answers": {"journey": [{"text": "createRequest의 반환 타입은 `std::unique_ptr<Request>`이며, 새로 생성된 빈 `Request` 객체를 가리킵니다. 오류가 발생하면 nullptr을 반환합니다.", "evidence": ["create"], "covers": ["journey"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest(uint64_t cookie)", "part_id": "create"}, {"text": "`Request::addBuffer()`는 버퍼가 속한 스트림을 지정하여 해당 버퍼를 요청에 추가합니다.", "evidence": ["buffer"], "covers": ["journey"], "kind": "behavior", "quote": "\\brief Add a FrameBuffer with its associated Stream to the Request\n * \\param[in] stream The stream the buffer belongs to\n * \\param[in] buffer The FrameBuffer to add to the request\n * \\param[in] fence The optional fence\n *\n * A reference to the buffer is stored in the request. The caller is responsible\n * for ensuring that the buffer will remain valid until the request complete\n * callback is called.\n *\n * A request can only contain one buffer per stream. If a buffer has already\n * been added to the request for the same stream, this function returns -EEXIST.\n *\n * A Fence can be optionally associated with the \\a buffer.\n *\n * When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.\n *\n * If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request. Attempting to add a buffer that still\n * contains a fence to a request will result in this function returning -EEXIST.\n *\n * \\sa FrameBuffer::releaseFence()\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -EEXIST The request already contains a buffer for the stream\n *  or the buffer still references a fence\n * \\retval -EINVAL The buffer does not reference a valid Stream\n */\nint Request::addBuffer(const Stream *stream, FrameBuffer *buffer,", "part_id": "buffer"}, {"text": "`Camera::queueRequest`가 0을 반환하면 요청이 성공적으로 큐에 등록되었음을 의미합니다. 큐에 등록된 요청의 완료는 이후 requestCompleted 신호로 알립니다.", "evidence": ["queue"], "covers": ["journey"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();\n\n\tint ret = d->isAccessAllowed(Private::CameraRunning);\n\tif (ret < 0)\n\t\treturn ret;\n\n\t/* Requests can only be queued to the camera that created them. */\n\tif (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;\n\t}\n\n\tif (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}\n\n\t/* Make sure the Request has a valid control list. */\n\tif (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * The camera state may change until the end of the function. No locking\n\t * is however needed as PipelineHandler::queueRequest() will handle\n\t * this.\n\t */\n\n\tif (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}\n\n\t/* Pre-process AeEnable. */\n\tpatchControlList(request->controls());\n\n\td->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;\n}\n\n/**\n * \\brief Start capture from camera", "part_id": "submission"}, {"text": "`waitingRequests_`는 준비를 기다리는 요청을 순서대로 보관하며, 맨 앞의 요청이 준비되지 않으면 후속 요청의 장치 전달을 멈춥니다. `maxQueuedRequestsDevice_`는 장치에 전달된 요청의 최대 개수를 정하며, 장치 큐의 요청 수가 이 값에 도달하면 추가 전달을 멈춥니다.", "evidence": ["device-queue"], "covers": ["journey"], "kind": "behavior", "quote": "\\fn PipelineHandler::registerRequest()\n * \\brief Register a request for use by the pipeline handler\n * \\param[in] request The request to register\n *\n * This function is called when the request is created, and allows the pipeline\n * handler to perform any one-time initialization it requries for the request.\n */\nvoid PipelineHandler::registerRequest(Request *request)\n{\n\t/*\n\t * Connect the request prepared signal to notify the pipeline handler\n\t * when a request is ready to be processed.\n\t */\n\trequest->_d()->prepared.connect(this, [this, request]() {\n\t\tdoQueueRequests(request->_d()->camera());\n\t});\n}\n\n/**\n * \\fn PipelineHandler::queueRequest()\n * \\brief Queue a request\n * \\param[in] request The request to queue\n *\n * This function queues a capture request to the pipeline handler for\n * processing. The request is first added to the internal list of waiting\n * requests which have to be prepared to make sure they are ready for being\n * queued to the pipeline handler.\n *\n * The queue of waiting requests is iterated and up to \\a\n * maxQueuedRequestsDevice_ prepared requests are passed to the pipeline handler\n * in the same order they have been queued by calling this function.\n *\n * If a Request fails during the preparation phase or if the pipeline handler\n * fails in queuing the request to the hardware the request is cancelled.\n *\n * Keeping track of queued requests ensures automatic completion of all requests\n * when the pipeline handler is stopped with stop(). Request completion shall be\n * signalled by the pipeline handler using the completeRequest() function.\n *\n * \\context This function is called from the CameraManager thread.\n */\nvoid PipelineHandler::queueRequest(Request *request)\n{\n\tLIBCAMERA_TRACEPOINT(request_queue, request);\n\n\tCamera *camera = request->_d()->camera();\n\tCamera::Private *data = camera->_d();\n\tdata->waitingRequests_.push(request);\n\n\trequest->_d()->prepare(300ms);\n}\n\n/**\n * \\brief Queue one requests to the device\n */\nvoid PipelineHandler::doQueueRequest(Request *request)\n{\n\tLIBCAMERA_TRACEPOINT(request_device_queue, request);\n\n\tCamera *camera = request->_d()->camera();\n\tCamera::Private *data = camera->_d();\n\tdata->queuedRequests_.push_back(request);\n\n\trequest->_d()->sequence_ = data->requestSequence_++;\n\n\tif (request->_d()->cancelled_) {\n\t\tcompleteRequest(request);\n\t\treturn;\n\t}\n\n\tint ret = queueRequestDevice(camera, request);\n\tif (ret)\n\t\tcancelRequest(request);\n}\n\n/**\n * \\brief Queue prepared requests to the device\n *\n * Iterate the list of waiting requests and queue them to the device one\n * by one if they have been prepared.\n */\nvoid PipelineHandler::doQueueRequests(Camera *camera)\n{\n\tCamera::Private *data = camera->_d();\n\twhile (!data->waitingRequests_.empty()) {\n\t\tif (data->queuedRequests_.size() == maxQueuedRequestsDevice_)\n\t\t\tbreak;\n\n\t\tRequest *request = data->waitingRequests_.front();\n\t\tif (!request->_d()->prepared_)\n\t\t\tbreak;\n\n\t\t/*\n\t\t * Pop the request first, in case doQueueRequests() is called\n\t\t * recursively from within doQueueRequest()\n\t\t */\n\t\tdata->waitingRequests_.pop();\n\t\tdoQueueRequest(request);\n\t}\n}\n\n/**\n * \\fn PipelineHandler::queueRequestDevice()\n * \\brief Queue a request to the device\n * \\param[in] camera The camera to queue the request to\n * \\param[in] request The request to queue\n *\n * This function queues a capture request to the device for processing. The\n * request contains a set of buffers associated with streams and a set of\n * parameters. The pipeline handler shall program the device to ensure that the\n * parameters will be applied to the frames captured in the buffers provided in\n * the request.\n *\n * \\context This function is called from the CameraManager thread.\n *\n * \\return 0 on success or a negative error code otherwise\n */\n\n/**\n * \\brief Complete a buffer for a request", "part_id": "waiting"}, {"text": "선두 요청의 준비 여부는 `prepared_` 멤버에서 읽으며, 그 값이 거짓이면 반복문을 종료합니다.", "evidence": ["waiting-prepared"], "covers": ["journey"], "kind": "behavior", "quote": "Request *request = data->waitingRequests_.front();\n\t\tif (!request->_d()->prepared_)\n\t\t\tbreak;", "part_id": "waiting-prepared"}, {"text": "doQueueRequest는 요청을 큐에 추가하고 시퀀스 번호를 지정한 뒤 `cancelled_`가 참이면 completeRequest를 호출하고 함수를 종료합니다. `cancelled_`가 거짓이면 queueRequestDevice를 호출하며, 그 반환값이 0이 아니면 cancelRequest를 호출합니다.", "evidence": ["dispatch"], "covers": ["journey"], "kind": "behavior", "quote": "void PipelineHandler::doQueueRequest(Request *request)\n{\n\tLIBCAMERA_TRACEPOINT(request_device_queue, request);\n\n\tCamera *camera = request->_d()->camera();\n\tCamera::Private *data = camera->_d();\n\tdata->queuedRequests_.push_back(request);\n\n\trequest->_d()->sequence_ = data->requestSequence_++;\n\n\tif (request->_d()->cancelled_) {\n\t\tcompleteRequest(request);\n\t\treturn;\n\t}\n\n\tint ret = queueRequestDevice(camera, request);\n\tif (ret)\n\t\tcancelRequest(request);\n}", "part_id": "dispatch"}, {"text": "함수의 이름은 `PipelineHandler::queueRequestDevice()`이며, 성공 시 0을 반환합니다.", "evidence": ["device-contract"], "covers": ["journey"], "kind": "behavior", "quote": "\\fn PipelineHandler::queueRequestDevice()\n * \\brief Queue a request to the device\n * \\param[in] camera The camera to queue the request to\n * \\param[in] request The request to queue\n *\n * This function queues a capture request to the device for processing. The\n * request contains a set of buffers associated with streams and a set of\n * parameters. The pipeline handler shall program the device to ensure that the\n * parameters will be applied to the frames captured in the buffers provided in\n * the request.\n *\n * \\context This function is called from the CameraManager thread.\n *\n * \\return 0 on success or a negative error code otherwise\n */", "part_id": "device-result"}, {"text": "오류 시 음수 오류 코드를 반환합니다.", "evidence": ["device-contract"], "covers": ["journey"], "kind": "behavior", "quote": "\\fn PipelineHandler::queueRequestDevice()\n * \\brief Queue a request to the device\n * \\param[in] camera The camera to queue the request to\n * \\param[in] request The request to queue\n *\n * This function queues a capture request to the device for processing. The\n * request contains a set of buffers associated with streams and a set of\n * parameters. The pipeline handler shall program the device to ensure that the\n * parameters will be applied to the frames captured in the buffers provided in\n * the request.\n *\n * \\context This function is called from the CameraManager thread.\n *\n * \\return 0 on success or a negative error code otherwise\n */", "part_id": "device-error"}, {"text": "파이프라인 핸들러는 요청의 버퍼 완료를 알리기 위해 `CameraManager` 스레드에서 completeBuffer()를 호출해야 합니다. 마지막 버퍼가 완료되어도 요청은 자동으로 완료되지 않으므로 completeRequest()로 명시적으로 완료해야 합니다.", "evidence": ["buffer-notice"], "covers": ["journey"], "kind": "behavior", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)", "part_id": "buffer-complete"}, {"text": "마지막 버퍼가 완료되어도 요청은 자동으로 완료되지 않으며, 파이프라인 핸들러는 completeRequest()를 명시적으로 호출하여 요청을 완료해야 합니다.", "evidence": ["request-duty"], "covers": ["journey"], "kind": "behavior", "quote": "The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().", "part_id": "request-duty"}, {"text": "completeRequest는 `queuedRequests_`가 빌 때까지 앞쪽 요청부터 확인합니다. 맨 앞 요청의 상태가 RequestPending이면 반복을 중단하므로 그 뒤의 요청은 확인하지 않습니다. 대기 중이 아닌 요청은 보류 중인 버퍼가 없음을 확인한 뒤 큐에서 제거하고 requestComplete()를 호출해 애플리케이션에 제출 순서대로 반환합니다.", "evidence": ["request-notice"], "covers": ["journey"], "kind": "behavior", "quote": "\\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}\n\n/**\n * \\brief Cancel request and signal its completion", "part_id": "request-complete"}, {"text": "이 분기는 요청의 상태가 `Request::RequestPending`인지 판단하며, 같으면 반복문을 종료합니다.", "evidence": ["completed-head"], "covers": ["journey"], "kind": "behavior", "quote": "if (req->status() == Request::RequestPending)\n\t\t\tbreak;", "part_id": "request-head"}], "resources": [{"text": "`Camera::createRequest()`가 반환한 요청의 소유권은 호출자에게 넘어가며, 호출자는 요청을 삭제할 책임이 있습니다. 호출자는 완료 핸들러에서 요청을 삭제하거나 `Request::reuse()`로 상태를 초기화한 뒤 재사용할 수 있습니다.", "evidence": ["create"], "covers": ["resources"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest(uint64_t cookie)", "part_id": "request-owner"}, {"text": "`Request::addBuffer()`는 요청에 버퍼의 참조를 저장합니다. 호출자는 요청 완료 콜백이 호출될 때까지 버퍼가 유효하게 유지되도록 해야 합니다.", "evidence": ["buffer-duty"], "covers": ["resources"], "kind": "behavior", "quote": "A reference to the buffer is stored in the request. The caller is responsible\n * for ensuring that the buffer will remain valid until the request complete\n * callback is called.", "part_id": "buffer-validity"}, {"text": "`Request::addBuffer`가 성공하면 유효한 `Fence`인 `fence`의 소유권이 대상 `FrameBuffer`인 `buffer`로 이동합니다.", "evidence": ["fence-move"], "covers": ["resources"], "kind": "behavior", "quote": "When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.", "part_id": "fence-transfer"}, {"text": "`Request::addBuffer()`가 실패하면 전달받은 `fence`의 소유권을 가져가지 않고 변경하지 않은 채 그대로 둡니다.", "evidence": ["fence-move"], "covers": ["resources"], "kind": "behavior", "quote": "When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.", "part_id": "fence-failure"}, {"text": "버퍼에 연결된 펜스가 신호되지 않으면 요청은 타임아웃 후 실패하고, 버퍼에는 펜스가 그대로 남습니다. 애플리케이션은 다른 요청에서 버퍼를 재사용하기 전에 `FrameBuffer::releaseFence()`로 펜스를 회수해야 합니다.", "evidence": ["fence-expiry"], "covers": ["resources"], "kind": "behavior", "quote": "If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request.", "part_id": "fence-timeout"}, {"text": "`Request::reuse()`는 `ReuseBuffers` 플래그가 설정된 경우 `bufferMap_`의 각 기존 버퍼에 대해 `buffer->_d()->setRequest(this)`를 호출하여 현재 요청을 연결합니다.", "evidence": ["reuse-link-call"], "covers": ["resources"], "kind": "behavior", "quote": "buffer->_d()->setRequest(this);", "part_id": "reset-buffer-link"}, {"text": "`Request::reuse()`는 `flags`에 `ReuseBuffers`가 설정되어 있으면 `bufferMap_`의 각 기존 버퍼에 이 요청을 설정한 다음 해당 버퍼를 `pending_`에 추가합니다.", "evidence": ["reuse-buffers"], "covers": ["resources"], "kind": "behavior", "quote": "if (flags & ReuseBuffers) {\n\t\tfor (const auto &[stream, buffer] : bufferMap_) {\n\t\t\tbuffer->_d()->setRequest(this);\n\t\t\t_d()->pending_.insert(buffer);\n\t\t}\n\t} else {\n\t\tbufferMap_.clear();\n\t}\n\n\tstatus_ = RequestPending;", "part_id": "reset-pending"}, {"text": "`Request::reuse()`는 `flags`에 `ReuseBuffers`가 없으면 `bufferMap_.clear()`를 호출해 `bufferMap_`을 비웁니다.", "evidence": ["reuse"], "covers": ["resources"], "kind": "behavior", "quote": "if (flags & ReuseBuffers) {\n\t\tfor (const auto &[stream, buffer] : bufferMap_) {\n\t\t\tbuffer->_d()->setRequest(this);\n\t\t\t_d()->pending_.insert(buffer);\n\t\t}\n\t} else {\n\t\tbufferMap_.clear();\n\t}", "part_id": "reset-buffer-clear"}, {"text": "`Request::reuse`의 이 대입문은 `status_`에 `RequestPending` 상태를 저장합니다.", "evidence": ["reuse-status"], "covers": ["resources"], "kind": "behavior", "quote": "status_ = RequestPending;", "part_id": "reset"}, {"text": "`Request::reuse`는 `controls_.clear()`를 호출해 `controls_`를 비웁니다.", "evidence": ["reuse-controls"], "covers": ["resources"], "kind": "behavior", "quote": "controls_.clear();", "part_id": "reset-controls"}, {"text": "`Request::reuse`는 `metadata_.clear()`를 호출해 `metadata_`를 비웁니다.", "evidence": ["reuse-metadata"], "covers": ["resources"], "kind": "behavior", "quote": "_d()->metadata_.clear();", "part_id": "reset-metadata"}, {"text": "`Request::ReuseBuffers` 플래그는 `addBuffer()`로 이전에 추가한 버퍼를 재사용하도록 유지합니다. 버퍼에 연결된 펜스는 재사용하지 않습니다.", "evidence": ["reuse-flags"], "covers": ["resources"], "kind": "behavior", "quote": "\\enum Request::ReuseFlag\n * Flags to control the behavior of Request::reuse()\n * \\var Request::Default\n * Don't reuse buffers\n * \\var Request::ReuseBuffers\n * Reuse the buffers that were previously added by addBuffer()\n *\n * \\note Fences associated with the buffers are not reused.\n *  This flag should not be used if fences are used.\n */", "part_id": "reuse-fences"}, {"text": "펜스를 사용하는 경우 `Request::ReuseBuffers` 플래그를 사용하지 않도록 권고합니다.", "evidence": ["reuse-advice"], "covers": ["resources"], "kind": "behavior", "quote": "This flag should not be used if fences are used.", "part_id": "reuse-advice"}, {"text": "`cancelRequest`는 요청을 취소한 뒤 `completeRequest`를 호출해 완료하며, `completeRequest`와 같은 규칙이 적용됩니다. 파이프라인 핸들러는 두 함수 중 호출한 함수가 반환된 후 해당 요청에 접근해서는 안 됩니다. 반환 후 요청은 더 이상 파이프라인 핸들러가 관리하지 않습니다.", "evidence": ["cancel-rules", "complete-access"], "covers": ["resources"], "kind": "behavior", "quote": "This function cancels and completes the request. The same rules as for\n * completeRequest() apply.", "part_id": "handler-access"}], "stopping": [{"text": "조사 계획으로 `Camera::stop` 호출 시 실제 카메라 상태와 `d->isRunning()`의 판단을 먼저 관찰합니다. 실행 중이 아니면 함수가 `0`을 반환하는지 확인하고, 실행 중이면 `d->isAccessAllowed(Private::CameraRunning)`의 반환값과 다음 분기를 확인합니다. 반환값이 음수이면 그 값을 반환하고, 그렇지 않으면 `CameraStopping`으로 상태를 바꾼 뒤 `PipelineHandler::stop`을 호출하고 대기 요청이 없다는 assertion을 거쳐 `CameraConfigured`로 상태를 바꿉니다.", "evidence": ["stop"], "covers": ["stopping"], "kind": "behavior", "quote": "/*\n\t * \\todo Make calling stop() when not in 'Running' part of the state\n\t * machine rather than take this shortcut\n\t */\n\tif (!d->isRunning())\n\t\treturn 0;", "part_id": "camera-entry"}, {"text": "조사 계획으로, `Camera::stop()`이 실행 중이고 접근 검사에서 음수 반환값이 나오지 않은 경우 `d->setState()`에 전달하는 `Private::CameraStopping` 값을 관찰합니다. 이 호출은 `PipelineHandler::stop`을 호출하기 전에 이루어집니다.", "evidence": ["stopping-call"], "covers": ["stopping"], "kind": "behavior", "quote": "d->setState(Private::CameraStopping);\n\n\td->pipe_->invokeMethod(&PipelineHandler::stop, ConnectionTypeBlocking,\n\t\t\t       this);", "part_id": "blocking"}, {"text": "조사 계획으로, `Camera::stop()`에서 실행 중이 아니면 `0`을 반환하고 `isAccessAllowed(Private::CameraRunning)`의 반환값이 음수이면 그 값을 반환하는 분기를 확인합니다. 두 분기를 통과하면 `Private::CameraStopping`으로 상태를 설정한 뒤 `ConnectionTypeBlocking`으로 `PipelineHandler::stop`을 호출하는 지점과 그 호출에서 복귀하는 지점을 관찰합니다.", "evidence": ["stopping-call"], "covers": ["stopping"], "kind": "behavior", "quote": "d->setState(Private::CameraStopping);\n\n\td->pipe_->invokeMethod(&PipelineHandler::stop, ConnectionTypeBlocking,\n\t\t\t       this);", "part_id": "blocking-call"}, {"text": "조사 계획으로 `PipelineHandler::stop`이 `waitingRequests_`를 지역 큐로 분리하는 지점과 `stopDevice`의 진입·복귀 지점을 관찰합니다. `stopDevice`에 진입했지만 복귀가 관찰되지 않으면 장치 내부에서 멎었는지 조사합니다. 복귀가 관찰되면 다음 반복문에서 지역 큐의 요청을 꺼내 취소하고 `doQueueRequest()`를 호출하는 흐름을 살펴봅니다.", "evidence": ["device-stop"], "covers": ["stopping"], "kind": "behavior", "quote": "\\brief Stop capturing from all running streams and cancel pending requests\n * \\param[in] camera The camera to stop\n *\n * This function stops capturing and processing requests immediately. All\n * pending requests are cancelled and complete immediately in an error state.\n *\n * \\context This function is called from the CameraManager thread.\n */\nvoid PipelineHandler::stop(Camera *camera)\n{\n\t/*\n\t * Take all waiting requests so that they are not requeued in response\n\t * to completeRequest() being called inside stopDevice(). Cancel them\n\t * after the device to keep them in order.\n\t */\n\tCamera::Private *data = camera->_d();\n\tstd::queue<Request *> waitingRequests;\n\twaitingRequests.swap(data->waitingRequests_);", "part_id": "device-entry"}, {"text": "조사 계획에서는 `PipelineHandler::stop()`이 대기 중인 요청을 취소한 뒤 호출하는 `doQueueRequest()`와 전달 인자인 `request`를 기록합니다.", "evidence": ["pending-requeue"], "covers": ["stopping"], "kind": "behavior", "quote": "doQueueRequest(request);", "part_id": "pending"}, {"text": "조사 계획은 `PipelineHandler::stop()`의 두 `ASSERT`에 도달했을 때 `data->queuedRequests_`와 `data->waitingRequests_`가 각각 비어 있는지 관찰하는 것입니다. 검사 지점은 `waitingRequests_`를 로컬 큐와 교환하고 `stopDevice(camera)`를 호출한 뒤, 로컬 큐의 요청을 차례로 취소하고 `doQueueRequest()`에 전달하는 반복문이 끝난 다음입니다. 두 검사는 `requestSequence_`를 0으로 설정하기 전에 실행됩니다.", "evidence": ["stop-assertions"], "covers": ["stopping"], "kind": "behavior", "quote": "ASSERT(data->queuedRequests_.empty());\n\tASSERT(data->waitingRequests_.empty());", "part_id": "queue-assertions"}, {"text": "파이프라인 핸들러는 `completeRequest()`를 `CameraManager` 스레드에서 호출해야 합니다. 조사 계획으로, 기존 호출의 실행 문맥과 `queuedRequests_`의 맨 앞 요청 상태를 확인합니다. 맨 앞 요청이 `Request::RequestPending`이면 루프가 중단되며, 그렇지 않으면 해당 요청을 큐에서 꺼내 `camera->requestComplete(req)`를 호출합니다. 이 호출 이후 애플리케이션 콜백이 실제로 실행되는지는 별도로 확인합니다.", "evidence": ["completion"], "covers": ["stopping"], "kind": "behavior", "quote": "/**\n * \\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();", "part_id": "completion"}, {"text": "`Camera::disconnect()`는 내부 처리 함수인 `_d()->disconnect()`를 호출합니다.", "evidence": ["disconnect-internal"], "covers": ["stopping"], "kind": "behavior", "quote": "_d()->disconnect();", "part_id": "disconnect"}, {"text": "`Camera::disconnect()`의 이 호출은 `disconnected` 신호를 발행합니다.", "evidence": ["disconnect-signal"], "covers": ["stopping"], "kind": "behavior", "quote": "disconnected.emit();", "part_id": "disconnect-signal"}, {"text": "`Camera::disconnect()`의 TODO는 카메라가 실행 중인 상태에서 연결이 끊어졌을 때 대기 중인 요청을 처리 대상으로 남겨 둡니다.", "evidence": ["disconnect-todo"], "covers": ["stopping"], "kind": "behavior", "quote": "\\todo Deal with pending requests if the camera is disconnected in a\n * running state.", "part_id": "disconnect-todo"}, {"text": "실행 중인 상태에서 카메라 연결이 끊어졌을 때 대기 중인 요청을 처리하는 TODO는 `Camera::disconnect()` 함수에 속합니다.", "evidence": ["disconnect-todo-owner"], "covers": ["stopping"], "kind": "behavior", "quote": "\\brief Notify camera disconnection\n *\n * This function is used to notify the camera instance that the underlying\n * hardware has been unplugged. In response to the disconnection the camera\n * instance notifies the application by emitting the #disconnected signal, and\n * ensures that all new calls to the application-facing Camera API return an\n * error immediately.\n *\n * \\todo Deal with pending requests if the camera is disconnected in a\n * running state.\n */\nvoid Camera::disconnect()", "part_id": "disconnect-todo-owner"}], "review": [{"text": "queueRequest의 반환값을 기록 항목으로 제안합니다. 성공 시 0, 오류 시 음수 오류 코드와 그 의미를 기록합니다: -ENODEV는 카메라 연결 해제, -EACCES는 카메라가 실행 중이 아님, -EXDEV는 요청이 해당 카메라에 속하지 않음, -EINVAL은 유효하지 않은 요청, -ENOMEM은 요청 처리에 사용할 버퍼 메모리가 없음을 나타냅니다.", "evidence": ["queue"], "covers": ["review"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();\n\n\tint ret = d->isAccessAllowed(Private::CameraRunning);\n\tif (ret < 0)\n\t\treturn ret;\n\n\t/* Requests can only be queued to the camera that created them. */\n\tif (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;\n\t}\n\n\tif (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}\n\n\t/* Make sure the Request has a valid control list. */\n\tif (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * The camera state may change until the end of the function. No locking\n\t * is however needed as PipelineHandler::queueRequest() will handle\n\t * this.\n\t */\n\n\tif (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;\n\t}\n\n\tfor (const auto &[stream, buffer] : request->buffers()) {\n\t\tif (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;\n\t\t}\n\t}\n\n\t/* Pre-process AeEnable. */\n\tpatchControlList(request->controls());\n\n\td->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);\n\n\treturn 0;\n}\n\n/**\n * \\brief Start capture from camera", "part_id": "submission-record"}, {"text": "대상 변수는 `status_`입니다. 기록 항목으로 `Request::reuse()`에서 대입 전후의 `status_` 값과 대입값 RequestPending을 제안합니다.", "evidence": ["record-status"], "covers": ["review"], "kind": "behavior", "quote": "status_ = RequestPending;", "part_id": "reuse-state-record"}, {"text": "clear 호출의 대상 변수인 `controls_`를 기록 항목으로 제안합니다.", "evidence": ["record-controls"], "covers": ["review"], "kind": "behavior", "quote": "controls_.clear();", "part_id": "reuse-data-record"}, {"text": "clear 호출의 대상 변수인 `metadata_`를 기록 항목으로 제안합니다.", "evidence": ["record-metadata"], "covers": ["review"], "kind": "behavior", "quote": "_d()->metadata_.clear();", "part_id": "reuse-metadata-record"}, {"text": "선두 요청의 상태 조회식 `req->status()`의 반환값을 기록 항목으로 제안합니다.", "evidence": ["record-head-status"], "covers": ["review"], "kind": "behavior", "quote": "if (req->status() == Request::RequestPending)\n\t\t\tbreak;", "part_id": "completion-record"}, {"text": "`PipelineHandler::stop`에서 stopDevice(camera) 호출 지점의 도달 여부를 기록하도록 제안합니다.", "evidence": ["record-device"], "covers": ["review"], "kind": "behavior", "quote": "stopDevice(camera);", "part_id": "stop-record"}, {"text": "조사 시 기록 항목으로 ASSERT가 검사하는 큐 식 `data->queuedRequests_`와 해당 큐가 비어 있는지 여부를 제안합니다.", "evidence": ["record-queued"], "covers": ["review"], "kind": "behavior", "quote": "ASSERT(data->queuedRequests_.empty());", "part_id": "stop-queued-record"}, {"text": "조사 계획의 기록 항목에 ASSERT가 검사하는 큐 식 `data->waitingRequests_`와 해당 큐가 비어 있는지 여부를 포함합니다.", "evidence": ["record-waiting"], "covers": ["review"], "kind": "behavior", "quote": "ASSERT(data->waitingRequests_.empty());", "part_id": "stop-waiting-record"}]}, "topic_inputs": {"journey": "300db49fa9b53c2eccbada23f97789707a3dd477cfd588722e736a087c3117c7", "resources": "24aee7b760d163a0ca521c2a80cf8e811689a1ed87993a7b29c08461b398df9e", "stopping": "d0e952df5ca7adc32c8ca6cc5f991d73c39e651d820db32465529eb7e047cf8c", "review": "d3feeca7eddfebfa7ef830a2f4107ed1e87f9720313dec44e70392a3a0eec2b3"}, "reused_topics": ["journey", "resources", "stopping", "review"], "replayed_units": [], "generated_topics": [], "topic_agents": {"journey": "cli/codex/gpt-6.1-terra", "resources": "cli/codex/gpt-6.1-terra", "stopping": "cli/codex/gpt-6.1-terra", "review": "cli/codex/gpt-6.1-terra"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "e0c429a5c80a01c34563ce00a616df89d8f75c735f8669bcbd1f75d84cce82a6", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "d4af3d834d8b1c99a6c9311612712a64112c30fa4621b375904d172f361285b8", "design_contracts": "b293a0012d1fcb6340fcaf94d481cf900212686978bc96fb118a0cdaddf3c091", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "65c405dc11cd8c43e2bce26ffbd96a47f37a784df59a4969be589ed8318f7be0", "answer_contracts": "1e0d24e0cf26ded53ecec2e5a6fbc51836bac6e17530318a9fa7cffaa936c00b", "design_response": "ce93f02b72371ed40f1b1124e78cef512baea31aa2df988db0c689f8169f783c", "design_validation": "608d2eed51e4ad5d5693fbc9b7d669ae1ba8e503f6736b62ea1ca068ce706556"}, "validation_model": "5ddbcbf91a6b516c4f71596d64b6286295bfd0cac771a7ca749ca78e25a2d752", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "f8fd5a3d8041c23fc68b93ff32b8727e98393383b5099032eb00ad0013e7611c"}, "reuse_lineage": {"source_commit": "e117198c015057761bb0bbaa85f963c41ce412d7", "body_sha256": "7279273e2e540c746b32ec5103dc018687b30352fa02c4dcae144c6ffcf9c7d6", "topics": ["journey", "resources", "stopping", "review"], "validation": "current source, contract and editorial checks; human review pending"}, "body_sha256": "7279273e2e540c746b32ec5103dc018687b30352fa02c4dcae144c6ffcf9c7d6"}
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

createRequest의 반환 타입은 `std::unique_ptr<Request>`이며, 새로 생성된 빈 `Request` 객체를 가리킵니다. 오류가 발생하면 nullptr을 반환합니다. `Request::addBuffer()`는 버퍼가 속한 스트림을 지정하여 해당 버퍼를 요청에 추가합니다. `src/libcamera/camera.cpp:1243`, `src/libcamera/request.cpp:442`

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

`Camera::queueRequest`가 0을 반환하면 요청이 성공적으로 큐에 등록되었음을 의미합니다. 큐에 등록된 요청의 완료는 이후 requestCompleted 신호로 알립니다. `waitingRequests_`는 준비를 기다리는 요청을 순서대로 보관하며, 맨 앞의 요청이 준비되지 않으면 후속 요청의 장치 전달을 멈춥니다. `maxQueuedRequestsDevice_`는 장치에 전달된 요청의 최대 개수를 정하며, 장치 큐의 요청 수가 이 값에 도달하면 추가 전달을 멈춥니다. `src/libcamera/camera.cpp:1308`, `src/libcamera/pipeline_handler.cpp:428`

선두 요청의 준비 여부는 `prepared_` 멤버에서 읽으며, 그 값이 거짓이면 반복문을 종료합니다. doQueueRequest는 요청을 큐에 추가하고 시퀀스 번호를 지정한 뒤 `cancelled_`가 참이면 completeRequest를 호출하고 함수를 종료합니다. `cancelled_`가 거짓이면 queueRequestDevice를 호출하며, 그 반환값이 0이 아니면 cancelRequest를 호출합니다. 함수의 이름은 `PipelineHandler::queueRequestDevice()`이며, 성공 시 0을 반환합니다. `src/libcamera/pipeline_handler.cpp:516`, `src/libcamera/pipeline_handler.cpp:483`, `src/libcamera/pipeline_handler.cpp:530`

오류 시 음수 오류 코드를 반환합니다. 파이프라인 핸들러는 요청의 버퍼 완료를 알리기 위해 `CameraManager` 스레드에서 completeBuffer()를 호출해야 합니다. 마지막 버퍼가 완료되어도 요청은 자동으로 완료되지 않으므로 completeRequest()로 명시적으로 완료해야 합니다. 마지막 버퍼가 완료되어도 요청은 자동으로 완료되지 않으며, 파이프라인 핸들러는 completeRequest()를 명시적으로 호출하여 요청을 완료해야 합니다. `src/libcamera/pipeline_handler.cpp:530`, `src/libcamera/pipeline_handler.cpp:547`, `src/libcamera/pipeline_handler.cpp:553`

completeRequest는 `queuedRequests_`가 빌 때까지 앞쪽 요청부터 확인합니다. 맨 앞 요청의 상태가 RequestPending이면 반복을 중단하므로 그 뒤의 요청은 확인하지 않습니다. 대기 중이 아닌 요청은 보류 중인 버퍼가 없음을 확인한 뒤 큐에서 제거하고 requestComplete()를 호출해 애플리케이션에 제출 순서대로 반환합니다. 이 분기는 요청의 상태가 `Request::RequestPending`인지 판단하며, 같으면 반복문을 종료합니다. `src/libcamera/pipeline_handler.cpp:571`, `src/libcamera/pipeline_handler.cpp:594`

근거 원문: [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) · [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) · [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) · [src/libcamera/pipeline_handler.cpp:483](#source-7348e9b4af985eb2) · [src/libcamera/pipeline_handler.cpp:530](#source-c05f8214908fe4fe) · [src/libcamera/pipeline_handler.cpp:547](#source-ab8710f8a8a7905d) · [src/libcamera/pipeline_handler.cpp:571](#source-236c920e906cb6fd) · [src/libcamera/pipeline_handler.cpp:516](#source-a637b7daf9acb7ac) · [src/libcamera/pipeline_handler.cpp:553](#source-5b0ae08604dff588) · [src/libcamera/pipeline_handler.cpp:594](#source-bae861ceef5e8406)

## 요청·버퍼·fence의 수명

`Camera::createRequest()`가 반환한 요청의 소유권은 호출자에게 넘어가며, 호출자는 요청을 삭제할 책임이 있습니다. 호출자는 완료 핸들러에서 요청을 삭제하거나 `Request::reuse()`로 상태를 초기화한 뒤 재사용할 수 있습니다. `Request::addBuffer()`는 요청에 버퍼의 참조를 저장합니다. 호출자는 요청 완료 콜백이 호출될 때까지 버퍼가 유효하게 유지되도록 해야 합니다. `src/libcamera/camera.cpp:1243`, `src/libcamera/request.cpp:447`

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

`Request::addBuffer`가 성공하면 유효한 `Fence`인 `fence`의 소유권이 대상 `FrameBuffer`인 `buffer`로 이동합니다. `Request::addBuffer()`가 실패하면 전달받은 `fence`의 소유권을 가져가지 않고 변경하지 않은 채 그대로 둡니다. 버퍼에 연결된 펜스가 신호되지 않으면 요청은 타임아웃 후 실패하고, 버퍼에는 펜스가 그대로 남습니다. 애플리케이션은 다른 요청에서 버퍼를 재사용하기 전에 `FrameBuffer::releaseFence()`로 펜스를 회수해야 합니다. `src/libcamera/request.cpp:456`, `src/libcamera/request.cpp:462`

`Request::reuse()`는 `ReuseBuffers` 플래그가 설정된 경우 `bufferMap_`의 각 기존 버퍼에 대해 `buffer->_d()->setRequest(this)`를 호출하여 현재 요청을 연결합니다. `Request::reuse()`는 `flags`에 `ReuseBuffers`가 설정되어 있으면 `bufferMap_`의 각 기존 버퍼에 이 요청을 설정한 다음 해당 버퍼를 `pending_`에 추가합니다. `Request::reuse()`는 `flags`에 `ReuseBuffers`가 없으면 `bufferMap_.clear()`를 호출해 `bufferMap_`을 비웁니다. `Request::reuse`의 이 대입문은 `status_`에 `RequestPending` 상태를 저장합니다. `src/libcamera/request.cpp:393`, `src/libcamera/request.cpp:391`, `src/libcamera/request.cpp:376`, `src/libcamera/request.cpp:400`

`Request::reuse`는 `controls_.clear()`를 호출해 `controls_`를 비웁니다. `Request::reuse`는 `metadata_.clear()`를 호출해 `metadata_`를 비웁니다. `Request::ReuseBuffers` 플래그는 `addBuffer()`로 이전에 추가한 버퍼를 재사용하도록 유지합니다. 버퍼에 연결된 펜스는 재사용하지 않습니다. `src/libcamera/request.cpp:402`, `src/libcamera/request.cpp:403`, `src/libcamera/request.cpp:326`

펜스를 사용하는 경우 `Request::ReuseBuffers` 플래그를 사용하지 않도록 권고합니다. `cancelRequest`는 요청을 취소한 뒤 `completeRequest`를 호출해 완료하며, `completeRequest`와 같은 규칙이 적용됩니다. 파이프라인 핸들러는 두 함수 중 호출한 함수가 반환된 후 해당 요청에 접근해서는 안 됩니다. 반환 후 요청은 더 이상 파이프라인 핸들러가 관리하지 않습니다. `src/libcamera/request.cpp:334`, `src/libcamera/pipeline_handler.cpp:610`, `src/libcamera/pipeline_handler.cpp:575`

근거 원문: [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) · [src/libcamera/request.cpp:376](#source-38494771cb29cc8c) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) · [src/libcamera/request.cpp:326](#source-447804db33308244) · [src/libcamera/request.cpp:456](#source-86a8d784a8348122) · [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) · [src/libcamera/request.cpp:400](#source-a98823fa5ec440a2) · [src/libcamera/request.cpp:402](#source-c8638489aa83cfd1) · [src/libcamera/request.cpp:403](#source-47569737e131b31a) · [src/libcamera/request.cpp:391](#source-e41b7fa688c1de2e) · [src/libcamera/request.cpp:447](#source-4cdce80c57526221) · [src/libcamera/pipeline_handler.cpp:575](#source-d93a02e9220fa760) · [src/libcamera/pipeline_handler.cpp:610](#source-52fb58c8956b1a91) · [src/libcamera/request.cpp:334](#source-d9944a69f2dd6758) · [src/libcamera/request.cpp:393](#source-bf1ee390b8473e16) · [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1)

## 정지와 연결 해제를 구분하기

조사 계획으로 `Camera::stop` 호출 시 실제 카메라 상태와 `d->isRunning()`의 판단을 먼저 관찰합니다. 실행 중이 아니면 함수가 `0`을 반환하는지 확인하고, 실행 중이면 `d->isAccessAllowed(Private::CameraRunning)`의 반환값과 다음 분기를 확인합니다. 반환값이 음수이면 그 값을 반환하고, 그렇지 않으면 `CameraStopping`으로 상태를 바꾼 뒤 `PipelineHandler::stop`을 호출하고 대기 요청이 없다는 assertion을 거쳐 `CameraConfigured`로 상태를 바꿉니다. `src/libcamera/camera.cpp:1431`

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

조사 계획으로, `Camera::stop()`이 실행 중이고 접근 검사에서 음수 반환값이 나오지 않은 경우 `d->setState()`에 전달하는 `Private::CameraStopping` 값을 관찰합니다. 이 호출은 `PipelineHandler::stop`을 호출하기 전에 이루어집니다. 조사 계획으로, `Camera::stop()`에서 실행 중이 아니면 `0`을 반환하고 `isAccessAllowed(Private::CameraRunning)`의 반환값이 음수이면 그 값을 반환하는 분기를 확인합니다. 두 분기를 통과하면 `Private::CameraStopping`으로 상태를 설정한 뒤 `ConnectionTypeBlocking`으로 `PipelineHandler::stop`을 호출하는 지점과 그 호출에서 복귀하는 지점을 관찰합니다. `src/libcamera/camera.cpp:1462`

조사 계획으로 `PipelineHandler::stop`이 `waitingRequests_`를 지역 큐로 분리하는 지점과 `stopDevice`의 진입·복귀 지점을 관찰합니다. `stopDevice`에 진입했지만 복귀가 관찰되지 않으면 장치 내부에서 멎었는지 조사합니다. 복귀가 관찰되면 다음 반복문에서 지역 큐의 요청을 꺼내 취소하고 `doQueueRequest()`를 호출하는 흐름을 살펴봅니다. 조사 계획에서는 `PipelineHandler::stop()`이 대기 중인 요청을 취소한 뒤 호출하는 `doQueueRequest()`와 전달 인자인 `request`를 기록합니다. `src/libcamera/pipeline_handler.cpp:359`, `src/libcamera/pipeline_handler.cpp:394`

조사 계획은 `PipelineHandler::stop()`의 두 `ASSERT`에 도달했을 때 `data->queuedRequests_`와 `data->waitingRequests_`가 각각 비어 있는지 관찰하는 것입니다. 검사 지점은 `waitingRequests_`를 로컬 큐와 교환하고 `stopDevice(camera)`를 호출한 뒤, 로컬 큐의 요청을 차례로 취소하고 `doQueueRequest()`에 전달하는 반복문이 끝난 다음입니다. 두 검사는 `requestSequence_`를 0으로 설정하기 전에 실행됩니다. `src/libcamera/pipeline_handler.cpp:398`

파이프라인 핸들러는 `completeRequest()`를 `CameraManager` 스레드에서 호출해야 합니다. 조사 계획으로, 기존 호출의 실행 문맥과 `queuedRequests_`의 맨 앞 요청 상태를 확인합니다. 맨 앞 요청이 `Request::RequestPending`이면 루프가 중단되며, 그렇지 않으면 해당 요청을 큐에서 꺼내 `camera->requestComplete(req)`를 호출합니다. 이 호출 이후 애플리케이션 콜백이 실제로 실행되는지는 별도로 확인합니다. `src/libcamera/pipeline_handler.cpp:547`

`Camera::disconnect()`는 내부 처리 함수인 `_d()->disconnect()`를 호출합니다. `Camera::disconnect()`의 이 호출은 `disconnected` 신호를 발행합니다. `Camera::disconnect()`의 TODO는 카메라가 실행 중인 상태에서 연결이 끊어졌을 때 대기 중인 요청을 처리 대상으로 남겨 둡니다. 실행 중인 상태에서 카메라 연결이 끊어졌을 때 대기 중인 요청을 처리하는 TODO는 `Camera::disconnect()` 함수에 속합니다. `src/libcamera/camera.cpp:959`, `src/libcamera/camera.cpp:960`, `src/libcamera/camera.cpp:952`, `src/libcamera/camera.cpp:944`

근거 원문: [src/libcamera/camera.cpp:1431](#source-e09324743def3f09) · [src/libcamera/pipeline_handler.cpp:359](#source-eefd1bbecb1aad0a) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) · [src/libcamera/camera.cpp:1462](#source-6191f91df6cbffa2) · [src/libcamera/pipeline_handler.cpp:398](#source-5e7914238ff81605) · [src/libcamera/camera.cpp:952](#source-1d583253fc11ef1c) · [src/libcamera/pipeline_handler.cpp:394](#source-fd5daba4aa44adfd) · [src/libcamera/camera.cpp:959](#source-56494d0aedf70c2d) · [src/libcamera/camera.cpp:960](#source-7d48ce2e18c8877c) · [src/libcamera/camera.cpp:944](#source-2758e9ddd31ad41d) · [src/libcamera/camera.cpp:944](#source-839140c350119dd1)

## 변경 검토와 실행 확인

queueRequest의 반환값을 기록 항목으로 제안합니다. 성공 시 0, 오류 시 음수 오류 코드와 그 의미를 기록합니다: -ENODEV는 카메라 연결 해제, -EACCES는 카메라가 실행 중이 아님, -EXDEV는 요청이 해당 카메라에 속하지 않음, -EINVAL은 유효하지 않은 요청, -ENOMEM은 요청 처리에 사용할 버퍼 메모리가 없음을 나타냅니다. 대상 변수는 `status_`입니다. 기록 항목으로 `Request::reuse()`에서 대입 전후의 `status_` 값과 대입값 RequestPending을 제안합니다. `src/libcamera/camera.cpp:1308`, `src/libcamera/request.cpp:400`

clear 호출의 대상 변수인 `controls_`를 기록 항목으로 제안합니다. clear 호출의 대상 변수인 `metadata_`를 기록 항목으로 제안합니다. 선두 요청의 상태 조회식 `req->status()`의 반환값을 기록 항목으로 제안합니다. `PipelineHandler::stop`에서 stopDevice(camera) 호출 지점의 도달 여부를 기록하도록 제안합니다. `src/libcamera/request.cpp:402`, `src/libcamera/request.cpp:403`, `src/libcamera/pipeline_handler.cpp:594`, `src/libcamera/pipeline_handler.cpp:379`

조사 시 기록 항목으로 ASSERT가 검사하는 큐 식 `data->queuedRequests_`와 해당 큐가 비어 있는지 여부를 제안합니다. 조사 계획의 기록 항목에 ASSERT가 검사하는 큐 식 `data->waitingRequests_`와 해당 큐가 비어 있는지 여부를 포함합니다. `src/libcamera/pipeline_handler.cpp:398`, `src/libcamera/pipeline_handler.cpp:399`

근거 원문: [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/request.cpp:400](#source-a98823fa5ec440a2) · [src/libcamera/request.cpp:402](#source-c8638489aa83cfd1) · [src/libcamera/request.cpp:403](#source-47569737e131b31a) · [src/libcamera/pipeline_handler.cpp:594](#source-bae861ceef5e8406) · [src/libcamera/pipeline_handler.cpp:379](#source-1bc6b7c1710b9de4) · [src/libcamera/pipeline_handler.cpp:398](#source-22bd3eab4afc5389) · [src/libcamera/pipeline_handler.cpp:399](#source-8a8099ed4a95531d)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 제출 성공 이후의 대기 조건과 완료 책임은 무엇입니까? | [제출에서 완료까지](#제출에서-완료까지) | 코드 근거와 설명 연결 |
    | 어떤 자원을 누가 유지하고 완료 후 무엇을 초기화해야 합니까? | [요청·버퍼·fence의 수명](#요청버퍼fence의-수명) | 코드 근거와 설명 연결 |
    | 정지 중 요청 반환과 연결 해제의 보장 범위는 어떻게 다릅니까? | [정지와 연결 해제를 구분하기](#정지와-연결-해제를-구분하기) | 코드 근거와 설명 연결 |
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
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `e117198c01`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-29 · 사람 검토 전

다음 단계: [구성과 요청 오류 조사](request-diagnosis.md)
