---
generated_at: 2026-11-04 20:05:26+00:00
source_commit: da6a6ed33ed0ab305f10b6f8b44736150d39cef4
status: ok
section: vendor-assurance
generation_method: facts-and-llm
evidence_fingerprint: d806346a28f8875ebaaa267c2e6496124770532213291fbbe56b387ccbfda232
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design:
  schema: 1
  input_fingerprint: d806346a28f8875ebaaa267c2e6496124770532213291fbbe56b387ccbfda232
  answers:
    constraints:
    - text: '`CameraConfiguration::Invalid`는 구성이 유효하지 않고 조정할 수 없음을 뜻하며, 구성이 비어 있는
        경우와 같은 극단적인 경우에만 발생할 수 있습니다.'
      evidence:
      - invalid
      covers:
      - constraints
      kind: behavior
      quote: "\\retval CameraConfiguration::Invalid The configuration is invalid and\
        \ can't\n * be adjusted. This may only occur in extreme cases such as when\
        \ the\n * configuration is empty."
      part_id: invalid
    - text: '`CameraConfiguration::Adjusted`는 구성이 조정되었으며 조정 후 유효함을 나타냅니다.'
      evidence:
      - adjusted-state
      covers:
      - constraints
      kind: behavior
      quote: "\\retval CameraConfiguration::Adjusted The configuration has been adjusted\n\
        \ * and is now valid."
      part_id: adjusted
    - text: '`CameraConfiguration::validate()`가 `CameraConfiguration::Adjusted`를 반환한
        경우 어느 스트림의 파라미터든 바뀌었을 수 있고 일부 스트림만 바뀌었을 수도 있으며, 스트림 구성이 삭제되었을 수도 있습니다.'
      evidence:
      - adjusted-changes
      covers:
      - constraints
      kind: behavior
      quote: "Parameters may have changed for any stream, and stream\n * configurations\
        \ may have been removed."
      part_id: adjusted-changes
    - text: '`CameraConfiguration::Adjusted`일 때 호출자는 구성을 주의 깊게 확인해야 합니다.'
      evidence:
      - adjusted
      covers:
      - constraints
      kind: behavior
      quote: "The caller shall check the\n * configuration carefully."
      part_id: adjusted-review
    - text: '`CameraConfiguration::validate()`가 `CameraConfiguration::Valid`를 반환하면
        원래 구성이 이미 유효했고 조정되지 않았음을 뜻합니다.'
      evidence:
      - valid
      covers:
      - constraints
      kind: behavior
      quote: "\\fn CameraConfiguration::validate()\n * \\brief Validate and possibly\
        \ adjust the camera configuration\n *\n * This function adjusts the camera\
        \ configuration to the closest valid\n * configuration and returns the validation\
        \ status.\n *\n * \\todo Define exactly when to return each status code. Should\
        \ stream\n * parameters set to 0 by the caller be adjusted without returning\
        \ Adjusted ?\n * This would potentially be useful for applications but would\
        \ get in the way\n * in Camera::configure(). Do we need an extra status code\
        \ to signal this ?\n *\n * \\todo Handle validation of buffers count when\
        \ refactoring the buffers API.\n *\n * \\return A CameraConfiguration::Status\
        \ value that describes the validation\n * status.\n * \\retval CameraConfiguration::Invalid\
        \ The configuration is invalid and can't\n * be adjusted. This may only occur\
        \ in extreme cases such as when the\n * configuration is empty.\n * \\retval\
        \ CameraConfiguration::Adjusted The configuration has been adjusted\n * and\
        \ is now valid. Parameters may have changed for any stream, and stream\n *\
        \ configurations may have been removed. The caller shall check the\n * configuration\
        \ carefully.\n * \\retval CameraConfiguration::Valid The configuration was\
        \ already valid and\n * hasn't been adjusted."
      part_id: valid
    - text: '`PipelineHandler::generateConfiguration()`은 `roles`로 요청한 스트림 역할을 충족할
        수 있으면 유효한 `CameraConfiguration`을 반환하고, 충족할 수 없으면 `null` 포인터를 반환합니다.'
      evidence:
      - generate-contract
      covers:
      - constraints
      kind: behavior
      quote: "\\fn PipelineHandler::generateConfiguration()\n * \\brief Generate a\
        \ camera configuration for a specified camera\n * \\param[in] camera The camera\
        \ to generate a default configuration for\n * \\param[in] roles A list of\
        \ stream roles\n *\n * Generate a default configuration for the \\a camera\
        \ for a specified list of\n * stream roles. The caller shall populate the\
        \ \\a roles with the use-cases it\n * wishes to fetch the default configuration\
        \ for. The returned configuration\n * can then be examined by the caller to\
        \ learn about the selected streams and\n * their default parameters.\n *\n\
        \ * The intended companion to this is \\a configure() which can be used to\
        \ change\n * the group of streams parameters.\n *\n * \\context This function\
        \ may be called from any thread and shall be\n * \\threadsafe. It shall not\
        \ modify the state of the \\a camera in the pipeline\n * handler.\n *\n *\
        \ \\return A valid CameraConfiguration if the requested roles can be satisfied,\n\
        \ * or a null pointer otherwise.\n */"
      part_id: roles
    - text: '`PipelineHandler::configure()`에 전달되는 설정은 `CameraConfiguration::validate()`로
        검증되어 있음이 보장되므로, 파이프라인 핸들러 구현자는 추가 검증을 해서는 안 됩니다.'
      evidence:
      - configure-input
      covers:
      - constraints
      kind: behavior
      quote: "The configuration is guaranteed to have been validated with\n * CameraConfiguration::validate().\
        \ The pipeline handler implementation shall\n * not perform further validation"
      part_id: configure-input
    - text: '`PipelineHandler::configure()` 구현자는 구성에 성공하면 `0`을, 실패하면 음수 오류 코드를 반환해야
        합니다.'
      evidence:
      - configure-result
      covers:
      - constraints
      kind: behavior
      quote: "\\context This function is called from the CameraManager thread.\n *\n\
        \ * \\return 0 on success or a negative error code otherwise"
      part_id: configure
    measurement:
    - text: '`DebayerCpu`의 내장 벤치마크는 통계를 수집하고 디베이어링하는 처리에 걸린 시간만 측정합니다. 프레임 캡처와 출력에
        걸린 시간은 측정하지 않습니다.'
      evidence:
      - benchmark
      covers:
      - measurement
      kind: behavior
      quote: 'The DebayerCpu class has a builtin benchmark. This benchmark measures
        the time

        spent on processing (collecting statistics and debayering) only, it does not

        measure the time spent on capturing or outputting the frames.'
      part_id: scope
    - text: 이 벤치마크는 `Software ISP`를 사용하는 파이프라인에서 `cam` 또는 `qcam`을 실행하여 사용할 수 있습니다.
      evidence:
      - benchmark
      covers:
      - measurement
      kind: behavior
      quote: 'The builtin benchmark always runs. So this can be used by simply running
        "cam"

        or "qcam" with a pipeline using the Software ISP.'
      part_id: procedure
  topic_inputs:
    constraints: 5f18adc276274a1a5691814a3dcbc343b5ed0789d3cb34f0b00c26c05f0e28f9
    measurement: 18d9f7dba85d7406538f64676d2c51c931060db239437e683bbe7c44830786ec
  reused_topics:
  - constraints
  - measurement
  replayed_units: []
  generated_topics: []
  topic_agents:
    constraints: cli/codex/gpt-6.1-terra
    measurement: cli/codex/gpt-6.1-terra
  grounding_review: passed
  grounding_policy: 3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2
  validation_policy:
    manuscript: 367d18b95f8f0d01a15ae0f4d1b70f7e13e4d0298df4215e2c449ac4905db6f9
    semantic: 571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968
    duplicates: 93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38
    design_contracts: 9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0
    validate: 78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372
    reader_profiles: ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797
    contract_schema: 2f593eec0430a4e6b5822e642c0a7a1227fc150a0b27d8a71f521acf93b6439e
    answer_contracts: 1e0d24e0cf26ded53ecec2e5a6fbc51836bac6e17530318a9fa7cffaa936c00b
    reader_scope: 1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782
    product_context: 050c20aa2fdcceae10c6275fbb5f850f616ab5051bb67ccbcb4a204877a238d9
    design_response: deb70dda7ad27f001267e4a9712c5b0dc1fe9fa67acd13bedbfefaaad0ad83c8
    design_validation: 946deebb694018f6361ee86669e1a7a26cd61dfffef11bb3a7de0a193639fabe
  validation_model: 094be2ee160010ee5486f46e7ff820935534721e3f4a94f5bcd191773985f4a9
  style_policy:
    fluent-korean.md: ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975
    i-have-adhd.md: 3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9
    README.md: b87a84b1bc31079837dc4dc4527ce02c9dc2cbc3a26ff7e99e0872941d213995
  reuse_lineage:
    source_commit: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61
    body_sha256: 686f8d51e7e4d66d86d6155c7ea29e72ae0ce4cca554db6b8d9e8e83a6568244
    topics:
    - constraints
    - measurement
    validation: current source, contract and editorial checks; human review pending
  body_sha256: 968aeae7dc836bca4bcf7be0ab78dc57acbcb5855a057c7ec7c2e5677a780978
