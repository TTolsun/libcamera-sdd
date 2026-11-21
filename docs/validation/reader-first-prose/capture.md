---
generated_at: 2026-11-21T15:07:40+00:00
source_commit: adfa719f8ed67d18fd8a0739fc088a1f8b9e7252
status: ok
section: capture
generation_method: facts-and-llm
evidence_fingerprint: 24b4ab2aa507aea9636a68e5dfea4fa53eff85bac3bf9911fdd12f469944f2ad
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
---

# 촬영 요청과 완료 알림

**이 절의 표부터 확인하세요.**



## 보낸 요청은 언제 돌아올까요?

`queueRequest()`가 0을 반환하면 캡처 요청을 처리할 `PipelineHandler::queueRequest()` 호출이 비동기로 예약된 것입니다. 이 호출은 예약한 함수의 실행이나 촬영 완료를 기다리지 않습니다 `src/libcamera/camera.cpp:1308` `src/libcamera/base/bound_method.cpp:37`.

미리보기와 저장 버퍼를 한 요청에 담으면 `bufferCompleted` 알림으로 각 버퍼의 완료를 구별하고, 요청 전체가 끝나기 전에도 완료된 버퍼의 내용을 확인할 수 있습니다 `Documentation/guides/application-developer.rst:356`. 마지막 버퍼가 완료돼도 요청이 자동으로 완료되지는 않으며, 파이프라인 핸들러가 `completeRequest()`를 명시적으로 호출하면 모든 버퍼가 완료된 요청에 대해 `requestCompleted` 알림이 전달됩니다 `src/libcamera/pipeline_handler.cpp:547` `Documentation/guides/application-developer.rst:356`.

앱이 요청 두 개를 차례로 보내면 `requestCompleted` 알림도 보낸 순서대로 받습니다 `Documentation/guides/application-developer.rst:356`. 앱은 알림을 받을 슬롯을 연결하고, 요청이 취소되지 않았는지 확인한 뒤 완료 처리를 마치면 `reuse(Request::ReuseBuffers)`로 요청과 버퍼를 재사용하고 다시 큐에 넣을 수 있습니다 `Documentation/guides/application-developer.rst:356` `Documentation/guides/application-developer.rst:395` `Documentation/guides/application-developer.rst:480`.

근거 원문: [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/pipeline_handler.cpp:547](#source-06476cd330c20a72) · [Documentation/guides/application-developer.rst:356](#source-3648e925190e03c0) · [Documentation/guides/application-developer.rst:480](#source-e15437c22dd9738f) · [src/libcamera/framebuffer.cpp:42](#source-5dbcfed07c8f2f4d) · [Documentation/guides/application-developer.rst:395](#source-08190455a50b5dad) · [src/libcamera/base/bound_method.cpp:37](#source-20ef8212f674f5b2)

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

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

<a id="source-06476cd330c20a72"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:547"
    `src/libcamera/pipeline_handler.cpp:547`에서 시작하는 발췌입니다. 종료 줄은 607이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `a6424bed506015ac59d0572098681d73d5e91e1152641f70a4a04cfb401266fc`
    
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
    ```

<a id="source-3648e925190e03c0"></a>

??? note "소스 근거: Documentation/guides/application-developer.rst:356"
    `Documentation/guides/application-developer.rst:356`에서 시작하는 발췌입니다. 종료 줄은 372이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `13899d3574a46517dea0b938bdf75d8296e96e743e593170f4b2dec2214cdba4`
    
    ```text
    The ``Camera::bufferCompleted`` signal notifies applications that a buffer with
    image data is available. Receiving notifications about the single buffer
    completion event allows applications to implement partial request completion
    support, and to inspect the buffer content before the request it is part of has
    fully completed.
    
    The ``Camera::requestCompleted`` signal notifies applications that a request
    has completed, which means all the buffers the request contains have now
    completed. Request completion notifications are always emitted in the same order
    as the requests have been queued to the camera.
    
    To receive the signals emission notifications, connect a slot function to the
    signal to handle it in the application code.
    
    .. code:: cpp
    
       camera->requestCompleted.connect(requestComplete);
    ```

<a id="source-e15437c22dd9738f"></a>

??? note "소스 근거: Documentation/guides/application-developer.rst:480"
    `Documentation/guides/application-developer.rst:480`에서 시작하는 발췌입니다. 종료 줄은 487이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `39ba50dbb15823e3f31f09e8b2bde78aaa001e2e76325d39a2eea87311ea6c12`
    
    ```text
    With the handling of this request completed, it is possible to re-use the
    request and the associated buffers and re-queue it to the camera
    device:
    
    .. code:: cpp
    
       request->reuse(Request::ReuseBuffers);
       camera->queueRequest(request);
    ```

<a id="source-5dbcfed07c8f2f4d"></a>

??? note "소스 근거: src/libcamera/framebuffer.cpp:42"
    `src/libcamera/framebuffer.cpp:42`에서 시작하는 발췌입니다. 종료 줄은 44이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `44851ddad267db9f155b6ad759eaa1a89d8e39973d8680f164e7744722a08995`
    
    ```text
    \var FrameMetadata::FrameSuccess
     * The frame has been captured with success and contains valid data. All fields
     * of the FrameMetadata structure are valid.
    ```

<a id="source-08190455a50b5dad"></a>

??? note "소스 근거: Documentation/guides/application-developer.rst:395"
    `Documentation/guides/application-developer.rst:395`에서 시작하는 발췌입니다. 종료 줄은 404이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `ccaab7c9c96c479b619702df2459fa756a4e8b59c9d7bf27229c3dd22f6ea783`
    
    ```text
    Request completion events can be emitted for requests which have been canceled,
    for example, by unexpected application shutdown. To avoid an application
    processing invalid image data, it's worth checking that the request has
    completed successfully. The list of request completion statuses is available in
    the :doxy-pub:`Request::Status` class enum documentation.
    
    .. code:: cpp
    
       if (request->status() == Request::RequestCancelled)
          return;
    ```

<a id="source-20ef8212f674f5b2"></a>

??? note "소스 근거: src/libcamera/base/bound_method.cpp:37"
    `src/libcamera/base/bound_method.cpp:37`에서 시작하는 발췌입니다. 종료 줄은 44이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `11ec2744416fc4349794c44aaacd157899d1c63c973f5d2d7d1e9213bae9eb63`
    
    ```text
    \var ConnectionTypeQueued
     * \brief The receiver is invoked asynchronously
     *
     * Invoke the receiver asynchronously in its thread when control returns to the
     * thread's event loop. The sender proceeds without waiting for the invocation
     * to complete.
     *
     * \var ConnectionTypeBlocking
    ```

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `Documentation/guides/application-developer.rst`, `src/libcamera/base/bound_method.cpp`, `src/libcamera/camera.cpp`, `src/libcamera/framebuffer.cpp`, `src/libcamera/pipeline_handler.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `adfa719f8e`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-22 · 사람 검토 전

다음 단계: [버퍼 완료와 요청 완료를 그림으로 보기](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#버퍼-완료와-명시적-요청-완료의-경계)
