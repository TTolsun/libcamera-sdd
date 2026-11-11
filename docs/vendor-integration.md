---
generated_at: 2026-11-11 19:43:47+00:00
source_commit: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
status: ok
section: vendor-integration
generation_method: facts-and-llm
evidence_fingerprint: 7333c0840e570d83c5558815669560e0761251ddc6ee3aad5dacfcd710ef4075
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design:
  schema: 1
  input_fingerprint: 7333c0840e570d83c5558815669560e0761251ddc6ee3aad5dacfcd710ef4075
  answers:
    integration:
    - text: 애플리케이션은 촬영을 준비하려면 카메라를 확보하고 구성해야 하며, 카메라를 시작하면 정지할 때까지 요청을 처리할 수 있고, 사용을
        마치면 카메라를 해제해야 합니다.
      evidence:
      - camera
      covers:
      - integration
      kind: behavior
      quote: "An application needs to perform a sequence of operations on a camera\
        \ before\n * it is ready to process requests. The camera needs to be acquired\
        \ and\n * configured to prepare the camera for capture. Once started the camera\
        \ can\n * process requests until it is stopped. When an application is done\
        \ with a\n * camera, the camera needs to be released."
      part_id: application
    - text: 애플리케이션은 카메라를 해제하지 않은 동안 여러 번 시작하고 정지할 수 있으며, 카메라를 재구성할 수도 있습니다.
      evidence:
      - restart
      covers:
      - integration
      kind: behavior
      quote: "An application may start and stop a camera multiple times as long as\
        \ it is\n * not released. The camera may also be reconfigured."
      part_id: restart
    - text: '`Camera` 클래스는 카메라 상태에 영향을 주는 함수들을 일반적으로 서로 동기화하지 않으므로, 필요한 경우 호출자가 동기화해야
        합니다.'
      evidence:
      - synchronization
      covers:
      - integration
      kind: behavior
      quote: "Functions that affect the camera state as defined below are generally\
        \ not\n * synchronized with each other by the Camera class. The caller is\
        \ responsible\n * for ensuring their synchronization if necessary."
      part_id: synchronization
    boundary:
    - text: '`PipelineHandler::match()` 구현자는 단일 파이프라인에 필요한 미디어 장치를 모두 찾으면 각 장치에 대해
        `MediaDevice::acquire()`를 호출해 확보한 다음, 해당 `Camera` 인스턴스를 하나 이상 생성하고 내부에 저장하며
        카메라 매니저에 등록한 뒤 `true`를 반환해야 합니다.'
      evidence:
      - handler
      covers:
      - boundary
      kind: behavior
      quote: "This function is the main entry point of the pipeline handler. It is\
        \ called\n * by the camera manager with the \\a enumerator passed as an argument.\
        \ It shall\n * acquire from the \\a enumerator all the media devices it needs\
        \ for a single\n * pipeline, create one or multiple Camera instances and register\
        \ them with the\n * camera manager.\n *\n * If all media devices needed by\
        \ the pipeline handler are found, they must all\n * be acquired by a call\
        \ to MediaDevice::acquire(). This function shall then\n * create the corresponding\
        \ Camera instances, store them internally, and return\n * true. Otherwise\
        \ it shall not acquire any media device (or shall release all\n * the media\
        \ devices is has acquired by calling MediaDevice::release()) and\n * return\
        \ false.\n *"
      part_id: success
    - text: '`PipelineHandler::match()` 구현자는 필요한 미디어 장치를 모두 찾지 못했을 때 아직 장치를 확보하지 않았다면
        어떤 장치도 확보해서는 안 되며, 이미 일부를 확보했다면 `MediaDevice::release()`를 호출해 확보한 장치를 모두 해제하고
        `false`를 반환해야 합니다.'
      evidence:
      - failure
      covers:
      - boundary
      kind: behavior
      quote: "If all media devices needed by the pipeline handler are found, they\
        \ must all\n * be acquired by a call to MediaDevice::acquire(). This function\
        \ shall then\n * create the corresponding Camera instances, store them internally,\
        \ and return\n * true. Otherwise it shall not acquire any media device (or\
        \ shall release all\n * the media devices is has acquired by calling MediaDevice::release())\
        \ and\n * return false.\n *"
      part_id: failure
    - text: '`PipelineHandler::match()`는 `CameraManager` 스레드에서 호출되며, `true`를 반환하면
        새로운 `PipelineHandler` 인스턴스가 생성되고 그 인스턴스의 `match()`가 호출됩니다.'
      evidence:
      - repeat
      covers:
      - boundary
      kind: behavior
      quote: "If this function returns true, a new instance of the pipeline handler\
        \ will\n * be created and its match() function called.\n *\n * \\context This\
        \ function is called from the CameraManager thread."
      part_id: repeat
    configuration:
    - text: '`generateConfiguration`의 호출자는 기본 구성을 가져오려는 사용 사례를 `roles`에 채워야 합니다.'
      evidence:
      - generate-input
      covers:
      - configuration
      kind: behavior
      quote: "Generate a default configuration for the \\a camera for a specified\
        \ list of\n * stream roles. The caller shall populate the \\a roles with the\
        \ use-cases it\n * wishes to fetch the default configuration for. The returned\
        \ configuration\n * can then be examined by the caller to learn about the\
        \ selected streams and\n * their default parameters."
      part_id: generate
    - text: '`generateConfiguration()`이 반환하는 구성은 선택된 스트림과 그 스트림의 기본 파라미터를 호출자가 확인할
        수 있는 정보를 포함합니다.'
      evidence:
      - generate-input
      covers:
      - configuration
      kind: behavior
      quote: "Generate a default configuration for the \\a camera for a specified\
        \ list of\n * stream roles. The caller shall populate the \\a roles with the\
        \ use-cases it\n * wishes to fetch the default configuration for. The returned\
        \ configuration\n * can then be examined by the caller to learn about the\
        \ selected streams and\n * their default parameters."
      part_id: generate-output
    - text: '`PipelineHandler::generateConfiguration()`은 요청된 `roles`를 충족할 수 있으면 유효한
        `CameraConfiguration`을 반환하고, 그렇지 않으면 `null` 포인터를 반환해야 합니다.'
      evidence:
      - generate-result
      covers:
      - configuration
      kind: behavior
      quote: "\\return A valid CameraConfiguration if the requested roles can be satisfied,\n\
        \ * or a null pointer otherwise."
      part_id: generate-result
    - text: '`PipelineHandler::generateConfiguration()` 구현은 어떤 스레드에서든 호출될 수 있으므로 스레드
        안전성을 갖춰야 합니다.'
      evidence:
      - generate-context
      covers:
      - configuration
      kind: behavior
      quote: "\\context This function may be called from any thread and shall be\n\
        \ * \\threadsafe."
      part_id: generate-safety
    - text: '`PipelineHandler::generateConfiguration()` 구현자는 파이프라인 핸들러 내에서 `camera`의
        상태를 변경해서는 안 됩니다.'
      evidence:
      - generate-state
      covers:
      - configuration
      kind: behavior
      quote: "It shall not modify the state of the \\a camera in the pipeline\n *\
        \ handler."
      part_id: generate-state
    - text: '`PipelineHandler::configure()`에 전달되는 설정은 `CameraConfiguration::validate()`로
        검증되었음이 보장되므로, 파이프라인 핸들러 구현은 추가 검증을 해서는 안 됩니다.'
      evidence:
      - configure-input
      covers:
      - configuration
      kind: behavior
      quote: "The configuration is guaranteed to have been validated with\n * CameraConfiguration::validate().\
        \ The pipeline handler implementation shall\n * not perform further validation"
      part_id: configure
    - text: '`PipelineHandler::configure()` 구현은 자체 `CameraConfiguration` 파생 클래스에 저장된
        모든 사용자 정의 필드에 의존할 수 있습니다.'
      evidence:
      - configure-fields
      covers:
      - configuration
      kind: behavior
      quote: "may rely on any custom field stored in its\n * custom CameraConfiguration\
        \ derived class."
      part_id: configure-fields
    - text: '`PipelineHandler::configure()` 구현자는 카메라를 구성할 때 `StreamConfiguration::setStream()`을
        사용해 `CameraConfiguration`의 각 `StreamConfiguration` 항목에 `Stream` 인스턴스를 연결해야
        합니다.'
      evidence:
      - configure-stream
      covers:
      - configuration
      kind: behavior
      quote: "When configuring the camera the pipeline handler shall associate a Stream\n\
        \ * instance to each StreamConfiguration entry in the CameraConfiguration\
        \ using\n * the StreamConfiguration::setStream() function."
      part_id: configure-stream
    - text: '`PipelineHandler::configure()`는 `CameraManager` 스레드에서 호출되며, 구현은 성공 시
        `0`을, 실패 시 음수 오류 코드를 반환해야 합니다.'
      evidence:
      - configure-result
      covers:
      - configuration
      kind: behavior
      quote: "\\context This function is called from the CameraManager thread.\n *\n\
        \ * \\return 0 on success or a negative error code otherwise"
      part_id: configure-result
    request:
    - text: 요청에는 버퍼 집합이 들어 있으며, 이 버퍼들은 스트림에 연결됩니다. 요청에는 파라미터 집합도 들어 있습니다. `queueRequestDevice`
        구현자는 요청에서 제공한 버퍼에 캡처되는 프레임에 해당 파라미터가 적용되도록 장치를 프로그래밍해야 합니다.
      evidence:
      - device
      covers:
      - request
      kind: behavior
      quote: "This function queues a capture request to the device for processing.\
        \ The\n * request contains a set of buffers associated with streams and a\
        \ set of\n * parameters. The pipeline handler shall program the device to\
        \ ensure that the\n * parameters will be applied to the frames captured in\
        \ the buffers provided in\n * the request.\n *"
      part_id: device
    - text: '`queueRequestDevice` 구현자는 성공하면 `0`을, 실패하면 음수 오류 코드를 반환해야 합니다.'
      evidence:
      - device-result
      covers:
      - request
      kind: behavior
      quote: "\\context This function is called from the CameraManager thread.\n *\n\
        \ * \\return 0 on success or a negative error code otherwise"
      part_id: device-result
    - text: '`PipelineHandler::queueRequestDevice()`는 `CameraManager` 스레드에서 호출됩니다.'
      evidence:
      - device-result
      covers:
      - request
      kind: behavior
      quote: "\\context This function is called from the CameraManager thread.\n *\n\
        \ * \\return 0 on success or a negative error code otherwise"
      part_id: device-context
    - text: 파이프라인 핸들러는 요청의 버퍼 완료를 알리기 위해 `CameraManager` 스레드에서 `completeBuffer`를 호출해야
        합니다. `completeBuffer`는 애플리케이션에 버퍼 완료를 통지하고 요청 내부의 버퍼 추적을 갱신합니다.
      evidence:
      - buffer
      - completion-context
      covers:
      - request
      kind: behavior
      quote: "This function shall be called by pipeline handlers to signal completion\
        \ of\n * the \\a buffer part of the \\a request. It notifies applications\
        \ of buffer\n * completion and updates the request's internal buffer tracking."
      part_id: buffer
    - text: 마지막 버퍼가 완료되어도 요청은 자동으로 완료되지 않으므로 파이프라인 핸들러가 `completeRequest()`를 명시적으로
        호출해 요청을 완료해야 합니다.
      evidence:
      - completion
      - notification
      covers:
      - request
      kind: behavior
      quote: "The request\n * is not completed automatically when the last buffer\
        \ completes to give\n * pipeline handlers a chance to perform any operation\
        \ that may still be\n * needed."
      part_id: completion
    algorithm:
    - text: '`createIPA`는 `module`을 호출할 때 이름을 나타내는 `name`, 최소 버전을 나타내는 `minVersion`,
        최대 버전을 나타내는 `maxVersion`을 순서대로 전달합니다.'
      evidence:
      - module-call
      covers:
      - algorithm
      kind: behavior
      quote: IPAModule *m = module(name, minVersion, maxVersion);
      part_id: module
    - text: '`IPAManager::module`은 모듈을 순회하며 이름과 허용 버전 범위에 대해 첫 `match`가 성립하면 해당 모듈을
        반환하고 검색을 끝냅니다. 끝까지 일치하는 모듈이 없으면 `nullptr`을 반환합니다.'
      evidence:
      - module-lookup
      covers:
      - algorithm
      kind: behavior
      quote: "\\brief Retrieve an IPA module that matches a given pipeline handler\n\
        \ * \\param[in] name The IPA module string identifier\n * \\param[in] minVersion\
        \ Minimum acceptable version of IPA module\n * \\param[in] maxVersion Maximum\
        \ acceptable version of IPA module\n */\nIPAModule *IPAManager::module(const\
        \ char *name, uint32_t minVersion,\n\t\t\t      uint32_t maxVersion)\n{\n\t\
        for (const auto &module : modules_) {\n\t\tif (module->match(name, minVersion,\
        \ maxVersion))\n\t\t\treturn module.get();\n\t}\n\n\treturn nullptr;\n}"
      part_id: module-lookup
    - text: '`createIPA`는 `module`의 결과를 `m`에 받고, `!m`이면 `nullptr`을 반환합니다.'
      evidence:
      - module-missing
      covers:
      - algorithm
      kind: behavior
      quote: "IPAModule *m = module(name, minVersion, maxVersion);\n\t\tif (!m)\n\t\
        \t\treturn nullptr;"
      part_id: module-lookup
    - text: '`createIPA` 내부 람다는 `isSignatureValid(m)`이 참이면 `T::Threaded` 프록시 객체를 생성하고,
        거짓이면 `T::Isolated` 프록시 객체를 생성합니다.'
      evidence:
      - proxy-kind
      covers:
      - algorithm
      kind: behavior
      quote: "auto proxy = [&]() -> std::unique_ptr<T> {\n\t\t\tif (isSignatureValid(m))\n\
        \t\t\t\treturn std::make_unique<typename T::Threaded>(m, cm_);\n\t\t\telse\n\
        \t\t\t\treturn std::make_unique<typename T::Isolated>(m, cm_);\n\t\t}();"
      part_id: signature
    - text: '`createIPA`는 생성한 프록시의 `isValid` 검사가 실패하면 `Failed to load proxy` 오류를 기록하고
        `nullptr`을 반환합니다.'
      evidence:
      - create-full
      covers:
      - algorithm
      kind: behavior
      quote: "if (!proxy->isValid()) {\n\t\t\tLOG(IPAManager, Error) << \"Failed to\
        \ load proxy\";\n\t\t\treturn nullptr;\n\t\t}"
      part_id: proxy
    - text: '`createIPA`는 생성한 프록시가 유효성 검사를 통과하면 해당 프록시를 반환합니다.'
      evidence:
      - create-full
      covers:
      - algorithm
      kind: behavior
      quote: "return proxy;\n\t}"
      part_id: proxy-success
    shutdown:
    - text: '`PipelineHandler::stop()`은 먼저 `waitingRequests.swap(data->waitingRequests_)`를
        실행한 다음 `stopDevice(camera)`를 호출합니다.'
      evidence:
      - stop-order
      covers:
      - shutdown
      kind: behavior
      quote: "void PipelineHandler::stop(Camera *camera)\n{\n\t/*\n\t * Take all waiting\
        \ requests so that they are not requeued in response\n\t * to completeRequest()\
        \ being called inside stopDevice(). Cancel them\n\t * after the device to\
        \ keep them in order.\n\t */\n\tCamera::Private *data = camera->_d();\n\t\
        std::queue<Request *> waitingRequests;\n\twaitingRequests.swap(data->waitingRequests_);\n\
        \n\t/* Stop the pipeline handler and let the queued requests complete. */\n\
        \tstopDevice(camera);"
      part_id: order
    - text: '`PipelineHandler::stop()`은 `stopDevice()` 내부에서 `completeRequest()`가 호출될
        때 대기 중인 요청이 다시 큐에 들어가지 않도록 이 요청들을 따로 옮깁니다.'
      evidence:
      - stop-rationale
      covers:
      - shutdown
      kind: behavior
      quote: "Take all waiting requests so that they are not requeued in response\n\
        \t * to completeRequest() being called inside stopDevice()."
      part_id: rationale
    - text: '`stopDevice()` 구현자는 실행 중인 모든 스트림의 캡처와 요청 처리를 즉시 중단하고, 해당 장치의 미완료 요청을
        모두 취소해 즉시 오류 상태로 완료해야 합니다.'
      evidence:
      - device
      covers:
      - shutdown
      kind: behavior
      quote: "\\fn PipelineHandler::stopDevice()\n * \\brief Stop capturing from all\
        \ running streams\n * \\param[in] camera The camera to stop\n *\n * This function\
        \ stops capturing and processing requests immediately. All\n * pending requests\
        \ are cancelled and complete immediately in an error state.\n */"
      part_id: device
    - text: '`PipelineHandler::stop()`은 대기 요청을 따로 꺼낸 뒤 `stopDevice()`를 호출하고, 각 대기
        요청을 취소한 후 `doQueueRequest()`로 전달하여 순번을 부여하고 `queuedRequests_`에 임시로 추가해 `completeRequest()`에서
        완료할 수 있게 합니다.'
      evidence:
      - stop
      covers:
      - shutdown
      kind: behavior
      quote: "void PipelineHandler::stop(Camera *camera)\n{\n\t/*\n\t * Take all waiting\
        \ requests so that they are not requeued in response\n\t * to completeRequest()\
        \ being called inside stopDevice(). Cancel them\n\t * after the device to\
        \ keep them in order.\n\t */\n\tCamera::Private *data = camera->_d();\n\t\
        std::queue<Request *> waitingRequests;\n\twaitingRequests.swap(data->waitingRequests_);\n\
        \n\t/* Stop the pipeline handler and let the queued requests complete. */\n\
        \tstopDevice(camera);\n\n\t/* Cancel and signal as complete all waiting requests.\
        \ */\n\twhile (!waitingRequests.empty()) {\n\t\tRequest *request = waitingRequests.front();\n\
        \t\twaitingRequests.pop();\n\n\t\t/*\n\t\t * Cancel all requests by marking\
        \ them as cancelled and calling\n\t\t * doQueueRequest() instead of cancelRequest().\
        \ This ensures\n\t\t * that the requests get a sequence number and are temporarily\n\
        \t\t * added to queuedRequests_ so they can be properly completed in\n\t\t\
        \ * completeRequest().\n\t\t */\n\t\trequest->_d()->cancel();\n\t\tdoQueueRequest(request);\n\
        \t}\n\n\t/* Make sure no requests are pending. */\n\tASSERT(data->queuedRequests_.empty());\n\
        \tASSERT(data->waitingRequests_.empty());\n\n\tdata->requestSequence_ = 0;\n\
        }"
      part_id: waiting
    - text: '`PipelineHandler::stop()`은 대기 요청을 처리한 뒤 두 `ASSERT`로 `queuedRequests_`와
        `waitingRequests_`가 비어 있는지 확인하고, `requestSequence_`에 `0`을 저장합니다.'
      evidence:
      - stop
      covers:
      - shutdown
      kind: behavior
      quote: "void PipelineHandler::stop(Camera *camera)\n{\n\t/*\n\t * Take all waiting\
        \ requests so that they are not requeued in response\n\t * to completeRequest()\
        \ being called inside stopDevice(). Cancel them\n\t * after the device to\
        \ keep them in order.\n\t */\n\tCamera::Private *data = camera->_d();\n\t\
        std::queue<Request *> waitingRequests;\n\twaitingRequests.swap(data->waitingRequests_);\n\
        \n\t/* Stop the pipeline handler and let the queued requests complete. */\n\
        \tstopDevice(camera);\n\n\t/* Cancel and signal as complete all waiting requests.\
        \ */\n\twhile (!waitingRequests.empty()) {\n\t\tRequest *request = waitingRequests.front();\n\
        \t\twaitingRequests.pop();\n\n\t\t/*\n\t\t * Cancel all requests by marking\
        \ them as cancelled and calling\n\t\t * doQueueRequest() instead of cancelRequest().\
        \ This ensures\n\t\t * that the requests get a sequence number and are temporarily\n\
        \t\t * added to queuedRequests_ so they can be properly completed in\n\t\t\
        \ * completeRequest().\n\t\t */\n\t\trequest->_d()->cancel();\n\t\tdoQueueRequest(request);\n\
        \t}\n\n\t/* Make sure no requests are pending. */\n\tASSERT(data->queuedRequests_.empty());\n\
        \tASSERT(data->waitingRequests_.empty());\n\n\tdata->requestSequence_ = 0;\n\
        }"
      part_id: final-state
    validation:
    - text: 파이프라인 핸들러 구현자는 `completeRequest`가 반환된 뒤 해당 요청에 접근해서는 안 됩니다.
      evidence:
      - completion
      covers:
      - validation
      kind: behavior
      quote: "\\brief Signal request completion\n * \\param[in] request The request\
        \ that has completed\n *\n * The pipeline handler shall call this function\
        \ to notify the \\a camera that\n * the request has completed. The request\
        \ is no longer managed by the pipeline\n * handler and shall not be accessed\
        \ once this function returns.\n *\n * This function ensures that requests\
        \ will be returned to the application in\n * submission order, the pipeline\
        \ handler may call it on any complete request\n * without any ordering constraint.\n\
        \ *\n * \\context This function shall be called from the CameraManager thread.\n\
        \ */\nvoid PipelineHandler::completeRequest"
      part_id: lifetime
    - text: 파이프라인 핸들러는 완료된 요청을 순서 제약 없이 `completeRequest`에 전달할 수 있으며, 이 함수는 요청을 제출
        순서대로 애플리케이션에 반환합니다.
      evidence:
      - completion-order
      covers:
      - validation
      kind: behavior
      quote: "This function ensures that requests will be returned to the application\
        \ in\n * submission order, the pipeline handler may call it on any complete\
        \ request\n * without any ordering constraint."
      part_id: order
    - text: 파이프라인 핸들러는 `completeRequest`를 `CameraManager` 스레드에서 호출해야 합니다.
      evidence:
      - completion-thread
      covers:
      - validation
      kind: behavior
      quote: "\\context This function shall be called from the CameraManager thread.\n\
        \ */"
      part_id: context
  topic_inputs:
    integration: 03768be1406e56532b961ebd1e06d9db959b372568944b24bc233542e030a519
    boundary: c38647930d04bb610c7b7497d1b9689995ed11eb2793fe85479f14a504466e1a
    configuration: f0c3ab72edf0b37eea23ddcbfde3ae1685b5e173a40886e78254fc39125bbead
    request: 1d2ac6be6b677be7d17eb32468885e84d0a0217bfaaccb19bc486895ed1610b8
    algorithm: 90945b9d2c41c43f8a09b9ac4ddff2424e984698ea1abc2385aa9f3ba3ed0b14
    shutdown: f92b884e45f0cc3b22250f559b153e2d145ee0e57ca234d135b6948815ebd970
    validation: c7a7c22ae75fbf958e3e6a7d2b48a12b348e25754554303bfb2ecd4ca4f04ab8
  reused_topics: []
  replayed_units: []
  generated_topics:
  - integration
  - boundary
  - configuration
  - request
  - algorithm
  - shutdown
  - validation
  topic_agents:
    integration: cli/codex/gpt-6.1-terra
    boundary: cli/codex/gpt-6.1-terra
    configuration: cli/codex/gpt-6.1-terra
    request: cli/codex/gpt-6.1-terra
    algorithm: cli/codex/gpt-6.1-terra
    shutdown: cli/codex/gpt-6.1-terra
    validation: cli/codex/gpt-6.1-terra
  grounding_review: passed
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
    design_validation: 92ddb9a65c909173ff4c7cb627dff83e71c10c8258c51344ef0eb1a7a023937f
  validation_model: 92458604f55e12d305fd877f3a14d61b5aaf4596d84fb28092d3322433cc2806
  style_policy:
    fluent-korean.md: ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975
    i-have-adhd.md: 3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9
    README.md: b87a84b1bc31079837dc4dc4527ce02c9dc2cbc3a26ff7e99e0872941d213995
  checkpoint_units:
  - checkpoint: ce0dd8b4f708ca51d1f2e2783982297fa3070878469a48ab6f858654e98d45af.json
    topic: integration
    part: application
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/001.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/002.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/003.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/004.receipt.json
  - checkpoint: c2f37f716be09b1697ddc63706fa0bb7c27caa0696b3e77d4a10a8eb49fe3edf.json
    topic: integration
    part: restart
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/005.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/006.receipt.json
  - checkpoint: 102371f43460b16c89bb98c8aadad1ad44e27ea7c0d2210f3b2e5b52c2b4d106.json
    topic: integration
    part: synchronization
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/007.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/008.receipt.json
  - checkpoint: 895bb3037cce54a639d1091e1b3c48de16e6e8409e2b80d89d8bfa86f7eb1abe.json
    topic: boundary
    part: success
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/009.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/010.receipt.json
  - checkpoint: 66c1be6e3de127e0fb36bfe560d439ebc20c405ad8c6ef40563b8b01bece9a61.json
    topic: boundary
    part: failure
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/011.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/012.receipt.json
  - checkpoint: 6ab0d1bb8210fcff14a50e919ae723e9563d57d8634687129d4fc4fc35bb7e95.json
    topic: boundary
    part: repeat
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/013.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/014.receipt.json
  - checkpoint: 1f2bbec9fb1920027ce24665845d39814ed59177ba877b6a1527b581e045e846.json
    topic: configuration
    part: generate
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/015.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/016.receipt.json
  - checkpoint: c68841bbd9b50fff787ccfc2323275e50b24dda8b50c0636e9ccb97f2c70a2f1.json
    topic: configuration
    part: generate-output
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/017.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/018.receipt.json
  - checkpoint: 4e105d04c485b5dab6dea3f7d0e38e3a15e84f5c3be7fc7f6708b5cbf6c5501f.json
    topic: configuration
    part: generate-result
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/019.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/020.receipt.json
  - checkpoint: ff5273a4ae66407e54cd1693e49d18419731074d3f98db781c4f548388f6e2ec.json
    topic: configuration
    part: generate-safety
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/021.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/022.receipt.json
  - checkpoint: 5b3ee04871ee5c5359fa936cb7785e181e4b975e0751a9d4dedbaf2a0aabace3.json
    topic: configuration
    part: generate-state
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/023.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/024.receipt.json
  - checkpoint: 2138b02906d74f51d9180117e0b33945e62ece525ae630c0f27557f9192f6654.json
    topic: configuration
    part: configure
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/025.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/026.receipt.json
  - checkpoint: 832326ac7c372a43739b646315d51e4b0ea2ebf500f16d2a561c74e048dd01da.json
    topic: configuration
    part: configure-fields
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/027.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/028.receipt.json
  - checkpoint: fefab167eb625c5b0cfaa67cdfc6d201ad2689c5d59466d1193d0e6dedba39e8.json
    topic: configuration
    part: configure-stream
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/029.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/030.receipt.json
  - checkpoint: f683005081b577040a555509d29f83c392eaf2c5c3960c4f2a97f42c1c9b7a59.json
    topic: configuration
    part: configure-result
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/031.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/032.receipt.json
  - checkpoint: db9fa0e2d1396155173bd62cd1cff08e585bcea4133d493dfaf558abcbfd5186.json
    topic: request
    part: device
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/033.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/034.receipt.json
  - checkpoint: 1d61588d3d06fa5f01968fe2a1b5f2d21121ca23bd1f245dd46baf8c062a9b8b.json
    topic: request
    part: device-result
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/035.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/036.receipt.json
  - checkpoint: ae9265e36f0c869a04f0d422a8e805bf991fcdbc7f055e27c479193c1bf9dd23.json
    topic: request
    part: device-context
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/037.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/038.receipt.json
  - checkpoint: d3390fdac44874fb3111e7767736a9589156460c0233fb3aed82808eed1be480.json
    topic: request
    part: buffer
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/039.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/040.receipt.json
  - checkpoint: 2bf525fe811dd042ca86e9d73b82528ab1d1a26e9c89686118d638ced9ab5ccd.json
    topic: request
    part: completion
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/041.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/042.receipt.json
  - checkpoint: 9d840da77add322aad4ba37c1c63dcab7cc9ff915690ee5d91bb978829b46453.json
    topic: algorithm
    part: module
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/043.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/044.receipt.json
  - checkpoint: f2305218a3b103a42c477de44126055483fe134d3608e269804f14ff4a359b7e.json
    topic: algorithm
    part: module-lookup
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/045.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/046.receipt.json
  - checkpoint: 14f03adb5458897f6a385820c77ca2ef36d0b2ffe7e3c4439e8d59fe028abc68.json
    topic: algorithm
    part: signature
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/047.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/048.receipt.json
  - checkpoint: 43a91cc996ef8275f585fb41c6679c0454a6c6945689b02b05b0bfb96cbc9e8b.json
    topic: algorithm
    part: proxy
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 3ad154b391d74761ac681e7f7705ab34/001.receipt.json
    - 3ad154b391d74761ac681e7f7705ab34/002.receipt.json
  - checkpoint: ee2839f81e9dadb19f146a8e772bb22a7f9299313cbf0ad8d8e650f401e45410.json
    topic: algorithm
    part: proxy-success
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 3ad154b391d74761ac681e7f7705ab34/003.receipt.json
    - 3ad154b391d74761ac681e7f7705ab34/004.receipt.json
  - checkpoint: e08b9da40deb51f3d93107cfbe560ece53101ef7716f1770a7aa8f2b83a86f50.json
    topic: shutdown
    part: order
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/053.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/054.receipt.json
  - checkpoint: 436e9d47e1300bc355bec6c1ee977fa8a140c320016532b144579a61e5119560.json
    topic: shutdown
    part: rationale
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/055.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/056.receipt.json
  - checkpoint: a5293854ebff5642f10879ebdbc2e72f5bfcbb651952d889954fc4b21cc168c1.json
    topic: shutdown
    part: device
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/057.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/058.receipt.json
  - checkpoint: 620c1a146e6f4407dfc87cdb733fb4625e8d5b3b28545cc06b4ef6670f0f4772.json
    topic: shutdown
    part: waiting
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/059.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/060.receipt.json
  - checkpoint: 86f0836dc5c45f319e40e447c219e40a91cd42148ea583858b7d4a8f739daa82.json
    topic: shutdown
    part: final-state
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/061.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/062.receipt.json
  - checkpoint: 4f0cec35f6a588dbbf8eade089d71f2c3617e97cd83d2e9089fe997a4e0cb17f.json
    topic: validation
    part: lifetime
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/063.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/064.receipt.json
  - checkpoint: a5809c4e93d8c3d0d9235cabca5de52dc0b25e565eb2275d140360e16131b5a8.json
    topic: validation
    part: order
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/065.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/066.receipt.json
  - checkpoint: be3b9343223db159861b744a23bfbe7acbad2f54b6ebf2b519fa9c447ce2e22d.json
    topic: validation
    part: context
    subpart: null
    revalidated: false
    new_grounding_review: false
    receipts:
    - 1d97c62c9a614425831b4c6f6a62d72c/067.receipt.json
    - 1d97c62c9a614425831b4c6f6a62d72c/068.receipt.json
  body_sha256: afb1e83e788dca16ce874ea1ddd69a51e72a4447c9fb8f815eca6d6fd4f58989
