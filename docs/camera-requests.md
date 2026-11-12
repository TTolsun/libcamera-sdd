---
generated_at: 2026-11-11 17:00:37+00:00
source_commit: da6a6ed33ed0ab305f10b6f8b44736150d39cef4
status: ok
section: camera-requests
generation_method: facts-and-llm
evidence_fingerprint: f80ef79d7e3ca5c83cfdaeeb641473a5f01f947e03731ba1c83a537d5d1703bf
semantic_review: human-review-required
agent: cli/claude/claude-haiku-5-5
generated_design:
  schema: 1
  input_fingerprint: f80ef79d7e3ca5c83cfdaeeb641473a5f01f947e03731ba1c83a537d5d1703bf
  answers:
    request:
    - text: '`createRequest`는 새로 만든 빈 `Request` 객체를 `std::unique_ptr<Request>`로 반환하며,
        오류가 나면 `nullptr`을 반환합니다. 반환된 객체의 소유권은 호출자에게 넘어가며, 호출자가 이를 삭제할 책임을 가집니다. 요청은
        완료 핸들러에서 삭제되거나, `Request::reuse()`로 상태를 초기화한 뒤 재사용될 수 있습니다.'
      evidence:
      - create
      covers:
      - request
      kind: behavior
      quote: "\\brief Create a request object for the camera\n * \\param[in] cookie\
        \ Opaque cookie for application use\n *\n * This function creates an empty\
        \ request for the application to fill with\n * buffers and parameters, and\
        \ queue for capture.\n *\n * The \\a cookie is stored in the request and is\
        \ accessible through the\n * Request::cookie() function at any time. It is\
        \ typically used by applications\n * to map the request to an external resource\
        \ in the request completion\n * handler, and is completely opaque to libcamera.\n\
        \ *\n * The ownership of the returned request is passed to the caller, which\
        \ is\n * responsible for deleting it. The request may be deleted in the completion\n\
        \ * handler, or reused after resetting its state with Request::reuse().\n\
        \ *\n * \\context This function is \\threadsafe. It may only be called when\
        \ the camera\n * is in the Configured or Running state as defined in \\ref\
        \ camera_operation.\n *\n * \\return A pointer to the newly created request,\
        \ or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest(uint64_t\
        \ cookie)"
      part_id: create-owner
    - text: 호출자는 `Request::addBuffer`로 한 요청에 같은 스트림의 버퍼를 둘 이상 연결해서는 안 되며, 한 요청은 스트림당
        버퍼를 하나만 포함할 수 있습니다.
      evidence:
      - buffer
      covers:
      - request
      kind: behavior
      quote: "\\brief Add a FrameBuffer with its associated Stream to the Request\n\
        \ * \\param[in] stream The stream the buffer belongs to\n * \\param[in] buffer\
        \ The FrameBuffer to add to the request\n * \\param[in] fence The optional\
        \ fence\n *\n * A reference to the buffer is stored in the request. The caller\
        \ is responsible\n * for ensuring that the buffer will remain valid until\
        \ the request complete\n * callback is called.\n *\n * A request can only\
        \ contain one buffer per stream. If a buffer has already\n * been added to\
        \ the request for the same stream, this function returns -EEXIST.\n *\n *\
        \ A Fence can be optionally associated with the \\a buffer.\n *\n * When a\
        \ valid Fence is provided to this function, \\a fence is moved to \\a\n *\
        \ buffer and this Request will only be queued to the device once the\n * fences\
        \ of all its buffers have been correctly signalled. Ownership of the\n * fence\
        \ will only be taken in case of success, otherwise the fence will\n * be left\
        \ unmodified.\n *\n * If the \\a fence associated with \\a buffer isn't signalled,\
        \ the request will\n * fail after a timeout. The buffer will still contain\
        \ the fence, which\n * applications must retrieve with FrameBuffer::releaseFence()\
        \ before the buffer\n * can be reused in another request. Attempting to add\
        \ a buffer that still\n * contains a fence to a request will result in this\
        \ function returning -EEXIST.\n *\n * \\sa FrameBuffer::releaseFence()\n *\n\
        \ * \\return 0 on success or a negative error code otherwise\n * \\retval\
        \ -EEXIST The request already contains a buffer for the stream\n *  or the\
        \ buffer still references a fence\n * \\retval -EINVAL The buffer does not\
        \ reference a valid Stream\n */\nint Request::addBuffer(const Stream *stream,\
        \ FrameBuffer *buffer,"
      part_id: attach-buffer
    - text: '`Request::addBuffer()`는 먼저 `!stream` 조건을 확인하고, 참이면 "Invalid stream reference"
        오류 로그를 남긴 뒤 `-EINVAL`을 반환합니다. 다음으로 `buffer->_d()->fence()`가 남아 있으면 `-EEXIST`를
        반환하므로, fence가 남아 있는 버퍼는 이 단계에서 등록되지 않습니다. 마지막으로 `bufferMap_.try_emplace(stream,
        buffer)`의 `inserted`가 false이면, 로그 "`FrameBuffer` already set for stream"과
        함께 `-EEXIST`를 반환합니다.'
      evidence:
      - buffer-code
      covers:
      - request
      kind: behavior
      quote: "int Request::addBuffer(const Stream *stream, FrameBuffer *buffer,\n\t\
        \t       std::unique_ptr<Fence> &&fence)\n{\n\tif (!stream) {\n\t\tLOG(Request,\
        \ Error) << \"Invalid stream reference\";\n\t\treturn -EINVAL;\n\t}"
      part_id: buffer-rejection
    - text: '`!stream` 검사, fence 검사, `inserted` 검사를 모두 통과하고 `bufferMap_.try_emplace`가
        `inserted`가 true인 경우에만 `buffer->_d()->setRequest(this)`와 `_d()->pending_.insert(buffer)`가
        이 순서대로 실행됩니다. 이 두 줄 뒤에는 fence 설정 분기가 이어지고, 함수는 `return 0;`으로 끝납니다.'
      evidence:
      - buffer-code
      covers:
      - request
      kind: behavior
      quote: "buffer->_d()->setRequest(this);\n\t_d()->pending_.insert(buffer);"
      part_id: buffer-rejection
    - text: 애플리케이션은 `createRequest()`로 요청을 만든 뒤 `queueRequest`를 호출하기 전에 그 요청에 캡처 버퍼를
        하나 이상 채워야 하며, 버퍼가 없는 요청은 큐에 넣지 않고 거부됩니다.
      evidence:
      - queue
      covers:
      - request
      kind: behavior
      quote: "\\brief Queue a request to the camera\n * \\param[in] request The request\
        \ to queue to the camera\n *\n * This function queues a \\a request to the\
        \ camera for capture.\n *\n * After allocating the request with createRequest(),\
        \ the application shall\n * fill it with at least one capture buffer before\
        \ queuing it. Requests that\n * contain no buffers are invalid and are rejected\
        \ without being queued.\n *\n * Once the request has been queued, the camera\
        \ will notify its completion\n * through the \\ref requestCompleted signal.\n\
        \ *\n * \\context This function is \\threadsafe. It may only be called when\
        \ the camera\n * is in the Running state as defined in \\ref camera_operation.\n\
        \ *\n * \\return 0 on success or a negative error code otherwise\n * \\retval\
        \ -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES\
        \ The camera is not running so requests can't be queued\n * \\retval -EXDEV\
        \ The request does not belong to this camera\n * \\retval -EINVAL The request\
        \ is invalid\n * \\retval -ENOMEM No buffer memory was available to handle\
        \ the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate\
        \ *const d = _d();"
      part_id: queue-input
    - text: '`Camera::queueRequest`는 접근 검사에서 반환하지 않고 생성 카메라 검사에 도달한 경우, 요청을 생성한 카메라가
        현재 카메라와 다르면 `-EXDEV`를 반환합니다.'
      evidence:
      - queue-owner-guard
      covers:
      - request
      kind: behavior
      quote: "if (request->_d()->camera() != this) {\n\t\tLOG(Camera, Error) << \"\
        Request was not created by this camera\";\n\t\treturn -EXDEV;"
      part_id: queue-owner
    - text: '`Camera::queueRequest`는 접근 검사와 요청을 생성한 카메라 검사를 통과해 상태 검사에 도달한 경우, `request->status()`가
        `Request::RequestPending`과 일치하지 않으면 `-EINVAL`을 반환합니다.'
      evidence:
      - queue-code
      covers:
      - request
      kind: behavior
      quote: "if (request->status() != Request::RequestPending) {\n\t\tLOG(Camera,\
        \ Error) << request->toString() << \" is not valid\";\n\t\treturn -EINVAL;\n\
        \t}"
      part_id: queue-status
    - text: '`Camera::queueRequest()`는 접근, 요청을 생성한 카메라, 요청 상태 검사에서 반환하지 않고 controls
        검사에 도달한 경우, `request->controls().infoMap()`이 `Camera::controls()`의 주소와 다르면
        `-EINVAL`을 반환합니다.'
      evidence:
      - queue-controls-guard
      covers:
      - request
      kind: behavior
      quote: "if (request->controls().infoMap() != &controls()) {\n\t\tLOG(Camera,\
        \ Error) << \"Overwriting Request::controls() is not allowed\";\n\t\treturn\
        \ -EINVAL;"
      part_id: queue-controls
    - text: '`Camera::queueRequest`가 앞선 접근·요청 생성 카메라·요청 상태·`controls` 검사를 통과해 이 검사에
        도달하면, `buffers` 목록이 비어 있는 경우 `-EINVAL`을 반환합니다. 앞선 검사에서는 접근 검사 결과가 음수이면 그 값을
        반환하고, 요청을 만든 카메라가 다르면 `-EXDEV`를, 요청 상태나 `controls` 검사가 실패하면 `-EINVAL`을 반환합니다.'
      evidence:
      - queue-buffers-guard
      - queue-code
      covers:
      - request
      kind: behavior
      quote: "if (request->buffers().empty()) {\n\t\tLOG(Camera, Error) << \"Request\
        \ contains no buffers\";\n\t\treturn -EINVAL;"
      part_id: queue-buffers
    - text: '`Camera::queueRequest`가 앞선 검사와 빈 버퍼 검사를 통과해 스트림 순회에 도달한 경우, 요청의 각 스트림이
        `activeStreams_`에 포함되어 있는지 검사하고 포함되지 않은 스트림이 있으면 `-EINVAL`을 반환합니다.'
      evidence:
      - queue-stream-guard
      covers:
      - request
      kind: behavior
      quote: "if (d->activeStreams_.find(stream) == d->activeStreams_.end()) {\n\t\
        \t\tLOG(Camera, Error) << \"Invalid request\";\n\t\t\treturn -EINVAL;"
      part_id: queue-stream
    - text: '`Camera::queueRequest()`는 요청 검사를 마친 뒤 `ConnectionTypeQueued`를 지정해 `invokeMethod`로
        `PipelineHandler::queueRequest`를 호출하고, 그 호출 뒤에 `0`을 반환합니다. 이 `0`은 `invokeMethod`
        호출 뒤의 반환값이며, 요청 완료는 카메라가 `requestCompleted` 신호로 별도로 알립니다.'
      evidence:
      - queue-code
      - queue
      covers:
      - request
      kind: behavior
      quote: "d->pipe_->invokeMethod(&PipelineHandler::queueRequest,\n\t\t\t     \
        \  ConnectionTypeQueued, request);"
      part_id: completion-signal
    lifetime:
    - text: '`Request::addBuffer`는 버퍼에 대한 참조를 요청에 저장합니다. 호출자는 요청 완료 콜백이 호출될 때까지 해당
        버퍼가 유효하게 남아 있도록 보장해야 합니다.'
      evidence:
      - buffer
      covers:
      - lifetime
      kind: behavior
      quote: "\\brief Add a FrameBuffer with its associated Stream to the Request\n\
        \ * \\param[in] stream The stream the buffer belongs to\n * \\param[in] buffer\
        \ The FrameBuffer to add to the request\n * \\param[in] fence The optional\
        \ fence\n *\n * A reference to the buffer is stored in the request. The caller\
        \ is responsible\n * for ensuring that the buffer will remain valid until\
        \ the request complete\n * callback is called.\n *\n * A request can only\
        \ contain one buffer per stream. If a buffer has already\n * been added to\
        \ the request for the same stream, this function returns -EEXIST.\n *\n *\
        \ A Fence can be optionally associated with the \\a buffer.\n *\n * When a\
        \ valid Fence is provided to this function, \\a fence is moved to \\a\n *\
        \ buffer and this Request will only be queued to the device once the\n * fences\
        \ of all its buffers have been correctly signalled. Ownership of the\n * fence\
        \ will only be taken in case of success, otherwise the fence will\n * be left\
        \ unmodified.\n *\n * If the \\a fence associated with \\a buffer isn't signalled,\
        \ the request will\n * fail after a timeout. The buffer will still contain\
        \ the fence, which\n * applications must retrieve with FrameBuffer::releaseFence()\
        \ before the buffer\n * can be reused in another request. Attempting to add\
        \ a buffer that still\n * contains a fence to a request will result in this\
        \ function returning -EEXIST.\n *\n * \\sa FrameBuffer::releaseFence()\n *\n\
        \ * \\return 0 on success or a negative error code otherwise\n * \\retval\
        \ -EEXIST The request already contains a buffer for the stream\n *  or the\
        \ buffer still references a fence\n * \\retval -EINVAL The buffer does not\
        \ reference a valid Stream\n */\nint Request::addBuffer(const Stream *stream,\
        \ FrameBuffer *buffer,"
      part_id: buffer-validity
    - text: '`Request::addBuffer`가 성공하면 유효한 `Fence`의 소유권은 `buffer`(`FrameBuffer`)로
        이동합니다. 이때 `fence`는 `buffer`로 옮겨집니다.'
      evidence:
      - fence-move
      covers:
      - lifetime
      kind: behavior
      quote: "When a valid Fence is provided to this function, \\a fence is moved\
        \ to \\a\n * buffer and this Request will only be queued to the device once\
        \ the\n * fences of all its buffers have been correctly signalled. Ownership\
        \ of the\n * fence will only be taken in case of success, otherwise the fence\
        \ will\n * be left unmodified."
      part_id: fence-transfer
    - text: '`addBuffer`가 실패하면 `fence`의 소유권은 가져가지 않으며, 전달받은 `fence`는 변경되지 않고 그대로 유지됩니다.'
      evidence:
      - fence-move
      covers:
      - lifetime
      kind: behavior
      quote: "When a valid Fence is provided to this function, \\a fence is moved\
        \ to \\a\n * buffer and this Request will only be queued to the device once\
        \ the\n * fences of all its buffers have been correctly signalled. Ownership\
        \ of the\n * fence will only be taken in case of success, otherwise the fence\
        \ will\n * be left unmodified."
      part_id: fence-failure
    - text: 펜스가 신호되지 않으면 요청은 타임아웃 후 실패합니다. 이때 버퍼에는 펜스가 그대로 남아 있으며, 애플리케이션은 다른 요청에
        버퍼를 재사용하기 전에 `FrameBuffer::releaseFence()`로 이 펜스를 회수해야 합니다.
      evidence:
      - fence-expiry
      covers:
      - lifetime
      kind: behavior
      quote: "If the \\a fence associated with \\a buffer isn't signalled, the request\
        \ will\n * fail after a timeout. The buffer will still contain the fence,\
        \ which\n * applications must retrieve with FrameBuffer::releaseFence() before\
        \ the buffer\n * can be reused in another request."
      part_id: fence-timeout
    - text: '`Request::reuse`는 `flags`에 `ReuseBuffers`가 설정된 경우 `bufferMap_`의 각 버퍼마다
        `buffer->_d()->setRequest(this)`를 호출해 그 버퍼를 현재 요청에 연결한 뒤, `_d()->pending_`에
        그 버퍼를 추가합니다.'
      evidence:
      - reuse-buffers
      - reuse-link-call
      covers:
      - lifetime
      kind: behavior
      quote: "if (flags & ReuseBuffers) {\n\t\tfor (const auto &[stream, buffer] :\
        \ bufferMap_) {\n\t\t\tbuffer->_d()->setRequest(this);\n\t\t\t_d()->pending_.insert(buffer);\n\
        \t\t}\n\t} else {\n\t\tbufferMap_.clear();\n\t}\n\n\tstatus_ = RequestPending;"
      part_id: reset-buffer-link
    - text: '`Request::reuse()`에서 `flags & ReuseBuffers`가 거짓이면 else 분기가 실행되며, 이때 `bufferMap_.clear()`를
        호출해 `bufferMap_`의 모든 항목을 비웁니다.'
      evidence:
      - reuse
      - reuse-buffers
      covers:
      - lifetime
      kind: behavior
      quote: "if (flags & ReuseBuffers) {\n\t\tfor (const auto &[stream, buffer] :\
        \ bufferMap_) {\n\t\t\tbuffer->_d()->setRequest(this);\n\t\t\t_d()->pending_.insert(buffer);\n\
        \t\t}\n\t} else {\n\t\tbufferMap_.clear();\n\t}"
      part_id: reset-buffer-clear
    - text: '`Request::reuse`는 `status_`를 `RequestPending`으로 설정한 뒤, `controls_`와 `_d()->metadata_`를
        각각 `clear()`합니다.'
      evidence:
      - reuse-status
      - reuse-controls
      - reuse-metadata
      covers:
      - lifetime
      kind: behavior
      quote: status_ = RequestPending;
      part_id: reset
    - text: '`Request::ReuseBuffers` 플래그는 `Request::reuse()` 호출 시 `addBuffer()`로 이전에
        추가한 버퍼를 다시 사용하여 기존 버퍼를 유지합니다. 다만 버퍼에 연결된 펜스는 재사용되지 않으며, 소스 주석은 펜스를 사용하는 경우
        이 플래그를 피하도록 권고합니다.'
      evidence:
      - reuse-flags
      - reuse-advice
      covers:
      - lifetime
      kind: behavior
      quote: "\\enum Request::ReuseFlag\n * Flags to control the behavior of Request::reuse()\n\
        \ * \\var Request::Default\n * Don't reuse buffers\n * \\var Request::ReuseBuffers\n\
        \ * Reuse the buffers that were previously added by addBuffer()\n *\n * \\\
        note Fences associated with the buffers are not reused.\n *  This flag should\
        \ not be used if fences are used.\n */"
      part_id: reuse-fences
  topic_inputs:
    request: 2b7d75514178f7988aad0c1834a34ff5ec86e4cba775a26fa4484c14472bb34c
    lifetime: ffc00ba2220ddaf9a9dd46a41a8c3ec1046b05445126f79e93243a66eef50def
  reused_topics:
  - lifetime
  replayed_units: []
  generated_topics:
  - request
  topic_agents:
    request: cli/claude/claude-haiku-5-5
    lifetime: cli/claude/claude-haiku-5-5
  grounding_review: not-run
  grounding_policy: 3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2
  validation_policy:
    manuscript: 367d18b95f8f0d01a15ae0f4d1b70f7e13e4d0298df4215e2c449ac4905db6f9
    semantic: 571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968
    duplicates: 93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38
    design_contracts: 9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0
    validate: 78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372
    reader_profiles: ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797
    contract_schema: d0f7ab4c48fcf52409935931eb9b93aacd48af4b19e9bb816fa496f1214fdb2f
    answer_contracts: a39c9a8818afc47e059141d486337c0f12a7fd34319e2b6f7674fc428bc83e2b
    reader_scope: 1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782
    product_context: 050c20aa2fdcceae10c6275fbb5f850f616ab5051bb67ccbcb4a204877a238d9
    explanation: 69bcaa207ef39d20f6a47ac201c3edf119f59b333e85131dea1bce85eef4006b
    design_response: a7c199bc52bcc0e749ef01186e50bca98107473d5c82e2248712f465d02e1e69
    design_validation: a4edf8364d73d169c3f10ecbadf487a8a4dc10328622d07578b281eae810c3aa
  validation_model: bbc736f073fba4b1b466e5ab1fc0b8ca33c851d77f3914fab7710622e4a42f6b
  style_policy:
    fluent-korean.md: ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975
    i-have-adhd.md: 3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9
    README.md: b87a84b1bc31079837dc4dc4527ce02c9dc2cbc3a26ff7e99e0872941d213995
  partial_revision:
    changed_units:
    - topic: request
      part: queue-owner
      native_record:
        checkpoint: 82e5d878a5a5923d0a85dc92410473e4c6b5bf202fe0bd64e468465b5de125a7.json
        topic: request
        part: queue-owner
        subpart: null
        revalidated: false
        new_grounding_review: false
        receipts:
        - 4036e38245ae41d0978823b392b7c6fe/098.receipt.json
        - 4036e38245ae41d0978823b392b7c6fe/099.receipt.json
      action: checkpoint-reused
      verified_checkpoint: C:\Users\baboe\.codex\worktrees\5dee\camera-hal-sdd-generator\build\contract-ambiguities\base\build\cli-checkpoints\82e5d878a5a5923d0a85dc92410473e4c6b5bf202fe0bd64e468465b5de125a7.json
      checkpoint_sha256: 5558fa1d23e261eaaace9c47b6aefa70dd6d072e89ea09878179a32e3aa3d12c
      native_receipts:
      - 4036e38245ae41d0978823b392b7c6fe/098.receipt.json
      - 4036e38245ae41d0978823b392b7c6fe/099.receipt.json
    - topic: request
      part: queue-status
      native_record:
        checkpoint: 786096065f59faeebbd19049271a1ea524053d5650c40b076751d2fb127c343d.json
        topic: request
        part: queue-status
        subpart: null
        revalidated: true
        new_grounding_review: false
        receipts:
        - 4036e38245ae41d0978823b392b7c6fe/100.receipt.json
        - 4036e38245ae41d0978823b392b7c6fe/101.receipt.json
      action: checkpoint-revalidated
      verified_checkpoint: C:\Users\baboe\.codex\worktrees\5dee\camera-hal-sdd-generator\build\contract-ambiguities\base\build\cli-checkpoints\786096065f59faeebbd19049271a1ea524053d5650c40b076751d2fb127c343d.json
      checkpoint_sha256: b1678aa96c9d603623a4ed003e0abef57cb88286895bd69b89e1b1e563c4ccb4
      native_receipts:
      - 4036e38245ae41d0978823b392b7c6fe/100.receipt.json
      - 4036e38245ae41d0978823b392b7c6fe/101.receipt.json
    - topic: request
      part: queue-controls
      native_record:
        checkpoint: 48ffdec6aecf62642965e973066c70047f89f59d5a08e8f917c718769e5d7be6.json
        topic: request
        part: queue-controls
        subpart: null
        revalidated: false
        new_grounding_review: false
        receipts:
        - 4036e38245ae41d0978823b392b7c6fe/102.receipt.json
        - 4036e38245ae41d0978823b392b7c6fe/103.receipt.json
      action: checkpoint-reused
      verified_checkpoint: C:\Users\baboe\.codex\worktrees\5dee\camera-hal-sdd-generator\build\contract-ambiguities\base\build\cli-checkpoints\48ffdec6aecf62642965e973066c70047f89f59d5a08e8f917c718769e5d7be6.json
      checkpoint_sha256: 567691408293b2ba2acd35e8e1ece542b68569fdd843cb01c0cfe874a86edc4d
      native_receipts:
      - 4036e38245ae41d0978823b392b7c6fe/102.receipt.json
      - 4036e38245ae41d0978823b392b7c6fe/103.receipt.json
    - topic: request
      part: queue-buffers
      native_record:
        checkpoint: 03a810bb56a71c1e1d968ff4c543df47e21914469887ad682baeb97fa4c6f44d.json
        topic: request
        part: queue-buffers
        subpart: null
        revalidated: false
        new_grounding_review: false
        receipts:
        - e04a5faa9c12474c87ee30d6893b384d/091.receipt.json
        - e04a5faa9c12474c87ee30d6893b384d/092.receipt.json
      action: checkpoint-reused
      verified_checkpoint: C:\Users\baboe\.codex\worktrees\5dee\camera-hal-sdd-generator\build\contract-ambiguities\base\build\cli-checkpoints\03a810bb56a71c1e1d968ff4c543df47e21914469887ad682baeb97fa4c6f44d.json
      checkpoint_sha256: bb641b81fda2664fcf411431362208e67709c6209fca78473fcd305707e312bf
      native_receipts:
      - e04a5faa9c12474c87ee30d6893b384d/091.receipt.json
      - e04a5faa9c12474c87ee30d6893b384d/092.receipt.json
    - topic: request
      part: queue-stream
      native_record:
        checkpoint: 4bae1d888acab25e4bf834bcd8b9634d5b7e35229f81b4f58310878eda0ffcca.json
        topic: request
        part: queue-stream
        subpart: null
        revalidated: false
        new_grounding_review: false
        receipts:
        - e04a5faa9c12474c87ee30d6893b384d/093.receipt.json
        - e04a5faa9c12474c87ee30d6893b384d/094.receipt.json
      action: checkpoint-reused
      verified_checkpoint: C:\Users\baboe\.codex\worktrees\5dee\camera-hal-sdd-generator\build\contract-ambiguities\base\build\cli-checkpoints\4bae1d888acab25e4bf834bcd8b9634d5b7e35229f81b4f58310878eda0ffcca.json
      checkpoint_sha256: 0b52d9a29a0dc9cc9308ff3de4899f4ea693232a20c923d3c084d7b6a40c3e21
      native_receipts:
      - e04a5faa9c12474c87ee30d6893b384d/093.receipt.json
      - e04a5faa9c12474c87ee30d6893b384d/094.receipt.json
    prior_manuscript_sha256: 2a2941379888dac0ff76bb0992bbaa23237d8d588a93e5a7784a58acd55534f9
    prior_revision:
      changed_units:
      - topic: request
        part: queue-owner
        native_record:
          checkpoint: 82e5d878a5a5923d0a85dc92410473e4c6b5bf202fe0bd64e468465b5de125a7.json
          topic: request
          part: queue-owner
          subpart: null
          revalidated: false
          new_grounding_review: false
          receipts:
          - 4036e38245ae41d0978823b392b7c6fe/098.receipt.json
          - 4036e38245ae41d0978823b392b7c6fe/099.receipt.json
        verified_checkpoint: C:\Users\baboe\.codex\worktrees\5dee\camera-hal-sdd-generator\build\contract-ambiguities\base\build\cli-checkpoints\82e5d878a5a5923d0a85dc92410473e4c6b5bf202fe0bd64e468465b5de125a7.json
        checkpoint_sha256: 5558fa1d23e261eaaace9c47b6aefa70dd6d072e89ea09878179a32e3aa3d12c
        native_receipts:
        - 4036e38245ae41d0978823b392b7c6fe/098.receipt.json
        - 4036e38245ae41d0978823b392b7c6fe/099.receipt.json
      - topic: request
        part: queue-status
        native_record:
          checkpoint: 786096065f59faeebbd19049271a1ea524053d5650c40b076751d2fb127c343d.json
          topic: request
          part: queue-status
          subpart: null
          revalidated: false
          new_grounding_review: false
          receipts:
          - 4036e38245ae41d0978823b392b7c6fe/100.receipt.json
          - 4036e38245ae41d0978823b392b7c6fe/101.receipt.json
        verified_checkpoint: C:\Users\baboe\.codex\worktrees\5dee\camera-hal-sdd-generator\build\contract-ambiguities\base\build\cli-checkpoints\786096065f59faeebbd19049271a1ea524053d5650c40b076751d2fb127c343d.json
        checkpoint_sha256: b1678aa96c9d603623a4ed003e0abef57cb88286895bd69b89e1b1e563c4ccb4
        native_receipts:
        - 4036e38245ae41d0978823b392b7c6fe/100.receipt.json
        - 4036e38245ae41d0978823b392b7c6fe/101.receipt.json
      - topic: request
        part: queue-controls
        native_record:
          checkpoint: 48ffdec6aecf62642965e973066c70047f89f59d5a08e8f917c718769e5d7be6.json
          topic: request
          part: queue-controls
          subpart: null
          revalidated: false
          new_grounding_review: false
          receipts:
          - 4036e38245ae41d0978823b392b7c6fe/102.receipt.json
          - 4036e38245ae41d0978823b392b7c6fe/103.receipt.json
        verified_checkpoint: C:\Users\baboe\.codex\worktrees\5dee\camera-hal-sdd-generator\build\contract-ambiguities\base\build\cli-checkpoints\48ffdec6aecf62642965e973066c70047f89f59d5a08e8f917c718769e5d7be6.json
        checkpoint_sha256: 567691408293b2ba2acd35e8e1ece542b68569fdd843cb01c0cfe874a86edc4d
        native_receipts:
        - 4036e38245ae41d0978823b392b7c6fe/102.receipt.json
        - 4036e38245ae41d0978823b392b7c6fe/103.receipt.json
      - topic: request
        part: queue-buffers
        native_record:
          checkpoint: 03a810bb56a71c1e1d968ff4c543df47e21914469887ad682baeb97fa4c6f44d.json
          topic: request
          part: queue-buffers
          subpart: null
          revalidated: false
          new_grounding_review: false
          receipts:
          - e04a5faa9c12474c87ee30d6893b384d/091.receipt.json
          - e04a5faa9c12474c87ee30d6893b384d/092.receipt.json
        verified_checkpoint: C:\Users\baboe\.codex\worktrees\5dee\camera-hal-sdd-generator\build\contract-ambiguities\base\build\cli-checkpoints\03a810bb56a71c1e1d968ff4c543df47e21914469887ad682baeb97fa4c6f44d.json
        checkpoint_sha256: bb641b81fda2664fcf411431362208e67709c6209fca78473fcd305707e312bf
        native_receipts:
        - e04a5faa9c12474c87ee30d6893b384d/091.receipt.json
        - e04a5faa9c12474c87ee30d6893b384d/092.receipt.json
      - topic: request
        part: queue-stream
        native_record:
          checkpoint: 4bae1d888acab25e4bf834bcd8b9634d5b7e35229f81b4f58310878eda0ffcca.json
          topic: request
          part: queue-stream
          subpart: null
          revalidated: false
          new_grounding_review: false
          receipts:
          - e04a5faa9c12474c87ee30d6893b384d/093.receipt.json
          - e04a5faa9c12474c87ee30d6893b384d/094.receipt.json
        verified_checkpoint: C:\Users\baboe\.codex\worktrees\5dee\camera-hal-sdd-generator\build\contract-ambiguities\base\build\cli-checkpoints\4bae1d888acab25e4bf834bcd8b9634d5b7e35229f81b4f58310878eda0ffcca.json
        checkpoint_sha256: 0b52d9a29a0dc9cc9308ff3de4899f4ea693232a20c923d3c084d7b6a40c3e21
        native_receipts:
        - e04a5faa9c12474c87ee30d6893b384d/093.receipt.json
        - e04a5faa9c12474c87ee30d6893b384d/094.receipt.json
      prior_manuscript_sha256: 14e30766a16a31fc141453ff835a01bc7489b156f7017f713705165cf3c505a4
      prior_revision:
        changed_units:
        - topic: request
          part: queue-buffers
          native_record: null
        - topic: request
          part: queue-stream
          native_record: null
        prior_manuscript_sha256: 493764a46d7c33eab59bc2ef8358b56e0f2127b1f2b6ecde79308bf8be04264b
        retained_topic_identities: Historical identities retained; no current-profile
          reuse promotion
        retained_statement_count: 17
        human_review: pending
      prior_grounding_review: passed
      retained_topic_identities: Historical identities retained; no current-profile
        reuse promotion
      retained_statement_count: 14
      new_unit_grounding_review: passed; common native validation and receipt-bound
        checkpoints verified
      new_unit_agent:
        runner: codex
        model: gpt-6.1-terra
        command: []
        args:
        - -c
        - model_reasoning_effort="high"
      human_review: pending
    prior_grounding_review: not-run
    retained_topic_identities: Historical identities retained; no current-profile
      reuse promotion
    retained_statement_count: 14
    selected_unit_grounding_review: passed; may reuse historical grounding; see each
      unit action and native receipts
    new_unit_agent:
      runner: codex
      model: gpt-6.1-terra
      command: []
      args:
      - -c
      - model_reasoning_effort="high"
    human_review: pending
  body_sha256: c24c738d0638acf6263f2cdf7e5e6e29031610a8d5b38b10caa29dd6db8414e4
