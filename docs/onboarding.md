---
generated_at: 2026-11-04 05:02:45+00:00
source_commit: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
status: ok
section: onboarding
generation_method: facts-and-llm
evidence_fingerprint: 87424992956beb9f6d59f825944a1136a38c1acb800575d2fa4c87daf994a388
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design:
  schema: 1
  input_fingerprint: 87424992956beb9f6d59f825944a1136a38c1acb800575d2fa4c87daf994a388
  answers:
    try:
    - text: 시스템에서 감지된 카메라 목록은 `cam -l`로 확인하고, 첫 번째 카메라에서 10프레임을 캡처해 디스크에 저장하려면 `cam
        -c 1 --capture=10 --file`을 사용합니다. 문제가 발생하면 `LIBCAMERA_LOG_LEVELS=*:DEBUG cam
        -l`로 상세한 libcamera 디버그 로그를 얻을 수 있습니다.
      evidence:
      - cam
      covers:
      - try
      kind: behavior
      quote: "The ``cam`` utility can be used for basic testing. You can list the\
        \ cameras\ndetected on the system with ``cam -l``, and capture ten frames\
        \ from the first\ncamera and save them to disk with ``cam -c 1 --capture=10\
        \ --file``. See\n``cam -h`` for more information about the ``cam`` tool.\n\
        \nIn case of problems, a detailed debug log can be obtained from libcamera\
        \ by\nsetting the ``LIBCAMERA_LOG_LEVELS`` environment variable:\n\n.. code::\n\
        \n    :~$ LIBCAMERA_LOG_LEVELS=*:DEBUG cam -l"
      part_id: steps
    why:
    - text: 애플리케이션은 createRequest()로 요청을 할당한 후 queueRequest를 호출하기 전에 캡처 버퍼를 하나 이상
        채워야 합니다. 버퍼가 없는 요청은 유효하지 않아 큐에 들어가지 않고 거부됩니다. 요청이 큐에 들어간 후 카메라는 requestCompleted
        시그널을 통해 완료를 알립니다.
      evidence:
      - accept
      covers:
      - why
      kind: behavior
      quote: "This function queues a \\a request to the camera for capture.\n *\n\
        \ * After allocating the request with createRequest(), the application shall\n\
        \ * fill it with at least one capture buffer before queuing it. Requests that\n\
        \ * contain no buffers are invalid and are rejected without being queued.\n\
        \ *\n * Once the request has been queued, the camera will notify its completion\n\
        \ * through the \\ref requestCompleted signal."
      part_id: accept
    - text: 파이프라인 핸들러가 completeBuffer를 호출해 요청의 마지막 버퍼가 완료되었음을 알리더라도, 그 시점에 요청은 자동으로
        완료되지 않습니다. 이는 파이프라인 핸들러가 여전히 필요할 수 있는 작업을 수행할 기회를 주기 위한 것이며, 핸들러는 completeRequest()로
        요청을 명시적으로 완료해야 합니다.
      evidence:
      - buffer
      covers:
      - why
      kind: behavior
      quote: "This function shall be called by pipeline handlers to signal completion\
        \ of\n * the \\a buffer part of the \\a request. It notifies applications\
        \ of buffer\n * completion and updates the request's internal buffer tracking.\
        \ The request\n * is not completed automatically when the last buffer completes\
        \ to give\n * pipeline handlers a chance to perform any operation that may\
        \ still be\n * needed. They shall complete requests explicitly with completeRequest()."
      part_id: buffer
    - text: 요청은 제출된 순서대로 애플리케이션에 반환되며, 파이프라인 핸들러는 순서 제약 없이 완료된 요청에 대해 completeRequest()를
        호출할 수 있습니다.
      evidence:
      - order
      covers:
      - why
      kind: behavior
      quote: "The pipeline handler shall call this function to notify the \\a camera\
        \ that\n * the request has completed. The request is no longer managed by\
        \ the pipeline\n * handler and shall not be accessed once this function returns.\n\
        \ *\n * This function ensures that requests will be returned to the application\
        \ in\n * submission order, the pipeline handler may call it on any complete\
        \ request\n * without any ordering constraint."
      part_id: order
  topic_inputs:
    try: f1330202e4f8be9faf6a194b2518d761bd3cf790a432f0e53d787e2dc562a692
    why: 14526615e52156ee29a02bbff1677b8ed1162f905a5e318d1d23064771318325
  reused_topics:
  - try
  - why
  replayed_units: []
  generated_topics: []
  topic_agents:
    try: cli/codex/gpt-6.1-terra
    why: cli/codex/gpt-6.1-terra
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
    body_sha256: 39d209c45e22da9bc2d2b6a32d82c0d41db89a82fd81d74feecf42049a1dae31
    topics:
    - try
    - why
    validation: current source, contract and editorial checks; human review pending
  body_sha256: 9bc413e0fa4cf38092682fa012da4c1ab39c6420332e1902b9fbe634f6fa8040