generated_visuals:
  schema: 1
  records:
    handler-configuration-contracts:
      input_fingerprint: 0196dd711c6f04d1aca167fe354c6580e23a2a89d699cb266e87f9a1f38461f7
      draft:
        nodes:
        - id: generate
          symbol: generateConfiguration
          label: generateConfiguration은 camera와 roles를 입력받습니다. caller는 기본 구성을 원하는
            사용 사례를 roles에 채워야 합니다.
          label_en: generateConfiguration takes camera and roles. The caller must
            populate roles with the use cases for which it wants a default configuration.
          shape: process
          quote_ids:
          - generate-api:0
        - id: result
          symbol: CameraConfiguration
          label: 요청한 roles를 만족할 수 있으면 유효한 CameraConfiguration을 반환하고, 그렇지 않으면 null
            포인터를 반환합니다.
          label_en: It returns a valid CameraConfiguration if the requested roles
            can be satisfied, or a null pointer otherwise.
          shape: box
          quote_ids:
          - generate-api:0
        - id: inspection
          symbol: caller
          label: non-null CameraConfiguration이 반환된 경우 caller는 선택된 streams와 그 기본 parameters를
            살펴볼 수 있습니다.
          label_en: When a non-null CameraConfiguration is returned, the caller can
            inspect the selected streams and their default parameters.
          shape: box
          quote_ids:
          - generate-api:0
        - id: configure
          symbol: configure
          label: configure는 camera와 config를 입력받습니다. config는 이미 검증되었으며 구현은 추가 검증을 해서는
            안 됩니다.
          label_en: configure takes camera and config. The config is already validated,
            and the implementation must not perform further validation.
          shape: process
          quote_ids:
          - configure-api:0
        - id: return
          symbol: negative
          label: configure는 성공하면 0을 반환하고, 그렇지 않으면 음수 오류 코드를 반환합니다.
          label_en: configure returns 0 on success or a negative error code otherwise.
          shape: box
          quote_ids:
          - configure-api:0
        - id: setstream
          symbol: setStream
          label: 파이프라인 핸들러는 카메라를 구성할 때 setStream으로 각 StreamConfiguration 항목에 Stream
            인스턴스를 연결해야 합니다.
          label_en: When configuring the camera, the pipeline handler must use setStream
            to associate a Stream instance with each StreamConfiguration entry.
          shape: process
          quote_ids:
          - configure-api:0
        edges:
        - from: generate
          to: result
          label: generateConfiguration은 요청을 만족할 수 있는지에 따라 결과를 반환합니다.
          label_en: generateConfiguration returns a result based on whether the request
            can be satisfied.
          condition_ref: always
          quote_ids:
          - generate-api:0
        - from: result
          to: inspection
          label: non-null CameraConfiguration이 반환되면 caller가 구성을 살펴볼 수 있습니다.
          label_en: When a non-null CameraConfiguration is returned, the caller can
            inspect it.
          condition_ref: always
          quote_ids:
          - generate-api:0
        - from: generate
          to: configure
          label: configure는 스트림 매개변수를 바꾸는 데 쓸 수 있는 companion API입니다.
          label_en: configure is the companion API that can be used to change stream
            parameters.
          condition_ref: always
          quote_ids:
          - generate-api:0
        - from: configure
          to: setstream
          label: 카메라를 구성할 때 각 항목에 Stream을 연결해야 합니다.
          label_en: When configuring the camera, it must associate a Stream with each
            entry.
          condition_ref: always
          quote_ids:
          - configure-api:0
        - from: configure
          to: return
          label: configure는 성공 또는 오류 결과를 반환합니다.
          label_en: configure returns a success or error result.
          condition_ref: always
          quote_ids:
          - configure-api:0
      graph:
        id: handler-configuration-contracts
        topic: configuration
        kind: ownership
        title: 설정 인터페이스별 입력과 결과
        question: generateConfiguration과 configure의 입력·반환 및 성공 시 Stream 연결 의무는 무엇입니까?
        condition_display: inline
        nodes:
        - id: generate
          label: generateConfiguration은 camera와 roles를 입력받습니다. caller는 기본 구성을 원하는
            사용 사례를 roles에 채워야 합니다.
          label_en: generateConfiguration takes camera and roles. The caller must
            populate roles with the use cases for which it wants a default configuration.
          shape: box
          evidence:
          - source: configuration/generate-api
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
        - id: result
          label: 요청한 roles를 만족할 수 있으면 유효한 CameraConfiguration을 반환하고, 그렇지 않으면 null
            포인터를 반환합니다.
          label_en: It returns a valid CameraConfiguration if the requested roles
            can be satisfied, or a null pointer otherwise.
          shape: box
          evidence:
          - source: configuration/generate-api
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
        - id: inspection
          label: non-null CameraConfiguration이 반환된 경우 caller는 선택된 streams와 그 기본 parameters를
            살펴볼 수 있습니다.
          label_en: When a non-null CameraConfiguration is returned, the caller can
            inspect the selected streams and their default parameters.
          shape: box
          evidence:
          - source: configuration/generate-api
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
        - id: configure
          label: configure는 camera와 config를 입력받습니다. config는 이미 검증되었으며 구현은 추가 검증을 해서는
            안 됩니다.
          label_en: configure takes camera and config. The config is already validated,
            and the implementation must not perform further validation.
          shape: box
          evidence:
          - source: configuration/configure-api
            sha256: 5b219c0d287985da85343ebfed58f2c0ab7fc65635129141016b21bd45969a40
            quote: "\\fn PipelineHandler::configure()\n * \\brief Configure a group\
              \ of streams for capture\n * \\param[in] camera The camera to configure\n\
              \ * \\param[in] config The camera configurations to setup\n *\n * Configure\
              \ the specified group of streams for \\a camera according to the\n *\
              \ configuration specified in \\a config. The intended caller of this\
              \ interface\n * is the Camera class which will receive configuration\
              \ to apply from the\n * application.\n *\n * The configuration is guaranteed\
              \ to have been validated with\n * CameraConfiguration::validate(). The\
              \ pipeline handler implementation shall\n * not perform further validation\
              \ and may rely on any custom field stored in its\n * custom CameraConfiguration\
              \ derived class.\n *\n * When configuring the camera the pipeline handler\
              \ shall associate a Stream\n * instance to each StreamConfiguration\
              \ entry in the CameraConfiguration using\n * the StreamConfiguration::setStream()\
              \ function.\n *\n * \\context This function is called from the CameraManager\
              \ thread.\n *\n * \\return 0 on success or a negative error code otherwise\n\
              \ */"
        - id: return
          label: configure는 성공하면 0을 반환하고, 그렇지 않으면 음수 오류 코드를 반환합니다.
          label_en: configure returns 0 on success or a negative error code otherwise.
          shape: box
          evidence:
          - source: configuration/configure-api
            sha256: 5b219c0d287985da85343ebfed58f2c0ab7fc65635129141016b21bd45969a40
            quote: "\\fn PipelineHandler::configure()\n * \\brief Configure a group\
              \ of streams for capture\n * \\param[in] camera The camera to configure\n\
              \ * \\param[in] config The camera configurations to setup\n *\n * Configure\
              \ the specified group of streams for \\a camera according to the\n *\
              \ configuration specified in \\a config. The intended caller of this\
              \ interface\n * is the Camera class which will receive configuration\
              \ to apply from the\n * application.\n *\n * The configuration is guaranteed\
              \ to have been validated with\n * CameraConfiguration::validate(). The\
              \ pipeline handler implementation shall\n * not perform further validation\
              \ and may rely on any custom field stored in its\n * custom CameraConfiguration\
              \ derived class.\n *\n * When configuring the camera the pipeline handler\
              \ shall associate a Stream\n * instance to each StreamConfiguration\
              \ entry in the CameraConfiguration using\n * the StreamConfiguration::setStream()\
              \ function.\n *\n * \\context This function is called from the CameraManager\
              \ thread.\n *\n * \\return 0 on success or a negative error code otherwise\n\
              \ */"
        - id: setstream
          label: 파이프라인 핸들러는 카메라를 구성할 때 setStream으로 각 StreamConfiguration 항목에 Stream
            인스턴스를 연결해야 합니다.
          label_en: When configuring the camera, the pipeline handler must use setStream
            to associate a Stream instance with each StreamConfiguration entry.
          shape: box
          evidence:
          - source: configuration/configure-api
            sha256: 5b219c0d287985da85343ebfed58f2c0ab7fc65635129141016b21bd45969a40
            quote: "\\fn PipelineHandler::configure()\n * \\brief Configure a group\
              \ of streams for capture\n * \\param[in] camera The camera to configure\n\
              \ * \\param[in] config The camera configurations to setup\n *\n * Configure\
              \ the specified group of streams for \\a camera according to the\n *\
              \ configuration specified in \\a config. The intended caller of this\
              \ interface\n * is the Camera class which will receive configuration\
              \ to apply from the\n * application.\n *\n * The configuration is guaranteed\
              \ to have been validated with\n * CameraConfiguration::validate(). The\
              \ pipeline handler implementation shall\n * not perform further validation\
              \ and may rely on any custom field stored in its\n * custom CameraConfiguration\
              \ derived class.\n *\n * When configuring the camera the pipeline handler\
              \ shall associate a Stream\n * instance to each StreamConfiguration\
              \ entry in the CameraConfiguration using\n * the StreamConfiguration::setStream()\
              \ function.\n *\n * \\context This function is called from the CameraManager\
              \ thread.\n *\n * \\return 0 on success or a negative error code otherwise\n\
              \ */"
        edges:
        - from: generate
          to: result
          label: generateConfiguration은 요청을 만족할 수 있는지에 따라 결과를 반환합니다.
          label_en: generateConfiguration returns a result based on whether the request
            can be satisfied.
          evidence:
          - source: configuration/generate-api
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
        - from: result
          to: inspection
          label: non-null CameraConfiguration이 반환되면 caller가 구성을 살펴볼 수 있습니다.
          label_en: When a non-null CameraConfiguration is returned, the caller can
            inspect it.
          evidence:
          - source: configuration/generate-api
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
        - from: generate
          to: configure
          label: configure는 스트림 매개변수를 바꾸는 데 쓸 수 있는 companion API입니다.
          label_en: configure is the companion API that can be used to change stream
            parameters.
          evidence:
          - source: configuration/generate-api
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
        - from: configure
          to: setstream
          label: 카메라를 구성할 때 각 항목에 Stream을 연결해야 합니다.
          label_en: When configuring the camera, it must associate a Stream with each
            entry.
          evidence:
          - source: configuration/configure-api
            sha256: 5b219c0d287985da85343ebfed58f2c0ab7fc65635129141016b21bd45969a40
            quote: "\\fn PipelineHandler::configure()\n * \\brief Configure a group\
              \ of streams for capture\n * \\param[in] camera The camera to configure\n\
              \ * \\param[in] config The camera configurations to setup\n *\n * Configure\
              \ the specified group of streams for \\a camera according to the\n *\
              \ configuration specified in \\a config. The intended caller of this\
              \ interface\n * is the Camera class which will receive configuration\
              \ to apply from the\n * application.\n *\n * The configuration is guaranteed\
              \ to have been validated with\n * CameraConfiguration::validate(). The\
              \ pipeline handler implementation shall\n * not perform further validation\
              \ and may rely on any custom field stored in its\n * custom CameraConfiguration\
              \ derived class.\n *\n * When configuring the camera the pipeline handler\
              \ shall associate a Stream\n * instance to each StreamConfiguration\
              \ entry in the CameraConfiguration using\n * the StreamConfiguration::setStream()\
              \ function.\n *\n * \\context This function is called from the CameraManager\
              \ thread.\n *\n * \\return 0 on success or a negative error code otherwise\n\
              \ */"
        - from: configure
          to: return
          label: configure는 성공 또는 오류 결과를 반환합니다.
          label_en: configure returns a success or error result.
          evidence:
          - source: configuration/configure-api
            sha256: 5b219c0d287985da85343ebfed58f2c0ab7fc65635129141016b21bd45969a40
            quote: "\\fn PipelineHandler::configure()\n * \\brief Configure a group\
              \ of streams for capture\n * \\param[in] camera The camera to configure\n\
              \ * \\param[in] config The camera configurations to setup\n *\n * Configure\
              \ the specified group of streams for \\a camera according to the\n *\
              \ configuration specified in \\a config. The intended caller of this\
              \ interface\n * is the Camera class which will receive configuration\
              \ to apply from the\n * application.\n *\n * The configuration is guaranteed\
              \ to have been validated with\n * CameraConfiguration::validate(). The\
              \ pipeline handler implementation shall\n * not perform further validation\
              \ and may rely on any custom field stored in its\n * custom CameraConfiguration\
              \ derived class.\n *\n * When configuring the camera the pipeline handler\
              \ shall associate a Stream\n * instance to each StreamConfiguration\
              \ entry in the CameraConfiguration using\n * the StreamConfiguration::setStream()\
              \ function.\n *\n * \\context This function is called from the CameraManager\
              \ thread.\n *\n * \\return 0 on success or a negative error code otherwise\n\
              \ */"
        producer: cli/codex/gpt-6.1-terra
      producer: cli/codex/gpt-6.1-terra
      generation_commit: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
      citation_binding_policy: identifier-and-guard-boundaries-v2
      reused: true
  body_sha256: afb1e83e788dca16ce874ea1ddd69a51e72a4447c9fb8f815eca6d6fd4f58989