generated_visuals:
  schema: 1
  records:
    validation-results:
      input_fingerprint: 4e9a42607d66f617348778f5f219613687f595214265eda1100a0dfe51278949
      draft:
        nodes:
          n0:
            label: CameraConfiguration::validate는 카메라 구성을 검증하고 필요하면 가장 가까운 유효한 구성으로
              조정한 뒤 검증 상태를 반환합니다.
            label_en: CameraConfiguration::validate validates the camera configuration,
              may adjust it to the closest valid configuration, and returns the validation
              status.
            shape: process
            quote_ids:
            - valid:0
          n1:
            label: Invalid는 구성이 유효하지 않고 조정할 수도 없다는 뜻입니다. 빈 구성처럼 극단적인 경우에만 발생할 수 있습니다.
            label_en: Invalid means the configuration is invalid and cannot be adjusted.
              It may occur only in extreme cases, such as an empty configuration.
            shape: box
            quote_ids:
            - valid:1
          n2:
            label: Adjusted는 구성을 조정해 유효해졌다는 뜻입니다. 어느 스트림의 파라미터든 변경되었을 가능성이 있고, 스트림
              구성이 삭제되었을 가능성도 있으므로 호출자는 구성을 주의 깊게 확인해야 합니다.
            label_en: Adjusted means the configuration was adjusted and is now valid.
              Parameters for any stream may have changed, and stream configurations
              may have been removed, so the caller must carefully check the configuration.
            shape: box
            quote_ids:
            - valid:2
          n3:
            label: Valid는 구성이 이미 유효했고 조정되지 않았다는 뜻입니다.
            label_en: Valid means the configuration was already valid and was not
              adjusted.
            shape: box
            quote_ids:
            - valid:3
        edges:
        - from: n0
          to: n1
          label: 검증 상태로 Invalid를 반환할 수 있습니다.
          label_en: It may return Invalid as the validation status.
          condition_ref: always
          quote_ids:
          - valid:1
        - from: n0
          to: n2
          label: 검증 상태로 Adjusted를 반환할 수 있습니다.
          label_en: It may return Adjusted as the validation status.
          condition_ref: always
          quote_ids:
          - valid:2
        - from: n0
          to: n3
          label: 검증 상태로 Valid를 반환할 수 있습니다.
          label_en: It may return Valid as the validation status.
          condition_ref: always
          quote_ids:
          - valid:3
      graph:
        id: validation-results
        topic: constraints
        kind: decision
        title: validate() 결과별 호출자의 책임
        question: validate()의 Invalid·Adjusted·Valid는 무엇을 뜻하며, Adjusted이면 호출자는 무엇을
          다시 확인해야 합니까?
        nodes:
        - id: n0
          label: CameraConfiguration::validate는 카메라 구성을 검증하고 필요하면 가장 가까운 유효한 구성으로
            조정한 뒤 검증 상태를 반환합니다.
          label_en: CameraConfiguration::validate validates the camera configuration,
            may adjust it to the closest valid configuration, and returns the validation
            status.
          shape: box
          evidence:
          - source: constraints/valid
            sha256: 86bf9109257512866bf70a5d42cd3da29c70d851d871f0e496058141ba377623
            quote: "\\fn CameraConfiguration::validate()\n * \\brief Validate and\
              \ possibly adjust the camera configuration\n *\n * This function adjusts\
              \ the camera configuration to the closest valid\n * configuration and\
              \ returns the validation status.\n *\n * \\todo Define exactly when\
              \ to return each status code. Should stream\n * parameters set to 0\
              \ by the caller be adjusted without returning Adjusted ?\n * This would\
              \ potentially be useful for applications but would get in the way\n\
              \ * in Camera::configure(). Do we need an extra status code to signal\
              \ this ?\n *\n * \\todo Handle validation of buffers count when refactoring\
              \ the buffers API.\n *\n * \\return A CameraConfiguration::Status value\
              \ that describes the validation\n * status."
        - id: n1
          label: Invalid는 구성이 유효하지 않고 조정할 수도 없다는 뜻입니다. 빈 구성처럼 극단적인 경우에만 발생할 수 있습니다.
          label_en: Invalid means the configuration is invalid and cannot be adjusted.
            It may occur only in extreme cases, such as an empty configuration.
          shape: box
          evidence:
          - source: constraints/valid
            sha256: 86bf9109257512866bf70a5d42cd3da29c70d851d871f0e496058141ba377623
            quote: "\\fn CameraConfiguration::validate()\n * \\brief Validate and\
              \ possibly adjust the camera configuration\n *\n * This function adjusts\
              \ the camera configuration to the closest valid\n * configuration and\
              \ returns the validation status.\n *\n * \\todo Define exactly when\
              \ to return each status code. Should stream\n * parameters set to 0\
              \ by the caller be adjusted without returning Adjusted ?\n * This would\
              \ potentially be useful for applications but would get in the way\n\
              \ * in Camera::configure(). Do we need an extra status code to signal\
              \ this ?\n *\n * \\todo Handle validation of buffers count when refactoring\
              \ the buffers API.\n *\n * \\return A CameraConfiguration::Status value\
              \ that describes the validation\n * status.\n * \\retval CameraConfiguration::Invalid\
              \ The configuration is invalid and can't\n * be adjusted. This may only\
              \ occur in extreme cases such as when the\n * configuration is empty."
        - id: n2
          label: Adjusted는 구성을 조정해 유효해졌다는 뜻입니다. 어느 스트림의 파라미터든 변경되었을 가능성이 있고, 스트림 구성이
            삭제되었을 가능성도 있으므로 호출자는 구성을 주의 깊게 확인해야 합니다.
          label_en: Adjusted means the configuration was adjusted and is now valid.
            Parameters for any stream may have changed, and stream configurations
            may have been removed, so the caller must carefully check the configuration.
          shape: box
          evidence:
          - source: constraints/valid
            sha256: 86bf9109257512866bf70a5d42cd3da29c70d851d871f0e496058141ba377623
            quote: "\\fn CameraConfiguration::validate()\n * \\brief Validate and\
              \ possibly adjust the camera configuration\n *\n * This function adjusts\
              \ the camera configuration to the closest valid\n * configuration and\
              \ returns the validation status.\n *\n * \\todo Define exactly when\
              \ to return each status code. Should stream\n * parameters set to 0\
              \ by the caller be adjusted without returning Adjusted ?\n * This would\
              \ potentially be useful for applications but would get in the way\n\
              \ * in Camera::configure(). Do we need an extra status code to signal\
              \ this ?\n *\n * \\todo Handle validation of buffers count when refactoring\
              \ the buffers API.\n *\n * \\return A CameraConfiguration::Status value\
              \ that describes the validation\n * status.\n * \\retval CameraConfiguration::Invalid\
              \ The configuration is invalid and can't\n * be adjusted. This may only\
              \ occur in extreme cases such as when the\n * configuration is empty.\n\
              \ * \\retval CameraConfiguration::Adjusted The configuration has been\
              \ adjusted\n * and is now valid. Parameters may have changed for any\
              \ stream, and stream\n * configurations may have been removed. The caller\
              \ shall check the\n * configuration carefully."
        - id: n3
          label: Valid는 구성이 이미 유효했고 조정되지 않았다는 뜻입니다.
          label_en: Valid means the configuration was already valid and was not adjusted.
          shape: box
          evidence:
          - source: constraints/valid
            sha256: 86bf9109257512866bf70a5d42cd3da29c70d851d871f0e496058141ba377623
            quote: "\\fn CameraConfiguration::validate()\n * \\brief Validate and\
              \ possibly adjust the camera configuration\n *\n * This function adjusts\
              \ the camera configuration to the closest valid\n * configuration and\
              \ returns the validation status.\n *\n * \\todo Define exactly when\
              \ to return each status code. Should stream\n * parameters set to 0\
              \ by the caller be adjusted without returning Adjusted ?\n * This would\
              \ potentially be useful for applications but would get in the way\n\
              \ * in Camera::configure(). Do we need an extra status code to signal\
              \ this ?\n *\n * \\todo Handle validation of buffers count when refactoring\
              \ the buffers API.\n *\n * \\return A CameraConfiguration::Status value\
              \ that describes the validation\n * status.\n * \\retval CameraConfiguration::Invalid\
              \ The configuration is invalid and can't\n * be adjusted. This may only\
              \ occur in extreme cases such as when the\n * configuration is empty.\n\
              \ * \\retval CameraConfiguration::Adjusted The configuration has been\
              \ adjusted\n * and is now valid. Parameters may have changed for any\
              \ stream, and stream\n * configurations may have been removed. The caller\
              \ shall check the\n * configuration carefully.\n * \\retval CameraConfiguration::Valid\
              \ The configuration was already valid and\n * hasn't been adjusted."
        edges:
        - from: n0
          to: n1
          label: 검증 상태로 Invalid를 반환할 수 있습니다.
          label_en: It may return Invalid as the validation status.
          evidence:
          - source: constraints/valid
            sha256: 86bf9109257512866bf70a5d42cd3da29c70d851d871f0e496058141ba377623
            quote: "\\fn CameraConfiguration::validate()\n * \\brief Validate and\
              \ possibly adjust the camera configuration\n *\n * This function adjusts\
              \ the camera configuration to the closest valid\n * configuration and\
              \ returns the validation status.\n *\n * \\todo Define exactly when\
              \ to return each status code. Should stream\n * parameters set to 0\
              \ by the caller be adjusted without returning Adjusted ?\n * This would\
              \ potentially be useful for applications but would get in the way\n\
              \ * in Camera::configure(). Do we need an extra status code to signal\
              \ this ?\n *\n * \\todo Handle validation of buffers count when refactoring\
              \ the buffers API.\n *\n * \\return A CameraConfiguration::Status value\
              \ that describes the validation\n * status.\n * \\retval CameraConfiguration::Invalid\
              \ The configuration is invalid and can't\n * be adjusted. This may only\
              \ occur in extreme cases such as when the\n * configuration is empty."
        - from: n0
          to: n2
          label: 검증 상태로 Adjusted를 반환할 수 있습니다.
          label_en: It may return Adjusted as the validation status.
          evidence:
          - source: constraints/valid
            sha256: 86bf9109257512866bf70a5d42cd3da29c70d851d871f0e496058141ba377623
            quote: "\\fn CameraConfiguration::validate()\n * \\brief Validate and\
              \ possibly adjust the camera configuration\n *\n * This function adjusts\
              \ the camera configuration to the closest valid\n * configuration and\
              \ returns the validation status.\n *\n * \\todo Define exactly when\
              \ to return each status code. Should stream\n * parameters set to 0\
              \ by the caller be adjusted without returning Adjusted ?\n * This would\
              \ potentially be useful for applications but would get in the way\n\
              \ * in Camera::configure(). Do we need an extra status code to signal\
              \ this ?\n *\n * \\todo Handle validation of buffers count when refactoring\
              \ the buffers API.\n *\n * \\return A CameraConfiguration::Status value\
              \ that describes the validation\n * status.\n * \\retval CameraConfiguration::Invalid\
              \ The configuration is invalid and can't\n * be adjusted. This may only\
              \ occur in extreme cases such as when the\n * configuration is empty.\n\
              \ * \\retval CameraConfiguration::Adjusted The configuration has been\
              \ adjusted\n * and is now valid. Parameters may have changed for any\
              \ stream, and stream\n * configurations may have been removed. The caller\
              \ shall check the\n * configuration carefully."
        - from: n0
          to: n3
          label: 검증 상태로 Valid를 반환할 수 있습니다.
          label_en: It may return Valid as the validation status.
          evidence:
          - source: constraints/valid
            sha256: 86bf9109257512866bf70a5d42cd3da29c70d851d871f0e496058141ba377623
            quote: "\\fn CameraConfiguration::validate()\n * \\brief Validate and\
              \ possibly adjust the camera configuration\n *\n * This function adjusts\
              \ the camera configuration to the closest valid\n * configuration and\
              \ returns the validation status.\n *\n * \\todo Define exactly when\
              \ to return each status code. Should stream\n * parameters set to 0\
              \ by the caller be adjusted without returning Adjusted ?\n * This would\
              \ potentially be useful for applications but would get in the way\n\
              \ * in Camera::configure(). Do we need an extra status code to signal\
              \ this ?\n *\n * \\todo Handle validation of buffers count when refactoring\
              \ the buffers API.\n *\n * \\return A CameraConfiguration::Status value\
              \ that describes the validation\n * status.\n * \\retval CameraConfiguration::Invalid\
              \ The configuration is invalid and can't\n * be adjusted. This may only\
              \ occur in extreme cases such as when the\n * configuration is empty.\n\
              \ * \\retval CameraConfiguration::Adjusted The configuration has been\
              \ adjusted\n * and is now valid. Parameters may have changed for any\
              \ stream, and stream\n * configurations may have been removed. The caller\
              \ shall check the\n * configuration carefully.\n * \\retval CameraConfiguration::Valid\
              \ The configuration was already valid and\n * hasn't been adjusted."
        producer: cli/codex/gpt-6.1-terra
      producer: cli/codex/gpt-6.1-terra
      generation_commit: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61
      citation_binding_policy: identifier-boundaries-v1
      reused: true
      citation_binding_revalidation:
        policy: identifier-and-guard-boundaries-v2
        original_input_fingerprint: 4e9a42607d66f617348778f5f219613687f595214265eda1100a0dfe51278949
        new_inference: false
    configuration-contract-validity:
      input_fingerprint: 96232a874f0e49506eced7c4e4d7ab0b03a8dd252807b3f1ddd01d0942095c61
      draft:
        nodes:
        - id: request
          symbol: PipelineHandler::generateConfiguration
          label: 호출자는 기본 구성을 얻으려는 용도로 roles를 채워야 하며, PipelineHandler::generateConfiguration은
            해당 카메라의 기본 구성 생성을 요청받습니다.
          label_en: The caller must populate roles with the intended use cases; PipelineHandler::generateConfiguration
            is asked to generate a default configuration for the camera.
          shape: process
          quote_ids:
          - generate-contract:0
        - id: valid
          symbol: CameraConfiguration
          label: 요청한 roles를 만족할 수 있으면 유효한 CameraConfiguration을 반환합니다.
          label_en: If the requested roles can be satisfied, it returns a valid CameraConfiguration.
          shape: box
          quote_ids:
          - generate-contract:0
        - id: 'null'
          symbol: 'null'
          label: 요청한 roles를 만족할 수 없으면 null 포인터를 반환합니다.
          label_en: If the requested roles cannot be satisfied, it returns a null
            pointer.
          shape: box
          quote_ids:
          - generate-contract:0
        edges:
        - from: request
          to: valid
          label: 요청한 roles를 만족할 수 있으면 반환합니다.
          label_en: It returns this if the requested roles can be satisfied.
          condition_ref: always
          quote_ids:
          - generate-contract:0
        - from: request
          to: 'null'
          label: 요청한 roles를 만족할 수 없으면 반환합니다.
          label_en: It returns this if the requested roles cannot be satisfied.
          condition_ref: always
          quote_ids:
          - generate-contract:0
      graph:
        id: configuration-contract-validity
        topic: constraints
        kind: flow
        title: 역할 기반 구성 생성의 반환 계약
        question: PipelineHandler::generateConfiguration은 요청한 roles를 만족할 수 있을 때와 없을
          때 무엇을 반환합니까?
        condition_display: inline
        nodes:
        - id: request
          label: 호출자는 기본 구성을 얻으려는 용도로 roles를 채워야 하며, PipelineHandler::generateConfiguration은
            해당 카메라의 기본 구성 생성을 요청받습니다.
          label_en: The caller must populate roles with the intended use cases; PipelineHandler::generateConfiguration
            is asked to generate a default configuration for the camera.
          shape: box
          evidence:
          - source: constraints/generate-contract
            sha256: c1f4cc7aeedfc57e2bc5ebd6825a77f605173b44f7fde564aebc01bb013119cf
            quote: "\\fn PipelineHandler::generateConfiguration()\n * \\brief Generate\
              \ a camera configuration for a specified camera\n * \\param[in] camera\
              \ The camera to generate a default configuration for\n * \\param[in]\
              \ roles A list of stream roles\n *\n * Generate a default configuration\
              \ for the \\a camera for a specified list of\n * stream roles. The caller\
              \ shall populate the \\a roles with the use-cases it\n * wishes to fetch\
              \ the default configuration for. The returned configuration\n * can\
              \ then be examined by the caller to learn about the selected streams\
              \ and\n * their default parameters.\n *\n * The intended companion to\
              \ this is \\a configure() which can be used to change\n * the group\
              \ of streams parameters.\n *\n * \\context This function may be called\
              \ from any thread and shall be\n * \\threadsafe. It shall not modify\
              \ the state of the \\a camera in the pipeline\n * handler.\n *\n * \\\
              return A valid CameraConfiguration if the requested roles can be satisfied,\n\
              \ * or a null pointer otherwise.\n */"
        - id: valid
          label: 요청한 roles를 만족할 수 있으면 유효한 CameraConfiguration을 반환합니다.
          label_en: If the requested roles can be satisfied, it returns a valid CameraConfiguration.
          shape: box
          evidence:
          - source: constraints/generate-contract
            sha256: c1f4cc7aeedfc57e2bc5ebd6825a77f605173b44f7fde564aebc01bb013119cf
            quote: "\\fn PipelineHandler::generateConfiguration()\n * \\brief Generate\
              \ a camera configuration for a specified camera\n * \\param[in] camera\
              \ The camera to generate a default configuration for\n * \\param[in]\
              \ roles A list of stream roles\n *\n * Generate a default configuration\
              \ for the \\a camera for a specified list of\n * stream roles. The caller\
              \ shall populate the \\a roles with the use-cases it\n * wishes to fetch\
              \ the default configuration for. The returned configuration\n * can\
              \ then be examined by the caller to learn about the selected streams\
              \ and\n * their default parameters.\n *\n * The intended companion to\
              \ this is \\a configure() which can be used to change\n * the group\
              \ of streams parameters.\n *\n * \\context This function may be called\
              \ from any thread and shall be\n * \\threadsafe. It shall not modify\
              \ the state of the \\a camera in the pipeline\n * handler.\n *\n * \\\
              return A valid CameraConfiguration if the requested roles can be satisfied,\n\
              \ * or a null pointer otherwise.\n */"
        - id: 'null'
          label: 요청한 roles를 만족할 수 없으면 null 포인터를 반환합니다.
          label_en: If the requested roles cannot be satisfied, it returns a null
            pointer.
          shape: box
          evidence:
          - source: constraints/generate-contract
            sha256: c1f4cc7aeedfc57e2bc5ebd6825a77f605173b44f7fde564aebc01bb013119cf
            quote: "\\fn PipelineHandler::generateConfiguration()\n * \\brief Generate\
              \ a camera configuration for a specified camera\n * \\param[in] camera\
              \ The camera to generate a default configuration for\n * \\param[in]\
              \ roles A list of stream roles\n *\n * Generate a default configuration\
              \ for the \\a camera for a specified list of\n * stream roles. The caller\
              \ shall populate the \\a roles with the use-cases it\n * wishes to fetch\
              \ the default configuration for. The returned configuration\n * can\
              \ then be examined by the caller to learn about the selected streams\
              \ and\n * their default parameters.\n *\n * The intended companion to\
              \ this is \\a configure() which can be used to change\n * the group\
              \ of streams parameters.\n *\n * \\context This function may be called\
              \ from any thread and shall be\n * \\threadsafe. It shall not modify\
              \ the state of the \\a camera in the pipeline\n * handler.\n *\n * \\\
              return A valid CameraConfiguration if the requested roles can be satisfied,\n\
              \ * or a null pointer otherwise.\n */"
        edges:
        - from: request
          to: valid
          label: 요청한 roles를 만족할 수 있으면 반환합니다.
          label_en: It returns this if the requested roles can be satisfied.
          evidence:
          - source: constraints/generate-contract
            sha256: c1f4cc7aeedfc57e2bc5ebd6825a77f605173b44f7fde564aebc01bb013119cf
            quote: "\\fn PipelineHandler::generateConfiguration()\n * \\brief Generate\
              \ a camera configuration for a specified camera\n * \\param[in] camera\
              \ The camera to generate a default configuration for\n * \\param[in]\
              \ roles A list of stream roles\n *\n * Generate a default configuration\
              \ for the \\a camera for a specified list of\n * stream roles. The caller\
              \ shall populate the \\a roles with the use-cases it\n * wishes to fetch\
              \ the default configuration for. The returned configuration\n * can\
              \ then be examined by the caller to learn about the selected streams\
              \ and\n * their default parameters.\n *\n * The intended companion to\
              \ this is \\a configure() which can be used to change\n * the group\
              \ of streams parameters.\n *\n * \\context This function may be called\
              \ from any thread and shall be\n * \\threadsafe. It shall not modify\
              \ the state of the \\a camera in the pipeline\n * handler.\n *\n * \\\
              return A valid CameraConfiguration if the requested roles can be satisfied,\n\
              \ * or a null pointer otherwise.\n */"
        - from: request
          to: 'null'
          label: 요청한 roles를 만족할 수 없으면 반환합니다.
          label_en: It returns this if the requested roles cannot be satisfied.
          evidence:
          - source: constraints/generate-contract
            sha256: c1f4cc7aeedfc57e2bc5ebd6825a77f605173b44f7fde564aebc01bb013119cf
            quote: "\\fn PipelineHandler::generateConfiguration()\n * \\brief Generate\
              \ a camera configuration for a specified camera\n * \\param[in] camera\
              \ The camera to generate a default configuration for\n * \\param[in]\
              \ roles A list of stream roles\n *\n * Generate a default configuration\
              \ for the \\a camera for a specified list of\n * stream roles. The caller\
              \ shall populate the \\a roles with the use-cases it\n * wishes to fetch\
              \ the default configuration for. The returned configuration\n * can\
              \ then be examined by the caller to learn about the selected streams\
              \ and\n * their default parameters.\n *\n * The intended companion to\
              \ this is \\a configure() which can be used to change\n * the group\
              \ of streams parameters.\n *\n * \\context This function may be called\
              \ from any thread and shall be\n * \\threadsafe. It shall not modify\
              \ the state of the \\a camera in the pipeline\n * handler.\n *\n * \\\
              return A valid CameraConfiguration if the requested roles can be satisfied,\n\
              \ * or a null pointer otherwise.\n */"
        producer: cli/codex/gpt-6.1-terra
      producer: cli/codex/gpt-6.1-terra
      generation_commit: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61
      citation_binding_policy: identifier-boundaries-v1
      reused: true
      citation_binding_revalidation:
        policy: identifier-and-guard-boundaries-v2
        original_input_fingerprint: 96232a874f0e49506eced7c4e4d7ab0b03a8dd252807b3f1ddd01d0942095c61
        new_inference: false
  body_sha256: 968aeae7dc836bca4bcf7be0ab78dc57acbcb5855a057c7ec7c2e5677a780978