managed_visual_refresh:
- schema: 1
  source_commit: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
  original_manuscript_sha256: f4b5f9fc862ef062cae2ff57a2a787da1eb2416e244e20d98f76e2c3e64b4014
  previous_body_sha256: 9f4e9bfb67cb5ebac3f35d65f6f98b8edac5ad58dd56b4d91cf7e6e57ff5e12e
  body_sha256: c24c738d0638acf6263f2cdf7e5e6e29031610a8d5b38b10caa29dd6db8414e4
  visual_definitions_sha256: 8a2e0af8b81a6474a6637d7b49190ddbfe9edbc37d2234b796ae1bbfeda5d591
  unchanged_native_records_sha256: 44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a
  preserved_outside_body_sha256: bca4ae4276f4952ad6dd83d5729ed0524bd15a6c4f83ece6ae55d6238b1f29f6
  owned_edit_regions:
  - original_start_byte: 1059
    original_end_byte: 4952
    original_sha256: 77f7162b7ec23fc254e6926483e6171500212fcf0a0326d15f89400b76f8f274
    replacement_sha256: 77f7162b7ec23fc254e6926483e6171500212fcf0a0326d15f89400b76f8f274
    visual_ids:
    - add-buffer-rejections
  - original_start_byte: 4954
    original_end_byte: 7098
    original_sha256: d0a46e9eb6b40fa5aee6ac7169ce8a807ebf0da2b2ff3b2eb55801a36c819565
    replacement_sha256: 0d0cae9c45fafdb13adc3a87f5815119d94fb7471566fc507995f4b61d3e9703
    visual_ids:
    - queue-return-completion
    - queued-request-data-checks
  - original_start_byte: 11292
    original_end_byte: 14277
    original_sha256: 60051c2aa25024c18b51dbfebd9ff586fe5e0218a907bbefc39843a401afc53b
    replacement_sha256: 60051c2aa25024c18b51dbfebd9ff586fe5e0218a907bbefc39843a401afc53b
    visual_ids:
    - request-ownership
  - original_start_byte: 14279
    original_end_byte: 17036
    original_sha256: 04a0e9c3a2f474ae5f98c996371e88ad1b5653972351dabee7025a5d9fddfb6c
    replacement_sha256: 04a0e9c3a2f474ae5f98c996371e88ad1b5653972351dabee7025a5d9fddfb6c
    visual_ids:
    - timeout-fence-recovery
  - original_start_byte: 17038
    original_end_byte: 19203
    original_sha256: 1bab6d08593000b855cbb24b278d5b6c42c59ea759437dde3bb9b97f45b7bfaf
    replacement_sha256: 1bab6d08593000b855cbb24b278d5b6c42c59ea759437dde3bb9b97f45b7bfaf
    visual_ids:
    - reuse-buffer-relink
  - original_start_byte: 19205
    original_end_byte: 21879
    original_sha256: 37eedccadde23aded5d0d2e8735b39dea6c70d14fda0abe0222a4f6c266ab1d1
    replacement_sha256: 650998e98d62d7549fa1e9a2b2384630e193e0442e5fa9c328cfc764628d362c
    visual_ids:
    - reuse-buffer-fence-distinction
    - add-buffer-fence-transfer
  added_visuals:
  - add-buffer-fence-transfer
  - queued-request-data-checks
  scope: Configured figure reassembly only; figure authorship remains per visual
  new_inference: false
  semantic_approval: false
  human_review: unchanged
