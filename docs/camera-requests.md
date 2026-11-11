---
generated_at: 2026-10-31T11:33:28+00:00
source_commit: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
status: ok
section: camera-requests
generation_method: facts-and-llm
evidence_fingerprint: a640984c4ec5f1240d2662b60a86eb6c18a271b84b99b0a725bef4c0a7299131
semantic_review: human-review-required
agent: cli/claude/claude-haiku-5-5
generated_design: {"schema": 1, "input_fingerprint": "a640984c4ec5f1240d2662b60a86eb6c18a271b84b99b0a725bef4c0a7299131", "answers": {"request": [{"text": "`createRequest`는 새로 만든 빈 `Request` 객체를 `std::unique_ptr<Request>`로 반환하며, 오류가 나면 `nullptr`을 반환합니다. 반환된 객체의 소유권은 호출자에게 넘어가며, 호출자가 이를 삭제할 책임을 가집니다. 요청은 완료 핸들러에서 삭제되거나, `Request::reuse()`로 상태를 초기화한 뒤 재사용될 수 있습니다.", "evidence": ["create"], "covers": ["request"], "kind": "behavior", "quote": "\\brief Create a request object for the camera\n * \\param[in] cookie Opaque cookie for application use\n *\n * This function creates an empty request for the application to fill with\n * buffers and parameters, and queue for capture.\n *\n * The \\a cookie is stored in the request and is accessible through the\n * Request::cookie() function at any time. It is typically used by applications\n * to map the request to an external resource in the request completion\n * handler, and is completely opaque to libcamera.\n *\n * The ownership of the returned request is passed to the caller, which is\n * responsible for deleting it. The request may be deleted in the completion\n * handler, or reused after resetting its state with Request::reuse().\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest(uint64_t cookie)", "part_id": "create-owner"}, {"text": "호출자는 `Request::addBuffer`로 한 요청에 같은 스트림의 버퍼를 둘 이상 연결해서는 안 되며, 한 요청은 스트림당 버퍼를 하나만 포함할 수 있습니다.", "evidence": ["buffer"], "covers": ["request"], "kind": "behavior", "quote": "\\brief Add a FrameBuffer with its associated Stream to the Request\n * \\param[in] stream The stream the buffer belongs to\n * \\param[in] buffer The FrameBuffer to add to the request\n * \\param[in] fence The optional fence\n *\n * A reference to the buffer is stored in the request. The caller is responsible\n * for ensuring that the buffer will remain valid until the request complete\n * callback is called.\n *\n * A request can only contain one buffer per stream. If a buffer has already\n * been added to the request for the same stream, this function returns -EEXIST.\n *\n * A Fence can be optionally associated with the \\a buffer.\n *\n * When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.\n *\n * If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request. Attempting to add a buffer that still\n * contains a fence to a request will result in this function returning -EEXIST.\n *\n * \\sa FrameBuffer::releaseFence()\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -EEXIST The request already contains a buffer for the stream\n *  or the buffer still references a fence\n * \\retval -EINVAL The buffer does not reference a valid Stream\n */\nint Request::addBuffer(const Stream *stream, FrameBuffer *buffer,", "part_id": "attach-buffer"}, {"text": "`Request::addBuffer()`는 먼저 `!stream` 조건을 확인하고, 참이면 \"Invalid stream reference\" 오류 로그를 남긴 뒤 `-EINVAL`을 반환합니다. 다음으로 `buffer->_d()->fence()`가 남아 있으면 `-EEXIST`를 반환하므로, fence가 남아 있는 버퍼는 이 단계에서 등록되지 않습니다. 마지막으로 `bufferMap_.try_emplace(stream, buffer)`의 `inserted`가 false이면, 로그 \"`FrameBuffer` already set for stream\"과 함께 `-EEXIST`를 반환합니다.", "evidence": ["buffer-code"], "covers": ["request"], "kind": "behavior", "quote": "int Request::addBuffer(const Stream *stream, FrameBuffer *buffer,\n\t\t       std::unique_ptr<Fence> &&fence)\n{\n\tif (!stream) {\n\t\tLOG(Request, Error) << \"Invalid stream reference\";\n\t\treturn -EINVAL;\n\t}", "part_id": "buffer-rejection"}, {"text": "`!stream` 검사, fence 검사, `inserted` 검사를 모두 통과하고 `bufferMap_.try_emplace`가 `inserted`가 true인 경우에만 `buffer->_d()->setRequest(this)`와 `_d()->pending_.insert(buffer)`가 이 순서대로 실행됩니다. 이 두 줄 뒤에는 fence 설정 분기가 이어지고, 함수는 `return 0;`으로 끝납니다.", "evidence": ["buffer-code"], "covers": ["request"], "kind": "behavior", "quote": "buffer->_d()->setRequest(this);\n\t_d()->pending_.insert(buffer);", "part_id": "buffer-rejection"}, {"text": "애플리케이션은 `createRequest()`로 요청을 만든 뒤 `queueRequest`를 호출하기 전에 그 요청에 캡처 버퍼를 하나 이상 채워야 하며, 버퍼가 없는 요청은 큐에 넣지 않고 거부됩니다.", "evidence": ["queue"], "covers": ["request"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();", "part_id": "queue-input"}, {"text": "`Camera::queueRequest()`는 `request->_d()->camera()`가 `this`와 다르면, 즉 요청을 만든 카메라가 현재 카메라가 아니면 \"`Request` was not created by this camera\" 오류를 기록하고 `-EXDEV`를 반환합니다.", "evidence": ["queue-owner-guard"], "covers": ["request"], "kind": "behavior", "quote": "if (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"Request was not created by this camera\";\n\t\treturn -EXDEV;", "part_id": "queue-owner"}, {"text": "`Camera::queueRequest`는 `request->status()`가 `Request::RequestPending`과 일치하지 않으면 `-EINVAL`을 반환합니다.", "evidence": ["queue-code"], "covers": ["request"], "kind": "behavior", "quote": "if (request->status() != Request::RequestPending) {\n\t\tLOG(Camera, Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\t}", "part_id": "queue-status"}, {"text": "`Camera::queueRequest()`는 `request->controls().infoMap()`과 `&controls()`를 `!=`로 비교하여 두 값이 다르면 `LOG(Camera, Error)`로 \"Overwriting `Request::controls()` is not allowed\"를 기록하고 `-EINVAL`을 반환합니다.", "evidence": ["queue-controls-guard"], "covers": ["request"], "kind": "behavior", "quote": "if (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera, Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn -EINVAL;", "part_id": "queue-controls"}, {"text": "`Camera::queueRequest()`는 `request->buffers()`가 비어 있으면, 즉 `empty()`가 참이면 `Request contains no buffers` 오류를 기록하고 `-EINVAL`을 반환합니다.", "evidence": ["queue-buffers-guard"], "covers": ["request"], "kind": "behavior", "quote": "if (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request contains no buffers\";\n\t\treturn -EINVAL;", "part_id": "queue-buffers"}, {"text": "`Camera::queueRequest()`는 `request->buffers()`의 각 `stream`이 `d->activeStreams_`에 없으면(`find`가 `end()`를 반환하면) `-EINVAL`을 반환합니다.", "evidence": ["queue-stream-guard"], "covers": ["request"], "kind": "behavior", "quote": "if (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;", "part_id": "queue-stream"}, {"text": "`Camera::queueRequest()`는 요청 검사를 마친 뒤 `ConnectionTypeQueued`를 지정해 `invokeMethod`로 `PipelineHandler::queueRequest`를 호출하고, 그 호출 뒤에 `0`을 반환합니다. 이 `0`은 `invokeMethod` 호출 뒤의 반환값이며, 요청 완료는 카메라가 `requestCompleted` 신호로 별도로 알립니다.", "evidence": ["queue-code", "queue"], "covers": ["request"], "kind": "behavior", "quote": "d->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t       ConnectionTypeQueued, request);", "part_id": "completion-signal"}], "lifetime": [{"text": "`Request::addBuffer`는 버퍼에 대한 참조를 요청에 저장합니다. 호출자는 요청 완료 콜백이 호출될 때까지 해당 버퍼가 유효하게 남아 있도록 보장해야 합니다.", "evidence": ["buffer"], "covers": ["lifetime"], "kind": "behavior", "quote": "\\brief Add a FrameBuffer with its associated Stream to the Request\n * \\param[in] stream The stream the buffer belongs to\n * \\param[in] buffer The FrameBuffer to add to the request\n * \\param[in] fence The optional fence\n *\n * A reference to the buffer is stored in the request. The caller is responsible\n * for ensuring that the buffer will remain valid until the request complete\n * callback is called.\n *\n * A request can only contain one buffer per stream. If a buffer has already\n * been added to the request for the same stream, this function returns -EEXIST.\n *\n * A Fence can be optionally associated with the \\a buffer.\n *\n * When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.\n *\n * If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request. Attempting to add a buffer that still\n * contains a fence to a request will result in this function returning -EEXIST.\n *\n * \\sa FrameBuffer::releaseFence()\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -EEXIST The request already contains a buffer for the stream\n *  or the buffer still references a fence\n * \\retval -EINVAL The buffer does not reference a valid Stream\n */\nint Request::addBuffer(const Stream *stream, FrameBuffer *buffer,", "part_id": "buffer-validity"}, {"text": "`Request::addBuffer`가 성공하면 유효한 `Fence`의 소유권은 `buffer`(`FrameBuffer`)로 이동합니다. 이때 `fence`는 `buffer`로 옮겨집니다.", "evidence": ["fence-move"], "covers": ["lifetime"], "kind": "behavior", "quote": "When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.", "part_id": "fence-transfer"}, {"text": "`addBuffer`가 실패하면 `fence`의 소유권은 가져가지 않으며, 전달받은 `fence`는 변경되지 않고 그대로 유지됩니다.", "evidence": ["fence-move"], "covers": ["lifetime"], "kind": "behavior", "quote": "When a valid Fence is provided to this function, \\a fence is moved to \\a\n * buffer and this Request will only be queued to the device once the\n * fences of all its buffers have been correctly signalled. Ownership of the\n * fence will only be taken in case of success, otherwise the fence will\n * be left unmodified.", "part_id": "fence-failure"}, {"text": "펜스가 신호되지 않으면 요청은 타임아웃 후 실패합니다. 이때 버퍼에는 펜스가 그대로 남아 있으며, 애플리케이션은 다른 요청에 버퍼를 재사용하기 전에 `FrameBuffer::releaseFence()`로 이 펜스를 회수해야 합니다.", "evidence": ["fence-expiry"], "covers": ["lifetime"], "kind": "behavior", "quote": "If the \\a fence associated with \\a buffer isn't signalled, the request will\n * fail after a timeout. The buffer will still contain the fence, which\n * applications must retrieve with FrameBuffer::releaseFence() before the buffer\n * can be reused in another request.", "part_id": "fence-timeout"}, {"text": "`Request::reuse`는 `flags`에 `ReuseBuffers`가 설정된 경우 `bufferMap_`의 각 버퍼마다 `buffer->_d()->setRequest(this)`를 호출해 그 버퍼를 현재 요청에 연결한 뒤, `_d()->pending_`에 그 버퍼를 추가합니다.", "evidence": ["reuse-buffers", "reuse-link-call"], "covers": ["lifetime"], "kind": "behavior", "quote": "if (flags & ReuseBuffers) {\n\t\tfor (const auto &[stream, buffer] : bufferMap_) {\n\t\t\tbuffer->_d()->setRequest(this);\n\t\t\t_d()->pending_.insert(buffer);\n\t\t}\n\t} else {\n\t\tbufferMap_.clear();\n\t}\n\n\tstatus_ = RequestPending;", "part_id": "reset-buffer-link"}, {"text": "`Request::reuse()`에서 `flags & ReuseBuffers`가 거짓이면 else 분기가 실행되며, 이때 `bufferMap_.clear()`를 호출해 `bufferMap_`의 모든 항목을 비웁니다.", "evidence": ["reuse", "reuse-buffers"], "covers": ["lifetime"], "kind": "behavior", "quote": "if (flags & ReuseBuffers) {\n\t\tfor (const auto &[stream, buffer] : bufferMap_) {\n\t\t\tbuffer->_d()->setRequest(this);\n\t\t\t_d()->pending_.insert(buffer);\n\t\t}\n\t} else {\n\t\tbufferMap_.clear();\n\t}", "part_id": "reset-buffer-clear"}, {"text": "`Request::reuse`는 `status_`를 `RequestPending`으로 설정한 뒤, `controls_`와 `_d()->metadata_`를 각각 `clear()`합니다.", "evidence": ["reuse-status", "reuse-controls", "reuse-metadata"], "covers": ["lifetime"], "kind": "behavior", "quote": "status_ = RequestPending;", "part_id": "reset"}, {"text": "`Request::ReuseBuffers` 플래그는 `Request::reuse()` 호출 시 `addBuffer()`로 이전에 추가한 버퍼를 다시 사용하여 기존 버퍼를 유지합니다. 다만 버퍼에 연결된 펜스는 재사용되지 않으며, 소스 주석은 펜스를 사용하는 경우 이 플래그를 피하도록 권고합니다.", "evidence": ["reuse-flags", "reuse-advice"], "covers": ["lifetime"], "kind": "behavior", "quote": "\\enum Request::ReuseFlag\n * Flags to control the behavior of Request::reuse()\n * \\var Request::Default\n * Don't reuse buffers\n * \\var Request::ReuseBuffers\n * Reuse the buffers that were previously added by addBuffer()\n *\n * \\note Fences associated with the buffers are not reused.\n *  This flag should not be used if fences are used.\n */", "part_id": "reuse-fences"}]}, "topic_inputs": {"request": "2b7d75514178f7988aad0c1834a34ff5ec86e4cba775a26fa4484c14472bb34c", "lifetime": "ffc00ba2220ddaf9a9dd46a41a8c3ec1046b05445126f79e93243a66eef50def"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["request", "lifetime"], "topic_agents": {"request": "cli/claude/claude-haiku-5-5", "lifetime": "cli/claude/claude-haiku-5-5"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "367d18b95f8f0d01a15ae0f4d1b70f7e13e4d0298df4215e2c449ac4905db6f9", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "2f593eec0430a4e6b5822e642c0a7a1227fc150a0b27d8a71f521acf93b6439e", "answer_contracts": "1e0d24e0cf26ded53ecec2e5a6fbc51836bac6e17530318a9fa7cffaa936c00b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "57cc3233cfdcf429751f31081ffca06a8f8b53fb15fb1e3a5256aa7998a8ceb4", "design_response": "deb70dda7ad27f001267e4a9712c5b0dc1fe9fa67acd13bedbfefaaad0ad83c8", "design_validation": "946deebb694018f6361ee86669e1a7a26cd61dfffef11bb3a7de0a193639fabe"}, "validation_model": "5c62ad01223b0d3de6ef258bca56a03057c3bf0019b375b2a7892b6e2d6a307b", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "f8fd5a3d8041c23fc68b93ff32b8727e98393383b5099032eb00ad0013e7611c"}, "checkpoint_units": [{"checkpoint": "0906502a7f967d2058a33421fc165e9289317caf38ee8b85a3981465ce6a6d0b.json", "topic": "request", "part": "create-owner", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["af2ac4674230404da418796c410d43b2/001.receipt.json", "af2ac4674230404da418796c410d43b2/002.receipt.json"]}, {"checkpoint": "5c0eea6c0c63c5e8aebfd3103e327f8d8f9c5baff3270afae44131764633bd11.json", "topic": "request", "part": "buffer-rejection", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["af2ac4674230404da418796c410d43b2/005.receipt.json", "af2ac4674230404da418796c410d43b2/006.receipt.json"]}, {"checkpoint": "e1fe28d315a925da91dfc36ad77c0c8996b9cac9ad0956bf8c530ba69a788925.json", "topic": "request", "part": "queue-input", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["af2ac4674230404da418796c410d43b2/007.receipt.json", "af2ac4674230404da418796c410d43b2/008.receipt.json"]}, {"checkpoint": "03b9d1b9a1b9c5bcb3f19a9381de442878191906aeca0d27ef1bfc502efed7e2.json", "topic": "request", "part": "completion-signal", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["af2ac4674230404da418796c410d43b2/019.receipt.json", "af2ac4674230404da418796c410d43b2/020.receipt.json"]}, {"checkpoint": "ae683ff5275c03a363e6ddde8d0487839e25b1c76720740f5c3641c07bb9ecdc.json", "topic": "lifetime", "part": "buffer-validity", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["af2ac4674230404da418796c410d43b2/021.receipt.json", "af2ac4674230404da418796c410d43b2/022.receipt.json"]}, {"checkpoint": "de04b90a73800867d1f8e67fecd3fb8ce03e5fe5a6c222c8864a419cd3335025.json", "topic": "lifetime", "part": "fence-timeout", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["af2ac4674230404da418796c410d43b2/028.receipt.json", "af2ac4674230404da418796c410d43b2/029.receipt.json"]}, {"checkpoint": "cc4759f70f53951aadd72f183b51c75d93c77020d64651e372624bcea9aac1bd.json", "topic": "lifetime", "part": "reset-buffer-link", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["af2ac4674230404da418796c410d43b2/030.receipt.json", "af2ac4674230404da418796c410d43b2/031.receipt.json"]}, {"checkpoint": "06ee2ebeda1cc9e223c93776225d7c4fa971b470a98f29b040efbe053b339745.json", "topic": "lifetime", "part": "reset", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["af2ac4674230404da418796c410d43b2/034.receipt.json", "af2ac4674230404da418796c410d43b2/035.receipt.json"]}, {"checkpoint": "72c22c5fc7cff94a2c97ea0a13ca517637d7d6cca3fd592f2601b9d65f66b489.json", "topic": "lifetime", "part": "reuse-fences", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["af2ac4674230404da418796c410d43b2/036.receipt.json", "af2ac4674230404da418796c410d43b2/037.receipt.json"]}], "body_sha256": "e7c215c0f3fbf24b9c9368c55856ca8d209a5528d9cb9972d37dcd7fce8c1f7e"}
revalidated_from: be7e83e91348250c015aad6d6f59f1468555bae8
---

# 요청 객체와 버퍼 수명

**요청 생성과 제출, 버퍼·펜스의 유지와 재사용 조건을 코드와 대조하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 클래스의 책임, 요청과 버퍼의 수명, 상태 전이와 종료·동기화 계약을 코드 근거로 확인하세요. | [카메라와 요청 모델](camera-model.md) |

## 요청 생성과 완료

`createRequest`는 새로 만든 빈 `Request` 객체를 `std::unique_ptr<Request>`로 반환하며, 오류가 나면 `nullptr`을 반환합니다. 반환된 객체의 소유권은 호출자에게 넘어가며, 호출자가 이를 삭제할 책임을 가집니다. 요청은 완료 핸들러에서 삭제되거나, `Request::reuse()`로 상태를 초기화한 뒤 재사용될 수 있습니다. 호출자는 `Request::addBuffer`로 한 요청에 같은 스트림의 버퍼를 둘 이상 연결해서는 안 되며, 한 요청은 스트림당 버퍼를 하나만 포함할 수 있습니다. `src/libcamera/camera.cpp:1243`, `src/libcamera/request.cpp:442`

<!-- sdd:visual:add-buffer-rejections -->
### 버퍼 연결 실패를 구분하는 순서

```mermaid
flowchart TB
%% sdd:translations {"-EEXIST: 남은 fence": "-EEXIST: retained fence", "-EEXIST: 중복 stream": "-EEXIST: duplicate stream", "-EINVAL 반환": "Return -EINVAL", "0 반환": "Return 0", "stream이 비었나요?": "Is stream null?", "stream이 이미 등록됐나요?": "Is the stream already <br/>registered?", "버퍼에 fence가 남았나요?": "Does the buffer retain a <br/>fence?", "아니요": "No", "예": "Yes", "요청 연결과 pending_ 추가": "Attach request and add <br/>pending_", "유효한 fence가 있으면 <br/>이동한 뒤 반환": "Move a valid supplied fence <br/>if present, then return"}
  v_stream{"stream이 비었나요?"}
  v_invalid["-EINVAL 반환"]
  v_fence{"버퍼에 fence가 남았나요?"}
  v_retained["-EEXIST: 남은 fence"]
  v_duplicate{"stream이 이미 등록됐나요?"}
  v_existing["-EEXIST: 중복 stream"]
  v_attach["요청 연결과 pending_ 추가"]
  v_success["0 반환"]
  v_stream -->|"예"| v_invalid
  v_stream -->|"아니요"| v_fence
  v_fence -->|"예"| v_retained
  v_fence -->|"아니요"| v_duplicate
  v_duplicate -->|"예"| v_existing
  v_duplicate -->|"아니요"| v_attach
  v_attach -->|"유효한 fence가 있으면 <br/>이동한 뒤 반환"| v_success
```

[Mermaid 원문](camera-requests.add-buffer-rejections.mmd)

??? note "그림 근거와 확인 범위"
    같은 -EEXIST라도 남은 fence와 중복 stream을 구분하고, 실패 검사 뒤의 요청 연결 경계를 확인합니다.
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | stream이 비었나요? | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | -EINVAL 반환 | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | 버퍼에 fence가 남았나요? | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | -EEXIST: 남은 fence | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | stream이 이미 등록됐나요? | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | -EEXIST: 중복 stream | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | 요청 연결과 pending_ 추가 | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | 0 반환 | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | 예 | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | 아니요 | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | 예 | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | 아니요 | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | 예 | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | 아니요 | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | 유효한 fence가 있으면 이동한 뒤 반환 | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
<!-- /sdd:visual:add-buffer-rejections -->

<!-- sdd:visual:queue-return-completion -->
### 접수 반환과 완료 알림

```mermaid
flowchart TB
%% sdd:translations {"API의 완료 알림 계약": "API completion-notification <br/>contract", "ConnectionTypeQueued 호출": "Invoke with <br/>ConnectionTypeQueued", "queueRequest: 0 반환": "queueRequest returns 0", "완료 시 requestCompleted <br/>알림": "Notify completion through <br/>requestCompleted", "큐에 넣은 요청": "Queued request", "호출 뒤 반환": "Return after invoking"}
  v_invoke["ConnectionTypeQueued 호출"]
  v_zero["queueRequest: 0 반환"]
  v_queued["큐에 넣은 요청"]
  v_complete["완료 시 requestCompleted <br/>알림"]
  v_invoke -->|"호출 뒤 반환"| v_zero
  v_queued -->|"API의 완료 알림 계약"| v_complete
```

[Mermaid 원문](camera-requests.queue-return-completion.mmd)

??? note "그림 근거와 확인 범위"
    queueRequest의 0 반환과 requestCompleted 알림은 각각 무엇을 뜻합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | ConnectionTypeQueued 호출 | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | queueRequest: 0 반환 | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | 큐에 넣은 요청 | [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) |
    | 완료 시 requestCompleted 알림 | [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) |
    | 호출 뒤 반환 | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | API의 완료 알림 계약 | [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) |
<!-- /sdd:visual:queue-return-completion -->

`Request::addBuffer()`는 먼저 `!stream` 조건을 확인하고, 참이면 "Invalid stream reference" 오류 로그를 남긴 뒤 `-EINVAL`을 반환합니다. 다음으로 `buffer->_d()->fence()`가 남아 있으면 `-EEXIST`를 반환하므로, fence가 남아 있는 버퍼는 이 단계에서 등록되지 않습니다. 마지막으로 `bufferMap_.try_emplace(stream, buffer)`의 `inserted`가 false이면, 로그 "`FrameBuffer` already set for stream"과 함께 `-EEXIST`를 반환합니다. `src/libcamera/request.cpp:475`

`!stream` 검사, fence 검사, `inserted` 검사를 모두 통과하고 `bufferMap_.try_emplace`가 `inserted`가 true인 경우에만 `buffer->_d()->setRequest(this)`와 `_d()->pending_.insert(buffer)`가 이 순서대로 실행됩니다. 이 두 줄 뒤에는 fence 설정 분기가 이어지고, 함수는 `return 0;`으로 끝납니다. 애플리케이션은 `createRequest()`로 요청을 만든 뒤 `queueRequest`를 호출하기 전에 그 요청에 캡처 버퍼를 하나 이상 채워야 하며, 버퍼가 없는 요청은 큐에 넣지 않고 거부됩니다. `src/libcamera/request.cpp:475`, `src/libcamera/camera.cpp:1308`

`Camera::queueRequest()`는 `request->_d()->camera()`가 `this`와 다르면, 즉 요청을 만든 카메라가 현재 카메라가 아니면 "`Request` was not created by this camera" 오류를 기록하고 `-EXDEV`를 반환합니다. `Camera::queueRequest`는 `request->status()`가 `Request::RequestPending`과 일치하지 않으면 `-EINVAL`을 반환합니다. `Camera::queueRequest()`는 `request->controls().infoMap()`과 `&controls()`를 `!=`로 비교하여 두 값이 다르면 `LOG(Camera, Error)`로 "Overwriting `Request::controls()` is not allowed"를 기록하고 `-EINVAL`을 반환합니다. `src/libcamera/camera.cpp:1339`, `src/libcamera/camera.cpp:1330`, `src/libcamera/camera.cpp:1350`

`Camera::queueRequest()`는 `request->buffers()`가 비어 있으면, 즉 `empty()`가 참이면 `Request contains no buffers` 오류를 기록하고 `-EINVAL`을 반환합니다. `Camera::queueRequest()`는 `request->buffers()`의 각 `stream`이 `d->activeStreams_`에 없으면(`find`가 `end()`를 반환하면) `-EINVAL`을 반환합니다. `Camera::queueRequest()`는 요청 검사를 마친 뒤 `ConnectionTypeQueued`를 지정해 `invokeMethod`로 `PipelineHandler::queueRequest`를 호출하고, 그 호출 뒤에 `0`을 반환합니다. 이 `0`은 `invokeMethod` 호출 뒤의 반환값이며, 요청 완료는 카메라가 `requestCompleted` 신호로 별도로 알립니다. `src/libcamera/camera.cpp:1361`, `src/libcamera/camera.cpp:1367`, `src/libcamera/camera.cpp:1330`, `src/libcamera/camera.cpp:1308`

근거 원문: [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) · [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) · [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) · [src/libcamera/camera.cpp:1339](#source-a03c9ac514bfd95e) · [src/libcamera/camera.cpp:1350](#source-980d3a2f94252f0c) · [src/libcamera/camera.cpp:1361](#source-d572e3b4aa0a295b) · [src/libcamera/camera.cpp:1367](#source-589094bc9fe6e38d) · [src/libcamera/request.cpp:475](#source-605100b059a6864d)

## 소유권과 재사용

`Request::addBuffer`는 버퍼에 대한 참조를 요청에 저장합니다. 호출자는 요청 완료 콜백이 호출될 때까지 해당 버퍼가 유효하게 남아 있도록 보장해야 합니다. `Request::addBuffer`가 성공하면 유효한 `Fence`의 소유권은 `buffer`(`FrameBuffer`)로 이동합니다. 이때 `fence`는 `buffer`로 옮겨집니다. `src/libcamera/request.cpp:442`, `src/libcamera/request.cpp:456`

<!-- sdd:visual:request-ownership -->
### 요청과 버퍼를 유지할 기간

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

[Mermaid 원문](camera-requests.request-ownership.mmd)

??? note "그림 근거와 확인 범위"
    요청의 소유권은 호출자에게 있습니다. 버퍼 참조를 연결해도 호출자의 버퍼 유지 책임은 계속됩니다.
    
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

<!-- sdd:visual:timeout-fence-recovery -->
### 타임아웃 뒤 펜스 회수

```mermaid
flowchart TB
%% sdd:translations {"그 뒤 다른 요청에서 버퍼 <br/>재사용": "Then reuse the buffer in <br/>another request", "버퍼에 펜스가 남음": "Buffer still contains its <br/>fence", "애플리케이션이 <br/>releaseFence()로 회수": "Application retrieves with <br/>releaseFence()", "요청 실패 뒤에도 유지": "Remains after request <br/>failure", "재사용 전 회수 의무": "Must retrieve before reuse", "펜스 미신호: 요청 타임아웃": "Unsignalled fence: request <br/>times out", "회수 후 재사용 가능": "Reuse after retrieval"}
  v_timeout["펜스 미신호: 요청 타임아웃"]
  v_retained["버퍼에 펜스가 남음"]
  v_retrieve["애플리케이션이 <br/>releaseFence()로 회수"]
  v_reuse["그 뒤 다른 요청에서 버퍼 <br/>재사용"]
  v_timeout -->|"요청 실패 뒤에도 유지"| v_retained
  v_retained -->|"재사용 전 회수 의무"| v_retrieve
  v_retrieve -->|"회수 후 재사용 가능"| v_reuse
```

[Mermaid 원문](camera-requests.timeout-fence-recovery.mmd)

??? note "그림 근거와 확인 범위"
    신호되지 않은 펜스로 타임아웃이 나면 다른 요청에 재사용하기 전에 무엇을 해야 합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | 펜스 미신호: 요청 타임아웃 | [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) |
    | 버퍼에 펜스가 남음 | [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) |
    | 애플리케이션이 releaseFence()로 회수 | [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) |
    | 그 뒤 다른 요청에서 버퍼 재사용 | [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) |
    | 요청 실패 뒤에도 유지 | [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) |
    | 재사용 전 회수 의무 | [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) |
    | 회수 후 재사용 가능 | [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) |
<!-- /sdd:visual:timeout-fence-recovery -->

<!-- sdd:visual:reuse-buffer-relink -->
### 재사용 버퍼의 요청 연결

```mermaid
flowchart TB
%% sdd:translations {"ReuseBuffers: 기존 <br/>bufferMap_ 순회": "ReuseBuffers: iterate <br/>existing bufferMap_", "각 기존 버퍼의 연결 갱신": "Update each retained buffer <br/>link", "각 버퍼를 pending_에 추가": "Insert each buffer into <br/>pending_", "각 버퍼의 setRequest(this)": "setRequest(this) on each <br/>buffer", "연결한 뒤 대기 집합에 추가": "Insert into pending after <br/>relinking"}
  v_retained["ReuseBuffers: 기존 <br/>bufferMap_ 순회"]
  v_request["각 버퍼의 setRequest(this)"]
  v_pending["각 버퍼를 pending_에 추가"]
  v_retained -->|"각 기존 버퍼의 연결 갱신"| v_request
  v_request -->|"연결한 뒤 대기 집합에 추가"| v_pending
```

[Mermaid 원문](camera-requests.reuse-buffer-relink.mmd)

??? note "그림 근거와 확인 범위"
    ReuseBuffers 경로에서 각 버퍼는 어떤 순서로 다시 요청에 연결됩니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | ReuseBuffers: 기존 bufferMap_ 순회 | [src/libcamera/request.cpp:391](#source-e41b7fa688c1de2e) |
    | 각 버퍼의 setRequest(this) | [src/libcamera/request.cpp:391](#source-e41b7fa688c1de2e) |
    | 각 버퍼를 pending_에 추가 | [src/libcamera/request.cpp:391](#source-e41b7fa688c1de2e) |
    | 각 기존 버퍼의 연결 갱신 | [src/libcamera/request.cpp:391](#source-e41b7fa688c1de2e) |
    | 연결한 뒤 대기 집합에 추가 | [src/libcamera/request.cpp:391](#source-e41b7fa688c1de2e) |
<!-- /sdd:visual:reuse-buffer-relink -->

<!-- sdd:visual:reuse-buffer-fence-distinction -->
### 버퍼 재사용과 펜스 권고

```mermaid
flowchart TB
%% sdd:translations {"API의 should not 권고": "API should-not <br/>recommendation", "ReuseBuffers": "ReuseBuffers", "버퍼와 펜스의 범위 구분": "Distinguish buffer and <br/>fence reuse", "앞서 addBuffer로 넣은 버퍼 <br/>재사용": "Reuse buffers previously <br/>added by addBuffer", "연결된 펜스는 재사용하지 <br/>않음": "Associated fences are not <br/>reused", "펜스를 쓰면 이 플래그를 <br/>피하도록 권고": "Should not use this flag <br/>with fences", "플래그의 재사용 범위": "Flag reuse scope"}
  v_flag["ReuseBuffers"]
  v_buffers["앞서 addBuffer로 넣은 버퍼 <br/>재사용"]
  v_fences["연결된 펜스는 재사용하지 <br/>않음"]
  v_advice["펜스를 쓰면 이 플래그를 <br/>피하도록 권고"]
  v_flag -->|"플래그의 재사용 범위"| v_buffers
  v_buffers -->|"버퍼와 펜스의 범위 구분"| v_fences
  v_fences -->|"API의 should not 권고"| v_advice
```

[Mermaid 원문](camera-requests.reuse-buffer-fence-distinction.mmd)

??? note "그림 근거와 확인 범위"
    ReuseBuffers가 재사용하는 대상과 펜스 사용 시 권고는 무엇입니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | ReuseBuffers | [src/libcamera/request.cpp:326](#source-447804db33308244) |
    | 앞서 addBuffer로 넣은 버퍼 재사용 | [src/libcamera/request.cpp:326](#source-447804db33308244) |
    | 연결된 펜스는 재사용하지 않음 | [src/libcamera/request.cpp:326](#source-447804db33308244) |
    | 펜스를 쓰면 이 플래그를 피하도록 권고 | [src/libcamera/request.cpp:326](#source-447804db33308244) |
    | 플래그의 재사용 범위 | [src/libcamera/request.cpp:326](#source-447804db33308244) |
    | 버퍼와 펜스의 범위 구분 | [src/libcamera/request.cpp:326](#source-447804db33308244) |
    | API의 should not 권고 | [src/libcamera/request.cpp:326](#source-447804db33308244) |
<!-- /sdd:visual:reuse-buffer-fence-distinction -->

`addBuffer`가 실패하면 `fence`의 소유권은 가져가지 않으며, 전달받은 `fence`는 변경되지 않고 그대로 유지됩니다. 펜스가 신호되지 않으면 요청은 타임아웃 후 실패합니다. 이때 버퍼에는 펜스가 그대로 남아 있으며, 애플리케이션은 다른 요청에 버퍼를 재사용하기 전에 `FrameBuffer::releaseFence()`로 이 펜스를 회수해야 합니다. `Request::reuse`는 `flags`에 `ReuseBuffers`가 설정된 경우 `bufferMap_`의 각 버퍼마다 `buffer->_d()->setRequest(this)`를 호출해 그 버퍼를 현재 요청에 연결한 뒤, `_d()->pending_`에 그 버퍼를 추가합니다. `src/libcamera/request.cpp:456`, `src/libcamera/request.cpp:462`, `src/libcamera/request.cpp:391`, `src/libcamera/request.cpp:393`

`Request::reuse()`에서 `flags & ReuseBuffers`가 거짓이면 else 분기가 실행되며, 이때 `bufferMap_.clear()`를 호출해 `bufferMap_`의 모든 항목을 비웁니다. `Request::reuse`는 `status_`를 `RequestPending`으로 설정한 뒤, `controls_`와 `_d()->metadata_`를 각각 `clear()`합니다. `Request::ReuseBuffers` 플래그는 `Request::reuse()` 호출 시 `addBuffer()`로 이전에 추가한 버퍼를 다시 사용하여 기존 버퍼를 유지합니다. 다만 버퍼에 연결된 펜스는 재사용되지 않으며, 소스 주석은 펜스를 사용하는 경우 이 플래그를 피하도록 권고합니다. `src/libcamera/request.cpp:376`, `src/libcamera/request.cpp:391`, `src/libcamera/request.cpp:400`, `src/libcamera/request.cpp:402`, `src/libcamera/request.cpp:403`, `src/libcamera/request.cpp:326`, `src/libcamera/request.cpp:334`

근거 원문: [src/libcamera/request.cpp:376](#source-38494771cb29cc8c) · [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) · [src/libcamera/request.cpp:326](#source-447804db33308244) · [src/libcamera/request.cpp:456](#source-86a8d784a8348122) · [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) · [src/libcamera/request.cpp:400](#source-a98823fa5ec440a2) · [src/libcamera/request.cpp:402](#source-c8638489aa83cfd1) · [src/libcamera/request.cpp:403](#source-47569737e131b31a) · [src/libcamera/request.cpp:391](#source-e41b7fa688c1de2e) · [src/libcamera/request.cpp:393](#source-bf1ee390b8473e16) · [src/libcamera/request.cpp:334](#source-d9944a69f2dd6758)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 요청 생성부터 완료 통지까지 객체 수명과 호출 순서는 무엇입니까? | [요청 생성과 완료](#요청-생성과-완료) | 코드 근거와 설명 연결 |
    | 요청이 진행 중일 때와 완료된 뒤의 소유권, ReuseBuffers와 fence 규칙은 무엇입니까? | [소유권과 재사용](#소유권과-재사용) | 코드 근거와 설명 연결 |

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

<a id="source-a6565762f1627660"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1330"
    `src/libcamera/camera.cpp:1330`에서 시작하는 발췌입니다. 종료 줄은 1383이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `b375a7828af46db11a4e6308cc634ebb265619e76e9f173907d16d9009fe2c51`
    
    ```text
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

<a id="source-a03c9ac514bfd95e"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1339"
    `src/libcamera/camera.cpp:1339`에서 시작하는 발췌입니다. 종료 줄은 1341이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `51b2d34ec47a0b6ce4959a45e21a5ab5f667d3c996c6a152fdd85fd6e1e967b4`
    
    ```text
    if (request->_d()->camera() != this) {
    		LOG(Camera, Error) << "Request was not created by this camera";
    		return -EXDEV;
    ```

<a id="source-980d3a2f94252f0c"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1350"
    `src/libcamera/camera.cpp:1350`에서 시작하는 발췌입니다. 종료 줄은 1352이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `21331d8e4da77f65f47cb7839303a4d0b612d033f9ac661fc4c954b506495ee5`
    
    ```text
    if (request->controls().infoMap() != &controls()) {
    		LOG(Camera, Error) << "Overwriting Request::controls() is not allowed";
    		return -EINVAL;
    ```

<a id="source-d572e3b4aa0a295b"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1361"
    `src/libcamera/camera.cpp:1361`에서 시작하는 발췌입니다. 종료 줄은 1363이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `76a3abbddd8350d57239dd636efe9210ec70ee57eb0b688796169fd3c0fab9a4`
    
    ```text
    if (request->buffers().empty()) {
    		LOG(Camera, Error) << "Request contains no buffers";
    		return -EINVAL;
    ```

<a id="source-589094bc9fe6e38d"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1367"
    `src/libcamera/camera.cpp:1367`에서 시작하는 발췌입니다. 종료 줄은 1369이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `f6125338e1ec0b5e371a073942e4e5a3912505ca3b455e2fbae553e891cb8c7b`
    
    ```text
    if (d->activeStreams_.find(stream) == d->activeStreams_.end()) {
    			LOG(Camera, Error) << "Invalid request";
    			return -EINVAL;
    ```

<a id="source-605100b059a6864d"></a>

??? note "소스 근거: src/libcamera/request.cpp:475"
    `src/libcamera/request.cpp:475`에서 시작하는 발췌입니다. 종료 줄은 505이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `c1c0b55f2925856df843fa155a14bb07eb616f52b6bde75cd3b0b5a4ab03b64a`
    
    ```text
    int Request::addBuffer(const Stream *stream, FrameBuffer *buffer,
    		       std::unique_ptr<Fence> &&fence)
    {
    	if (!stream) {
    		LOG(Request, Error) << "Invalid stream reference";
    		return -EINVAL;
    	}
    
    	/*
    	 * Make sure the fence has been extracted from the buffer
    	 * to avoid waiting on a stale fence.
    	 */
    	if (buffer->_d()->fence()) {
    		LOG(Request, Error) << "Can't add buffer that still references a fence";
    		return -EEXIST;
    	}
    
    	auto [it, inserted] = bufferMap_.try_emplace(stream, buffer);
    	if (!inserted) {
    		LOG(Request, Error) << "FrameBuffer already set for stream";
    		return -EEXIST;
    	}
    
    	buffer->_d()->setRequest(this);
    	_d()->pending_.insert(buffer);
    
    	if (fence && fence->isValid())
    		buffer->_d()->setFence(std::move(fence));
    
    	return 0;
    }
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

<a id="source-bf1ee390b8473e16"></a>

??? note "소스 근거: src/libcamera/request.cpp:393"
    `src/libcamera/request.cpp:393`에서 시작하는 발췌입니다. 종료 줄은 393이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `ede3bfeddecbdb89f3d76930ab26a1c4c232bab0eb12712ce122ad99e600af8c`
    
    ```text
    buffer->_d()->setRequest(this);
    ```

<a id="source-d9944a69f2dd6758"></a>

??? note "소스 근거: src/libcamera/request.cpp:334"
    `src/libcamera/request.cpp:334`에서 시작하는 발췌입니다. 종료 줄은 334이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `7b740fbb97fdbfb9b7d270aa48ba5e7902f04d691349b58981ea011f324282d5`
    
    ```text
    This flag should not be used if fences are used.
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
    - 근거 파일: `include/libcamera/camera.h`, `include/libcamera/camera_manager.h`, `include/libcamera/request.h`, `src/libcamera/camera.cpp`, `src/libcamera/camera_manager.cpp`, `src/libcamera/request.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `293d751a81`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-31 · 사람 검토 전

다음 단계: [Pipeline Handler](pipeline-handler.md)