revalidated_from: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
---

# 지원 범위와 검증

**지원 조건과 구성 제약을 확인하고 제품 도입 전에 검증할 범위를 정하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 제품이 무엇이고 어디까지 지원하는지, 공통 설계가 구현자에게 해 주는 일을 확인하고 도입할 범위를 판단하세요. | [libcamera 제품 개요](vendor-overview.md) |
| 연동 순서와 구현 책임을 확인하고 설정·요청·정지 계약을 적용하세요. | [연동 가이드](vendor-integration.md) |
| 파이프라인 구현이 지켜야 하는 구성·요청·완료·종료 계약을 확인하세요. | [Pipeline Handler](pipeline-handler.md) |

## 지원 조건과 제약

`CameraConfiguration::Invalid`는 구성이 유효하지 않고 조정할 수 없음을 뜻하며, 구성이 비어 있는 경우와 같은 극단적인 경우에만 발생할 수 있습니다. `CameraConfiguration::Adjusted`는 구성이 조정되었으며 조정 후 유효함을 나타냅니다. `CameraConfiguration::validate()`가 `CameraConfiguration::Adjusted`를 반환한 경우 어느 스트림의 파라미터든 바뀌었을 수 있고 일부 스트림만 바뀌었을 수도 있으며, 스트림 구성이 삭제되었을 수도 있습니다. `CameraConfiguration::Adjusted`일 때 호출자는 구성을 주의 깊게 확인해야 합니다. `src/libcamera/camera.cpp:338`, `src/libcamera/camera.cpp:341`, `src/libcamera/camera.cpp:342`, `src/libcamera/camera.cpp:343`