revalidated_from: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
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
%% sdd:translations {"-EEXIST: 남은 fence": "-EEXIST: retained fence", "-EEXIST: 중복 stream": "-EEXIST: duplicate stream", "-EINVAL 반환": "Return -EINVAL", "0 반환": "Return 0", "stream이 비었나요?": "Is stream null?", "stream이 이미 등록됐나요?": "Is the stream already <br/>registered?", "버퍼에 fence가 남았나요?": "Does the buffer retain a <br/>fence?", "아니요": "No", "예": "Yes", "요청 연결과 pending#95; 추가": "Attach request and add <br/>pending#95;", "유효한 fence가 있으면 <br/>이동한 뒤 반환": "Move a valid supplied fence <br/>if present, then return"}
  v_stream{"stream이 비었나요?"}
  v_invalid["-EINVAL 반환"]
  v_fence{"버퍼에 fence가 남았나요?"}
  v_retained["-EEXIST: 남은 fence"]
  v_duplicate{"stream이 이미 등록됐나요?"}
  v_existing["-EEXIST: 중복 stream"]
  v_attach["요청 연결과 pending#95; 추가"]
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
    | <span data-sdd-label-en="Is stream null?">stream이 비었나요?</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Return -EINVAL">-EINVAL 반환</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Does the buffer retain a fence?">버퍼에 fence가 남았나요?</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="-EEXIST: retained fence">-EEXIST: 남은 fence</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Is the stream already registered?">stream이 이미 등록됐나요?</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="-EEXIST: duplicate stream">-EEXIST: 중복 stream</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Attach request and add pending_">요청 연결과 pending&#95; 추가</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Return 0">0 반환</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Yes">예</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="No">아니요</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Yes">예</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="No">아니요</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Yes">예</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="No">아니요</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Move a valid supplied fence if present, then return">유효한 fence가 있으면 이동한 뒤 반환</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
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
    | <span data-sdd-label-en="Invoke with ConnectionTypeQueued">ConnectionTypeQueued 호출</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | <span data-sdd-label-en="queueRequest returns 0">queueRequest: 0 반환</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | <span data-sdd-label-en="Queued request">큐에 넣은 요청</span> | [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) |
    | <span data-sdd-label-en="Notify completion through requestCompleted">완료 시 requestCompleted 알림</span> | [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) |
    | <span data-sdd-label-en="Return after invoking">호출 뒤 반환</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | <span data-sdd-label-en="API completion-notification contract">API의 완료 알림 계약</span> | [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) |