managed_visual_refresh:
- schema: 1
  source_commit: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
  original_manuscript_sha256: fe4e79cb19712c6833d47522b1b83be5d0b6a5d628b462bea77a0f85dcdfb858
  previous_body_sha256: d6ff9d5404e58f38a34e0a3f1eb5bf764b8fd789cf05dace48d57f80cee6700e
  body_sha256: afb1e83e788dca16ce874ea1ddd69a51e72a4447c9fb8f815eca6d6fd4f58989
  visual_definitions_sha256: 7e07d24786d418628e3a7a110cfd78c1d1d69f01f852a78d36650c9ef602500d
  unchanged_native_records_sha256: 7d891090a49b0e9b55ac59401193c6c34e541fc9fbaa88e271bb40c43ae89469
  preserved_outside_body_sha256: faee809122fc6767d11112fd10bf22e2fe0a5599a46d331d56619cc10f7207c2
  owned_edit_regions:
  - original_start_byte: 1380
    original_end_byte: 4179
    original_sha256: 5a0cb8652d3edc82dc78d3b31b43130a0145dc6b7136f0243d70005c3e773484
    replacement_sha256: 5a0cb8652d3edc82dc78d3b31b43130a0145dc6b7136f0243d70005c3e773484
    visual_ids:
    - integration-stages
  - original_start_byte: 5484
    original_end_byte: 10923
    original_sha256: f7cf2ccf9a95c7185f587fb085b5ca30b32a18c2b63b6ed9029becd2d11ce270
    replacement_sha256: f7cf2ccf9a95c7185f587fb085b5ca30b32a18c2b63b6ed9029becd2d11ce270
    visual_ids:
    - item-boundary
  - original_start_byte: 11961
    original_end_byte: 20581
    original_sha256: 098e89237be4486f6154fa3f49467a22ef4fbb1d071b44dc1bdd7eb5d6b96651
    replacement_sha256: 098e89237be4486f6154fa3f49467a22ef4fbb1d071b44dc1bdd7eb5d6b96651
    visual_ids:
    - handler-configuration-contracts
  - original_start_byte: 23054
    original_end_byte: 23054
    original_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    replacement_sha256: a5dd9fd656f7b4a5813d8ef9a6559256ced3b0da4fd23b767f17b8f1909d77a9
    visual_ids:
    - device-queue-and-completion
  - original_start_byte: 24911
    original_end_byte: 33226
    original_sha256: b55c86abd5c55b721550637a9cf6537511f022bc41405ec26d6c749b027cf9ce
    replacement_sha256: 2b998799d4b6ada71cfd0df5c786c5771c8e323dc89e2f0582fc30b5e3a0ae8a
    visual_ids:
    - item-algorithm
  - original_start_byte: 34842
    original_end_byte: 34842
    original_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    replacement_sha256: cd47d06488df0f7acec9efcaa5a9259d407906c64d57912dd6419a577a6e082b
    visual_ids:
    - shutdown-device-and-waiting-requests
  added_visuals:
  - device-queue-and-completion
  - shutdown-device-and-waiting-requests
  scope: Configured figure reassembly only; figure authorship remains per visual
  new_inference: false
  semantic_approval: false
  human_review: unchanged