<!-- sdd:visual:validation-results -->
### validate() 결과별 호출자의 책임

```mermaid
flowchart TB
%% sdd:translations {"Adjusted는 구성을 조정해 <br/>유효해졌다는 뜻입니다. 어느 <br/>스트림의 파라미터든 <br/>변경되었을 가능성이 있고, <br/>스트림 구성이 삭제되었을 <br/>가능성도 있으므로 호출자는 <br/>구성을 주의 깊게 확인해야 <br/>합니다.": "Adjusted means the <br/>configuration was adjusted <br/>and is now valid. <br/>Parameters for any stream <br/>may have changed, and <br/>stream configurations may <br/>have been removed, so the <br/>caller must carefully check <br/>the configuration.", "CameraConfiguration::<br/>validate는 카메라 구성을 <br/>검증하고 필요하면 가장 <br/>가까운 유효한 구성으로 <br/>조정한 뒤 검증 상태를 <br/>반환합니다.": "CameraConfiguration::<br/>validate validates the <br/>camera configuration, may <br/>adjust it to the closest <br/>valid configuration, and <br/>returns the validation <br/>status.", "Invalid는 구성이 유효하지 <br/>않고 조정할 수도 없다는 <br/>뜻입니다. 빈 구성처럼 <br/>극단적인 경우에만 발생할 수 <br/>있습니다.": "Invalid means the <br/>configuration is invalid <br/>and cannot be adjusted. It <br/>may occur only in extreme <br/>cases, such as an empty <br/>configuration.", "Valid는 구성이 이미 <br/>유효했고 조정되지 않았다는 <br/>뜻입니다.": "Valid means the <br/>configuration was already <br/>valid and was not adjusted.", "검증 상태로 Adjusted를 <br/>반환할 수 있습니다.": "It may return Adjusted as <br/>the validation status.", "검증 상태로 Invalid를 <br/>반환할 수 있습니다.": "It may return Invalid as <br/>the validation status.", "검증 상태로 Valid를 반환할 <br/>수 있습니다.": "It may return Valid as the <br/>validation status."}
  v_n0["CameraConfiguration::<br/>validate는 카메라 구성을 <br/>검증하고 필요하면 가장 <br/>가까운 유효한 구성으로 <br/>조정한 뒤 검증 상태를 <br/>반환합니다."]
  v_n1["Invalid는 구성이 유효하지 <br/>않고 조정할 수도 없다는 <br/>뜻입니다. 빈 구성처럼 <br/>극단적인 경우에만 발생할 수 <br/>있습니다."]
  v_n2["Adjusted는 구성을 조정해 <br/>유효해졌다는 뜻입니다. 어느 <br/>스트림의 파라미터든 <br/>변경되었을 가능성이 있고, <br/>스트림 구성이 삭제되었을 <br/>가능성도 있으므로 호출자는 <br/>구성을 주의 깊게 확인해야 <br/>합니다."]
  v_n3["Valid는 구성이 이미 <br/>유효했고 조정되지 않았다는 <br/>뜻입니다."]
  v_n0 -->|"검증 상태로 Invalid를 <br/>반환할 수 있습니다."| v_n1
  v_n0 -->|"검증 상태로 Adjusted를 <br/>반환할 수 있습니다."| v_n2
  v_n0 -->|"검증 상태로 Valid를 반환할 <br/>수 있습니다."| v_n3
```