<!-- /sdd:visual:queue-return-completion -->

<!-- sdd:visual:queued-request-data-checks -->
### 요청 데이터의 거절 조건

```mermaid
flowchart TB
%% sdd:translations {"같은 제어 맵입니다.": "The control info map <br/>matches.", "다른 제어 맵입니다.": "The control info map <br/>differs.", "대기 상태가 아닙니다.": "The request is not pending.", "대기 상태입니다.": "The request is pending.", "모든 스트림이 활성 목록에 <br/>있습니다.": "Every stream is in the <br/>active set.", "버퍼가 없습니다.": "There are no buffers.", "버퍼가 있습니다.": "There are buffers.", "아니오.": "No.", "연결된 모든 버퍼의 스트림이 <br/>활성 스트림입니까?": "Does every attached buffer <br/>belong to an active stream?", "예.": "Yes.", "요청 데이터 검사에서 <br/>-EINVAL을 반환합니다.": "Return -EINVAL from the <br/>failed request-data check.", "요청 상태가 <br/>RequestPending입니까?": "Is the request still <br/>RequestPending?", "요청에 버퍼가 한 개 이상 <br/>있습니까?": "Does the request contain at <br/>least one buffer?", "요청을 만든 카메라가 달라 <br/>-EXDEV를 반환합니다.": "Return -EXDEV because a <br/>different camera created <br/>the request.", "접근 검사를 통과한 요청이 <br/>현재 카메라에서 <br/>만들어졌습니까?": "After the access check <br/>passes, did this camera <br/>create the request?", "제어 목록의 infoMap이 현재 <br/>카메라의 제어 맵입니까?": "Does the control list use <br/>this camera’s control info <br/>map?", "제어를 사전 처리하고 <br/>파이프라인 큐 호출을 <br/>비동기로 예약한 뒤 0을 <br/>반환합니다.": "Preprocess controls, queue <br/>the asynchronous pipeline <br/>call, and return 0.", "활성 목록에 없는 스트림이 <br/>있습니다.": "A stream is absent from the <br/>active set."}
  v_camera{"접근 검사를 통과한 요청이 <br/>현재 카메라에서 <br/>만들어졌습니까?"}
  v_wrong-camera["요청을 만든 카메라가 달라 <br/>-EXDEV를 반환합니다."]
  v_status{"요청 상태가 <br/>RequestPending입니까?"}
  v_controls{"제어 목록의 infoMap이 현재 <br/>카메라의 제어 맵입니까?"}
  v_buffers{"요청에 버퍼가 한 개 이상 <br/>있습니까?"}
  v_streams{"연결된 모든 버퍼의 스트림이 <br/>활성 스트림입니까?"}
  v_invalid["요청 데이터 검사에서 <br/>-EINVAL을 반환합니다."]
  v_submit["제어를 사전 처리하고 <br/>파이프라인 큐 호출을 <br/>비동기로 예약한 뒤 0을 <br/>반환합니다."]
  v_camera -->|"아니오."| v_wrong-camera
  v_camera -->|"예."| v_status
  v_status -->|"대기 상태가 아닙니다."| v_invalid
  v_status -->|"대기 상태입니다."| v_controls
  v_controls -->|"다른 제어 맵입니다."| v_invalid
  v_controls -->|"같은 제어 맵입니다."| v_buffers
  v_buffers -->|"버퍼가 없습니다."| v_invalid
  v_buffers -->|"버퍼가 있습니다."| v_streams
  v_streams -->|"활성 목록에 없는 스트림이 <br/>있습니다."| v_invalid
  v_streams -->|"모든 스트림이 활성 목록에 <br/>있습니다."| v_submit
```

