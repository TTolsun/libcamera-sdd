---
generated_at: 2026-11-11T21:04:22+00:00
source_commit: da6a6ed33ed0ab305f10b6f8b44736150d39cef4
status: ok
section: framebuffer-allocator-boundary
generation_method: facts-and-llm
evidence_fingerprint: be3e8380b20431255112d3d79b0e707d0e2dbc2883faf0b46bddd6e4f4cc2e82
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "be3e8380b20431255112d3d79b0e707d0e2dbc2883faf0b46bddd6e4f4cc2e82", "answers": {"allocation-preconditions": [{"text": "`allocate()`를 호출하기 전에 카메라는 `Camera::configure()`로 이미 구성되고 정지된 상태여야 하며, 스트림은 활성 카메라 구성에 속해야 합니다.", "evidence": ["allocate-preconditions"], "covers": ["allocation-preconditions"], "kind": "behavior", "quote": "Allocate buffers suitable for capturing frames from the \\a stream. The Camera\n * shall have been previously configured with Camera::configure() and shall be\n * stopped, and the stream shall be part of the active camera configuration.", "part_id": "configured-stopped-stream"}, {"text": "`-EACCES`는 카메라가 버퍼를 할당할 수 없는 상태일 때 반환되며, `-EINVAL`은 스트림이 카메라에 속하지 않거나 활성 카메라 구성에 포함되지 않을 때 반환됩니다.", "evidence": ["allocate-state-stream-errors"], "covers": ["allocation-preconditions"], "kind": "behavior", "quote": "\\retval -EACCES The camera is not in a state where buffers can be allocated\n * \\retval -EINVAL The \\a stream does not belong to the camera or the stream is\n * not part of the active camera configuration", "part_id": "access-stream-errors"}], "reference-lifetime": [{"text": "`buffers()`는 해당 스트림에 대해 `allocate()`로 버퍼를 성공적으로 할당한 후에만 호출해야 합니다.", "evidence": ["buffers-precondition"], "covers": ["reference-lifetime"], "kind": "behavior", "quote": "This function shall only be called after successfully allocating buffers for\n * \\a stream with allocate().", "part_id": "successful-allocation"}, {"text": "`buffers()`가 반환하는 버퍼는 같은 스트림에 대해 `free()`가 호출되거나 `FrameBufferAllocator` 인스턴스가 파괴될 때까지 유효합니다.", "evidence": ["buffers-validity"], "covers": ["reference-lifetime"], "kind": "behavior", "quote": "The returned buffers are valid until free() is\n * called for the same stream or the FrameBufferAllocator instance is destroyed.", "part_id": "valid-until"}], "allocation-failure": [{"text": "`FrameBufferAllocator::allocate`는 `try_emplace`의 `inserted`가 false이면 버퍼가 이미 할당되었다는 오류를 기록하고 `-EBUSY`를 반환합니다.", "evidence": ["allocation-body"], "covers": ["allocation-failure"], "kind": "behavior", "quote": "if (!inserted) {\n\t\tLOG(Allocator, Error) << \"Buffers already allocated for stream\";\n\t\treturn -EBUSY;\n\t}", "part_id": "duplicate-allocation"}, {"text": "`FrameBufferAllocator::allocate()`는 `exportFrameBuffers()`의 반환값을 `ret`에 저장하고, `ret`가 음수이면 `buffers_.erase(it)`로 해당 `buffers_` 항목을 제거합니다.", "evidence": ["allocation-body"], "covers": ["allocation-failure"], "kind": "behavior", "quote": "if (ret < 0)\n\t\tbuffers_.erase(it);", "part_id": "export-failure"}, {"text": "`FrameBufferAllocator::allocate`는 `exportFrameBuffers`를 호출한 경우 그 결과인 `ret`를 음수 여부와 관계없이 반환합니다.", "evidence": ["export-return-code"], "covers": ["allocation-failure"], "kind": "behavior", "quote": "int ret = camera_->exportFrameBuffers(stream, &it->second);\n\tif (ret == -EINVAL)\n\t\tLOG(Allocator, Error)\n\t\t\t<< \"Stream is not part of \" << camera_->id()\n\t\t\t<< \" active configuration\";\n\n\tif (ret < 0)\n\t\tbuffers_.erase(it);\n\n\treturn ret;", "part_id": "export-return"}], "free-result": [{"text": "`FrameBufferAllocator::free`는 스트림을 찾지 못하면 `-EINVAL`을 반환하며 `buffers_` 항목을 제거하지 않습니다. 스트림을 찾으면 해당 `buffers_` 항목을 제거하고 `0`을 반환합니다.", "evidence": ["free-body"], "covers": ["free-result"], "kind": "behavior", "quote": "int FrameBufferAllocator::free(Stream *stream)\n{\n\tauto iter = buffers_.find(stream);\n\tif (iter == buffers_.end())\n\t\treturn -EINVAL;\n\n\tbuffers_.erase(iter);\n\n\treturn 0;\n}", "part_id": "stream-result"}]}, "topic_inputs": {"allocation-preconditions": "d80161760b902a2bf0e7b6c534af3c8162a7e323b04002b13efb2b922a7d057e", "reference-lifetime": "d1a8de261d78b33768b5df32cf0a1a34c5267caa479e52c86b356117b14febc9", "allocation-failure": "26c8e58f18a5557385c55ba21a2f5897ba7ec24bed7856c199dbe047b26c30ad", "free-result": "19558f7a2631971f2dbd741ac3055cbf6850cfc4a114c7e2631ba9ad7ea94c05"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["allocation-preconditions", "reference-lifetime", "allocation-failure", "free-result"], "topic_agents": {"allocation-preconditions": "cli/codex/gpt-6.1-terra", "reference-lifetime": "cli/codex/gpt-6.1-terra", "allocation-failure": "cli/codex/gpt-6.1-terra", "free-result": "cli/codex/gpt-6.1-terra"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "367d18b95f8f0d01a15ae0f4d1b70f7e13e4d0298df4215e2c449ac4905db6f9", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "d0f7ab4c48fcf52409935931eb9b93aacd48af4b19e9bb816fa496f1214fdb2f", "answer_contracts": "a39c9a8818afc47e059141d486337c0f12a7fd34319e2b6f7674fc428bc83e2b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "050c20aa2fdcceae10c6275fbb5f850f616ab5051bb67ccbcb4a204877a238d9", "explanation": "69bcaa207ef39d20f6a47ac201c3edf119f59b333e85131dea1bce85eef4006b", "design_response": "a7c199bc52bcc0e749ef01186e50bca98107473d5c82e2248712f465d02e1e69", "design_validation": "92ddb9a65c909173ff4c7cb627dff83e71c10c8258c51344ef0eb1a7a023937f"}, "validation_model": "db6c5bf57ead3ade75be2621f553363aac6222c51b55401a5bcb2b7116c69a06", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "b87a84b1bc31079837dc4dc4527ce02c9dc2cbc3a26ff7e99e0872941d213995"}, "body_sha256": "73620ea2e765317b707303d96fb709b797795b06eb4ab4776bf6bbaf99366f60"}
generated_visuals: {"schema": 1, "records": {"item-allocation-preconditions": {"input_fingerprint": "64b19ec41bcd14d7217f2d2a5725f0ffae3cd55f3e99618c026ffef78ce91cfb", "draft": {"nodes": [{"id": "camera_precondition", "symbol": "Camera", "label": "allocate()를 호출하기 전에 Camera는 Camera::configure()로 설정되어 있어야 하며 정지해 있어야 합니다.", "label_en": "Before allocate(), Camera must have been configured with Camera::configure() and stopped.", "shape": "box", "quote_ids": ["allocate-preconditions:0"]}, {"id": "stream", "symbol": "stream", "label": "stream은 활성 카메라 설정의 일부여야 합니다.", "label_en": "The stream must be part of the active camera configuration.", "shape": "box", "quote_ids": ["allocate-preconditions:0"]}, {"id": "camera", "symbol": "camera", "label": "카메라가 버퍼를 할당할 수 있는 상태인지 확인합니다.", "label_en": "Check whether the camera is in a state where buffers can be allocated.", "shape": "box", "quote_ids": ["allocate-state-stream-errors:0"]}, {"id": "eacces", "symbol": "EACCES", "label": "카메라가 버퍼를 할당할 수 있는 상태가 아니면 -EACCES가 반환됩니다.", "label_en": "If the camera cannot allocate buffers in its current state, -EACCES is returned.", "shape": "box", "quote_ids": ["allocate-state-stream-errors:0"]}, {"id": "einval", "symbol": "EINVAL", "label": "stream이 카메라에 속하지 않거나 활성 설정의 일부가 아니면 -EINVAL이 반환됩니다.", "label_en": "If stream does not belong to the camera or its active configuration, -EINVAL is returned.", "shape": "box", "quote_ids": ["allocate-state-stream-errors:1"]}], "edges": [{"from": "camera_precondition", "to": "stream", "label": "stream은 활성 카메라 설정의 일부여야 합니다.", "label_en": "The stream must be part of the active camera configuration.", "condition_ref": "always", "quote_ids": ["allocate-preconditions:0"]}, {"from": "camera", "to": "stream", "label": "stream은 카메라에 속해야 합니다.", "label_en": "The stream must belong to the camera.", "condition_ref": "always", "quote_ids": ["allocate-state-stream-errors:1"]}, {"from": "camera", "to": "eacces", "label": "카메라가 버퍼를 할당할 수 없는 상태이면 -EACCES가 반환됩니다.", "label_en": "If the camera cannot allocate buffers in its state, -EACCES is returned.", "condition_ref": "always", "quote_ids": ["allocate-state-stream-errors:0"]}, {"from": "stream", "to": "einval", "label": "stream이 카메라에 속하지 않으면 -EINVAL이 반환됩니다.", "label_en": "If stream does not belong to the camera, -EINVAL is returned.", "condition_ref": "always", "quote_ids": ["allocate-state-stream-errors:1"]}, {"from": "stream", "to": "einval", "label": "stream이 활성 카메라 설정의 일부가 아니면 -EINVAL이 반환됩니다.", "label_en": "If stream is not in the active configuration, -EINVAL is returned.", "condition_ref": "always", "quote_ids": ["allocate-state-stream-errors:1"]}]}, "graph": {"id": "item-allocation-preconditions", "topic": "allocation-preconditions", "kind": "ownership", "title": "할당 전에 확인할 카메라 상태와 스트림의 관계와 경계", "question": "allocate() 호출 전에 카메라와 스트림은 어떤 조건을 충족해야 하며, 어떤 조건에서 -EACCES와 -EINVAL이 반환되는가?", "condition_display": "evidence", "nodes": [{"id": "camera_precondition", "label": "allocate()를 호출하기 전에 Camera는 Camera::configure()로 설정되어 있어야 하며 정지해 있어야 합니다.", "label_en": "Before allocate(), Camera must have been configured with Camera::configure() and stopped.", "shape": "box", "evidence": [{"source": "allocation-preconditions/allocate-preconditions", "sha256": "87ee819fc59da5231c8e99985771ae1821150196f2ed452822578208da94972f", "quote": "Allocate buffers suitable for capturing frames from the \\a stream. The Camera\n * shall have been previously configured with Camera::configure() and shall be\n * stopped, and the stream shall be part of the active camera configuration."}]}, {"id": "stream", "label": "stream은 활성 카메라 설정의 일부여야 합니다.", "label_en": "The stream must be part of the active camera configuration.", "shape": "box", "evidence": [{"source": "allocation-preconditions/allocate-preconditions", "sha256": "87ee819fc59da5231c8e99985771ae1821150196f2ed452822578208da94972f", "quote": "Allocate buffers suitable for capturing frames from the \\a stream. The Camera\n * shall have been previously configured with Camera::configure() and shall be\n * stopped, and the stream shall be part of the active camera configuration."}]}, {"id": "camera", "label": "카메라가 버퍼를 할당할 수 있는 상태인지 확인합니다.", "label_en": "Check whether the camera is in a state where buffers can be allocated.", "shape": "box", "evidence": [{"source": "allocation-preconditions/allocate-state-stream-errors", "sha256": "46d80bb2f91831ad0dda0a83fea0d3139ce6c0f156cf75033d97a9947cafde1e", "quote": "\\retval -EACCES The camera is not in a state where buffers can be allocated"}]}, {"id": "eacces", "label": "카메라가 버퍼를 할당할 수 있는 상태가 아니면 -EACCES가 반환됩니다.", "label_en": "If the camera cannot allocate buffers in its current state, -EACCES is returned.", "shape": "box", "evidence": [{"source": "allocation-preconditions/allocate-state-stream-errors", "sha256": "46d80bb2f91831ad0dda0a83fea0d3139ce6c0f156cf75033d97a9947cafde1e", "quote": "\\retval -EACCES The camera is not in a state where buffers can be allocated"}]}, {"id": "einval", "label": "stream이 카메라에 속하지 않거나 활성 설정의 일부가 아니면 -EINVAL이 반환됩니다.", "label_en": "If stream does not belong to the camera or its active configuration, -EINVAL is returned.", "shape": "box", "evidence": [{"source": "allocation-preconditions/allocate-state-stream-errors", "sha256": "46d80bb2f91831ad0dda0a83fea0d3139ce6c0f156cf75033d97a9947cafde1e", "quote": "\\retval -EACCES The camera is not in a state where buffers can be allocated\n * \\retval -EINVAL The \\a stream does not belong to the camera or the stream is\n * not part of the active camera configuration"}]}], "edges": [{"from": "camera_precondition", "to": "stream", "label": "stream은 활성 카메라 설정의 일부여야 합니다.", "label_en": "The stream must be part of the active camera configuration.", "evidence": [{"source": "allocation-preconditions/allocate-preconditions", "sha256": "87ee819fc59da5231c8e99985771ae1821150196f2ed452822578208da94972f", "quote": "Allocate buffers suitable for capturing frames from the \\a stream. The Camera\n * shall have been previously configured with Camera::configure() and shall be\n * stopped, and the stream shall be part of the active camera configuration."}]}, {"from": "camera", "to": "stream", "label": "stream은 카메라에 속해야 합니다.", "label_en": "The stream must belong to the camera.", "evidence": [{"source": "allocation-preconditions/allocate-state-stream-errors", "sha256": "46d80bb2f91831ad0dda0a83fea0d3139ce6c0f156cf75033d97a9947cafde1e", "quote": "\\retval -EACCES The camera is not in a state where buffers can be allocated\n * \\retval -EINVAL The \\a stream does not belong to the camera or the stream is\n * not part of the active camera configuration"}]}, {"from": "camera", "to": "eacces", "label": "카메라가 버퍼를 할당할 수 없는 상태이면 -EACCES가 반환됩니다.", "label_en": "If the camera cannot allocate buffers in its state, -EACCES is returned.", "evidence": [{"source": "allocation-preconditions/allocate-state-stream-errors", "sha256": "46d80bb2f91831ad0dda0a83fea0d3139ce6c0f156cf75033d97a9947cafde1e", "quote": "\\retval -EACCES The camera is not in a state where buffers can be allocated"}]}, {"from": "stream", "to": "einval", "label": "stream이 카메라에 속하지 않으면 -EINVAL이 반환됩니다.", "label_en": "If stream does not belong to the camera, -EINVAL is returned.", "evidence": [{"source": "allocation-preconditions/allocate-state-stream-errors", "sha256": "46d80bb2f91831ad0dda0a83fea0d3139ce6c0f156cf75033d97a9947cafde1e", "quote": "\\retval -EACCES The camera is not in a state where buffers can be allocated\n * \\retval -EINVAL The \\a stream does not belong to the camera or the stream is\n * not part of the active camera configuration"}]}, {"from": "stream", "to": "einval", "label": "stream이 활성 카메라 설정의 일부가 아니면 -EINVAL이 반환됩니다.", "label_en": "If stream is not in the active configuration, -EINVAL is returned.", "evidence": [{"source": "allocation-preconditions/allocate-state-stream-errors", "sha256": "46d80bb2f91831ad0dda0a83fea0d3139ce6c0f156cf75033d97a9947cafde1e", "quote": "\\retval -EACCES The camera is not in a state where buffers can be allocated\n * \\retval -EINVAL The \\a stream does not belong to the camera or the stream is\n * not part of the active camera configuration"}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "293d751a814e0d4c34e85ad457ccd9d5eefd1a61", "reused": true, "citation_binding_revalidation": {"policy": "identifier-and-guard-boundaries-v2", "original_input_fingerprint": "64b19ec41bcd14d7217f2d2a5725f0ffae3cd55f3e99618c026ffef78ce91cfb", "new_inference": false}}, "item-reference-lifetime": {"input_fingerprint": "77da5f7326077328511a93e8691d1a1da910eba3221c5953f41afb79c2c5d1f3", "draft": {"nodes": [{"id": "allocate", "symbol": "allocate", "label": "allocate()로 해당 stream의 버퍼를 성공적으로 할당합니다.", "label_en": "Successfully allocate buffers for the stream with allocate().", "shape": "process", "quote_ids": ["buffers-precondition:0"]}, {"id": "buffers", "symbol": "buffers", "label": "buffers()는 해당 stream의 버퍼를 성공적으로 할당한 뒤에만 호출해야 합니다.", "label_en": "Call buffers() only after successfully allocating buffers for the stream.", "shape": "process", "quote_ids": ["buffers-precondition:0"]}, {"id": "returned", "symbol": "returned", "label": "반환된 버퍼는 아래 두 사건 중 먼저 발생하는 사건까지 유효합니다.", "label_en": "Returned buffers are valid until the first of the two events below.", "shape": "box", "quote_ids": ["buffers-validity:0"]}, {"id": "free", "symbol": "free", "label": "같은 stream에 대한 free() 호출은 유효기간을 끝내는 사건입니다.", "label_en": "Calling free() for the same stream is an event that ends validity.", "shape": "process", "quote_ids": ["buffers-validity:0"]}, {"id": "allocator", "symbol": "FrameBufferAllocator", "label": "FrameBufferAllocator 인스턴스의 파괴는 유효기간을 끝내는 사건입니다.", "label_en": "Destruction of the FrameBufferAllocator instance is an event that ends validity.", "shape": "process", "quote_ids": ["buffers-validity:0"]}], "edges": [{"from": "allocate", "to": "buffers", "label": "성공적으로 할당한 뒤에만 buffers()를 호출해야 합니다.", "label_en": "Call buffers() only after successful allocation.", "condition_ref": "always", "quote_ids": ["buffers-precondition:0"]}, {"from": "buffers", "to": "returned", "label": "반환된 버퍼는 아래 두 사건 중 먼저 발생하는 사건까지 유효합니다.", "label_en": "Returned buffers are valid until the first of the two events below.", "condition_ref": "always", "quote_ids": ["buffers-validity:0"]}, {"from": "returned", "to": "free", "label": "같은 stream에 대한 free() 호출이 유효기간을 끝낼 수 있습니다.", "label_en": "Calling free() for the same stream can end validity.", "condition_ref": "always", "quote_ids": ["buffers-validity:0"]}, {"from": "returned", "to": "allocator", "label": "FrameBufferAllocator 인스턴스의 파괴가 유효기간을 끝낼 수 있습니다.", "label_en": "Destruction of the FrameBufferAllocator instance can end validity.", "condition_ref": "always", "quote_ids": ["buffers-validity:0"]}]}, "graph": {"id": "item-reference-lifetime", "topic": "reference-lifetime", "kind": "ownership", "title": "buffers 반환 참조의 유효기간의 관계와 경계", "question": "buffers()는 언제 호출할 수 있으며, 반환 버퍼의 유효기간은 어떤 사건으로 끝나는가?", "condition_display": "evidence", "nodes": [{"id": "allocate", "label": "allocate()로 해당 stream의 버퍼를 성공적으로 할당합니다.", "label_en": "Successfully allocate buffers for the stream with allocate().", "shape": "box", "evidence": [{"source": "reference-lifetime/buffers-precondition", "sha256": "a12056e800d2035f519dc58a4be3dc5e3c9d51920102cc9bc27c60a32790a663", "quote": "This function shall only be called after successfully allocating buffers for\n * \\a stream with allocate()."}]}, {"id": "buffers", "label": "buffers()는 해당 stream의 버퍼를 성공적으로 할당한 뒤에만 호출해야 합니다.", "label_en": "Call buffers() only after successfully allocating buffers for the stream.", "shape": "box", "evidence": [{"source": "reference-lifetime/buffers-precondition", "sha256": "a12056e800d2035f519dc58a4be3dc5e3c9d51920102cc9bc27c60a32790a663", "quote": "This function shall only be called after successfully allocating buffers for\n * \\a stream with allocate()."}]}, {"id": "returned", "label": "반환된 버퍼는 아래 두 사건 중 먼저 발생하는 사건까지 유효합니다.", "label_en": "Returned buffers are valid until the first of the two events below.", "shape": "box", "evidence": [{"source": "reference-lifetime/buffers-validity", "sha256": "7c43c6133e383a9e56e3a9163cfca05e8df576398f363e1b13bd5056664df86b", "quote": "The returned buffers are valid until free() is\n * called for the same stream or the FrameBufferAllocator instance is destroyed."}]}, {"id": "free", "label": "같은 stream에 대한 free() 호출은 유효기간을 끝내는 사건입니다.", "label_en": "Calling free() for the same stream is an event that ends validity.", "shape": "box", "evidence": [{"source": "reference-lifetime/buffers-validity", "sha256": "7c43c6133e383a9e56e3a9163cfca05e8df576398f363e1b13bd5056664df86b", "quote": "The returned buffers are valid until free() is\n * called for the same stream or the FrameBufferAllocator instance is destroyed."}]}, {"id": "allocator", "label": "FrameBufferAllocator 인스턴스의 파괴는 유효기간을 끝내는 사건입니다.", "label_en": "Destruction of the FrameBufferAllocator instance is an event that ends validity.", "shape": "box", "evidence": [{"source": "reference-lifetime/buffers-validity", "sha256": "7c43c6133e383a9e56e3a9163cfca05e8df576398f363e1b13bd5056664df86b", "quote": "The returned buffers are valid until free() is\n * called for the same stream or the FrameBufferAllocator instance is destroyed."}]}], "edges": [{"from": "allocate", "to": "buffers", "label": "성공적으로 할당한 뒤에만 buffers()를 호출해야 합니다.", "label_en": "Call buffers() only after successful allocation.", "evidence": [{"source": "reference-lifetime/buffers-precondition", "sha256": "a12056e800d2035f519dc58a4be3dc5e3c9d51920102cc9bc27c60a32790a663", "quote": "This function shall only be called after successfully allocating buffers for\n * \\a stream with allocate()."}]}, {"from": "buffers", "to": "returned", "label": "반환된 버퍼는 아래 두 사건 중 먼저 발생하는 사건까지 유효합니다.", "label_en": "Returned buffers are valid until the first of the two events below.", "evidence": [{"source": "reference-lifetime/buffers-validity", "sha256": "7c43c6133e383a9e56e3a9163cfca05e8df576398f363e1b13bd5056664df86b", "quote": "The returned buffers are valid until free() is\n * called for the same stream or the FrameBufferAllocator instance is destroyed."}]}, {"from": "returned", "to": "free", "label": "같은 stream에 대한 free() 호출이 유효기간을 끝낼 수 있습니다.", "label_en": "Calling free() for the same stream can end validity.", "evidence": [{"source": "reference-lifetime/buffers-validity", "sha256": "7c43c6133e383a9e56e3a9163cfca05e8df576398f363e1b13bd5056664df86b", "quote": "The returned buffers are valid until free() is\n * called for the same stream or the FrameBufferAllocator instance is destroyed."}]}, {"from": "returned", "to": "allocator", "label": "FrameBufferAllocator 인스턴스의 파괴가 유효기간을 끝낼 수 있습니다.", "label_en": "Destruction of the FrameBufferAllocator instance can end validity.", "evidence": [{"source": "reference-lifetime/buffers-validity", "sha256": "7c43c6133e383a9e56e3a9163cfca05e8df576398f363e1b13bd5056664df86b", "quote": "The returned buffers are valid until free() is\n * called for the same stream or the FrameBufferAllocator instance is destroyed."}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78", "citation_binding_policy": "identifier-and-guard-boundaries-v2", "reused": false}, "item-allocation-failure": {"input_fingerprint": "4b111362ea5911ce6fa5978e43bd4dfe505cb6de0ab4c4500b9464100cba3f86", "draft": {"nodes": [{"id": "insert", "symbol": "inserted", "label": "buffers_.try_emplace(stream)의 삽입 결과를 확인합니다.", "label_en": "Check the insertion result of buffers_.try_emplace(stream).", "shape": "decision", "quote_ids": ["allocation-body:0", "allocation-body:1"]}, {"id": "busy", "symbol": "EBUSY", "label": "중복 할당을 기록하고 -EBUSY를 반환합니다. 기존 buffers_ 항목은 지우지 않습니다.", "label_en": "Log the duplicate allocation and return -EBUSY; keep the existing buffers_ entry.", "shape": "box", "quote_ids": ["allocation-body:0", "allocation-body:1"]}, {"id": "export", "symbol": "exportFrameBuffers", "label": "새 항목에 버퍼를 내보내고 결과를 ret에 저장합니다.", "label_en": "Export buffers to the new entry and save the result in ret.", "shape": "process", "quote_ids": ["allocation-body:0", "allocation-body:2"]}, {"id": "invalid", "symbol": "ret", "label": "ret이 구성 오류인지 확인합니다.", "label_en": "Check ret for a configuration error.", "shape": "decision", "quote_ids": ["allocation-body:2"]}, {"id": "log", "symbol": "LOG", "label": "stream이 활성 구성에 속하지 않는다는 오류를 기록합니다.", "label_en": "Log that stream is not part of the active configuration.", "shape": "process", "quote_ids": ["allocation-body:2"]}, {"id": "failure", "symbol": "if", "label": "내보내기 결과가 실패인지 확인합니다.", "label_en": "Check whether the export result indicates failure.", "shape": "decision", "quote_ids": ["allocation-body:3"]}, {"id": "erase", "symbol": "erase", "label": "내보내기에 실패하면 새 buffers_ 항목을 지웁니다.", "label_en": "Erase the new buffers_ entry when export fails.", "shape": "process", "quote_ids": ["allocation-body:3"]}, {"id": "result", "symbol": "return", "label": "내보내기 결과 ret을 반환합니다.", "label_en": "Return the export result ret.", "shape": "box", "quote_ids": ["allocation-body:4"]}], "edges": [{"from": "insert", "to": "busy", "label": "삽입되지 않으면 중복 할당으로 종료합니다.", "label_en": "If insertion fails, return for duplicate allocation.", "condition_ref": "c0:true", "quote_ids": ["allocation-body:0", "allocation-body:1"]}, {"from": "insert", "to": "export", "label": "삽입되면 버퍼를 내보냅니다.", "label_en": "If insertion succeeds, export the buffers.", "condition_ref": "c0:false", "quote_ids": ["allocation-body:0", "allocation-body:1", "allocation-body:2"]}, {"from": "export", "to": "invalid", "label": "내보내기 결과를 확인합니다.", "label_en": "Check the export result.", "condition_ref": "always", "quote_ids": ["allocation-body:2"]}, {"from": "invalid", "to": "log", "label": "구성 오류이면 오류를 기록합니다.", "label_en": "If it is a configuration error, log it.", "condition_ref": "c2:true", "quote_ids": ["allocation-body:2"]}, {"from": "invalid", "to": "failure", "label": "구성 오류가 아니면 실패 여부를 확인합니다.", "label_en": "Otherwise, check for failure.", "condition_ref": "c2:false", "quote_ids": ["allocation-body:2", "allocation-body:3"]}, {"from": "log", "to": "failure", "label": "오류를 기록한 뒤 실패 여부를 확인합니다.", "label_en": "After logging, check for failure.", "condition_ref": "always", "quote_ids": ["allocation-body:2", "allocation-body:3"]}, {"from": "failure", "to": "erase", "label": "실패하면 항목을 지웁니다.", "label_en": "If export fails, erase the entry.", "condition_ref": "c1:true", "quote_ids": ["allocation-body:3"]}, {"from": "erase", "to": "result", "label": "항목을 지운 뒤 ret을 반환합니다.", "label_en": "After erasing the entry, return ret.", "condition_ref": "always", "quote_ids": ["allocation-body:3", "allocation-body:4"]}, {"from": "failure", "to": "result", "label": "실패하지 않으면 항목을 지우지 않고 ret을 반환합니다.", "label_en": "Otherwise, return ret without erasing the entry.", "condition_ref": "c1:false", "quote_ids": ["allocation-body:3", "allocation-body:4"]}]}, "graph": {"id": "item-allocation-failure", "topic": "allocation-failure", "kind": "ownership", "title": "중복 할당과 내보내기 실패를 구분하기의 관계와 경계", "question": "중복 할당과 내보내기 실패는 처리 흐름, 반환값 및 buffers_ 항목 처리에서 어떻게 다른가?", "condition_display": "evidence", "nodes": [{"id": "insert", "label": "buffers_.try_emplace(stream)의 삽입 결과를 확인합니다.", "label_en": "Check the insertion result of buffers_.try_emplace(stream).", "shape": "decision", "evidence": [{"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "int FrameBufferAllocator::allocate(Stream *stream)\n{\n\tconst auto &[it, inserted] = buffers_.try_emplace(stream);"}, {"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "if (!inserted) {\n\t\tLOG(Allocator, Error) << \"Buffers already allocated for stream\";\n\t\treturn -EBUSY;\n\t}"}]}, {"id": "busy", "label": "중복 할당을 기록하고 -EBUSY를 반환합니다. 기존 buffers_ 항목은 지우지 않습니다.", "label_en": "Log the duplicate allocation and return -EBUSY; keep the existing buffers_ entry.", "shape": "box", "evidence": [{"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "int FrameBufferAllocator::allocate(Stream *stream)\n{\n\tconst auto &[it, inserted] = buffers_.try_emplace(stream);"}, {"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "if (!inserted) {\n\t\tLOG(Allocator, Error) << \"Buffers already allocated for stream\";\n\t\treturn -EBUSY;\n\t}"}]}, {"id": "export", "label": "새 항목에 버퍼를 내보내고 결과를 ret에 저장합니다.", "label_en": "Export buffers to the new entry and save the result in ret.", "shape": "box", "evidence": [{"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "int FrameBufferAllocator::allocate(Stream *stream)\n{\n\tconst auto &[it, inserted] = buffers_.try_emplace(stream);"}, {"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "int ret = camera_->exportFrameBuffers(stream, &it->second);\n\tif (ret == -EINVAL)\n\t\tLOG(Allocator, Error)\n\t\t\t<< \"Stream is not part of \" << camera_->id()\n\t\t\t<< \" active configuration\";"}]}, {"id": "invalid", "label": "ret이 구성 오류인지 확인합니다.", "label_en": "Check ret for a configuration error.", "shape": "decision", "evidence": [{"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "int ret = camera_->exportFrameBuffers(stream, &it->second);\n\tif (ret == -EINVAL)\n\t\tLOG(Allocator, Error)\n\t\t\t<< \"Stream is not part of \" << camera_->id()\n\t\t\t<< \" active configuration\";"}]}, {"id": "log", "label": "stream이 활성 구성에 속하지 않는다는 오류를 기록합니다.", "label_en": "Log that stream is not part of the active configuration.", "shape": "box", "evidence": [{"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "int ret = camera_->exportFrameBuffers(stream, &it->second);\n\tif (ret == -EINVAL)\n\t\tLOG(Allocator, Error)\n\t\t\t<< \"Stream is not part of \" << camera_->id()\n\t\t\t<< \" active configuration\";"}]}, {"id": "failure", "label": "내보내기 결과가 실패인지 확인합니다.", "label_en": "Check whether the export result indicates failure.", "shape": "decision", "evidence": [{"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "if (ret < 0)\n\t\tbuffers_.erase(it);"}]}, {"id": "erase", "label": "내보내기에 실패하면 새 buffers_ 항목을 지웁니다.", "label_en": "Erase the new buffers_ entry when export fails.", "shape": "box", "evidence": [{"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "if (ret < 0)\n\t\tbuffers_.erase(it);"}]}, {"id": "result", "label": "내보내기 결과 ret을 반환합니다.", "label_en": "Return the export result ret.", "shape": "box", "evidence": [{"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "return ret;\n}"}]}], "edges": [{"from": "insert", "to": "busy", "label": "삽입되지 않으면 중복 할당으로 종료합니다. · !inserted [true]", "label_en": "If insertion fails, return for duplicate allocation. · !inserted [true]", "evidence": [{"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "int FrameBufferAllocator::allocate(Stream *stream)\n{\n\tconst auto &[it, inserted] = buffers_.try_emplace(stream);"}, {"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "if (!inserted) {\n\t\tLOG(Allocator, Error) << \"Buffers already allocated for stream\";\n\t\treturn -EBUSY;\n\t}"}]}, {"from": "insert", "to": "export", "label": "삽입되면 버퍼를 내보냅니다. · !inserted [false]", "label_en": "If insertion succeeds, export the buffers. · !inserted [false]", "evidence": [{"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "int FrameBufferAllocator::allocate(Stream *stream)\n{\n\tconst auto &[it, inserted] = buffers_.try_emplace(stream);"}, {"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "if (!inserted) {\n\t\tLOG(Allocator, Error) << \"Buffers already allocated for stream\";\n\t\treturn -EBUSY;\n\t}"}, {"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "int ret = camera_->exportFrameBuffers(stream, &it->second);\n\tif (ret == -EINVAL)\n\t\tLOG(Allocator, Error)\n\t\t\t<< \"Stream is not part of \" << camera_->id()\n\t\t\t<< \" active configuration\";"}]}, {"from": "export", "to": "invalid", "label": "내보내기 결과를 확인합니다.", "label_en": "Check the export result.", "evidence": [{"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "int ret = camera_->exportFrameBuffers(stream, &it->second);\n\tif (ret == -EINVAL)\n\t\tLOG(Allocator, Error)\n\t\t\t<< \"Stream is not part of \" << camera_->id()\n\t\t\t<< \" active configuration\";"}]}, {"from": "invalid", "to": "log", "label": "구성 오류이면 오류를 기록합니다. · ret == -EINVAL [true]", "label_en": "If it is a configuration error, log it. · ret == -EINVAL [true]", "evidence": [{"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "int ret = camera_->exportFrameBuffers(stream, &it->second);\n\tif (ret == -EINVAL)\n\t\tLOG(Allocator, Error)\n\t\t\t<< \"Stream is not part of \" << camera_->id()\n\t\t\t<< \" active configuration\";"}]}, {"from": "invalid", "to": "failure", "label": "구성 오류가 아니면 실패 여부를 확인합니다. · ret == -EINVAL [false]", "label_en": "Otherwise, check for failure. · ret == -EINVAL [false]", "evidence": [{"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "int ret = camera_->exportFrameBuffers(stream, &it->second);\n\tif (ret == -EINVAL)\n\t\tLOG(Allocator, Error)\n\t\t\t<< \"Stream is not part of \" << camera_->id()\n\t\t\t<< \" active configuration\";"}, {"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "if (ret < 0)\n\t\tbuffers_.erase(it);"}]}, {"from": "log", "to": "failure", "label": "오류를 기록한 뒤 실패 여부를 확인합니다.", "label_en": "After logging, check for failure.", "evidence": [{"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "int ret = camera_->exportFrameBuffers(stream, &it->second);\n\tif (ret == -EINVAL)\n\t\tLOG(Allocator, Error)\n\t\t\t<< \"Stream is not part of \" << camera_->id()\n\t\t\t<< \" active configuration\";"}, {"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "if (ret < 0)\n\t\tbuffers_.erase(it);"}]}, {"from": "failure", "to": "erase", "label": "실패하면 항목을 지웁니다. · ret < 0 [true]", "label_en": "If export fails, erase the entry. · ret < 0 [true]", "evidence": [{"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "if (ret < 0)\n\t\tbuffers_.erase(it);"}]}, {"from": "erase", "to": "result", "label": "항목을 지운 뒤 ret을 반환합니다.", "label_en": "After erasing the entry, return ret.", "evidence": [{"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "if (ret < 0)\n\t\tbuffers_.erase(it);"}, {"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "return ret;\n}"}]}, {"from": "failure", "to": "result", "label": "실패하지 않으면 항목을 지우지 않고 ret을 반환합니다. · ret < 0 [false]", "label_en": "Otherwise, return ret without erasing the entry. · ret < 0 [false]", "evidence": [{"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "if (ret < 0)\n\t\tbuffers_.erase(it);"}, {"source": "allocation-failure/allocation-body", "sha256": "0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b", "quote": "return ret;\n}"}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "293d751a814e0d4c34e85ad457ccd9d5eefd1a61", "reused": true, "citation_binding_revalidation": {"policy": "identifier-and-guard-boundaries-v2", "original_input_fingerprint": "4b111362ea5911ce6fa5978e43bd4dfe505cb6de0ab4c4500b9464100cba3f86", "new_inference": false}}}, "body_sha256": "73620ea2e765317b707303d96fb709b797795b06eb4ab4776bf6bbaf99366f60"}
revalidated_from: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
---

# FrameBufferAllocator의 실패와 참조 수명

**중복 할당·버퍼 내보내기 실패와 반환 버퍼의 유효기간을 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| `allocate()`를 호출하기 전에 카메라는 `Camera::configure()`로 이미 구성되고 정지된 상태여야 하며, 스트림은 활성 카메라 구성에 속해야 합니다. | [할당 전에 확인할 카메라 상태와 스트림](#할당-전에-확인할-카메라-상태와-스트림) |
| `buffers()`는 해당 스트림에 대해 `allocate()`로 버퍼를 성공적으로 할당한 후에만 호출해야 합니다. | [buffers 반환 참조의 유효기간](#buffers-반환-참조의-유효기간) |
| `FrameBufferAllocator::allocate`는 `try_emplace`의 `inserted`가 false이면 버퍼가 이미 할당되었다는 오류를 기록하고 `-EBUSY`를 반환합니다. | [중복 할당과 내보내기 실패를 구분하기](#중복-할당과-내보내기-실패를-구분하기) |
| `FrameBufferAllocator::free`는 스트림을 찾지 못하면 `-EINVAL`을 반환하며 `buffers_` 항목을 제거하지 않습니다. | [free의 스트림 조회와 반환값](#free의-스트림-조회와-반환값) |

## 할당 전에 확인할 카메라 상태와 스트림

`allocate()`를 호출하기 전에 카메라는 `Camera::configure()`로 이미 구성되고 정지된 상태여야 하며, 스트림은 활성 카메라 구성에 속해야 합니다. `-EACCES`는 카메라가 버퍼를 할당할 수 없는 상태일 때 반환되며, `-EINVAL`은 스트림이 카메라에 속하지 않거나 활성 카메라 구성에 포함되지 않을 때 반환됩니다. `src/libcamera/framebuffer_allocator.cpp:72`, `src/libcamera/framebuffer_allocator.cpp:81`

<!-- sdd:visual:item-allocation-preconditions -->
### 할당 전에 확인할 카메라 상태와 스트림의 관계와 경계

```mermaid
flowchart TB
%% sdd:translations {"allocate#40;#41;를 호출하기 전에 <br/>Camera는 <br/>Camera::configure#40;#41;로 <br/>설정되어 있어야 하며 정지해 <br/>있어야 합니다.": "Before allocate#40;#41;, Camera <br/>must have been configured <br/>with Camera::configure#40;#41; <br/>and stopped.", "stream은 카메라에 속해야 <br/>합니다.": "The stream must belong to <br/>the camera.", "stream은 활성 카메라 설정의 <br/>일부여야 합니다.": "The stream must be part of <br/>the active camera <br/>configuration.", "stream이 카메라에 속하지 <br/>않거나 활성 설정의 일부가 <br/>아니면 -EINVAL이 반환됩니다.": "If stream does not belong <br/>to the camera or its active <br/>configuration, -EINVAL is <br/>returned.", "stream이 카메라에 속하지 <br/>않으면 -EINVAL이 반환됩니다.": "If stream does not belong <br/>to the camera, -EINVAL is <br/>returned.", "stream이 활성 카메라 설정의 <br/>일부가 아니면 -EINVAL이 <br/>반환됩니다.": "If stream is not in the <br/>active configuration, <br/>-EINVAL is returned.", "카메라가 버퍼를 할당할 수 <br/>없는 상태이면 -EACCES가 <br/>반환됩니다.": "If the camera cannot <br/>allocate buffers in its <br/>state, -EACCES is returned.", "카메라가 버퍼를 할당할 수 <br/>있는 상태가 아니면 <br/>-EACCES가 반환됩니다.": "If the camera cannot <br/>allocate buffers in its <br/>current state, -EACCES is <br/>returned.", "카메라가 버퍼를 할당할 수 <br/>있는 상태인지 확인합니다.": "Check whether the camera is <br/>in a state where buffers <br/>can be allocated."}
  v_camera_precondition["allocate#40;#41;를 호출하기 전에 <br/>Camera는 <br/>Camera::configure#40;#41;로 <br/>설정되어 있어야 하며 정지해 <br/>있어야 합니다."]
  v_stream["stream은 활성 카메라 설정의 <br/>일부여야 합니다."]
  v_camera["카메라가 버퍼를 할당할 수 <br/>있는 상태인지 확인합니다."]
  v_eacces["카메라가 버퍼를 할당할 수 <br/>있는 상태가 아니면 <br/>-EACCES가 반환됩니다."]
  v_einval["stream이 카메라에 속하지 <br/>않거나 활성 설정의 일부가 <br/>아니면 -EINVAL이 반환됩니다."]
  v_camera_precondition -->|"stream은 활성 카메라 설정의 <br/>일부여야 합니다."| v_stream
  v_camera -->|"stream은 카메라에 속해야 <br/>합니다."| v_stream
  v_camera -->|"카메라가 버퍼를 할당할 수 <br/>없는 상태이면 -EACCES가 <br/>반환됩니다."| v_eacces
  v_stream -->|"stream이 카메라에 속하지 <br/>않으면 -EINVAL이 반환됩니다."| v_einval
  v_stream -->|"stream이 활성 카메라 설정의 <br/>일부가 아니면 -EINVAL이 <br/>반환됩니다."| v_einval
```

[Mermaid 원문](framebuffer-allocator.item-allocation-preconditions.mmd)

??? note "그림 근거와 확인 범위"
    allocate() 호출 전에 카메라와 스트림은 어떤 조건을 충족해야 하며, 어떤 조건에서 -EACCES와 -EINVAL이 반환되는가?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Before allocate(), Camera must have been configured with Camera::configure() and stopped.">allocate&#40;&#41;를 호출하기 전에 Camera는 Camera::configure&#40;&#41;로 설정되어 있어야 하며 정지해 있어야 합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:72](#source-4f32d036f2dee319) |
    | <span data-sdd-label-en="The stream must be part of the active camera configuration.">stream은 활성 카메라 설정의 일부여야 합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:72](#source-4f32d036f2dee319) |
    | <span data-sdd-label-en="Check whether the camera is in a state where buffers can be allocated.">카메라가 버퍼를 할당할 수 있는 상태인지 확인합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:81](#source-224d9d0ce4f1ad7f) |
    | <span data-sdd-label-en="If the camera cannot allocate buffers in its current state, -EACCES is returned.">카메라가 버퍼를 할당할 수 있는 상태가 아니면 -EACCES가 반환됩니다.</span> | [src/libcamera/framebuffer_allocator.cpp:81](#source-224d9d0ce4f1ad7f) |
    | <span data-sdd-label-en="If stream does not belong to the camera or its active configuration, -EINVAL is returned.">stream이 카메라에 속하지 않거나 활성 설정의 일부가 아니면 -EINVAL이 반환됩니다.</span> | [src/libcamera/framebuffer_allocator.cpp:81](#source-224d9d0ce4f1ad7f) |
    | <span data-sdd-label-en="The stream must be part of the active camera configuration.">stream은 활성 카메라 설정의 일부여야 합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:72](#source-4f32d036f2dee319) |
    | <span data-sdd-label-en="The stream must belong to the camera.">stream은 카메라에 속해야 합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:81](#source-224d9d0ce4f1ad7f) |
    | <span data-sdd-label-en="If the camera cannot allocate buffers in its state, -EACCES is returned.">카메라가 버퍼를 할당할 수 없는 상태이면 -EACCES가 반환됩니다.</span> | [src/libcamera/framebuffer_allocator.cpp:81](#source-224d9d0ce4f1ad7f) |
    | <span data-sdd-label-en="If stream does not belong to the camera, -EINVAL is returned.">stream이 카메라에 속하지 않으면 -EINVAL이 반환됩니다.</span> | [src/libcamera/framebuffer_allocator.cpp:81](#source-224d9d0ce4f1ad7f) |
    | <span data-sdd-label-en="If stream is not in the active configuration, -EINVAL is returned.">stream이 활성 카메라 설정의 일부가 아니면 -EINVAL이 반환됩니다.</span> | [src/libcamera/framebuffer_allocator.cpp:81](#source-224d9d0ce4f1ad7f) |
<!-- /sdd:visual:item-allocation-preconditions -->

근거 원문: [src/libcamera/framebuffer_allocator.cpp:72](#source-4f32d036f2dee319) · [src/libcamera/framebuffer_allocator.cpp:81](#source-224d9d0ce4f1ad7f)

## buffers 반환 참조의 유효기간

`buffers()`는 해당 스트림에 대해 `allocate()`로 버퍼를 성공적으로 할당한 후에만 호출해야 합니다. `buffers()`가 반환하는 버퍼는 같은 스트림에 대해 `free()`가 호출되거나 `FrameBufferAllocator` 인스턴스가 파괴될 때까지 유효합니다. `src/libcamera/framebuffer_allocator.cpp:141`, `src/libcamera/framebuffer_allocator.cpp:142`

<!-- sdd:visual:item-reference-lifetime -->
### buffers 반환 참조의 유효기간의 관계와 경계

```mermaid
flowchart TB
%% sdd:translations {"FrameBufferAllocator <br/>인스턴스의 파괴가 <br/>유효기간을 끝낼 수 있습니다.": "Destruction of the <br/>FrameBufferAllocator <br/>instance can end validity.", "FrameBufferAllocator <br/>인스턴스의 파괴는 <br/>유효기간을 끝내는 <br/>사건입니다.": "Destruction of the <br/>FrameBufferAllocator <br/>instance is an event that <br/>ends validity.", "allocate#40;#41;로 해당 stream의 <br/>버퍼를 성공적으로 <br/>할당합니다.": "Successfully allocate <br/>buffers for the stream with <br/>allocate#40;#41;.", "buffers#40;#41;는 해당 stream의 <br/>버퍼를 성공적으로 할당한 <br/>뒤에만 호출해야 합니다.": "Call buffers#40;#41; only after <br/>successfully allocating <br/>buffers for the stream.", "같은 stream에 대한 free#40;#41; <br/>호출은 유효기간을 끝내는 <br/>사건입니다.": "Calling free#40;#41; for the same <br/>stream is an event that <br/>ends validity.", "같은 stream에 대한 free#40;#41; <br/>호출이 유효기간을 끝낼 수 <br/>있습니다.": "Calling free#40;#41; for the same <br/>stream can end validity.", "반환된 버퍼는 아래 두 사건 <br/>중 먼저 발생하는 사건까지 <br/>유효합니다.": "Returned buffers are valid <br/>until the first of the two <br/>events below.", "성공적으로 할당한 뒤에만 <br/>buffers#40;#41;를 호출해야 합니다.": "Call buffers#40;#41; only after <br/>successful allocation."}
  v_allocate["allocate#40;#41;로 해당 stream의 <br/>버퍼를 성공적으로 <br/>할당합니다."]
  v_buffers["buffers#40;#41;는 해당 stream의 <br/>버퍼를 성공적으로 할당한 <br/>뒤에만 호출해야 합니다."]
  v_returned["반환된 버퍼는 아래 두 사건 <br/>중 먼저 발생하는 사건까지 <br/>유효합니다."]
  v_free["같은 stream에 대한 free#40;#41; <br/>호출은 유효기간을 끝내는 <br/>사건입니다."]
  v_allocator["FrameBufferAllocator <br/>인스턴스의 파괴는 <br/>유효기간을 끝내는 <br/>사건입니다."]
  v_allocate -->|"성공적으로 할당한 뒤에만 <br/>buffers#40;#41;를 호출해야 합니다."| v_buffers
  v_buffers -->|"반환된 버퍼는 아래 두 사건 <br/>중 먼저 발생하는 사건까지 <br/>유효합니다."| v_returned
  v_returned -->|"같은 stream에 대한 free#40;#41; <br/>호출이 유효기간을 끝낼 수 <br/>있습니다."| v_free
  v_returned -->|"FrameBufferAllocator <br/>인스턴스의 파괴가 <br/>유효기간을 끝낼 수 있습니다."| v_allocator
```

[Mermaid 원문](framebuffer-allocator.item-reference-lifetime.mmd)

??? note "그림 근거와 확인 범위"
    buffers()는 언제 호출할 수 있으며, 반환 버퍼의 유효기간은 어떤 사건으로 끝나는가?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Successfully allocate buffers for the stream with allocate().">allocate&#40;&#41;로 해당 stream의 버퍼를 성공적으로 할당합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:141](#source-68023250094ce1a8) |
    | <span data-sdd-label-en="Call buffers() only after successfully allocating buffers for the stream.">buffers&#40;&#41;는 해당 stream의 버퍼를 성공적으로 할당한 뒤에만 호출해야 합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:141](#source-68023250094ce1a8) |
    | <span data-sdd-label-en="Returned buffers are valid until the first of the two events below.">반환된 버퍼는 아래 두 사건 중 먼저 발생하는 사건까지 유효합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:142](#source-d60c5ad57e6699de) |
    | <span data-sdd-label-en="Calling free() for the same stream is an event that ends validity.">같은 stream에 대한 free&#40;&#41; 호출은 유효기간을 끝내는 사건입니다.</span> | [src/libcamera/framebuffer_allocator.cpp:142](#source-d60c5ad57e6699de) |
    | <span data-sdd-label-en="Destruction of the FrameBufferAllocator instance is an event that ends validity.">FrameBufferAllocator 인스턴스의 파괴는 유효기간을 끝내는 사건입니다.</span> | [src/libcamera/framebuffer_allocator.cpp:142](#source-d60c5ad57e6699de) |
    | <span data-sdd-label-en="Call buffers() only after successful allocation.">성공적으로 할당한 뒤에만 buffers&#40;&#41;를 호출해야 합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:141](#source-68023250094ce1a8) |
    | <span data-sdd-label-en="Returned buffers are valid until the first of the two events below.">반환된 버퍼는 아래 두 사건 중 먼저 발생하는 사건까지 유효합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:142](#source-d60c5ad57e6699de) |
    | <span data-sdd-label-en="Calling free() for the same stream can end validity.">같은 stream에 대한 free&#40;&#41; 호출이 유효기간을 끝낼 수 있습니다.</span> | [src/libcamera/framebuffer_allocator.cpp:142](#source-d60c5ad57e6699de) |
    | <span data-sdd-label-en="Destruction of the FrameBufferAllocator instance can end validity.">FrameBufferAllocator 인스턴스의 파괴가 유효기간을 끝낼 수 있습니다.</span> | [src/libcamera/framebuffer_allocator.cpp:142](#source-d60c5ad57e6699de) |
<!-- /sdd:visual:item-reference-lifetime -->

근거 원문: [src/libcamera/framebuffer_allocator.cpp:141](#source-68023250094ce1a8) · [src/libcamera/framebuffer_allocator.cpp:142](#source-d60c5ad57e6699de)

## 중복 할당과 내보내기 실패를 구분하기

`FrameBufferAllocator::allocate`는 `try_emplace`의 `inserted`가 false이면 버퍼가 이미 할당되었다는 오류를 기록하고 `-EBUSY`를 반환합니다. `FrameBufferAllocator::allocate()`는 `exportFrameBuffers()`의 반환값을 `ret`에 저장하고, `ret`가 음수이면 `buffers_.erase(it)`로 해당 `buffers_` 항목을 제거합니다. `FrameBufferAllocator::allocate`는 `exportFrameBuffers`를 호출한 경우 그 결과인 `ret`를 음수 여부와 관계없이 반환합니다. `src/libcamera/framebuffer_allocator.cpp:86`, `src/libcamera/framebuffer_allocator.cpp:95`

<!-- sdd:visual:item-allocation-failure -->
### 중복 할당과 내보내기 실패를 구분하기의 관계와 경계

```mermaid
flowchart TB
%% sdd:translations {"buffers#95;.try#95;emplace#40;stream#41;<br/>의 삽입 결과를 확인합니다.": "Check the insertion result <br/>of <br/>buffers#95;.try#95;emplace#40;stream#41;<br/>.", "ret이 구성 오류인지 <br/>확인합니다.": "Check ret for a <br/>configuration error.", "stream이 활성 구성에 속하지 <br/>않는다는 오류를 기록합니다.": "Log that stream is not part <br/>of the active configuration.", "구성 오류가 아니면 실패 <br/>여부를 확인합니다. #91;false#93;": "Otherwise, check for <br/>failure. #91;false#93;", "구성 오류이면 오류를 <br/>기록합니다. #91;true#93;": "If it is a configuration <br/>error, log it. #91;true#93;", "내보내기 결과 ret을 <br/>반환합니다.": "Return the export result <br/>ret.", "내보내기 결과가 실패인지 <br/>확인합니다.": "Check whether the export <br/>result indicates failure.", "내보내기 결과를 확인합니다.": "Check the export result.", "내보내기에 실패하면 새 <br/>buffers#95; 항목을 지웁니다.": "Erase the new buffers#95; <br/>entry when export fails.", "삽입되면 버퍼를 내보냅니다. <br/>#91;false#93;": "If insertion succeeds, <br/>export the buffers. #91;false#93;", "삽입되지 않으면 중복 <br/>할당으로 종료합니다. #91;true#93;": "If insertion fails, return <br/>for duplicate allocation. <br/>#91;true#93;", "새 항목에 버퍼를 내보내고 <br/>결과를 ret에 저장합니다.": "Export buffers to the new <br/>entry and save the result <br/>in ret.", "실패하면 항목을 지웁니다. <br/>#91;true#93;": "If export fails, erase the <br/>entry. #91;true#93;", "실패하지 않으면 항목을 <br/>지우지 않고 ret을 <br/>반환합니다. #91;false#93;": "Otherwise, return ret <br/>without erasing the entry. <br/>#91;false#93;", "오류를 기록한 뒤 실패 <br/>여부를 확인합니다.": "After logging, check for <br/>failure.", "중복 할당을 기록하고 <br/>-EBUSY를 반환합니다. 기존 <br/>buffers#95; 항목은 지우지 <br/>않습니다.": "Log the duplicate <br/>allocation and return <br/>-EBUSY; keep the existing <br/>buffers#95; entry.", "항목을 지운 뒤 ret을 <br/>반환합니다.": "After erasing the entry, <br/>return ret."}
  v_insert{"buffers#95;.try#95;emplace#40;stream#41;<br/>의 삽입 결과를 확인합니다."}
  v_busy["중복 할당을 기록하고 <br/>-EBUSY를 반환합니다. 기존 <br/>buffers#95; 항목은 지우지 <br/>않습니다."]
  v_export["새 항목에 버퍼를 내보내고 <br/>결과를 ret에 저장합니다."]
  v_invalid{"ret이 구성 오류인지 <br/>확인합니다."}
  v_log["stream이 활성 구성에 속하지 <br/>않는다는 오류를 기록합니다."]
  v_failure{"내보내기 결과가 실패인지 <br/>확인합니다."}
  v_erase["내보내기에 실패하면 새 <br/>buffers#95; 항목을 지웁니다."]
  v_result["내보내기 결과 ret을 <br/>반환합니다."]
  v_insert -->|"삽입되지 않으면 중복 <br/>할당으로 종료합니다. #91;true#93;"| v_busy
  v_insert -->|"삽입되면 버퍼를 내보냅니다. <br/>#91;false#93;"| v_export
  v_export -->|"내보내기 결과를 확인합니다."| v_invalid
  v_invalid -->|"구성 오류이면 오류를 <br/>기록합니다. #91;true#93;"| v_log
  v_invalid -->|"구성 오류가 아니면 실패 <br/>여부를 확인합니다. #91;false#93;"| v_failure
  v_log -->|"오류를 기록한 뒤 실패 <br/>여부를 확인합니다."| v_failure
  v_failure -->|"실패하면 항목을 지웁니다. <br/>#91;true#93;"| v_erase
  v_erase -->|"항목을 지운 뒤 ret을 <br/>반환합니다."| v_result
  v_failure -->|"실패하지 않으면 항목을 <br/>지우지 않고 ret을 <br/>반환합니다. #91;false#93;"| v_result
```

[Mermaid 원문](framebuffer-allocator.item-allocation-failure.mmd)

??? note "그림 근거와 확인 범위"
    중복 할당과 내보내기 실패는 처리 흐름, 반환값 및 buffers_ 항목 처리에서 어떻게 다른가?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Check the insertion result of buffers_.try_emplace(stream).">buffers&#95;.try&#95;emplace&#40;stream&#41;의 삽입 결과를 확인합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) |
    | <span data-sdd-label-en="Log the duplicate allocation and return -EBUSY; keep the existing buffers_ entry.">중복 할당을 기록하고 -EBUSY를 반환합니다. 기존 buffers&#95; 항목은 지우지 않습니다.</span> | [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) |
    | <span data-sdd-label-en="Export buffers to the new entry and save the result in ret.">새 항목에 버퍼를 내보내고 결과를 ret에 저장합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) |
    | <span data-sdd-label-en="Check ret for a configuration error.">ret이 구성 오류인지 확인합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) |
    | <span data-sdd-label-en="Log that stream is not part of the active configuration.">stream이 활성 구성에 속하지 않는다는 오류를 기록합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) |
    | <span data-sdd-label-en="Check whether the export result indicates failure.">내보내기 결과가 실패인지 확인합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) |
    | <span data-sdd-label-en="Erase the new buffers_ entry when export fails.">내보내기에 실패하면 새 buffers&#95; 항목을 지웁니다.</span> | [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) |
    | <span data-sdd-label-en="Return the export result ret.">내보내기 결과 ret을 반환합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) |
    | <span data-sdd-label-en="If insertion fails, return for duplicate allocation. · !inserted [true]">삽입되지 않으면 중복 할당으로 종료합니다. · &#33;inserted &#91;true&#93;</span> | [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) |
    | <span data-sdd-label-en="If insertion succeeds, export the buffers. · !inserted [false]">삽입되면 버퍼를 내보냅니다. · &#33;inserted &#91;false&#93;</span> | [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) |
    | <span data-sdd-label-en="Check the export result.">내보내기 결과를 확인합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) |
    | <span data-sdd-label-en="If it is a configuration error, log it. · ret == -EINVAL [true]">구성 오류이면 오류를 기록합니다. · ret == -EINVAL &#91;true&#93;</span> | [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) |
    | <span data-sdd-label-en="Otherwise, check for failure. · ret == -EINVAL [false]">구성 오류가 아니면 실패 여부를 확인합니다. · ret == -EINVAL &#91;false&#93;</span> | [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) |
    | <span data-sdd-label-en="After logging, check for failure.">오류를 기록한 뒤 실패 여부를 확인합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) |
    | <span data-sdd-label-en="If export fails, erase the entry. · ret &lt; 0 [true]">실패하면 항목을 지웁니다. · ret &lt; 0 &#91;true&#93;</span> | [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) |
    | <span data-sdd-label-en="After erasing the entry, return ret.">항목을 지운 뒤 ret을 반환합니다.</span> | [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) |
    | <span data-sdd-label-en="Otherwise, return ret without erasing the entry. · ret &lt; 0 [false]">실패하지 않으면 항목을 지우지 않고 ret을 반환합니다. · ret &lt; 0 &#91;false&#93;</span> | [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) |
<!-- /sdd:visual:item-allocation-failure -->

근거 원문: [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) · [src/libcamera/framebuffer_allocator.cpp:95](#source-c091763d679ea029)

## free의 스트림 조회와 반환값

`FrameBufferAllocator::free`는 스트림을 찾지 못하면 `-EINVAL`을 반환하며 `buffers_` 항목을 제거하지 않습니다. 스트림을 찾으면 해당 `buffers_` 항목을 제거하고 `0`을 반환합니다. `src/libcamera/framebuffer_allocator.cpp:119`

근거 원문: [src/libcamera/framebuffer_allocator.cpp:119](#source-fe0210ae47a5ebe2)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | allocate를 호출하기 위한 카메라·스트림 조건과 상태·스트림 오류의 원인은 무엇입니까? | [할당 전에 확인할 카메라 상태와 스트림](#할당-전에-확인할-카메라-상태와-스트림) | 코드 근거와 설명 연결 |
    | 중복 할당과 버퍼 내보내기 실패는 반환값과 할당 항목 처리에서 어떻게 다릅니까? | [중복 할당과 내보내기 실패를 구분하기](#중복-할당과-내보내기-실패를-구분하기) | 코드 근거와 설명 연결 |
    | free는 모르는 스트림과 등록된 스트림에 각각 무엇을 반환합니까? | [free의 스트림 조회와 반환값](#free의-스트림-조회와-반환값) | 코드 근거와 설명 연결 |
    | buffers를 호출할 수 있는 시점과 반환 참조의 유효기간은 무엇입니까? | [buffers 반환 참조의 유효기간](#buffers-반환-참조의-유효기간) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-4f32d036f2dee319"></a>

??? note "소스 근거: src/libcamera/framebuffer_allocator.cpp:72"
    `src/libcamera/framebuffer_allocator.cpp:72`에서 시작하는 발췌입니다. 종료 줄은 74이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `87ee819fc59da5231c8e99985771ae1821150196f2ed452822578208da94972f`
    
    ```text
    Allocate buffers suitable for capturing frames from the \a stream. The Camera
     * shall have been previously configured with Camera::configure() and shall be
     * stopped, and the stream shall be part of the active camera configuration.
    ```

<a id="source-224d9d0ce4f1ad7f"></a>

??? note "소스 근거: src/libcamera/framebuffer_allocator.cpp:81"
    `src/libcamera/framebuffer_allocator.cpp:81`에서 시작하는 발췌입니다. 종료 줄은 83이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `46d80bb2f91831ad0dda0a83fea0d3139ce6c0f156cf75033d97a9947cafde1e`
    
    ```text
    \retval -EACCES The camera is not in a state where buffers can be allocated
     * \retval -EINVAL The \a stream does not belong to the camera or the stream is
     * not part of the active camera configuration
    ```

<a id="source-68023250094ce1a8"></a>

??? note "소스 근거: src/libcamera/framebuffer_allocator.cpp:141"
    `src/libcamera/framebuffer_allocator.cpp:141`에서 시작하는 발췌입니다. 종료 줄은 142이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `a12056e800d2035f519dc58a4be3dc5e3c9d51920102cc9bc27c60a32790a663`
    
    ```text
    This function shall only be called after successfully allocating buffers for
     * \a stream with allocate().
    ```

<a id="source-d60c5ad57e6699de"></a>

??? note "소스 근거: src/libcamera/framebuffer_allocator.cpp:142"
    `src/libcamera/framebuffer_allocator.cpp:142`에서 시작하는 발췌입니다. 종료 줄은 143이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `7c43c6133e383a9e56e3a9163cfca05e8df576398f363e1b13bd5056664df86b`
    
    ```text
    The returned buffers are valid until free() is
     * called for the same stream or the FrameBufferAllocator instance is destroyed.
    ```

<a id="source-78a6c2f7dbdebb0f"></a>

??? note "소스 근거: src/libcamera/framebuffer_allocator.cpp:86"
    `src/libcamera/framebuffer_allocator.cpp:86`에서 시작하는 발췌입니다. 종료 줄은 105이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b`
    
    ```text
    int FrameBufferAllocator::allocate(Stream *stream)
    {
    	const auto &[it, inserted] = buffers_.try_emplace(stream);
    
    	if (!inserted) {
    		LOG(Allocator, Error) << "Buffers already allocated for stream";
    		return -EBUSY;
    	}
    
    	int ret = camera_->exportFrameBuffers(stream, &it->second);
    	if (ret == -EINVAL)
    		LOG(Allocator, Error)
    			<< "Stream is not part of " << camera_->id()
    			<< " active configuration";
    
    	if (ret < 0)
    		buffers_.erase(it);
    
    	return ret;
    }
    ```

<a id="source-c091763d679ea029"></a>

??? note "소스 근거: src/libcamera/framebuffer_allocator.cpp:95"
    `src/libcamera/framebuffer_allocator.cpp:95`에서 시작하는 발췌입니다. 종료 줄은 104이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `338a363feb53fd2928cc9b6d8a4d32dbfa921f4143079264e4264f9eae921b1e`
    
    ```text
    int ret = camera_->exportFrameBuffers(stream, &it->second);
    	if (ret == -EINVAL)
    		LOG(Allocator, Error)
    			<< "Stream is not part of " << camera_->id()
    			<< " active configuration";
    
    	if (ret < 0)
    		buffers_.erase(it);
    
    	return ret;
    ```

<a id="source-fe0210ae47a5ebe2"></a>

??? note "소스 근거: src/libcamera/framebuffer_allocator.cpp:119"
    `src/libcamera/framebuffer_allocator.cpp:119`에서 시작하는 발췌입니다. 종료 줄은 128이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `17715b15ff5a7663326b0ac1cd2248be6bf221eaa7551d1579901a1bb87ff6a6`
    
    ```text
    int FrameBufferAllocator::free(Stream *stream)
    {
    	auto iter = buffers_.find(stream);
    	if (iter == buffers_.end())
    		return -EINVAL;
    
    	buffers_.erase(iter);
    
    	return 0;
    }
    ```

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `src/libcamera/framebuffer_allocator.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `c19d05128f`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-12 · 사람 검토 전

다음 단계: [Camera·Request와 버퍼 참조의 책임](camera-model.md)