---

# 연동 가이드

**연동 순서와 구현 책임을 확인하고 설정·요청·정지 계약을 적용하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 제품이 무엇이고 어디까지 지원하는지, 공통 설계가 구현자에게 해 주는 일을 확인하고 도입할 범위를 판단하세요. | [libcamera 제품 개요](vendor-overview.md) |
| 지원 조건과 구성 제약을 확인하고 제품 도입 전에 검증할 범위를 정하세요. | [지원 범위와 검증](vendor-assurance.md) |
| 파이프라인 구현이 지켜야 하는 구성·요청·완료·종료 계약을 확인하세요. | [Pipeline Handler](pipeline-handler.md) |

## 연동 순서와 책임

애플리케이션은 촬영을 준비하려면 카메라를 확보하고 구성해야 하며, 카메라를 시작하면 정지할 때까지 요청을 처리할 수 있고, 사용을 마치면 카메라를 해제해야 합니다. 애플리케이션은 카메라를 해제하지 않은 동안 여러 번 시작하고 정지할 수 있으며, 카메라를 재구성할 수도 있습니다. `Camera` 클래스는 카메라 상태에 영향을 주는 함수들을 일반적으로 서로 동기화하지 않으므로, 필요한 경우 호출자가 동기화해야 합니다. `src/libcamera/camera.cpp:771`, `src/libcamera/camera.cpp:777`, `src/libcamera/camera.cpp:780`

<!-- sdd:visual:integration-stages -->
### 획득부터 해제까지의 연동 순서

```mermaid
flowchart TB
%% sdd:translations {"구성": "Configure", "사용 종료 후 해제": "Release when finished", "세션 종료": "End capture session", "시작·요청 처리": "Start and process requests", "정지": "Stop", "준비 뒤 시작": "Start after preparation", "촬영 준비": "Prepare capture", "카메라 사용이 끝난 경우": "When finished using the <br/>camera", "해제 전에는 재시작 가능": "May restart before release", "획득": "Acquire"}
  v_acquire["획득"]
  v_configure["구성"]
  v_start["시작·요청 처리"]
  v_stop["정지"]
  v_release["사용 종료 후 해제"]
  v_acquire -->|"촬영 준비"| v_configure
  v_configure -->|"준비 뒤 시작"| v_start
  v_start -->|"세션 종료"| v_stop
  v_stop -->|"카메라 사용이 끝난 경우"| v_release
  v_stop -->|"해제 전에는 재시작 가능"| v_start
```

[Mermaid 원문](vendor-integration.integration-stages.mmd)