generated_visuals:
  schema: 1
  records:
    request-completion-contract:
      input_fingerprint: dda3f29fafc54cdad1b109bd79e5223477425d47a9bc17a1f59c8344cf4771e1
      draft:
        nodes:
        - id: submission
          symbol: request
          label: 앱은 제출 전에 request에 캡처 버퍼를 하나 이상 넣어야 합니다. 버퍼가 없으면 요청은 큐에 들어가지 못합니다.
          label_en: The app must add a capture buffer before submission; a bufferless
            request is rejected.
          shape: process
          quote_ids:
          - accept:0
        - id: buffer
          symbol: buffer
          label: completeBuffer는 버퍼 완료를 알립니다. 마지막 버퍼가 완료되어도 요청은 자동으로 완료되지 않습니다.
          label_en: completeBuffer signals buffer completion; the last buffer does
            not complete the request.
          shape: process
          quote_ids:
          - buffer:0
        - id: explicit
          symbol: completeRequest
          label: 핸들러는 필요한 후속 작업을 할 기회를 가진 뒤 completeRequest를 명시적으로 호출해야 합니다. 반환 후에는
            요청에 접근하면 안 됩니다.
          label_en: Handlers can perform needed work and must call completeRequest.
            No access is allowed after it returns.
          shape: process
          quote_ids:
          - buffer:0
          - order:0
        - id: application
          symbol: application
          label: 핸들러의 completeRequest 호출 순서에는 제약이 없지만, 요청은 원래 제출 순서로 앱에 돌아갑니다.
          label_en: Calls have no ordering constraint; requests return to the app
            in submission order.
          shape: box
          quote_ids:
          - buffer:0
          - order:0
        - id: notification
          symbol: requestCompleted
          label: 큐에 들어간 요청이 완료되면 카메라는 requestCompleted 신호로 알립니다.
          label_en: The camera signals completion of a queued request via requestCompleted.
          shape: box
          quote_ids:
          - accept:0
        edges:
        - from: submission
          to: buffer
          label: 버퍼가 있는 요청을 큐에 넣으면 핸들러가 버퍼 완료를 알립니다.
          label_en: Handlers signal completion of a queued request's buffer.
          condition_ref: always
          quote_ids:
          - accept:0
          - buffer:0
        - from: buffer
          to: explicit
          label: 버퍼 완료 후에도 핸들러가 요청을 명시적으로 완료해야 합니다.
          label_en: Handlers must explicitly complete the request.
          condition_ref: always
          quote_ids:
          - buffer:0
        - from: explicit
          to: application
          label: 핸들러의 호출 순서와 관계없이 앱에는 제출 순서로 반환됩니다.
          label_en: Requests return to the app in submission order.
          condition_ref: always
          quote_ids:
          - buffer:0
          - order:0
        - from: explicit
          to: notification
          label: 핸들러가 요청 완료를 알리면 카메라는 완료 신호로 앱에 알립니다.
          label_en: The camera signals the request's completion.
          condition_ref: always
          quote_ids:
          - buffer:0
          - accept:0
          - order:0
      graph:
        id: request-completion-contract
        topic: why
        kind: flow
        title: 요청 제출과 버퍼·요청 완료의 책임
        question: 요청의 제출 조건, 버퍼 완료와 명시적 요청 완료, 앱에 전달하는 순서는 어떻게 연결됩니까?
        nodes:
        - id: submission
          label: 앱은 제출 전에 request에 캡처 버퍼를 하나 이상 넣어야 합니다. 버퍼가 없으면 요청은 큐에 들어가지 못합니다.
          label_en: The app must add a capture buffer before submission; a bufferless
            request is rejected.
          shape: box
          evidence:
          - source: why/accept
            sha256: e28ed33dec85a5e783457be419afac5b7c646b588c24bc311d46265b1ae7f37a
            quote: "This function queues a \\a request to the camera for capture.\n\
              \ *\n * After allocating the request with createRequest(), the application\
              \ shall\n * fill it with at least one capture buffer before queuing\
              \ it. Requests that\n * contain no buffers are invalid and are rejected\
              \ without being queued.\n *\n * Once the request has been queued, the\
              \ camera will notify its completion\n * through the \\ref requestCompleted\
              \ signal."
        - id: buffer
          label: completeBuffer는 버퍼 완료를 알립니다. 마지막 버퍼가 완료되어도 요청은 자동으로 완료되지 않습니다.
          label_en: completeBuffer signals buffer completion; the last buffer does
            not complete the request.
          shape: box
          evidence:
          - source: why/buffer
            sha256: dc60b6f028df4f7341facfcbd3ebade17f81bb4d2e72ce580ba93c7a1c449b42
            quote: "This function shall be called by pipeline handlers to signal completion\
              \ of\n * the \\a buffer part of the \\a request. It notifies applications\
              \ of buffer\n * completion and updates the request's internal buffer\
              \ tracking. The request\n * is not completed automatically when the\
              \ last buffer completes to give\n * pipeline handlers a chance to perform\
              \ any operation that may still be\n * needed. They shall complete requests\
              \ explicitly with completeRequest()."
        - id: explicit
          label: 핸들러는 필요한 후속 작업을 할 기회를 가진 뒤 completeRequest를 명시적으로 호출해야 합니다. 반환 후에는
            요청에 접근하면 안 됩니다.
          label_en: Handlers can perform needed work and must call completeRequest.
            No access is allowed after it returns.
          shape: box
          evidence:
          - source: why/buffer
            sha256: dc60b6f028df4f7341facfcbd3ebade17f81bb4d2e72ce580ba93c7a1c449b42
            quote: "This function shall be called by pipeline handlers to signal completion\
              \ of\n * the \\a buffer part of the \\a request. It notifies applications\
              \ of buffer\n * completion and updates the request's internal buffer\
              \ tracking. The request\n * is not completed automatically when the\
              \ last buffer completes to give\n * pipeline handlers a chance to perform\
              \ any operation that may still be\n * needed. They shall complete requests\
              \ explicitly with completeRequest()."
          - source: why/order
            sha256: 5df554f7462852344c1f8f25dd3bf2f16f22ab34e3f96d948d54ec44baca7217
            quote: "The pipeline handler shall call this function to notify the \\\
              a camera that\n * the request has completed. The request is no longer\
              \ managed by the pipeline\n * handler and shall not be accessed once\
              \ this function returns.\n *\n * This function ensures that requests\
              \ will be returned to the application in\n * submission order, the pipeline\
              \ handler may call it on any complete request\n * without any ordering\
              \ constraint."
        - id: application
          label: 핸들러의 completeRequest 호출 순서에는 제약이 없지만, 요청은 원래 제출 순서로 앱에 돌아갑니다.
          label_en: Calls have no ordering constraint; requests return to the app
            in submission order.
          shape: box
          evidence:
          - source: why/buffer
            sha256: dc60b6f028df4f7341facfcbd3ebade17f81bb4d2e72ce580ba93c7a1c449b42
            quote: "This function shall be called by pipeline handlers to signal completion\
              \ of\n * the \\a buffer part of the \\a request. It notifies applications\
              \ of buffer\n * completion and updates the request's internal buffer\
              \ tracking. The request\n * is not completed automatically when the\
              \ last buffer completes to give\n * pipeline handlers a chance to perform\
              \ any operation that may still be\n * needed. They shall complete requests\
              \ explicitly with completeRequest()."
          - source: why/order
            sha256: 5df554f7462852344c1f8f25dd3bf2f16f22ab34e3f96d948d54ec44baca7217
            quote: "The pipeline handler shall call this function to notify the \\\
              a camera that\n * the request has completed. The request is no longer\
              \ managed by the pipeline\n * handler and shall not be accessed once\
              \ this function returns.\n *\n * This function ensures that requests\
              \ will be returned to the application in\n * submission order, the pipeline\
              \ handler may call it on any complete request\n * without any ordering\
              \ constraint."
        - id: notification
          label: 큐에 들어간 요청이 완료되면 카메라는 requestCompleted 신호로 알립니다.
          label_en: The camera signals completion of a queued request via requestCompleted.
          shape: box
          evidence:
          - source: why/accept
            sha256: e28ed33dec85a5e783457be419afac5b7c646b588c24bc311d46265b1ae7f37a
            quote: "This function queues a \\a request to the camera for capture.\n\
              \ *\n * After allocating the request with createRequest(), the application\
              \ shall\n * fill it with at least one capture buffer before queuing\
              \ it. Requests that\n * contain no buffers are invalid and are rejected\
              \ without being queued.\n *\n * Once the request has been queued, the\
              \ camera will notify its completion\n * through the \\ref requestCompleted\
              \ signal."
        edges:
        - from: submission
          to: buffer
          label: 버퍼가 있는 요청을 큐에 넣으면 핸들러가 버퍼 완료를 알립니다.
          label_en: Handlers signal completion of a queued request's buffer.
          evidence:
          - source: why/accept
            sha256: e28ed33dec85a5e783457be419afac5b7c646b588c24bc311d46265b1ae7f37a
            quote: "This function queues a \\a request to the camera for capture.\n\
              \ *\n * After allocating the request with createRequest(), the application\
              \ shall\n * fill it with at least one capture buffer before queuing\
              \ it. Requests that\n * contain no buffers are invalid and are rejected\
              \ without being queued.\n *\n * Once the request has been queued, the\
              \ camera will notify its completion\n * through the \\ref requestCompleted\
              \ signal."
          - source: why/buffer
            sha256: dc60b6f028df4f7341facfcbd3ebade17f81bb4d2e72ce580ba93c7a1c449b42
            quote: "This function shall be called by pipeline handlers to signal completion\
              \ of\n * the \\a buffer part of the \\a request. It notifies applications\
              \ of buffer\n * completion and updates the request's internal buffer\
              \ tracking. The request\n * is not completed automatically when the\
              \ last buffer completes to give\n * pipeline handlers a chance to perform\
              \ any operation that may still be\n * needed. They shall complete requests\
              \ explicitly with completeRequest()."
        - from: buffer
          to: explicit
          label: 버퍼 완료 후에도 핸들러가 요청을 명시적으로 완료해야 합니다.
          label_en: Handlers must explicitly complete the request.
          evidence:
          - source: why/buffer
            sha256: dc60b6f028df4f7341facfcbd3ebade17f81bb4d2e72ce580ba93c7a1c449b42
            quote: "This function shall be called by pipeline handlers to signal completion\
              \ of\n * the \\a buffer part of the \\a request. It notifies applications\
              \ of buffer\n * completion and updates the request's internal buffer\
              \ tracking. The request\n * is not completed automatically when the\
              \ last buffer completes to give\n * pipeline handlers a chance to perform\
              \ any operation that may still be\n * needed. They shall complete requests\
              \ explicitly with completeRequest()."
        - from: explicit
          to: application
          label: 핸들러의 호출 순서와 관계없이 앱에는 제출 순서로 반환됩니다.
          label_en: Requests return to the app in submission order.
          evidence:
          - source: why/buffer
            sha256: dc60b6f028df4f7341facfcbd3ebade17f81bb4d2e72ce580ba93c7a1c449b42
            quote: "This function shall be called by pipeline handlers to signal completion\
              \ of\n * the \\a buffer part of the \\a request. It notifies applications\
              \ of buffer\n * completion and updates the request's internal buffer\
              \ tracking. The request\n * is not completed automatically when the\
              \ last buffer completes to give\n * pipeline handlers a chance to perform\
              \ any operation that may still be\n * needed. They shall complete requests\
              \ explicitly with completeRequest()."
          - source: why/order
            sha256: 5df554f7462852344c1f8f25dd3bf2f16f22ab34e3f96d948d54ec44baca7217
            quote: "The pipeline handler shall call this function to notify the \\\
              a camera that\n * the request has completed. The request is no longer\
              \ managed by the pipeline\n * handler and shall not be accessed once\
              \ this function returns.\n *\n * This function ensures that requests\
              \ will be returned to the application in\n * submission order, the pipeline\
              \ handler may call it on any complete request\n * without any ordering\
              \ constraint."
        - from: explicit
          to: notification
          label: 핸들러가 요청 완료를 알리면 카메라는 완료 신호로 앱에 알립니다.
          label_en: The camera signals the request's completion.
          evidence:
          - source: why/buffer
            sha256: dc60b6f028df4f7341facfcbd3ebade17f81bb4d2e72ce580ba93c7a1c449b42
            quote: "This function shall be called by pipeline handlers to signal completion\
              \ of\n * the \\a buffer part of the \\a request. It notifies applications\
              \ of buffer\n * completion and updates the request's internal buffer\
              \ tracking. The request\n * is not completed automatically when the\
              \ last buffer completes to give\n * pipeline handlers a chance to perform\
              \ any operation that may still be\n * needed. They shall complete requests\
              \ explicitly with completeRequest()."
          - source: why/accept
            sha256: e28ed33dec85a5e783457be419afac5b7c646b588c24bc311d46265b1ae7f37a
            quote: "This function queues a \\a request to the camera for capture.\n\
              \ *\n * After allocating the request with createRequest(), the application\
              \ shall\n * fill it with at least one capture buffer before queuing\
              \ it. Requests that\n * contain no buffers are invalid and are rejected\
              \ without being queued.\n *\n * Once the request has been queued, the\
              \ camera will notify its completion\n * through the \\ref requestCompleted\
              \ signal."
          - source: why/order
            sha256: 5df554f7462852344c1f8f25dd3bf2f16f22ab34e3f96d948d54ec44baca7217
            quote: "The pipeline handler shall call this function to notify the \\\
              a camera that\n * the request has completed. The request is no longer\
              \ managed by the pipeline\n * handler and shall not be accessed once\
              \ this function returns.\n *\n * This function ensures that requests\
              \ will be returned to the application in\n * submission order, the pipeline\
              \ handler may call it on any complete request\n * without any ordering\
              \ constraint."
        producer: cli/codex/gpt-6.1-terra
      producer: cli/codex/gpt-6.1-terra
      generation_commit: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61
      reused: true
      citation_binding_revalidation:
        policy: identifier-and-guard-boundaries-v2
        original_input_fingerprint: dda3f29fafc54cdad1b109bd79e5223477425d47a9bc17a1f59c8344cf4771e1
        new_inference: false
  body_sha256: 9bc413e0fa4cf38092682fa012da4c1ab39c6420332e1902b9fbe634f6fa8040
