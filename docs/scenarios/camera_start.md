---
generated_at: 2026-11-04 05:03:21+00:00
source_commit: da6a6ed33ed0ab305f10b6f8b44736150d39cef4
status: ok
section: scenario-camera_start
generation_method: facts-and-llm
scenario_id: camera_start
entry: Camera::start(const ControlList *)
scenario_fingerprint: 32f0d03b3491b90ffb0736a642fac9e6a9d8a5ad23bf22f4fa5d67ba9f53f295
evidence_fingerprint: 9b88c4cce5298ba7054b8518bcf99ef2da0d6d6ddb7c5aa8c24a4b3d6cc1bb9d
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design:
  schema: 1
  input_fingerprint: 9b88c4cce5298ba7054b8518bcf99ef2da0d6d6ddb7c5aa8c24a4b3d6cc1bb9d
  answers:
    session:
    - text: '`Camera::start()`는 카메라 캡처 세션을 시작하며, 선택적으로 시작 전에 적용할 `controls` 목록을 받습니다.
        카메라가 시작되면 애플리케이션은 `stop()`으로 캡처 세션을 종료할 때까지 카메라가 처리하고 애플리케이션에 반환할 요청을 큐에 넣을
        수 있습니다. 호출자는 카메라가 `Configured` 상태일 때만 이 함수를 호출해야 하며, 카메라 상태에 영향을 주는 다른 함수와
        호출을 동기화해야 합니다. 카메라의 시스템 연결이 해제된 경우 `-ENODEV`를, 시작할 수 없는 상태인 경우 `-EACCES`를
        반환합니다.'
      evidence:
      - start
      covers:
      - session
      kind: behavior
      quote: "\\brief Start capture from camera\n * \\param[in] controls Controls\
        \ to be applied before starting the Camera\n *\n * Start the camera capture\
        \ session, optionally providing a list of controls to\n * apply before starting.\
        \ Once the camera is started the application can queue\n * requests to the\
        \ camera to process and return to the application until the\n * capture session\
        \ is terminated with \\a stop().\n *\n * \\context This function may only\
        \ be called when the camera is in the\n * Configured state as defined in \\\
        ref camera_operation, and shall be\n * synchronized by the caller with other\
        \ functions that affect the camera\n * state.\n *\n * \\return 0 on success\
        \ or a negative error code otherwise\n * \\retval -ENODEV The camera has been\
        \ disconnected from the system\n * \\retval -EACCES The camera is not in a\
        \ state where it can be started\n */"
      part_id: answer
    activation:
    - text: '`Camera::start`는 `controls`가 있으면 `ControlList` 복사본을 만들고 `patchControlList`로
        전처리한 뒤 그 복사본을 전달하며, 없으면 `nullptr`을 전달합니다. 두 분기 모두 `PipelineHandler::start`를
        `ConnectionTypeBlocking`으로 호출하며, 이 함수는 `CameraManager` 스레드에서 호출됩니다.'
      evidence:
      - start
      - pipeline-start
      covers:
      - activation
      kind: behavior
      quote: "if (controls) {\n\t\tControlList copy(*controls);\n\t\tpatchControlList(copy);\n\
        \t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\t\t\t\t\t    \
        \ ConnectionTypeBlocking, this, &copy);\n\t} else {\n\t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\
        \t\t\t\t\t     ConnectionTypeBlocking, this, nullptr);\n\t}"
      part_id: answer
    - text: '`Camera::start`는 호출 결과인 `ret`이 0이 아니면 `CameraRunning` 상태를 설정하지 않고 `ret`을
        그대로 반환합니다. `ret`이 0이면 `CameraRunning` 상태를 설정하고 0을 반환합니다.'
      evidence:
      - start
      covers:
      - activation
      kind: behavior
      quote: "if (ret)\n\t\treturn ret;"
      part_id: answer
    - text: '`Camera::start`는 `PipelineHandler::start`를 호출하기 전에 `ASSERT(d->requestSequence_
        == 0)`을 실행합니다. 이 검사가 실패하면 `ASSERT`는 오류 메시지를 `Fatal` 로그 수준으로 기록하고 프로그램 실행을
        중단하며, 일반 오류 반환과는 다르게 동작합니다. `log.h`를 포함하기 전에 `NDEBUG`가 정의되면 `ASSERT`는 코드를
        생성하지 않습니다.'
      evidence:
      - start
      - logging
      covers:
      - activation
      kind: behavior
      quote: ASSERT(d->requestSequence_ == 0);
      part_id: answer
  topic_inputs:
    session: f3da69f705c2bb896ed8087e8cc457c02e4d68e7bc326d3ce448031f876ff3db
    activation: 7fc85998685d1ee766bfab8423a47f55fc49428219cd3fb867756cb87a2ccfb0
  reused_topics:
  - session
  - activation
  replayed_units: []
  generated_topics: []
  topic_agents:
    session: cli/codex/gpt-6.1-terra
    activation: cli/codex/gpt-6.1-terra
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
    product_context: 57cc3233cfdcf429751f31081ffca06a8f8b53fb15fb1e3a5256aa7998a8ceb4
    design_response: deb70dda7ad27f001267e4a9712c5b0dc1fe9fa67acd13bedbfefaaad0ad83c8
    design_validation: 0613b830b96fd2828171dea499807c3366edd72208ed814a95e5228dd106dd73
  validation_model: 81a82b9d94ef92ea1b2731b1be27f0face4475a818b926b9b2862183fbb064f8
  style_policy:
    fluent-korean.md: ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975
    i-have-adhd.md: 3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9
    README.md: b87a84b1bc31079837dc4dc4527ce02c9dc2cbc3a26ff7e99e0872941d213995
  reuse_lineage:
    source_commit: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61
    body_sha256: 67e0675dc4ceb7c209762301ee2d6c12c58e2b4f50bcbb3f57392c230afcd01c
    topics:
    - session
    - activation
    validation: current source, contract and editorial checks; human review pending
  body_sha256: 119cbe385fdde8d5859e4aa678a043d2ba0dc99fa760d5be035ab4e22ce87c8e
generated_visuals:
  schema: 1
  records:
    item-session:
      input_fingerprint: 012f38883a3f4667e713e8fa9a75cbb39a120a92ec1ef2772590f4c902dd1a46
      draft:
        nodes:
        - id: start
          symbol: Start
          label: Camera::start는 카메라 캡처 세션을 시작합니다.
          label_en: Camera::start starts a camera capture session.
          shape: box
          quote_ids:
          - start:0
        - id: configured
          symbol: Configured
          label: 카메라가 Configured 상태일 때만 시작 함수를 호출할 수 있습니다.
          label_en: The start function may only be called when the camera is Configured.
          shape: box
          quote_ids:
          - start:0
        - id: controls
          symbol: controls
          label: controls 목록은 선택 사항이며 제공하면 카메라를 시작하기 전에 적용합니다.
          label_en: The controls list is optional and is applied before the camera
            starts if provided.
          shape: box
          quote_ids:
          - start:0
        - id: caller
          symbol: caller
          label: 호출자는 시작 함수를 카메라 상태에 영향을 주는 다른 함수와 동기화해야 합니다.
          label_en: The caller must synchronize the start function with other functions
            affecting camera state.
          shape: box
          quote_ids:
          - start:0
        - id: enodev
          symbol: ENODEV
          label: -ENODEV는 카메라가 시스템에서 연결 해제되었음을 뜻합니다.
          label_en: -ENODEV means the camera has been disconnected from the system.
          shape: box
          quote_ids:
          - start:1
        - id: eacces
          symbol: EACCES
          label: -EACCES는 카메라가 시작할 수 있는 상태가 아님을 뜻합니다.
          label_en: -EACCES means the camera is not in a state where it can be started.
          shape: box
          quote_ids:
          - start:2
        - id: requests
          symbol: requests
          label: 카메라가 시작되면 애플리케이션은 처리 후 자신에게 반환할 요청을 카메라에 큐로 제출할 수 있습니다.
          label_en: Once the camera starts, the application can queue requests for
            processing and return to it.
          shape: box
          quote_ids:
          - start:0
        - id: stop
          symbol: stop
          label: stop()은 캡처 세션을 종료합니다.
          label_en: stop() terminates the capture session.
          shape: box
          quote_ids:
          - start:0
        edges:
        - from: configured
          to: start
          label: Configured는 시작 함수 호출의 전제입니다.
          label_en: Configured is a precondition for calling the start function.
          condition_ref: always
          quote_ids:
          - start:0
        - from: controls
          to: start
          label: 선택적으로 제공한 controls는 시작 전에 적용합니다.
          label_en: Optional controls are applied before starting.
          condition_ref: always
          quote_ids:
          - start:0
        - from: caller
          to: start
          label: caller는 시작 함수를 카메라 상태에 영향을 주는 다른 함수와 동기화해야 합니다.
          label_en: The caller must synchronize start with other state-affecting functions.
          condition_ref: always
          quote_ids:
          - start:0
        - from: start
          to: enodev
          label: 카메라가 시스템에서 연결 해제되었으면 시작 함수는 -ENODEV를 반환합니다.
          label_en: The start function returns -ENODEV if the camera is disconnected.
          condition_ref: always
          quote_ids:
          - start:1
        - from: start
          to: eacces
          label: 카메라가 시작할 수 있는 상태가 아니면 시작 함수는 -EACCES를 반환합니다.
          label_en: The start function returns -EACCES if the camera cannot be started.
          condition_ref: always
          quote_ids:
          - start:2
        - from: start
          to: requests
          label: 카메라가 시작되면 애플리케이션은 요청을 큐로 제출할 수 있습니다.
          label_en: Once the camera starts, the application can queue requests.
          condition_ref: always
          quote_ids:
          - start:0
        - from: requests
          to: stop
          label: 애플리케이션은 stop()으로 세션이 종료될 때까지 요청을 큐로 제출할 수 있습니다.
          label_en: The application can queue requests until stop() ends the session.
          condition_ref: always
          quote_ids:
          - start:0
      graph:
        id: item-session
        topic: session
        kind: ownership
        title: 요청을 제출할 캡처 세션을 시작하기의 관계와 경계
        question: Configured 전제와 선택적 제어값, 시작 오류, 요청 제출 및 stop은 캡처 세션에서 어떻게 연결되는가?
        condition_display: evidence
        nodes:
        - id: start
          label: Camera::start는 카메라 캡처 세션을 시작합니다.
          label_en: Camera::start starts a camera capture session.
          shape: box
          evidence:
          - source: session/start
            sha256: 9121c6f5bd2e73de134af571dd2a8a2089f052b08739b10519bdf9433ea1b2b9
            quote: "\\brief Start capture from camera\n * \\param[in] controls Controls\
              \ to be applied before starting the Camera\n *\n * Start the camera\
              \ capture session, optionally providing a list of controls to\n * apply\
              \ before starting. Once the camera is started the application can queue\n\
              \ * requests to the camera to process and return to the application\
              \ until the\n * capture session is terminated with \\a stop().\n *\n\
              \ * \\context This function may only be called when the camera is in\
              \ the\n * Configured state as defined in \\ref camera_operation, and\
              \ shall be\n * synchronized by the caller with other functions that\
              \ affect the camera\n * state.\n *\n * \\return 0 on success or a negative\
              \ error code otherwise"
        - id: configured
          label: 카메라가 Configured 상태일 때만 시작 함수를 호출할 수 있습니다.
          label_en: The start function may only be called when the camera is Configured.
          shape: box
          evidence:
          - source: session/start
            sha256: 9121c6f5bd2e73de134af571dd2a8a2089f052b08739b10519bdf9433ea1b2b9
            quote: "\\brief Start capture from camera\n * \\param[in] controls Controls\
              \ to be applied before starting the Camera\n *\n * Start the camera\
              \ capture session, optionally providing a list of controls to\n * apply\
              \ before starting. Once the camera is started the application can queue\n\
              \ * requests to the camera to process and return to the application\
              \ until the\n * capture session is terminated with \\a stop().\n *\n\
              \ * \\context This function may only be called when the camera is in\
              \ the\n * Configured state as defined in \\ref camera_operation, and\
              \ shall be\n * synchronized by the caller with other functions that\
              \ affect the camera\n * state.\n *\n * \\return 0 on success or a negative\
              \ error code otherwise"
        - id: controls
          label: controls 목록은 선택 사항이며 제공하면 카메라를 시작하기 전에 적용합니다.
          label_en: The controls list is optional and is applied before the camera
            starts if provided.
          shape: box
          evidence:
          - source: session/start
            sha256: 9121c6f5bd2e73de134af571dd2a8a2089f052b08739b10519bdf9433ea1b2b9
            quote: "\\brief Start capture from camera\n * \\param[in] controls Controls\
              \ to be applied before starting the Camera\n *\n * Start the camera\
              \ capture session, optionally providing a list of controls to\n * apply\
              \ before starting. Once the camera is started the application can queue\n\
              \ * requests to the camera to process and return to the application\
              \ until the\n * capture session is terminated with \\a stop().\n *\n\
              \ * \\context This function may only be called when the camera is in\
              \ the\n * Configured state as defined in \\ref camera_operation, and\
              \ shall be\n * synchronized by the caller with other functions that\
              \ affect the camera\n * state.\n *\n * \\return 0 on success or a negative\
              \ error code otherwise"
        - id: caller
          label: 호출자는 시작 함수를 카메라 상태에 영향을 주는 다른 함수와 동기화해야 합니다.
          label_en: The caller must synchronize the start function with other functions
            affecting camera state.
          shape: box
          evidence:
          - source: session/start
            sha256: 9121c6f5bd2e73de134af571dd2a8a2089f052b08739b10519bdf9433ea1b2b9
            quote: "\\brief Start capture from camera\n * \\param[in] controls Controls\
              \ to be applied before starting the Camera\n *\n * Start the camera\
              \ capture session, optionally providing a list of controls to\n * apply\
              \ before starting. Once the camera is started the application can queue\n\
              \ * requests to the camera to process and return to the application\
              \ until the\n * capture session is terminated with \\a stop().\n *\n\
              \ * \\context This function may only be called when the camera is in\
              \ the\n * Configured state as defined in \\ref camera_operation, and\
              \ shall be\n * synchronized by the caller with other functions that\
              \ affect the camera\n * state.\n *\n * \\return 0 on success or a negative\
              \ error code otherwise"
        - id: enodev
          label: -ENODEV는 카메라가 시스템에서 연결 해제되었음을 뜻합니다.
          label_en: -ENODEV means the camera has been disconnected from the system.
          shape: box
          evidence:
          - source: session/start
            sha256: 9121c6f5bd2e73de134af571dd2a8a2089f052b08739b10519bdf9433ea1b2b9
            quote: "\\brief Start capture from camera\n * \\param[in] controls Controls\
              \ to be applied before starting the Camera\n *\n * Start the camera\
              \ capture session, optionally providing a list of controls to\n * apply\
              \ before starting. Once the camera is started the application can queue\n\
              \ * requests to the camera to process and return to the application\
              \ until the\n * capture session is terminated with \\a stop().\n *\n\
              \ * \\context This function may only be called when the camera is in\
              \ the\n * Configured state as defined in \\ref camera_operation, and\
              \ shall be\n * synchronized by the caller with other functions that\
              \ affect the camera\n * state.\n *\n * \\return 0 on success or a negative\
              \ error code otherwise\n * \\retval -ENODEV The camera has been disconnected\
              \ from the system"
        - id: eacces
          label: -EACCES는 카메라가 시작할 수 있는 상태가 아님을 뜻합니다.
          label_en: -EACCES means the camera is not in a state where it can be started.
          shape: box
          evidence:
          - source: session/start
            sha256: 9121c6f5bd2e73de134af571dd2a8a2089f052b08739b10519bdf9433ea1b2b9
            quote: "\\brief Start capture from camera\n * \\param[in] controls Controls\
              \ to be applied before starting the Camera\n *\n * Start the camera\
              \ capture session, optionally providing a list of controls to\n * apply\
              \ before starting. Once the camera is started the application can queue\n\
              \ * requests to the camera to process and return to the application\
              \ until the\n * capture session is terminated with \\a stop().\n *\n\
              \ * \\context This function may only be called when the camera is in\
              \ the\n * Configured state as defined in \\ref camera_operation, and\
              \ shall be\n * synchronized by the caller with other functions that\
              \ affect the camera\n * state.\n *\n * \\return 0 on success or a negative\
              \ error code otherwise\n * \\retval -ENODEV The camera has been disconnected\
              \ from the system\n * \\retval -EACCES The camera is not in a state\
              \ where it can be started\n */"
        - id: requests
          label: 카메라가 시작되면 애플리케이션은 처리 후 자신에게 반환할 요청을 카메라에 큐로 제출할 수 있습니다.
          label_en: Once the camera starts, the application can queue requests for
            processing and return to it.
          shape: box
          evidence:
          - source: session/start
            sha256: 9121c6f5bd2e73de134af571dd2a8a2089f052b08739b10519bdf9433ea1b2b9
            quote: "\\brief Start capture from camera\n * \\param[in] controls Controls\
              \ to be applied before starting the Camera\n *\n * Start the camera\
              \ capture session, optionally providing a list of controls to\n * apply\
              \ before starting. Once the camera is started the application can queue\n\
              \ * requests to the camera to process and return to the application\
              \ until the\n * capture session is terminated with \\a stop().\n *\n\
              \ * \\context This function may only be called when the camera is in\
              \ the\n * Configured state as defined in \\ref camera_operation, and\
              \ shall be\n * synchronized by the caller with other functions that\
              \ affect the camera\n * state.\n *\n * \\return 0 on success or a negative\
              \ error code otherwise"
        - id: stop
          label: stop()은 캡처 세션을 종료합니다.
          label_en: stop() terminates the capture session.
          shape: box
          evidence:
          - source: session/start
            sha256: 9121c6f5bd2e73de134af571dd2a8a2089f052b08739b10519bdf9433ea1b2b9
            quote: "\\brief Start capture from camera\n * \\param[in] controls Controls\
              \ to be applied before starting the Camera\n *\n * Start the camera\
              \ capture session, optionally providing a list of controls to\n * apply\
              \ before starting. Once the camera is started the application can queue\n\
              \ * requests to the camera to process and return to the application\
              \ until the\n * capture session is terminated with \\a stop().\n *\n\
              \ * \\context This function may only be called when the camera is in\
              \ the\n * Configured state as defined in \\ref camera_operation, and\
              \ shall be\n * synchronized by the caller with other functions that\
              \ affect the camera\n * state.\n *\n * \\return 0 on success or a negative\
              \ error code otherwise"
        edges:
        - from: configured
          to: start
          label: Configured는 시작 함수 호출의 전제입니다.
          label_en: Configured is a precondition for calling the start function.
          evidence:
          - source: session/start
            sha256: 9121c6f5bd2e73de134af571dd2a8a2089f052b08739b10519bdf9433ea1b2b9
            quote: "\\brief Start capture from camera\n * \\param[in] controls Controls\
              \ to be applied before starting the Camera\n *\n * Start the camera\
              \ capture session, optionally providing a list of controls to\n * apply\
              \ before starting. Once the camera is started the application can queue\n\
              \ * requests to the camera to process and return to the application\
              \ until the\n * capture session is terminated with \\a stop().\n *\n\
              \ * \\context This function may only be called when the camera is in\
              \ the\n * Configured state as defined in \\ref camera_operation, and\
              \ shall be\n * synchronized by the caller with other functions that\
              \ affect the camera\n * state.\n *\n * \\return 0 on success or a negative\
              \ error code otherwise"
        - from: controls
          to: start
          label: 선택적으로 제공한 controls는 시작 전에 적용합니다.
          label_en: Optional controls are applied before starting.
          evidence:
          - source: session/start
            sha256: 9121c6f5bd2e73de134af571dd2a8a2089f052b08739b10519bdf9433ea1b2b9
            quote: "\\brief Start capture from camera\n * \\param[in] controls Controls\
              \ to be applied before starting the Camera\n *\n * Start the camera\
              \ capture session, optionally providing a list of controls to\n * apply\
              \ before starting. Once the camera is started the application can queue\n\
              \ * requests to the camera to process and return to the application\
              \ until the\n * capture session is terminated with \\a stop().\n *\n\
              \ * \\context This function may only be called when the camera is in\
              \ the\n * Configured state as defined in \\ref camera_operation, and\
              \ shall be\n * synchronized by the caller with other functions that\
              \ affect the camera\n * state.\n *\n * \\return 0 on success or a negative\
              \ error code otherwise"
        - from: caller
          to: start
          label: caller는 시작 함수를 카메라 상태에 영향을 주는 다른 함수와 동기화해야 합니다.
          label_en: The caller must synchronize start with other state-affecting functions.
          evidence:
          - source: session/start
            sha256: 9121c6f5bd2e73de134af571dd2a8a2089f052b08739b10519bdf9433ea1b2b9
            quote: "\\brief Start capture from camera\n * \\param[in] controls Controls\
              \ to be applied before starting the Camera\n *\n * Start the camera\
              \ capture session, optionally providing a list of controls to\n * apply\
              \ before starting. Once the camera is started the application can queue\n\
              \ * requests to the camera to process and return to the application\
              \ until the\n * capture session is terminated with \\a stop().\n *\n\
              \ * \\context This function may only be called when the camera is in\
              \ the\n * Configured state as defined in \\ref camera_operation, and\
              \ shall be\n * synchronized by the caller with other functions that\
              \ affect the camera\n * state.\n *\n * \\return 0 on success or a negative\
              \ error code otherwise"
        - from: start
          to: enodev
          label: 카메라가 시스템에서 연결 해제되었으면 시작 함수는 -ENODEV를 반환합니다.
          label_en: The start function returns -ENODEV if the camera is disconnected.
          evidence:
          - source: session/start
            sha256: 9121c6f5bd2e73de134af571dd2a8a2089f052b08739b10519bdf9433ea1b2b9
            quote: "\\brief Start capture from camera\n * \\param[in] controls Controls\
              \ to be applied before starting the Camera\n *\n * Start the camera\
              \ capture session, optionally providing a list of controls to\n * apply\
              \ before starting. Once the camera is started the application can queue\n\
              \ * requests to the camera to process and return to the application\
              \ until the\n * capture session is terminated with \\a stop().\n *\n\
              \ * \\context This function may only be called when the camera is in\
              \ the\n * Configured state as defined in \\ref camera_operation, and\
              \ shall be\n * synchronized by the caller with other functions that\
              \ affect the camera\n * state.\n *\n * \\return 0 on success or a negative\
              \ error code otherwise\n * \\retval -ENODEV The camera has been disconnected\
              \ from the system"
        - from: start
          to: eacces
          label: 카메라가 시작할 수 있는 상태가 아니면 시작 함수는 -EACCES를 반환합니다.
          label_en: The start function returns -EACCES if the camera cannot be started.
          evidence:
          - source: session/start
            sha256: 9121c6f5bd2e73de134af571dd2a8a2089f052b08739b10519bdf9433ea1b2b9
            quote: "\\brief Start capture from camera\n * \\param[in] controls Controls\
              \ to be applied before starting the Camera\n *\n * Start the camera\
              \ capture session, optionally providing a list of controls to\n * apply\
              \ before starting. Once the camera is started the application can queue\n\
              \ * requests to the camera to process and return to the application\
              \ until the\n * capture session is terminated with \\a stop().\n *\n\
              \ * \\context This function may only be called when the camera is in\
              \ the\n * Configured state as defined in \\ref camera_operation, and\
              \ shall be\n * synchronized by the caller with other functions that\
              \ affect the camera\n * state.\n *\n * \\return 0 on success or a negative\
              \ error code otherwise\n * \\retval -ENODEV The camera has been disconnected\
              \ from the system\n * \\retval -EACCES The camera is not in a state\
              \ where it can be started\n */"
        - from: start
          to: requests
          label: 카메라가 시작되면 애플리케이션은 요청을 큐로 제출할 수 있습니다.
          label_en: Once the camera starts, the application can queue requests.
          evidence:
          - source: session/start
            sha256: 9121c6f5bd2e73de134af571dd2a8a2089f052b08739b10519bdf9433ea1b2b9
            quote: "\\brief Start capture from camera\n * \\param[in] controls Controls\
              \ to be applied before starting the Camera\n *\n * Start the camera\
              \ capture session, optionally providing a list of controls to\n * apply\
              \ before starting. Once the camera is started the application can queue\n\
              \ * requests to the camera to process and return to the application\
              \ until the\n * capture session is terminated with \\a stop().\n *\n\
              \ * \\context This function may only be called when the camera is in\
              \ the\n * Configured state as defined in \\ref camera_operation, and\
              \ shall be\n * synchronized by the caller with other functions that\
              \ affect the camera\n * state.\n *\n * \\return 0 on success or a negative\
              \ error code otherwise"
        - from: requests
          to: stop
          label: 애플리케이션은 stop()으로 세션이 종료될 때까지 요청을 큐로 제출할 수 있습니다.
          label_en: The application can queue requests until stop() ends the session.
          evidence:
          - source: session/start
            sha256: 9121c6f5bd2e73de134af571dd2a8a2089f052b08739b10519bdf9433ea1b2b9
            quote: "\\brief Start capture from camera\n * \\param[in] controls Controls\
              \ to be applied before starting the Camera\n *\n * Start the camera\
              \ capture session, optionally providing a list of controls to\n * apply\
              \ before starting. Once the camera is started the application can queue\n\
              \ * requests to the camera to process and return to the application\
              \ until the\n * capture session is terminated with \\a stop().\n *\n\
              \ * \\context This function may only be called when the camera is in\
              \ the\n * Configured state as defined in \\ref camera_operation, and\
              \ shall be\n * synchronized by the caller with other functions that\
              \ affect the camera\n * state.\n *\n * \\return 0 on success or a negative\
              \ error code otherwise"
        producer: cli/codex/gpt-6.1-terra
      producer: cli/codex/gpt-6.1-terra
      generation_commit: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
      citation_binding_policy: identifier-and-guard-boundaries-v2
      reused: false
    item-activation:
      input_fingerprint: 17dede3b5a09996fd6fcbfa2963dd01b4d7dadcec181c775d28a4e27c3c2eb18
      draft:
        nodes:
        - id: access
          symbol: isAccessAllowed
          label: CameraConfigured 접근 확인 결과가 음수인지 검사합니다.
          label_en: It checks whether the CameraConfigured access result is negative.
          shape: decision
          quote_ids:
          - start:1
        - id: returned
          symbol: return
          label: 접근 확인 결과가 음수이거나 파이프라인 결과가 0이 아니면 해당 결과를 그대로 반환합니다.
          label_en: It returns a negative access result or a nonzero pipeline result
            unchanged.
          shape: box
          quote_ids:
          - start:1
          - start:5
        - id: assertion
          symbol: ASSERT
          label: ASSERT가 활성화되어 있으면 requestSequence_가 0인지 검사합니다.
          label_en: When enabled, ASSERT checks whether requestSequence_ is zero.
          shape: process
          quote_ids:
          - start:3
          - logging:1
        - id: fatal
          symbol: Fatal
          label: ASSERT의 조건이 거짓이면 Fatal 오류를 기록하고 프로그램 실행을 중단합니다.
          label_en: If the ASSERT condition is false, it logs a Fatal error and aborts
            execution.
          shape: box
          quote_ids:
          - logging:1
        - id: ndebug
          symbol: NDEBUG
          label: log.h를 포함하기 전에 NDEBUG를 정의하면 ASSERT 코드는 생성되지 않습니다.
          label_en: If NDEBUG is defined before including log.h, ASSERT generates
            no code.
          shape: box
          quote_ids:
          - logging:1
        - id: controls
          symbol: controls
          label: controls의 유무에 따라 전달할 제어값을 정합니다.
          label_en: It chooses what to pass based on whether controls is present.
          shape: decision
          quote_ids:
          - start:4
        - id: copy
          symbol: copy
          label: controls를 복사하고 copy에 patchControlList를 적용합니다.
          label_en: It copies controls and applies patchControlList to copy.
          shape: process
          quote_ids:
          - start:4
        - id: 'null'
          symbol: nullptr
          label: controls가 없으면 nullptr을 전달합니다.
          label_en: It passes nullptr when controls is absent.
          shape: process
          quote_ids:
          - start:4
        - id: invoke
          symbol: PipelineHandler::start
          label: PipelineHandler::start는 ConnectionTypeBlocking으로 호출되며 CameraManager
            스레드에서 실행됩니다.
          label_en: PipelineHandler::start runs on the CameraManager thread via ConnectionTypeBlocking.
          shape: process
          quote_ids:
          - start:4
          - pipeline-start:0
        - id: result
          symbol: ret
          label: 파이프라인 호출 결과 ret이 0인지 검사합니다.
          label_en: It checks whether the pipeline call result ret is zero.
          shape: decision
          quote_ids:
          - start:4
          - start:5
        - id: running
          symbol: setState
          label: 결과가 0이면 상태를 Private::CameraRunning으로 갱신합니다.
          label_en: If the result is zero, it sets the state to Private::CameraRunning.
          shape: process
          quote_ids:
          - start:5
          - start:6
        edges:
        - from: access
          to: returned
          label: 음수 결과를 그대로 반환합니다.
          label_en: It returns the negative result unchanged.
          condition_ref: c2:true
          quote_ids:
          - start:1
        - from: access
          to: assertion
          label: 결과가 음수가 아니면 ASSERT에 도달합니다.
          label_en: If the result is not negative, execution reaches ASSERT.
          condition_ref: c2:false
          quote_ids:
          - start:1
          - start:2
          - start:3
        - from: assertion
          to: fatal
          label: 활성화된 검사 조건이 거짓이면 실행을 중단합니다.
          label_en: If the enabled assertion is false, execution aborts.
          condition_ref: always
          quote_ids:
          - logging:1
        - from: assertion
          to: ndebug
          label: ASSERT 코드 생성 여부는 NDEBUG 정의에 따라 달라집니다.
          label_en: ASSERT code generation depends on the NDEBUG definition.
          condition_ref: always
          quote_ids:
          - logging:1
        - from: assertion
          to: controls
          label: 실행이 계속되면 controls를 확인합니다.
          label_en: If execution continues, it checks controls.
          condition_ref: always
          quote_ids:
          - start:3
          - start:4
          - logging:1
        - from: controls
          to: copy
          label: controls가 있으면 복사하고 수정합니다.
          label_en: If controls is present, it copies and patches it.
          condition_ref: c0:true
          quote_ids:
          - start:4
        - from: controls
          to: 'null'
          label: controls가 없으면 nullptr을 사용합니다.
          label_en: If controls is absent, it uses nullptr.
          condition_ref: c0:false
          quote_ids:
          - start:4
        - from: copy
          to: invoke
          label: 수정한 copy의 주소를 전달합니다.
          label_en: It passes the address of the patched copy.
          condition_ref: c0:true
          quote_ids:
          - start:4
        - from: 'null'
          to: invoke
          label: nullptr을 전달합니다.
          label_en: It passes nullptr.
          condition_ref: c0:false
          quote_ids:
          - start:4
        - from: invoke
          to: result
          label: 호출 결과를 ret에 저장하고 검사합니다.
          label_en: It stores the call result in ret and checks it.
          condition_ref: always
          quote_ids:
          - start:4
          - start:5
        - from: result
          to: returned
          label: 결과가 0이 아니면 그대로 반환합니다.
          label_en: If the result is nonzero, it returns it unchanged.
          condition_ref: c1:true
          quote_ids:
          - start:5
        - from: result
          to: running
          label: 결과가 0이면 상태를 갱신합니다.
          label_en: If the result is zero, it updates the state.
          condition_ref: c1:false
          quote_ids:
          - start:5
          - start:6
      graph:
        id: item-activation
        topic: activation
        kind: ownership
        title: 시작 제어값과 파이프라인 결과 반영의 관계와 경계
        question: ASSERT, 제어값 분기, blocking 파이프라인 호출과 반환값 분기는 어떻게 원래 오류 반환 또는 CameraRunning
          갱신으로 이어지는가?
        condition_display: evidence
        nodes:
        - id: access
          label: CameraConfigured 접근 확인 결과가 음수인지 검사합니다.
          label_en: It checks whether the CameraConfigured access result is negative.
          shape: decision
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "int ret = d->isAccessAllowed(Private::CameraConfigured);\n\tif\
              \ (ret < 0)\n\t\treturn ret;"
        - id: returned
          label: 접근 확인 결과가 음수이거나 파이프라인 결과가 0이 아니면 해당 결과를 그대로 반환합니다.
          label_en: It returns a negative access result or a nonzero pipeline result
            unchanged.
          shape: box
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "int ret = d->isAccessAllowed(Private::CameraConfigured);\n\tif\
              \ (ret < 0)\n\t\treturn ret;"
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "if (ret)\n\t\treturn ret;"
        - id: assertion
          label: ASSERT가 활성화되어 있으면 requestSequence_가 0인지 검사합니다.
          label_en: When enabled, ASSERT checks whether requestSequence_ is zero.
          shape: box
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: ASSERT(d->requestSequence_ == 0);
          - source: activation/logging
            sha256: 52e64d292f59786541e66fe48f5bae65256bdced60c803aa76bf3637083b47b0
            quote: "/**\n * \\def ASSERT(condition)\n * \\hideinitializer\n * \\brief\
              \ Abort program execution if assertion fails\n *\n * If \\a condition\
              \ is false, ASSERT() logs an error message with the Fatal log\n * level\
              \ and aborts program execution.\n *\n * If the macro NDEBUG is defined\
              \ before including log.h, ASSERT() generates no\n * code.\n *\n * Using\
              \ conditions that have side effects with ASSERT() is not recommended,\
              \ as\n * these effects would depend on whether NDEBUG is defined or\
              \ not. Similarly,\n * ASSERT() should not be used to check for errors\
              \ that can occur under normal\n * conditions as those checks would then\
              \ be removed when compiling with NDEBUG.\n */"
        - id: fatal
          label: ASSERT의 조건이 거짓이면 Fatal 오류를 기록하고 프로그램 실행을 중단합니다.
          label_en: If the ASSERT condition is false, it logs a Fatal error and aborts
            execution.
          shape: box
          evidence:
          - source: activation/logging
            sha256: 52e64d292f59786541e66fe48f5bae65256bdced60c803aa76bf3637083b47b0
            quote: "/**\n * \\def ASSERT(condition)\n * \\hideinitializer\n * \\brief\
              \ Abort program execution if assertion fails\n *\n * If \\a condition\
              \ is false, ASSERT() logs an error message with the Fatal log\n * level\
              \ and aborts program execution.\n *\n * If the macro NDEBUG is defined\
              \ before including log.h, ASSERT() generates no\n * code.\n *\n * Using\
              \ conditions that have side effects with ASSERT() is not recommended,\
              \ as\n * these effects would depend on whether NDEBUG is defined or\
              \ not. Similarly,\n * ASSERT() should not be used to check for errors\
              \ that can occur under normal\n * conditions as those checks would then\
              \ be removed when compiling with NDEBUG.\n */"
        - id: ndebug
          label: log.h를 포함하기 전에 NDEBUG를 정의하면 ASSERT 코드는 생성되지 않습니다.
          label_en: If NDEBUG is defined before including log.h, ASSERT generates
            no code.
          shape: box
          evidence:
          - source: activation/logging
            sha256: 52e64d292f59786541e66fe48f5bae65256bdced60c803aa76bf3637083b47b0
            quote: "/**\n * \\def ASSERT(condition)\n * \\hideinitializer\n * \\brief\
              \ Abort program execution if assertion fails\n *\n * If \\a condition\
              \ is false, ASSERT() logs an error message with the Fatal log\n * level\
              \ and aborts program execution.\n *\n * If the macro NDEBUG is defined\
              \ before including log.h, ASSERT() generates no\n * code.\n *\n * Using\
              \ conditions that have side effects with ASSERT() is not recommended,\
              \ as\n * these effects would depend on whether NDEBUG is defined or\
              \ not. Similarly,\n * ASSERT() should not be used to check for errors\
              \ that can occur under normal\n * conditions as those checks would then\
              \ be removed when compiling with NDEBUG.\n */"
        - id: controls
          label: controls의 유무에 따라 전달할 제어값을 정합니다.
          label_en: It chooses what to pass based on whether controls is present.
          shape: decision
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "if (controls) {\n\t\tControlList copy(*controls);\n\t\tpatchControlList(copy);\n\
              \t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\t\t\t\t\t\
              \     ConnectionTypeBlocking, this, &copy);\n\t} else {\n\t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\
              \t\t\t\t\t     ConnectionTypeBlocking, this, nullptr);\n\t}"
        - id: copy
          label: controls를 복사하고 copy에 patchControlList를 적용합니다.
          label_en: It copies controls and applies patchControlList to copy.
          shape: box
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "if (controls) {\n\t\tControlList copy(*controls);\n\t\tpatchControlList(copy);\n\
              \t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\t\t\t\t\t\
              \     ConnectionTypeBlocking, this, &copy);\n\t} else {\n\t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\
              \t\t\t\t\t     ConnectionTypeBlocking, this, nullptr);\n\t}"
        - id: 'null'
          label: controls가 없으면 nullptr을 전달합니다.
          label_en: It passes nullptr when controls is absent.
          shape: box
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "if (controls) {\n\t\tControlList copy(*controls);\n\t\tpatchControlList(copy);\n\
              \t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\t\t\t\t\t\
              \     ConnectionTypeBlocking, this, &copy);\n\t} else {\n\t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\
              \t\t\t\t\t     ConnectionTypeBlocking, this, nullptr);\n\t}"
        - id: invoke
          label: PipelineHandler::start는 ConnectionTypeBlocking으로 호출되며 CameraManager
            스레드에서 실행됩니다.
          label_en: PipelineHandler::start runs on the CameraManager thread via ConnectionTypeBlocking.
          shape: box
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "if (controls) {\n\t\tControlList copy(*controls);\n\t\tpatchControlList(copy);\n\
              \t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\t\t\t\t\t\
              \     ConnectionTypeBlocking, this, &copy);\n\t} else {\n\t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\
              \t\t\t\t\t     ConnectionTypeBlocking, this, nullptr);\n\t}"
          - source: activation/pipeline-start
            sha256: ea0201de61631e8e9551d0c94503e5b000439f9b1a1242dded9abeb9b5870c2e
            quote: "\\fn PipelineHandler::start()\n * \\brief Start capturing from\
              \ a group of streams\n * \\param[in] camera The camera to start\n *\
              \ \\param[in] controls Controls to be applied before starting the Camera\n\
              \ *\n * Start the group of streams that have been configured for capture\
              \ by\n * \\a configure(). The intended caller of this function is the\
              \ Camera class\n * which will in turn be called from the application\
              \ to indicate that it has\n * configured the streams and is ready to\
              \ capture.\n *\n * \\context This function is called from the CameraManager\
              \ thread.\n *\n * \\return 0 on success or a negative error code otherwise\n\
              \ */"
        - id: result
          label: 파이프라인 호출 결과 ret이 0인지 검사합니다.
          label_en: It checks whether the pipeline call result ret is zero.
          shape: decision
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "if (controls) {\n\t\tControlList copy(*controls);\n\t\tpatchControlList(copy);\n\
              \t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\t\t\t\t\t\
              \     ConnectionTypeBlocking, this, &copy);\n\t} else {\n\t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\
              \t\t\t\t\t     ConnectionTypeBlocking, this, nullptr);\n\t}"
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "if (ret)\n\t\treturn ret;"
        - id: running
          label: 결과가 0이면 상태를 Private::CameraRunning으로 갱신합니다.
          label_en: If the result is zero, it sets the state to Private::CameraRunning.
          shape: box
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "if (ret)\n\t\treturn ret;"
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: d->setState(Private::CameraRunning);
        edges:
        - from: access
          to: returned
          label: 음수 결과를 그대로 반환합니다. · ret < 0 [true]
          label_en: It returns the negative result unchanged. · ret < 0 [true]
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "int ret = d->isAccessAllowed(Private::CameraConfigured);\n\tif\
              \ (ret < 0)\n\t\treturn ret;"
        - from: access
          to: assertion
          label: 결과가 음수가 아니면 ASSERT에 도달합니다. · ret < 0 [false]
          label_en: If the result is not negative, execution reaches ASSERT. · ret
            < 0 [false]
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "int ret = d->isAccessAllowed(Private::CameraConfigured);\n\tif\
              \ (ret < 0)\n\t\treturn ret;"
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: LOG(Camera, Debug) << "Starting capture";
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: ASSERT(d->requestSequence_ == 0);
        - from: assertion
          to: fatal
          label: 활성화된 검사 조건이 거짓이면 실행을 중단합니다.
          label_en: If the enabled assertion is false, execution aborts.
          evidence:
          - source: activation/logging
            sha256: 52e64d292f59786541e66fe48f5bae65256bdced60c803aa76bf3637083b47b0
            quote: "/**\n * \\def ASSERT(condition)\n * \\hideinitializer\n * \\brief\
              \ Abort program execution if assertion fails\n *\n * If \\a condition\
              \ is false, ASSERT() logs an error message with the Fatal log\n * level\
              \ and aborts program execution.\n *\n * If the macro NDEBUG is defined\
              \ before including log.h, ASSERT() generates no\n * code.\n *\n * Using\
              \ conditions that have side effects with ASSERT() is not recommended,\
              \ as\n * these effects would depend on whether NDEBUG is defined or\
              \ not. Similarly,\n * ASSERT() should not be used to check for errors\
              \ that can occur under normal\n * conditions as those checks would then\
              \ be removed when compiling with NDEBUG.\n */"
        - from: assertion
          to: ndebug
          label: ASSERT 코드 생성 여부는 NDEBUG 정의에 따라 달라집니다.
          label_en: ASSERT code generation depends on the NDEBUG definition.
          evidence:
          - source: activation/logging
            sha256: 52e64d292f59786541e66fe48f5bae65256bdced60c803aa76bf3637083b47b0
            quote: "/**\n * \\def ASSERT(condition)\n * \\hideinitializer\n * \\brief\
              \ Abort program execution if assertion fails\n *\n * If \\a condition\
              \ is false, ASSERT() logs an error message with the Fatal log\n * level\
              \ and aborts program execution.\n *\n * If the macro NDEBUG is defined\
              \ before including log.h, ASSERT() generates no\n * code.\n *\n * Using\
              \ conditions that have side effects with ASSERT() is not recommended,\
              \ as\n * these effects would depend on whether NDEBUG is defined or\
              \ not. Similarly,\n * ASSERT() should not be used to check for errors\
              \ that can occur under normal\n * conditions as those checks would then\
              \ be removed when compiling with NDEBUG.\n */"
        - from: assertion
          to: controls
          label: 실행이 계속되면 controls를 확인합니다.
          label_en: If execution continues, it checks controls.
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: ASSERT(d->requestSequence_ == 0);
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "if (controls) {\n\t\tControlList copy(*controls);\n\t\tpatchControlList(copy);\n\
              \t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\t\t\t\t\t\
              \     ConnectionTypeBlocking, this, &copy);\n\t} else {\n\t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\
              \t\t\t\t\t     ConnectionTypeBlocking, this, nullptr);\n\t}"
          - source: activation/logging
            sha256: 52e64d292f59786541e66fe48f5bae65256bdced60c803aa76bf3637083b47b0
            quote: "/**\n * \\def ASSERT(condition)\n * \\hideinitializer\n * \\brief\
              \ Abort program execution if assertion fails\n *\n * If \\a condition\
              \ is false, ASSERT() logs an error message with the Fatal log\n * level\
              \ and aborts program execution.\n *\n * If the macro NDEBUG is defined\
              \ before including log.h, ASSERT() generates no\n * code.\n *\n * Using\
              \ conditions that have side effects with ASSERT() is not recommended,\
              \ as\n * these effects would depend on whether NDEBUG is defined or\
              \ not. Similarly,\n * ASSERT() should not be used to check for errors\
              \ that can occur under normal\n * conditions as those checks would then\
              \ be removed when compiling with NDEBUG.\n */"
        - from: controls
          to: copy
          label: controls가 있으면 복사하고 수정합니다. · controls [true]
          label_en: If controls is present, it copies and patches it. · controls [true]
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "if (controls) {\n\t\tControlList copy(*controls);\n\t\tpatchControlList(copy);\n\
              \t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\t\t\t\t\t\
              \     ConnectionTypeBlocking, this, &copy);\n\t} else {\n\t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\
              \t\t\t\t\t     ConnectionTypeBlocking, this, nullptr);\n\t}"
        - from: controls
          to: 'null'
          label: controls가 없으면 nullptr을 사용합니다. · controls [false]
          label_en: If controls is absent, it uses nullptr. · controls [false]
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "if (controls) {\n\t\tControlList copy(*controls);\n\t\tpatchControlList(copy);\n\
              \t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\t\t\t\t\t\
              \     ConnectionTypeBlocking, this, &copy);\n\t} else {\n\t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\
              \t\t\t\t\t     ConnectionTypeBlocking, this, nullptr);\n\t}"
        - from: copy
          to: invoke
          label: 수정한 copy의 주소를 전달합니다. · controls [true]
          label_en: It passes the address of the patched copy. · controls [true]
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "if (controls) {\n\t\tControlList copy(*controls);\n\t\tpatchControlList(copy);\n\
              \t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\t\t\t\t\t\
              \     ConnectionTypeBlocking, this, &copy);\n\t} else {\n\t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\
              \t\t\t\t\t     ConnectionTypeBlocking, this, nullptr);\n\t}"
        - from: 'null'
          to: invoke
          label: nullptr을 전달합니다. · controls [false]
          label_en: It passes nullptr. · controls [false]
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "if (controls) {\n\t\tControlList copy(*controls);\n\t\tpatchControlList(copy);\n\
              \t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\t\t\t\t\t\
              \     ConnectionTypeBlocking, this, &copy);\n\t} else {\n\t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\
              \t\t\t\t\t     ConnectionTypeBlocking, this, nullptr);\n\t}"
        - from: invoke
          to: result
          label: 호출 결과를 ret에 저장하고 검사합니다.
          label_en: It stores the call result in ret and checks it.
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "if (controls) {\n\t\tControlList copy(*controls);\n\t\tpatchControlList(copy);\n\
              \t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\t\t\t\t\t\
              \     ConnectionTypeBlocking, this, &copy);\n\t} else {\n\t\tret = d->pipe_->invokeMethod(&PipelineHandler::start,\n\
              \t\t\t\t\t     ConnectionTypeBlocking, this, nullptr);\n\t}"
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "if (ret)\n\t\treturn ret;"
        - from: result
          to: returned
          label: 결과가 0이 아니면 그대로 반환합니다. · ret [true]
          label_en: If the result is nonzero, it returns it unchanged. · ret [true]
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "if (ret)\n\t\treturn ret;"
        - from: result
          to: running
          label: 결과가 0이면 상태를 갱신합니다. · ret [false]
          label_en: If the result is zero, it updates the state. · ret [false]
          evidence:
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: "if (ret)\n\t\treturn ret;"
          - source: activation/start
            sha256: a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73
            quote: d->setState(Private::CameraRunning);
        producer: cli/codex/gpt-6.1-terra
      producer: cli/codex/gpt-6.1-terra
      generation_commit: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
      citation_binding_policy: identifier-and-guard-boundaries-v2
      reused: false
  body_sha256: 119cbe385fdde8d5859e4aa678a043d2ba0dc99fa760d5be035ab4e22ce87c8e
managed_visual_refresh:
- schema: 2
  source_commit: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
  original_manuscript_sha256: 8bcca32389a898b54665aa8da6e72db9d5f4a970e457fa4aeb3bd4afd4da67d0
  previous_body_sha256: 00d1c8b05b587431b19e16263752dac8013b5b8fa787bf58797e72a8df860f1f
  body_sha256: 119cbe385fdde8d5859e4aa678a043d2ba0dc99fa760d5be035ab4e22ce87c8e
  visual_definitions_sha256: 811ac4e658c1d2738e44c163e961f7087638ec0beb7c22832108839bd5ff5660
  preserved_outside_body_sha256: 5cabf84032765aff018bf8967c64c08875aff1a03ef1a4bd17dd1e26f73c046c
  owned_edit_regions:
  - original_start_byte: 1199
    original_end_byte: 10078
    original_sha256: 133d52504a78aff7365010581c52c147db1564460416e94c7a88f641cde801fa
    replacement_sha256: 3aee08a7d5464fbf97af666f35340c5345d11364cde4818a1c8b600e695888f5
    visual_ids:
    - item-session
  - original_start_byte: 10847
    original_end_byte: 22813
    original_sha256: f5ca7c0f3852384f6ff108896e59fd6028fe69883f393cbde1954969283d1504
    replacement_sha256: 12ac71de425c78df2d3d831fcb35961e9e9eb73f5aa1a0f2f05976e597aaad77
    visual_ids:
    - item-activation
  added_visuals: []
  scope: Separately generated native graph replacement; original prose/authorship
    retained
  new_inference: false
  semantic_approval: false
  human_review: unchanged
  graph_records_replaced: true
  previous_native_records_sha256: 8e89f832d88244d4ce3b9a12fba8799060f5206ef9ad0e5f19aee42f51ef9eab
  current_native_records_sha256: 1b3cd43a2bc6531ae16984c90f2b4d3f79decac024ae2d8ac5d7e70a6bd7901b
revalidated_from: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
---

# 캡처 시작

**구성이 끝난 카메라를 시작하고 성공 뒤 요청을 제출할 수 있는 상태인지 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| <a id="이-흐름에서-확인할-것"></a>구성이 끝난 카메라를 시작하고 성공 뒤 요청을 제출할 수 있는 상태인지 확인하세요. | [요청을 제출할 캡처 세션을 시작하기](#요청을-제출할-캡처-세션을-시작하기) |

## 요청을 제출할 캡처 세션을 시작하기

`Camera::start()`는 카메라 캡처 세션을 시작하며, 선택적으로 시작 전에 적용할 `controls` 목록을 받습니다. 카메라가 시작되면 애플리케이션은 `stop()`으로 캡처 세션을 종료할 때까지 카메라가 처리하고 애플리케이션에 반환할 요청을 큐에 넣을 수 있습니다. 호출자는 카메라가 `Configured` 상태일 때만 이 함수를 호출해야 하며, 카메라 상태에 영향을 주는 다른 함수와 호출을 동기화해야 합니다. 카메라의 시스템 연결이 해제된 경우 `-ENODEV`를, 시작할 수 없는 상태인 경우 `-EACCES`를 반환합니다. `src/libcamera/camera.cpp:1383`

<!-- sdd:visual:item-session -->
### 요청을 제출할 캡처 세션을 시작하기의 관계와 경계

```mermaid
flowchart TB
%% sdd:translations {"-EACCES는 카메라가 시작할 <br/>수 있는 상태가 아님을 <br/>뜻합니다.": "-EACCES means the camera is <br/>not in a state where it can <br/>be started.", "-ENODEV는 카메라가 <br/>시스템에서 연결 <br/>해제되었음을 뜻합니다.": "-ENODEV means the camera <br/>has been disconnected from <br/>the system.", "Camera::start는 카메라 캡처 <br/>세션을 시작합니다.": "Camera::start starts a <br/>camera capture session.", "Configured는 시작 함수 <br/>호출의 전제입니다.": "Configured is a <br/>precondition for calling <br/>the start function.", "caller는 시작 함수를 카메라 <br/>상태에 영향을 주는 다른 <br/>함수와 동기화해야 합니다.": "The caller must synchronize <br/>start with other <br/>state-affecting functions.", "controls 목록은 선택 <br/>사항이며 제공하면 카메라를 <br/>시작하기 전에 적용합니다.": "The controls list is <br/>optional and is applied <br/>before the camera starts if <br/>provided.", "stop#40;#41;은 캡처 세션을 <br/>종료합니다.": "stop#40;#41; terminates the <br/>capture session.", "선택적으로 제공한 <br/>controls는 시작 전에 <br/>적용합니다.": "Optional controls are <br/>applied before starting.", "애플리케이션은 stop#40;#41;으로 <br/>세션이 종료될 때까지 요청을 <br/>큐로 제출할 수 있습니다.": "The application can queue <br/>requests until stop#40;#41; ends <br/>the session.", "카메라가 Configured 상태일 <br/>때만 시작 함수를 호출할 수 <br/>있습니다.": "The start function may only <br/>be called when the camera <br/>is Configured.", "카메라가 시스템에서 연결 <br/>해제되었으면 시작 함수는 <br/>-ENODEV를 반환합니다.": "The start function returns <br/>-ENODEV if the camera is <br/>disconnected.", "카메라가 시작되면 <br/>애플리케이션은 요청을 큐로 <br/>제출할 수 있습니다.": "Once the camera starts, the <br/>application can queue <br/>requests.", "카메라가 시작되면 <br/>애플리케이션은 처리 후 <br/>자신에게 반환할 요청을 <br/>카메라에 큐로 제출할 수 <br/>있습니다.": "Once the camera starts, the <br/>application can queue <br/>requests for processing and <br/>return to it.", "카메라가 시작할 수 있는 <br/>상태가 아니면 시작 함수는 <br/>-EACCES를 반환합니다.": "The start function returns <br/>-EACCES if the camera <br/>cannot be started.", "호출자는 시작 함수를 카메라 <br/>상태에 영향을 주는 다른 <br/>함수와 동기화해야 합니다.": "The caller must synchronize <br/>the start function with <br/>other functions affecting <br/>camera state."}
  v_start["Camera::start는 카메라 캡처 <br/>세션을 시작합니다."]
  v_configured["카메라가 Configured 상태일 <br/>때만 시작 함수를 호출할 수 <br/>있습니다."]
  v_controls["controls 목록은 선택 <br/>사항이며 제공하면 카메라를 <br/>시작하기 전에 적용합니다."]
  v_caller["호출자는 시작 함수를 카메라 <br/>상태에 영향을 주는 다른 <br/>함수와 동기화해야 합니다."]
  v_enodev["-ENODEV는 카메라가 <br/>시스템에서 연결 <br/>해제되었음을 뜻합니다."]
  v_eacces["-EACCES는 카메라가 시작할 <br/>수 있는 상태가 아님을 <br/>뜻합니다."]
  v_requests["카메라가 시작되면 <br/>애플리케이션은 처리 후 <br/>자신에게 반환할 요청을 <br/>카메라에 큐로 제출할 수 <br/>있습니다."]
  v_stop["stop#40;#41;은 캡처 세션을 <br/>종료합니다."]
  v_configured -->|"Configured는 시작 함수 <br/>호출의 전제입니다."| v_start
  v_controls -->|"선택적으로 제공한 <br/>controls는 시작 전에 <br/>적용합니다."| v_start
  v_caller -->|"caller는 시작 함수를 카메라 <br/>상태에 영향을 주는 다른 <br/>함수와 동기화해야 합니다."| v_start
  v_start -->|"카메라가 시스템에서 연결 <br/>해제되었으면 시작 함수는 <br/>-ENODEV를 반환합니다."| v_enodev
  v_start -->|"카메라가 시작할 수 있는 <br/>상태가 아니면 시작 함수는 <br/>-EACCES를 반환합니다."| v_eacces
  v_start -->|"카메라가 시작되면 <br/>애플리케이션은 요청을 큐로 <br/>제출할 수 있습니다."| v_requests
  v_requests -->|"애플리케이션은 stop#40;#41;으로 <br/>세션이 종료될 때까지 요청을 <br/>큐로 제출할 수 있습니다."| v_stop