[Mermaid 원문](vendor-assurance.validation-results.mmd)

??? note "그림 근거와 확인 범위"
    validate()의 Invalid·Adjusted·Valid는 무엇을 뜻하며, Adjusted이면 호출자는 무엇을 다시 확인해야 합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="CameraConfiguration::validate validates the camera configuration, may adjust it to the closest valid configuration, and returns the validation status.">CameraConfiguration::validate는 카메라 구성을 검증하고 필요하면 가장 가까운 유효한 구성으로 조정한 뒤 검증 상태를 반환합니다.</span> | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
    | <span data-sdd-label-en="Invalid means the configuration is invalid and cannot be adjusted. It may occur only in extreme cases, such as an empty configuration.">Invalid는 구성이 유효하지 않고 조정할 수도 없다는 뜻입니다. 빈 구성처럼 극단적인 경우에만 발생할 수 있습니다.</span> | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
    | <span data-sdd-label-en="Adjusted means the configuration was adjusted and is now valid. Parameters for any stream may have changed, and stream configurations may have been removed, so the caller must carefully check the configuration.">Adjusted는 구성을 조정해 유효해졌다는 뜻입니다. 어느 스트림의 파라미터든 변경되었을 가능성이 있고, 스트림 구성이 삭제되었을 가능성도 있으므로 호출자는 구성을 주의 깊게 확인해야 합니다.</span> | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
    | <span data-sdd-label-en="Valid means the configuration was already valid and was not adjusted.">Valid는 구성이 이미 유효했고 조정되지 않았다는 뜻입니다.</span> | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
    | <span data-sdd-label-en="It may return Invalid as the validation status.">검증 상태로 Invalid를 반환할 수 있습니다.</span> | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
    | <span data-sdd-label-en="It may return Adjusted as the validation status.">검증 상태로 Adjusted를 반환할 수 있습니다.</span> | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
    | <span data-sdd-label-en="It may return Valid as the validation status.">검증 상태로 Valid를 반환할 수 있습니다.</span> | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
