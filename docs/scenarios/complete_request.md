---
generated_at: 2026-11-11T20:47:59+00:00
source_commit: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
status: ok
section: scenario-complete_request
generation_method: facts-and-llm
scenario_id: complete_request
entry: PipelineHandler::completeRequest(Request *)
scenario_fingerprint: cd861883aaa4fa13d5e12af7800b8d3eca0fb9fbf81fdb726d2a03f57c4a010e
evidence_fingerprint: ac54592b16f2effb314534c2a61325df29d46b723d0009b56bd9ff994e122adb
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "ac54592b16f2effb314534c2a61325df29d46b723d0009b56bd9ff994e122adb", "answers": {"delivery": [{"text": "`Request::Private::complete`는 요청 상태가 `RequestPending`이고 대기 버퍼가 없는지 `ASSERT`로 검사합니다. 이어서 `cancelled_`가 참이면 상태를 `RequestCancelled`로, 거짓이면 `RequestComplete`로 갱신합니다. `ASSERT`는 `log.h`를 포함하기 전에 `NDEBUG`가 정의되면 코드를 생성하지 않습니다.", "evidence": ["request", "logging"], "covers": ["delivery"], "kind": "behavior", "quote": "ASSERT(request->status() == RequestPending);\n\tASSERT(!hasPendingBuffers());", "part_id": "answer"}, {"text": "`PipelineHandler::completeRequest`는 전달받은 요청을 완료 처리한 뒤 `queuedRequests_`를 앞에서부터 확인합니다. 맨 앞 요청이 `RequestPending`이면 `break`하여 그 요청을 제거하지 않습니다. 그렇지 않으면 대기 버퍼가 없는지 `ASSERT`로 검사하고 `pop_front`로 제거한 뒤 `Camera::requestComplete`를 호출합니다.", "evidence": ["complete"], "covers": ["delivery"], "kind": "behavior", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;", "part_id": "answer"}, {"text": "`Camera::requestComplete`는 `allowDisconnected=true`로 `CameraStopping`부터 `CameraRunning`까지의 상태를 검사합니다. 상태가 이 범위 안이면 `requestCompleted.emit(request)`로 알립니다. 범위 밖이면 `Fatal` 로그를 출력하고 실행을 중단합니다.", "evidence": ["notification", "state", "logging"], "covers": ["delivery"], "kind": "behavior", "quote": "\\brief Handle request completion and notify application\n * \\param[in] request The request that has completed\n *\n * This function is called by the pipeline handler to notify the camera that\n * the request has completed. It emits the requestCompleted signal.\n */\nvoid Camera::requestComplete(Request *request)\n{\n\t/* Disconnected cameras are still able to complete requests. */\n\tif (_d()->isAccessAllowed(Private::CameraStopping, Private::CameraRunning,\n\t\t\t\t  true))\n\t\tLOG(Camera, Fatal) << \"Trying to complete a request when stopped\";", "part_id": "answer"}, {"text": "`PipelineHandler::completeRequest`는 정상 경로에서 루프 뒤에 `doQueueRequests(camera)`를 호출하여 대기 중인 요청을 파이프라인에 큐잉할 수 있게 합니다.", "evidence": ["complete"], "covers": ["delivery"], "kind": "behavior", "quote": "/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}", "part_id": "answer"}], "responsibility": [{"text": "파이프라인 핸들러는 `CameraManager` 스레드에서 `completeBuffer`를 호출해야 하며, 이 함수는 버퍼 완료를 알린 뒤 요청의 내부 버퍼 추적을 갱신합니다. 모든 버퍼가 완료되고 필요한 추가 작업을 마친 뒤 핸들러는 같은 스레드에서 `completeRequest`를 호출해 카메라에 요청 완료를 알려야 하며, 이 함수가 반환한 뒤에는 해당 요청에 접근해서는 안 됩니다. `completeRequest`의 함수 반환 시점과 별개로 요청은 앱에 제출 순서대로 반환됩니다. 공통 `cancelRequest`는 `Request::Private::cancel`이 정상 복귀한 뒤 직접 `completeRequest`를 호출하며, `doCancelRequest`의 버퍼 완료 알림 자체가 요청 완료를 보장하지는 않습니다.", "evidence": ["buffer", "complete", "ordered-completion", "pipeline-cancel", "cancel-private", "cancel-details"], "covers": ["responsibility"], "kind": "behavior", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}", "part_id": "caller-completion-boundaries"}]}, "topic_inputs": {"responsibility": "936378781b709b8162fd5dd1b6ee8e1a901f99de03379ef038c8c4c974c2014b", "delivery": "033aecb33c848acfd83026dc8456421cdf57846c26698de31f57f49582641f53"}, "reused_topics": ["delivery"], "replayed_units": [], "generated_topics": ["responsibility"], "topic_agents": {"delivery": "cli/codex/gpt-6.1-terra", "responsibility": "cli/codex/gpt-6.1-terra"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "367d18b95f8f0d01a15ae0f4d1b70f7e13e4d0298df4215e2c449ac4905db6f9", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "d0f7ab4c48fcf52409935931eb9b93aacd48af4b19e9bb816fa496f1214fdb2f", "answer_contracts": "a39c9a8818afc47e059141d486337c0f12a7fd34319e2b6f7674fc428bc83e2b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "050c20aa2fdcceae10c6275fbb5f850f616ab5051bb67ccbcb4a204877a238d9", "explanation": "69bcaa207ef39d20f6a47ac201c3edf119f59b333e85131dea1bce85eef4006b", "design_response": "a7c199bc52bcc0e749ef01186e50bca98107473d5c82e2248712f465d02e1e69", "design_validation": "92ddb9a65c909173ff4c7cb627dff83e71c10c8258c51344ef0eb1a7a023937f"}, "validation_model": "e28b3989273637b5f773b10775e0a5530215c64f48b33b2022d41b7ab590b6f5", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "b87a84b1bc31079837dc4dc4527ce02c9dc2cbc3a26ff7e99e0872941d213995"}, "reuse_lineage": {"source_commit": "c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78", "body_sha256": "9c0f79396848975ea0641760adf813094ea1b89719b4571e34850b2d8b4807ac", "topics": ["delivery"], "validation": "current source, contract and editorial checks; human review pending"}, "body_sha256": "d7fb90431a6e152f00ab82d3ffcd1c1ab3c6ff60ddfcb967c5cb0623571e7594"}
generated_visuals: {"schema": 1, "records": {"ordered-completion-loop": {"input_fingerprint": "16ba5c5b35c55efe0eb09c08853bf9b46621768a048ef108e99e0550162969aa", "draft": {"nodes": [{"id": "entry", "symbol": "completeRequest", "label": "PipelineHandler의 completeRequest가 입력 request의 complete를 호출합니다.", "label_en": "PipelineHandler calls complete for the input request.", "shape": "process", "quote_ids": ["complete:0"]}, {"id": "input_assert", "symbol": "ASSERT", "label": "입력 request가 Pending이고 대기 버퍼가 없는지 ASSERT로 검사합니다. 활성 검사가 실패하면 실행을 중단합니다.", "label_en": "ASSERT checks that the input request is pending and has no pending buffers. An active failure aborts execution.", "shape": "process", "quote_ids": ["request:0", "logging:0"]}, {"id": "input_status", "symbol": "request", "label": "검사가 통과하거나 컴파일되지 않았다면 cancelled_가 참일 때 RequestCancelled, 거짓일 때 RequestComplete를 저장합니다.", "label_en": "If the checks pass or are omitted, request stores RequestCancelled when cancelled_ is true, else RequestComplete.", "shape": "process", "quote_ids": ["request:0"]}, {"id": "queue", "symbol": "while", "label": "queuedRequests_가 비어 있는지 확인합니다.", "label_en": "Check whether queuedRequests_ is empty.", "shape": "decision", "quote_ids": ["complete:0"]}, {"id": "front", "symbol": "req", "label": "큐 앞의 req가 RequestPending인지 확인합니다. 이 req는 입력 request와 다를 수 있습니다.", "label_en": "Check whether the front req is RequestPending. It may differ from the input request.", "shape": "decision", "quote_ids": ["complete:0"]}, {"id": "front_assert", "symbol": "ASSERT", "label": "앞의 req에 대기 버퍼가 없는지 ASSERT로 검사합니다. 활성 검사가 실패하면 실행을 중단합니다.", "label_en": "ASSERT checks that the front req has no pending buffers. An active failure aborts execution.", "shape": "process", "quote_ids": ["complete:0", "logging:0"]}, {"id": "pop", "symbol": "pop_front", "label": "검사가 통과하거나 컴파일되지 않았다면 큐 앞의 req를 제거합니다.", "label_en": "If the check passes or is omitted, remove the front req from the queue.", "shape": "process", "quote_ids": ["complete:0"]}, {"id": "notify", "symbol": "requestComplete", "label": "Camera의 requestComplete에 제거한 req를 전달합니다.", "label_en": "Pass the removed req to Camera's requestComplete.", "shape": "process", "quote_ids": ["complete:0"]}, {"id": "resume", "symbol": "doQueueRequests", "label": "doQueueRequests가 대기 중인 요청을 파이프라인에 큐잉할 수 있게 한 뒤 completeRequest가 끝납니다.", "label_en": "doQueueRequests allows waiting requests to be queued to the pipeline, and completeRequest ends.", "shape": "process", "quote_ids": ["complete:0"]}], "edges": [{"from": "entry", "to": "input_assert", "label": "호출한 complete가 입력 request를 검사합니다.", "label_en": "The called complete checks the input request.", "condition_ref": "always", "quote_ids": ["complete:0", "request:0"]}, {"from": "input_assert", "to": "input_status", "label": "검사가 통과하거나 컴파일되지 않은 경우 상태를 저장합니다.", "label_en": "Store the status if the checks pass or are omitted.", "condition_ref": "always", "quote_ids": ["request:0"]}, {"from": "input_status", "to": "queue", "label": "complete가 정상 복귀하면 큐를 확인합니다.", "label_en": "Check the queue when complete returns normally.", "condition_ref": "always", "quote_ids": ["complete:0"]}, {"from": "queue", "to": "front", "label": "큐에 요청이 있으면 앞의 요청을 확인합니다.", "label_en": "Check the front request if the queue is nonempty.", "condition_ref": "c1:true", "quote_ids": ["complete:0"]}, {"from": "queue", "to": "resume", "label": "큐가 비어 있으면 대기 요청의 큐잉을 재개합니다.", "label_en": "Allow waiting requests to be queued if the queue is empty.", "condition_ref": "c1:false", "quote_ids": ["complete:0"]}, {"from": "front", "to": "resume", "label": "앞의 요청이 Pending이면 반복을 끝내고 대기 요청의 큐잉을 재개합니다.", "label_en": "If the front request is pending, break and allow waiting requests to be queued.", "condition_ref": "c4:true", "quote_ids": ["complete:0"]}, {"from": "front", "to": "front_assert", "label": "앞의 요청이 Pending이 아니면 대기 버퍼를 검사합니다.", "label_en": "If the front request is not pending, check its pending buffers.", "condition_ref": "c4:false", "quote_ids": ["complete:0"]}, {"from": "front_assert", "to": "pop", "label": "검사가 통과하거나 컴파일되지 않은 경우 제거합니다.", "label_en": "Remove the request if the check passes or is omitted.", "condition_ref": "always", "quote_ids": ["complete:0"]}, {"from": "pop", "to": "notify", "label": "제거한 요청을 전달합니다.", "label_en": "Pass the removed request.", "condition_ref": "always", "quote_ids": ["complete:0"]}, {"from": "notify", "to": "queue", "label": "requestComplete가 정상 복귀할 때만 큐를 다시 확인합니다.", "label_en": "Check the queue again only if requestComplete returns normally.", "condition_ref": "always", "quote_ids": ["complete:0"]}]}, "graph": {"id": "ordered-completion-loop", "topic": "delivery", "kind": "flow", "title": "요청 상태 갱신과 제출 순서 반환", "question": "completeRequest는 상태를 갱신한 뒤 큐 앞의 어떤 조건을 검사하고 언제 대기 큐 전달을 재개합니까?", "condition_display": "evidence", "nodes": [{"id": "entry", "label": "PipelineHandler의 completeRequest가 입력 request의 complete를 호출합니다.", "label_en": "PipelineHandler calls complete for the input request.", "shape": "box", "evidence": [{"source": "delivery/complete", "sha256": "06aba06c3d636ad21e1409ac329ab9c3853776a2eef8ca443acbb49c8893e90b", "quote": "void PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}"}]}, {"id": "input_assert", "label": "입력 request가 Pending이고 대기 버퍼가 없는지 ASSERT로 검사합니다. 활성 검사가 실패하면 실행을 중단합니다.", "label_en": "ASSERT checks that the input request is pending and has no pending buffers. An active failure aborts execution.", "shape": "box", "evidence": [{"source": "delivery/request", "sha256": "045f2e5cc0e38ea289081014b5a245bbff80c5d3ecc255ed620a1e5d486ba8ec", "quote": "void Request::Private::complete()\n{\n\tRequest *request = _o<Request>();\n\n\tASSERT(request->status() == RequestPending);\n\tASSERT(!hasPendingBuffers());\n\n\trequest->status_ = cancelled_ ? RequestCancelled : RequestComplete;\n\n\tLOG(Request, Debug) << request->toString();\n\n\tLIBCAMERA_TRACEPOINT(request_complete, this);\n}"}, {"source": "delivery/logging", "sha256": "52e64d292f59786541e66fe48f5bae65256bdced60c803aa76bf3637083b47b0", "quote": "\\def LOG(category, severity)\n * \\hideinitializer\n * \\brief Log a message\n * \\param[in] category Category (optional)\n * \\param[in] severity Severity\n *\n * Return an std::ostream reference to which a message can be logged using the\n * iostream API. The \\a category, if specified, sets the message category. When\n * absent the default category is used. The  \\a severity controls whether the\n * message is printed or discarded, depending on the log level for the category.\n *\n * If the severity is set to Fatal, execution is aborted and the program\n * terminates immediately after printing the message.\n *\n * \\warning Logging from the destructor of a global object, either directly or\n * indirectly, results in undefined behaviour.\n *\n * \\todo Allow logging from destructors of global objects to the largest\n * possible extent\n */\n\n/**\n * \\def ASSERT(condition)\n * \\hideinitializer\n * \\brief Abort program execution if assertion fails\n *\n * If \\a condition is false, ASSERT() logs an error message with the Fatal log\n * level and aborts program execution.\n *\n * If the macro NDEBUG is defined before including log.h, ASSERT() generates no\n * code.\n *\n * Using conditions that have side effects with ASSERT() is not recommended, as\n * these effects would depend on whether NDEBUG is defined or not. Similarly,\n * ASSERT() should not be used to check for errors that can occur under normal\n * conditions as those checks would then be removed when compiling with NDEBUG.\n */\n\n} /* namespace libcamera */"}]}, {"id": "input_status", "label": "검사가 통과하거나 컴파일되지 않았다면 cancelled_가 참일 때 RequestCancelled, 거짓일 때 RequestComplete를 저장합니다.", "label_en": "If the checks pass or are omitted, request stores RequestCancelled when cancelled_ is true, else RequestComplete.", "shape": "box", "evidence": [{"source": "delivery/request", "sha256": "045f2e5cc0e38ea289081014b5a245bbff80c5d3ecc255ed620a1e5d486ba8ec", "quote": "void Request::Private::complete()\n{\n\tRequest *request = _o<Request>();\n\n\tASSERT(request->status() == RequestPending);\n\tASSERT(!hasPendingBuffers());\n\n\trequest->status_ = cancelled_ ? RequestCancelled : RequestComplete;\n\n\tLOG(Request, Debug) << request->toString();\n\n\tLIBCAMERA_TRACEPOINT(request_complete, this);\n}"}]}, {"id": "queue", "label": "queuedRequests_가 비어 있는지 확인합니다.", "label_en": "Check whether queuedRequests_ is empty.", "shape": "decision", "evidence": [{"source": "delivery/complete", "sha256": "06aba06c3d636ad21e1409ac329ab9c3853776a2eef8ca443acbb49c8893e90b", "quote": "void PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}"}]}, {"id": "front", "label": "큐 앞의 req가 RequestPending인지 확인합니다. 이 req는 입력 request와 다를 수 있습니다.", "label_en": "Check whether the front req is RequestPending. It may differ from the input request.", "shape": "decision", "evidence": [{"source": "delivery/complete", "sha256": "06aba06c3d636ad21e1409ac329ab9c3853776a2eef8ca443acbb49c8893e90b", "quote": "void PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}"}]}, {"id": "front_assert", "label": "앞의 req에 대기 버퍼가 없는지 ASSERT로 검사합니다. 활성 검사가 실패하면 실행을 중단합니다.", "label_en": "ASSERT checks that the front req has no pending buffers. An active failure aborts execution.", "shape": "box", "evidence": [{"source": "delivery/complete", "sha256": "06aba06c3d636ad21e1409ac329ab9c3853776a2eef8ca443acbb49c8893e90b", "quote": "void PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}"}, {"source": "delivery/logging", "sha256": "52e64d292f59786541e66fe48f5bae65256bdced60c803aa76bf3637083b47b0", "quote": "\\def LOG(category, severity)\n * \\hideinitializer\n * \\brief Log a message\n * \\param[in] category Category (optional)\n * \\param[in] severity Severity\n *\n * Return an std::ostream reference to which a message can be logged using the\n * iostream API. The \\a category, if specified, sets the message category. When\n * absent the default category is used. The  \\a severity controls whether the\n * message is printed or discarded, depending on the log level for the category.\n *\n * If the severity is set to Fatal, execution is aborted and the program\n * terminates immediately after printing the message.\n *\n * \\warning Logging from the destructor of a global object, either directly or\n * indirectly, results in undefined behaviour.\n *\n * \\todo Allow logging from destructors of global objects to the largest\n * possible extent\n */\n\n/**\n * \\def ASSERT(condition)\n * \\hideinitializer\n * \\brief Abort program execution if assertion fails\n *\n * If \\a condition is false, ASSERT() logs an error message with the Fatal log\n * level and aborts program execution.\n *\n * If the macro NDEBUG is defined before including log.h, ASSERT() generates no\n * code.\n *\n * Using conditions that have side effects with ASSERT() is not recommended, as\n * these effects would depend on whether NDEBUG is defined or not. Similarly,\n * ASSERT() should not be used to check for errors that can occur under normal\n * conditions as those checks would then be removed when compiling with NDEBUG.\n */\n\n} /* namespace libcamera */"}]}, {"id": "pop", "label": "검사가 통과하거나 컴파일되지 않았다면 큐 앞의 req를 제거합니다.", "label_en": "If the check passes or is omitted, remove the front req from the queue.", "shape": "box", "evidence": [{"source": "delivery/complete", "sha256": "06aba06c3d636ad21e1409ac329ab9c3853776a2eef8ca443acbb49c8893e90b", "quote": "void PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}"}]}, {"id": "notify", "label": "Camera의 requestComplete에 제거한 req를 전달합니다.", "label_en": "Pass the removed req to Camera's requestComplete.", "shape": "box", "evidence": [{"source": "delivery/complete", "sha256": "06aba06c3d636ad21e1409ac329ab9c3853776a2eef8ca443acbb49c8893e90b", "quote": "void PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}"}]}, {"id": "resume", "label": "doQueueRequests가 대기 중인 요청을 파이프라인에 큐잉할 수 있게 한 뒤 completeRequest가 끝납니다.", "label_en": "doQueueRequests allows waiting requests to be queued to the pipeline, and completeRequest ends.", "shape": "box", "evidence": [{"source": "delivery/complete", "sha256": "06aba06c3d636ad21e1409ac329ab9c3853776a2eef8ca443acbb49c8893e90b", "quote": "void PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}"}]}], "edges": [{"from": "entry", "to": "input_assert", "label": "호출한 complete가 입력 request를 검사합니다.", "label_en": "The called complete checks the input request.", "evidence": [{"source": "delivery/complete", "sha256": "06aba06c3d636ad21e1409ac329ab9c3853776a2eef8ca443acbb49c8893e90b", "quote": "void PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}"}, {"source": "delivery/request", "sha256": "045f2e5cc0e38ea289081014b5a245bbff80c5d3ecc255ed620a1e5d486ba8ec", "quote": "void Request::Private::complete()\n{\n\tRequest *request = _o<Request>();\n\n\tASSERT(request->status() == RequestPending);\n\tASSERT(!hasPendingBuffers());\n\n\trequest->status_ = cancelled_ ? RequestCancelled : RequestComplete;\n\n\tLOG(Request, Debug) << request->toString();\n\n\tLIBCAMERA_TRACEPOINT(request_complete, this);\n}"}]}, {"from": "input_assert", "to": "input_status", "label": "검사가 통과하거나 컴파일되지 않은 경우 상태를 저장합니다.", "label_en": "Store the status if the checks pass or are omitted.", "evidence": [{"source": "delivery/request", "sha256": "045f2e5cc0e38ea289081014b5a245bbff80c5d3ecc255ed620a1e5d486ba8ec", "quote": "void Request::Private::complete()\n{\n\tRequest *request = _o<Request>();\n\n\tASSERT(request->status() == RequestPending);\n\tASSERT(!hasPendingBuffers());\n\n\trequest->status_ = cancelled_ ? RequestCancelled : RequestComplete;\n\n\tLOG(Request, Debug) << request->toString();\n\n\tLIBCAMERA_TRACEPOINT(request_complete, this);\n}"}]}, {"from": "input_status", "to": "queue", "label": "complete가 정상 복귀하면 큐를 확인합니다.", "label_en": "Check the queue when complete returns normally.", "evidence": [{"source": "delivery/complete", "sha256": "06aba06c3d636ad21e1409ac329ab9c3853776a2eef8ca443acbb49c8893e90b", "quote": "void PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}"}]}, {"from": "queue", "to": "front", "label": "큐에 요청이 있으면 앞의 요청을 확인합니다. · !data->queuedRequests_.empty() [true]", "label_en": "Check the front request if the queue is nonempty. · !data->queuedRequests_.empty() [true]", "evidence": [{"source": "delivery/complete", "sha256": "06aba06c3d636ad21e1409ac329ab9c3853776a2eef8ca443acbb49c8893e90b", "quote": "void PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}"}]}, {"from": "queue", "to": "resume", "label": "큐가 비어 있으면 대기 요청의 큐잉을 재개합니다. · !data->queuedRequests_.empty() [false]", "label_en": "Allow waiting requests to be queued if the queue is empty. · !data->queuedRequests_.empty() [false]", "evidence": [{"source": "delivery/complete", "sha256": "06aba06c3d636ad21e1409ac329ab9c3853776a2eef8ca443acbb49c8893e90b", "quote": "void PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}"}]}, {"from": "front", "to": "resume", "label": "앞의 요청이 Pending이면 반복을 끝내고 대기 요청의 큐잉을 재개합니다. · req->status() == Request::RequestPending [true]", "label_en": "If the front request is pending, break and allow waiting requests to be queued. · req->status() == Request::RequestPending [true]", "evidence": [{"source": "delivery/complete", "sha256": "06aba06c3d636ad21e1409ac329ab9c3853776a2eef8ca443acbb49c8893e90b", "quote": "void PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}"}]}, {"from": "front", "to": "front_assert", "label": "앞의 요청이 Pending이 아니면 대기 버퍼를 검사합니다. · req->status() == Request::RequestPending [false]", "label_en": "If the front request is not pending, check its pending buffers. · req->status() == Request::RequestPending [false]", "evidence": [{"source": "delivery/complete", "sha256": "06aba06c3d636ad21e1409ac329ab9c3853776a2eef8ca443acbb49c8893e90b", "quote": "void PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}"}]}, {"from": "front_assert", "to": "pop", "label": "검사가 통과하거나 컴파일되지 않은 경우 제거합니다.", "label_en": "Remove the request if the check passes or is omitted.", "evidence": [{"source": "delivery/complete", "sha256": "06aba06c3d636ad21e1409ac329ab9c3853776a2eef8ca443acbb49c8893e90b", "quote": "void PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}"}]}, {"from": "pop", "to": "notify", "label": "제거한 요청을 전달합니다.", "label_en": "Pass the removed request.", "evidence": [{"source": "delivery/complete", "sha256": "06aba06c3d636ad21e1409ac329ab9c3853776a2eef8ca443acbb49c8893e90b", "quote": "void PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}"}]}, {"from": "notify", "to": "queue", "label": "requestComplete가 정상 복귀할 때만 큐를 다시 확인합니다.", "label_en": "Check the queue again only if requestComplete returns normally.", "evidence": [{"source": "delivery/complete", "sha256": "06aba06c3d636ad21e1409ac329ab9c3853776a2eef8ca443acbb49c8893e90b", "quote": "void PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();\n\n\trequest->_d()->complete();\n\n\tCamera::Private *data = camera->_d();\n\n\twhile (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;\n\n\t\tASSERT(!req->hasPendingBuffers());\n\t\tdata->queuedRequests_.pop_front();\n\t\tcamera->requestComplete(req);\n\t}\n\n\t/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}"}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78", "citation_binding_policy": "identifier-and-guard-boundaries-v2", "reused": true}, "camera-completion-notification-guard": {"input_fingerprint": "f3e0815106aad0f7b0e2dd1d71b712742208479ae48831946a4f909a462676b0", "draft": {"nodes": [{"id": "check", "symbol": "isAccessAllowed", "label": "접근 검사가 상태를 거절했습니까? CameraStopping부터 CameraRunning까지 양끝을 포함해 검사하며 연결 해제를 허용합니다.", "label_en": "Does the access check reject the state? It checks CameraStopping through CameraRunning and allows disconnection.", "shape": "decision", "quote_ids": ["notification:0", "state:0"]}, {"id": "fatal", "symbol": "Fatal", "label": "범위 밖이면 검사가 -EACCES를 반환합니다. Fatal은 메시지를 출력한 뒤 프로그램을 즉시 중단합니다.", "label_en": "Outside the range, the check returns -EACCES. Fatal terminates the program immediately after printing the message.", "shape": "process", "quote_ids": ["notification:0", "state:0", "logging:0"]}, {"id": "emit", "symbol": "requestCompleted", "label": "범위 안이면 검사가 0을 반환합니다. requestCompleted.emit(request)를 호출한 뒤 함수가 끝납니다.", "label_en": "Inside the range, the check returns 0. The function ends after calling requestCompleted.emit(request).", "shape": "process", "quote_ids": ["notification:0", "state:0"]}], "edges": [{"from": "check", "to": "fatal", "label": "예. 검사가 0이 아닌 값을 반환합니다.", "label_en": "Yes. The check returns a nonzero value.", "condition_ref": "c1:true", "quote_ids": ["notification:0", "state:0", "logging:0"]}, {"from": "check", "to": "emit", "label": "아니요. 검사가 0을 반환합니다.", "label_en": "No. The check returns 0.", "condition_ref": "c1:false", "quote_ids": ["notification:0", "state:0"]}]}, "graph": {"id": "camera-completion-notification-guard", "topic": "delivery", "kind": "flow", "title": "카메라 상태에 따른 완료 알림과 Fatal", "question": "Camera::requestComplete는 상태 검사 결과에 따라 언제 Fatal로 중단하고 언제 requestCompleted를 내보냅니까?", "condition_display": "evidence", "nodes": [{"id": "check", "label": "접근 검사가 상태를 거절했습니까? CameraStopping부터 CameraRunning까지 양끝을 포함해 검사하며 연결 해제를 허용합니다.", "label_en": "Does the access check reject the state? It checks CameraStopping through CameraRunning and allows disconnection.", "shape": "decision", "evidence": [{"source": "delivery/notification", "sha256": "9e8e2a873ef95a0b778292f2da2da90ec0b5ef5b312ffe88b7298d3aed624c47", "quote": "\\brief Handle request completion and notify application\n * \\param[in] request The request that has completed\n *\n * This function is called by the pipeline handler to notify the camera that\n * the request has completed. It emits the requestCompleted signal.\n */\nvoid Camera::requestComplete(Request *request)\n{\n\t/* Disconnected cameras are still able to complete requests. */\n\tif (_d()->isAccessAllowed(Private::CameraStopping, Private::CameraRunning,\n\t\t\t\t  true))\n\t\tLOG(Camera, Fatal) << \"Trying to complete a request when stopped\";\n\n\trequestCompleted.emit(request);\n}"}, {"source": "delivery/state", "sha256": "d04dbcf64bf95e8e89669e5c85602d590cd8d6530e44cd275cee39348d644b8f", "quote": "int Camera::Private::isAccessAllowed(State low, State high,\n\t\t\t\t     bool allowDisconnected,\n\t\t\t\t     const char *from) const\n{\n\tif (!allowDisconnected && disconnected_)\n\t\treturn -ENODEV;\n\n\tState currentState = state_.load(std::memory_order_acquire);\n\tif (currentState >= low && currentState <= high)\n\t\treturn 0;\n\n\tASSERT(static_cast<unsigned int>(low) < std::size(camera_state_names) &&\n\t       static_cast<unsigned int>(high) < std::size(camera_state_names));\n\n\tLOG(Camera, Error) << \"Camera in \" << camera_state_names[currentState]\n\t\t\t   << \" state trying \" << from\n\t\t\t   << \"() requiring state between \"\n\t\t\t   << camera_state_names[low] << \" and \"\n\t\t\t   << camera_state_names[high];\n\n\treturn -EACCES;\n}"}]}, {"id": "fatal", "label": "범위 밖이면 검사가 -EACCES를 반환합니다. Fatal은 메시지를 출력한 뒤 프로그램을 즉시 중단합니다.", "label_en": "Outside the range, the check returns -EACCES. Fatal terminates the program immediately after printing the message.", "shape": "box", "evidence": [{"source": "delivery/notification", "sha256": "9e8e2a873ef95a0b778292f2da2da90ec0b5ef5b312ffe88b7298d3aed624c47", "quote": "\\brief Handle request completion and notify application\n * \\param[in] request The request that has completed\n *\n * This function is called by the pipeline handler to notify the camera that\n * the request has completed. It emits the requestCompleted signal.\n */\nvoid Camera::requestComplete(Request *request)\n{\n\t/* Disconnected cameras are still able to complete requests. */\n\tif (_d()->isAccessAllowed(Private::CameraStopping, Private::CameraRunning,\n\t\t\t\t  true))\n\t\tLOG(Camera, Fatal) << \"Trying to complete a request when stopped\";\n\n\trequestCompleted.emit(request);\n}"}, {"source": "delivery/state", "sha256": "d04dbcf64bf95e8e89669e5c85602d590cd8d6530e44cd275cee39348d644b8f", "quote": "int Camera::Private::isAccessAllowed(State low, State high,\n\t\t\t\t     bool allowDisconnected,\n\t\t\t\t     const char *from) const\n{\n\tif (!allowDisconnected && disconnected_)\n\t\treturn -ENODEV;\n\n\tState currentState = state_.load(std::memory_order_acquire);\n\tif (currentState >= low && currentState <= high)\n\t\treturn 0;\n\n\tASSERT(static_cast<unsigned int>(low) < std::size(camera_state_names) &&\n\t       static_cast<unsigned int>(high) < std::size(camera_state_names));\n\n\tLOG(Camera, Error) << \"Camera in \" << camera_state_names[currentState]\n\t\t\t   << \" state trying \" << from\n\t\t\t   << \"() requiring state between \"\n\t\t\t   << camera_state_names[low] << \" and \"\n\t\t\t   << camera_state_names[high];\n\n\treturn -EACCES;\n}"}, {"source": "delivery/logging", "sha256": "52e64d292f59786541e66fe48f5bae65256bdced60c803aa76bf3637083b47b0", "quote": "\\def LOG(category, severity)\n * \\hideinitializer\n * \\brief Log a message\n * \\param[in] category Category (optional)\n * \\param[in] severity Severity\n *\n * Return an std::ostream reference to which a message can be logged using the\n * iostream API. The \\a category, if specified, sets the message category. When\n * absent the default category is used. The  \\a severity controls whether the\n * message is printed or discarded, depending on the log level for the category.\n *\n * If the severity is set to Fatal, execution is aborted and the program\n * terminates immediately after printing the message.\n *\n * \\warning Logging from the destructor of a global object, either directly or\n * indirectly, results in undefined behaviour.\n *\n * \\todo Allow logging from destructors of global objects to the largest\n * possible extent\n */\n\n/**\n * \\def ASSERT(condition)\n * \\hideinitializer\n * \\brief Abort program execution if assertion fails\n *\n * If \\a condition is false, ASSERT() logs an error message with the Fatal log\n * level and aborts program execution.\n *\n * If the macro NDEBUG is defined before including log.h, ASSERT() generates no\n * code.\n *\n * Using conditions that have side effects with ASSERT() is not recommended, as\n * these effects would depend on whether NDEBUG is defined or not. Similarly,\n * ASSERT() should not be used to check for errors that can occur under normal\n * conditions as those checks would then be removed when compiling with NDEBUG.\n */\n\n} /* namespace libcamera */"}]}, {"id": "emit", "label": "범위 안이면 검사가 0을 반환합니다. requestCompleted.emit(request)를 호출한 뒤 함수가 끝납니다.", "label_en": "Inside the range, the check returns 0. The function ends after calling requestCompleted.emit(request).", "shape": "box", "evidence": [{"source": "delivery/notification", "sha256": "9e8e2a873ef95a0b778292f2da2da90ec0b5ef5b312ffe88b7298d3aed624c47", "quote": "\\brief Handle request completion and notify application\n * \\param[in] request The request that has completed\n *\n * This function is called by the pipeline handler to notify the camera that\n * the request has completed. It emits the requestCompleted signal.\n */\nvoid Camera::requestComplete(Request *request)\n{\n\t/* Disconnected cameras are still able to complete requests. */\n\tif (_d()->isAccessAllowed(Private::CameraStopping, Private::CameraRunning,\n\t\t\t\t  true))\n\t\tLOG(Camera, Fatal) << \"Trying to complete a request when stopped\";\n\n\trequestCompleted.emit(request);\n}"}, {"source": "delivery/state", "sha256": "d04dbcf64bf95e8e89669e5c85602d590cd8d6530e44cd275cee39348d644b8f", "quote": "int Camera::Private::isAccessAllowed(State low, State high,\n\t\t\t\t     bool allowDisconnected,\n\t\t\t\t     const char *from) const\n{\n\tif (!allowDisconnected && disconnected_)\n\t\treturn -ENODEV;\n\n\tState currentState = state_.load(std::memory_order_acquire);\n\tif (currentState >= low && currentState <= high)\n\t\treturn 0;\n\n\tASSERT(static_cast<unsigned int>(low) < std::size(camera_state_names) &&\n\t       static_cast<unsigned int>(high) < std::size(camera_state_names));\n\n\tLOG(Camera, Error) << \"Camera in \" << camera_state_names[currentState]\n\t\t\t   << \" state trying \" << from\n\t\t\t   << \"() requiring state between \"\n\t\t\t   << camera_state_names[low] << \" and \"\n\t\t\t   << camera_state_names[high];\n\n\treturn -EACCES;\n}"}]}], "edges": [{"from": "check", "to": "fatal", "label": "예. 검사가 0이 아닌 값을 반환합니다. · _d()->isAccessAllowed(Private::CameraStopping, Private::CameraRunning, true) [true]", "label_en": "Yes. The check returns a nonzero value. · _d()->isAccessAllowed(Private::CameraStopping, Private::CameraRunning, true) [true]", "evidence": [{"source": "delivery/notification", "sha256": "9e8e2a873ef95a0b778292f2da2da90ec0b5ef5b312ffe88b7298d3aed624c47", "quote": "\\brief Handle request completion and notify application\n * \\param[in] request The request that has completed\n *\n * This function is called by the pipeline handler to notify the camera that\n * the request has completed. It emits the requestCompleted signal.\n */\nvoid Camera::requestComplete(Request *request)\n{\n\t/* Disconnected cameras are still able to complete requests. */\n\tif (_d()->isAccessAllowed(Private::CameraStopping, Private::CameraRunning,\n\t\t\t\t  true))\n\t\tLOG(Camera, Fatal) << \"Trying to complete a request when stopped\";\n\n\trequestCompleted.emit(request);\n}"}, {"source": "delivery/state", "sha256": "d04dbcf64bf95e8e89669e5c85602d590cd8d6530e44cd275cee39348d644b8f", "quote": "int Camera::Private::isAccessAllowed(State low, State high,\n\t\t\t\t     bool allowDisconnected,\n\t\t\t\t     const char *from) const\n{\n\tif (!allowDisconnected && disconnected_)\n\t\treturn -ENODEV;\n\n\tState currentState = state_.load(std::memory_order_acquire);\n\tif (currentState >= low && currentState <= high)\n\t\treturn 0;\n\n\tASSERT(static_cast<unsigned int>(low) < std::size(camera_state_names) &&\n\t       static_cast<unsigned int>(high) < std::size(camera_state_names));\n\n\tLOG(Camera, Error) << \"Camera in \" << camera_state_names[currentState]\n\t\t\t   << \" state trying \" << from\n\t\t\t   << \"() requiring state between \"\n\t\t\t   << camera_state_names[low] << \" and \"\n\t\t\t   << camera_state_names[high];\n\n\treturn -EACCES;\n}"}, {"source": "delivery/logging", "sha256": "52e64d292f59786541e66fe48f5bae65256bdced60c803aa76bf3637083b47b0", "quote": "\\def LOG(category, severity)\n * \\hideinitializer\n * \\brief Log a message\n * \\param[in] category Category (optional)\n * \\param[in] severity Severity\n *\n * Return an std::ostream reference to which a message can be logged using the\n * iostream API. The \\a category, if specified, sets the message category. When\n * absent the default category is used. The  \\a severity controls whether the\n * message is printed or discarded, depending on the log level for the category.\n *\n * If the severity is set to Fatal, execution is aborted and the program\n * terminates immediately after printing the message.\n *\n * \\warning Logging from the destructor of a global object, either directly or\n * indirectly, results in undefined behaviour.\n *\n * \\todo Allow logging from destructors of global objects to the largest\n * possible extent\n */\n\n/**\n * \\def ASSERT(condition)\n * \\hideinitializer\n * \\brief Abort program execution if assertion fails\n *\n * If \\a condition is false, ASSERT() logs an error message with the Fatal log\n * level and aborts program execution.\n *\n * If the macro NDEBUG is defined before including log.h, ASSERT() generates no\n * code.\n *\n * Using conditions that have side effects with ASSERT() is not recommended, as\n * these effects would depend on whether NDEBUG is defined or not. Similarly,\n * ASSERT() should not be used to check for errors that can occur under normal\n * conditions as those checks would then be removed when compiling with NDEBUG.\n */\n\n} /* namespace libcamera */"}]}, {"from": "check", "to": "emit", "label": "아니요. 검사가 0을 반환합니다. · _d()->isAccessAllowed(Private::CameraStopping, Private::CameraRunning, true) [false]", "label_en": "No. The check returns 0. · _d()->isAccessAllowed(Private::CameraStopping, Private::CameraRunning, true) [false]", "evidence": [{"source": "delivery/notification", "sha256": "9e8e2a873ef95a0b778292f2da2da90ec0b5ef5b312ffe88b7298d3aed624c47", "quote": "\\brief Handle request completion and notify application\n * \\param[in] request The request that has completed\n *\n * This function is called by the pipeline handler to notify the camera that\n * the request has completed. It emits the requestCompleted signal.\n */\nvoid Camera::requestComplete(Request *request)\n{\n\t/* Disconnected cameras are still able to complete requests. */\n\tif (_d()->isAccessAllowed(Private::CameraStopping, Private::CameraRunning,\n\t\t\t\t  true))\n\t\tLOG(Camera, Fatal) << \"Trying to complete a request when stopped\";\n\n\trequestCompleted.emit(request);\n}"}, {"source": "delivery/state", "sha256": "d04dbcf64bf95e8e89669e5c85602d590cd8d6530e44cd275cee39348d644b8f", "quote": "int Camera::Private::isAccessAllowed(State low, State high,\n\t\t\t\t     bool allowDisconnected,\n\t\t\t\t     const char *from) const\n{\n\tif (!allowDisconnected && disconnected_)\n\t\treturn -ENODEV;\n\n\tState currentState = state_.load(std::memory_order_acquire);\n\tif (currentState >= low && currentState <= high)\n\t\treturn 0;\n\n\tASSERT(static_cast<unsigned int>(low) < std::size(camera_state_names) &&\n\t       static_cast<unsigned int>(high) < std::size(camera_state_names));\n\n\tLOG(Camera, Error) << \"Camera in \" << camera_state_names[currentState]\n\t\t\t   << \" state trying \" << from\n\t\t\t   << \"() requiring state between \"\n\t\t\t   << camera_state_names[low] << \" and \"\n\t\t\t   << camera_state_names[high];\n\n\treturn -EACCES;\n}"}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78", "citation_binding_policy": "identifier-and-guard-boundaries-v2", "reused": true}, "normal-buffer-request-duties": {"input_fingerprint": "9dad54346f945499c7277e44abb81eb12a5cbf4108b27649e004dd07f4c16849", "draft": {"nodes": [{"id": "handler", "symbol": "PipelineHandler", "label": "PipelineHandler는 버퍼 완료와 요청 완료를 알릴 책임이 있습니다.", "label_en": "PipelineHandler is responsible for signaling buffer and request completion.", "shape": "box", "quote_ids": ["buffer:0"]}, {"id": "complete_buffer", "symbol": "PipelineHandler::completeBuffer", "label": "completeBuffer는 CameraManager 스레드에서 호출해야 하며, 앱에 버퍼 완료를 알린 뒤 요청의 내부 버퍼 추적을 갱신합니다.", "label_en": "Call completeBuffer on the CameraManager thread; it notifies the app and updates buffer tracking.", "shape": "process", "quote_ids": ["buffer:0"]}, {"id": "buffer_result", "symbol": "bool", "label": "completeBuffer는 요청의 모든 버퍼가 완료되면 true를, 그렇지 않으면 false를 반환합니다.", "label_en": "completeBuffer returns true if all buffers in the request are complete, and false otherwise.", "shape": "box", "quote_ids": ["buffer:0"]}, {"id": "complete_request", "symbol": "completeRequest", "label": "마지막 버퍼도 요청을 자동 완료하지 않습니다. 필요한 추가 작업 기회가 주어진 뒤 handler가 completeRequest를 명시 호출해야 합니다.", "label_en": "The last buffer does not complete the request; the handler must explicitly call completeRequest after any needed work.", "shape": "process", "quote_ids": ["buffer:0"]}, {"id": "request", "symbol": "request", "label": "완료된 request를 알리는 함수는 CameraManager 스레드에서 호출해야 하며, 반환 후 handler가 해당 request에 접근하면 안 됩니다.", "label_en": "Call the completion function on the CameraManager thread; the handler must not access the request after it returns.", "shape": "box", "quote_ids": ["complete:0"]}, {"id": "application", "symbol": "application", "label": "요청은 application에 제출 순서로 반환됩니다. handler는 완료된 요청을 순서 제약 없이 알릴 수 있습니다.", "label_en": "Requests return to the application in submission order; the handler may report completed requests in any order.", "shape": "box", "quote_ids": ["complete:0"]}, {"id": "private_complete", "symbol": "Request::Private::complete", "label": "Request::Private::complete는 요청 상태가 RequestPending이고 대기 중인 버퍼가 없는지 ASSERT로 검사합니다.", "label_en": "Request::Private::complete asserts that the request is RequestPending and has no pending buffers.", "shape": "process", "quote_ids": ["request-complete-asserts:0"]}, {"id": "assert", "symbol": "ASSERT", "label": "ASSERT 조건이 거짓이면 Fatal 오류를 기록하고 실행을 중단합니다. NDEBUG로 코드가 제외되거나 검사를 통과하면 중단하지 않습니다.", "label_en": "ASSERT logs a Fatal error and aborts if false; passing or compiling it out with NDEBUG does not abort.", "shape": "box", "quote_ids": ["assert-contract:0"]}], "edges": [{"from": "handler", "to": "complete_buffer", "label": "handler는 버퍼 완료 알림에 completeBuffer를 호출해야 합니다.", "label_en": "The handler must call completeBuffer to signal buffer completion.", "condition_ref": "always", "quote_ids": ["buffer:0"]}, {"from": "handler", "to": "complete_request", "label": "handler는 요청 완료에 completeRequest를 명시 호출해야 합니다.", "label_en": "The handler must explicitly call completeRequest to complete the request.", "condition_ref": "always", "quote_ids": ["buffer:0"]}, {"from": "complete_buffer", "to": "buffer_result", "label": "completeBuffer의 반환값은 모든 버퍼의 완료 여부를 나타냅니다.", "label_en": "The completeBuffer return value reports whether all buffers are complete.", "condition_ref": "always", "quote_ids": ["buffer:0"]}, {"from": "complete_buffer", "to": "request", "label": "request는 완료된 버퍼가 속한 요청입니다.", "label_en": "The request contains the completed buffer.", "condition_ref": "always", "quote_ids": ["buffer:0"]}, {"from": "complete_request", "to": "request", "label": "completeRequest는 버퍼 완료만으로 자동 완료되지 않은 request를 명시 완료합니다.", "label_en": "completeRequest explicitly completes a request that buffer completion alone does not complete.", "condition_ref": "always", "quote_ids": ["buffer:0"]}, {"from": "request", "to": "application", "label": "완료된 요청은 application에 제출 순서로 반환됩니다.", "label_en": "Completed requests return to the application in submission order.", "condition_ref": "always", "quote_ids": ["complete:0"]}, {"from": "request", "to": "private_complete", "label": "Request::Private::complete는 request의 상태와 대기 버퍼를 검사합니다.", "label_en": "Request::Private::complete checks the request status and pending buffers.", "condition_ref": "always", "quote_ids": ["request-complete-asserts:0"]}, {"from": "private_complete", "to": "assert", "label": "이 완료 함수는 두 전제에 ASSERT를 사용합니다.", "label_en": "This completion function uses ASSERT for both preconditions.", "condition_ref": "always", "quote_ids": ["request-complete-asserts:0"]}]}, "graph": {"id": "normal-buffer-request-duties", "topic": "responsibility", "kind": "ownership", "title": "정상 버퍼 완료와 명시 요청 완료의 책임", "question": "정상 버퍼 완료 경로에서 어떤 API를 어느 스레드에서 호출하며 요청 완료 전제와 반환 후 의무는 무엇입니까?", "condition_display": "evidence", "nodes": [{"id": "handler", "label": "PipelineHandler는 버퍼 완료와 요청 완료를 알릴 책임이 있습니다.", "label_en": "PipelineHandler is responsible for signaling buffer and request completion.", "shape": "box", "evidence": [{"source": "responsibility/buffer", "sha256": "2ac611d3ff5edaf4e1f140f09f9bbe2f9304b41b9e198beb46a5660e5f195282", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}"}]}, {"id": "complete_buffer", "label": "completeBuffer는 CameraManager 스레드에서 호출해야 하며, 앱에 버퍼 완료를 알린 뒤 요청의 내부 버퍼 추적을 갱신합니다.", "label_en": "Call completeBuffer on the CameraManager thread; it notifies the app and updates buffer tracking.", "shape": "box", "evidence": [{"source": "responsibility/buffer", "sha256": "2ac611d3ff5edaf4e1f140f09f9bbe2f9304b41b9e198beb46a5660e5f195282", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}"}]}, {"id": "buffer_result", "label": "completeBuffer는 요청의 모든 버퍼가 완료되면 true를, 그렇지 않으면 false를 반환합니다.", "label_en": "completeBuffer returns true if all buffers in the request are complete, and false otherwise.", "shape": "box", "evidence": [{"source": "responsibility/buffer", "sha256": "2ac611d3ff5edaf4e1f140f09f9bbe2f9304b41b9e198beb46a5660e5f195282", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}"}]}, {"id": "complete_request", "label": "마지막 버퍼도 요청을 자동 완료하지 않습니다. 필요한 추가 작업 기회가 주어진 뒤 handler가 completeRequest를 명시 호출해야 합니다.", "label_en": "The last buffer does not complete the request; the handler must explicitly call completeRequest after any needed work.", "shape": "box", "evidence": [{"source": "responsibility/buffer", "sha256": "2ac611d3ff5edaf4e1f140f09f9bbe2f9304b41b9e198beb46a5660e5f195282", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}"}]}, {"id": "request", "label": "완료된 request를 알리는 함수는 CameraManager 스레드에서 호출해야 하며, 반환 후 handler가 해당 request에 접근하면 안 됩니다.", "label_en": "Call the completion function on the CameraManager thread; the handler must not access the request after it returns.", "shape": "box", "evidence": [{"source": "responsibility/complete", "sha256": "9a0ed4d736b974c075804a539949762c99c31dc1c6ad62f7185af6f1b9c6e741", "quote": "\\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */"}]}, {"id": "application", "label": "요청은 application에 제출 순서로 반환됩니다. handler는 완료된 요청을 순서 제약 없이 알릴 수 있습니다.", "label_en": "Requests return to the application in submission order; the handler may report completed requests in any order.", "shape": "box", "evidence": [{"source": "responsibility/complete", "sha256": "9a0ed4d736b974c075804a539949762c99c31dc1c6ad62f7185af6f1b9c6e741", "quote": "\\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */"}]}, {"id": "private_complete", "label": "Request::Private::complete는 요청 상태가 RequestPending이고 대기 중인 버퍼가 없는지 ASSERT로 검사합니다.", "label_en": "Request::Private::complete asserts that the request is RequestPending and has no pending buffers.", "shape": "box", "evidence": [{"source": "responsibility/request-complete-asserts", "sha256": "045f2e5cc0e38ea289081014b5a245bbff80c5d3ecc255ed620a1e5d486ba8ec", "quote": "void Request::Private::complete()\n{\n\tRequest *request = _o<Request>();\n\n\tASSERT(request->status() == RequestPending);\n\tASSERT(!hasPendingBuffers());\n\n\trequest->status_ = cancelled_ ? RequestCancelled : RequestComplete;\n\n\tLOG(Request, Debug) << request->toString();\n\n\tLIBCAMERA_TRACEPOINT(request_complete, this);\n}"}]}, {"id": "assert", "label": "ASSERT 조건이 거짓이면 Fatal 오류를 기록하고 실행을 중단합니다. NDEBUG로 코드가 제외되거나 검사를 통과하면 중단하지 않습니다.", "label_en": "ASSERT logs a Fatal error and aborts if false; passing or compiling it out with NDEBUG does not abort.", "shape": "box", "evidence": [{"source": "responsibility/assert-contract", "sha256": "522875c26e54ef1cc9cce7c4797356dda57027e4fb9bd25ceb4b352ccc7bcefe", "quote": "\\def ASSERT(condition)\n * \\hideinitializer\n * \\brief Abort program execution if assertion fails\n *\n * If \\a condition is false, ASSERT() logs an error message with the Fatal log\n * level and aborts program execution.\n *\n * If the macro NDEBUG is defined before including log.h, ASSERT() generates no\n * code.\n *\n * Using conditions that have side effects with ASSERT() is not recommended, as\n * these effects would depend on whether NDEBUG is defined or not. Similarly,\n * ASSERT() should not be used to check for errors that can occur under normal\n * conditions as those checks would then be removed when compiling with NDEBUG.\n */"}]}], "edges": [{"from": "handler", "to": "complete_buffer", "label": "handler는 버퍼 완료 알림에 completeBuffer를 호출해야 합니다.", "label_en": "The handler must call completeBuffer to signal buffer completion.", "evidence": [{"source": "responsibility/buffer", "sha256": "2ac611d3ff5edaf4e1f140f09f9bbe2f9304b41b9e198beb46a5660e5f195282", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}"}]}, {"from": "handler", "to": "complete_request", "label": "handler는 요청 완료에 completeRequest를 명시 호출해야 합니다.", "label_en": "The handler must explicitly call completeRequest to complete the request.", "evidence": [{"source": "responsibility/buffer", "sha256": "2ac611d3ff5edaf4e1f140f09f9bbe2f9304b41b9e198beb46a5660e5f195282", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}"}]}, {"from": "complete_buffer", "to": "buffer_result", "label": "completeBuffer의 반환값은 모든 버퍼의 완료 여부를 나타냅니다.", "label_en": "The completeBuffer return value reports whether all buffers are complete.", "evidence": [{"source": "responsibility/buffer", "sha256": "2ac611d3ff5edaf4e1f140f09f9bbe2f9304b41b9e198beb46a5660e5f195282", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}"}]}, {"from": "complete_buffer", "to": "request", "label": "request는 완료된 버퍼가 속한 요청입니다.", "label_en": "The request contains the completed buffer.", "evidence": [{"source": "responsibility/buffer", "sha256": "2ac611d3ff5edaf4e1f140f09f9bbe2f9304b41b9e198beb46a5660e5f195282", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}"}]}, {"from": "complete_request", "to": "request", "label": "completeRequest는 버퍼 완료만으로 자동 완료되지 않은 request를 명시 완료합니다.", "label_en": "completeRequest explicitly completes a request that buffer completion alone does not complete.", "evidence": [{"source": "responsibility/buffer", "sha256": "2ac611d3ff5edaf4e1f140f09f9bbe2f9304b41b9e198beb46a5660e5f195282", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}"}]}, {"from": "request", "to": "application", "label": "완료된 요청은 application에 제출 순서로 반환됩니다.", "label_en": "Completed requests return to the application in submission order.", "evidence": [{"source": "responsibility/complete", "sha256": "9a0ed4d736b974c075804a539949762c99c31dc1c6ad62f7185af6f1b9c6e741", "quote": "\\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */"}]}, {"from": "request", "to": "private_complete", "label": "Request::Private::complete는 request의 상태와 대기 버퍼를 검사합니다.", "label_en": "Request::Private::complete checks the request status and pending buffers.", "evidence": [{"source": "responsibility/request-complete-asserts", "sha256": "045f2e5cc0e38ea289081014b5a245bbff80c5d3ecc255ed620a1e5d486ba8ec", "quote": "void Request::Private::complete()\n{\n\tRequest *request = _o<Request>();\n\n\tASSERT(request->status() == RequestPending);\n\tASSERT(!hasPendingBuffers());\n\n\trequest->status_ = cancelled_ ? RequestCancelled : RequestComplete;\n\n\tLOG(Request, Debug) << request->toString();\n\n\tLIBCAMERA_TRACEPOINT(request_complete, this);\n}"}]}, {"from": "private_complete", "to": "assert", "label": "이 완료 함수는 두 전제에 ASSERT를 사용합니다.", "label_en": "This completion function uses ASSERT for both preconditions.", "evidence": [{"source": "responsibility/request-complete-asserts", "sha256": "045f2e5cc0e38ea289081014b5a245bbff80c5d3ecc255ed620a1e5d486ba8ec", "quote": "void Request::Private::complete()\n{\n\tRequest *request = _o<Request>();\n\n\tASSERT(request->status() == RequestPending);\n\tASSERT(!hasPendingBuffers());\n\n\trequest->status_ = cancelled_ ? RequestCancelled : RequestComplete;\n\n\tLOG(Request, Debug) << request->toString();\n\n\tLIBCAMERA_TRACEPOINT(request_complete, this);\n}"}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78", "citation_binding_policy": "identifier-and-guard-boundaries-v2", "reused": true}, "pipeline-cancellation-boundary": {"input_fingerprint": "b252936a36e5caa42d3c9a7398099fad1432101e070277817f25b8fd3be005e5", "draft": {"nodes": [{"id": "pipeline", "symbol": "cancelRequest", "label": "PipelineHandler.cancelRequest가 요청 취소를 시작합니다.", "label_en": "PipelineHandler.cancelRequest starts cancelling the request.", "shape": "process", "quote_ids": ["pipeline-cancel:0"]}, {"id": "cancel_entry", "symbol": "cancel", "label": "Request::Private::cancel에 진입합니다.", "label_en": "Request::Private::cancel is entered.", "shape": "process", "quote_ids": ["pipeline-cancel:0", "cancel-private:0"]}, {"id": "assert", "symbol": "ASSERT", "label": "활성 ASSERT가 실패하면 Fatal 오류를 기록하고 프로그램을 중단합니다. log.h를 포함하기 전에 NDEBUG를 정의하면 ASSERT 코드는 생성되지 않습니다.", "label_en": "If active ASSERT fails, it logs a Fatal error and aborts. If NDEBUG is defined before including log.h, ASSERT generates no code.", "shape": "process", "quote_ids": ["cancel-private:0", "assert-contract:0"]}, {"id": "helper", "symbol": "doCancelRequest", "label": "doCancelRequest는 각 pending 버퍼를 취소하고 bufferCompleted를 직접 emit한 뒤 cancelled_를 설정하고 pending_, notifiers_, timer_를 정리합니다.", "label_en": "doCancelRequest cancels each pending buffer and directly emits bufferCompleted, then sets cancelled_ and clears pending_, notifiers_ and timer_.", "shape": "process", "quote_ids": ["cancel-details:0"]}, {"id": "cancel_return", "symbol": "cancel", "label": "doCancelRequest가 정상 복귀하면 cancel이 정상 반환합니다. doCancelRequest만 호출한다고 다른 문맥에서도 요청 완료가 보장되지는 않습니다.", "label_en": "When doCancelRequest returns normally, cancel returns normally. Calling doCancelRequest alone does not guarantee request completion in other contexts.", "shape": "process", "quote_ids": ["cancel-private:0", "cancel-details:0"]}, {"id": "complete", "symbol": "completeRequest", "label": "cancelRequest가 completeRequest를 호출합니다.", "label_en": "cancelRequest calls completeRequest.", "shape": "process", "quote_ids": ["pipeline-cancel:0"]}], "edges": [{"from": "pipeline", "to": "cancel_entry", "label": "cancelRequest가 cancel을 호출합니다.", "label_en": "cancelRequest calls cancel.", "condition_ref": "always", "quote_ids": ["pipeline-cancel:0"]}, {"from": "cancel_entry", "to": "assert", "label": "cancel이 RequestPending 상태를 ASSERT로 확인합니다.", "label_en": "cancel checks the RequestPending status with ASSERT.", "condition_ref": "always", "quote_ids": ["cancel-private:0"]}, {"from": "assert", "to": "helper", "label": "ASSERT가 통과하거나 코드가 제거되어 실행이 계속되면 doCancelRequest를 호출합니다.", "label_en": "If ASSERT passes or its code is removed and execution continues, cancel calls doCancelRequest.", "condition_ref": "always", "quote_ids": ["cancel-private:0", "assert-contract:0"]}, {"from": "helper", "to": "cancel_return", "label": "doCancelRequest가 정상 복귀하면 cancel이 반환합니다.", "label_en": "When doCancelRequest returns normally, cancel returns.", "condition_ref": "always", "quote_ids": ["cancel-private:0"]}, {"from": "cancel_return", "to": "complete", "label": "cancel이 정상 반환하면 cancelRequest가 completeRequest를 호출합니다.", "label_en": "When cancel returns normally, cancelRequest calls completeRequest.", "condition_ref": "always", "quote_ids": ["pipeline-cancel:0"]}]}, "graph": {"id": "pipeline-cancellation-boundary", "topic": "responsibility", "kind": "flow", "title": "공통 취소 함수와 내부 버퍼 통지의 경계", "question": "PipelineHandler.cancelRequest는 어떤 호출 순서로 요청을 완료하며 내부 doCancelRequest만의 호출은 무엇을 보장하지 않습니까?", "condition_display": "evidence", "nodes": [{"id": "pipeline", "label": "PipelineHandler.cancelRequest가 요청 취소를 시작합니다.", "label_en": "PipelineHandler.cancelRequest starts cancelling the request.", "shape": "box", "evidence": [{"source": "responsibility/pipeline-cancel", "sha256": "a3d0d59ae735b64d64f8b6d8d5393bfa75cd803c646d9d3f7b2a8c1b14d3be36", "quote": "void PipelineHandler::cancelRequest(Request *request)\n{\n\trequest->_d()->cancel();\n\tcompleteRequest(request);\n}"}]}, {"id": "cancel_entry", "label": "Request::Private::cancel에 진입합니다.", "label_en": "Request::Private::cancel is entered.", "shape": "box", "evidence": [{"source": "responsibility/pipeline-cancel", "sha256": "a3d0d59ae735b64d64f8b6d8d5393bfa75cd803c646d9d3f7b2a8c1b14d3be36", "quote": "void PipelineHandler::cancelRequest(Request *request)\n{\n\trequest->_d()->cancel();\n\tcompleteRequest(request);\n}"}, {"source": "responsibility/cancel-private", "sha256": "e17ceaea94ddf2edb3419c9b474af9c94383a8b300edbb495cf440024e60128c", "quote": "void Request::Private::cancel()\n{\n\tLIBCAMERA_TRACEPOINT(request_cancel, this);\n\n\tRequest *request = _o<Request>();\n\tASSERT(request->status() == RequestPending);\n\n\tdoCancelRequest();\n}"}]}, {"id": "assert", "label": "활성 ASSERT가 실패하면 Fatal 오류를 기록하고 프로그램을 중단합니다. log.h를 포함하기 전에 NDEBUG를 정의하면 ASSERT 코드는 생성되지 않습니다.", "label_en": "If active ASSERT fails, it logs a Fatal error and aborts. If NDEBUG is defined before including log.h, ASSERT generates no code.", "shape": "box", "evidence": [{"source": "responsibility/cancel-private", "sha256": "e17ceaea94ddf2edb3419c9b474af9c94383a8b300edbb495cf440024e60128c", "quote": "void Request::Private::cancel()\n{\n\tLIBCAMERA_TRACEPOINT(request_cancel, this);\n\n\tRequest *request = _o<Request>();\n\tASSERT(request->status() == RequestPending);\n\n\tdoCancelRequest();\n}"}, {"source": "responsibility/assert-contract", "sha256": "522875c26e54ef1cc9cce7c4797356dda57027e4fb9bd25ceb4b352ccc7bcefe", "quote": "\\def ASSERT(condition)\n * \\hideinitializer\n * \\brief Abort program execution if assertion fails\n *\n * If \\a condition is false, ASSERT() logs an error message with the Fatal log\n * level and aborts program execution.\n *\n * If the macro NDEBUG is defined before including log.h, ASSERT() generates no\n * code.\n *\n * Using conditions that have side effects with ASSERT() is not recommended, as\n * these effects would depend on whether NDEBUG is defined or not. Similarly,\n * ASSERT() should not be used to check for errors that can occur under normal\n * conditions as those checks would then be removed when compiling with NDEBUG.\n */"}]}, {"id": "helper", "label": "doCancelRequest는 각 pending 버퍼를 취소하고 bufferCompleted를 직접 emit한 뒤 cancelled_를 설정하고 pending_, notifiers_, timer_를 정리합니다.", "label_en": "doCancelRequest cancels each pending buffer and directly emits bufferCompleted, then sets cancelled_ and clears pending_, notifiers_ and timer_.", "shape": "box", "evidence": [{"source": "responsibility/cancel-details", "sha256": "f3ccc6e43d58f4af003478867e265560de0674cd1f1c454d6178ff47529eb06c", "quote": "void Request::Private::doCancelRequest()\n{\n\tRequest *request = _o<Request>();\n\n\tfor (FrameBuffer *buffer : pending_) {\n\t\tbuffer->_d()->cancel();\n\t\tcamera_->bufferCompleted.emit(request, buffer);\n\t}\n\n\tcancelled_ = true;\n\tpending_.clear();\n\tnotifiers_.clear();\n\ttimer_.reset();\n}"}]}, {"id": "cancel_return", "label": "doCancelRequest가 정상 복귀하면 cancel이 정상 반환합니다. doCancelRequest만 호출한다고 다른 문맥에서도 요청 완료가 보장되지는 않습니다.", "label_en": "When doCancelRequest returns normally, cancel returns normally. Calling doCancelRequest alone does not guarantee request completion in other contexts.", "shape": "box", "evidence": [{"source": "responsibility/cancel-private", "sha256": "e17ceaea94ddf2edb3419c9b474af9c94383a8b300edbb495cf440024e60128c", "quote": "void Request::Private::cancel()\n{\n\tLIBCAMERA_TRACEPOINT(request_cancel, this);\n\n\tRequest *request = _o<Request>();\n\tASSERT(request->status() == RequestPending);\n\n\tdoCancelRequest();\n}"}, {"source": "responsibility/cancel-details", "sha256": "f3ccc6e43d58f4af003478867e265560de0674cd1f1c454d6178ff47529eb06c", "quote": "void Request::Private::doCancelRequest()\n{\n\tRequest *request = _o<Request>();\n\n\tfor (FrameBuffer *buffer : pending_) {\n\t\tbuffer->_d()->cancel();\n\t\tcamera_->bufferCompleted.emit(request, buffer);\n\t}\n\n\tcancelled_ = true;\n\tpending_.clear();\n\tnotifiers_.clear();\n\ttimer_.reset();\n}"}]}, {"id": "complete", "label": "cancelRequest가 completeRequest를 호출합니다.", "label_en": "cancelRequest calls completeRequest.", "shape": "box", "evidence": [{"source": "responsibility/pipeline-cancel", "sha256": "a3d0d59ae735b64d64f8b6d8d5393bfa75cd803c646d9d3f7b2a8c1b14d3be36", "quote": "void PipelineHandler::cancelRequest(Request *request)\n{\n\trequest->_d()->cancel();\n\tcompleteRequest(request);\n}"}]}], "edges": [{"from": "pipeline", "to": "cancel_entry", "label": "cancelRequest가 cancel을 호출합니다.", "label_en": "cancelRequest calls cancel.", "evidence": [{"source": "responsibility/pipeline-cancel", "sha256": "a3d0d59ae735b64d64f8b6d8d5393bfa75cd803c646d9d3f7b2a8c1b14d3be36", "quote": "void PipelineHandler::cancelRequest(Request *request)\n{\n\trequest->_d()->cancel();\n\tcompleteRequest(request);\n}"}]}, {"from": "cancel_entry", "to": "assert", "label": "cancel이 RequestPending 상태를 ASSERT로 확인합니다.", "label_en": "cancel checks the RequestPending status with ASSERT.", "evidence": [{"source": "responsibility/cancel-private", "sha256": "e17ceaea94ddf2edb3419c9b474af9c94383a8b300edbb495cf440024e60128c", "quote": "void Request::Private::cancel()\n{\n\tLIBCAMERA_TRACEPOINT(request_cancel, this);\n\n\tRequest *request = _o<Request>();\n\tASSERT(request->status() == RequestPending);\n\n\tdoCancelRequest();\n}"}]}, {"from": "assert", "to": "helper", "label": "ASSERT가 통과하거나 코드가 제거되어 실행이 계속되면 doCancelRequest를 호출합니다.", "label_en": "If ASSERT passes or its code is removed and execution continues, cancel calls doCancelRequest.", "evidence": [{"source": "responsibility/cancel-private", "sha256": "e17ceaea94ddf2edb3419c9b474af9c94383a8b300edbb495cf440024e60128c", "quote": "void Request::Private::cancel()\n{\n\tLIBCAMERA_TRACEPOINT(request_cancel, this);\n\n\tRequest *request = _o<Request>();\n\tASSERT(request->status() == RequestPending);\n\n\tdoCancelRequest();\n}"}, {"source": "responsibility/assert-contract", "sha256": "522875c26e54ef1cc9cce7c4797356dda57027e4fb9bd25ceb4b352ccc7bcefe", "quote": "\\def ASSERT(condition)\n * \\hideinitializer\n * \\brief Abort program execution if assertion fails\n *\n * If \\a condition is false, ASSERT() logs an error message with the Fatal log\n * level and aborts program execution.\n *\n * If the macro NDEBUG is defined before including log.h, ASSERT() generates no\n * code.\n *\n * Using conditions that have side effects with ASSERT() is not recommended, as\n * these effects would depend on whether NDEBUG is defined or not. Similarly,\n * ASSERT() should not be used to check for errors that can occur under normal\n * conditions as those checks would then be removed when compiling with NDEBUG.\n */"}]}, {"from": "helper", "to": "cancel_return", "label": "doCancelRequest가 정상 복귀하면 cancel이 반환합니다.", "label_en": "When doCancelRequest returns normally, cancel returns.", "evidence": [{"source": "responsibility/cancel-private", "sha256": "e17ceaea94ddf2edb3419c9b474af9c94383a8b300edbb495cf440024e60128c", "quote": "void Request::Private::cancel()\n{\n\tLIBCAMERA_TRACEPOINT(request_cancel, this);\n\n\tRequest *request = _o<Request>();\n\tASSERT(request->status() == RequestPending);\n\n\tdoCancelRequest();\n}"}]}, {"from": "cancel_return", "to": "complete", "label": "cancel이 정상 반환하면 cancelRequest가 completeRequest를 호출합니다.", "label_en": "When cancel returns normally, cancelRequest calls completeRequest.", "evidence": [{"source": "responsibility/pipeline-cancel", "sha256": "a3d0d59ae735b64d64f8b6d8d5393bfa75cd803c646d9d3f7b2a8c1b14d3be36", "quote": "void PipelineHandler::cancelRequest(Request *request)\n{\n\trequest->_d()->cancel();\n\tcompleteRequest(request);\n}"}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78", "citation_binding_policy": "identifier-and-guard-boundaries-v2", "reused": true}}, "body_sha256": "d7fb90431a6e152f00ab82d3ffcd1c1ab3c6ff60ddfcb967c5cb0623571e7594"}
---