[Mermaid 원문](camera-requests.queued-request-data-checks.mmd)

??? note "그림 근거와 확인 범위"
    접근 검사를 통과한 뒤 큐에 제출하는 요청의 소속·상태·제어·버퍼에서 어떤 값이 거절됩니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="After the access check passes, did this camera create the request?">접근 검사를 통과한 요청이 현재 카메라에서 만들어졌습니까?</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | <span data-sdd-label-en="Return -EXDEV because a different camera created the request.">요청을 만든 카메라가 달라 -EXDEV를 반환합니다.</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | <span data-sdd-label-en="Is the request still RequestPending?">요청 상태가 RequestPending입니까?</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | <span data-sdd-label-en="Does the control list use this camera’s control info map?">제어 목록의 infoMap이 현재 카메라의 제어 맵입니까?</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | <span data-sdd-label-en="Does the request contain at least one buffer?">요청에 버퍼가 한 개 이상 있습니까?</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | <span data-sdd-label-en="Does every attached buffer belong to an active stream?">연결된 모든 버퍼의 스트림이 활성 스트림입니까?</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | <span data-sdd-label-en="Return -EINVAL from the failed request-data check.">요청 데이터 검사에서 -EINVAL을 반환합니다.</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) · [src/libcamera/camera.cpp:1350](#source-980d3a2f94252f0c) · [src/libcamera/camera.cpp:1361](#source-d572e3b4aa0a295b) · [src/libcamera/camera.cpp:1367](#source-589094bc9fe6e38d) |
    | <span data-sdd-label-en="Preprocess controls, queue the asynchronous pipeline call, and return 0.">제어를 사전 처리하고 파이프라인 큐 호출을 비동기로 예약한 뒤 0을 반환합니다.</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | <span data-sdd-label-en="No.">아니오.</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | <span data-sdd-label-en="Yes.">예.</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | <span data-sdd-label-en="The request is not pending.">대기 상태가 아닙니다.</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) · [src/libcamera/camera.cpp:1350](#source-980d3a2f94252f0c) · [src/libcamera/camera.cpp:1361](#source-d572e3b4aa0a295b) · [src/libcamera/camera.cpp:1367](#source-589094bc9fe6e38d) |
    | <span data-sdd-label-en="The request is pending.">대기 상태입니다.</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | <span data-sdd-label-en="The control info map differs.">다른 제어 맵입니다.</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) · [src/libcamera/camera.cpp:1350](#source-980d3a2f94252f0c) · [src/libcamera/camera.cpp:1361](#source-d572e3b4aa0a295b) · [src/libcamera/camera.cpp:1367](#source-589094bc9fe6e38d) |
    | <span data-sdd-label-en="The control info map matches.">같은 제어 맵입니다.</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | <span data-sdd-label-en="There are no buffers.">버퍼가 없습니다.</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) · [src/libcamera/camera.cpp:1350](#source-980d3a2f94252f0c) · [src/libcamera/camera.cpp:1361](#source-d572e3b4aa0a295b) · [src/libcamera/camera.cpp:1367](#source-589094bc9fe6e38d) |
    | <span data-sdd-label-en="There are buffers.">버퍼가 있습니다.</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
    | <span data-sdd-label-en="A stream is absent from the active set.">활성 목록에 없는 스트림이 있습니다.</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) · [src/libcamera/camera.cpp:1350](#source-980d3a2f94252f0c) · [src/libcamera/camera.cpp:1361](#source-d572e3b4aa0a295b) · [src/libcamera/camera.cpp:1367](#source-589094bc9fe6e38d) |
    | <span data-sdd-label-en="Every stream is in the active set.">모든 스트림이 활성 목록에 있습니다.</span> | [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) |
<!-- /sdd:visual:queued-request-data-checks -->

`Request::addBuffer()`는 먼저 `!stream` 조건을 확인하고, 참이면 "Invalid stream reference" 오류 로그를 남긴 뒤 `-EINVAL`을 반환합니다. 다음으로 `buffer->_d()->fence()`가 남아 있으면 `-EEXIST`를 반환하므로, fence가 남아 있는 버퍼는 이 단계에서 등록되지 않습니다. 마지막으로 `bufferMap_.try_emplace(stream, buffer)`의 `inserted`가 false이면, 로그 "`FrameBuffer` already set for stream"과 함께 `-EEXIST`를 반환합니다. `src/libcamera/request.cpp:475`

`!stream` 검사, fence 검사, `inserted` 검사를 모두 통과하고 `bufferMap_.try_emplace`가 `inserted`가 true인 경우에만 `buffer->_d()->setRequest(this)`와 `_d()->pending_.insert(buffer)`가 이 순서대로 실행됩니다. 이 두 줄 뒤에는 fence 설정 분기가 이어지고, 함수는 `return 0;`으로 끝납니다. 애플리케이션은 `createRequest()`로 요청을 만든 뒤 `queueRequest`를 호출하기 전에 그 요청에 캡처 버퍼를 하나 이상 채워야 하며, 버퍼가 없는 요청은 큐에 넣지 않고 거부됩니다. `Camera::queueRequest`는 접근 검사에서 반환하지 않고 생성 카메라 검사에 도달한 경우, 요청을 생성한 카메라가 현재 카메라와 다르면 `-EXDEV`를 반환합니다. `src/libcamera/request.cpp:475`, `src/libcamera/camera.cpp:1308`, `src/libcamera/camera.cpp:1339`

`Camera::queueRequest`는 접근 검사와 요청을 생성한 카메라 검사를 통과해 상태 검사에 도달한 경우, `request->status()`가 `Request::RequestPending`과 일치하지 않으면 `-EINVAL`을 반환합니다. `Camera::queueRequest()`는 접근, 요청을 생성한 카메라, 요청 상태 검사에서 반환하지 않고 controls 검사에 도달한 경우, `request->controls().infoMap()`이 `Camera::controls()`의 주소와 다르면 `-EINVAL`을 반환합니다. `src/libcamera/camera.cpp:1330`, `src/libcamera/camera.cpp:1350`

`Camera::queueRequest`가 앞선 접근·요청 생성 카메라·요청 상태·`controls` 검사를 통과해 이 검사에 도달하면, `buffers` 목록이 비어 있는 경우 `-EINVAL`을 반환합니다. 앞선 검사에서는 접근 검사 결과가 음수이면 그 값을 반환하고, 요청을 만든 카메라가 다르면 `-EXDEV`를, 요청 상태나 `controls` 검사가 실패하면 `-EINVAL`을 반환합니다. `Camera::queueRequest`가 앞선 검사와 빈 버퍼 검사를 통과해 스트림 순회에 도달한 경우, 요청의 각 스트림이 `activeStreams_`에 포함되어 있는지 검사하고 포함되지 않은 스트림이 있으면 `-EINVAL`을 반환합니다. `src/libcamera/camera.cpp:1361`, `src/libcamera/camera.cpp:1330`, `src/libcamera/camera.cpp:1367`

`Camera::queueRequest()`는 요청 검사를 마친 뒤 `ConnectionTypeQueued`를 지정해 `invokeMethod`로 `PipelineHandler::queueRequest`를 호출하고, 그 호출 뒤에 `0`을 반환합니다. 이 `0`은 `invokeMethod` 호출 뒤의 반환값이며, 요청 완료는 카메라가 `requestCompleted` 신호로 별도로 알립니다. `src/libcamera/camera.cpp:1330`, `src/libcamera/camera.cpp:1308`

근거 원문: [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) · [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) · [src/libcamera/camera.cpp:1330](#source-a6565762f1627660) · [src/libcamera/camera.cpp:1339](#source-a03c9ac514bfd95e) · [src/libcamera/camera.cpp:1350](#source-980d3a2f94252f0c) · [src/libcamera/camera.cpp:1361](#source-d572e3b4aa0a295b) · [src/libcamera/camera.cpp:1367](#source-589094bc9fe6e38d) · [src/libcamera/request.cpp:475](#source-605100b059a6864d)

## 소유권과 재사용

`Request::addBuffer`는 버퍼에 대한 참조를 요청에 저장합니다. 호출자는 요청 완료 콜백이 호출될 때까지 해당 버퍼가 유효하게 남아 있도록 보장해야 합니다. `Request::addBuffer`가 성공하면 유효한 `Fence`의 소유권은 `buffer`(`FrameBuffer`)로 이동합니다. 이때 `fence`는 `buffer`로 옮겨집니다. `src/libcamera/request.cpp:442`, `src/libcamera/request.cpp:456`

<!-- sdd:visual:request-ownership -->
### 요청과 버퍼를 유지할 기간

```mermaid
flowchart TB
%% sdd:translations {"Request가 버퍼를 참조": "Request references buffer", "addBuffer#40;#41;": "addBuffer#40;#41;", "reuse#40;#41; 후 다시 제출": "Reset before requeue", "완료 핸들러에서 삭제 가능": "May delete in completion <br/>handler", "요청 삭제": "Delete request", "요청 완료 콜백": "Request completion callback", "이 시점까지 버퍼를 유효하게 <br/>유지": "Keep buffer valid until <br/>this point", "재사용 전 상태 초기화": "Reset state before reuse", "호출자가 Request를 소유": "Caller owns Request"}
  v_caller["호출자가 Request를 소유"]
  v_buffer["Request가 버퍼를 참조"]
  v_callback["요청 완료 콜백"]
  v_delete["요청 삭제"]
  v_reuse["reuse#40;#41; 후 다시 제출"]
  v_caller -->|"addBuffer#40;#41;"| v_buffer
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
    | <span data-sdd-label-en="Caller owns Request">호출자가 Request를 소유</span> | [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) |
    | <span data-sdd-label-en="Request references buffer">Request가 버퍼를 참조</span> | [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) |
    | <span data-sdd-label-en="Request completion callback">요청 완료 콜백</span> | [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) |
    | <span data-sdd-label-en="Delete request">요청 삭제</span> | [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) |
    | <span data-sdd-label-en="Reset before requeue">reuse&#40;&#41; 후 다시 제출</span> | [src/libcamera/request.cpp:376](#source-38494771cb29cc8c) |
    | <span data-sdd-label-en="addBuffer()">addBuffer&#40;&#41;</span> | [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) |
    | <span data-sdd-label-en="Keep buffer valid until this point">이 시점까지 버퍼를 유효하게 유지</span> | [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) |
    | <span data-sdd-label-en="May delete in completion handler">완료 핸들러에서 삭제 가능</span> | [src/libcamera/camera.cpp:1243](#source-0ae00d77839f61cb) |
    | <span data-sdd-label-en="Reset state before reuse">재사용 전 상태 초기화</span> | [src/libcamera/request.cpp:376](#source-38494771cb29cc8c) |
<!-- /sdd:visual:request-ownership -->

<!-- sdd:visual:timeout-fence-recovery -->
### 타임아웃 뒤 펜스 회수

```mermaid
flowchart TB
%% sdd:translations {"그 뒤 다른 요청에서 버퍼 <br/>재사용": "Then reuse the buffer in <br/>another request", "버퍼에 펜스가 남음": "Buffer still contains its <br/>fence", "애플리케이션이 <br/>releaseFence#40;#41;로 회수": "Application retrieves with <br/>releaseFence#40;#41;", "요청 실패 뒤에도 유지": "Remains after request <br/>failure", "재사용 전 회수 의무": "Must retrieve before reuse", "펜스 미신호: 요청 타임아웃": "Unsignalled fence: request <br/>times out", "회수 후 재사용 가능": "Reuse after retrieval"}
  v_timeout["펜스 미신호: 요청 타임아웃"]
  v_retained["버퍼에 펜스가 남음"]
  v_retrieve["애플리케이션이 <br/>releaseFence#40;#41;로 회수"]
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
    | <span data-sdd-label-en="Unsignalled fence: request times out">펜스 미신호: 요청 타임아웃</span> | [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) |
    | <span data-sdd-label-en="Buffer still contains its fence">버퍼에 펜스가 남음</span> | [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) |
    | <span data-sdd-label-en="Application retrieves with releaseFence()">애플리케이션이 releaseFence&#40;&#41;로 회수</span> | [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) |
    | <span data-sdd-label-en="Then reuse the buffer in another request">그 뒤 다른 요청에서 버퍼 재사용</span> | [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) |
    | <span data-sdd-label-en="Remains after request failure">요청 실패 뒤에도 유지</span> | [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) |
    | <span data-sdd-label-en="Must retrieve before reuse">재사용 전 회수 의무</span> | [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) |
    | <span data-sdd-label-en="Reuse after retrieval">회수 후 재사용 가능</span> | [src/libcamera/request.cpp:462](#source-d8cf34a75a4333a7) |
<!-- /sdd:visual:timeout-fence-recovery -->

<!-- sdd:visual:reuse-buffer-relink -->
### 재사용 버퍼의 요청 연결

```mermaid
flowchart TB
%% sdd:translations {"ReuseBuffers: 기존 <br/>bufferMap#95; 순회": "ReuseBuffers: iterate <br/>existing bufferMap#95;", "각 기존 버퍼의 연결 갱신": "Update each retained buffer <br/>link", "각 버퍼를 pending#95;에 추가": "Insert each buffer into <br/>pending#95;", "각 버퍼의 setRequest#40;this#41;": "setRequest#40;this#41; on each <br/>buffer", "연결한 뒤 대기 집합에 추가": "Insert into pending after <br/>relinking"}
  v_retained["ReuseBuffers: 기존 <br/>bufferMap#95; 순회"]
  v_request["각 버퍼의 setRequest#40;this#41;"]
  v_pending["각 버퍼를 pending#95;에 추가"]
  v_retained -->|"각 기존 버퍼의 연결 갱신"| v_request
  v_request -->|"연결한 뒤 대기 집합에 추가"| v_pending
```

[Mermaid 원문](camera-requests.reuse-buffer-relink.mmd)

??? note "그림 근거와 확인 범위"
    ReuseBuffers 경로에서 각 버퍼는 어떤 순서로 다시 요청에 연결됩니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="ReuseBuffers: iterate existing bufferMap_">ReuseBuffers: 기존 bufferMap&#95; 순회</span> | [src/libcamera/request.cpp:391](#source-e41b7fa688c1de2e) |
    | <span data-sdd-label-en="setRequest(this) on each buffer">각 버퍼의 setRequest&#40;this&#41;</span> | [src/libcamera/request.cpp:391](#source-e41b7fa688c1de2e) |
    | <span data-sdd-label-en="Insert each buffer into pending_">각 버퍼를 pending&#95;에 추가</span> | [src/libcamera/request.cpp:391](#source-e41b7fa688c1de2e) |
    | <span data-sdd-label-en="Update each retained buffer link">각 기존 버퍼의 연결 갱신</span> | [src/libcamera/request.cpp:391](#source-e41b7fa688c1de2e) |
    | <span data-sdd-label-en="Insert into pending after relinking">연결한 뒤 대기 집합에 추가</span> | [src/libcamera/request.cpp:391](#source-e41b7fa688c1de2e) |
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
    | <span data-sdd-label-en="ReuseBuffers">ReuseBuffers</span> | [src/libcamera/request.cpp:326](#source-447804db33308244) |
    | <span data-sdd-label-en="Reuse buffers previously added by addBuffer">앞서 addBuffer로 넣은 버퍼 재사용</span> | [src/libcamera/request.cpp:326](#source-447804db33308244) |
    | <span data-sdd-label-en="Associated fences are not reused">연결된 펜스는 재사용하지 않음</span> | [src/libcamera/request.cpp:326](#source-447804db33308244) |
    | <span data-sdd-label-en="Should not use this flag with fences">펜스를 쓰면 이 플래그를 피하도록 권고</span> | [src/libcamera/request.cpp:326](#source-447804db33308244) |
    | <span data-sdd-label-en="Flag reuse scope">플래그의 재사용 범위</span> | [src/libcamera/request.cpp:326](#source-447804db33308244) |
    | <span data-sdd-label-en="Distinguish buffer and fence reuse">버퍼와 펜스의 범위 구분</span> | [src/libcamera/request.cpp:326](#source-447804db33308244) |
    | <span data-sdd-label-en="API should-not recommendation">API의 should not 권고</span> | [src/libcamera/request.cpp:326](#source-447804db33308244) |
<!-- /sdd:visual:reuse-buffer-fence-distinction -->

<!-- sdd:visual:add-buffer-fence-transfer -->
### addBuffer의 펜스 소유권

```mermaid
flowchart TB
%% sdd:translations {"버퍼 추가 결과를 확인합니다.": "Check the result of adding <br/>the buffer.", "버퍼 추가가 성공했습니까?": "Did adding the buffer <br/>succeed?", "성공했습니다.": "Adding the buffer succeeded.", "실패하면 펜스 소유권은 <br/>호출자에게 남습니다.": "On failure, the caller <br/>retains fence ownership.", "실패했습니다.": "Adding the buffer failed.", "유효한 펜스가 없습니다.": "No valid fence was supplied.", "유효한 펜스가 없으면 <br/>소유권을 옮기지 않습니다.": "Without a valid fence, <br/>there is no fence ownership <br/>transfer.", "유효한 펜스를 제공했습니까?": "Was a valid fence supplied?", "유효한 펜스를 제공했습니다.": "A valid fence was supplied.", "유효한 펜스의 소유권을 <br/>FrameBuffer로 옮깁니다.": "Move ownership of the valid <br/>fence to the FrameBuffer.", "호출자가 addBuffer에 펜스를 <br/>제공할 수 있습니다.": "The caller can supply a <br/>fence to addBuffer."}
  v_input["호출자가 addBuffer에 펜스를 <br/>제공할 수 있습니다."]
  v_result{"버퍼 추가가 성공했습니까?"}
  v_caller["실패하면 펜스 소유권은 <br/>호출자에게 남습니다."]
  v_valid{"유효한 펜스를 제공했습니까?"}
  v_buffer["유효한 펜스의 소유권을 <br/>FrameBuffer로 옮깁니다."]
  v_none["유효한 펜스가 없으면 <br/>소유권을 옮기지 않습니다."]
  v_input -->|"버퍼 추가 결과를 확인합니다."| v_result
  v_result -->|"실패했습니다."| v_caller
  v_result -->|"성공했습니다."| v_valid
  v_valid -->|"유효한 펜스를 제공했습니다."| v_buffer
  v_valid -->|"유효한 펜스가 없습니다."| v_none
```

[Mermaid 원문](camera-requests.add-buffer-fence-transfer.mmd)

??? note "그림 근거와 확인 범위"
    addBuffer의 성공과 실패에 따라 호출자가 제공한 유효한 펜스를 누가 소유합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="The caller can supply a fence to addBuffer.">호출자가 addBuffer에 펜스를 제공할 수 있습니다.</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Did adding the buffer succeed?">버퍼 추가가 성공했습니까?</span> | [src/libcamera/request.cpp:456](#source-86a8d784a8348122) |
    | <span data-sdd-label-en="On failure, the caller retains fence ownership.">실패하면 펜스 소유권은 호출자에게 남습니다.</span> | [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) |
    | <span data-sdd-label-en="Was a valid fence supplied?">유효한 펜스를 제공했습니까?</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Move ownership of the valid fence to the FrameBuffer.">유효한 펜스의 소유권을 FrameBuffer로 옮깁니다.</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Without a valid fence, there is no fence ownership transfer.">유효한 펜스가 없으면 소유권을 옮기지 않습니다.</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Check the result of adding the buffer.">버퍼 추가 결과를 확인합니다.</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) · [src/libcamera/request.cpp:456](#source-86a8d784a8348122) |
    | <span data-sdd-label-en="Adding the buffer failed.">실패했습니다.</span> | [src/libcamera/request.cpp:456](#source-86a8d784a8348122) · [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) |
    | <span data-sdd-label-en="Adding the buffer succeeded.">성공했습니다.</span> | [src/libcamera/request.cpp:456](#source-86a8d784a8348122) · [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="A valid fence was supplied.">유효한 펜스를 제공했습니다.</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="No valid fence was supplied.">유효한 펜스가 없습니다.</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
<!-- /sdd:visual:add-buffer-fence-transfer -->

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
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `be7e83e913`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-12 · 사람 검토 전

다음 단계: [Pipeline Handler](pipeline-handler.md)
