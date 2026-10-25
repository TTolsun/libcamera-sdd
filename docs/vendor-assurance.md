---
generated_at: 2026-10-25T11:41:02+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: vendor-assurance
generation_method: facts-and-llm
evidence_fingerprint: c8823111054deef9525dc61d59f4e265824b48e0eff79eb809ee51ed65b847e0
semantic_review: human-review-required
agent: response-bundle/qwen3.5:9b
generated_design: {"schema": 1, "input_fingerprint": "c8823111054deef9525dc61d59f4e265824b48e0eff79eb809ee51ed65b847e0", "answers": {"constraints": [{"text": "`CameraConfiguration::Invalid` 은 설정이 유효하지 않아 조정할 수 없는 상태를 의미하며, 이는 설정이 비어 있는 것과 같은 극단적인 경우에만 발생할 수 있습니다.", "covers": ["constraints"], "kind": "behavior", "quote": "\\retval CameraConfiguration::Invalid The configuration is invalid and can't\n * be adjusted. This may only occur in extreme cases such as when the\n * configuration is empty.", "evidence": ["invalid"], "part_id": "invalid"}, {"text": "`CameraConfiguration::validate()` 함수는 구성이 조정되었음을 나타내는 `CameraConfiguration::Adjusted` 반환 값을 반환할 때, 해당 구성은 이미 조정되었으며 현재 유효한 상태임을 의미합니다.", "covers": ["constraints"], "kind": "behavior", "quote": "\\retval CameraConfiguration::Adjusted The configuration has been adjusted\n * and is now valid.", "evidence": ["adjusted-state"], "part_id": "adjusted"}, {"text": "`CameraConfiguration::validate()` 함수는 어떤 스트림의 파라미터가 변경되었을 수 있으며, 스트림 구성이 제거되었을 수도 있음을 명시합니다.", "covers": ["constraints"], "kind": "behavior", "quote": "Parameters may have changed for any stream, and stream\n * configurations may have been removed.", "evidence": ["adjusted-changes"], "part_id": "adjusted-changes"}, {"text": "`CameraConfiguration::validate()` 함수가 `CameraConfiguration::Adjusted`를 반환하면 호출자는 스트림 구성이 변경되었거나 제거되었을 수 있으므로 최종 설정을 신중하게 확인해야 합니다.", "covers": ["constraints"], "kind": "behavior", "quote": "\\retval CameraConfiguration::Adjusted The configuration has been adjusted\n * and is now valid. Parameters may have changed for any stream, and stream\n * configurations may have been removed. The caller shall check the\n * configuration carefully.", "evidence": ["adjusted"], "part_id": "adjusted-review"}, {"text": "`CameraConfiguration::validate()` 함수가 `CameraConfiguration::Valid` 상태를 반환하면, 이미 유효한 구성이므로 조정 없이 원래 구성 그대로 유지됩니다.", "covers": ["constraints"], "kind": "behavior", "quote": "\\fn CameraConfiguration::validate()\n * \\brief Validate and possibly adjust the camera configuration\n *\n * This function adjusts the camera configuration to the closest valid\n * configuration and returns the validation status.\n *\n * \\todo Define exactly when to return each status code. Should stream\n * parameters set to 0 by the caller be adjusted without returning Adjusted ?\n * This would potentially be useful for applications but would get in the way\n * in Camera::configure(). Do we need an extra status code to signal this ?\n *\n * \\todo Handle validation of buffers count when refactoring the buffers API.\n *\n * \\return A CameraConfiguration::Status value that describes the validation\n * status.\n * \\retval CameraConfiguration::Invalid The configuration is invalid and can't\n * be adjusted. This may only occur in extreme cases such as when the\n * configuration is empty.\n * \\retval CameraConfiguration::Adjusted The configuration has been adjusted\n * and is now valid. Parameters may have changed for any stream, and stream\n * configurations may have been removed. The caller shall check the\n * configuration carefully.\n * \\retval CameraConfiguration::Valid The configuration was already valid and\n * hasn't been adjusted.", "evidence": ["valid"], "part_id": "valid"}, {"text": "`PipelineHandler::generateConfiguration()` 함수는 요청된 역할 목록 (`roles`) 을 충족할 수 있으면 유효한 `CameraConfiguration` 객체를 반환하고, 그렇지 않으면 `nullptr`를 반환합니다.", "covers": ["constraints"], "kind": "behavior", "quote": "\\return A valid CameraConfiguration if the requested roles can be satisfied,\n * or a null pointer otherwise.", "evidence": ["generate-result"], "part_id": "roles"}, {"text": "`PipelineHandler::configure()` 함수는 `CameraConfiguration::validate()` 를 통해 검증된 구성만 받으며, 구현자는 추가 검증을 수행해서는 안 됩니다.", "covers": ["constraints"], "kind": "behavior", "quote": "The configuration is guaranteed to have been validated with\n * CameraConfiguration::validate(). The pipeline handler implementation shall\n * not perform further validation", "evidence": ["configure-input"], "part_id": "configure-input"}, {"text": "`PipelineHandler::configure()` 함수는 호출이 성공하면 `0`을 반환하고, 실패하거나 오류가 발생하면 음수 값의 오류 코드를 반환해야 합니다.", "covers": ["constraints"], "kind": "behavior", "quote": "\\context This function is called from the CameraManager thread.\n *\n * \\return 0 on success or a negative error code otherwise", "evidence": ["configure-result"], "part_id": "configure"}], "measurement": [{"text": "`DebayerCpu` 클래스에 내장된 벤치마크는 프레임 캡처나 출력에 소요되는 시간을 측정하지 않고, 통계 수집과 디베이어 처리에만 소요되는 시간만 측정합니다.", "covers": ["measurement"], "kind": "behavior", "quote": "The DebayerCpu class has a builtin benchmark. This benchmark measures the time\nspent on processing (collecting statistics and debayering) only, it does not\nmeasure the time spent on capturing or outputting the frames.", "evidence": ["benchmark"], "part_id": "scope"}, {"text": "`Software ISP` 파이프라인을 사용하는 `cam` 또는 `qcam` 명령어를 실행하면 내장 벤치마크가 자동으로 실행됩니다.", "covers": ["measurement"], "kind": "behavior", "quote": "The builtin benchmark always runs. So this can be used by simply running \"cam\"\nor \"qcam\" with a pipeline using the Software ISP.", "evidence": ["benchmark"], "part_id": "procedure"}]}, "topic_inputs": {"constraints": "f9833a5420183f7e0b8a0c2ca0b4ed444651fc8b8dcda04d2318d17dd6cb770a", "measurement": "09f854bcc832a7fb0311fd450d7c25fc78d980ab2effbb5f83377de23cf14f49"}, "reused_topics": [], "generated_topics": ["constraints", "measurement"], "topic_agents": {"constraints": "response-bundle/qwen3.5:9b", "measurement": "response-bundle/qwen3.5:9b"}, "body_sha256": "9effda582327d4b8e80cd0765b22b6efec102502027cbb8ea75aa3dc045cdc3d"}
generated_visuals: {"schema": 1, "records": {"validation-results": {"input_fingerprint": "2bad6d67544260c197f1c44a198bc616abf9efff6252ea3625ec6ea3026dc6fb", "draft": {"nodes": {"n0": {"label": "CameraConfiguration::validate 가 상태를 반환합니다", "label_en": "CameraConfiguration::validate returns a status", "shape": "box", "quote_ids": ["valid:0"]}, "n1": {"label": "Invalid: 구성이 유효하지 않아 조정 불가 (극단적 경우)", "label_en": "Invalid: configuration invalid and can't be adjusted (extreme case)", "shape": "decision", "quote_ids": ["valid:1"]}, "n2": {"label": "Adjusted: 파라미터 변경·스트림 삭제 가능, 호출자는 신중히 재확인해야 함", "label_en": "Adjusted: parameters may have changed or streams removed; caller shall check carefully", "shape": "box", "quote_ids": ["valid:2"]}, "n3": {"label": "Valid: 이미 유효하여 조정 불필요", "label_en": "Valid: configuration was already valid and hasn't been adjusted", "shape": "box", "quote_ids": ["valid:3"]}}, "edges": [{"from": "n0", "to": "n1", "label": "유효하지 않아 조정 불가", "label_en": "invalid and can't be adjusted", "condition_ref": "always", "quote_ids": ["valid:1"]}, {"from": "n0", "to": "n2", "label": "조정됨, 파라미터 변경 또는 스트림 삭제 가능, 호출자가 확인해야 함", "label_en": "adjusted and now valid; parameters may have changed or streams removed; caller shall check", "condition_ref": "always", "quote_ids": ["valid:2"]}, {"from": "n0", "to": "n3", "label": "이미 유효하여 조정 불필요", "label_en": "already valid and hasn't been adjusted", "condition_ref": "always", "quote_ids": ["valid:3"]}]}, "graph": {"id": "validation-results", "topic": "constraints", "kind": "decision", "title": "validate() 결과별 호출자의 책임", "question": "validate()의 Invalid·Adjusted·Valid는 무엇을 뜻하며, Adjusted이면 호출자는 무엇을 다시 확인해야 합니까?", "nodes": [{"id": "n0", "label": "CameraConfiguration::validate 가 상태를 반환합니다", "label_en": "CameraConfiguration::validate returns a status", "shape": "box", "evidence": [{"source": "constraints/valid", "sha256": "86bf9109257512866bf70a5d42cd3da29c70d851d871f0e496058141ba377623", "quote": "\\fn CameraConfiguration::validate()\n * \\brief Validate and possibly adjust the camera configuration\n *\n * This function adjusts the camera configuration to the closest valid\n * configuration and returns the validation status.\n *\n * \\todo Define exactly when to return each status code. Should stream\n * parameters set to 0 by the caller be adjusted without returning Adjusted ?\n * This would potentially be useful for applications but would get in the way\n * in Camera::configure(). Do we need an extra status code to signal this ?\n *\n * \\todo Handle validation of buffers count when refactoring the buffers API.\n *\n * \\return A CameraConfiguration::Status value that describes the validation\n * status."}]}, {"id": "n1", "label": "Invalid: 구성이 유효하지 않아 조정 불가 (극단적 경우)", "label_en": "Invalid: configuration invalid and can't be adjusted (extreme case)", "shape": "decision", "evidence": [{"source": "constraints/valid", "sha256": "86bf9109257512866bf70a5d42cd3da29c70d851d871f0e496058141ba377623", "quote": "\\fn CameraConfiguration::validate()\n * \\brief Validate and possibly adjust the camera configuration\n *\n * This function adjusts the camera configuration to the closest valid\n * configuration and returns the validation status.\n *\n * \\todo Define exactly when to return each status code. Should stream\n * parameters set to 0 by the caller be adjusted without returning Adjusted ?\n * This would potentially be useful for applications but would get in the way\n * in Camera::configure(). Do we need an extra status code to signal this ?\n *\n * \\todo Handle validation of buffers count when refactoring the buffers API.\n *\n * \\return A CameraConfiguration::Status value that describes the validation\n * status.\n * \\retval CameraConfiguration::Invalid The configuration is invalid and can't\n * be adjusted. This may only occur in extreme cases such as when the\n * configuration is empty."}]}, {"id": "n2", "label": "Adjusted: 파라미터 변경·스트림 삭제 가능, 호출자는 신중히 재확인해야 함", "label_en": "Adjusted: parameters may have changed or streams removed; caller shall check carefully", "shape": "box", "evidence": [{"source": "constraints/valid", "sha256": "86bf9109257512866bf70a5d42cd3da29c70d851d871f0e496058141ba377623", "quote": "\\fn CameraConfiguration::validate()\n * \\brief Validate and possibly adjust the camera configuration\n *\n * This function adjusts the camera configuration to the closest valid\n * configuration and returns the validation status.\n *\n * \\todo Define exactly when to return each status code. Should stream\n * parameters set to 0 by the caller be adjusted without returning Adjusted ?\n * This would potentially be useful for applications but would get in the way\n * in Camera::configure(). Do we need an extra status code to signal this ?\n *\n * \\todo Handle validation of buffers count when refactoring the buffers API.\n *\n * \\return A CameraConfiguration::Status value that describes the validation\n * status.\n * \\retval CameraConfiguration::Invalid The configuration is invalid and can't\n * be adjusted. This may only occur in extreme cases such as when the\n * configuration is empty.\n * \\retval CameraConfiguration::Adjusted The configuration has been adjusted\n * and is now valid. Parameters may have changed for any stream, and stream\n * configurations may have been removed. The caller shall check the\n * configuration carefully."}]}, {"id": "n3", "label": "Valid: 이미 유효하여 조정 불필요", "label_en": "Valid: configuration was already valid and hasn't been adjusted", "shape": "box", "evidence": [{"source": "constraints/valid", "sha256": "86bf9109257512866bf70a5d42cd3da29c70d851d871f0e496058141ba377623", "quote": "\\fn CameraConfiguration::validate()\n * \\brief Validate and possibly adjust the camera configuration\n *\n * This function adjusts the camera configuration to the closest valid\n * configuration and returns the validation status.\n *\n * \\todo Define exactly when to return each status code. Should stream\n * parameters set to 0 by the caller be adjusted without returning Adjusted ?\n * This would potentially be useful for applications but would get in the way\n * in Camera::configure(). Do we need an extra status code to signal this ?\n *\n * \\todo Handle validation of buffers count when refactoring the buffers API.\n *\n * \\return A CameraConfiguration::Status value that describes the validation\n * status.\n * \\retval CameraConfiguration::Invalid The configuration is invalid and can't\n * be adjusted. This may only occur in extreme cases such as when the\n * configuration is empty.\n * \\retval CameraConfiguration::Adjusted The configuration has been adjusted\n * and is now valid. Parameters may have changed for any stream, and stream\n * configurations may have been removed. The caller shall check the\n * configuration carefully.\n * \\retval CameraConfiguration::Valid The configuration was already valid and\n * hasn't been adjusted."}]}], "edges": [{"from": "n0", "to": "n1", "label": "유효하지 않아 조정 불가", "label_en": "invalid and can't be adjusted", "evidence": [{"source": "constraints/valid", "sha256": "86bf9109257512866bf70a5d42cd3da29c70d851d871f0e496058141ba377623", "quote": "\\fn CameraConfiguration::validate()\n * \\brief Validate and possibly adjust the camera configuration\n *\n * This function adjusts the camera configuration to the closest valid\n * configuration and returns the validation status.\n *\n * \\todo Define exactly when to return each status code. Should stream\n * parameters set to 0 by the caller be adjusted without returning Adjusted ?\n * This would potentially be useful for applications but would get in the way\n * in Camera::configure(). Do we need an extra status code to signal this ?\n *\n * \\todo Handle validation of buffers count when refactoring the buffers API.\n *\n * \\return A CameraConfiguration::Status value that describes the validation\n * status.\n * \\retval CameraConfiguration::Invalid The configuration is invalid and can't\n * be adjusted. This may only occur in extreme cases such as when the\n * configuration is empty."}]}, {"from": "n0", "to": "n2", "label": "조정됨, 파라미터 변경 또는 스트림 삭제 가능, 호출자가 확인해야 함", "label_en": "adjusted and now valid; parameters may have changed or streams removed; caller shall check", "evidence": [{"source": "constraints/valid", "sha256": "86bf9109257512866bf70a5d42cd3da29c70d851d871f0e496058141ba377623", "quote": "\\fn CameraConfiguration::validate()\n * \\brief Validate and possibly adjust the camera configuration\n *\n * This function adjusts the camera configuration to the closest valid\n * configuration and returns the validation status.\n *\n * \\todo Define exactly when to return each status code. Should stream\n * parameters set to 0 by the caller be adjusted without returning Adjusted ?\n * This would potentially be useful for applications but would get in the way\n * in Camera::configure(). Do we need an extra status code to signal this ?\n *\n * \\todo Handle validation of buffers count when refactoring the buffers API.\n *\n * \\return A CameraConfiguration::Status value that describes the validation\n * status.\n * \\retval CameraConfiguration::Invalid The configuration is invalid and can't\n * be adjusted. This may only occur in extreme cases such as when the\n * configuration is empty.\n * \\retval CameraConfiguration::Adjusted The configuration has been adjusted\n * and is now valid. Parameters may have changed for any stream, and stream\n * configurations may have been removed. The caller shall check the\n * configuration carefully."}]}, {"from": "n0", "to": "n3", "label": "이미 유효하여 조정 불필요", "label_en": "already valid and hasn't been adjusted", "evidence": [{"source": "constraints/valid", "sha256": "86bf9109257512866bf70a5d42cd3da29c70d851d871f0e496058141ba377623", "quote": "\\fn CameraConfiguration::validate()\n * \\brief Validate and possibly adjust the camera configuration\n *\n * This function adjusts the camera configuration to the closest valid\n * configuration and returns the validation status.\n *\n * \\todo Define exactly when to return each status code. Should stream\n * parameters set to 0 by the caller be adjusted without returning Adjusted ?\n * This would potentially be useful for applications but would get in the way\n * in Camera::configure(). Do we need an extra status code to signal this ?\n *\n * \\todo Handle validation of buffers count when refactoring the buffers API.\n *\n * \\return A CameraConfiguration::Status value that describes the validation\n * status.\n * \\retval CameraConfiguration::Invalid The configuration is invalid and can't\n * be adjusted. This may only occur in extreme cases such as when the\n * configuration is empty.\n * \\retval CameraConfiguration::Adjusted The configuration has been adjusted\n * and is now valid. Parameters may have changed for any stream, and stream\n * configurations may have been removed. The caller shall check the\n * configuration carefully.\n * \\retval CameraConfiguration::Valid The configuration was already valid and\n * hasn't been adjusted."}]}], "producer": "response-bundle/qwen3.5:9b"}, "producer": "response-bundle/qwen3.5:9b", "generation_commit": "2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f", "reused": false}}, "body_sha256": "9effda582327d4b8e80cd0765b22b6efec102502027cbb8ea75aa3dc045cdc3d"}
---

