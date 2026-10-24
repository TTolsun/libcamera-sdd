---
generated_at: 2026-10-24T08:53:45+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: request-lifecycle
generation_method: facts-and-llm
evidence_fingerprint: 8d5b5eb1cd473d156ee2e8725b8ea5f676efe1188706721dfc9e737d20e2653d
semantic_review: human-review-required
agent: response-bundle/codex-session
generated_design: {"schema": 1, "input_fingerprint": "8d5b5eb1cd473d156ee2e8725b8ea5f676efe1188706721dfc9e737d20e2653d", "answers": {"journey": [{"text": "요청은 `Camera::createRequest()`에서 빈 객체로 시작합니다. 애플리케이션이 버퍼와 제어 값을 채우며, 요청의 소유권도 호출자에게 있습니다. 생성은 `Configured`와 `Running` 상태에서 가능합니다.", "covers": ["journey"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest(uint64_t cookie)", "evidence": ["create"]}, {"text": "`Request::addBuffer()`는 스트림과 버퍼의 참조를 연결합니다. 한 요청에는 스트림마다 버퍼 하나만 넣을 수 있고, 버퍼는 요청 완료 콜백까지 유효해야 합니다.", "covers": ["journey"], "kind": "behavior", "quote": "\\brief Add a FrameBuffer with its associated Stream to the Request\n * \\param[in] stream The stream the buffer belongs to\n * \\param[in] buffer The FrameBuffer to add to the request\n * \\param[in] fence The optional fence\n *\n * A reference to the buffer is stored in the request. The caller is responsible\n * for ensuring that the buffer will remain valid until the request complete\n * callback is called.\n *\n * A request can only contain one buffer per stream. If a buffer has already\n * been added to the request for the same stream, this function returns -EEXIST.\n *\n * A Fence can be optionally associated with the \\a buffer.\n *\n * When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.\n *\n * If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request. Attempting to add a buffer that still\n * contains a fence to a request will result in this function returning -EEXIST.\n *\n * \\sa FrameBuffer::releaseFence()\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -EEXIST The request already contains a buffer for the stream\n *  or the buffer still references a fence\n * \\retval -EINVAL The buffer does not reference a valid Stream\n */\nint Request::addBuffer(const Stream *stream, FrameBuffer *buffer,", "evidence": ["buffer"]}, {"text": "`Camera::queueRequest()`는 실행 상태와 요청 내용을 검사한 뒤 `ConnectionTypeQueued`로 파이프라인 호출을 예약합니다. 0은 이 제출 단계의 성공이며, 프레임 처리가 끝났다는 의미는 아닙니다. 완료는 `requestCompleted` 신호로 구분합니다.", "covers": ["journey"], "kind": "behavior", "quote": "d->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);", "evidence": ["queue"]}, {"text": "파이프라인은 요청을 대기 큐에 넣어 준비시킨 뒤 맨 앞부터 장치로 보냅니다. 맨 앞 요청이 아직 준비되지 않았거나 장치 큐 크기가 한도와 같으면 제출 순회를 멈춥니다. `queueRequestDevice()` 구현은 요청의 파라미터가 해당 버퍼의 프레임에 적용되도록 장치를 설정합니다.", "covers": ["journey"], "kind": "behavior", "quote": "/**\n * \\brief Queue prepared requests to the device\n *\n * Iterate the list of waiting requests and queue them to the device one\n * by one if they have been prepared.\n */\nvoid PipelineHandler::doQueueRequests(Camera *camera)\n{\n\tCamera::Private *data = camera->_d();\n\twhile (!data->waitingRequests_.empty()) {\n\t\tif (data->queuedRequests_.size() == maxQueuedRequestsDevice_)\n\t\t\tbreak;", "evidence": ["device-queue"]}, {"text": "버퍼 완료는 `completeBuffer()`로 알리지만, 마지막 버퍼가 끝나도 요청이 자동으로 완료되지는 않습니다. 파이프라인이 `completeRequest()`를 명시적으로 호출해야 하며, 공통 코드는 요청을 애플리케이션에 제출 순서대로 돌려줍니다.", "covers": ["journey"], "kind": "behavior", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}", "evidence": ["completion"]}, {"text": "파이프라인의 완료 함수는 `CameraManager` 스레드에서 실행하는 계약을 가집니다. 이 계약만으로 애플리케이션 콜백의 실행 스레드까지 정할 수는 없으며, 신호 연결 방식은 별도로 확인해야 합니다.", "covers": ["journey"], "kind": "behavior", "quote": "/**\n * \\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();", "evidence": ["completion"]}], "resources": [{"text": "요청 객체는 애플리케이션이 소유합니다. 완료 핸들러에서 파괴할 수 있고, 계속 사용하려면 새로 큐에 넣기 전에 `reuse()`로 초기화합니다.", "covers": ["resources"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest(uint64_t cookie)", "evidence": ["create"]}, {"text": "`reuse()`는 요청을 `RequestPending`으로 돌리고 controls와 metadata를 비웁니다. `ReuseBuffers`가 있으면 기존 버퍼를 다시 미완료 집합에 넣으며, 없으면 버퍼 맵을 비웁니다. 따라서 재사용 시 제어 값과 버퍼를 어떤 방식으로 다시 채우는지 구분해야 합니다.", "covers": ["resources"], "kind": "behavior", "quote": "if (flags & ReuseBuffers) {\n\t\tfor (const auto &[stream, buffer] : bufferMap_) {\n\t\t\tbuffer->_d()->setRequest(this);\n\t\t\t_d()->pending_.insert(buffer);\n\t\t}\n\t} else {\n\t\tbufferMap_.clear();\n\t}", "evidence": ["reuse"]}, {"text": "버퍼는 요청이 참조하므로 요청 완료 콜백까지 유효해야 합니다. fence 소유권은 `addBuffer()`가 성공했을 때 버퍼로 이동합니다. fence 대기 타임아웃 뒤에는 버퍼에 fence가 남으므로, 다른 요청에 추가하기 전에 `releaseFence()`로 회수해야 합니다.", "covers": ["resources"], "kind": "behavior", "quote": "\\brief Add a FrameBuffer with its associated Stream to the Request\n * \\param[in] stream The stream the buffer belongs to\n * \\param[in] buffer The FrameBuffer to add to the request\n * \\param[in] fence The optional fence\n *\n * A reference to the buffer is stored in the request. The caller is responsible\n * for ensuring that the buffer will remain valid until the request complete\n * callback is called.\n *\n * A request can only contain one buffer per stream. If a buffer has already\n * been added to the request for the same stream, this function returns -EEXIST.\n *\n * A Fence can be optionally associated with the \\a buffer.\n *\n * When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.\n *\n * If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request. Attempting to add a buffer that still\n * contains a fence to a request will result in this function returning -EEXIST.\n *\n * \\sa FrameBuffer::releaseFence()\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -EEXIST The request already contains a buffer for the stream\n *  or the buffer still references a fence\n * \\retval -EINVAL The buffer does not reference a valid Stream\n */\nint Request::addBuffer(const Stream *stream, FrameBuffer *buffer,", "evidence": ["buffer"]}, {"text": "`ReuseBuffers`는 fence를 재사용하지 않습니다. 소스는 fence를 사용하는 경우 이 플래그를 사용하지 말라고 명시하므로, 버퍼 재사용과 fence 수명을 같은 동작으로 취급하면 안 됩니다.", "covers": ["resources"], "kind": "behavior", "quote": "\\enum Request::ReuseFlag\n * Flags to control the behavior of Request::reuse()\n * \\var Request::Default\n * Don't reuse buffers\n * \\var Request::ReuseBuffers\n * Reuse the buffers that were previously added by addBuffer()\n *\n * \\note Fences associated with the buffers are not reused.\n *  This flag should not be used if fences are used.\n */", "evidence": ["reuse-flags"]}, {"text": "파이프라인 핸들러는 `completeRequest()`가 반환한 뒤 해당 요청에 접근하면 안 됩니다. 요청을 취소하고 완료까지 처리하는 `cancelRequest()`에도 같은 규칙이 적용됩니다.", "covers": ["resources"], "kind": "behavior", "quote": "/**\n * \\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();", "evidence": ["completion"]}], "diagnosis": [{"text": "버퍼 연결 단계의 `-EEXIST`는 같은 스트림에 이미 버퍼가 있거나, 추가하려는 버퍼에 fence가 남은 경우를 구분해야 합니다. 이는 카메라의 요청 제출 오류와 다른 단계에서 발생합니다.", "covers": ["diagnosis"], "kind": "behavior", "quote": "\\brief Add a FrameBuffer with its associated Stream to the Request\n * \\param[in] stream The stream the buffer belongs to\n * \\param[in] buffer The FrameBuffer to add to the request\n * \\param[in] fence The optional fence\n *\n * A reference to the buffer is stored in the request. The caller is responsible\n * for ensuring that the buffer will remain valid until the request complete\n * callback is called.\n *\n * A request can only contain one buffer per stream. If a buffer has already\n * been added to the request for the same stream, this function returns -EEXIST.\n *\n * A Fence can be optionally associated with the \\a buffer.\n *\n * When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.\n *\n * If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request. Attempting to add a buffer that still\n * contains a fence to a request will result in this function returning -EEXIST.\n *\n * \\sa FrameBuffer::releaseFence()\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -EEXIST The request already contains a buffer for the stream\n *  or the buffer still references a fence\n * \\retval -EINVAL The buffer does not reference a valid Stream\n */\nint Request::addBuffer(const Stream *stream, FrameBuffer *buffer,", "evidence": ["buffer"]}, {"text": "`Camera::queueRequest()`에서 `-ENODEV`는 연결 해제, `-EACCES`는 실행 중이 아닌 상태, `-EXDEV`는 다른 카메라가 만든 요청을 가리킵니다. `-EINVAL`은 요청 내용 검사에서 발생하므로 요청 상태와 버퍼·제어 정보를 이어서 확인하는 기준이 됩니다.", "covers": ["diagnosis"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();", "evidence": ["queue"]}, {"text": "구현의 `-EINVAL` 조건은 `RequestPending`이 아닌 요청, 카메라와 다른 controls 정보 맵, 빈 버퍼 목록, 활성 스트림에 속하지 않는 버퍼입니다. 단순히 제출 실패로 묶지 않고 어느 조건에서 반환했는지 구분할 수 있습니다.", "covers": ["diagnosis"], "kind": "behavior", "quote": "if (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}", "evidence": ["queue"]}, {"text": "제출이 성공한 뒤의 정체는 준비 대기와 장치 전달을 나눠 봅니다. 대기 큐 앞 요청의 `prepared_`가 거짓이면 뒤의 요청도 진행하지 않고, 장치 큐가 한도에 도달해도 순회가 멈춥니다. `queueRequestDevice()`가 오류를 반환한 요청은 취소 경로로 갑니다.", "covers": ["diagnosis"], "kind": "behavior", "quote": "Request *request = data->waitingRequests_.front();\n\t\tif (!request->_d()->prepared_)\n\t\t\tbreak;", "evidence": ["device-queue"]}, {"text": "버퍼가 끝났더라도 명시적인 요청 완료가 빠지면 완료 경로가 끝나지 않습니다. 또한 `completeRequest()`는 장치 큐 앞 요청이 `RequestPending`이면 반환 순회를 멈추므로, 뒤 요청의 완료와 애플리케이션 반환 시점도 구분해야 합니다.", "covers": ["diagnosis"], "kind": "behavior", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;", "evidence": ["completion"]}], "stopping": [{"text": "`Camera::stop()`은 실행 중이 아니면 실제 구현에서 0을 반환합니다. 실행 중이면 접근 검사 뒤 `Stopping`으로 바꾸고 파이프라인 정지를 blocking 방식으로 호출합니다. 미완료 요청이 없는지 확인한 다음 `Configured`로 돌아갑니다.", "covers": ["stopping"], "kind": "behavior", "quote": "/*\n\t * \\todo Make calling stop() when not in 'Running' part of the state\n\t * machine rather than take this shortcut\n\t */\n\tif (!d->isRunning())\n\t\treturn 0;", "evidence": ["stop"]}, {"text": "`PipelineHandler::stop()`은 대기 큐를 먼저 분리하고 `stopDevice()`를 호출합니다. 장치 정지 중 완료 통지가 발생해도 분리한 요청이 다시 제출되지 않게 하며, 장치 쪽 완료 이후에 대기 요청을 취소해 순서를 유지합니다.", "covers": ["stopping"], "kind": "behavior", "quote": "\\brief Stop capturing from all running streams and cancel pending requests\n * \\param[in] camera The camera to stop\n *\n * This function stops capturing and processing requests immediately. All\n * pending requests are cancelled and complete immediately in an error state.\n *\n * \\context This function is called from the CameraManager thread.\n */\nvoid PipelineHandler::stop(Camera *camera)\n{\n\t/*\n\t * Take all waiting requests so that they are not requeued in response\n\t * to completeRequest() being called inside stopDevice(). Cancel them\n\t * after the device to keep them in order.\n\t */\n\tCamera::Private *data = camera->_d();\n\tstd::queue<Request *> waitingRequests;\n\twaitingRequests.swap(data->waitingRequests_);", "evidence": ["device-stop"]}, {"text": "분리한 요청은 취소 표시 후 `doQueueRequest()`에 넣어 순번을 받고 공통 완료 경로를 거칩니다. 마지막에는 두 큐가 비었는지 검사하고 순번을 초기화합니다. `stopDevice()`의 계약은 미완료 요청을 즉시 오류 상태로 취소·완료하는 것입니다.", "covers": ["stopping"], "kind": "behavior", "quote": "/*\n\t\t * Cancel all requests by marking them as cancelled and calling\n\t\t * doQueueRequest() instead of cancelRequest(). This ensures\n\t\t * that the requests get a sequence number and are temporarily\n\t\t * added to queuedRequests_ so they can be properly completed in\n\t\t * completeRequest().\n\t\t */\n\t\trequest->_d()->cancel();\n\t\tdoQueueRequest(request);\n\t}", "evidence": ["device-stop"]}, {"text": "정상 `stop()`은 미완료 요청의 동기 취소·완료를 명시하지만, 연결 해제 경로에는 실행 중 대기 요청 처리가 TODO로 남아 있습니다. 따라서 `disconnect()` 알림을 정상 정지 완료와 동일하게 해석하면 안 됩니다.", "covers": ["stopping"], "kind": "behavior", "quote": "\\brief Notify camera disconnection\n *\n * This function is used to notify the camera instance that the underlying\n * hardware has been unplugged. In response to the disconnection the camera\n * instance notifies the application by emitting the #disconnected signal, and\n * ensures that all new calls to the application-facing Camera API return an\n * error immediately.\n *\n * \\todo Deal with pending requests if the camera is disconnected in a\n * running state.\n */\nvoid Camera::disconnect()\n{\n\tLOG(Camera, Debug) << \"Disconnecting camera \" << id();", "evidence": ["notification"]}, {"text": "정지 함수의 동기 완료 계약만으로 별도 스레드에 전달된 애플리케이션 콜백의 후속 작업까지 모두 끝났다고 증명할 수는 없습니다. 콜백 연결과 애플리케이션 작업 종료는 별도 확인 대상입니다.", "covers": ["stopping"], "kind": "limitation", "quote": "\\brief Stop capture from camera\n *\n * This function stops capturing and processing requests immediately. All\n * pending requests are cancelled and complete synchronously in an error state.\n *\n * \\context This function may be called in any camera state as defined in \\ref\n * camera_operation, and shall be synchronized by the caller with other\n * functions that affect the camera state. If called when the camera isn't\n * running, it is a no-op.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so can't be stopped\n */\nint Camera::stop()\n{\n\tPrivate *const d = _d();", "evidence": ["stop"]}], "review": [{"text": "소스에서 구분되는 첫 경계는 제출 성공과 요청 완료입니다. `queueRequest()`는 파이프라인 호출을 예약하고 반환하므로, 성공 반환을 완료 통지 대신 사용하면 안 됩니다.", "covers": ["review"], "kind": "behavior", "quote": "d->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);", "evidence": ["queue"]}, {"text": "완료 경로에는 명시적인 `completeRequest()` 호출과 제출 순서 보존이라는 두 조건이 있습니다. 앞 요청이 `RequestPending`이면 뒤의 완료 요청을 바로 반환하지 않으며, 버퍼 완료만으로 요청 완료 책임이 사라지지 않습니다.", "covers": ["review"], "kind": "behavior", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;", "evidence": ["completion"]}, {"text": "`reuse()`는 controls와 metadata를 비우고 요청 상태를 초기화합니다. 버퍼 재사용 여부도 플래그로 구분하므로, 요청을 다시 제출할 때 이전 제어 값이 그대로 남는다고 가정하면 안 됩니다.", "covers": ["review"], "kind": "behavior", "quote": "controls_.clear();\n\t_d()->metadata_.clear();\n}", "evidence": ["reuse"]}, {"text": "`PipelineHandler::stop()`은 장치를 멈추기 전에 대기 큐를 분리합니다. 정지 중 완료 통지가 대기 요청을 다시 제출하지 않도록 하는 순서를 유지합니다.", "covers": ["review"], "kind": "behavior", "quote": "\\brief Stop capturing from all running streams and cancel pending requests\n * \\param[in] camera The camera to stop\n *\n * This function stops capturing and processing requests immediately. All\n * pending requests are cancelled and complete immediately in an error state.\n *\n * \\context This function is called from the CameraManager thread.\n */\nvoid PipelineHandler::stop(Camera *camera)\n{\n\t/*\n\t * Take all waiting requests so that they are not requeued in response\n\t * to completeRequest() being called inside stopDevice(). Cancel them\n\t * after the device to keep them in order.\n\t */\n\tCamera::Private *data = camera->_d();\n\tstd::queue<Request *> waitingRequests;\n\twaitingRequests.swap(data->waitingRequests_);", "evidence": ["device-stop"]}, {"text": "정상 반복 캡처, fence 대기, 장치 제출 오류, 미완료 요청이 있는 정지는 실제 실행으로 확인할 항목입니다. 이 소스 대조에는 해당 장치 시험 결과나 정상 지연 수치가 포함되지 않습니다.", "covers": ["review"], "kind": "limitation", "quote": "/**\n * \\fn PipelineHandler::stopDevice()\n * \\brief Stop capturing from all running streams\n * \\param[in] camera The camera to stop\n *\n * This function stops capturing and processing requests immediately. All\n * pending requests are cancelled and complete immediately in an error state.\n */", "evidence": ["device-stop"]}]}, "body_sha256": "3a8ee47b36c3c5aabff81275713eb08f5a605864925f862f2a06b4d330845485"}
---

# 요청 처리와 문제 진단

**요청의 제출 성공과 촬영 완료를 구분하고, 버퍼를 유지할 기간과 오류가 난 위치를 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 요청 제출과 완료의 연결을 확인합니다. | [제출에서 완료까지](#제출에서-완료까지) |
| 자원을 재사용하거나 해제할 시점을 확인합니다. | [요청·버퍼·fence의 수명](#요청버퍼fence의-수명) |
| 오류가 난 단계를 찾습니다. | [실패 위치별 확인 순서](#실패-위치별-확인-순서) |
| 정지와 연결 해제의 차이를 확인합니다. | [정지와 연결 해제를 구분하기](#정지와-연결-해제를-구분하기) |

## 제출에서 완료까지

요청은 `Camera::createRequest()`에서 빈 객체로 시작합니다. 애플리케이션이 버퍼와 제어 값을 채우며, 요청의 소유권도 호출자에게 있습니다. 생성은 `Configured`와 `Running` 상태에서 가능합니다. `src/libcamera/camera.cpp:1243`

`Request::addBuffer()`는 스트림과 버퍼의 참조를 연결합니다. 한 요청에는 스트림마다 버퍼 하나만 넣을 수 있고, 버퍼는 요청 완료 콜백까지 유효해야 합니다. `src/libcamera/request.cpp:442`

`Camera::queueRequest()`는 실행 상태와 요청 내용을 검사한 뒤 `ConnectionTypeQueued`로 파이프라인 호출을 예약합니다. 0은 이 제출 단계의 성공이며, 프레임 처리가 끝났다는 의미는 아닙니다. 완료는 `requestCompleted` 신호로 구분합니다. `src/libcamera/camera.cpp:1308`

파이프라인은 요청을 대기 큐에 넣어 준비시킨 뒤 맨 앞부터 장치로 보냅니다. 맨 앞 요청이 아직 준비되지 않았거나 장치 큐 크기가 한도와 같으면 제출 순회를 멈춥니다. `queueRequestDevice()` 구현은 요청의 파라미터가 해당 버퍼의 프레임에 적용되도록 장치를 설정합니다. `src/libcamera/pipeline_handler.cpp:428`

버퍼 완료는 `completeBuffer()`로 알리지만, 마지막 버퍼가 끝나도 요청이 자동으로 완료되지는 않습니다. 파이프라인이 `completeRequest()`를 명시적으로 호출해야 하며, 공통 코드는 요청을 애플리케이션에 제출 순서대로 돌려줍니다. `src/libcamera/pipeline_handler.cpp:547`

파이프라인의 완료 함수는 `CameraManager` 스레드에서 실행하는 계약을 가집니다. 이 계약만으로 애플리케이션 콜백의 실행 스레드까지 정할 수는 없으며, 신호 연결 방식은 별도로 확인해야 합니다. `src/libcamera/pipeline_handler.cpp:547`

근거 원문: [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) · [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) · [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a)

## 요청·버퍼·fence의 수명

요청 객체는 애플리케이션이 소유합니다. 완료 핸들러에서 파괴할 수 있고, 계속 사용하려면 새로 큐에 넣기 전에 `reuse()`로 초기화합니다. `src/libcamera/camera.cpp:1243`

`reuse()`는 요청을 `RequestPending`으로 돌리고 controls와 metadata를 비웁니다. `ReuseBuffers`가 있으면 기존 버퍼를 다시 미완료 집합에 넣으며, 없으면 버퍼 맵을 비웁니다. 따라서 재사용 시 제어 값과 버퍼를 어떤 방식으로 다시 채우는지 구분해야 합니다. `src/libcamera/request.cpp:376`

버퍼는 요청이 참조하므로 요청 완료 콜백까지 유효해야 합니다. fence 소유권은 `addBuffer()`가 성공했을 때 버퍼로 이동합니다. fence 대기 타임아웃 뒤에는 버퍼에 fence가 남으므로, 다른 요청에 추가하기 전에 `releaseFence()`로 회수해야 합니다. `src/libcamera/request.cpp:442`

`ReuseBuffers`는 fence를 재사용하지 않습니다. 소스는 fence를 사용하는 경우 이 플래그를 사용하지 말라고 명시하므로, 버퍼 재사용과 fence 수명을 같은 동작으로 취급하면 안 됩니다. `src/libcamera/request.cpp:326`

파이프라인 핸들러는 `completeRequest()`가 반환한 뒤 해당 요청에 접근하면 안 됩니다. 요청을 취소하고 완료까지 처리하는 `cancelRequest()`에도 같은 규칙이 적용됩니다. `src/libcamera/pipeline_handler.cpp:547`

근거 원문: [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) · [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) · [src/libcamera/request.cpp:376](#source-38494771cb29cc8c) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) · [src/libcamera/request.cpp:326](#source-447804db33308244)

## 실패 위치별 확인 순서

버퍼 연결 단계의 `-EEXIST`는 같은 스트림에 이미 버퍼가 있거나, 추가하려는 버퍼에 fence가 남은 경우를 구분해야 합니다. 이는 카메라의 요청 제출 오류와 다른 단계에서 발생합니다. `src/libcamera/request.cpp:442`

`Camera::queueRequest()`에서 `-ENODEV`는 연결 해제, `-EACCES`는 실행 중이 아닌 상태, `-EXDEV`는 다른 카메라가 만든 요청을 가리킵니다. `-EINVAL`은 요청 내용 검사에서 발생하므로 요청 상태와 버퍼·제어 정보를 이어서 확인하는 기준이 됩니다. `src/libcamera/camera.cpp:1308`

구현의 `-EINVAL` 조건은 `RequestPending`이 아닌 요청, 카메라와 다른 controls 정보 맵, 빈 버퍼 목록, 활성 스트림에 속하지 않는 버퍼입니다. 단순히 제출 실패로 묶지 않고 어느 조건에서 반환했는지 구분할 수 있습니다. `src/libcamera/camera.cpp:1308`

제출이 성공한 뒤의 정체는 준비 대기와 장치 전달을 나눠 봅니다. 대기 큐 앞 요청의 `prepared_`가 거짓이면 뒤의 요청도 진행하지 않고, 장치 큐가 한도에 도달해도 순회가 멈춥니다. `queueRequestDevice()`가 오류를 반환한 요청은 취소 경로로 갑니다. `src/libcamera/pipeline_handler.cpp:428`

버퍼가 끝났더라도 명시적인 요청 완료가 빠지면 완료 경로가 끝나지 않습니다. 또한 `completeRequest()`는 장치 큐 앞 요청이 `RequestPending`이면 반환 순회를 멈추므로, 뒤 요청의 완료와 애플리케이션 반환 시점도 구분해야 합니다. `src/libcamera/pipeline_handler.cpp:547`

근거 원문: [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) · [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a)

## 정지와 연결 해제를 구분하기

`Camera::stop()`은 실행 중이 아니면 실제 구현에서 0을 반환합니다. 실행 중이면 접근 검사 뒤 `Stopping`으로 바꾸고 파이프라인 정지를 blocking 방식으로 호출합니다. 미완료 요청이 없는지 확인한 다음 `Configured`로 돌아갑니다. `src/libcamera/camera.cpp:1431`

`PipelineHandler::stop()`은 대기 큐를 먼저 분리하고 `stopDevice()`를 호출합니다. 장치 정지 중 완료 통지가 발생해도 분리한 요청이 다시 제출되지 않게 하며, 장치 쪽 완료 이후에 대기 요청을 취소해 순서를 유지합니다. `src/libcamera/pipeline_handler.cpp:359`

분리한 요청은 취소 표시 후 `doQueueRequest()`에 넣어 순번을 받고 공통 완료 경로를 거칩니다. 마지막에는 두 큐가 비었는지 검사하고 순번을 초기화합니다. `stopDevice()`의 계약은 미완료 요청을 즉시 오류 상태로 취소·완료하는 것입니다. `src/libcamera/pipeline_handler.cpp:359`

정상 `stop()`은 미완료 요청의 동기 취소·완료를 명시하지만, 연결 해제 경로에는 실행 중 대기 요청 처리가 TODO로 남아 있습니다. 따라서 `disconnect()` 알림을 정상 정지 완료와 동일하게 해석하면 안 됩니다. `src/libcamera/camera.cpp:944`

실행 확인 항목: 정지 함수의 동기 완료 계약만으로 별도 스레드에 전달된 애플리케이션 콜백의 후속 작업까지 모두 끝났다고 증명할 수는 없습니다. 콜백 연결과 애플리케이션 작업 종료는 별도 확인 대상입니다. `src/libcamera/camera.cpp:1431`

근거 원문: [src/libcamera/camera.cpp:1431](#source-e09324743def3f09) · [src/libcamera/pipeline_handler.cpp:359](#source-eefd1bbecb1aad0a) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) · [src/libcamera/camera.cpp:944](#source-2758e9ddd31ad41d)

## 변경 검토와 실행 확인

소스에서 구분되는 첫 경계는 제출 성공과 요청 완료입니다. `queueRequest()`는 파이프라인 호출을 예약하고 반환하므로, 성공 반환을 완료 통지 대신 사용하면 안 됩니다. `src/libcamera/camera.cpp:1308`

완료 경로에는 명시적인 `completeRequest()` 호출과 제출 순서 보존이라는 두 조건이 있습니다. 앞 요청이 `RequestPending`이면 뒤의 완료 요청을 바로 반환하지 않으며, 버퍼 완료만으로 요청 완료 책임이 사라지지 않습니다. `src/libcamera/pipeline_handler.cpp:547`

`reuse()`는 controls와 metadata를 비우고 요청 상태를 초기화합니다. 버퍼 재사용 여부도 플래그로 구분하므로, 요청을 다시 제출할 때 이전 제어 값이 그대로 남는다고 가정하면 안 됩니다. `src/libcamera/request.cpp:376`

`PipelineHandler::stop()`은 장치를 멈추기 전에 대기 큐를 분리합니다. 정지 중 완료 통지가 대기 요청을 다시 제출하지 않도록 하는 순서를 유지합니다. `src/libcamera/pipeline_handler.cpp:359`

실행 확인 항목: 정상 반복 캡처, fence 대기, 장치 제출 오류, 미완료 요청이 있는 정지는 실제 실행으로 확인할 항목입니다. 이 소스 대조에는 해당 장치 시험 결과나 정상 지연 수치가 포함되지 않습니다. `src/libcamera/pipeline_handler.cpp:359`

근거 원문: [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/request.cpp:376](#source-38494771cb29cc8c) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) · [src/libcamera/pipeline_handler.cpp:359](#source-eefd1bbecb1aad0a)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 제출 성공 이후의 대기 조건과 완료 책임은 무엇입니까? | [제출에서 완료까지](#제출에서-완료까지) | 코드 근거와 설명 연결 |
    | 어떤 자원을 누가 유지하고 완료 후 무엇을 초기화해야 합니까? | [요청·버퍼·fence의 수명](#요청버퍼fence의-수명) | 코드 근거와 설명 연결 |
    | 제출 실패와 제출 후 완료 지연을 어떻게 구분합니까? | [실패 위치별 확인 순서](#실패-위치별-확인-순서) | 코드 근거와 설명 연결 |
    | 정지 중 요청 반환과 연결 해제의 보장 범위는 어떻게 다릅니까? | [정지와 연결 해제를 구분하기](#정지와-연결-해제를-구분하기) | 코드 근거와 설명 연결 · 실행 확인 항목 별도 |
    | 문서를 읽고 어떤 질문에 답하고 어떤 실행 증거를 확보해야 합니까? | [변경 검토와 실행 확인](#변경-검토와-실행-확인) | 코드 근거와 설명 연결 · 실행 확인 항목 별도 |

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

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `include/libcamera/camera.h`, `include/libcamera/internal/pipeline_handler.h`, `include/libcamera/request.h`, `src/libcamera/camera.cpp`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/request.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `2c4b67c079`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-24 · 사람 검토 전

다음 단계: [Pipeline Handler](pipeline-handler.md)