```

[Mermaid 원문](camera_start.item-session.mmd)

??? note "그림 근거와 확인 범위"
    Configured 전제와 선택적 제어값, 시작 오류, 요청 제출 및 stop은 캡처 세션에서 어떻게 연결되는가?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Camera::start starts a camera capture session.">Camera::start는 카메라 캡처 세션을 시작합니다.</span> | [src/libcamera/camera.cpp:1383](#source-1bb135021258e6a5) |
    | <span data-sdd-label-en="The start function may only be called when the camera is Configured.">카메라가 Configured 상태일 때만 시작 함수를 호출할 수 있습니다.</span> | [src/libcamera/camera.cpp:1383](#source-1bb135021258e6a5) |
    | <span data-sdd-label-en="The controls list is optional and is applied before the camera starts if provided.">controls 목록은 선택 사항이며 제공하면 카메라를 시작하기 전에 적용합니다.</span> | [src/libcamera/camera.cpp:1383](#source-1bb135021258e6a5) |
    | <span data-sdd-label-en="The caller must synchronize the start function with other functions affecting camera state.">호출자는 시작 함수를 카메라 상태에 영향을 주는 다른 함수와 동기화해야 합니다.</span> | [src/libcamera/camera.cpp:1383](#source-1bb135021258e6a5) |
    | <span data-sdd-label-en="-ENODEV means the camera has been disconnected from the system.">-ENODEV는 카메라가 시스템에서 연결 해제되었음을 뜻합니다.</span> | [src/libcamera/camera.cpp:1383](#source-1bb135021258e6a5) |
    | <span data-sdd-label-en="-EACCES means the camera is not in a state where it can be started.">-EACCES는 카메라가 시작할 수 있는 상태가 아님을 뜻합니다.</span> | [src/libcamera/camera.cpp:1383](#source-1bb135021258e6a5) |
    | <span data-sdd-label-en="Once the camera starts, the application can queue requests for processing and return to it.">카메라가 시작되면 애플리케이션은 처리 후 자신에게 반환할 요청을 카메라에 큐로 제출할 수 있습니다.</span> | [src/libcamera/camera.cpp:1383](#source-1bb135021258e6a5) |
    | <span data-sdd-label-en="stop() terminates the capture session.">stop&#40;&#41;은 캡처 세션을 종료합니다.</span> | [src/libcamera/camera.cpp:1383](#source-1bb135021258e6a5) |
    | <span data-sdd-label-en="Configured is a precondition for calling the start function.">Configured는 시작 함수 호출의 전제입니다.</span> | [src/libcamera/camera.cpp:1383](#source-1bb135021258e6a5) |
    | <span data-sdd-label-en="Optional controls are applied before starting.">선택적으로 제공한 controls는 시작 전에 적용합니다.</span> | [src/libcamera/camera.cpp:1383](#source-1bb135021258e6a5) |
    | <span data-sdd-label-en="The caller must synchronize start with other state-affecting functions.">caller는 시작 함수를 카메라 상태에 영향을 주는 다른 함수와 동기화해야 합니다.</span> | [src/libcamera/camera.cpp:1383](#source-1bb135021258e6a5) |
    | <span data-sdd-label-en="The start function returns -ENODEV if the camera is disconnected.">카메라가 시스템에서 연결 해제되었으면 시작 함수는 -ENODEV를 반환합니다.</span> | [src/libcamera/camera.cpp:1383](#source-1bb135021258e6a5) |
    | <span data-sdd-label-en="The start function returns -EACCES if the camera cannot be started.">카메라가 시작할 수 있는 상태가 아니면 시작 함수는 -EACCES를 반환합니다.</span> | [src/libcamera/camera.cpp:1383](#source-1bb135021258e6a5) |
    | <span data-sdd-label-en="Once the camera starts, the application can queue requests.">카메라가 시작되면 애플리케이션은 요청을 큐로 제출할 수 있습니다.</span> | [src/libcamera/camera.cpp:1383](#source-1bb135021258e6a5) |
    | <span data-sdd-label-en="The application can queue requests until stop() ends the session.">애플리케이션은 stop&#40;&#41;으로 세션이 종료될 때까지 요청을 큐로 제출할 수 있습니다.</span> | [src/libcamera/camera.cpp:1383](#source-1bb135021258e6a5) |
<!-- /sdd:visual:item-session -->

근거 원문: [src/libcamera/camera.cpp:1383](#source-1bb135021258e6a5)

## 시작 제어값과 파이프라인 결과 반영

`Camera::start`는 `controls`가 있으면 `ControlList` 복사본을 만들고 `patchControlList`로 전처리한 뒤 그 복사본을 전달하며, 없으면 `nullptr`을 전달합니다. 두 분기 모두 `PipelineHandler::start`를 `ConnectionTypeBlocking`으로 호출하며, 이 함수는 `CameraManager` 스레드에서 호출됩니다. `Camera::start`는 호출 결과인 `ret`이 0이 아니면 `CameraRunning` 상태를 설정하지 않고 `ret`을 그대로 반환합니다. `ret`이 0이면 `CameraRunning` 상태를 설정하고 0을 반환합니다. `src/libcamera/camera.cpp:1400`, `src/libcamera/pipeline_handler.cpp:343`

<!-- sdd:visual:item-activation -->
### 시작 제어값과 파이프라인 결과 반영의 관계와 경계

```mermaid
flowchart TB
%% sdd:translations {"ASSERT 코드 생성 여부는 <br/>NDEBUG 정의에 따라 <br/>달라집니다.": "ASSERT code generation <br/>depends on the NDEBUG <br/>definition.", "ASSERT가 활성화되어 있으면 <br/>requestSequence#95;가 0인지 <br/>검사합니다.": "When enabled, ASSERT checks <br/>whether requestSequence#95; is <br/>zero.", "ASSERT의 조건이 거짓이면 <br/>Fatal 오류를 기록하고 <br/>프로그램 실행을 중단합니다.": "If the ASSERT condition is <br/>false, it logs a Fatal <br/>error and aborts execution.", "CameraConfigured 접근 확인 <br/>결과가 음수인지 검사합니다.": "It checks whether the <br/>CameraConfigured access <br/>result is negative.", "PipelineHandler::start는 <br/>ConnectionTypeBlocking으로 <br/>호출되며 CameraManager <br/>스레드에서 실행됩니다.": "PipelineHandler::start runs <br/>on the CameraManager thread <br/>via ConnectionTypeBlocking.", "controls가 없으면 nullptr을 <br/>사용합니다. #91;false#93;": "If controls is absent, it <br/>uses nullptr. #91;false#93;", "controls가 없으면 nullptr을 <br/>전달합니다.": "It passes nullptr when <br/>controls is absent.", "controls가 있으면 복사하고 <br/>수정합니다. #91;true#93;": "If controls is present, it <br/>copies and patches it. <br/>#91;true#93;", "controls를 복사하고 copy에 <br/>patchControlList를 <br/>적용합니다.": "It copies controls and <br/>applies patchControlList to <br/>copy.", "controls의 유무에 따라 <br/>전달할 제어값을 정합니다.": "It chooses what to pass <br/>based on whether controls <br/>is present.", "log.h를 포함하기 전에 <br/>NDEBUG를 정의하면 ASSERT <br/>코드는 생성되지 않습니다.": "If NDEBUG is defined before <br/>including log.h, ASSERT <br/>generates no code.", "nullptr을 전달합니다. <br/>#91;false#93;": "It passes nullptr. #91;false#93;", "결과가 0이 아니면 그대로 <br/>반환합니다. #91;true#93;": "If the result is nonzero, <br/>it returns it unchanged. <br/>#91;true#93;", "결과가 0이면 상태를 <br/>Private::CameraRunning으로 <br/>갱신합니다.": "If the result is zero, it <br/>sets the state to <br/>Private::CameraRunning.", "결과가 0이면 상태를 <br/>갱신합니다. #91;false#93;": "If the result is zero, it <br/>updates the state. #91;false#93;", "결과가 음수가 아니면 <br/>ASSERT에 도달합니다. #91;false#93;": "If the result is not <br/>negative, execution reaches <br/>ASSERT. #91;false#93;", "수정한 copy의 주소를 <br/>전달합니다. #91;true#93;": "It passes the address of <br/>the patched copy. #91;true#93;", "실행이 계속되면 controls를 <br/>확인합니다.": "If execution continues, it <br/>checks controls.", "음수 결과를 그대로 <br/>반환합니다. #91;true#93;": "It returns the negative <br/>result unchanged. #91;true#93;", "접근 확인 결과가 음수이거나 <br/>파이프라인 결과가 0이 <br/>아니면 해당 결과를 그대로 <br/>반환합니다.": "It returns a negative <br/>access result or a nonzero <br/>pipeline result unchanged.", "파이프라인 호출 결과 ret이 <br/>0인지 검사합니다.": "It checks whether the <br/>pipeline call result ret is <br/>zero.", "호출 결과를 ret에 저장하고 <br/>검사합니다.": "It stores the call result <br/>in ret and checks it.", "활성화된 검사 조건이 <br/>거짓이면 실행을 중단합니다.": "If the enabled assertion is <br/>false, execution aborts."}
  v_access{"CameraConfigured 접근 확인 <br/>결과가 음수인지 검사합니다."}
  v_returned["접근 확인 결과가 음수이거나 <br/>파이프라인 결과가 0이 <br/>아니면 해당 결과를 그대로 <br/>반환합니다."]
  v_assertion["ASSERT가 활성화되어 있으면 <br/>requestSequence#95;가 0인지 <br/>검사합니다."]
  v_fatal["ASSERT의 조건이 거짓이면 <br/>Fatal 오류를 기록하고 <br/>프로그램 실행을 중단합니다."]
  v_ndebug["log.h를 포함하기 전에 <br/>NDEBUG를 정의하면 ASSERT <br/>코드는 생성되지 않습니다."]
  v_controls{"controls의 유무에 따라 <br/>전달할 제어값을 정합니다."}
  v_copy["controls를 복사하고 copy에 <br/>patchControlList를 <br/>적용합니다."]
  v_null["controls가 없으면 nullptr을 <br/>전달합니다."]
  v_invoke["PipelineHandler::start는 <br/>ConnectionTypeBlocking으로 <br/>호출되며 CameraManager <br/>스레드에서 실행됩니다."]
  v_result{"파이프라인 호출 결과 ret이 <br/>0인지 검사합니다."}
  v_running["결과가 0이면 상태를 <br/>Private::CameraRunning으로 <br/>갱신합니다."]
  v_access -->|"음수 결과를 그대로 <br/>반환합니다. #91;true#93;"| v_returned
  v_access -->|"결과가 음수가 아니면 <br/>ASSERT에 도달합니다. #91;false#93;"| v_assertion
  v_assertion -->|"활성화된 검사 조건이 <br/>거짓이면 실행을 중단합니다."| v_fatal
  v_assertion -->|"ASSERT 코드 생성 여부는 <br/>NDEBUG 정의에 따라 <br/>달라집니다."| v_ndebug
  v_assertion -->|"실행이 계속되면 controls를 <br/>확인합니다."| v_controls
  v_controls -->|"controls가 있으면 복사하고 <br/>수정합니다. #91;true#93;"| v_copy
  v_controls -->|"controls가 없으면 nullptr을 <br/>사용합니다. #91;false#93;"| v_null
  v_copy -->|"수정한 copy의 주소를 <br/>전달합니다. #91;true#93;"| v_invoke
  v_null -->|"nullptr을 전달합니다. <br/>#91;false#93;"| v_invoke
  v_invoke -->|"호출 결과를 ret에 저장하고 <br/>검사합니다."| v_result
  v_result -->|"결과가 0이 아니면 그대로 <br/>반환합니다. #91;true#93;"| v_returned
  v_result -->|"결과가 0이면 상태를 <br/>갱신합니다. #91;false#93;"| v_running