<!-- /sdd:visual:validation-results -->

<!-- sdd:visual:configuration-contract-validity -->
### 역할 기반 구성 생성의 반환 계약

```mermaid
flowchart TB
%% sdd:translations {"요청한 roles를 만족할 수 <br/>없으면 null 포인터를 <br/>반환합니다.": "If the requested roles <br/>cannot be satisfied, it <br/>returns a null pointer.", "요청한 roles를 만족할 수 <br/>없으면 반환합니다.": "It returns this if the <br/>requested roles cannot be <br/>satisfied.", "요청한 roles를 만족할 수 <br/>있으면 반환합니다.": "It returns this if the <br/>requested roles can be <br/>satisfied.", "요청한 roles를 만족할 수 <br/>있으면 유효한 <br/>CameraConfiguration을 <br/>반환합니다.": "If the requested roles can <br/>be satisfied, it returns a <br/>valid CameraConfiguration.", "호출자는 기본 구성을 <br/>얻으려는 용도로 roles를 <br/>채워야 하며, <br/>PipelineHandler::<br/>generateConfiguration은 <br/>해당 카메라의 기본 구성 <br/>생성을 요청받습니다.": "The caller must populate <br/>roles with the intended use <br/>cases; <br/>PipelineHandler::<br/>generateConfiguration is <br/>asked to generate a default <br/>configuration for the <br/>camera."}
  v_request["호출자는 기본 구성을 <br/>얻으려는 용도로 roles를 <br/>채워야 하며, <br/>PipelineHandler::<br/>generateConfiguration은 <br/>해당 카메라의 기본 구성 <br/>생성을 요청받습니다."]
  v_valid["요청한 roles를 만족할 수 <br/>있으면 유효한 <br/>CameraConfiguration을 <br/>반환합니다."]
  v_null["요청한 roles를 만족할 수 <br/>없으면 null 포인터를 <br/>반환합니다."]
  v_request -->|"요청한 roles를 만족할 수 <br/>있으면 반환합니다."| v_valid
  v_request -->|"요청한 roles를 만족할 수 <br/>없으면 반환합니다."| v_null
```