??? note "그림 근거와 확인 범위"
    애플리케이션의 세션 준비와 종료 순서입니다. 시작·정지는 해제 전까지 반복할 수 있습니다.
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Acquire">획득</span> | [src/libcamera/camera.cpp:771](#source-2683b4a5a1dbfee9) |
    | <span data-sdd-label-en="Configure">구성</span> | [src/libcamera/camera.cpp:771](#source-2683b4a5a1dbfee9) |
    | <span data-sdd-label-en="Start and process requests">시작·요청 처리</span> | [src/libcamera/camera.cpp:771](#source-2683b4a5a1dbfee9) |
    | <span data-sdd-label-en="Stop">정지</span> | [src/libcamera/camera.cpp:771](#source-2683b4a5a1dbfee9) |
    | <span data-sdd-label-en="Release when finished">사용 종료 후 해제</span> | [src/libcamera/camera.cpp:771](#source-2683b4a5a1dbfee9) |
    | <span data-sdd-label-en="Prepare capture">촬영 준비</span> | [src/libcamera/camera.cpp:771](#source-2683b4a5a1dbfee9) |
    | <span data-sdd-label-en="Start after preparation">준비 뒤 시작</span> | [src/libcamera/camera.cpp:771](#source-2683b4a5a1dbfee9) |
    | <span data-sdd-label-en="End capture session">세션 종료</span> | [src/libcamera/camera.cpp:771](#source-2683b4a5a1dbfee9) |
    | <span data-sdd-label-en="When finished using the camera">카메라 사용이 끝난 경우</span> | [src/libcamera/camera.cpp:771](#source-2683b4a5a1dbfee9) |
    | <span data-sdd-label-en="May restart before release">해제 전에는 재시작 가능</span> | [src/libcamera/camera.cpp:777](#source-948bd80fa1136291) |
<!-- /sdd:visual:integration-stages -->

근거 원문: [src/libcamera/camera.cpp:771](#source-2683b4a5a1dbfee9) · [src/libcamera/camera.cpp:780](#source-cc6c66b57cf028e6) · [src/libcamera/camera.cpp:777](#source-948bd80fa1136291) · [src/libcamera/camera.cpp:1032](#source-492118d913b10361)

## 하드웨어와 공통 계층의 경계

`PipelineHandler::match()` 구현자는 단일 파이프라인에 필요한 미디어 장치를 모두 찾으면 각 장치에 대해 `MediaDevice::acquire()`를 호출해 확보한 다음, 해당 `Camera` 인스턴스를 하나 이상 생성하고 내부에 저장하며 카메라 매니저에 등록한 뒤 `true`를 반환해야 합니다. `PipelineHandler::match()` 구현자는 필요한 미디어 장치를 모두 찾지 못했을 때 아직 장치를 확보하지 않았다면 어떤 장치도 확보해서는 안 되며, 이미 일부를 확보했다면 `MediaDevice::release()`를 호출해 확보한 장치를 모두 해제하고 `false`를 반환해야 합니다. `PipelineHandler::match()`는 `CameraManager` 스레드에서 호출되며, `true`를 반환하면 새로운 `PipelineHandler` 인스턴스가 생성되고 그 인스턴스의 `match()`가 호출됩니다. `src/libcamera/pipeline_handler.cpp:91`, `src/libcamera/pipeline_handler.cpp:97`, `src/libcamera/pipeline_handler.cpp:109`

<!-- sdd:visual:item-boundary -->
### 장치 매칭의 확보·등록과 실패 정리

```mermaid
flowchart TB
%% sdd:translations {"CameraManager가 열거자를 <br/>넘겨 match를 호출합니다.": "CameraManager calls match <br/>with the enumerator.", "match 구현자가 매칭을 <br/>확인합니다.": "The match implementation <br/>checks the devices.", "true를 반환했습니다.": "The call returned true.", "모두 찾았습니다.": "All required devices were <br/>found.", "새 핸들러 인스턴스를 만들고 <br/>다시 match를 호출합니다.": "Create a new handler <br/>instance and call match <br/>again.", "이 파이프라인에 필요한 <br/>미디어 장치를 모두 <br/>찾았습니까?": "Were all media devices <br/>required for this pipeline <br/>found?", "이 파이프라인에 필요한 <br/>장치를 모두 확보합니다.": "Acquire all devices <br/>required for this pipeline.", "장치를 확보하지 않거나 이미 <br/>확보한 장치를 모두 해제한 <br/>뒤 false를 반환합니다.": "Acquire no devices, or <br/>release all devices already <br/>acquired, then return false.", "카메라를 생성·보관하고 <br/>매니저에 등록한 뒤 true를 <br/>반환합니다.": "Create and store the <br/>cameras, register them with <br/>CameraManager, then return <br/>true.", "필요한 장치가 부족합니다.": "A required device is <br/>missing.", "확보한 뒤 카메라를 <br/>등록합니다.": "Register the cameras after <br/>acquisition."}
  v_call["CameraManager가 열거자를 <br/>넘겨 match를 호출합니다."]
  v_found{"이 파이프라인에 필요한 <br/>미디어 장치를 모두 <br/>찾았습니까?"}
  v_acquire["이 파이프라인에 필요한 <br/>장치를 모두 확보합니다."]
  v_register["카메라를 생성·보관하고 <br/>매니저에 등록한 뒤 true를 <br/>반환합니다."]
  v_repeat["새 핸들러 인스턴스를 만들고 <br/>다시 match를 호출합니다."]
  v_failure["장치를 확보하지 않거나 이미 <br/>확보한 장치를 모두 해제한 <br/>뒤 false를 반환합니다."]
  v_call -->|"match 구현자가 매칭을 <br/>확인합니다."| v_found
  v_found -->|"모두 찾았습니다."| v_acquire
  v_found -->|"필요한 장치가 부족합니다."| v_failure
  v_acquire -->|"확보한 뒤 카메라를 <br/>등록합니다."| v_register
  v_register -->|"true를 반환했습니다."| v_repeat
```

[Mermaid 원문](vendor-integration.item-boundary.mmd)

??? note "그림 근거와 확인 범위"
    누가 장치를 매칭하고 카메라를 등록하며, 매칭 결과에 따라 확보한 장치는 어떻게 처리됩니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="CameraManager calls match with the enumerator.">CameraManager가 열거자를 넘겨 match를 호출합니다.</span> | [src/libcamera/pipeline_handler.cpp:91](#source-5109302527925a6a) |
    | <span data-sdd-label-en="Were all media devices required for this pipeline found?">이 파이프라인에 필요한 미디어 장치를 모두 찾았습니까?</span> | [src/libcamera/pipeline_handler.cpp:91](#source-5109302527925a6a) |
    | <span data-sdd-label-en="Acquire all devices required for this pipeline.">이 파이프라인에 필요한 장치를 모두 확보합니다.</span> | [src/libcamera/pipeline_handler.cpp:91](#source-5109302527925a6a) |
    | <span data-sdd-label-en="Create and store the cameras, register them with CameraManager, then return true.">카메라를 생성·보관하고 매니저에 등록한 뒤 true를 반환합니다.</span> | [src/libcamera/pipeline_handler.cpp:91](#source-5109302527925a6a) |
    | <span data-sdd-label-en="Create a new handler instance and call match again.">새 핸들러 인스턴스를 만들고 다시 match를 호출합니다.</span> | [src/libcamera/pipeline_handler.cpp:109](#source-1afff120b5d66b3c) |
    | <span data-sdd-label-en="Acquire no devices, or release all devices already acquired, then return false.">장치를 확보하지 않거나 이미 확보한 장치를 모두 해제한 뒤 false를 반환합니다.</span> | [src/libcamera/pipeline_handler.cpp:97](#source-293bf5d4775550d0) |
    | <span data-sdd-label-en="The match implementation checks the devices.">match 구현자가 매칭을 확인합니다.</span> | [src/libcamera/pipeline_handler.cpp:91](#source-5109302527925a6a) |
    | <span data-sdd-label-en="All required devices were found.">모두 찾았습니다.</span> | [src/libcamera/pipeline_handler.cpp:91](#source-5109302527925a6a) |
    | <span data-sdd-label-en="A required device is missing.">필요한 장치가 부족합니다.</span> | [src/libcamera/pipeline_handler.cpp:91](#source-5109302527925a6a) · [src/libcamera/pipeline_handler.cpp:97](#source-293bf5d4775550d0) |
    | <span data-sdd-label-en="Register the cameras after acquisition.">확보한 뒤 카메라를 등록합니다.</span> | [src/libcamera/pipeline_handler.cpp:91](#source-5109302527925a6a) |
    | <span data-sdd-label-en="The call returned true.">true를 반환했습니다.</span> | [src/libcamera/pipeline_handler.cpp:91](#source-5109302527925a6a) · [src/libcamera/pipeline_handler.cpp:109](#source-1afff120b5d66b3c) |
<!-- /sdd:visual:item-boundary -->

근거 원문: [src/libcamera/pipeline_handler.cpp:91](#source-5109302527925a6a) · [src/libcamera/pipeline_handler.cpp:109](#source-1afff120b5d66b3c) · [src/libcamera/pipeline_handler.cpp:97](#source-293bf5d4775550d0)

## 구현할 설정 인터페이스

`generateConfiguration`의 호출자는 기본 구성을 가져오려는 사용 사례를 `roles`에 채워야 합니다. `generateConfiguration()`이 반환하는 구성은 선택된 스트림과 그 스트림의 기본 파라미터를 호출자가 확인할 수 있는 정보를 포함합니다. `PipelineHandler::generateConfiguration()`은 요청된 `roles`를 충족할 수 있으면 유효한 `CameraConfiguration`을 반환하고, 그렇지 않으면 `null` 포인터를 반환해야 합니다. `PipelineHandler::generateConfiguration()` 구현은 어떤 스레드에서든 호출될 수 있으므로 스레드 안전성을 갖춰야 합니다. `src/libcamera/pipeline_handler.cpp:276`, `src/libcamera/pipeline_handler.cpp:289`, `src/libcamera/pipeline_handler.cpp:285`

<!-- sdd:visual:handler-configuration-contracts -->
### 설정 인터페이스별 입력과 결과

```mermaid
flowchart TB
%% sdd:translations {"configure는 camera와 <br/>config를 입력받습니다. <br/>config는 이미 검증되었으며 <br/>구현은 추가 검증을 해서는 <br/>안 됩니다.": "configure takes camera and <br/>config. The config is <br/>already validated, and the <br/>implementation must not <br/>perform further validation.", "configure는 성공 또는 오류 <br/>결과를 반환합니다.": "configure returns a success <br/>or error result.", "configure는 성공하면 0을 <br/>반환하고, 그렇지 않으면 <br/>음수 오류 코드를 반환합니다.": "configure returns 0 on <br/>success or a negative error <br/>code otherwise.", "configure는 스트림 <br/>매개변수를 바꾸는 데 쓸 수 <br/>있는 companion API입니다.": "configure is the companion <br/>API that can be used to <br/>change stream parameters.", "generateConfiguration은 <br/>camera와 roles를 <br/>입력받습니다. caller는 기본 <br/>구성을 원하는 사용 사례를 <br/>roles에 채워야 합니다.": "generateConfiguration takes <br/>camera and roles. The <br/>caller must populate roles <br/>with the use cases for <br/>which it wants a default <br/>configuration.", "generateConfiguration은 <br/>요청을 만족할 수 있는지에 <br/>따라 결과를 반환합니다.": "generateConfiguration <br/>returns a result based on <br/>whether the request can be <br/>satisfied.", "non-null <br/>CameraConfiguration이 <br/>반환되면 caller가 구성을 <br/>살펴볼 수 있습니다.": "When a non-null <br/>CameraConfiguration is <br/>returned, the caller can <br/>inspect it.", "non-null <br/>CameraConfiguration이 <br/>반환된 경우 caller는 선택된 <br/>streams와 그 기본 <br/>parameters를 살펴볼 수 <br/>있습니다.": "When a non-null <br/>CameraConfiguration is <br/>returned, the caller can <br/>inspect the selected <br/>streams and their default <br/>parameters.", "요청한 roles를 만족할 수 <br/>있으면 유효한 <br/>CameraConfiguration을 <br/>반환하고, 그렇지 않으면 <br/>null 포인터를 반환합니다.": "It returns a valid <br/>CameraConfiguration if the <br/>requested roles can be <br/>satisfied, or a null <br/>pointer otherwise.", "카메라를 구성할 때 각 <br/>항목에 Stream을 연결해야 <br/>합니다.": "When configuring the <br/>camera, it must associate a <br/>Stream with each entry.", "파이프라인 핸들러는 <br/>카메라를 구성할 때 <br/>setStream으로 각 <br/>StreamConfiguration 항목에 <br/>Stream 인스턴스를 연결해야 <br/>합니다.": "When configuring the <br/>camera, the pipeline <br/>handler must use setStream <br/>to associate a Stream <br/>instance with each <br/>StreamConfiguration entry."}
  v_generate["generateConfiguration은 <br/>camera와 roles를 <br/>입력받습니다. caller는 기본 <br/>구성을 원하는 사용 사례를 <br/>roles에 채워야 합니다."]
  v_result["요청한 roles를 만족할 수 <br/>있으면 유효한 <br/>CameraConfiguration을 <br/>반환하고, 그렇지 않으면 <br/>null 포인터를 반환합니다."]
  v_inspection["non-null <br/>CameraConfiguration이 <br/>반환된 경우 caller는 선택된 <br/>streams와 그 기본 <br/>parameters를 살펴볼 수 <br/>있습니다."]
  v_configure["configure는 camera와 <br/>config를 입력받습니다. <br/>config는 이미 검증되었으며 <br/>구현은 추가 검증을 해서는 <br/>안 됩니다."]
  v_return["configure는 성공하면 0을 <br/>반환하고, 그렇지 않으면 <br/>음수 오류 코드를 반환합니다."]
  v_setstream["파이프라인 핸들러는 <br/>카메라를 구성할 때 <br/>setStream으로 각 <br/>StreamConfiguration 항목에 <br/>Stream 인스턴스를 연결해야 <br/>합니다."]
  v_generate -->|"generateConfiguration은 <br/>요청을 만족할 수 있는지에 <br/>따라 결과를 반환합니다."| v_result
  v_result -->|"non-null <br/>CameraConfiguration이 <br/>반환되면 caller가 구성을 <br/>살펴볼 수 있습니다."| v_inspection
  v_generate -->|"configure는 스트림 <br/>매개변수를 바꾸는 데 쓸 수 <br/>있는 companion API입니다."| v_configure
  v_configure -->|"카메라를 구성할 때 각 <br/>항목에 Stream을 연결해야 <br/>합니다."| v_setstream
  v_configure -->|"configure는 성공 또는 오류 <br/>결과를 반환합니다."| v_return
```

[Mermaid 원문](vendor-integration.handler-configuration-contracts.mmd)

??? note "그림 근거와 확인 범위"
    generateConfiguration과 configure의 입력·반환 및 성공 시 Stream 연결 의무는 무엇입니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="generateConfiguration takes camera and roles. The caller must populate roles with the use cases for which it wants a default configuration.">generateConfiguration은 camera와 roles를 입력받습니다. caller는 기본 구성을 원하는 사용 사례를 roles에 채워야 합니다.</span> | [src/libcamera/pipeline_handler.cpp:271](#source-23ff032cd1152d56) |
    | <span data-sdd-label-en="It returns a valid CameraConfiguration if the requested roles can be satisfied, or a null pointer otherwise.">요청한 roles를 만족할 수 있으면 유효한 CameraConfiguration을 반환하고, 그렇지 않으면 null 포인터를 반환합니다.</span> | [src/libcamera/pipeline_handler.cpp:271](#source-23ff032cd1152d56) |
    | <span data-sdd-label-en="When a non-null CameraConfiguration is returned, the caller can inspect the selected streams and their default parameters.">non-null CameraConfiguration이 반환된 경우 caller는 선택된 streams와 그 기본 parameters를 살펴볼 수 있습니다.</span> | [src/libcamera/pipeline_handler.cpp:271](#source-23ff032cd1152d56) |
    | <span data-sdd-label-en="configure takes camera and config. The config is already validated, and the implementation must not perform further validation.">configure는 camera와 config를 입력받습니다. config는 이미 검증되었으며 구현은 추가 검증을 해서는 안 됩니다.</span> | [src/libcamera/pipeline_handler.cpp:294](#source-4255f8449e37ebb8) |
    | <span data-sdd-label-en="configure returns 0 on success or a negative error code otherwise.">configure는 성공하면 0을 반환하고, 그렇지 않으면 음수 오류 코드를 반환합니다.</span> | [src/libcamera/pipeline_handler.cpp:294](#source-4255f8449e37ebb8) |
    | <span data-sdd-label-en="When configuring the camera, the pipeline handler must use setStream to associate a Stream instance with each StreamConfiguration entry.">파이프라인 핸들러는 카메라를 구성할 때 setStream으로 각 StreamConfiguration 항목에 Stream 인스턴스를 연결해야 합니다.</span> | [src/libcamera/pipeline_handler.cpp:294](#source-4255f8449e37ebb8) |
    | <span data-sdd-label-en="generateConfiguration returns a result based on whether the request can be satisfied.">generateConfiguration은 요청을 만족할 수 있는지에 따라 결과를 반환합니다.</span> | [src/libcamera/pipeline_handler.cpp:271](#source-23ff032cd1152d56) |
    | <span data-sdd-label-en="When a non-null CameraConfiguration is returned, the caller can inspect it.">non-null CameraConfiguration이 반환되면 caller가 구성을 살펴볼 수 있습니다.</span> | [src/libcamera/pipeline_handler.cpp:271](#source-23ff032cd1152d56) |
    | <span data-sdd-label-en="configure is the companion API that can be used to change stream parameters.">configure는 스트림 매개변수를 바꾸는 데 쓸 수 있는 companion API입니다.</span> | [src/libcamera/pipeline_handler.cpp:271](#source-23ff032cd1152d56) |
    | <span data-sdd-label-en="When configuring the camera, it must associate a Stream with each entry.">카메라를 구성할 때 각 항목에 Stream을 연결해야 합니다.</span> | [src/libcamera/pipeline_handler.cpp:294](#source-4255f8449e37ebb8) |
    | <span data-sdd-label-en="configure returns a success or error result.">configure는 성공 또는 오류 결과를 반환합니다.</span> | [src/libcamera/pipeline_handler.cpp:294](#source-4255f8449e37ebb8) |
<!-- /sdd:visual:handler-configuration-contracts -->

`PipelineHandler::generateConfiguration()` 구현자는 파이프라인 핸들러 내에서 `camera`의 상태를 변경해서는 안 됩니다. `PipelineHandler::configure()`에 전달되는 설정은 `CameraConfiguration::validate()`로 검증되었음이 보장되므로, 파이프라인 핸들러 구현은 추가 검증을 해서는 안 됩니다. `PipelineHandler::configure()` 구현은 자체 `CameraConfiguration` 파생 클래스에 저장된 모든 사용자 정의 필드에 의존할 수 있습니다. `PipelineHandler::configure()` 구현자는 카메라를 구성할 때 `StreamConfiguration::setStream()`을 사용해 `CameraConfiguration`의 각 `StreamConfiguration` 항목에 `Stream` 인스턴스를 연결해야 합니다. `src/libcamera/pipeline_handler.cpp:286`, `src/libcamera/pipeline_handler.cpp:304`, `src/libcamera/pipeline_handler.cpp:306`, `src/libcamera/pipeline_handler.cpp:309`

`PipelineHandler::configure()`는 `CameraManager` 스레드에서 호출되며, 구현은 성공 시 `0`을, 실패 시 음수 오류 코드를 반환해야 합니다. `src/libcamera/pipeline_handler.cpp:313`

근거 원문: [src/libcamera/pipeline_handler.cpp:276](#source-924d43ea4bcaf94b) · [src/libcamera/pipeline_handler.cpp:289](#source-4abbe39594a1bd27) · [src/libcamera/pipeline_handler.cpp:285](#source-2eae247c4c37371c) · [src/libcamera/pipeline_handler.cpp:304](#source-31c5407347b4d0d8) · [src/libcamera/pipeline_handler.cpp:309](#source-f3cf94b1dc7b9457) · [src/libcamera/pipeline_handler.cpp:313](#source-f87ceb096b9f931d) · [src/libcamera/pipeline_handler.cpp:306](#source-71079779113f431c) · [src/libcamera/pipeline_handler.cpp:286](#source-25fb9495d4ab94a1) · [src/libcamera/pipeline_handler.cpp:271](#source-23ff032cd1152d56) · [src/libcamera/pipeline_handler.cpp:294](#source-4255f8449e37ebb8) · [src/libcamera/camera.cpp:1191](#source-603af0dd7fa357d0)

## 요청을 장치에 전달하고 반환하기

요청에는 버퍼 집합이 들어 있으며, 이 버퍼들은 스트림에 연결됩니다. 요청에는 파라미터 집합도 들어 있습니다. `queueRequestDevice` 구현자는 요청에서 제공한 버퍼에 캡처되는 프레임에 해당 파라미터가 적용되도록 장치를 프로그래밍해야 합니다. `queueRequestDevice` 구현자는 성공하면 `0`을, 실패하면 음수 오류 코드를 반환해야 합니다. `src/libcamera/pipeline_handler.cpp:535`, `src/libcamera/pipeline_handler.cpp:541`

<!-- sdd:visual:device-queue-and-completion -->
### 장치 큐잉과 버퍼·요청 완료의 책임

```mermaid
flowchart TB
%% sdd:translations {"CameraManager 스레드에서 <br/>queueRequestDevice 구현자가 <br/>버퍼에 담길 프레임에 요청 <br/>파라미터를 적용하도록 <br/>장치를 설정합니다.": "On the CameraManager <br/>thread, the <br/>queueRequestDevice <br/>implementer programs the <br/>device to apply request <br/>parameters to frames <br/>captured in the supplied <br/>buffers.", "마지막 버퍼 완료 뒤에도 <br/>요청은 자동으로 완료되지 <br/>않습니다.": "The request does not <br/>automatically complete when <br/>the last buffer completes.", "마지막 버퍼인 경우": "When it is the last buffer", "성공하면 0, 실패하면 음수 <br/>오류를 반환합니다.": "Return 0 on success or a <br/>negative error on failure.", "요청 완료는 명시 호출": "Explicit request completion", "캡처한 버퍼가 완료될 때": "When a captured buffer <br/>completes", "큐잉 결과": "Queue result", "핸들러가 CameraManager <br/>스레드에서 completeBuffer로 <br/>앱에 알리고 추적을 <br/>갱신합니다.": "The handler calls <br/>completeBuffer on the <br/>CameraManager thread to <br/>notify the application and <br/>update tracking.", "핸들러가 필요한 작업을 마친 <br/>뒤 completeRequest를 <br/>명시적으로 호출합니다.": "The handler explicitly <br/>calls completeRequest after <br/>any remaining work."}
  v_program["CameraManager 스레드에서 <br/>queueRequestDevice 구현자가 <br/>버퍼에 담길 프레임에 요청 <br/>파라미터를 적용하도록 <br/>장치를 설정합니다."]
  v_queue_result["성공하면 0, 실패하면 음수 <br/>오류를 반환합니다."]
  v_buffer["핸들러가 CameraManager <br/>스레드에서 completeBuffer로 <br/>앱에 알리고 추적을 <br/>갱신합니다."]
  v_last["마지막 버퍼 완료 뒤에도 <br/>요청은 자동으로 완료되지 <br/>않습니다."]
  v_request["핸들러가 필요한 작업을 마친 <br/>뒤 completeRequest를 <br/>명시적으로 호출합니다."]
  v_program -->|"큐잉 결과"| v_queue_result
  v_program -->|"캡처한 버퍼가 완료될 때"| v_buffer
  v_buffer -->|"마지막 버퍼인 경우"| v_last
  v_last -->|"요청 완료는 명시 호출"| v_request
```

[Mermaid 원문](vendor-integration.device-queue-and-completion.mmd)

??? note "그림 근거와 확인 범위"
    누가 요청의 파라미터를 장치에 적용하고 버퍼와 요청을 각각 완료합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="On the CameraManager thread, the queueRequestDevice implementer programs the device to apply request parameters to frames captured in the supplied buffers.">CameraManager 스레드에서 queueRequestDevice 구현자가 버퍼에 담길 프레임에 요청 파라미터를 적용하도록 장치를 설정합니다.</span> | [src/libcamera/pipeline_handler.cpp:535](#source-a9ed7dcbf54ccaff) · [src/libcamera/pipeline_handler.cpp:541](#source-974203a2566eb6a7) |
    | <span data-sdd-label-en="Return 0 on success or a negative error on failure.">성공하면 0, 실패하면 음수 오류를 반환합니다.</span> | [src/libcamera/pipeline_handler.cpp:541](#source-974203a2566eb6a7) |
    | <span data-sdd-label-en="The handler calls completeBuffer on the CameraManager thread to notify the application and update tracking.">핸들러가 CameraManager 스레드에서 completeBuffer로 앱에 알리고 추적을 갱신합니다.</span> | [src/libcamera/pipeline_handler.cpp:551](#source-2c79d29bf7fe6699) · [src/libcamera/pipeline_handler.cpp:558](#source-699c5b0f43c595cf) |
    | <span data-sdd-label-en="The request does not automatically complete when the last buffer completes.">마지막 버퍼 완료 뒤에도 요청은 자동으로 완료되지 않습니다.</span> | [src/libcamera/pipeline_handler.cpp:553](#source-7b871a70bfc9aa8f) |
    | <span data-sdd-label-en="The handler explicitly calls completeRequest after any remaining work.">핸들러가 필요한 작업을 마친 뒤 completeRequest를 명시적으로 호출합니다.</span> | [src/libcamera/pipeline_handler.cpp:553](#source-7b871a70bfc9aa8f) · [src/libcamera/pipeline_handler.cpp:556](#source-e1c3bfd748ad8a33) |
    | <span data-sdd-label-en="Queue result">큐잉 결과</span> | [src/libcamera/pipeline_handler.cpp:535](#source-a9ed7dcbf54ccaff) · [src/libcamera/pipeline_handler.cpp:541](#source-974203a2566eb6a7) |
    | <span data-sdd-label-en="When a captured buffer completes">캡처한 버퍼가 완료될 때</span> | [src/libcamera/pipeline_handler.cpp:535](#source-a9ed7dcbf54ccaff) · [src/libcamera/pipeline_handler.cpp:551](#source-2c79d29bf7fe6699) |
    | <span data-sdd-label-en="When it is the last buffer">마지막 버퍼인 경우</span> | [src/libcamera/pipeline_handler.cpp:551](#source-2c79d29bf7fe6699) · [src/libcamera/pipeline_handler.cpp:553](#source-7b871a70bfc9aa8f) |
    | <span data-sdd-label-en="Explicit request completion">요청 완료는 명시 호출</span> | [src/libcamera/pipeline_handler.cpp:553](#source-7b871a70bfc9aa8f) · [src/libcamera/pipeline_handler.cpp:556](#source-e1c3bfd748ad8a33) |
<!-- /sdd:visual:device-queue-and-completion -->

`PipelineHandler::queueRequestDevice()`는 `CameraManager` 스레드에서 호출됩니다. 파이프라인 핸들러는 요청의 버퍼 완료를 알리기 위해 `CameraManager` 스레드에서 `completeBuffer`를 호출해야 합니다. `completeBuffer`는 애플리케이션에 버퍼 완료를 통지하고 요청 내부의 버퍼 추적을 갱신합니다. 마지막 버퍼가 완료되어도 요청은 자동으로 완료되지 않으므로 파이프라인 핸들러가 `completeRequest()`를 명시적으로 호출해 요청을 완료해야 합니다. `src/libcamera/pipeline_handler.cpp:541`, `src/libcamera/pipeline_handler.cpp:551`, `src/libcamera/pipeline_handler.cpp:558`, `src/libcamera/pipeline_handler.cpp:553`, `src/libcamera/pipeline_handler.cpp:556`

근거 원문: [src/libcamera/pipeline_handler.cpp:535](#source-a9ed7dcbf54ccaff) · [src/libcamera/pipeline_handler.cpp:541](#source-974203a2566eb6a7) · [src/libcamera/pipeline_handler.cpp:551](#source-2c79d29bf7fe6699) · [src/libcamera/pipeline_handler.cpp:553](#source-7b871a70bfc9aa8f) · [src/libcamera/pipeline_handler.cpp:558](#source-699c5b0f43c595cf) · [src/libcamera/pipeline_handler.cpp:556](#source-e1c3bfd748ad8a33)

## IPA 모듈 선택과 실패 조건

`createIPA`는 `module`을 호출할 때 이름을 나타내는 `name`, 최소 버전을 나타내는 `minVersion`, 최대 버전을 나타내는 `maxVersion`을 순서대로 전달합니다. `IPAManager::module`은 모듈을 순회하며 이름과 허용 버전 범위에 대해 첫 `match`가 성립하면 해당 모듈을 반환하고 검색을 끝냅니다. 끝까지 일치하는 모듈이 없으면 `nullptr`을 반환합니다. `createIPA`는 `module`의 결과를 `m`에 받고, `!m`이면 `nullptr`을 반환합니다. `include/libcamera/internal/ipa_manager.h:39`, `src/libcamera/ipa_manager.cpp:249`

<!-- sdd:visual:item-algorithm -->
### IPA 모듈 검색과 프록시 반환 분기

```mermaid
flowchart TB
%% sdd:translations {"Isolated 프록시를 <br/>생성합니다.": "Create the Isolated proxy.", "Threaded 프록시를 <br/>생성합니다.": "Create the Threaded proxy.", "isSignatureValid가 거짓을 <br/>반환합니다.": "isSignatureValid returns <br/>false.", "isSignatureValid가 참을 <br/>반환합니다.": "isSignatureValid returns <br/>true.", "검사할 모듈이 남았습니까?": "Is there another module to <br/>check?", "검사할 모듈이 있습니다.": "There is a module to check.", "모듈 목록을 확인합니다.": "Check the module list.", "목록이 비었거나 순회를 <br/>마쳤습니다.": "The list was empty or the <br/>search was exhausted.", "생성 결과를 검사합니다.": "Check the resulting proxy.", "생성한 프록시가 유효합니까?": "Is the new proxy valid?", "유효한 프록시를 반환합니다.": "Return the valid proxy.", "이름과 버전 범위가 <br/>일치합니까?": "Does the module match the <br/>name and version range?", "이름과 허용 버전 범위를 <br/>module에 전달합니다.": "Pass the name and allowed <br/>version range to module.", "일치하지 않아 남은 항목을 <br/>확인합니다.": "A mismatch leads back to <br/>the remaining modules.", "일치한 모듈이 없어 <br/>createIPA가 즉시 nullptr을 <br/>반환합니다.": "With no matching module, <br/>createIPA immediately <br/>returns nullptr.", "첫 일치 모듈로 검색을 <br/>끝냅니다.": "The first match ends the <br/>search.", "첫 일치 모듈에 대해 <br/>isSignatureValid가 참을 <br/>반환합니까?": "Does isSignatureValid <br/>return true for the first <br/>matching module?", "프록시 오류를 기록하고 <br/>nullptr을 반환합니다.": "Log the proxy error and <br/>return nullptr.", "프록시가 유효하지 않습니다.": "The proxy is invalid.", "프록시가 유효합니다.": "The proxy is valid."}
  v_lookup["이름과 허용 버전 범위를 <br/>module에 전달합니다."]
  v_remaining{"검사할 모듈이 남았습니까?"}
  v_match{"이름과 버전 범위가 <br/>일치합니까?"}
  v_missing["일치한 모듈이 없어 <br/>createIPA가 즉시 nullptr을 <br/>반환합니다."]
  v_signature{"첫 일치 모듈에 대해 <br/>isSignatureValid가 참을 <br/>반환합니까?"}
  v_threaded["Threaded 프록시를 <br/>생성합니다."]
  v_isolated["Isolated 프록시를 <br/>생성합니다."]
  v_valid{"생성한 프록시가 유효합니까?"}
  v_invalid["프록시 오류를 기록하고 <br/>nullptr을 반환합니다."]
  v_return["유효한 프록시를 반환합니다."]
  v_lookup -->|"모듈 목록을 확인합니다."| v_remaining
  v_remaining -->|"검사할 모듈이 있습니다."| v_match
  v_remaining -->|"목록이 비었거나 순회를 <br/>마쳤습니다."| v_missing
  v_match -->|"일치하지 않아 남은 항목을 <br/>확인합니다."| v_remaining
  v_match -->|"첫 일치 모듈로 검색을 <br/>끝냅니다."| v_signature
  v_signature -->|"isSignatureValid가 참을 <br/>반환합니다."| v_threaded
  v_signature -->|"isSignatureValid가 거짓을 <br/>반환합니다."| v_isolated
  v_threaded -->|"생성 결과를 검사합니다."| v_valid
  v_isolated -->|"생성 결과를 검사합니다."| v_valid
  v_valid -->|"프록시가 유효하지 않습니다."| v_invalid
  v_valid -->|"프록시가 유효합니다."| v_return
```

[Mermaid 원문](vendor-integration.item-algorithm.mmd)

??? note "그림 근거와 확인 범위"
    createIPA는 일치하는 모듈과 프록시 종류를 어떻게 선택하며 어느 분기에서 nullptr을 반환합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Pass the name and allowed version range to module.">이름과 허용 버전 범위를 module에 전달합니다.</span> | [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) |
    | <span data-sdd-label-en="Is there another module to check?">검사할 모듈이 남았습니까?</span> | [src/libcamera/ipa_manager.cpp:249](#source-f61e5a9ff79a97a8) |
    | <span data-sdd-label-en="Does the module match the name and version range?">이름과 버전 범위가 일치합니까?</span> | [src/libcamera/ipa_manager.cpp:249](#source-f61e5a9ff79a97a8) |
    | <span data-sdd-label-en="With no matching module, createIPA immediately returns nullptr.">일치한 모듈이 없어 createIPA가 즉시 nullptr을 반환합니다.</span> | [src/libcamera/ipa_manager.cpp:249](#source-f61e5a9ff79a97a8) · [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) |
    | <span data-sdd-label-en="Does isSignatureValid return true for the first matching module?">첫 일치 모듈에 대해 isSignatureValid가 참을 반환합니까?</span> | [src/libcamera/ipa_manager.cpp:249](#source-f61e5a9ff79a97a8) · [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) |
    | <span data-sdd-label-en="Create the Threaded proxy.">Threaded 프록시를 생성합니다.</span> | [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) |
    | <span data-sdd-label-en="Create the Isolated proxy.">Isolated 프록시를 생성합니다.</span> | [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) |
    | <span data-sdd-label-en="Is the new proxy valid?">생성한 프록시가 유효합니까?</span> | [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) |
    | <span data-sdd-label-en="Log the proxy error and return nullptr.">프록시 오류를 기록하고 nullptr을 반환합니다.</span> | [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) |
    | <span data-sdd-label-en="Return the valid proxy.">유효한 프록시를 반환합니다.</span> | [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) |
    | <span data-sdd-label-en="Check the module list.">모듈 목록을 확인합니다.</span> | [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) · [src/libcamera/ipa_manager.cpp:249](#source-f61e5a9ff79a97a8) |
    | <span data-sdd-label-en="There is a module to check.">검사할 모듈이 있습니다.</span> | [src/libcamera/ipa_manager.cpp:249](#source-f61e5a9ff79a97a8) |
    | <span data-sdd-label-en="The list was empty or the search was exhausted.">목록이 비었거나 순회를 마쳤습니다.</span> | [src/libcamera/ipa_manager.cpp:249](#source-f61e5a9ff79a97a8) · [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) |
    | <span data-sdd-label-en="A mismatch leads back to the remaining modules.">일치하지 않아 남은 항목을 확인합니다.</span> | [src/libcamera/ipa_manager.cpp:249](#source-f61e5a9ff79a97a8) |
    | <span data-sdd-label-en="The first match ends the search.">첫 일치 모듈로 검색을 끝냅니다.</span> | [src/libcamera/ipa_manager.cpp:249](#source-f61e5a9ff79a97a8) · [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) |
    | <span data-sdd-label-en="isSignatureValid returns true.">isSignatureValid가 참을 반환합니다.</span> | [src/libcamera/ipa_manager.cpp:249](#source-f61e5a9ff79a97a8) · [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) |
    | <span data-sdd-label-en="isSignatureValid returns false.">isSignatureValid가 거짓을 반환합니다.</span> | [src/libcamera/ipa_manager.cpp:249](#source-f61e5a9ff79a97a8) · [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) |
    | <span data-sdd-label-en="Check the resulting proxy.">생성 결과를 검사합니다.</span> | [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) |
    | <span data-sdd-label-en="Check the resulting proxy.">생성 결과를 검사합니다.</span> | [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) |
    | <span data-sdd-label-en="The proxy is invalid.">프록시가 유효하지 않습니다.</span> | [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) |
    | <span data-sdd-label-en="The proxy is valid.">프록시가 유효합니다.</span> | [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) |
<!-- /sdd:visual:item-algorithm -->

`createIPA` 내부 람다는 `isSignatureValid(m)`이 참이면 `T::Threaded` 프록시 객체를 생성하고, 거짓이면 `T::Isolated` 프록시 객체를 생성합니다. `createIPA`는 생성한 프록시의 `isValid` 검사가 실패하면 `Failed to load proxy` 오류를 기록하고 `nullptr`을 반환합니다. `createIPA`는 생성한 프록시가 유효성 검사를 통과하면 해당 프록시를 반환합니다. `include/libcamera/internal/ipa_manager.h:43`, `include/libcamera/internal/ipa_manager.h:35`

근거 원문: [include/libcamera/internal/ipa_manager.h:35](#source-1bc92c4993a1c4dc) · [include/libcamera/internal/ipa_manager.h:43](#source-6dc4133d5797f19b) · [include/libcamera/internal/ipa_manager.h:39](#source-88cede73f337db67) · [include/libcamera/internal/ipa_manager.h:39](#source-da860180dc9199e6) · [src/libcamera/ipa_manager.cpp:249](#source-f61e5a9ff79a97a8)

## 정지와 오류 처리의 책임

`PipelineHandler::stop()`은 먼저 `waitingRequests.swap(data->waitingRequests_)`를 실행한 다음 `stopDevice(camera)`를 호출합니다. `PipelineHandler::stop()`은 `stopDevice()` 내부에서 `completeRequest()`가 호출될 때 대기 중인 요청이 다시 큐에 들어가지 않도록 이 요청들을 따로 옮깁니다. `stopDevice()` 구현자는 실행 중인 모든 스트림의 캡처와 요청 처리를 즉시 중단하고, 해당 장치의 미완료 요청을 모두 취소해 즉시 오류 상태로 완료해야 합니다. `src/libcamera/pipeline_handler.cpp:367`, `src/libcamera/pipeline_handler.cpp:370`, `src/libcamera/pipeline_handler.cpp:405`

<!-- sdd:visual:shutdown-device-and-waiting-requests -->
### 장치 정지와 대기 요청의 반환 순서

```mermaid
flowchart TB
%% sdd:translations {"stopDevice 구현자가 캡처를 <br/>멈추고 장치의 미완료 요청을 <br/>오류로 완료합니다.": "The stopDevice implementer <br/>stops capture and completes <br/>pending device requests in <br/>error.", "공통 stop이 <br/>waitingRequests#95;를 지역 <br/>큐로 옮깁니다.": "The common stop moves <br/>waitingRequests#95; to a local <br/>queue.", "다음 대기 요청을 확인합니다.": "Check the next waiting <br/>request.", "대기 요청을 취소하고 <br/>doQueueRequest로 순번을 <br/>부여해 완료 경로에 넣습니다.": "Cancel the waiting request <br/>and send it through <br/>doQueueRequest to assign a <br/>sequence number and enter <br/>completion.", "대기 요청이 있습니다.": "There is a waiting request.", "두 요청 큐가 비었는지 <br/>ASSERT로 검사하고 <br/>requestSequence#95;를 0으로 <br/>초기화합니다.": "Assert both request queues <br/>are empty and reset <br/>requestSequence#95; to zero.", "장치 정지 호출이 반환한 뒤": "After the device stop call <br/>returns", "재투입을 막기 위해 먼저 분리": "Separate first to prevent <br/>requeue", "지역 큐가 비었습니다.": "The local queue is empty.", "지역 큐에 대기 요청이 <br/>남았습니까?": "Is there another waiting <br/>request in the local queue?"}
  v_isolate["공통 stop이 <br/>waitingRequests#95;를 지역 <br/>큐로 옮깁니다."]
  v_device["stopDevice 구현자가 캡처를 <br/>멈추고 장치의 미완료 요청을 <br/>오류로 완료합니다."]
  v_waiting{"지역 큐에 대기 요청이 <br/>남았습니까?"}
  v_cancel["대기 요청을 취소하고 <br/>doQueueRequest로 순번을 <br/>부여해 완료 경로에 넣습니다."]
  v_reset["두 요청 큐가 비었는지 <br/>ASSERT로 검사하고 <br/>requestSequence#95;를 0으로 <br/>초기화합니다."]
  v_isolate -->|"재투입을 막기 위해 먼저 분리"| v_device
  v_device -->|"장치 정지 호출이 반환한 뒤"| v_waiting
  v_waiting -->|"대기 요청이 있습니다."| v_cancel
  v_cancel -->|"다음 대기 요청을 확인합니다."| v_waiting
  v_waiting -->|"지역 큐가 비었습니다."| v_reset
```

[Mermaid 원문](vendor-integration.shutdown-device-and-waiting-requests.mmd)

??? note "그림 근거와 확인 범위"
    공통 stop과 stopDevice 구현자가 각각 어떤 요청을 언제 처리합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="The common stop moves waitingRequests_ to a local queue.">공통 stop이 waitingRequests&#95;를 지역 큐로 옮깁니다.</span> | [src/libcamera/pipeline_handler.cpp:367](#source-1cc522721d2c5142) · [src/libcamera/pipeline_handler.cpp:370](#source-486f3f81acba3c1f) |
    | <span data-sdd-label-en="The stopDevice implementer stops capture and completes pending device requests in error.">stopDevice 구현자가 캡처를 멈추고 장치의 미완료 요청을 오류로 완료합니다.</span> | [src/libcamera/pipeline_handler.cpp:367](#source-7097caa35d0e97c8) · [src/libcamera/pipeline_handler.cpp:405](#source-a1eeb263fc114d2f) |
    | <span data-sdd-label-en="Is there another waiting request in the local queue?">지역 큐에 대기 요청이 남았습니까?</span> | [src/libcamera/pipeline_handler.cpp:367](#source-1cc522721d2c5142) |
    | <span data-sdd-label-en="Cancel the waiting request and send it through doQueueRequest to assign a sequence number and enter completion.">대기 요청을 취소하고 doQueueRequest로 순번을 부여해 완료 경로에 넣습니다.</span> | [src/libcamera/pipeline_handler.cpp:367](#source-1cc522721d2c5142) |
    | <span data-sdd-label-en="Assert both request queues are empty and reset requestSequence_ to zero.">두 요청 큐가 비었는지 ASSERT로 검사하고 requestSequence&#95;를 0으로 초기화합니다.</span> | [src/libcamera/pipeline_handler.cpp:367](#source-1cc522721d2c5142) |
    | <span data-sdd-label-en="Separate first to prevent requeue">재투입을 막기 위해 먼저 분리</span> | [src/libcamera/pipeline_handler.cpp:370](#source-486f3f81acba3c1f) · [src/libcamera/pipeline_handler.cpp:367](#source-1cc522721d2c5142) · [src/libcamera/pipeline_handler.cpp:367](#source-7097caa35d0e97c8) |
    | <span data-sdd-label-en="After the device stop call returns">장치 정지 호출이 반환한 뒤</span> | [src/libcamera/pipeline_handler.cpp:367](#source-7097caa35d0e97c8) · [src/libcamera/pipeline_handler.cpp:367](#source-1cc522721d2c5142) |
    | <span data-sdd-label-en="There is a waiting request.">대기 요청이 있습니다.</span> | [src/libcamera/pipeline_handler.cpp:367](#source-1cc522721d2c5142) |
    | <span data-sdd-label-en="Check the next waiting request.">다음 대기 요청을 확인합니다.</span> | [src/libcamera/pipeline_handler.cpp:367](#source-1cc522721d2c5142) |
    | <span data-sdd-label-en="The local queue is empty.">지역 큐가 비었습니다.</span> | [src/libcamera/pipeline_handler.cpp:367](#source-1cc522721d2c5142) |
<!-- /sdd:visual:shutdown-device-and-waiting-requests -->

`PipelineHandler::stop()`은 대기 요청을 따로 꺼낸 뒤 `stopDevice()`를 호출하고, 각 대기 요청을 취소한 후 `doQueueRequest()`로 전달하여 순번을 부여하고 `queuedRequests_`에 임시로 추가해 `completeRequest()`에서 완료할 수 있게 합니다. `PipelineHandler::stop()`은 대기 요청을 처리한 뒤 두 `ASSERT`로 `queuedRequests_`와 `waitingRequests_`가 비어 있는지 확인하고, `requestSequence_`에 `0`을 저장합니다. `src/libcamera/pipeline_handler.cpp:367`

근거 원문: [src/libcamera/pipeline_handler.cpp:367](#source-1cc522721d2c5142) · [src/libcamera/pipeline_handler.cpp:405](#source-a1eeb263fc114d2f) · [src/libcamera/pipeline_handler.cpp:367](#source-7097caa35d0e97c8) · [src/libcamera/pipeline_handler.cpp:370](#source-486f3f81acba3c1f)

## 구현 뒤 확인할 계약과 실행 한계

파이프라인 핸들러 구현자는 `completeRequest`가 반환된 뒤 해당 요청에 접근해서는 안 됩니다. 파이프라인 핸들러는 완료된 요청을 순서 제약 없이 `completeRequest`에 전달할 수 있으며, 이 함수는 요청을 제출 순서대로 애플리케이션에 반환합니다. 파이프라인 핸들러는 `completeRequest`를 `CameraManager` 스레드에서 호출해야 합니다. `src/libcamera/pipeline_handler.cpp:571`, `src/libcamera/pipeline_handler.cpp:578`, `src/libcamera/pipeline_handler.cpp:582`

근거 원문: [src/libcamera/pipeline_handler.cpp:571](#source-7ac40780a56ae3a9) · [src/libcamera/pipeline_handler.cpp:578](#source-16187edaf24c09f5) · [src/libcamera/pipeline_handler.cpp:582](#source-72e48606b2a92dcc)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 연동을 시작할 순서와 제공 측·Vendor의 구현 책임은 무엇입니까? | [연동 순서와 책임](#연동-순서와-책임) | 코드 근거와 설명 연결 |
    | 하드웨어의 장치 매칭과 카메라 등록은 누가 구현합니까? | [하드웨어와 공통 계층의 경계](#하드웨어와-공통-계층의-경계) | 코드 근거와 설명 연결 |
    | 스트림 구성 구현은 어떤 입력과 출력 계약을 지킵니까? | [구현할 설정 인터페이스](#구현할-설정-인터페이스) | 코드 근거와 설명 연결 |
    | 공통 큐와 하드웨어 구현은 요청 처리 책임을 어떻게 나눕니까? | [요청을 장치에 전달하고 반환하기](#요청을-장치에-전달하고-반환하기) | 코드 근거와 설명 연결 |
    | IPA 모듈과 실행 방식은 어떻게 선택되며 언제 생성에 실패합니까? | [IPA 모듈 선택과 실패 조건](#ipa-모듈-선택과-실패-조건) | 코드 근거와 설명 연결 |
    | 정지 시 공통 코드와 하드웨어 구현은 무엇을 끝내야 합니까? | [정지와 오류 처리의 책임](#정지와-오류-처리의-책임) | 코드 근거와 설명 연결 |
    | 코드 계약과 별도 실행 검증 항목은 무엇입니까? | [구현 뒤 확인할 계약과 실행 한계](#구현-뒤-확인할-계약과-실행-한계) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-2683b4a5a1dbfee9"></a>

??? note "소스 근거: src/libcamera/camera.cpp:771"
    `src/libcamera/camera.cpp:771`에서 시작하는 발췌입니다. 종료 줄은 775이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `2727ed2082026463f6e5fe4b907fefa46749d0ff9d9122ad2d578b6440c206a0`
    
    ```text
    An application needs to perform a sequence of operations on a camera before
     * it is ready to process requests. The camera needs to be acquired and
     * configured to prepare the camera for capture. Once started the camera can
     * process requests until it is stopped. When an application is done with a
     * camera, the camera needs to be released.
    ```

<a id="source-cc6c66b57cf028e6"></a>

??? note "소스 근거: src/libcamera/camera.cpp:780"
    `src/libcamera/camera.cpp:780`에서 시작하는 발췌입니다. 종료 줄은 782이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `de3ba7a26c3bbaf6bbb33d1749b99829fdc58e13718068d149c849d0b2c43388`
    
    ```text
    Functions that affect the camera state as defined below are generally not
     * synchronized with each other by the Camera class. The caller is responsible
     * for ensuring their synchronization if necessary.
    ```

<a id="source-948bd80fa1136291"></a>

??? note "소스 근거: src/libcamera/camera.cpp:777"
    `src/libcamera/camera.cpp:777`에서 시작하는 발췌입니다. 종료 줄은 778이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `4af35cfde252bae9391fc55c13025c02f8bd98084b9f53807de39707feb33377`
    
    ```text
    An application may start and stop a camera multiple times as long as it is
     * not released. The camera may also be reconfigured.
    ```

<a id="source-492118d913b10361"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1032"
    `src/libcamera/camera.cpp:1032`에서 시작하는 발췌입니다. 종료 줄은 1062이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `734a942c1c3483d82cacc5da96ae3bd47ee8fe8d38d223c41777fbe244ccad1c`
    
    ```text
    \brief Release exclusive access to the camera device
     *
     * Releasing the camera device allows other users to acquire exclusive access
     * with the acquire() function.
     *
     * \context This function may only be called when the camera is in the
     * Available or Configured state as defined in \ref camera_operation, and shall
     * be synchronized by the caller with other functions that affect the camera
     * state.
     *
     * \return 0 on success or a negative error code otherwise
     * \retval -EBUSY The camera is running and can't be released
     */
    int Camera::release()
    {
    	Private *const d = _d();
    
    	int ret = d->isAccessAllowed(Private::CameraAvailable,
    				     Private::CameraConfigured, true);
    	if (ret < 0)
    		return ret == -EACCES ? -EBUSY : ret;
    
    	if (d->isAcquired())
    		d->pipe_->invokeMethod(&PipelineHandler::release,
    				       ConnectionTypeBlocking, this);
    
    	d->setState(Private::CameraAvailable);
    
    	return 0;
    }
    
    ```

<a id="source-5109302527925a6a"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:91"
    `src/libcamera/pipeline_handler.cpp:91`에서 시작하는 발췌입니다. 종료 줄은 103이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `f71446293f48c042c9685cc078c8474d78182a065365d2c02185640d8bdb385c`
    
    ```text
    This function is the main entry point of the pipeline handler. It is called
     * by the camera manager with the \a enumerator passed as an argument. It shall
     * acquire from the \a enumerator all the media devices it needs for a single
     * pipeline, create one or multiple Camera instances and register them with the
     * camera manager.
     *
     * If all media devices needed by the pipeline handler are found, they must all
     * be acquired by a call to MediaDevice::acquire(). This function shall then
     * create the corresponding Camera instances, store them internally, and return
     * true. Otherwise it shall not acquire any media device (or shall release all
     * the media devices is has acquired by calling MediaDevice::release()) and
     * return false.
     *
    ```

<a id="source-1afff120b5d66b3c"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:109"
    `src/libcamera/pipeline_handler.cpp:109`에서 시작하는 발췌입니다. 종료 줄은 112이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `3e2c9aaca45aae2be928349e1a9f3eaa34c12a0a9ba701fe08112f604927640a`
    
    ```text
    If this function returns true, a new instance of the pipeline handler will
     * be created and its match() function called.
     *
     * \context This function is called from the CameraManager thread.
    ```

<a id="source-293bf5d4775550d0"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:97"
    `src/libcamera/pipeline_handler.cpp:97`에서 시작하는 발췌입니다. 종료 줄은 103이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `55f330a97aaa4bc7d7e5d20f1afe49867ececda542794b11da4c861513563745`
    
    ```text
    If all media devices needed by the pipeline handler are found, they must all
     * be acquired by a call to MediaDevice::acquire(). This function shall then
     * create the corresponding Camera instances, store them internally, and return
     * true. Otherwise it shall not acquire any media device (or shall release all
     * the media devices is has acquired by calling MediaDevice::release()) and
     * return false.
     *
    ```

<a id="source-924d43ea4bcaf94b"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:276"
    `src/libcamera/pipeline_handler.cpp:276`에서 시작하는 발췌입니다. 종료 줄은 280이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `38af3c19eb234dbcc39befcd4bafc97cb1029422310cc38e47bad37f84940db5`
    
    ```text
    Generate a default configuration for the \a camera for a specified list of
     * stream roles. The caller shall populate the \a roles with the use-cases it
     * wishes to fetch the default configuration for. The returned configuration
     * can then be examined by the caller to learn about the selected streams and
     * their default parameters.
    ```

<a id="source-4abbe39594a1bd27"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:289"
    `src/libcamera/pipeline_handler.cpp:289`에서 시작하는 발췌입니다. 종료 줄은 290이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `b86c8678b02e96936d80626cefebf3811b6a991b459074e51c9f0e08457ff369`
    
    ```text
    \return A valid CameraConfiguration if the requested roles can be satisfied,
     * or a null pointer otherwise.
    ```

<a id="source-2eae247c4c37371c"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:285"
    `src/libcamera/pipeline_handler.cpp:285`에서 시작하는 발췌입니다. 종료 줄은 286이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `dcef1582ffd11183a0765511757597c9619de8b015f123e92622a389a4bebd26`
    
    ```text
    \context This function may be called from any thread and shall be
     * \threadsafe.
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

<a id="source-f3cf94b1dc7b9457"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:309"
    `src/libcamera/pipeline_handler.cpp:309`에서 시작하는 발췌입니다. 종료 줄은 311이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `7fb65d00aa32892f805904a4ada55b8f63566b0efc49ff0c5503bb821d3b79e0`
    
    ```text
    When configuring the camera the pipeline handler shall associate a Stream
     * instance to each StreamConfiguration entry in the CameraConfiguration using
     * the StreamConfiguration::setStream() function.
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

<a id="source-71079779113f431c"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:306"
    `src/libcamera/pipeline_handler.cpp:306`에서 시작하는 발췌입니다. 종료 줄은 307이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `8436da4de01d0e01f9c5763f9e9df0210c59e6b1efb703f1eff1107afc3186b8`
    
    ```text
    may rely on any custom field stored in its
     * custom CameraConfiguration derived class.
    ```

<a id="source-25fb9495d4ab94a1"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:286"
    `src/libcamera/pipeline_handler.cpp:286`에서 시작하는 발췌입니다. 종료 줄은 287이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `19e8cba75821e7582a759ecb13aaa7ec1439b76f0acf0aaa6b4bdcead0636ab6`
    
    ```text
    It shall not modify the state of the \a camera in the pipeline
     * handler.
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

<a id="source-4255f8449e37ebb8"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:294"
    `src/libcamera/pipeline_handler.cpp:294`에서 시작하는 발췌입니다. 종료 줄은 316이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `5b219c0d287985da85343ebfed58f2c0ab7fc65635129141016b21bd45969a40`
    
    ```text
    \fn PipelineHandler::configure()
     * \brief Configure a group of streams for capture
     * \param[in] camera The camera to configure
     * \param[in] config The camera configurations to setup
     *
     * Configure the specified group of streams for \a camera according to the
     * configuration specified in \a config. The intended caller of this interface
     * is the Camera class which will receive configuration to apply from the
     * application.
     *
     * The configuration is guaranteed to have been validated with
     * CameraConfiguration::validate(). The pipeline handler implementation shall
     * not perform further validation and may rely on any custom field stored in its
     * custom CameraConfiguration derived class.
     *
     * When configuring the camera the pipeline handler shall associate a Stream
     * instance to each StreamConfiguration entry in the CameraConfiguration using
     * the StreamConfiguration::setStream() function.
     *
     * \context This function is called from the CameraManager thread.
     *
     * \return 0 on success or a negative error code otherwise
     */
    ```

<a id="source-603af0dd7fa357d0"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1191"
    `src/libcamera/camera.cpp:1191`에서 시작하는 발췌입니다. 종료 줄은 1240이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `ff6ceda14768503bdfe753d462853457743d5b46a80e0808a97375632403cd36`
    
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
    ```

<a id="source-a9ed7dcbf54ccaff"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:535"
    `src/libcamera/pipeline_handler.cpp:535`에서 시작하는 발췌입니다. 종료 줄은 540이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `90f059dc331718ad68e3644501e4aec3dddc1fa95977d61cb36f32ed7d9722fd`
    
    ```text
    This function queues a capture request to the device for processing. The
     * request contains a set of buffers associated with streams and a set of
     * parameters. The pipeline handler shall program the device to ensure that the
     * parameters will be applied to the frames captured in the buffers provided in
     * the request.
     *
    ```

<a id="source-974203a2566eb6a7"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:541"
    `src/libcamera/pipeline_handler.cpp:541`에서 시작하는 발췌입니다. 종료 줄은 543이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `6e139b3c50660a7111d84bd00cfd17078b8b45d4a07688fa64b2d8af9ce52a22`
    
    ```text
    \context This function is called from the CameraManager thread.
     *
     * \return 0 on success or a negative error code otherwise
    ```

<a id="source-2c79d29bf7fe6699"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:551"
    `src/libcamera/pipeline_handler.cpp:551`에서 시작하는 발췌입니다. 종료 줄은 553이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `60f0e467f8ae13c4ddb878bc507741645fdc3e4ac08fd4975645667c0973c7f7`
    
    ```text
    This function shall be called by pipeline handlers to signal completion of
     * the \a buffer part of the \a request. It notifies applications of buffer
     * completion and updates the request's internal buffer tracking.
    ```

<a id="source-7b871a70bfc9aa8f"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:553"
    `src/libcamera/pipeline_handler.cpp:553`에서 시작하는 발췌입니다. 종료 줄은 556이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `6fd257c0a3f4e1d654e13a7de0624813b3e9153b824e4ae5e09f36da87950627`
    
    ```text
    The request
     * is not completed automatically when the last buffer completes to give
     * pipeline handlers a chance to perform any operation that may still be
     * needed.
    ```

<a id="source-699c5b0f43c595cf"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:558"
    `src/libcamera/pipeline_handler.cpp:558`에서 시작하는 발췌입니다. 종료 줄은 558이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `0f7e50ba80f907cc3c696082a4898c3540fbe4390ac47fc4f4cceabf5644df8d`
    
    ```text
    \context This function shall be called from the CameraManager thread.
    ```

<a id="source-e1c3bfd748ad8a33"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:556"
    `src/libcamera/pipeline_handler.cpp:556`에서 시작하는 발췌입니다. 종료 줄은 556이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `53620638ce4f05ea0ffdbf203d2e1c4689c6fc325aae57af105a88f01af48dc5`
    
    ```text
    They shall complete requests explicitly with completeRequest().
    ```

<a id="source-1bc92c4993a1c4dc"></a>

??? note "소스 근거: include/libcamera/internal/ipa_manager.h:35"
    `include/libcamera/internal/ipa_manager.h:35`에서 시작하는 발췌입니다. 종료 줄은 56이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `a8677961db1bb04a435196457a57d7f77bfdce934023d68a657a72bf3d468abf`
    
    ```text
    template<typename T>
    	std::unique_ptr<T> createIPA(const char *name, uint32_t minVersion,
    				     uint32_t maxVersion)
    	{
    		IPAModule *m = module(name, minVersion, maxVersion);
    		if (!m)
    			return nullptr;
    
    		auto proxy = [&]() -> std::unique_ptr<T> {
    			if (isSignatureValid(m))
    				return std::make_unique<typename T::Threaded>(m, cm_);
    			else
    				return std::make_unique<typename T::Isolated>(m, cm_);
    		}();
    
    		if (!proxy->isValid()) {
    			LOG(IPAManager, Error) << "Failed to load proxy";
    			return nullptr;
    		}
    
    		return proxy;
    	}
    ```

<a id="source-6dc4133d5797f19b"></a>

??? note "소스 근거: include/libcamera/internal/ipa_manager.h:43"
    `include/libcamera/internal/ipa_manager.h:43`에서 시작하는 발췌입니다. 종료 줄은 48이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `8dd07139188ee0ecf096f7b10adb371325923fd96667ed987098ba80c3cea94f`
    
    ```text
    auto proxy = [&]() -> std::unique_ptr<T> {
    			if (isSignatureValid(m))
    				return std::make_unique<typename T::Threaded>(m, cm_);
    			else
    				return std::make_unique<typename T::Isolated>(m, cm_);
    		}();
    ```

<a id="source-88cede73f337db67"></a>

??? note "소스 근거: include/libcamera/internal/ipa_manager.h:39"
    `include/libcamera/internal/ipa_manager.h:39`에서 시작하는 발췌입니다. 종료 줄은 39이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `abe3700a1da7f3f2eb981affc5f0e293b2e1acc38b3566ae91bb3dd5283f2e4c`
    
    ```text
    IPAModule *m = module(name, minVersion, maxVersion);
    ```

<a id="source-da860180dc9199e6"></a>

??? note "소스 근거: include/libcamera/internal/ipa_manager.h:39"
    `include/libcamera/internal/ipa_manager.h:39`에서 시작하는 발췌입니다. 종료 줄은 41이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `177bd03308c1f0c5ca690d6960c7defda327b0c9bec1228cb75851a3ed5a9100`
    
    ```text
    IPAModule *m = module(name, minVersion, maxVersion);
    		if (!m)
    			return nullptr;
    ```

<a id="source-f61e5a9ff79a97a8"></a>

??? note "소스 근거: src/libcamera/ipa_manager.cpp:249"
    `src/libcamera/ipa_manager.cpp:249`에서 시작하는 발췌입니다. 종료 줄은 263이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `2921c9966e20f365d405810ba3d0ea3b95298348355fd8a51631b5a163846dfb`
    
    ```text
    \brief Retrieve an IPA module that matches a given pipeline handler
     * \param[in] name The IPA module string identifier
     * \param[in] minVersion Minimum acceptable version of IPA module
     * \param[in] maxVersion Maximum acceptable version of IPA module
     */
    IPAModule *IPAManager::module(const char *name, uint32_t minVersion,
    			      uint32_t maxVersion)
    {
    	for (const auto &module : modules_) {
    		if (module->match(name, minVersion, maxVersion))
    			return module.get();
    	}
    
    	return nullptr;
    }
    ```

<a id="source-1cc522721d2c5142"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:367"
    `src/libcamera/pipeline_handler.cpp:367`에서 시작하는 발췌입니다. 종료 줄은 402이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `43962342db73d223e196b6bae1c49c79db3d3a68de4893cba3ddad50945c23d2`
    
    ```text
    void PipelineHandler::stop(Camera *camera)
    {
    	/*
    	 * Take all waiting requests so that they are not requeued in response
    	 * to completeRequest() being called inside stopDevice(). Cancel them
    	 * after the device to keep them in order.
    	 */
    	Camera::Private *data = camera->_d();
    	std::queue<Request *> waitingRequests;
    	waitingRequests.swap(data->waitingRequests_);
    
    	/* Stop the pipeline handler and let the queued requests complete. */
    	stopDevice(camera);
    
    	/* Cancel and signal as complete all waiting requests. */
    	while (!waitingRequests.empty()) {
    		Request *request = waitingRequests.front();
    		waitingRequests.pop();
    
    		/*
    		 * Cancel all requests by marking them as cancelled and calling
    		 * doQueueRequest() instead of cancelRequest(). This ensures
    		 * that the requests get a sequence number and are temporarily
    		 * added to queuedRequests_ so they can be properly completed in
    		 * completeRequest().
    		 */
    		request->_d()->cancel();
    		doQueueRequest(request);
    	}
    
    	/* Make sure no requests are pending. */
    	ASSERT(data->queuedRequests_.empty());
    	ASSERT(data->waitingRequests_.empty());
    
    	data->requestSequence_ = 0;
    }
    ```

<a id="source-a1eeb263fc114d2f"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:405"
    `src/libcamera/pipeline_handler.cpp:405`에서 시작하는 발췌입니다. 종료 줄은 411이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `10e65d81029b39b67e5a3a0b9f6502965f8444fd0cfc459af29fbc511644930b`
    
    ```text
    \fn PipelineHandler::stopDevice()
     * \brief Stop capturing from all running streams
     * \param[in] camera The camera to stop
     *
     * This function stops capturing and processing requests immediately. All
     * pending requests are cancelled and complete immediately in an error state.
     */
    ```

<a id="source-7097caa35d0e97c8"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:367"
    `src/libcamera/pipeline_handler.cpp:367`에서 시작하는 발췌입니다. 종료 줄은 379이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `3c6cff12988571819f87137599bce3e890430991f6cef0f7428d891073c6d6be`
    
    ```text
    void PipelineHandler::stop(Camera *camera)
    {
    	/*
    	 * Take all waiting requests so that they are not requeued in response
    	 * to completeRequest() being called inside stopDevice(). Cancel them
    	 * after the device to keep them in order.
    	 */
    	Camera::Private *data = camera->_d();
    	std::queue<Request *> waitingRequests;
    	waitingRequests.swap(data->waitingRequests_);
    
    	/* Stop the pipeline handler and let the queued requests complete. */
    	stopDevice(camera);
    ```

<a id="source-486f3f81acba3c1f"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:370"
    `src/libcamera/pipeline_handler.cpp:370`에서 시작하는 발췌입니다. 종료 줄은 371이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `8c2bdec1e95f13a806ecac8a21da815c448c76042bab9658999a4a7636fe96b1`
    
    ```text
    Take all waiting requests so that they are not requeued in response
    	 * to completeRequest() being called inside stopDevice().
    ```

<a id="source-7ac40780a56ae3a9"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:571"
    `src/libcamera/pipeline_handler.cpp:571`에서 시작하는 발췌입니다. 종료 줄은 584이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `25903b4c6a305017b96bfe9117fe2b7b917b51fbeb2fd21139700b1fbf6a4fe2`
    
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
    void PipelineHandler::completeRequest
    ```

<a id="source-16187edaf24c09f5"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:578"
    `src/libcamera/pipeline_handler.cpp:578`에서 시작하는 발췌입니다. 종료 줄은 580이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `559a88834ae3bb13ac9f2d1844e5b87f1d863fd91b1c8ed252704bf1974adac6`
    
    ```text
    This function ensures that requests will be returned to the application in
     * submission order, the pipeline handler may call it on any complete request
     * without any ordering constraint.
    ```

<a id="source-72e48606b2a92dcc"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:582"
    `src/libcamera/pipeline_handler.cpp:582`에서 시작하는 발췌입니다. 종료 줄은 583이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `57320fd2a94f3a559970ad0de0160f8f6bd1373d83f964ff7ecd5c6a51485d7c`
    
    ```text
    \context This function shall be called from the CameraManager thread.
     */
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
    - 근거 파일: `include/libcamera/camera.h`, `include/libcamera/internal/ipa_manager.h`, `include/libcamera/internal/pipeline_handler.h`, `src/libcamera/camera.cpp`, `src/libcamera/ipa_manager.cpp`, `src/libcamera/pipeline/ipu3/ipu3.cpp`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp`, `src/libcamera/pipeline_handler.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `c19d05128f`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-12 · 사람 검토 전

다음 단계: [지원 범위와 검증](vendor-assurance.md)