# 지원 범위와 검증

**지원 조건과 구성 제약을 확인하고 제품 도입 전에 검증할 범위를 정하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| libcamera 제품 개요에서 필요한 내용을 확인합니다. | [libcamera 제품 개요](vendor-overview.md) |
| 연동 가이드에서 필요한 내용을 확인합니다. | [연동 가이드](vendor-integration.md) |
| 장치별 파이프라인을 구현합니다. | [Pipeline Handler](pipeline-handler.md) |

## 지원 조건과 제약

`CameraConfiguration::Invalid` 은 설정이 유효하지 않아 조정할 수 없는 상태를 의미하며, 이는 설정이 비어 있는 것과 같은 극단적인 경우에만 발생할 수 있습니다. `src/libcamera/camera.cpp:338`

<!-- sdd:visual:validation-results -->
### validate() 결과별 호출자의 책임

validate()의 Invalid·Adjusted·Valid는 무엇을 뜻하며, Adjusted이면 호출자는 무엇을 다시 확인해야 합니까?

LLM 그림 초안 · 사람 검토 전

작성 모델: `response-bundle/qwen3.5:9b`

```mermaid
flowchart TB
%% sdd:translations {"Adjusted: 파라미터 <br/>변경·스트림 삭제 가능, <br/>호출자는 신중히 재확인해야 <br/>함": "Adjusted: parameters may <br/>have changed or streams <br/>removed; caller shall check <br/>carefully", "CameraConfiguration::validat<br/>e 가 상태를 반환합니다": "CameraConfiguration::validat<br/>e returns a status", "Invalid: 구성이 유효하지 <br/>않아 조정 불가 (극단적 경우)": "Invalid: configuration <br/>invalid and can&#x27;t be <br/>adjusted (extreme case)", "Valid: 이미 유효하여 조정 <br/>불필요": "Valid: configuration was <br/>already valid and hasn&#x27;t <br/>been adjusted", "유효하지 않아 조정 불가": "invalid and can&#x27;t be <br/>adjusted", "이미 유효하여 조정 불필요": "already valid and hasn&#x27;t <br/>been adjusted", "조정됨, 파라미터 변경 또는 <br/>스트림 삭제 가능, 호출자가 <br/>확인해야 함": "adjusted and now valid; <br/>parameters may have changed <br/>or streams removed; caller <br/>shall check"}
  v_n0["CameraConfiguration::validat<br/>e 가 상태를 반환합니다"]
  v_n1{"Invalid: 구성이 유효하지 <br/>않아 조정 불가 (극단적 경우)"}
  v_n2["Adjusted: 파라미터 <br/>변경·스트림 삭제 가능, <br/>호출자는 신중히 재확인해야 <br/>함"]
  v_n3["Valid: 이미 유효하여 조정 <br/>불필요"]
  v_n0 -->|"유효하지 않아 조정 불가"| v_n1
  v_n0 -->|"조정됨, 파라미터 변경 또는 <br/>스트림 삭제 가능, 호출자가 <br/>확인해야 함"| v_n2
  v_n0 -->|"이미 유효하여 조정 불필요"| v_n3
```