revalidated_from: be7e83e91348250c015aad6d6f59f1468555bae8
---

# 실행해 보고 설계 이유 읽기

**먼저 cam 도구로 카메라를 확인한 뒤, 요청 접수와 완료가 나뉜 이유를 소스 주석에서 읽으세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 시스템에서 감지된 카메라 목록은 `cam -l`로 확인하고, 첫 번째 카메라에서 10프레임을 캡처해 디스크에 저장하려면 `cam -c 1 --capture=10 --file`을 사용합니다. | [직접 실행해 보기](#직접-실행해-보기) |
| 애플리케이션은 createRequest()로 요청을 할당한 후 queueRequest를 호출하기 전에 캡처 버퍼를 하나 이상 채워야 합니다. | [요청 접수와 완료를 나눈 이유](#요청-접수와-완료를-나눈-이유) |

## 직접 실행해 보기

시스템에서 감지된 카메라 목록은 `cam -l`로 확인하고, 첫 번째 카메라에서 10프레임을 캡처해 디스크에 저장하려면 `cam -c 1 --capture=10 --file`을 사용합니다. 문제가 발생하면 `LIBCAMERA_LOG_LEVELS=*:DEBUG cam -l`로 상세한 libcamera 디버그 로그를 얻을 수 있습니다. `README.rst:107`

근거 원문: [README.rst:107](#source-5bc9ee57c1b6daee)

## 요청 접수와 완료를 나눈 이유

애플리케이션은 createRequest()로 요청을 할당한 후 queueRequest를 호출하기 전에 캡처 버퍼를 하나 이상 채워야 합니다. 버퍼가 없는 요청은 유효하지 않아 큐에 들어가지 않고 거부됩니다. 요청이 큐에 들어간 후 카메라는 requestCompleted 시그널을 통해 완료를 알립니다. `src/libcamera/camera.cpp:1311`

<!-- sdd:visual:request-completion-contract -->
### 요청 제출과 버퍼·요청 완료의 책임

```mermaid
flowchart TB
%% sdd:translations {"completeBuffer는 버퍼 <br/>완료를 알립니다. 마지막 <br/>버퍼가 완료되어도 요청은 <br/>자동으로 완료되지 않습니다.": "completeBuffer signals <br/>buffer completion; the last <br/>buffer does not complete <br/>the request.", "버퍼 완료 후에도 핸들러가 <br/>요청을 명시적으로 완료해야 <br/>합니다.": "Handlers must explicitly <br/>complete the request.", "버퍼가 있는 요청을 큐에 <br/>넣으면 핸들러가 버퍼 완료를 <br/>알립니다.": "Handlers signal completion <br/>of a queued request#39;s <br/>buffer.", "앱은 제출 전에 request에 <br/>캡처 버퍼를 하나 이상 <br/>넣어야 합니다. 버퍼가 <br/>없으면 요청은 큐에 들어가지 <br/>못합니다.": "The app must add a capture <br/>buffer before submission; a <br/>bufferless request is <br/>rejected.", "큐에 들어간 요청이 완료되면 <br/>카메라는 requestCompleted <br/>신호로 알립니다.": "The camera signals <br/>completion of a queued <br/>request via <br/>requestCompleted.", "핸들러가 요청 완료를 알리면 <br/>카메라는 완료 신호로 앱에 <br/>알립니다.": "The camera signals the <br/>request#39;s completion.", "핸들러는 필요한 후속 작업을 <br/>할 기회를 가진 뒤 <br/>completeRequest를 <br/>명시적으로 호출해야 합니다. <br/>반환 후에는 요청에 접근하면 <br/>안 됩니다.": "Handlers can perform needed <br/>work and must call <br/>completeRequest. No access <br/>is allowed after it returns.", "핸들러의 completeRequest <br/>호출 순서에는 제약이 <br/>없지만, 요청은 원래 제출 <br/>순서로 앱에 돌아갑니다.": "Calls have no ordering <br/>constraint; requests return <br/>to the app in submission <br/>order.", "핸들러의 호출 순서와 <br/>관계없이 앱에는 제출 순서로 <br/>반환됩니다.": "Requests return to the app <br/>in submission order."}
  v_submission["앱은 제출 전에 request에 <br/>캡처 버퍼를 하나 이상 <br/>넣어야 합니다. 버퍼가 <br/>없으면 요청은 큐에 들어가지 <br/>못합니다."]
  v_buffer["completeBuffer는 버퍼 <br/>완료를 알립니다. 마지막 <br/>버퍼가 완료되어도 요청은 <br/>자동으로 완료되지 않습니다."]
  v_explicit["핸들러는 필요한 후속 작업을 <br/>할 기회를 가진 뒤 <br/>completeRequest를 <br/>명시적으로 호출해야 합니다. <br/>반환 후에는 요청에 접근하면 <br/>안 됩니다."]
  v_application["핸들러의 completeRequest <br/>호출 순서에는 제약이 <br/>없지만, 요청은 원래 제출 <br/>순서로 앱에 돌아갑니다."]
  v_notification["큐에 들어간 요청이 완료되면 <br/>카메라는 requestCompleted <br/>신호로 알립니다."]
  v_submission -->|"버퍼가 있는 요청을 큐에 <br/>넣으면 핸들러가 버퍼 완료를 <br/>알립니다."| v_buffer
  v_buffer -->|"버퍼 완료 후에도 핸들러가 <br/>요청을 명시적으로 완료해야 <br/>합니다."| v_explicit
  v_explicit -->|"핸들러의 호출 순서와 <br/>관계없이 앱에는 제출 순서로 <br/>반환됩니다."| v_application
  v_explicit -->|"핸들러가 요청 완료를 알리면 <br/>카메라는 완료 신호로 앱에 <br/>알립니다."| v_notification
```

[Mermaid 원문](onboarding.request-completion-contract.mmd)

??? note "그림 근거와 확인 범위"
    요청의 제출 조건, 버퍼 완료와 명시적 요청 완료, 앱에 전달하는 순서는 어떻게 연결됩니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="The app must add a capture buffer before submission; a bufferless request is rejected.">앱은 제출 전에 request에 캡처 버퍼를 하나 이상 넣어야 합니다. 버퍼가 없으면 요청은 큐에 들어가지 못합니다.</span> | [src/libcamera/camera.cpp:1311](#source-a697a2ba4de7965c) |
    | <span data-sdd-label-en="completeBuffer signals buffer completion; the last buffer does not complete the request.">completeBuffer는 버퍼 완료를 알립니다. 마지막 버퍼가 완료되어도 요청은 자동으로 완료되지 않습니다.</span> | [src/libcamera/pipeline_handler.cpp:551](#source-9bd7c9fb9847e336) |
    | <span data-sdd-label-en="Handlers can perform needed work and must call completeRequest. No access is allowed after it returns.">핸들러는 필요한 후속 작업을 할 기회를 가진 뒤 completeRequest를 명시적으로 호출해야 합니다. 반환 후에는 요청에 접근하면 안 됩니다.</span> | [src/libcamera/pipeline_handler.cpp:551](#source-9bd7c9fb9847e336) · [src/libcamera/pipeline_handler.cpp:574](#source-77cb263c0a63392c) |
    | <span data-sdd-label-en="Calls have no ordering constraint; requests return to the app in submission order.">핸들러의 completeRequest 호출 순서에는 제약이 없지만, 요청은 원래 제출 순서로 앱에 돌아갑니다.</span> | [src/libcamera/pipeline_handler.cpp:551](#source-9bd7c9fb9847e336) · [src/libcamera/pipeline_handler.cpp:574](#source-77cb263c0a63392c) |
    | <span data-sdd-label-en="The camera signals completion of a queued request via requestCompleted.">큐에 들어간 요청이 완료되면 카메라는 requestCompleted 신호로 알립니다.</span> | [src/libcamera/camera.cpp:1311](#source-a697a2ba4de7965c) |
    | <span data-sdd-label-en="Handlers signal completion of a queued request&#x27;s buffer.">버퍼가 있는 요청을 큐에 넣으면 핸들러가 버퍼 완료를 알립니다.</span> | [src/libcamera/camera.cpp:1311](#source-a697a2ba4de7965c) · [src/libcamera/pipeline_handler.cpp:551](#source-9bd7c9fb9847e336) |
    | <span data-sdd-label-en="Handlers must explicitly complete the request.">버퍼 완료 후에도 핸들러가 요청을 명시적으로 완료해야 합니다.</span> | [src/libcamera/pipeline_handler.cpp:551](#source-9bd7c9fb9847e336) |
    | <span data-sdd-label-en="Requests return to the app in submission order.">핸들러의 호출 순서와 관계없이 앱에는 제출 순서로 반환됩니다.</span> | [src/libcamera/pipeline_handler.cpp:551](#source-9bd7c9fb9847e336) · [src/libcamera/pipeline_handler.cpp:574](#source-77cb263c0a63392c) |
    | <span data-sdd-label-en="The camera signals the request&#x27;s completion.">핸들러가 요청 완료를 알리면 카메라는 완료 신호로 앱에 알립니다.</span> | [src/libcamera/pipeline_handler.cpp:551](#source-9bd7c9fb9847e336) · [src/libcamera/camera.cpp:1311](#source-a697a2ba4de7965c) · [src/libcamera/pipeline_handler.cpp:574](#source-77cb263c0a63392c) |
<!-- /sdd:visual:request-completion-contract -->

파이프라인 핸들러가 completeBuffer를 호출해 요청의 마지막 버퍼가 완료되었음을 알리더라도, 그 시점에 요청은 자동으로 완료되지 않습니다. 이는 파이프라인 핸들러가 여전히 필요할 수 있는 작업을 수행할 기회를 주기 위한 것이며, 핸들러는 completeRequest()로 요청을 명시적으로 완료해야 합니다. 요청은 제출된 순서대로 애플리케이션에 반환되며, 파이프라인 핸들러는 순서 제약 없이 완료된 요청에 대해 completeRequest()를 호출할 수 있습니다. `src/libcamera/pipeline_handler.cpp:551`, `src/libcamera/pipeline_handler.cpp:574`

근거 원문: [src/libcamera/camera.cpp:1311](#source-a697a2ba4de7965c) · [src/libcamera/pipeline_handler.cpp:551](#source-9bd7c9fb9847e336) · [src/libcamera/pipeline_handler.cpp:574](#source-77cb263c0a63392c)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 카메라를 직접 확인해 보려면 무엇을 실행합니까? | [직접 실행해 보기](#직접-실행해-보기) | 코드 근거와 설명 연결 |
    | 요청 접수와 완료 통지가 별도 단계인 이유 중 소스가 직접 밝힌 것은 무엇입니까? | [요청 접수와 완료를 나눈 이유](#요청-접수와-완료를-나눈-이유) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-5bc9ee57c1b6daee"></a>

??? note "소스 근거: README.rst:107"
    `README.rst:107`에서 시작하는 발췌입니다. 종료 줄은 117이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `c35f23844229f0b6dc8411bca6eea313eb05f11d9b9a4524f5375c921b09afc4`
    
    ```text
    The ``cam`` utility can be used for basic testing. You can list the cameras
    detected on the system with ``cam -l``, and capture ten frames from the first
    camera and save them to disk with ``cam -c 1 --capture=10 --file``. See
    ``cam -h`` for more information about the ``cam`` tool.
    
    In case of problems, a detailed debug log can be obtained from libcamera by
    setting the ``LIBCAMERA_LOG_LEVELS`` environment variable:
    
    .. code::
    
        :~$ LIBCAMERA_LOG_LEVELS=*:DEBUG cam -l
    ```

<a id="source-a697a2ba4de7965c"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1311"
    `src/libcamera/camera.cpp:1311`에서 시작하는 발췌입니다. 종료 줄은 1318이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e28ed33dec85a5e783457be419afac5b7c646b588c24bc311d46265b1ae7f37a`
    
    ```text
    This function queues a \a request to the camera for capture.
     *
     * After allocating the request with createRequest(), the application shall
     * fill it with at least one capture buffer before queuing it. Requests that
     * contain no buffers are invalid and are rejected without being queued.
     *
     * Once the request has been queued, the camera will notify its completion
     * through the \ref requestCompleted signal.
    ```

<a id="source-9bd7c9fb9847e336"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:551"
    `src/libcamera/pipeline_handler.cpp:551`에서 시작하는 발췌입니다. 종료 줄은 556이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `dc60b6f028df4f7341facfcbd3ebade17f81bb4d2e72ce580ba93c7a1c449b42`
    
    ```text
    This function shall be called by pipeline handlers to signal completion of
     * the \a buffer part of the \a request. It notifies applications of buffer
     * completion and updates the request's internal buffer tracking. The request
     * is not completed automatically when the last buffer completes to give
     * pipeline handlers a chance to perform any operation that may still be
     * needed. They shall complete requests explicitly with completeRequest().
    ```

<a id="source-77cb263c0a63392c"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:574"
    `src/libcamera/pipeline_handler.cpp:574`에서 시작하는 발췌입니다. 종료 줄은 580이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `5df554f7462852344c1f8f25dd3bf2f16f22ab34e3f96d948d54ec44baca7217`
    
    ```text
    The pipeline handler shall call this function to notify the \a camera that
     * the request has completed. The request is no longer managed by the pipeline
     * handler and shall not be accessed once this function returns.
     *
     * This function ensures that requests will be returned to the application in
     * submission order, the pipeline handler may call it on any complete request
     * without any ordering constraint.
    ```

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `README.rst`, `include/libcamera/camera.h`, `include/libcamera/internal/pipeline_handler.h`, `include/libcamera/request.h`, `src/libcamera/camera.cpp`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/request.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `293d751a81`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-04 · 사람 검토 전

다음 단계: [카메라와 요청 모델](camera-model.md)