```

[Mermaid 원문](camera_start.item-activation.mmd)

??? note "그림 근거와 확인 범위"
    ASSERT, 제어값 분기, blocking 파이프라인 호출과 반환값 분기는 어떻게 원래 오류 반환 또는 CameraRunning 갱신으로 이어지는가?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="It checks whether the CameraConfigured access result is negative.">CameraConfigured 접근 확인 결과가 음수인지 검사합니다.</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) |
    | <span data-sdd-label-en="It returns a negative access result or a nonzero pipeline result unchanged.">접근 확인 결과가 음수이거나 파이프라인 결과가 0이 아니면 해당 결과를 그대로 반환합니다.</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) |
    | <span data-sdd-label-en="When enabled, ASSERT checks whether requestSequence_ is zero.">ASSERT가 활성화되어 있으면 requestSequence&#95;가 0인지 검사합니다.</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) · [src/libcamera/base/log.cpp:1022](#source-47a6ef3943a7b53c) |
    | <span data-sdd-label-en="If the ASSERT condition is false, it logs a Fatal error and aborts execution.">ASSERT의 조건이 거짓이면 Fatal 오류를 기록하고 프로그램 실행을 중단합니다.</span> | [src/libcamera/base/log.cpp:1022](#source-47a6ef3943a7b53c) |
    | <span data-sdd-label-en="If NDEBUG is defined before including log.h, ASSERT generates no code.">log.h를 포함하기 전에 NDEBUG를 정의하면 ASSERT 코드는 생성되지 않습니다.</span> | [src/libcamera/base/log.cpp:1022](#source-47a6ef3943a7b53c) |
    | <span data-sdd-label-en="It chooses what to pass based on whether controls is present.">controls의 유무에 따라 전달할 제어값을 정합니다.</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) |
    | <span data-sdd-label-en="It copies controls and applies patchControlList to copy.">controls를 복사하고 copy에 patchControlList를 적용합니다.</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) |
    | <span data-sdd-label-en="It passes nullptr when controls is absent.">controls가 없으면 nullptr을 전달합니다.</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) |
    | <span data-sdd-label-en="PipelineHandler::start runs on the CameraManager thread via ConnectionTypeBlocking.">PipelineHandler::start는 ConnectionTypeBlocking으로 호출되며 CameraManager 스레드에서 실행됩니다.</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) · [src/libcamera/pipeline_handler.cpp:343](#source-490ad21ef2a56108) |
    | <span data-sdd-label-en="It checks whether the pipeline call result ret is zero.">파이프라인 호출 결과 ret이 0인지 검사합니다.</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) |
    | <span data-sdd-label-en="If the result is zero, it sets the state to Private::CameraRunning.">결과가 0이면 상태를 Private::CameraRunning으로 갱신합니다.</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) |
    | <span data-sdd-label-en="It returns the negative result unchanged. · ret &lt; 0 [true]">음수 결과를 그대로 반환합니다. · ret &lt; 0 &#91;true&#93;</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) |
    | <span data-sdd-label-en="If the result is not negative, execution reaches ASSERT. · ret &lt; 0 [false]">결과가 음수가 아니면 ASSERT에 도달합니다. · ret &lt; 0 &#91;false&#93;</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) |
    | <span data-sdd-label-en="If the enabled assertion is false, execution aborts.">활성화된 검사 조건이 거짓이면 실행을 중단합니다.</span> | [src/libcamera/base/log.cpp:1022](#source-47a6ef3943a7b53c) |
    | <span data-sdd-label-en="ASSERT code generation depends on the NDEBUG definition.">ASSERT 코드 생성 여부는 NDEBUG 정의에 따라 달라집니다.</span> | [src/libcamera/base/log.cpp:1022](#source-47a6ef3943a7b53c) |
    | <span data-sdd-label-en="If execution continues, it checks controls.">실행이 계속되면 controls를 확인합니다.</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) · [src/libcamera/base/log.cpp:1022](#source-47a6ef3943a7b53c) |
    | <span data-sdd-label-en="If controls is present, it copies and patches it. · controls [true]">controls가 있으면 복사하고 수정합니다. · controls &#91;true&#93;</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) |
    | <span data-sdd-label-en="If controls is absent, it uses nullptr. · controls [false]">controls가 없으면 nullptr을 사용합니다. · controls &#91;false&#93;</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) |
    | <span data-sdd-label-en="It passes the address of the patched copy. · controls [true]">수정한 copy의 주소를 전달합니다. · controls &#91;true&#93;</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) |
    | <span data-sdd-label-en="It passes nullptr. · controls [false]">nullptr을 전달합니다. · controls &#91;false&#93;</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) |
    | <span data-sdd-label-en="It stores the call result in ret and checks it.">호출 결과를 ret에 저장하고 검사합니다.</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) |
    | <span data-sdd-label-en="If the result is nonzero, it returns it unchanged. · ret [true]">결과가 0이 아니면 그대로 반환합니다. · ret &#91;true&#93;</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) |
    | <span data-sdd-label-en="If the result is zero, it updates the state. · ret [false]">결과가 0이면 상태를 갱신합니다. · ret &#91;false&#93;</span> | [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) |
<!-- /sdd:visual:item-activation -->

`Camera::start`는 `PipelineHandler::start`를 호출하기 전에 `ASSERT(d->requestSequence_ == 0)`을 실행합니다. 이 검사가 실패하면 `ASSERT`는 오류 메시지를 `Fatal` 로그 수준으로 기록하고 프로그램 실행을 중단하며, 일반 오류 반환과는 다르게 동작합니다. `log.h`를 포함하기 전에 `NDEBUG`가 정의되면 `ASSERT`는 코드를 생성하지 않습니다. `src/libcamera/camera.cpp:1400`, `src/libcamera/base/log.cpp:1022`

근거 원문: [src/libcamera/camera.cpp:1400](#source-05691b4c81e7ee1c) · [src/libcamera/pipeline_handler.cpp:343](#source-490ad21ef2a56108) · [src/libcamera/base/log.cpp:1022](#source-47a6ef3943a7b53c)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | Camera::start()의 캡처 세션 시작 목적, 선택 controls가 시작 전에 적용된다는 API 계약과 성공 뒤 요청 제출이 가능하고 stop까지 세션이 이어지는 범위를 설명하세요. Configured 상태 전제, 다른 상태 변경 함수와 호출자의 동기화 의무, 연결 해제·잘못된 상태 오류를 관련 조건과 함께 설명하세요. 숫자 성공 반환과 파이프라인 반환 전파는 다음 절에서만 설명하므로 반복하지 마세요. 두 문단 이내로 작성하세요. | [요청을 제출할 캡처 세션을 시작하기](#요청을-제출할-캡처-세션을-시작하기) | 코드 근거와 설명 연결 |
    | controls가 있으면 복사본을 patchControlList로 전처리하고 없으면 nullptr인 차이를 한 문단에서 설명하세요. 이 두 분기를 묶어 PipelineHandler::start를 ConnectionTypeBlocking으로 호출하고 CameraManager 스레드에서 처리한다는 계약을 설명하세요. ret이 0이 아니면 그대로 반환하여 CameraRunning을 갱신하지 않고 성공일 때만 CameraRunning과 0 반환에 도달하는 흐름을 한 번 설명하세요. requestSequence_==0 ASSERT를 일반 오류 반환과 구분하고, log.h를 포함하기 전에 NDEBUG가 정의되면 ASSERT 코드가 생성되지 않는다는 조건을 소스 계약으로 설명하세요. 소스에 없는 정보가 무엇인지를 설명하는 문단은 쓰지 마세요. 세 문단 이내로 작성하세요. 일반적인 ASSERT 사용 권고는 이 절의 범위에서 제외하고 실제 검사식과 NDEBUG 조건만 설명하세요. 권고를 의무로 바꾸지 마세요. ret 분기는 오류 경로 한 문장과 성공 경로 한 문장으로만 쓰고, 따라서·즉으로 시작하는 결과 요약을 덧붙이지 마세요. | [시작 제어값과 파이프라인 결과 반영](#시작-제어값과-파이프라인-결과-반영) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-1bb135021258e6a5"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1383"
    `src/libcamera/camera.cpp:1383`에서 시작하는 발췌입니다. 종료 줄은 1399이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `9121c6f5bd2e73de134af571dd2a8a2089f052b08739b10519bdf9433ea1b2b9`
    
    ```text
    \brief Start capture from camera
     * \param[in] controls Controls to be applied before starting the Camera
     *
     * Start the camera capture session, optionally providing a list of controls to
     * apply before starting. Once the camera is started the application can queue
     * requests to the camera to process and return to the application until the
     * capture session is terminated with \a stop().
     *
     * \context This function may only be called when the camera is in the
     * Configured state as defined in \ref camera_operation, and shall be
     * synchronized by the caller with other functions that affect the camera
     * state.
     *
     * \return 0 on success or a negative error code otherwise
     * \retval -ENODEV The camera has been disconnected from the system
     * \retval -EACCES The camera is not in a state where it can be started
     */
    ```

<a id="source-05691b4c81e7ee1c"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1400"
    `src/libcamera/camera.cpp:1400`에서 시작하는 발췌입니다. 종료 줄은 1428이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `a440ed27d1a8c891ff25f542252c50f9fc3040df4cc04346bf771ee8e4e54b73`
    
    ```text
    int Camera::start(const ControlList *controls)
    {
    	Private *const d = _d();
    
    	int ret = d->isAccessAllowed(Private::CameraConfigured);
    	if (ret < 0)
    		return ret;
    
    	LOG(Camera, Debug) << "Starting capture";
    
    	ASSERT(d->requestSequence_ == 0);
    
    	if (controls) {
    		ControlList copy(*controls);
    		patchControlList(copy);
    		ret = d->pipe_->invokeMethod(&PipelineHandler::start,
    					     ConnectionTypeBlocking, this, &copy);
    	} else {
    		ret = d->pipe_->invokeMethod(&PipelineHandler::start,
    					     ConnectionTypeBlocking, this, nullptr);
    	}
    
    	if (ret)
    		return ret;
    
    	d->setState(Private::CameraRunning);
    
    	return 0;
    }
    ```

<a id="source-490ad21ef2a56108"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:343"
    `src/libcamera/pipeline_handler.cpp:343`에서 시작하는 발췌입니다. 종료 줄은 356이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `ea0201de61631e8e9551d0c94503e5b000439f9b1a1242dded9abeb9b5870c2e`
    
    ```text
    \fn PipelineHandler::start()
     * \brief Start capturing from a group of streams
     * \param[in] camera The camera to start
     * \param[in] controls Controls to be applied before starting the Camera
     *
     * Start the group of streams that have been configured for capture by
     * \a configure(). The intended caller of this function is the Camera class
     * which will in turn be called from the application to indicate that it has
     * configured the streams and is ready to capture.
     *
     * \context This function is called from the CameraManager thread.
     *
     * \return 0 on success or a negative error code otherwise
     */
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
| 시작 요청 대상 | `Camera` → `PipelineHandler::start()` | 메서드 전달 대상이며 동기·비동기 여부는 호출부에서 확인해야 합니다. | `src/libcamera/camera.cpp:1415`, `src/libcamera/camera.cpp:1418` |
| 상태 반영 | `Camera` → `Private::setState()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1425` |