# 요청 완료 통지

**버퍼 완료와 요청 완료를 구분하고 제출 순서대로 돌아오는 알림과 접근 종료 책임을 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| <a id="이-흐름에서-확인할-것"></a>버퍼 완료와 요청 완료를 구분하고 제출 순서대로 돌아오는 알림과 접근 종료 책임을 확인하세요. | [요청 완료를 알릴 책임과 접근 종료](#요청-완료를-알릴-책임과-접근-종료) |

## 요청 완료를 알릴 책임과 접근 종료

파이프라인 핸들러는 `CameraManager` 스레드에서 `completeBuffer`를 호출해야 하며, 이 함수는 버퍼 완료를 알린 뒤 요청의 내부 버퍼 추적을 갱신합니다. 모든 버퍼가 완료되고 필요한 추가 작업을 마친 뒤 핸들러는 같은 스레드에서 `completeRequest`를 호출해 카메라에 요청 완료를 알려야 하며, 이 함수가 반환한 뒤에는 해당 요청에 접근해서는 안 됩니다. `completeRequest`의 함수 반환 시점과 별개로 요청은 앱에 제출 순서대로 반환됩니다. 공통 `cancelRequest`는 `Request::Private::cancel`이 정상 복귀한 뒤 직접 `completeRequest`를 호출하며, `doCancelRequest`의 버퍼 완료 알림 자체가 요청 완료를 보장하지는 않습니다. `src/libcamera/pipeline_handler.cpp:547`, `src/libcamera/pipeline_handler.cpp:571`, `src/libcamera/pipeline_handler.cpp:613`, `src/libcamera/request.cpp:162`, `src/libcamera/request.cpp:139`

<!-- sdd:visual:normal-buffer-request-duties -->
### 정상 버퍼 완료와 명시 요청 완료의 책임

```mermaid
flowchart TB
%% sdd:translations {"ASSERT 조건이 거짓이면 <br/>Fatal 오류를 기록하고 <br/>실행을 중단합니다. NDEBUG로 <br/>코드가 제외되거나 검사를 <br/>통과하면 중단하지 않습니다.": "ASSERT logs a Fatal error <br/>and aborts if false; <br/>passing or compiling it out <br/>with NDEBUG does not abort.", "PipelineHandler는 버퍼 <br/>완료와 요청 완료를 알릴 <br/>책임이 있습니다.": "PipelineHandler is <br/>responsible for signaling <br/>buffer and request <br/>completion.", "Request::Private::<br/>complete는 request의 상태와 <br/>대기 버퍼를 검사합니다.": "Request::Private::complete <br/>checks the request status <br/>and pending buffers.", "Request::Private::<br/>complete는 요청 상태가 <br/>RequestPending이고 대기 <br/>중인 버퍼가 없는지 ASSERT로 <br/>검사합니다.": "Request::Private::complete <br/>asserts that the request is <br/>RequestPending and has no <br/>pending buffers.", "completeBuffer는 <br/>CameraManager 스레드에서 <br/>호출해야 하며, 앱에 버퍼 <br/>완료를 알린 뒤 요청의 내부 <br/>버퍼 추적을 갱신합니다.": "Call completeBuffer on the <br/>CameraManager thread; it <br/>notifies the app and <br/>updates buffer tracking.", "completeBuffer는 요청의 <br/>모든 버퍼가 완료되면 <br/>true를, 그렇지 않으면 <br/>false를 반환합니다.": "completeBuffer returns true <br/>if all buffers in the <br/>request are complete, and <br/>false otherwise.", "completeBuffer의 반환값은 <br/>모든 버퍼의 완료 여부를 <br/>나타냅니다.": "The completeBuffer return <br/>value reports whether all <br/>buffers are complete.", "completeRequest는 버퍼 <br/>완료만으로 자동 완료되지 <br/>않은 request를 명시 <br/>완료합니다.": "completeRequest explicitly <br/>completes a request that <br/>buffer completion alone <br/>does not complete.", "handler는 버퍼 완료 알림에 <br/>completeBuffer를 호출해야 <br/>합니다.": "The handler must call <br/>completeBuffer to signal <br/>buffer completion.", "handler는 요청 완료에 <br/>completeRequest를 명시 <br/>호출해야 합니다.": "The handler must explicitly <br/>call completeRequest to <br/>complete the request.", "request는 완료된 버퍼가 <br/>속한 요청입니다.": "The request contains the <br/>completed buffer.", "마지막 버퍼도 요청을 자동 <br/>완료하지 않습니다. 필요한 <br/>추가 작업 기회가 주어진 뒤 <br/>handler가 completeRequest를 <br/>명시 호출해야 합니다.": "The last buffer does not <br/>complete the request; the <br/>handler must explicitly <br/>call completeRequest after <br/>any needed work.", "완료된 request를 알리는 <br/>함수는 CameraManager <br/>스레드에서 호출해야 하며, <br/>반환 후 handler가 해당 <br/>request에 접근하면 안 <br/>됩니다.": "Call the completion <br/>function on the <br/>CameraManager thread; the <br/>handler must not access the <br/>request after it returns.", "완료된 요청은 application에 <br/>제출 순서로 반환됩니다.": "Completed requests return <br/>to the application in <br/>submission order.", "요청은 application에 제출 <br/>순서로 반환됩니다. <br/>handler는 완료된 요청을 <br/>순서 제약 없이 알릴 수 <br/>있습니다.": "Requests return to the <br/>application in submission <br/>order; the handler may <br/>report completed requests <br/>in any order.", "이 완료 함수는 두 전제에 <br/>ASSERT를 사용합니다.": "This completion function <br/>uses ASSERT for both <br/>preconditions."}
  v_handler["PipelineHandler는 버퍼 <br/>완료와 요청 완료를 알릴 <br/>책임이 있습니다."]
  v_complete_buffer["completeBuffer는 <br/>CameraManager 스레드에서 <br/>호출해야 하며, 앱에 버퍼 <br/>완료를 알린 뒤 요청의 내부 <br/>버퍼 추적을 갱신합니다."]
  v_buffer_result["completeBuffer는 요청의 <br/>모든 버퍼가 완료되면 <br/>true를, 그렇지 않으면 <br/>false를 반환합니다."]
  v_complete_request["마지막 버퍼도 요청을 자동 <br/>완료하지 않습니다. 필요한 <br/>추가 작업 기회가 주어진 뒤 <br/>handler가 completeRequest를 <br/>명시 호출해야 합니다."]
  v_request["완료된 request를 알리는 <br/>함수는 CameraManager <br/>스레드에서 호출해야 하며, <br/>반환 후 handler가 해당 <br/>request에 접근하면 안 <br/>됩니다."]
  v_application["요청은 application에 제출 <br/>순서로 반환됩니다. <br/>handler는 완료된 요청을 <br/>순서 제약 없이 알릴 수 <br/>있습니다."]
  v_private_complete["Request::Private::<br/>complete는 요청 상태가 <br/>RequestPending이고 대기 <br/>중인 버퍼가 없는지 ASSERT로 <br/>검사합니다."]
  v_assert["ASSERT 조건이 거짓이면 <br/>Fatal 오류를 기록하고 <br/>실행을 중단합니다. NDEBUG로 <br/>코드가 제외되거나 검사를 <br/>통과하면 중단하지 않습니다."]
  v_handler -->|"handler는 버퍼 완료 알림에 <br/>completeBuffer를 호출해야 <br/>합니다."| v_complete_buffer
  v_handler -->|"handler는 요청 완료에 <br/>completeRequest를 명시 <br/>호출해야 합니다."| v_complete_request
  v_complete_buffer -->|"completeBuffer의 반환값은 <br/>모든 버퍼의 완료 여부를 <br/>나타냅니다."| v_buffer_result
  v_complete_buffer -->|"request는 완료된 버퍼가 <br/>속한 요청입니다."| v_request
  v_complete_request -->|"completeRequest는 버퍼 <br/>완료만으로 자동 완료되지 <br/>않은 request를 명시 <br/>완료합니다."| v_request
  v_request -->|"완료된 요청은 application에 <br/>제출 순서로 반환됩니다."| v_application
  v_request -->|"Request::Private::<br/>complete는 request의 상태와 <br/>대기 버퍼를 검사합니다."| v_private_complete
  v_private_complete -->|"이 완료 함수는 두 전제에 <br/>ASSERT를 사용합니다."| v_assert
```

[Mermaid 원문](complete_request.normal-buffer-request-duties.mmd)

??? note "그림 근거와 확인 범위"
    정상 버퍼 완료 경로에서 어떤 API를 어느 스레드에서 호출하며 요청 완료 전제와 반환 후 의무는 무엇입니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="PipelineHandler is responsible for signaling buffer and request completion.">PipelineHandler는 버퍼 완료와 요청 완료를 알릴 책임이 있습니다.</span> | [src/libcamera/pipeline_handler.cpp:547](#source-4c7b87eaff217a5f) |
    | <span data-sdd-label-en="Call completeBuffer on the CameraManager thread; it notifies the app and updates buffer tracking.">completeBuffer는 CameraManager 스레드에서 호출해야 하며, 앱에 버퍼 완료를 알린 뒤 요청의 내부 버퍼 추적을 갱신합니다.</span> | [src/libcamera/pipeline_handler.cpp:547](#source-4c7b87eaff217a5f) |
    | <span data-sdd-label-en="completeBuffer returns true if all buffers in the request are complete, and false otherwise.">completeBuffer는 요청의 모든 버퍼가 완료되면 true를, 그렇지 않으면 false를 반환합니다.</span> | [src/libcamera/pipeline_handler.cpp:547](#source-4c7b87eaff217a5f) |
    | <span data-sdd-label-en="The last buffer does not complete the request; the handler must explicitly call completeRequest after any needed work.">마지막 버퍼도 요청을 자동 완료하지 않습니다. 필요한 추가 작업 기회가 주어진 뒤 handler가 completeRequest를 명시 호출해야 합니다.</span> | [src/libcamera/pipeline_handler.cpp:547](#source-4c7b87eaff217a5f) |
    | <span data-sdd-label-en="Call the completion function on the CameraManager thread; the handler must not access the request after it returns.">완료된 request를 알리는 함수는 CameraManager 스레드에서 호출해야 하며, 반환 후 handler가 해당 request에 접근하면 안 됩니다.</span> | [src/libcamera/pipeline_handler.cpp:571](#source-fc411ef7c16f9e55) |
    | <span data-sdd-label-en="Requests return to the application in submission order; the handler may report completed requests in any order.">요청은 application에 제출 순서로 반환됩니다. handler는 완료된 요청을 순서 제약 없이 알릴 수 있습니다.</span> | [src/libcamera/pipeline_handler.cpp:571](#source-fc411ef7c16f9e55) |
    | <span data-sdd-label-en="Request::Private::complete asserts that the request is RequestPending and has no pending buffers.">Request::Private::complete는 요청 상태가 RequestPending이고 대기 중인 버퍼가 없는지 ASSERT로 검사합니다.</span> | [src/libcamera/request.cpp:125](#source-df36eeb30bb5a348) |
    | <span data-sdd-label-en="ASSERT logs a Fatal error and aborts if false; passing or compiling it out with NDEBUG does not abort.">ASSERT 조건이 거짓이면 Fatal 오류를 기록하고 실행을 중단합니다. NDEBUG로 코드가 제외되거나 검사를 통과하면 중단하지 않습니다.</span> | [src/libcamera/base/log.cpp:1044](#source-bae93ab8b66697ce) |
    | <span data-sdd-label-en="The handler must call completeBuffer to signal buffer completion.">handler는 버퍼 완료 알림에 completeBuffer를 호출해야 합니다.</span> | [src/libcamera/pipeline_handler.cpp:547](#source-4c7b87eaff217a5f) |
    | <span data-sdd-label-en="The handler must explicitly call completeRequest to complete the request.">handler는 요청 완료에 completeRequest를 명시 호출해야 합니다.</span> | [src/libcamera/pipeline_handler.cpp:547](#source-4c7b87eaff217a5f) |
    | <span data-sdd-label-en="The completeBuffer return value reports whether all buffers are complete.">completeBuffer의 반환값은 모든 버퍼의 완료 여부를 나타냅니다.</span> | [src/libcamera/pipeline_handler.cpp:547](#source-4c7b87eaff217a5f) |
    | <span data-sdd-label-en="The request contains the completed buffer.">request는 완료된 버퍼가 속한 요청입니다.</span> | [src/libcamera/pipeline_handler.cpp:547](#source-4c7b87eaff217a5f) |
    | <span data-sdd-label-en="completeRequest explicitly completes a request that buffer completion alone does not complete.">completeRequest는 버퍼 완료만으로 자동 완료되지 않은 request를 명시 완료합니다.</span> | [src/libcamera/pipeline_handler.cpp:547](#source-4c7b87eaff217a5f) |
    | <span data-sdd-label-en="Completed requests return to the application in submission order.">완료된 요청은 application에 제출 순서로 반환됩니다.</span> | [src/libcamera/pipeline_handler.cpp:571](#source-fc411ef7c16f9e55) |
    | <span data-sdd-label-en="Request::Private::complete checks the request status and pending buffers.">Request::Private::complete는 request의 상태와 대기 버퍼를 검사합니다.</span> | [src/libcamera/request.cpp:125](#source-df36eeb30bb5a348) |
    | <span data-sdd-label-en="This completion function uses ASSERT for both preconditions.">이 완료 함수는 두 전제에 ASSERT를 사용합니다.</span> | [src/libcamera/request.cpp:125](#source-df36eeb30bb5a348) |
<!-- /sdd:visual:normal-buffer-request-duties -->

<!-- sdd:visual:pipeline-cancellation-boundary -->
### 공통 취소 함수와 내부 버퍼 통지의 경계

```mermaid
flowchart TB
%% sdd:translations {"ASSERT가 통과하거나 코드가 <br/>제거되어 실행이 계속되면 <br/>doCancelRequest를 <br/>호출합니다.": "If ASSERT passes or its <br/>code is removed and <br/>execution continues, cancel <br/>calls doCancelRequest.", "PipelineHandler.<br/>cancelRequest가 요청 취소를 <br/>시작합니다.": "PipelineHandler.<br/>cancelRequest starts <br/>cancelling the request.", "Request::Private::cancel에 <br/>진입합니다.": "Request::Private::cancel is <br/>entered.", "cancelRequest가 <br/>completeRequest를 <br/>호출합니다.": "cancelRequest calls <br/>completeRequest.", "cancelRequest가 cancel을 <br/>호출합니다.": "cancelRequest calls cancel.", "cancel이 RequestPending <br/>상태를 ASSERT로 확인합니다.": "cancel checks the <br/>RequestPending status with <br/>ASSERT.", "cancel이 정상 반환하면 <br/>cancelRequest가 <br/>completeRequest를 <br/>호출합니다.": "When cancel returns <br/>normally, cancelRequest <br/>calls completeRequest.", "doCancelRequest가 정상 <br/>복귀하면 cancel이 <br/>반환합니다.": "When doCancelRequest <br/>returns normally, cancel <br/>returns.", "doCancelRequest가 정상 <br/>복귀하면 cancel이 정상 <br/>반환합니다. <br/>doCancelRequest만 <br/>호출한다고 다른 문맥에서도 <br/>요청 완료가 보장되지는 <br/>않습니다.": "When doCancelRequest <br/>returns normally, cancel <br/>returns normally. Calling <br/>doCancelRequest alone does <br/>not guarantee request <br/>completion in other <br/>contexts.", "doCancelRequest는 각 <br/>pending 버퍼를 취소하고 <br/>bufferCompleted를 직접 <br/>emit한 뒤 cancelled#95;를 <br/>설정하고 pending#95;, <br/>notifiers#95;, timer#95;를 <br/>정리합니다.": "doCancelRequest cancels <br/>each pending buffer and <br/>directly emits <br/>bufferCompleted, then sets <br/>cancelled#95; and clears <br/>pending#95;, notifiers#95; and <br/>timer#95;.", "활성 ASSERT가 실패하면 <br/>Fatal 오류를 기록하고 <br/>프로그램을 중단합니다. <br/>log.h를 포함하기 전에 <br/>NDEBUG를 정의하면 ASSERT <br/>코드는 생성되지 않습니다.": "If active ASSERT fails, it <br/>logs a Fatal error and <br/>aborts. If NDEBUG is <br/>defined before including <br/>log.h, ASSERT generates no <br/>code."}
  v_pipeline["PipelineHandler.<br/>cancelRequest가 요청 취소를 <br/>시작합니다."]
  v_cancel_entry["Request::Private::cancel에 <br/>진입합니다."]
  v_assert["활성 ASSERT가 실패하면 <br/>Fatal 오류를 기록하고 <br/>프로그램을 중단합니다. <br/>log.h를 포함하기 전에 <br/>NDEBUG를 정의하면 ASSERT <br/>코드는 생성되지 않습니다."]
  v_helper["doCancelRequest는 각 <br/>pending 버퍼를 취소하고 <br/>bufferCompleted를 직접 <br/>emit한 뒤 cancelled#95;를 <br/>설정하고 pending#95;, <br/>notifiers#95;, timer#95;를 <br/>정리합니다."]
  v_cancel_return["doCancelRequest가 정상 <br/>복귀하면 cancel이 정상 <br/>반환합니다. <br/>doCancelRequest만 <br/>호출한다고 다른 문맥에서도 <br/>요청 완료가 보장되지는 <br/>않습니다."]
  v_complete["cancelRequest가 <br/>completeRequest를 <br/>호출합니다."]
  v_pipeline -->|"cancelRequest가 cancel을 <br/>호출합니다."| v_cancel_entry
  v_cancel_entry -->|"cancel이 RequestPending <br/>상태를 ASSERT로 확인합니다."| v_assert
  v_assert -->|"ASSERT가 통과하거나 코드가 <br/>제거되어 실행이 계속되면 <br/>doCancelRequest를 <br/>호출합니다."| v_helper
  v_helper -->|"doCancelRequest가 정상 <br/>복귀하면 cancel이 <br/>반환합니다."| v_cancel_return
  v_cancel_return -->|"cancel이 정상 반환하면 <br/>cancelRequest가 <br/>completeRequest를 <br/>호출합니다."| v_complete
```

[Mermaid 원문](complete_request.pipeline-cancellation-boundary.mmd)

??? note "그림 근거와 확인 범위"
    PipelineHandler.cancelRequest는 어떤 호출 순서로 요청을 완료하며 내부 doCancelRequest만의 호출은 무엇을 보장하지 않습니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="PipelineHandler.cancelRequest starts cancelling the request.">PipelineHandler.cancelRequest가 요청 취소를 시작합니다.</span> | [src/libcamera/pipeline_handler.cpp:613](#source-6ba72880e6e3c679) |
    | <span data-sdd-label-en="Request::Private::cancel is entered.">Request::Private::cancel에 진입합니다.</span> | [src/libcamera/pipeline_handler.cpp:613](#source-6ba72880e6e3c679) · [src/libcamera/request.cpp:162](#source-e9fdc8369fb3af5d) |
    | <span data-sdd-label-en="If active ASSERT fails, it logs a Fatal error and aborts. If NDEBUG is defined before including log.h, ASSERT generates no code.">활성 ASSERT가 실패하면 Fatal 오류를 기록하고 프로그램을 중단합니다. log.h를 포함하기 전에 NDEBUG를 정의하면 ASSERT 코드는 생성되지 않습니다.</span> | [src/libcamera/request.cpp:162](#source-e9fdc8369fb3af5d) · [src/libcamera/base/log.cpp:1044](#source-bae93ab8b66697ce) |
    | <span data-sdd-label-en="doCancelRequest cancels each pending buffer and directly emits bufferCompleted, then sets cancelled_ and clears pending_, notifiers_ and timer_.">doCancelRequest는 각 pending 버퍼를 취소하고 bufferCompleted를 직접 emit한 뒤 cancelled&#95;를 설정하고 pending&#95;, notifiers&#95;, timer&#95;를 정리합니다.</span> | [src/libcamera/request.cpp:139](#source-cbbfc26d3f1b6807) |
    | <span data-sdd-label-en="When doCancelRequest returns normally, cancel returns normally. Calling doCancelRequest alone does not guarantee request completion in other contexts.">doCancelRequest가 정상 복귀하면 cancel이 정상 반환합니다. doCancelRequest만 호출한다고 다른 문맥에서도 요청 완료가 보장되지는 않습니다.</span> | [src/libcamera/request.cpp:162](#source-e9fdc8369fb3af5d) · [src/libcamera/request.cpp:139](#source-cbbfc26d3f1b6807) |
    | <span data-sdd-label-en="cancelRequest calls completeRequest.">cancelRequest가 completeRequest를 호출합니다.</span> | [src/libcamera/pipeline_handler.cpp:613](#source-6ba72880e6e3c679) |
    | <span data-sdd-label-en="cancelRequest calls cancel.">cancelRequest가 cancel을 호출합니다.</span> | [src/libcamera/pipeline_handler.cpp:613](#source-6ba72880e6e3c679) |
    | <span data-sdd-label-en="cancel checks the RequestPending status with ASSERT.">cancel이 RequestPending 상태를 ASSERT로 확인합니다.</span> | [src/libcamera/request.cpp:162](#source-e9fdc8369fb3af5d) |
    | <span data-sdd-label-en="If ASSERT passes or its code is removed and execution continues, cancel calls doCancelRequest.">ASSERT가 통과하거나 코드가 제거되어 실행이 계속되면 doCancelRequest를 호출합니다.</span> | [src/libcamera/request.cpp:162](#source-e9fdc8369fb3af5d) · [src/libcamera/base/log.cpp:1044](#source-bae93ab8b66697ce) |
    | <span data-sdd-label-en="When doCancelRequest returns normally, cancel returns.">doCancelRequest가 정상 복귀하면 cancel이 반환합니다.</span> | [src/libcamera/request.cpp:162](#source-e9fdc8369fb3af5d) |
    | <span data-sdd-label-en="When cancel returns normally, cancelRequest calls completeRequest.">cancel이 정상 반환하면 cancelRequest가 completeRequest를 호출합니다.</span> | [src/libcamera/pipeline_handler.cpp:613](#source-6ba72880e6e3c679) |
<!-- /sdd:visual:pipeline-cancellation-boundary -->

근거 원문: [src/libcamera/pipeline_handler.cpp:571](#source-fc411ef7c16f9e55) · [src/libcamera/pipeline_handler.cpp:547](#source-4c7b87eaff217a5f) · [src/libcamera/pipeline_handler.cpp:571](#source-2d8f7d0a25996e09) · [src/libcamera/request.cpp:125](#source-df36eeb30bb5a348) · [src/libcamera/request.cpp:139](#source-cbbfc26d3f1b6807) · [src/libcamera/pipeline_handler.cpp:613](#source-6ba72880e6e3c679) · [src/libcamera/request.cpp:162](#source-e9fdc8369fb3af5d) · [src/libcamera/base/log.cpp:1044](#source-bae93ab8b66697ce)

## 대기 요청을 확인하고 앱으로 알리는 경로

`Request::Private::complete`는 요청 상태가 `RequestPending`이고 대기 버퍼가 없는지 `ASSERT`로 검사합니다. 이어서 `cancelled_`가 참이면 상태를 `RequestCancelled`로, 거짓이면 `RequestComplete`로 갱신합니다. `ASSERT`는 `log.h`를 포함하기 전에 `NDEBUG`가 정의되면 코드를 생성하지 않습니다. `src/libcamera/request.cpp:125`, `src/libcamera/base/log.cpp:1022`

<!-- sdd:visual:ordered-completion-loop -->
### 요청 상태 갱신과 제출 순서 반환

```mermaid
flowchart TB
%% sdd:translations {"Camera의 requestComplete에 <br/>제거한 req를 전달합니다.": "Pass the removed req to <br/>Camera#39;s requestComplete.", "PipelineHandler의 <br/>completeRequest가 입력 <br/>request의 complete를 <br/>호출합니다.": "PipelineHandler calls <br/>complete for the input <br/>request.", "complete가 정상 복귀하면 <br/>큐를 확인합니다.": "Check the queue when <br/>complete returns normally.", "doQueueRequests가 대기 중인 <br/>요청을 파이프라인에 큐잉할 <br/>수 있게 한 뒤 <br/>completeRequest가 끝납니다.": "doQueueRequests allows <br/>waiting requests to be <br/>queued to the pipeline, and <br/>completeRequest ends.", "queuedRequests#95;가 비어 <br/>있는지 확인합니다.": "Check whether <br/>queuedRequests#95; is empty.", "requestComplete가 정상 <br/>복귀할 때만 큐를 다시 <br/>확인합니다.": "Check the queue again only <br/>if requestComplete returns <br/>normally.", "검사가 통과하거나 <br/>컴파일되지 않았다면 <br/>cancelled#95;가 참일 때 <br/>RequestCancelled, 거짓일 때 <br/>RequestComplete를 <br/>저장합니다.": "If the checks pass or are <br/>omitted, request stores <br/>RequestCancelled when <br/>cancelled#95; is true, else <br/>RequestComplete.", "검사가 통과하거나 <br/>컴파일되지 않았다면 큐 앞의 <br/>req를 제거합니다.": "If the check passes or is <br/>omitted, remove the front <br/>req from the queue.", "검사가 통과하거나 <br/>컴파일되지 않은 경우 <br/>제거합니다.": "Remove the request if the <br/>check passes or is omitted.", "검사가 통과하거나 <br/>컴파일되지 않은 경우 상태를 <br/>저장합니다.": "Store the status if the <br/>checks pass or are omitted.", "앞의 req에 대기 버퍼가 <br/>없는지 ASSERT로 검사합니다. <br/>활성 검사가 실패하면 실행을 <br/>중단합니다.": "ASSERT checks that the <br/>front req has no pending <br/>buffers. An active failure <br/>aborts execution.", "앞의 요청이 Pending이 <br/>아니면 대기 버퍼를 <br/>검사합니다. #91;false#93;": "If the front request is not <br/>pending, check its pending <br/>buffers. #91;false#93;", "앞의 요청이 Pending이면 <br/>반복을 끝내고 대기 요청의 <br/>큐잉을 재개합니다. #91;true#93;": "If the front request is <br/>pending, break and allow <br/>waiting requests to be <br/>queued. #91;true#93;", "입력 request가 Pending이고 <br/>대기 버퍼가 없는지 ASSERT로 <br/>검사합니다. 활성 검사가 <br/>실패하면 실행을 중단합니다.": "ASSERT checks that the <br/>input request is pending <br/>and has no pending buffers. <br/>An active failure aborts <br/>execution.", "제거한 요청을 전달합니다.": "Pass the removed request.", "큐 앞의 req가 <br/>RequestPending인지 <br/>확인합니다. 이 req는 입력 <br/>request와 다를 수 있습니다.": "Check whether the front req <br/>is RequestPending. It may <br/>differ from the input <br/>request.", "큐가 비어 있으면 대기 <br/>요청의 큐잉을 재개합니다. <br/>#91;false#93;": "Allow waiting requests to <br/>be queued if the queue is <br/>empty. #91;false#93;", "큐에 요청이 있으면 앞의 <br/>요청을 확인합니다. #91;true#93;": "Check the front request if <br/>the queue is nonempty. <br/>#91;true#93;", "호출한 complete가 입력 <br/>request를 검사합니다.": "The called complete checks <br/>the input request."}
  v_entry["PipelineHandler의 <br/>completeRequest가 입력 <br/>request의 complete를 <br/>호출합니다."]
  v_input_assert["입력 request가 Pending이고 <br/>대기 버퍼가 없는지 ASSERT로 <br/>검사합니다. 활성 검사가 <br/>실패하면 실행을 중단합니다."]
  v_input_status["검사가 통과하거나 <br/>컴파일되지 않았다면 <br/>cancelled#95;가 참일 때 <br/>RequestCancelled, 거짓일 때 <br/>RequestComplete를 <br/>저장합니다."]
  v_queue{"queuedRequests#95;가 비어 <br/>있는지 확인합니다."}
  v_front{"큐 앞의 req가 <br/>RequestPending인지 <br/>확인합니다. 이 req는 입력 <br/>request와 다를 수 있습니다."}
  v_front_assert["앞의 req에 대기 버퍼가 <br/>없는지 ASSERT로 검사합니다. <br/>활성 검사가 실패하면 실행을 <br/>중단합니다."]
  v_pop["검사가 통과하거나 <br/>컴파일되지 않았다면 큐 앞의 <br/>req를 제거합니다."]
  v_notify["Camera의 requestComplete에 <br/>제거한 req를 전달합니다."]
  v_resume["doQueueRequests가 대기 중인 <br/>요청을 파이프라인에 큐잉할 <br/>수 있게 한 뒤 <br/>completeRequest가 끝납니다."]
  v_entry -->|"호출한 complete가 입력 <br/>request를 검사합니다."| v_input_assert
  v_input_assert -->|"검사가 통과하거나 <br/>컴파일되지 않은 경우 상태를 <br/>저장합니다."| v_input_status
  v_input_status -->|"complete가 정상 복귀하면 <br/>큐를 확인합니다."| v_queue
  v_queue -->|"큐에 요청이 있으면 앞의 <br/>요청을 확인합니다. #91;true#93;"| v_front
  v_queue -->|"큐가 비어 있으면 대기 <br/>요청의 큐잉을 재개합니다. <br/>#91;false#93;"| v_resume
  v_front -->|"앞의 요청이 Pending이면 <br/>반복을 끝내고 대기 요청의 <br/>큐잉을 재개합니다. #91;true#93;"| v_resume
  v_front -->|"앞의 요청이 Pending이 <br/>아니면 대기 버퍼를 <br/>검사합니다. #91;false#93;"| v_front_assert
  v_front_assert -->|"검사가 통과하거나 <br/>컴파일되지 않은 경우 <br/>제거합니다."| v_pop
  v_pop -->|"제거한 요청을 전달합니다."| v_notify
  v_notify -->|"requestComplete가 정상 <br/>복귀할 때만 큐를 다시 <br/>확인합니다."| v_queue
```

[Mermaid 원문](complete_request.ordered-completion-loop.mmd)

??? note "그림 근거와 확인 범위"
    completeRequest는 상태를 갱신한 뒤 큐 앞의 어떤 조건을 검사하고 언제 대기 큐 전달을 재개합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="PipelineHandler calls complete for the input request.">PipelineHandler의 completeRequest가 입력 request의 complete를 호출합니다.</span> | [src/libcamera/pipeline_handler.cpp:584](#source-695328706c4e6d8e) |
    | <span data-sdd-label-en="ASSERT checks that the input request is pending and has no pending buffers. An active failure aborts execution.">입력 request가 Pending이고 대기 버퍼가 없는지 ASSERT로 검사합니다. 활성 검사가 실패하면 실행을 중단합니다.</span> | [src/libcamera/request.cpp:125](#source-df36eeb30bb5a348) · [src/libcamera/base/log.cpp:1022](#source-47a6ef3943a7b53c) |
    | <span data-sdd-label-en="If the checks pass or are omitted, request stores RequestCancelled when cancelled_ is true, else RequestComplete.">검사가 통과하거나 컴파일되지 않았다면 cancelled&#95;가 참일 때 RequestCancelled, 거짓일 때 RequestComplete를 저장합니다.</span> | [src/libcamera/request.cpp:125](#source-df36eeb30bb5a348) |
    | <span data-sdd-label-en="Check whether queuedRequests_ is empty.">queuedRequests&#95;가 비어 있는지 확인합니다.</span> | [src/libcamera/pipeline_handler.cpp:584](#source-695328706c4e6d8e) |
    | <span data-sdd-label-en="Check whether the front req is RequestPending. It may differ from the input request.">큐 앞의 req가 RequestPending인지 확인합니다. 이 req는 입력 request와 다를 수 있습니다.</span> | [src/libcamera/pipeline_handler.cpp:584](#source-695328706c4e6d8e) |
    | <span data-sdd-label-en="ASSERT checks that the front req has no pending buffers. An active failure aborts execution.">앞의 req에 대기 버퍼가 없는지 ASSERT로 검사합니다. 활성 검사가 실패하면 실행을 중단합니다.</span> | [src/libcamera/pipeline_handler.cpp:584](#source-695328706c4e6d8e) · [src/libcamera/base/log.cpp:1022](#source-47a6ef3943a7b53c) |
    | <span data-sdd-label-en="If the check passes or is omitted, remove the front req from the queue.">검사가 통과하거나 컴파일되지 않았다면 큐 앞의 req를 제거합니다.</span> | [src/libcamera/pipeline_handler.cpp:584](#source-695328706c4e6d8e) |
    | <span data-sdd-label-en="Pass the removed req to Camera&#x27;s requestComplete.">Camera의 requestComplete에 제거한 req를 전달합니다.</span> | [src/libcamera/pipeline_handler.cpp:584](#source-695328706c4e6d8e) |
    | <span data-sdd-label-en="doQueueRequests allows waiting requests to be queued to the pipeline, and completeRequest ends.">doQueueRequests가 대기 중인 요청을 파이프라인에 큐잉할 수 있게 한 뒤 completeRequest가 끝납니다.</span> | [src/libcamera/pipeline_handler.cpp:584](#source-695328706c4e6d8e) |
    | <span data-sdd-label-en="The called complete checks the input request.">호출한 complete가 입력 request를 검사합니다.</span> | [src/libcamera/pipeline_handler.cpp:584](#source-695328706c4e6d8e) · [src/libcamera/request.cpp:125](#source-df36eeb30bb5a348) |
    | <span data-sdd-label-en="Store the status if the checks pass or are omitted.">검사가 통과하거나 컴파일되지 않은 경우 상태를 저장합니다.</span> | [src/libcamera/request.cpp:125](#source-df36eeb30bb5a348) |
    | <span data-sdd-label-en="Check the queue when complete returns normally.">complete가 정상 복귀하면 큐를 확인합니다.</span> | [src/libcamera/pipeline_handler.cpp:584](#source-695328706c4e6d8e) |
    | <span data-sdd-label-en="Check the front request if the queue is nonempty. · !data-&gt;queuedRequests_.empty() [true]">큐에 요청이 있으면 앞의 요청을 확인합니다. · &#33;data-&gt;queuedRequests&#95;.empty&#40;&#41; &#91;true&#93;</span> | [src/libcamera/pipeline_handler.cpp:584](#source-695328706c4e6d8e) |
    | <span data-sdd-label-en="Allow waiting requests to be queued if the queue is empty. · !data-&gt;queuedRequests_.empty() [false]">큐가 비어 있으면 대기 요청의 큐잉을 재개합니다. · &#33;data-&gt;queuedRequests&#95;.empty&#40;&#41; &#91;false&#93;</span> | [src/libcamera/pipeline_handler.cpp:584](#source-695328706c4e6d8e) |
    | <span data-sdd-label-en="If the front request is pending, break and allow waiting requests to be queued. · req-&gt;status() == Request::RequestPending [true]">앞의 요청이 Pending이면 반복을 끝내고 대기 요청의 큐잉을 재개합니다. · req-&gt;status&#40;&#41; == Request::RequestPending &#91;true&#93;</span> | [src/libcamera/pipeline_handler.cpp:584](#source-695328706c4e6d8e) |
    | <span data-sdd-label-en="If the front request is not pending, check its pending buffers. · req-&gt;status() == Request::RequestPending [false]">앞의 요청이 Pending이 아니면 대기 버퍼를 검사합니다. · req-&gt;status&#40;&#41; == Request::RequestPending &#91;false&#93;</span> | [src/libcamera/pipeline_handler.cpp:584](#source-695328706c4e6d8e) |
    | <span data-sdd-label-en="Remove the request if the check passes or is omitted.">검사가 통과하거나 컴파일되지 않은 경우 제거합니다.</span> | [src/libcamera/pipeline_handler.cpp:584](#source-695328706c4e6d8e) |
    | <span data-sdd-label-en="Pass the removed request.">제거한 요청을 전달합니다.</span> | [src/libcamera/pipeline_handler.cpp:584](#source-695328706c4e6d8e) |
    | <span data-sdd-label-en="Check the queue again only if requestComplete returns normally.">requestComplete가 정상 복귀할 때만 큐를 다시 확인합니다.</span> | [src/libcamera/pipeline_handler.cpp:584](#source-695328706c4e6d8e) |
<!-- /sdd:visual:ordered-completion-loop -->

<!-- sdd:visual:camera-completion-notification-guard -->
### 카메라 상태에 따른 완료 알림과 Fatal

```mermaid
flowchart TB
%% sdd:translations {"범위 밖이면 검사가 <br/>-EACCES를 반환합니다. <br/>Fatal은 메시지를 출력한 뒤 <br/>프로그램을 즉시 중단합니다.": "Outside the range, the <br/>check returns -EACCES. <br/>Fatal terminates the <br/>program immediately after <br/>printing the message.", "범위 안이면 검사가 0을 <br/>반환합니다. <br/>requestCompleted.emit#40;<br/>request#41;를 호출한 뒤 함수가 <br/>끝납니다.": "Inside the range, the check <br/>returns 0. The function <br/>ends after calling <br/>requestCompleted.emit#40;<br/>request#41;.", "아니요. 검사가 0을 <br/>반환합니다. #91;false#93;": "No. The check returns 0. <br/>#91;false#93;", "예. 검사가 0이 아닌 값을 <br/>반환합니다. #91;true#93;": "Yes. The check returns a <br/>nonzero value. #91;true#93;", "접근 검사가 상태를 <br/>거절했습니까? <br/>CameraStopping부터 <br/>CameraRunning까지 양끝을 <br/>포함해 검사하며 연결 해제를 <br/>허용합니다.": "Does the access check <br/>reject the state? It checks <br/>CameraStopping through <br/>CameraRunning and allows <br/>disconnection."}
  v_check{"접근 검사가 상태를 <br/>거절했습니까? <br/>CameraStopping부터 <br/>CameraRunning까지 양끝을 <br/>포함해 검사하며 연결 해제를 <br/>허용합니다."}
  v_fatal["범위 밖이면 검사가 <br/>-EACCES를 반환합니다. <br/>Fatal은 메시지를 출력한 뒤 <br/>프로그램을 즉시 중단합니다."]
  v_emit["범위 안이면 검사가 0을 <br/>반환합니다. <br/>requestCompleted.emit#40;<br/>request#41;를 호출한 뒤 함수가 <br/>끝납니다."]
  v_check -->|"예. 검사가 0이 아닌 값을 <br/>반환합니다. #91;true#93;"| v_fatal
  v_check -->|"아니요. 검사가 0을 <br/>반환합니다. #91;false#93;"| v_emit
```

[Mermaid 원문](complete_request.camera-completion-notification-guard.mmd)

??? note "그림 근거와 확인 범위"
    Camera::requestComplete는 상태 검사 결과에 따라 언제 Fatal로 중단하고 언제 requestCompleted를 내보냅니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Does the access check reject the state? It checks CameraStopping through CameraRunning and allows disconnection.">접근 검사가 상태를 거절했습니까? CameraStopping부터 CameraRunning까지 양끝을 포함해 검사하며 연결 해제를 허용합니다.</span> | [src/libcamera/camera.cpp:1475](#source-10493c434ca1f81c) · [src/libcamera/camera.cpp:709](#source-0840d2509c9e395b) |
    | <span data-sdd-label-en="Outside the range, the check returns -EACCES. Fatal terminates the program immediately after printing the message.">범위 밖이면 검사가 -EACCES를 반환합니다. Fatal은 메시지를 출력한 뒤 프로그램을 즉시 중단합니다.</span> | [src/libcamera/camera.cpp:1475](#source-10493c434ca1f81c) · [src/libcamera/camera.cpp:709](#source-0840d2509c9e395b) · [src/libcamera/base/log.cpp:1022](#source-47a6ef3943a7b53c) |
    | <span data-sdd-label-en="Inside the range, the check returns 0. The function ends after calling requestCompleted.emit(request).">범위 안이면 검사가 0을 반환합니다. requestCompleted.emit&#40;request&#41;를 호출한 뒤 함수가 끝납니다.</span> | [src/libcamera/camera.cpp:1475](#source-10493c434ca1f81c) · [src/libcamera/camera.cpp:709](#source-0840d2509c9e395b) |
    | <span data-sdd-label-en="Yes. The check returns a nonzero value. · _d()-&gt;isAccessAllowed(Private::CameraStopping, Private::CameraRunning, true) [true]">예. 검사가 0이 아닌 값을 반환합니다. · &#95;d&#40;&#41;-&gt;isAccessAllowed&#40;Private::CameraStopping, Private::CameraRunning, true&#41; &#91;true&#93;</span> | [src/libcamera/camera.cpp:1475](#source-10493c434ca1f81c) · [src/libcamera/camera.cpp:709](#source-0840d2509c9e395b) · [src/libcamera/base/log.cpp:1022](#source-47a6ef3943a7b53c) |
    | <span data-sdd-label-en="No. The check returns 0. · _d()-&gt;isAccessAllowed(Private::CameraStopping, Private::CameraRunning, true) [false]">아니요. 검사가 0을 반환합니다. · &#95;d&#40;&#41;-&gt;isAccessAllowed&#40;Private::CameraStopping, Private::CameraRunning, true&#41; &#91;false&#93;</span> | [src/libcamera/camera.cpp:1475](#source-10493c434ca1f81c) · [src/libcamera/camera.cpp:709](#source-0840d2509c9e395b) |
<!-- /sdd:visual:camera-completion-notification-guard -->

`PipelineHandler::completeRequest`는 전달받은 요청을 완료 처리한 뒤 `queuedRequests_`를 앞에서부터 확인합니다. 맨 앞 요청이 `RequestPending`이면 `break`하여 그 요청을 제거하지 않습니다. 그렇지 않으면 대기 버퍼가 없는지 `ASSERT`로 검사하고 `pop_front`로 제거한 뒤 `Camera::requestComplete`를 호출합니다. `src/libcamera/pipeline_handler.cpp:584`

`Camera::requestComplete`는 `allowDisconnected=true`로 `CameraStopping`부터 `CameraRunning`까지의 상태를 검사합니다. 상태가 이 범위 안이면 `requestCompleted.emit(request)`로 알립니다. 범위 밖이면 `Fatal` 로그를 출력하고 실행을 중단합니다. `PipelineHandler::completeRequest`는 정상 경로에서 루프 뒤에 `doQueueRequests(camera)`를 호출하여 대기 중인 요청을 파이프라인에 큐잉할 수 있게 합니다. `src/libcamera/camera.cpp:1475`, `src/libcamera/camera.cpp:709`, `src/libcamera/base/log.cpp:1022`, `src/libcamera/pipeline_handler.cpp:584`

근거 원문: [src/libcamera/pipeline_handler.cpp:584](#source-695328706c4e6d8e) · [src/libcamera/camera.cpp:1475](#source-10493c434ca1f81c) · [src/libcamera/camera.cpp:709](#source-0840d2509c9e395b) · [src/libcamera/request.cpp:125](#source-df36eeb30bb5a348) · [src/libcamera/base/log.cpp:1022](#source-47a6ef3943a7b53c)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | PipelineHandler::completeRequest의 목적, CameraManager 스레드 호출 의무와 반환 뒤 핸들러의 요청 접근 금지를 첫 문단에서 함께 설명하세요. 둘째 문단에서는 마지막 completeBuffer만으로 요청이 자동 완료되지 않아 명시적인 요청 완료가 필요하며, 핸들러가 완료된 요청을 임의 순서로 통지해도 앱 반환은 제출 순서를 보존하는 계약을 설명하세요. completeRequest 호출 의무나 소유권을 별도 문단에서 반복하지 마세요. | [요청 완료를 알릴 책임과 접근 종료](#요청-완료를-알릴-책임과-접근-종료) | 코드 근거와 설명 연결 |
    | Request::Private::complete의 RequestPending·대기 버퍼 ASSERT와 cancelled_에 따른 RequestCancelled/RequestComplete 갱신을 설명하세요. PipelineHandler::completeRequest의 queuedRequests_ 맨 앞이 RequestPending이면 break하고 pop하지 않는 경로와, Pending이 아니면 대기 버퍼 ASSERT·pop_front·Camera::requestComplete로 진행하는 경로를 같은 문단에서 대조하세요. Camera::requestComplete의 CameraStopping부터 CameraRunning까지 상태 검사와 allowDisconnected=true를 설명하고 허용 상태에서 requestCompleted.emit으로 알리는 경로와 범위 밖 Fatal 로그에 따른 실행 중단을 구분하세요. ASSERT는 log.h 포함 전에 NDEBUG가 정의되면 코드가 생성되지 않는 검사임을 한 번 설명하세요. 정상 경로에서 루프 뒤 doQueueRequests가 대기 요청 큐잉을 허용하는 역할을 마지막 한 문단으로 설명하세요. 새 결과의 조건을 이해하는 데 필요한 짧은 참조는 허용하되 같은 결과의 전체 설명을 반복하지 마세요. doQueueRequests 구현의 발췌 범위 안내나 별도 확인 요청은 쓰지 말고 호출 역할만 설명하세요. 네 문단 이내로 작성하세요. | [대기 요청을 확인하고 앱으로 알리는 경로](#대기-요청을-확인하고-앱으로-알리는-경로) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-fc411ef7c16f9e55"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:571"
    `src/libcamera/pipeline_handler.cpp:571`에서 시작하는 발췌입니다. 종료 줄은 583이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `9a0ed4d736b974c075804a539949762c99c31dc1c6ad62f7185af6f1b9c6e741`
    
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
    ```

<a id="source-4c7b87eaff217a5f"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:547"
    `src/libcamera/pipeline_handler.cpp:547`에서 시작하는 발췌입니다. 종료 줄은 568이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `2ac611d3ff5edaf4e1f140f09f9bbe2f9304b41b9e198beb46a5660e5f195282`
    
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
    ```

<a id="source-2d8f7d0a25996e09"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:571"
    `src/libcamera/pipeline_handler.cpp:571`에서 시작하는 발췌입니다. 종료 줄은 604이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `b250ffb8ca77d7fd55df385a63f73ffa5b5fba5bbff4c79f5bd5edd8278fb6ee`
    
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
    ```

<a id="source-df36eeb30bb5a348"></a>

??? note "소스 근거: src/libcamera/request.cpp:125"
    `src/libcamera/request.cpp:125`에서 시작하는 발췌입니다. 종료 줄은 137이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `045f2e5cc0e38ea289081014b5a245bbff80c5d3ecc255ed620a1e5d486ba8ec`
    
    ```text
    void Request::Private::complete()
    {
    	Request *request = _o<Request>();
    
    	ASSERT(request->status() == RequestPending);
    	ASSERT(!hasPendingBuffers());
    
    	request->status_ = cancelled_ ? RequestCancelled : RequestComplete;
    
    	LOG(Request, Debug) << request->toString();
    
    	LIBCAMERA_TRACEPOINT(request_complete, this);
    }
    ```

<a id="source-cbbfc26d3f1b6807"></a>

??? note "소스 근거: src/libcamera/request.cpp:139"
    `src/libcamera/request.cpp:139`에서 시작하는 발췌입니다. 종료 줄은 152이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `f3ccc6e43d58f4af003478867e265560de0674cd1f1c454d6178ff47529eb06c`
    
    ```text
    void Request::Private::doCancelRequest()
    {
    	Request *request = _o<Request>();
    
    	for (FrameBuffer *buffer : pending_) {
    		buffer->_d()->cancel();
    		camera_->bufferCompleted.emit(request, buffer);
    	}
    
    	cancelled_ = true;
    	pending_.clear();
    	notifiers_.clear();
    	timer_.reset();
    }
    ```

<a id="source-6ba72880e6e3c679"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:613"
    `src/libcamera/pipeline_handler.cpp:613`에서 시작하는 발췌입니다. 종료 줄은 617이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `a3d0d59ae735b64d64f8b6d8d5393bfa75cd803c646d9d3f7b2a8c1b14d3be36`
    
    ```text
    void PipelineHandler::cancelRequest(Request *request)
    {
    	request->_d()->cancel();
    	completeRequest(request);
    }
    ```

<a id="source-e9fdc8369fb3af5d"></a>

??? note "소스 근거: src/libcamera/request.cpp:162"
    `src/libcamera/request.cpp:162`에서 시작하는 발췌입니다. 종료 줄은 170이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e17ceaea94ddf2edb3419c9b474af9c94383a8b300edbb495cf440024e60128c`
    
    ```text
    void Request::Private::cancel()
    {
    	LIBCAMERA_TRACEPOINT(request_cancel, this);
    
    	Request *request = _o<Request>();
    	ASSERT(request->status() == RequestPending);
    
    	doCancelRequest();
    }
    ```

<a id="source-bae93ab8b66697ce"></a>

??? note "소스 근거: src/libcamera/base/log.cpp:1044"
    `src/libcamera/base/log.cpp:1044`에서 시작하는 발췌입니다. 종료 줄은 1058이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `522875c26e54ef1cc9cce7c4797356dda57027e4fb9bd25ceb4b352ccc7bcefe`
    
    ```text
    \def ASSERT(condition)
     * \hideinitializer
     * \brief Abort program execution if assertion fails
     *
     * If \a condition is false, ASSERT() logs an error message with the Fatal log
     * level and aborts program execution.
     *
     * If the macro NDEBUG is defined before including log.h, ASSERT() generates no
     * code.
     *
     * Using conditions that have side effects with ASSERT() is not recommended, as
     * these effects would depend on whether NDEBUG is defined or not. Similarly,
     * ASSERT() should not be used to check for errors that can occur under normal
     * conditions as those checks would then be removed when compiling with NDEBUG.
     */
    ```

<a id="source-695328706c4e6d8e"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:584"
    `src/libcamera/pipeline_handler.cpp:584`에서 시작하는 발췌입니다. 종료 줄은 604이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `06aba06c3d636ad21e1409ac329ab9c3853776a2eef8ca443acbb49c8893e90b`
    
    ```text
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
    ```

<a id="source-10493c434ca1f81c"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1475"
    `src/libcamera/camera.cpp:1475`에서 시작하는 발췌입니다. 종료 줄은 1489이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `9e8e2a873ef95a0b778292f2da2da90ec0b5ef5b312ffe88b7298d3aed624c47`
    
    ```text
    \brief Handle request completion and notify application
     * \param[in] request The request that has completed
     *
     * This function is called by the pipeline handler to notify the camera that
     * the request has completed. It emits the requestCompleted signal.
     */
    void Camera::requestComplete(Request *request)
    {
    	/* Disconnected cameras are still able to complete requests. */
    	if (_d()->isAccessAllowed(Private::CameraStopping, Private::CameraRunning,
    				  true))
    		LOG(Camera, Fatal) << "Trying to complete a request when stopped";
    
    	requestCompleted.emit(request);
    }
    ```

<a id="source-0840d2509c9e395b"></a>

??? note "소스 근거: src/libcamera/camera.cpp:709"
    `src/libcamera/camera.cpp:709`에서 시작하는 발췌입니다. 종료 줄은 730이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `d04dbcf64bf95e8e89669e5c85602d590cd8d6530e44cd275cee39348d644b8f`
    
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
    ```

<a id="source-47a6ef3943a7b53c"></a>

??? note "소스 근거: src/libcamera/base/log.cpp:1022"
    `src/libcamera/base/log.cpp:1022`에서 시작하는 발췌입니다. 종료 줄은 1060이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `52e64d292f59786541e66fe48f5bae65256bdced60c803aa76bf3637083b47b0`
    
    ```text
    \def LOG(category, severity)
     * \hideinitializer
     * \brief Log a message
     * \param[in] category Category (optional)
     * \param[in] severity Severity
     *
     * Return an std::ostream reference to which a message can be logged using the
     * iostream API. The \a category, if specified, sets the message category. When
     * absent the default category is used. The  \a severity controls whether the
     * message is printed or discarded, depending on the log level for the category.
     *
     * If the severity is set to Fatal, execution is aborted and the program
     * terminates immediately after printing the message.
     *
     * \warning Logging from the destructor of a global object, either directly or
     * indirectly, results in undefined behaviour.
     *
     * \todo Allow logging from destructors of global objects to the largest
     * possible extent
     */
    
    /**
     * \def ASSERT(condition)
     * \hideinitializer
     * \brief Abort program execution if assertion fails
     *
     * If \a condition is false, ASSERT() logs an error message with the Fatal log
     * level and aborts program execution.
     *
     * If the macro NDEBUG is defined before including log.h, ASSERT() generates no
     * code.
     *
     * Using conditions that have side effects with ASSERT() is not recommended, as
     * these effects would depend on whether NDEBUG is defined or not. Similarly,
     * ASSERT() should not be used to check for errors that can occur under normal
     * conditions as those checks would then be removed when compiling with NDEBUG.
     */
    
    } /* namespace libcamera */
    ```

## 주요 확인 지점

아래 항목은 추출한 호출에서 고른 코드 탐색 지점입니다. 나열 순서는 실행 순서가 아닙니다.

| 확인할 내용 | 호출 측과 대상 | 구분 | 근거 |
|---|---|---|---|
| 완료 처리 | `PipelineHandler` → `Private::complete()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:588` |
| 완료 통지 | `PipelineHandler` → `Camera::requestComplete()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:599` |
| 대기 요청 처리 | `PipelineHandler` → `PipelineHandler::doQueueRequests()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:603` |
| 하드웨어별 큐잉 후보 | `PipelineHandler` → `PipelineHandlerISI::queueRequestDevice()`<br>`PipelineHandler` → `PipelineHandlerIPU3::queueRequestDevice()`<br>`PipelineHandler` → `PipelineHandlerMaliC55::queueRequestDevice()`<br>`PipelineHandler` → `PipelineHandlerRkISP1::queueRequestDevice()`<br>`PipelineHandler` → `PipelineHandlerBase::queueRequestDevice()`<br>`PipelineHandler` → `SimplePipelineHandler::queueRequestDevice()`<br>`PipelineHandler` → `PipelineHandlerUVC::queueRequestDevice()`<br>`PipelineHandler` → `PipelineHandlerVimc::queueRequestDevice()`<br>`PipelineHandler` → `PipelineHandlerVirtual::queueRequestDevice()` | 동적 디스패치 후보이며 실제 대상은 확인이 필요합니다. | `src/libcamera/pipeline_handler.cpp:498` |

## 주요 호출 관계

화살표는 호출 측과 대상을 연결합니다. 시간 순서나 모든 경로의 실행을 뜻하지 않습니다. 점선에는 가상 호출 후보·예약 대상 등 확인이 필요한 관계를 표시합니다.

```mermaid
flowchart LR
  p0["Camera"]
  p1["PipelineHandler"]
  p2["PipelineHandlerBase"]
  p3["PipelineHandlerIPU3"]
  p4["PipelineHandlerISI"]
  p5["PipelineHandlerMaliC55"]
  p6["PipelineHandlerRkISP1"]
  p7["PipelineHandlerUVC"]
  p8["PipelineHandlerVimc"]
  p9["PipelineHandlerVirtual"]
  p10["Private"]
  p11["SimplePipelineHandler"]
  p1 -->|"complete#40;#41;"| p10
  p1 -->|"requestComplete#40;#41;"| p0
  p1 -->|"doQueueRequests#40;#41;"| p1
  p1 -.->|"queueRequestDevice#40;#41; · virtual 후보"| p4
  p1 -.->|"queueRequestDevice#40;#41; · virtual 후보"| p3
  p1 -.->|"queueRequestDevice#40;#41; · virtual 후보"| p5
  p1 -.->|"queueRequestDevice#40;#41; · virtual 후보"| p6
  p1 -.->|"queueRequestDevice#40;#41; · virtual 후보"| p2
  p1 -.->|"queueRequestDevice#40;#41; · virtual 후보"| p11
  p1 -.->|"queueRequestDevice#40;#41; · virtual 후보"| p7
  p1 -.->|"queueRequestDevice#40;#41; · virtual 후보"| p8
  p1 -.->|"queueRequestDevice#40;#41; · virtual 후보"| p9
```

## 추적 범위와 경계

요약의 hide 규칙에 해당하는 호출은 63개입니다. 전체 추적 기록에는 해당 호출도 모두 보존합니다. 기록 번호는 정적 탐색의 식별자이며 실행 순번이 아닙니다.

조건 분기, 반복 횟수와 실제 실행 스레드는 이 호출 목록만으로 확정할 수 없습니다. 가상 호출 후보는 실제 객체에 따라 선택됩니다. 예약 표시는 인자로 전달한 메서드 대상을 뜻하며, 비동기 실행을 보증하지 않습니다. 호출부의 연결 방식과 동기화 계약을 확인해야 합니다.

| 호출 지점 | 후보 또는 예약 대상 | 확인할 경계 | 근거 |
|---|---|---|---|
| `PipelineHandler` | `PipelineHandlerISI::queueRequestDevice()`<br>`PipelineHandlerIPU3::queueRequestDevice()`<br>`PipelineHandlerMaliC55::queueRequestDevice()`<br>`PipelineHandlerRkISP1::queueRequestDevice()`<br>`PipelineHandlerBase::queueRequestDevice()`<br>`SimplePipelineHandler::queueRequestDevice()`<br>`PipelineHandlerUVC::queueRequestDevice()`<br>`PipelineHandlerVimc::queueRequestDevice()`<br>`PipelineHandlerVirtual::queueRequestDevice()` | 동적 디스패치 후보이며 실제 대상은 확인이 필요합니다. | `src/libcamera/pipeline_handler.cpp:498` |

## 전체 추적 기록

아래 구간을 펼치면 요약에서 제외된 호출까지 확인할 수 있습니다. 이 목록은 추출 깊이 안에서 수집한 기록이며, 소스의 모든 실행 경로를 포함한다는 뜻은 아닙니다.

??? note "추적 기록 1–25 / 126개"

    | 기록 | 호출 측 | 대상 | 구분 | 근거 |
    |---|---|---|---|---|
    | 1 | `PipelineHandler` | `Private::camera()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:586` |
    | 2 | `PipelineHandler` | `Request::_d()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:586` |
    | 3 | `PipelineHandler` | `Private::complete()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:588` |
    | 4 | `Private` | `Private::_o()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:127` |
    | 5 | `Private` | `Request::status()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:129` |
    | 6 | `Private` | `log::isLogSeverityEnabled()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:129` |
    | 7 | `Private` | `LogMessageAbortGuard::LogMessageAbortGuard()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:129` |
    | 8 | `Private` | `LogMessage::stream()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:129` |
    | 9 | `Private` | `log::_log()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:129` |
    | 10 | `log` | `LogMessage::LogMessage()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:990` |
    | 11 | `LogMessage` | `utils::basename()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:858` |
    | 12 | `Private` | `Private::hasPendingBuffers()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:130` |
    | 13 | `Private` | `log::isLogSeverityEnabled()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:130` |
    | 14 | `Private` | `LogMessageAbortGuard::LogMessageAbortGuard()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:130` |
    | 15 | `Private` | `LogMessage::stream()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:130` |
    | 16 | `Private` | `log::_log()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:130` |
    | 17 | `log` | `LogMessage::LogMessage()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:990` |
    | 18 | `LogMessage` | `utils::basename()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:858` |
    | 19 | `Private` | `log::isLogSeverityEnabled()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:134` |
    | 20 | `Private` | `LogMessageAbortGuard::LogMessageAbortGuard()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:134` |
    | 21 | `Private` | `LogMessage::stream()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:134` |
    | 22 | `Private` | `log::_log()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:134` |
    | 23 | `log` | `LogMessage::LogMessage()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:990` |
    | 24 | `LogMessage` | `utils::basename()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:858` |
    | 25 | `Private` | `Request::toString()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:134` |

??? note "추적 기록 26–50 / 126개"

    | 기록 | 호출 측 | 대상 | 구분 | 근거 |
    |---|---|---|---|---|
    | 26 | `Request` | `request::operator<<()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:592` |
    | 27 | `request` | `Request::sequence()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:609` |
    | 28 | `request` | `Request::status()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:609` |
    | 29 | `request` | `Request::_d()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:610` |
    | 30 | `request` | `Request::buffers()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:610` |
    | 31 | `request` | `Request::cookie()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:611` |
    | 32 | `PipelineHandler` | `Request::_d()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:588` |
    | 33 | `PipelineHandler` | `Camera::_d()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:590` |
    | 34 | `PipelineHandler` | `Request::status()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:594` |
    | 35 | `PipelineHandler` | `Request::hasPendingBuffers()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:597` |
    | 36 | `Request` | `Private::hasPendingBuffers()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:578` |
    | 37 | `Request` | `Request::_d()` | 정적 호출 지점입니다. | `src/libcamera/request.cpp:578` |
    | 38 | `PipelineHandler` | `log::isLogSeverityEnabled()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:597` |
    | 39 | `PipelineHandler` | `LogMessageAbortGuard::LogMessageAbortGuard()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:597` |
    | 40 | `PipelineHandler` | `LogMessage::stream()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:597` |
    | 41 | `PipelineHandler` | `log::_log()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:597` |
    | 42 | `log` | `LogMessage::LogMessage()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:990` |
    | 43 | `LogMessage` | `utils::basename()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:858` |
    | 44 | `PipelineHandler` | `Camera::requestComplete()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:599` |
    | 45 | `Camera` | `Private::isAccessAllowed()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1484` |
    | 46 | `Private` | `log::isLogSeverityEnabled()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:720` |
    | 47 | `Private` | `LogMessageAbortGuard::LogMessageAbortGuard()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:720` |
    | 48 | `Private` | `LogMessage::stream()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:720` |
    | 49 | `Private` | `log::_log()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:720` |
    | 50 | `log` | `LogMessage::LogMessage()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:990` |

??? note "추적 기록 51–75 / 126개"

    | 기록 | 호출 측 | 대상 | 구분 | 근거 |
    |---|---|---|---|---|
    | 51 | `Private` | `log::isLogSeverityEnabled()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:723` |
    | 52 | `Private` | `LogMessageAbortGuard::LogMessageAbortGuard()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:723` |
    | 53 | `Private` | `LogMessage::stream()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:723` |
    | 54 | `Private` | `log::_log()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:723` |
    | 55 | `log` | `LogMessage::LogMessage()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:990` |
    | 56 | `Camera` | `Camera::_d()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1484` |
    | 57 | `Camera` | `log::isLogSeverityEnabled()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1486` |
    | 58 | `Camera` | `LogMessageAbortGuard::LogMessageAbortGuard()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1486` |
    | 59 | `Camera` | `LogMessage::stream()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1486` |
    | 60 | `Camera` | `log::_log()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1486` |
    | 61 | `log` | `LogMessage::LogMessage()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:990` |
    | 62 | `LogMessage` | `utils::basename()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:858` |
    | 63 | `Camera` | `Signal::emit()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1488` |
    | 64 | `PipelineHandler` | `PipelineHandler::doQueueRequests()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:603` |
    | 65 | `PipelineHandler` | `Camera::_d()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:511` |
    | 66 | `PipelineHandler` | `Request::_d()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:517` |
    | 67 | `PipelineHandler` | `PipelineHandler::doQueueRequest()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:525` |
    | 68 | `PipelineHandler` | `Private::camera()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:487` |
    | 69 | `PipelineHandler` | `Request::_d()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:487` |
    | 70 | `PipelineHandler` | `Camera::_d()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:488` |
    | 71 | `PipelineHandler` | `Request::_d()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:491` |
    | 72 | `PipelineHandler` | `Request::_d()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:493` |
    | 73 | `PipelineHandler` | `PipelineHandler::completeRequest()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:494` |
    | 74 | `PipelineHandler` | `PipelineHandlerISI::queueRequestDevice()` | 동적 디스패치 후보이며 실제 대상은 확인이 필요합니다. | `src/libcamera/pipeline_handler.cpp:498` |
    | 75 | `PipelineHandlerISI` | `Request::buffers()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/imx8-isi/imx8-isi.cpp:958` |

??? note "추적 기록 76–100 / 126개"

    | 기록 | 호출 측 | 대상 | 구분 | 근거 |
    |---|---|---|---|---|
    | 76 | `PipelineHandlerISI` | `PipelineHandlerISI::pipeFromStream()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/imx8-isi/imx8-isi.cpp:959` |
    | 77 | `PipelineHandlerISI` | `V4L2VideoDevice::queueBuffer()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/imx8-isi/imx8-isi.cpp:961` |
    | 78 | `PipelineHandler` | `PipelineHandlerIPU3::queueRequestDevice()` | 동적 디스패치 후보이며 실제 대상은 확인이 필요합니다. | `src/libcamera/pipeline_handler.cpp:498` |
    | 79 | `PipelineHandlerIPU3` | `PipelineHandlerIPU3::cameraData()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/ipu3/ipu3.cpp:840` |
    | 80 | `PipelineHandlerIPU3` | `IPU3CameraData::queuePendingRequests()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/ipu3/ipu3.cpp:843` |
    | 81 | `PipelineHandler` | `PipelineHandlerMaliC55::queueRequestDevice()` | 동적 디스패치 후보이며 실제 대상은 확인이 필요합니다. | `src/libcamera/pipeline_handler.cpp:498` |
    | 82 | `PipelineHandlerMaliC55` | `PipelineHandlerMaliC55::cameraData()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:1563` |
    | 83 | `PipelineHandlerMaliC55` | `PipelineHandlerMaliC55::queueRequestToCru()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:1570` |
    | 84 | `PipelineHandlerMaliC55` | `MaliC55FrameInfo::MaliC55FrameInfo()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:1577` |
    | 85 | `PipelineHandlerMaliC55` | `MaliC55FrameInfo::operator=()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:1584` |
    | 86 | `PipelineHandlerMaliC55` | `Request::sequence()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:1584` |
    | 87 | `PipelineHandlerMaliC55` | `Request::buffers()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:1586` |
    | 88 | `PipelineHandlerMaliC55` | `PipelineHandlerMaliC55::pipeFromStream()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:1587` |
    | 89 | `PipelineHandlerMaliC55` | `V4L2VideoDevice::queueBuffer()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:1589` |
    | 90 | `PipelineHandlerMaliC55` | `PipelineHandlerMaliC55::prepareFrameInfo()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:1595` |
    | 91 | `PipelineHandlerMaliC55` | `log::isLogSeverityEnabled()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:1596` |
    | 92 | `PipelineHandlerMaliC55` | `LogMessageAbortGuard::LogMessageAbortGuard()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:1596` |
    | 93 | `PipelineHandlerMaliC55` | `LogMessage::stream()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:1596` |
    | 94 | `PipelineHandlerMaliC55` | `log::_log()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:1596` |
    | 95 | `PipelineHandlerMaliC55` | `Request::sequence()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:1598` |
    | 96 | `PipelineHandlerMaliC55` | `Request::controls()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:1598` |
    | 97 | `PipelineHandlerMaliC55` | `Request::sequence()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:1599` |
    | 98 | `PipelineHandlerMaliC55` | `FrameBuffer::cookie()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:1600` |
    | 99 | `PipelineHandler` | `PipelineHandlerRkISP1::queueRequestDevice()` | 동적 디스패치 후보이며 실제 대상은 확인이 필요합니다. | `src/libcamera/pipeline_handler.cpp:498` |
    | 100 | `PipelineHandlerRkISP1` | `PipelineHandlerRkISP1::cameraData()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rkisp1/rkisp1.cpp:1343` |

??? note "추적 기록 101–125 / 126개"

    | 기록 | 호출 측 | 대상 | 구분 | 근거 |
    |---|---|---|---|---|
    | 101 | `PipelineHandlerRkISP1` | `RkISP1Frames::create()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rkisp1/rkisp1.cpp:1345` |
    | 102 | `PipelineHandlerRkISP1` | `Request::controls()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rkisp1/rkisp1.cpp:1349` |
    | 103 | `PipelineHandlerRkISP1` | `RkISP1Path::queueBuffer()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rkisp1/rkisp1.cpp:1352` |
    | 104 | `PipelineHandlerRkISP1` | `RkISP1Path::queueBuffer()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rkisp1/rkisp1.cpp:1355` |
    | 105 | `PipelineHandlerRkISP1` | `FrameBuffer::cookie()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rkisp1/rkisp1.cpp:1358` |
    | 106 | `PipelineHandler` | `PipelineHandlerBase::queueRequestDevice()` | 동적 디스패치 후보이며 실제 대상은 확인이 필요합니다. | `src/libcamera/pipeline_handler.cpp:498` |
    | 107 | `PipelineHandlerBase` | `PipelineHandlerBase::cameraData()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:757` |
    | 108 | `PipelineHandlerBase` | `CameraData::isRunning()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:759` |
    | 109 | `PipelineHandlerBase` | `log::isLogSeverityEnabled()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:762` |
    | 110 | `PipelineHandlerBase` | `LogMessageAbortGuard::LogMessageAbortGuard()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:762` |
    | 111 | `PipelineHandlerBase` | `LogMessage::stream()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:762` |
    | 112 | `PipelineHandlerBase` | `log::_log()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:762` |
    | 113 | `PipelineHandlerBase` | `Request::sequence()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:763` |
    | 114 | `PipelineHandlerBase` | `Flags::operator!()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:767` |
    | 115 | `PipelineHandlerBase` | `Flags::operator&()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:767` |
    | 116 | `PipelineHandlerBase` | `Stream::getFlags()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:767` |
    | 117 | `PipelineHandlerBase` | `Request::findBuffer()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:770` |
    | 118 | `PipelineHandlerBase` | `Stream::getBufferId()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:771` |
    | 119 | `PipelineHandlerBase` | `Stream::setExportedBuffer()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:777` |
    | 120 | `PipelineHandlerBase` | `Stream::queueBuffer()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:791` |
    | 121 | `PipelineHandlerBase` | `CameraData::handleState()` | 정적 호출 지점입니다. | `src/libcamera/pipeline/rpi/common/pipeline_base.cpp:798` |
    | 122 | `PipelineHandler` | `SimplePipelineHandler::queueRequestDevice()` | 동적 디스패치 후보이며 실제 대상은 확인이 필요합니다. | `src/libcamera/pipeline_handler.cpp:498` |
    | 123 | `PipelineHandler` | `PipelineHandlerUVC::queueRequestDevice()` | 동적 디스패치 후보이며 실제 대상은 확인이 필요합니다. | `src/libcamera/pipeline_handler.cpp:498` |
    | 124 | `PipelineHandler` | `PipelineHandlerVimc::queueRequestDevice()` | 동적 디스패치 후보이며 실제 대상은 확인이 필요합니다. | `src/libcamera/pipeline_handler.cpp:498` |
    | 125 | `PipelineHandler` | `PipelineHandlerVirtual::queueRequestDevice()` | 동적 디스패치 후보이며 실제 대상은 확인이 필요합니다. | `src/libcamera/pipeline_handler.cpp:498` |

??? note "추적 기록 126–126 / 126개"

    | 기록 | 호출 측 | 대상 | 구분 | 근거 |
    |---|---|---|---|---|
    | 126 | `PipelineHandler` | `PipelineHandler::cancelRequest()` | 정적 호출 지점입니다. | `src/libcamera/pipeline_handler.cpp:500` |

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `src/libcamera/base/log.cpp`, `src/libcamera/camera.cpp`, `src/libcamera/pipeline/imx8-isi/imx8-isi.cpp`, `src/libcamera/pipeline/ipu3/ipu3.cpp`, `src/libcamera/pipeline/mali-c55/mali-c55.cpp`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp`, `src/libcamera/pipeline/rpi/common/pipeline_base.cpp`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/request.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `c19d05128f`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-12 · 사람 검토 전

다음 단계: [캡처 종료 요청](camera_stop.md)
