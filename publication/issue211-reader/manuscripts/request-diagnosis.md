---
generated_at: 2026-10-31T04:15:55+00:00
source_commit: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61
status: ok
section: request-diagnosis
generation_method: facts-and-llm
evidence_fingerprint: 3b0f9b18c924ab6260433bb4e51f6e43e0eee509d22841493d89b7bd015ace78
semantic_review: human-review-required
agent: cli/claude/claude-haiku-5-5
generated_design: {"schema": 1, "input_fingerprint": "3b0f9b18c924ab6260433bb4e51f6e43e0eee509d22841493d89b7bd015ace78", "answers": {"configuration-failure": [{"text": "`Camera::configure`에서 `d->isAccessAllowed(Private::CameraAcquired, Private::CameraConfigured)` 호출의 반환값 `ret`을 호출 직후에 관찰하고, `if (ret < 0)` 분기에 들어가는지 기록하는 것을 제안합니다. `ret`이 음수이면 `return ret;`이 실행되어 `configure`는 같은 값을 반환하고, 그 뒤의 `cfg.setStream(nullptr)` 초기화, `config->validate()` 검사, `PipelineHandler::configure` 호출과 `Configured` 상태 전환이 실행되지 않습니다. 따라서 반환값이 음수일 때 `configuring streams:` 로그와 `Can't configure camera with invalid configuration` 로그가 나타나지 않는지 확인하고, `ret`이 0 이상이면 분기를 건너뛰어 뒤쪽 실행 경로를 이어서 기록합니다.", "evidence": ["configure-access"], "covers": ["configuration-failure"], "kind": "behavior", "quote": "int ret = d->isAccessAllowed(Private::CameraAcquired,\n\t\t\t\t     Private::CameraConfigured);\n\tif (ret < 0)\n\t\treturn ret;", "part_id": "entry"}, {"text": "조사 계획으로 `isAccessAllowed` 호출에서 먼저 `allowDisconnected`가 거짓이고 `disconnected_`가 참인지 확인합니다. 이 조건이 참이면 `-ENODEV`를 반환하는 선행 분기이므로, 이후 `currentState`·`low`·`high` 비교 관찰과 구분하여 기록합니다.", "evidence": ["access"], "covers": ["configuration-failure"], "kind": "behavior", "quote": "int Camera::Private::isAccessAllowed(State low, State high,\n\t\t\t\t     bool allowDisconnected,\n\t\t\t\t     const char *from) const\n{\n\tif (!allowDisconnected && disconnected_)\n\t\treturn -ENODEV;", "part_id": "access"}, {"text": "선행 분기를 통과하면 `currentState`가 `low`와 `high` 범위 안에 있는지 비교하고, 범위 안이면 `0`을 반환하는 위치를 관찰합니다. 범위 밖이면 `ASSERT`, `LOG(Camera, Error)` 출력, `-EACCES` 반환 위치를 순서대로 기록합니다.", "evidence": ["state-range"], "covers": ["configuration-failure"], "kind": "behavior", "quote": "State currentState = state_.load(std::memory_order_acquire);\n\tif (currentState >= low && currentState <= high)\n\t\treturn 0;\n\n\tASSERT(static_cast<unsigned int>(low) < std::size(camera_state_names) &&\n\t       static_cast<unsigned int>(high) < std::size(camera_state_names));\n\n\tLOG(Camera, Error) << \"Camera in \" << camera_state_names[currentState]\n\t\t\t   << \" state trying \" << from\n\t\t\t   << \"() requiring state between \"\n\t\t\t   << camera_state_names[low] << \" and \"\n\t\t\t   << camera_state_names[high];\n\n\treturn -EACCES;", "part_id": "access"}, {"text": "`CameraConfiguration::validate()`가 `CameraConfiguration::Adjusted`를 반환하면 구성은 유효하도록 조정된 상태이며, 이 경우 임의의 스트림에서 파라미터가 변경되거나 스트림 구성이 삭제될 수 있습니다.", "evidence": ["validate", "validation-changes"], "covers": ["configuration-failure"], "kind": "behavior", "quote": "Parameters may have changed for any stream, and stream\n * configurations may have been removed.", "part_id": "validation-effects"}, {"text": "`CameraConfiguration::Adjusted`가 반환되면 호출자는 설정을 주의 깊게 확인해야 합니다.", "evidence": ["validation-caller"], "covers": ["configuration-failure"], "kind": "behavior", "quote": "The caller shall check the\n * configuration carefully.", "part_id": "validation-caller"}, {"text": "조사 항목으로 `Camera::configure`에서 `config->validate()`의 반환값을 `CameraConfiguration::Valid`와 비교한 결과를 기록하고, 두 값이 같지 않을 때 `LOG(Camera, Error)`로 \"Can't configure camera with invalid configuration\"을 남긴 뒤 `pipe_->invokeMethod` 호출 전에 `-EINVAL`을 반환하는지 확인하는 것을 제안합니다.", "evidence": ["validation-check"], "covers": ["configuration-failure"], "kind": "behavior", "quote": "if (config->validate() != CameraConfiguration::Valid) {\n\t\tLOG(Camera, Error)\n\t\t\t<< \"Can't configure camera with invalid configuration\";\n\t\treturn -EINVAL;", "part_id": "validation-result"}, {"text": "`Camera::configure`에서 `config->validate()`를 호출하는 지점의 호출 스택을 기록하면서 `config`의 실제 타입과 `validate` 구현 위치를 함께 확인하는 것을 제안합니다. 또한 `pipe_->invokeMethod(&PipelineHandler::configure, ConnectionTypeBlocking, this, config)` 호출 직후 `ret` 값을 관찰하여 0이 아닌 `ret`이 `if (ret)` 분기에서 그대로 `return ret`으로 반환되는지 확인하고, `invokeMethod`가 연결한 실제 `PipelineHandler::configure` 구현을 호출 스택에 함께 기록하는 것을 제안합니다.", "evidence": ["configure-code", "validation-check"], "covers": ["configuration-failure"], "kind": "behavior", "quote": "ret = d->pipe_->invokeMethod(&PipelineHandler::configure,\n\t\t\t\t     ConnectionTypeBlocking, this, config);\n\tif (ret)\n\t\treturn ret;", "part_id": "device-configure"}, {"text": "`Camera::configure`의 `for (const StreamConfiguration &cfg : *config)` 반복문에서 `Stream *stream = cfg.stream();`으로 얻은 `stream`이 null이면 `if (!stream)` 분기가 실행됩니다. 이 분기에서 관찰할 위치는 `LOG(Camera, Fatal)` 출력 문자열 `Pipeline handler failed to update stream configuration`, `d->activeStreams_.clear()` 호출, `return -EINVAL;` 반환값입니다. 반환 뒤에는 `d->setState(Private::CameraConfigured)`와 `return 0;`에 도달하지 않으므로, 반환값이 `-EINVAL`인지와 상태 전환이 일어나지 않는지를 함께 기록하는 것을 제안합니다. 이 소스 조각에는 호출자가 `-EINVAL`을 받은 뒤의 복구 코드가 없으므로, 복구 여부는 이 근거만으로 판단할 수 없습니다.", "evidence": ["stream-check"], "covers": ["configuration-failure"], "kind": "behavior", "quote": "Stream *stream = cfg.stream();\n\t\tif (!stream) {\n\t\t\tLOG(Camera, Fatal)\n\t\t\t\t<< \"Pipeline handler failed to update stream configuration\";\n\t\t\td->activeStreams_.clear();\n\t\t\treturn -EINVAL;", "part_id": "stream-link"}], "diagnosis": [{"text": "조사 항목으로 `queueRequest` 호출의 반환값과 호출한 파일 위치를 함께 기록하는 것을 제안합니다. 반환값이 0이면 정상 접수, 음수 오류 코드이면 제출 오류로 나누어 구분할 수 있습니다. 0 반환은 접수 성공만 나타내므로 촬영 완료 여부와는 별도 항목으로 둡니다.", "evidence": ["queue"], "covers": ["diagnosis"], "kind": "behavior", "quote": "\\brief Queue a request to the camera\n * \\param[in] request The request to queue to the camera\n *\n * This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.\n *\n * \\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)\n{\n\tPrivate *const d = _d();", "part_id": "submission"}, {"text": "`Request::addBuffer()`에서 두 `-EEXIST` 원인을 나누는 관찰 지점은 펜스 검사 분기와 `try_emplace` 뒤의 `inserted`입니다. `buffer->_d()->fence()`가 참이면 로그 `Can't add buffer that still references a fence`를 남기고 `-EEXIST`를 반환하며, 이 경우 `bufferMap_`에 삽입을 시도하지 않습니다. 이 검사를 통과해 `try_emplace`에 도달했다면 `-EEXIST`는 `inserted`가 false일 때만 나오고, 로그는 `FrameBuffer already set for stream`입니다. 두 경로 모두 `-EEXIST`를 반환하므로 반환값만으로는 원인을 단정할 수 없으며, 분기 직전의 `fence()` 결과, `inserted` 값, 로그 문자열을 함께 확인합니다.", "evidence": ["buffer-code", "buffer"], "covers": ["diagnosis"], "kind": "behavior", "quote": "auto [it, inserted] = bufferMap_.try_emplace(stream, buffer);\n\tif (!inserted) {\n\t\tLOG(Request, Error) << \"FrameBuffer already set for stream\";\n\t\treturn -EEXIST;\n\t}", "part_id": "buffer-error"}, {"text": "조사 계획입니다. `doQueueRequests(Camera *camera)`는 `data->waitingRequests_`가 빌 때까지 반복하며, 각 반복의 시작에서 `data->queuedRequests_.size()`가 `maxQueuedRequestsDevice_`와 같은지 확인합니다. 같으면 `break`로 반복을 빠져나가므로, 관찰할 항목은 두 값, 분기 진입 여부, 그 시점의 `waitingRequests_` 크기입니다. 이 분기는 `waitingRequests_.pop()`과 `doQueueRequest(request)` 호출보다 앞에 있으므로, 한도에 도달해 빠져나간 요청은 대기 큐의 앞에 그대로 남아 있습니다.", "evidence": ["device-queue"], "covers": ["diagnosis"], "kind": "behavior", "quote": "/**\n * \\brief Queue prepared requests to the device\n *\n * Iterate the list of waiting requests and queue them to the device one\n * by one if they have been prepared.\n */\nvoid PipelineHandler::doQueueRequests(Camera *camera)\n{\n\tCamera::Private *data = camera->_d();\n\twhile (!data->waitingRequests_.empty()) {\n\t\tif (data->queuedRequests_.size() == maxQueuedRequestsDevice_)\n\t\t\tbreak;", "part_id": "capacity"}, {"text": "`doQueueRequests`에서 `data->waitingRequests_.front()`가 가리키는 선두 요청의 `request->_d()->prepared_` 값을 기록하는 것을 제안합니다. 값이 거짓이면 `break`가 `while` 반복문을 끝내며, 이 시점은 `pop()` 호출 전이므로 해당 요청은 `waitingRequests_` 선두에 그대로 남습니다. 함께 `queuedRequests_.size()`와 `maxQueuedRequestsDevice_`의 비교 결과, 그리고 `break` 직후 `waitingRequests_`의 크기가 변하지 않았는지를 기록하면 두 종료 경로를 구분할 수 있습니다. 값이 참이면 `pop()` 후 `doQueueRequest(request)`가 호출되는 순서가 소스대로 실행되는지 확인 항목으로 남기는 것을 제안합니다.", "evidence": ["prepared-branch"], "covers": ["diagnosis"], "kind": "behavior", "quote": "Request *request = data->waitingRequests_.front();\n\t\tif (!request->_d()->prepared_)\n\t\t\tbreak;", "part_id": "preparation"}, {"text": "`doQueueRequest`에서 `request->_d()->cancelled_`가 참이면 `completeRequest(request)`를 호출한 뒤 `return`으로 함수를 반환하므로 `queueRequestDevice`는 호출되지 않으며, 조사에서는 `cancelled_` 값과 `completeRequest` 호출 여부를 기록하는 것을 제안합니다.", "evidence": ["cancelled-branch"], "covers": ["diagnosis"], "kind": "behavior", "quote": "if (request->_d()->cancelled_) {\n\t\tcompleteRequest(request);\n\t\treturn;", "part_id": "cancelled"}, {"text": "`doQueueRequest`는 `cancelled_`가 거짓인 경우에만 `int ret = queueRequestDevice(camera, request)`의 결과인 `ret`를 확인하며, `ret`가 0이 아니면 `cancelRequest(request)`를 호출하고 0이면 이 분기에서 추가로 호출하는 함수가 없으므로, 조사에서는 `ret` 값과 `cancelRequest` 호출 여부를 기록하는 것을 제안합니다.", "evidence": ["device-result-branch"], "covers": ["diagnosis"], "kind": "behavior", "quote": "int ret = queueRequestDevice(camera, request);\n\tif (ret)\n\t\tcancelRequest(request);", "part_id": "cancelled"}, {"text": "`completeBuffer`는 파이프라인 핸들러가 요청에 속한 버퍼 하나의 완료를 알릴 때 호출해야 합니다. 이 함수는 `bufferCompleted` 신호를 방출해 애플리케이션에 버퍼 완료를 알린 뒤, `request->_d()->completeBuffer(buffer)`의 결과를 그대로 반환합니다. 문서상 반환값 `true`는 요청에 포함된 모든 버퍼가 완료되었음을, `false`는 그렇지 않음을 뜻하므로, 각 호출의 반환값을 버퍼별로 기록해 마지막 버퍼에서만 `true`가 나오는지 확인하는 방법을 제안합니다. 다만 `true`가 반환되어도 요청은 자동으로 완료되지 않으므로, 핸들러는 `completeRequest`를 별도로 호출해야 합니다.", "evidence": ["completion"], "covers": ["diagnosis"], "kind": "behavior", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}", "part_id": "buffer-completion"}, {"text": "`completeRequest()`는 `data->queuedRequests_`의 맨 앞 요청 `req`의 `req->status()`가 `Request::RequestPending`이면 `break`로 while 루프를 빠져나가, 그 요청을 큐에 남깁니다. `Request::RequestPending`이 아닌 경우에만 `ASSERT(!req->hasPendingBuffers());` 식을 검사하고, 그다음 `pop_front()`로 제거한 뒤 `camera->requestComplete(req)`로 통지합니다. 따라서 맨 앞 요청이 Pending이면 그 뒤에 완료된 요청이 있어도 이 호출에서는 검사되지 않아 `requestComplete()`로 반환되지 않습니다. 관찰 계획으로는 루프 진입 시 `req->status()` 값, `break` 도달 여부, `!req->hasPendingBuffers()` 결과, `pop_front()` 이후 `queuedRequests_` 크기와 `requestComplete` 호출 순서를 기록하는 것을 제안합니다.", "evidence": ["completion"], "covers": ["diagnosis"], "kind": "behavior", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;", "part_id": "pending-head"}]}, "topic_inputs": {"configuration-failure": "0827e6f6f1b05a3bec7306d36f7ce9399afd79f368e040092b0ed613e9e68db9", "diagnosis": "a118b932413eb96396d24c23e115084bd486509cbe89e29cf9e0cd8be65eebcd"}, "reused_topics": ["configuration-failure"], "replayed_units": [], "generated_topics": ["diagnosis"], "topic_agents": {"configuration-failure": "cli/claude/claude-haiku-5-5", "diagnosis": "cli/claude/claude-haiku-5-5"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "e0c429a5c80a01c34563ce00a616df89d8f75c735f8669bcbd1f75d84cce82a6", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "2f593eec0430a4e6b5822e642c0a7a1227fc150a0b27d8a71f521acf93b6439e", "answer_contracts": "1e0d24e0cf26ded53ecec2e5a6fbc51836bac6e17530318a9fa7cffaa936c00b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "9db4d42a710b4a71a7d2bb16f69db06926409281dc1a200c796e77d5deaa25a0", "design_response": "deb70dda7ad27f001267e4a9712c5b0dc1fe9fa67acd13bedbfefaaad0ad83c8", "design_validation": "946deebb694018f6361ee86669e1a7a26cd61dfffef11bb3a7de0a193639fabe"}, "validation_model": "2eb3bf27fc8fdca03721abcecc71d006bc0c9612049018fdc117931887213ef9", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "f8fd5a3d8041c23fc68b93ff32b8727e98393383b5099032eb00ad0013e7611c"}, "reuse_lineage": {"source_commit": "293d751a814e0d4c34e85ad457ccd9d5eefd1a61", "body_sha256": "932eb366c6d960558410657b893e12d89422c93091eeccbdf3f1fbb2ccc54422", "topics": ["configuration-failure"], "validation": "current source, contract and editorial checks; human review pending"}, "checkpoint_units": [{"checkpoint": "7797edd05123c1072b01e1dc1daa139fdb3a617fbadd96a9bf028dec819807d1.json", "topic": "diagnosis", "part": "submission", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["b7bce1f7c7b24cbfb9741c54a1b20738/001.receipt.json", "b7bce1f7c7b24cbfb9741c54a1b20738/002.receipt.json"]}, {"checkpoint": "6fd97134729558568fdc4d5e747ce7a08a9905f5cc02412b74211e1129a7fac9.json", "topic": "diagnosis", "part": "buffer-error", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["da17812372884b868977a2ebbb032d76/017.receipt.json", "da17812372884b868977a2ebbb032d76/018.receipt.json"]}, {"checkpoint": "c5b14afe7efc6e26954697703952d7c6df937b34c3fe52dbff79e57ac6d9dd85.json", "topic": "diagnosis", "part": "capacity", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["da17812372884b868977a2ebbb032d76/019.receipt.json", "da17812372884b868977a2ebbb032d76/020.receipt.json"]}, {"checkpoint": "6e49696a343ac090d4a08ba19ec3bbcb3a30e35dc64b542bfcfb560524edcb1b.json", "topic": "diagnosis", "part": "preparation", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["da17812372884b868977a2ebbb032d76/021.receipt.json", "da17812372884b868977a2ebbb032d76/022.receipt.json"]}, {"checkpoint": "d464315580a12d1a8f8f0544df364596e4c93d3b01bb7d0bdd425d97ece063d8.json", "topic": "diagnosis", "part": "cancelled", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["da17812372884b868977a2ebbb032d76/023.receipt.json", "da17812372884b868977a2ebbb032d76/024.receipt.json"]}, {"checkpoint": "bae4cdea6be5c7428b4cf60c6d4b61856779d07cf33bd80d56ae4bb36d9be400.json", "topic": "diagnosis", "part": "buffer-completion", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["e79c61fcf15044bc979becc197414576/003.receipt.json", "e79c61fcf15044bc979becc197414576/004.receipt.json"]}], "body_sha256": "1f7b363cf0635e73ac7c3562d5478df805070a9a549d2f4347d9c8240ca45d42"}
---

# 구성과 요청 오류 조사

**실패가 발생한 상태 검사·설정·제출·장치 처리 위치를 좁히세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 요청의 제출 성공과 촬영 완료를 구분하고, 버퍼를 유지할 기간과 오류가 난 위치를 확인하세요. | [요청 처리와 문제 진단](request-lifecycle.md) |

## 구성 실패를 좁히는 순서

`Camera::configure`에서 `d->isAccessAllowed(Private::CameraAcquired, Private::CameraConfigured)` 호출의 반환값 `ret`을 호출 직후에 관찰하고, `if (ret < 0)` 분기에 들어가는지 기록하는 것을 제안합니다. `ret`이 음수이면 `return ret;`이 실행되어 `configure`는 같은 값을 반환하고, 그 뒤의 `cfg.setStream(nullptr)` 초기화, `config->validate()` 검사, `PipelineHandler::configure` 호출과 `Configured` 상태 전환이 실행되지 않습니다. 따라서 반환값이 음수일 때 `configuring streams:` 로그와 `Can't configure camera with invalid configuration` 로그가 나타나지 않는지 확인하고, `ret`이 0 이상이면 분기를 건너뛰어 뒤쪽 실행 경로를 이어서 기록합니다. `src/libcamera/camera.cpp:1195`

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

[Mermaid 원문](request-diagnosis.configure-failures.mmd)

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

조사 계획으로 `isAccessAllowed` 호출에서 먼저 `allowDisconnected`가 거짓이고 `disconnected_`가 참인지 확인합니다. 이 조건이 참이면 `-ENODEV`를 반환하는 선행 분기이므로, 이후 `currentState`·`low`·`high` 비교 관찰과 구분하여 기록합니다. 선행 분기를 통과하면 `currentState`가 `low`와 `high` 범위 안에 있는지 비교하고, 범위 안이면 `0`을 반환하는 위치를 관찰합니다. 범위 밖이면 `ASSERT`, `LOG(Camera, Error)` 출력, `-EACCES` 반환 위치를 순서대로 기록합니다. `src/libcamera/camera.cpp:709`, `src/libcamera/camera.cpp:716`

`CameraConfiguration::validate()`가 `CameraConfiguration::Adjusted`를 반환하면 구성은 유효하도록 조정된 상태이며, 이 경우 임의의 스트림에서 파라미터가 변경되거나 스트림 구성이 삭제될 수 있습니다. `CameraConfiguration::Adjusted`가 반환되면 호출자는 설정을 주의 깊게 확인해야 합니다. 조사 항목으로 `Camera::configure`에서 `config->validate()`의 반환값을 `CameraConfiguration::Valid`와 비교한 결과를 기록하고, 두 값이 같지 않을 때 `LOG(Camera, Error)`로 "Can't configure camera with invalid configuration"을 남긴 뒤 `pipe_->invokeMethod` 호출 전에 `-EINVAL`을 반환하는지 확인하는 것을 제안합니다. `src/libcamera/camera.cpp:323`, `src/libcamera/camera.cpp:342`, `src/libcamera/camera.cpp:343`, `src/libcamera/camera.cpp:1203`

`Camera::configure`에서 `config->validate()`를 호출하는 지점의 호출 스택을 기록하면서 `config`의 실제 타입과 `validate` 구현 위치를 함께 확인하는 것을 제안합니다. 또한 `pipe_->invokeMethod(&PipelineHandler::configure, ConnectionTypeBlocking, this, config)` 호출 직후 `ret` 값을 관찰하여 0이 아닌 `ret`이 `if (ret)` 분기에서 그대로 `return ret`으로 반환되는지 확인하고, `invokeMethod`가 연결한 실제 `PipelineHandler::configure` 구현을 호출 스택에 함께 기록하는 것을 제안합니다. `src/libcamera/camera.cpp:1191`, `src/libcamera/camera.cpp:1203`

`Camera::configure`의 `for (const StreamConfiguration &cfg : *config)` 반복문에서 `Stream *stream = cfg.stream();`으로 얻은 `stream`이 null이면 `if (!stream)` 분기가 실행됩니다. 이 분기에서 관찰할 위치는 `LOG(Camera, Fatal)` 출력 문자열 `Pipeline handler failed to update stream configuration`, `d->activeStreams_.clear()` 호출, `return -EINVAL;` 반환값입니다. 반환 뒤에는 `d->setState(Private::CameraConfigured)`와 `return 0;`에 도달하지 않으므로, 반환값이 `-EINVAL`인지와 상태 전환이 일어나지 않는지를 함께 기록하는 것을 제안합니다. 이 소스 조각에는 호출자가 `-EINVAL`을 받은 뒤의 복구 코드가 없으므로, 복구 여부는 이 근거만으로 판단할 수 없습니다. `src/libcamera/camera.cpp:1225`

근거 원문: [src/libcamera/camera.cpp:1163](#source-4e218db5e20840dc) · [src/libcamera/camera.cpp:709](#source-1e64f4ece8808997) · [src/libcamera/camera.cpp:323](#source-cb5242e98ac1e72c) · [src/libcamera/camera.cpp:1191](#source-846c5a830281fa6a) · [src/libcamera/camera.cpp:716](#source-9328b9e82bc716a1) · [src/libcamera/camera.cpp:342](#source-e13fede0aa40ada1) · [src/libcamera/camera.cpp:343](#source-e5758fc43bf244cd) · [src/libcamera/camera.cpp:1203](#source-fcc2510602fe412b) · [src/libcamera/camera.cpp:1225](#source-fa2c87e2c2f4e322) · [src/libcamera/camera.cpp:1195](#source-2da795dd561f56ec)

## 실패 위치별 확인 순서

조사 항목으로 `queueRequest` 호출의 반환값과 호출한 파일 위치를 함께 기록하는 것을 제안합니다. 반환값이 0이면 정상 접수, 음수 오류 코드이면 제출 오류로 나누어 구분할 수 있습니다. 0 반환은 접수 성공만 나타내므로 촬영 완료 여부와는 별도 항목으로 둡니다. `src/libcamera/camera.cpp:1308`

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

[Mermaid 원문](request-diagnosis.queue-gates.mmd)

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

`Request::addBuffer()`에서 두 `-EEXIST` 원인을 나누는 관찰 지점은 펜스 검사 분기와 `try_emplace` 뒤의 `inserted`입니다. `buffer->_d()->fence()`가 참이면 로그 `Can't add buffer that still references a fence`를 남기고 `-EEXIST`를 반환하며, 이 경우 `bufferMap_`에 삽입을 시도하지 않습니다. 이 검사를 통과해 `try_emplace`에 도달했다면 `-EEXIST`는 `inserted`가 false일 때만 나오고, 로그는 `FrameBuffer already set for stream`입니다. 두 경로 모두 `-EEXIST`를 반환하므로 반환값만으로는 원인을 단정할 수 없으며, 분기 직전의 `fence()` 결과, `inserted` 값, 로그 문자열을 함께 확인합니다. `src/libcamera/request.cpp:475`, `src/libcamera/request.cpp:442`

조사 계획입니다. `doQueueRequests(Camera *camera)`는 `data->waitingRequests_`가 빌 때까지 반복하며, 각 반복의 시작에서 `data->queuedRequests_.size()`가 `maxQueuedRequestsDevice_`와 같은지 확인합니다. 같으면 `break`로 반복을 빠져나가므로, 관찰할 항목은 두 값, 분기 진입 여부, 그 시점의 `waitingRequests_` 크기입니다. 이 분기는 `waitingRequests_.pop()`과 `doQueueRequest(request)` 호출보다 앞에 있으므로, 한도에 도달해 빠져나간 요청은 대기 큐의 앞에 그대로 남아 있습니다. `src/libcamera/pipeline_handler.cpp:428`

`doQueueRequests`에서 `data->waitingRequests_.front()`가 가리키는 선두 요청의 `request->_d()->prepared_` 값을 기록하는 것을 제안합니다. 값이 거짓이면 `break`가 `while` 반복문을 끝내며, 이 시점은 `pop()` 호출 전이므로 해당 요청은 `waitingRequests_` 선두에 그대로 남습니다. 함께 `queuedRequests_.size()`와 `maxQueuedRequestsDevice_`의 비교 결과, 그리고 `break` 직후 `waitingRequests_`의 크기가 변하지 않았는지를 기록하면 두 종료 경로를 구분할 수 있습니다. 값이 참이면 `pop()` 후 `doQueueRequest(request)`가 호출되는 순서가 소스대로 실행되는지 확인 항목으로 남기는 것을 제안합니다. `src/libcamera/pipeline_handler.cpp:516`

`doQueueRequest`에서 `request->_d()->cancelled_`가 참이면 `completeRequest(request)`를 호출한 뒤 `return`으로 함수를 반환하므로 `queueRequestDevice`는 호출되지 않으며, 조사에서는 `cancelled_` 값과 `completeRequest` 호출 여부를 기록하는 것을 제안합니다. `doQueueRequest`는 `cancelled_`가 거짓인 경우에만 `int ret = queueRequestDevice(camera, request)`의 결과인 `ret`를 확인하며, `ret`가 0이 아니면 `cancelRequest(request)`를 호출하고 0이면 이 분기에서 추가로 호출하는 함수가 없으므로, 조사에서는 `ret` 값과 `cancelRequest` 호출 여부를 기록하는 것을 제안합니다. `src/libcamera/pipeline_handler.cpp:493`, `src/libcamera/pipeline_handler.cpp:498`

`completeBuffer`는 파이프라인 핸들러가 요청에 속한 버퍼 하나의 완료를 알릴 때 호출해야 합니다. 이 함수는 `bufferCompleted` 신호를 방출해 애플리케이션에 버퍼 완료를 알린 뒤, `request->_d()->completeBuffer(buffer)`의 결과를 그대로 반환합니다. 문서상 반환값 `true`는 요청에 포함된 모든 버퍼가 완료되었음을, `false`는 그렇지 않음을 뜻하므로, 각 호출의 반환값을 버퍼별로 기록해 마지막 버퍼에서만 `true`가 나오는지 확인하는 방법을 제안합니다. 다만 `true`가 반환되어도 요청은 자동으로 완료되지 않으므로, 핸들러는 `completeRequest`를 별도로 호출해야 합니다. `src/libcamera/pipeline_handler.cpp:547`

`completeRequest()`는 `data->queuedRequests_`의 맨 앞 요청 `req`의 `req->status()`가 `Request::RequestPending`이면 `break`로 while 루프를 빠져나가, 그 요청을 큐에 남깁니다. `Request::RequestPending`이 아닌 경우에만 `ASSERT(!req->hasPendingBuffers());` 식을 검사하고, 그다음 `pop_front()`로 제거한 뒤 `camera->requestComplete(req)`로 통지합니다. 따라서 맨 앞 요청이 Pending이면 그 뒤에 완료된 요청이 있어도 이 호출에서는 검사되지 않아 `requestComplete()`로 반환되지 않습니다. 관찰 계획으로는 루프 진입 시 `req->status()` 값, `break` 도달 여부, `!req->hasPendingBuffers()` 결과, `pop_front()` 이후 `queuedRequests_` 크기와 `requestComplete` 호출 순서를 기록하는 것을 제안합니다. `src/libcamera/pipeline_handler.cpp:547`

근거 원문: [src/libcamera/camera.cpp:1308](#source-28d007de6ad1a8a5) · [src/libcamera/request.cpp:442](#source-95ae69eeb085e3b1) · [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) · [src/libcamera/pipeline_handler.cpp:516](#source-a637b7daf9acb7ac) · [src/libcamera/pipeline_handler.cpp:493](#source-0bb6ebc961be6e80) · [src/libcamera/pipeline_handler.cpp:498](#source-1e06e477d10056b7) · [src/libcamera/request.cpp:475](#source-605100b059a6864d)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 제출 실패와 제출 후 완료 지연을 어떻게 구분합니까? | [실패 위치별 확인 순서](#실패-위치별-확인-순서) | 코드 근거와 설명 연결 |
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

<a id="source-a637b7daf9acb7ac"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:516"
    `src/libcamera/pipeline_handler.cpp:516`에서 시작하는 발췌입니다. 종료 줄은 518이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `f655f79ce0ac9e9361d1759b2974e6f382b7fe1e9e3aa35b51952572af8d5a6f`
    
    ```text
    Request *request = data->waitingRequests_.front();
    		if (!request->_d()->prepared_)
    			break;
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

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `include/libcamera/camera.h`, `include/libcamera/internal/pipeline_handler.h`, `include/libcamera/request.h`, `src/libcamera/camera.cpp`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/request.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `293d751a81`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-31 · 사람 검토 전

다음 단계: [Pipeline Handler](pipeline-handler.md)