## 주요 호출 관계

화살표는 호출 측과 대상을 연결합니다. 시간 순서나 모든 경로의 실행을 뜻하지 않습니다. 점선에는 가상 호출 후보·예약 대상 등 확인이 필요한 관계를 표시합니다.

```mermaid
flowchart LR
  p0["Camera"]
  p1["PipelineHandler"]
  p2["Private"]
  p0 -.->|"start#40;#41; · 예약된 호출, 실행 순서는 정적으로 확인 불가"| p1
  p0 -->|"setState#40;#41;"| p2
```

## 추적 범위와 경계

요약의 hide 규칙에 해당하는 호출은 27개입니다. 전체 추적 기록에는 해당 호출도 모두 보존합니다. 기록 번호는 정적 탐색의 식별자이며 실행 순번이 아닙니다.

조건 분기, 반복 횟수와 실제 실행 스레드는 이 호출 목록만으로 확정할 수 없습니다. 가상 호출 후보는 실제 객체에 따라 선택됩니다. 예약 표시는 인자로 전달한 메서드 대상을 뜻하며, 비동기 실행을 보증하지 않습니다. 호출부의 연결 방식과 동기화 계약을 확인해야 합니다.

| 호출 지점 | 후보 또는 예약 대상 | 확인할 경계 | 근거 |
|---|---|---|---|
| `Camera` | `PipelineHandler::start()` | 메서드 전달 대상이며 동기·비동기 여부는 호출부에서 확인해야 합니다. | `src/libcamera/camera.cpp:1415` |
| `Camera` | `PipelineHandler::start()` | 메서드 전달 대상이며 동기·비동기 여부는 호출부에서 확인해야 합니다. | `src/libcamera/camera.cpp:1418` |