[Mermaid 원문](vendor-assurance.validation-results.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | CameraConfiguration::validate 가 상태를 반환합니다 | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
    | Invalid: 구성이 유효하지 않아 조정 불가 (극단적 경우) | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
    | Adjusted: 파라미터 변경·스트림 삭제 가능, 호출자는 신중히 재확인해야 함 | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
    | Valid: 이미 유효하여 조정 불필요 | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
    | 유효하지 않아 조정 불가 | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
    | 조정됨, 파라미터 변경 또는 스트림 삭제 가능, 호출자가 확인해야 함 | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
    | 이미 유효하여 조정 불필요 | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
<!-- /sdd:visual:validation-results -->

`CameraConfiguration::validate()` 함수는 구성이 조정되었음을 나타내는 `CameraConfiguration::Adjusted` 반환 값을 반환할 때, 해당 구성은 이미 조정되었으며 현재 유효한 상태임을 의미합니다. `src/libcamera/camera.cpp:341`

`CameraConfiguration::validate()` 함수는 어떤 스트림의 파라미터가 변경되었을 수 있으며, 스트림 구성이 제거되었을 수도 있음을 명시합니다. `src/libcamera/camera.cpp:342`

`CameraConfiguration::validate()` 함수가 `CameraConfiguration::Adjusted`를 반환하면 호출자는 스트림 구성이 변경되었거나 제거되었을 수 있으므로 최종 설정을 신중하게 확인해야 합니다. `src/libcamera/camera.cpp:341`

`CameraConfiguration::validate()` 함수가 `CameraConfiguration::Valid` 상태를 반환하면, 이미 유효한 구성이므로 조정 없이 원래 구성 그대로 유지됩니다. `src/libcamera/camera.cpp:323`

`PipelineHandler::generateConfiguration()` 함수는 요청된 역할 목록 (`roles`) 을 충족할 수 있으면 유효한 `CameraConfiguration` 객체를 반환하고, 그렇지 않으면 `nullptr`를 반환합니다. `src/libcamera/pipeline_handler.cpp:289`

`PipelineHandler::configure()` 함수는 `CameraConfiguration::validate()` 를 통해 검증된 구성만 받으며, 구현자는 추가 검증을 수행해서는 안 됩니다. `src/libcamera/pipeline_handler.cpp:304`

`PipelineHandler::configure()` 함수는 호출이 성공하면 `0`을 반환하고, 실패하거나 오류가 발생하면 음수 값의 오류 코드를 반환해야 합니다. `src/libcamera/pipeline_handler.cpp:313`

근거 원문: [src/libcamera/camera.cpp:338](#source-60ab47044c6107c5) · [src/libcamera/camera.cpp:341](#source-c14b4403062d5e35) · [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) · [src/libcamera/pipeline_handler.cpp:289](#source-4abbe39594a1bd27) · [src/libcamera/pipeline_handler.cpp:304](#source-31c5407347b4d0d8) · [src/libcamera/pipeline_handler.cpp:313](#source-f87ceb096b9f931d) · [src/libcamera/camera.cpp:341](#source-8b6aa81367245db5) · [src/libcamera/camera.cpp:342](#source-e13fede0aa40ada1)

## 성능 근거를 읽는 기준

`DebayerCpu` 클래스에 내장된 벤치마크는 프레임 캡처나 출력에 소요되는 시간을 측정하지 않고, 통계 수집과 디베이어 처리에만 소요되는 시간만 측정합니다. `Documentation/software-isp-benchmarking.rst:15`

`Software ISP` 파이프라인을 사용하는 `cam` 또는 `qcam` 명령어를 실행하면 내장 벤치마크가 자동으로 실행됩니다. `Documentation/software-isp-benchmarking.rst:15`

근거 원문: [Documentation/software-isp-benchmarking.rst:15](#source-551d2b5944a36d19)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 지원 전제와 제약은 무엇이며 별도 검증할 항목은 무엇입니까? | [지원 조건과 제약](#지원-조건과-제약) | 코드 근거와 설명 연결 |
    | 참고 벤치마크가 측정하는 범위와 별도 제품 검증 범위는 무엇입니까? | [성능 근거를 읽는 기준](#성능-근거를-읽는-기준) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-60ab47044c6107c5"></a>

??? note "소스 근거: src/libcamera/camera.cpp:338"
    `src/libcamera/camera.cpp:338`에서 시작하는 발췌입니다. 종료 줄은 340이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `2247db4a7b9353362f9df6c84aaa5c2810dec4eaaae4b3b36d19c57e427f5790`
    
    ```text
    \retval CameraConfiguration::Invalid The configuration is invalid and can't
     * be adjusted. This may only occur in extreme cases such as when the
     * configuration is empty.
    ```

<a id="source-c14b4403062d5e35"></a>

??? note "소스 근거: src/libcamera/camera.cpp:341"
    `src/libcamera/camera.cpp:341`에서 시작하는 발췌입니다. 종료 줄은 344이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `1305054b4a0655a883d0cef7398ff34824da06ecdbac0dfbf1f06de218bb6ebc`
    
    ```text
    \retval CameraConfiguration::Adjusted The configuration has been adjusted
     * and is now valid. Parameters may have changed for any stream, and stream
     * configurations may have been removed. The caller shall check the
     * configuration carefully.
    ```

<a id="source-2b31e92e3fb3f083"></a>

??? note "소스 근거: src/libcamera/camera.cpp:323"
    `src/libcamera/camera.cpp:323`에서 시작하는 발췌입니다. 종료 줄은 346이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `86bf9109257512866bf70a5d42cd3da29c70d851d871f0e496058141ba377623`
    
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
    ```

<a id="source-4abbe39594a1bd27"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:289"
    `src/libcamera/pipeline_handler.cpp:289`에서 시작하는 발췌입니다. 종료 줄은 290이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `b86c8678b02e96936d80626cefebf3811b6a991b459074e51c9f0e08457ff369`
    
    ```text
    \return A valid CameraConfiguration if the requested roles can be satisfied,
     * or a null pointer otherwise.
    ```

<a id="source-31c5407347b4d0d8"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:304"
    `src/libcamera/pipeline_handler.cpp:304`에서 시작하는 발췌입니다. 종료 줄은 306이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `625bd787da81f9407ba9e746d4939d93b7172a26642429bcfd3300aa6187675f`
    
    ```text
    The configuration is guaranteed to have been validated with
     * CameraConfiguration::validate(). The pipeline handler implementation shall
     * not perform further validation
    ```

<a id="source-f87ceb096b9f931d"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:313"
    `src/libcamera/pipeline_handler.cpp:313`에서 시작하는 발췌입니다. 종료 줄은 315이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `6e139b3c50660a7111d84bd00cfd17078b8b45d4a07688fa64b2d8af9ce52a22`
    
    ```text
    \context This function is called from the CameraManager thread.
     *
     * \return 0 on success or a negative error code otherwise
    ```

<a id="source-8b6aa81367245db5"></a>

??? note "소스 근거: src/libcamera/camera.cpp:341"
    `src/libcamera/camera.cpp:341`에서 시작하는 발췌입니다. 종료 줄은 342이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `bc530fdf77cefda77bfd8ae1cadf7df4edea81ddfce01bef24867681b29655f6`
    
    ```text
    \retval CameraConfiguration::Adjusted The configuration has been adjusted
     * and is now valid.
    ```

<a id="source-e13fede0aa40ada1"></a>

??? note "소스 근거: src/libcamera/camera.cpp:342"
    `src/libcamera/camera.cpp:342`에서 시작하는 발췌입니다. 종료 줄은 343이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `7c0debb896b6072c0bc59cf3589fbc49b607f915d96f30182d4e02038b94c156`
    
    ```text
    Parameters may have changed for any stream, and stream
     * configurations may have been removed.
    ```

<a id="source-551d2b5944a36d19"></a>

??? note "소스 근거: Documentation/software-isp-benchmarking.rst:15"
    `Documentation/software-isp-benchmarking.rst:15`에서 시작하는 발췌입니다. 종료 줄은 20이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `907d979f60258b4572a0557b6054ec814990084ca3e69a291317855a3b27084d`
    
    ```text
    The DebayerCpu class has a builtin benchmark. This benchmark measures the time
    spent on processing (collecting statistics and debayering) only, it does not
    measure the time spent on capturing or outputting the frames.
    
    The builtin benchmark always runs. So this can be used by simply running "cam"
    or "qcam" with a pipeline using the Software ISP.
    ```


<!-- sdd:class-diagram -->
## 클래스 관계

화살표의 글자는 추출한 관계를 나타내며, 점선은 상속입니다. 화살표는 참조 대상 또는 기반 클래스를 향합니다. 호출 순서를 뜻하지 않습니다.

```mermaid
flowchart LR
  c0["Camera"]
  c1["Extensible"]:::context
  c2["IPAManager"]
  c3["Object"]:::context
  c4["PipelineHandler"]
  c5["PipelineHandlerIPU3"]
  c6["PipelineHandlerRkISP1"]
  c0 -.->|상속| c1
  c0 -.->|상속| c3
  c4 -->|필드 참조| c0
  c4 -.->|상속| c3
  c5 -.->|상속| c4
  c6 -->|필드 참조| c0
  c6 -.->|상속| c4
  classDef context fill:#fafafa,stroke:#aaa,stroke-dasharray:4 3,color:#555
```
<!-- /sdd:class-diagram -->

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `Documentation/software-isp-benchmarking.rst`, `include/libcamera/camera.h`, `include/libcamera/internal/ipa_manager.h`, `include/libcamera/internal/pipeline_handler.h`, `src/libcamera/camera.cpp`, `src/libcamera/ipa_manager.cpp`, `src/libcamera/pipeline/ipu3/ipu3.cpp`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp`, `src/libcamera/pipeline_handler.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `2c4b67c079`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-25 · 사람 검토 전

다음 단계: [요청 처리와 문제 진단](request-lifecycle.md)