[Mermaid 원문](vendor-assurance.configuration-contract-validity.mmd)

??? note "그림 근거와 확인 범위"
    PipelineHandler::generateConfiguration은 요청한 roles를 만족할 수 있을 때와 없을 때 무엇을 반환합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="The caller must populate roles with the intended use cases; PipelineHandler::generateConfiguration is asked to generate a default configuration for the camera.">호출자는 기본 구성을 얻으려는 용도로 roles를 채워야 하며, PipelineHandler::generateConfiguration은 해당 카메라의 기본 구성 생성을 요청받습니다.</span> | [src/libcamera/pipeline_handler.cpp:271](#source-23ff032cd1152d56) |
    | <span data-sdd-label-en="If the requested roles can be satisfied, it returns a valid CameraConfiguration.">요청한 roles를 만족할 수 있으면 유효한 CameraConfiguration을 반환합니다.</span> | [src/libcamera/pipeline_handler.cpp:271](#source-23ff032cd1152d56) |
    | <span data-sdd-label-en="If the requested roles cannot be satisfied, it returns a null pointer.">요청한 roles를 만족할 수 없으면 null 포인터를 반환합니다.</span> | [src/libcamera/pipeline_handler.cpp:271](#source-23ff032cd1152d56) |
    | <span data-sdd-label-en="It returns this if the requested roles can be satisfied.">요청한 roles를 만족할 수 있으면 반환합니다.</span> | [src/libcamera/pipeline_handler.cpp:271](#source-23ff032cd1152d56) |
    | <span data-sdd-label-en="It returns this if the requested roles cannot be satisfied.">요청한 roles를 만족할 수 없으면 반환합니다.</span> | [src/libcamera/pipeline_handler.cpp:271](#source-23ff032cd1152d56) |
<!-- /sdd:visual:configuration-contract-validity -->

`CameraConfiguration::validate()`가 `CameraConfiguration::Valid`를 반환하면 원래 구성이 이미 유효했고 조정되지 않았음을 뜻합니다. `PipelineHandler::generateConfiguration()`은 `roles`로 요청한 스트림 역할을 충족할 수 있으면 유효한 `CameraConfiguration`을 반환하고, 충족할 수 없으면 `null` 포인터를 반환합니다. `PipelineHandler::configure()`에 전달되는 설정은 `CameraConfiguration::validate()`로 검증되어 있음이 보장되므로, 파이프라인 핸들러 구현자는 추가 검증을 해서는 안 됩니다. `PipelineHandler::configure()` 구현자는 구성에 성공하면 `0`을, 실패하면 음수 오류 코드를 반환해야 합니다. `src/libcamera/camera.cpp:323`, `src/libcamera/pipeline_handler.cpp:271`, `src/libcamera/pipeline_handler.cpp:304`, `src/libcamera/pipeline_handler.cpp:313`

근거 원문: [src/libcamera/camera.cpp:338](#source-60ab47044c6107c5) · [src/libcamera/camera.cpp:343](#source-e5758fc43bf244cd) · [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) · [src/libcamera/pipeline_handler.cpp:289](#source-4abbe39594a1bd27) · [src/libcamera/pipeline_handler.cpp:304](#source-31c5407347b4d0d8) · [src/libcamera/pipeline_handler.cpp:313](#source-f87ceb096b9f931d) · [src/libcamera/camera.cpp:341](#source-8b6aa81367245db5) · [src/libcamera/camera.cpp:342](#source-e13fede0aa40ada1) · [src/libcamera/pipeline_handler.cpp:271](#source-23ff032cd1152d56)

## 성능 근거를 읽는 기준

`DebayerCpu`의 내장 벤치마크는 통계를 수집하고 디베이어링하는 처리에 걸린 시간만 측정합니다. 프레임 캡처와 출력에 걸린 시간은 측정하지 않습니다. 이 벤치마크는 `Software ISP`를 사용하는 파이프라인에서 `cam` 또는 `qcam`을 실행하여 사용할 수 있습니다. `Documentation/software-isp-benchmarking.rst:15`

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

<a id="source-e5758fc43bf244cd"></a>

??? note "소스 근거: src/libcamera/camera.cpp:343"
    `src/libcamera/camera.cpp:343`에서 시작하는 발췌입니다. 종료 줄은 344이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `f2efdb13d4f1bd8dd432fb0badb987eab0cc484fe8ecb30b7ea9d47c0126590c`
    
    ```text
    The caller shall check the
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

<a id="source-23ff032cd1152d56"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:271"
    `src/libcamera/pipeline_handler.cpp:271`에서 시작하는 발췌입니다. 종료 줄은 291이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `c1f4cc7aeedfc57e2bc5ebd6825a77f605173b44f7fde564aebc01bb013119cf`
    
    ```text
    \fn PipelineHandler::generateConfiguration()
     * \brief Generate a camera configuration for a specified camera
     * \param[in] camera The camera to generate a default configuration for
     * \param[in] roles A list of stream roles
     *
     * Generate a default configuration for the \a camera for a specified list of
     * stream roles. The caller shall populate the \a roles with the use-cases it
     * wishes to fetch the default configuration for. The returned configuration
     * can then be examined by the caller to learn about the selected streams and
     * their default parameters.
     *
     * The intended companion to this is \a configure() which can be used to change
     * the group of streams parameters.
     *
     * \context This function may be called from any thread and shall be
     * \threadsafe. It shall not modify the state of the \a camera in the pipeline
     * handler.
     *
     * \return A valid CameraConfiguration if the requested roles can be satisfied,
     * or a null pointer otherwise.
     */
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
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `293d751a81`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-05 · 사람 검토 전

다음 단계: [요청 처리와 문제 진단](request-lifecycle.md)