추출 통계: 미해결 호출 0개, 예약된 호출 2개입니다.

## 전체 추적 기록

아래 구간을 펼치면 요약에서 제외된 호출까지 확인할 수 있습니다. 이 목록은 추출 깊이 안에서 수집한 기록이며, 소스의 모든 실행 경로를 포함한다는 뜻은 아닙니다.

??? note "추적 기록 1–25 / 48개"

    | 기록 | 호출 측 | 대상 | 구분 | 근거 |
    |---|---|---|---|---|
    | 1 | `Camera` | `Camera::_d()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1402` |
    | 2 | `Camera` | `Private::isAccessAllowed()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1404` |
    | 3 | `Private` | `log::isLogSeverityEnabled()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:700` |
    | 4 | `Private` | `LogMessageAbortGuard::LogMessageAbortGuard()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:700` |
    | 5 | `Private` | `LogMessage::stream()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:700` |
    | 6 | `Private` | `log::_log()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:700` |
    | 7 | `log` | `LogMessage::LogMessage()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:990` |
    | 8 | `LogMessage` | `utils::basename()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:858` |
    | 9 | `Private` | `log::isLogSeverityEnabled()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:702` |
    | 10 | `Private` | `LogMessageAbortGuard::LogMessageAbortGuard()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:702` |
    | 11 | `Private` | `LogMessage::stream()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:702` |
    | 12 | `Private` | `log::_log()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:702` |
    | 13 | `log` | `LogMessage::LogMessage()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:990` |
    | 14 | `LogMessage` | `utils::basename()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:858` |
    | 15 | `Camera` | `log::isLogSeverityEnabled()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1408` |
    | 16 | `Camera` | `LogMessageAbortGuard::LogMessageAbortGuard()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1408` |
    | 17 | `Camera` | `LogMessage::stream()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1408` |
    | 18 | `Camera` | `log::_log()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1408` |
    | 19 | `log` | `LogMessage::LogMessage()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:990` |
    | 20 | `LogMessage` | `utils::basename()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:858` |
    | 21 | `Camera` | `log::isLogSeverityEnabled()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1410` |
    | 22 | `Camera` | `LogMessageAbortGuard::LogMessageAbortGuard()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1410` |
    | 23 | `Camera` | `LogMessage::stream()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1410` |
    | 24 | `Camera` | `log::_log()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1410` |
    | 25 | `log` | `LogMessage::LogMessage()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:990` |

??? note "추적 기록 26–48 / 48개"

    | 기록 | 호출 측 | 대상 | 구분 | 근거 |
    |---|---|---|---|---|
    | 26 | `LogMessage` | `utils::basename()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:858` |
    | 27 | `Camera` | `ControlList::ControlList()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1413` |
    | 28 | `Camera` | `Camera::patchControlList()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1414` |
    | 29 | `Camera` | `ControlList::get()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1289` |
    | 30 | `Camera` | `ControlInfoMap::count()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1291` |
    | 31 | `ControlInfoMap` | `ControlInfoMap::find()` | 정적 호출 지점입니다. | `src/libcamera/controls.cpp:864` |
    | 32 | `Camera` | `Camera::_d()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1291` |
    | 33 | `Camera` | `ControlId::id()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1291` |
    | 34 | `Camera` | `ControlList::contains()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1292` |
    | 35 | `Camera` | `ControlId::id()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1292` |
    | 36 | `Camera` | `ControlList::set()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1293` |
    | 37 | `Camera` | `ControlInfoMap::count()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1298` |
    | 38 | `ControlInfoMap` | `ControlInfoMap::find()` | 정적 호출 지점입니다. | `src/libcamera/controls.cpp:864` |
    | 39 | `Camera` | `Camera::_d()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1298` |
    | 40 | `Camera` | `ControlId::id()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1298` |
    | 41 | `Camera` | `ControlList::contains()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1299` |
    | 42 | `Camera` | `ControlId::id()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1299` |
    | 43 | `Camera` | `ControlList::set()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1300` |
    | 44 | `Camera` | `Object::invokeMethod()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1415` |
    | 45 | `Camera` | `PipelineHandler::start()` | 메서드 전달 대상이며 동기·비동기 여부는 호출부에서 확인해야 합니다. | `src/libcamera/camera.cpp:1415` |
    | 46 | `Camera` | `Object::invokeMethod()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1418` |
    | 47 | `Camera` | `PipelineHandler::start()` | 메서드 전달 대상이며 동기·비동기 여부는 호출부에서 확인해야 합니다. | `src/libcamera/camera.cpp:1418` |
    | 48 | `Camera` | `Private::setState()` | 정적 호출 지점입니다. | `src/libcamera/camera.cpp:1425` |

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `src/libcamera/base/log.cpp`, `src/libcamera/camera.cpp`, `src/libcamera/controls.cpp`, `src/libcamera/pipeline_handler.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `293d751a81`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-04 · 사람 검토 전

다음 단계: [요청 제출](queue_request.md)
