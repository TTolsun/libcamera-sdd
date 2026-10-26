---
generated_at: 2026-10-26T14:23:05+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: pipeline-handler
generation_method: facts-and-llm
evidence_fingerprint: 0129b91370eccf4659f5e61748d6efad60fb4ba8627692b68ec471354695ac07
semantic_review: human-review-required
agent: ollama/qwen3.5:9b
generated_design: {"schema": 1, "input_fingerprint": "0129b91370eccf4659f5e61748d6efad60fb4ba8627692b68ec471354695ac07", "answers": {"responsibility": [{"text": "`PipelineHandler` 는 `DeviceEnumerator` 가 제공하는 미디어 장치와 지원 가능한 파이프라인을 매칭하여 해당하는 `Camera` 장치를 생성하고 관리합니다.", "evidence": ["handler"], "covers": ["responsibility"], "kind": "behavior", "quote": "\\class PipelineHandler\n * \\brief Create and manage cameras based on a set of media devices\n *\n * The PipelineHandler matches the media devices provided by a DeviceEnumerator\n * with the pipelines it supports and creates corresponding Camera devices.\n *\n * Pipeline handler instances are reference-counted through std::shared_ptr<>.\n * They implement std::enable_shared_from_this<> in order to create new\n * std::shared_ptr<> in code paths originating from member functions of the\n * PipelineHandler class where only the 'this' pointer is available.\n */"}, {"text": "`PipelineHandler` 인스턴스는 `std::shared_ptr`< > 를 통해 참조 카운팅되며, 멤버 함수에서 'this' 포인터만 사용 가능한 코드 경로에서 새로운 공유 포인터를 생성하기 위해 `std::enable_shared_from_this`< > 를 구현합니다.", "evidence": ["handler"], "covers": ["responsibility"], "kind": "behavior", "quote": "\\class PipelineHandler\n * \\brief Create and manage cameras based on a set of media devices\n *\n * The PipelineHandler matches the media devices provided by a DeviceEnumerator\n * with the pipelines it supports and creates corresponding Camera devices.\n *\n * Pipeline handler instances are reference-counted through std::shared_ptr<>.\n * They implement std::enable_shared_from_this<> in order to create new\n * std::shared_ptr<> in code paths originating from member functions of the\n * PipelineHandler class where only the 'this' pointer is available.\n */"}, {"text": "`PipelineHandler` 인스턴스는 수동으로 생성되어서는 안 되며, 항상 `PipelineHandlerFactoryBase::create()` 함수를 통해 생성되어야 합니다.", "evidence": ["handler"], "covers": ["responsibility"], "kind": "behavior", "quote": "/**\n * \\brief Construct a PipelineHandler instance\n * \\param[in] manager The camera manager\n * \\param[in] maxQueuedRequestsDevice The maximum number of requests queued to\n * the device\n *\n * In order to honour the std::enable_shared_from_this<> contract,\n * PipelineHandler instances shall never be constructed manually, but always\n * through the PipelineHandlerFactoryBase::create() function.\n */\nPipelineHandler::PipelineHandler(CameraManager *manager,\n\t\t\t\t unsigned int maxQueuedRequestsDevice)\n\t: manager_(manager), maxQueuedRequestsDevice_(maxQueuedRequestsDevice),\n\t  useCount_(0)\n{\n}"}, {"text": "`PipelineHandler` 가 소멸될 때, 매칭된 모든 `MediaDevice` 는 순차적으로 release() 호출을 통해 해제됩니다.", "evidence": ["handler"], "covers": ["responsibility"], "kind": "behavior", "quote": "PipelineHandler::~PipelineHandler()\n{\n\tfor (std::shared_ptr<MediaDevice> &media : mediaDevices_)\n\t\tmedia->release();\n}"}, {"text": "match() 함수는 파이프라인에 필요한 모든 미디어 장치가 시스템에서 발견되면 `MediaDevice::acquire()` 를 호출하여 장치를 확보하고, 해당하는 `Camera` 인스턴스를 생성한 후 카메라 매니저에 등록합니다.", "evidence": ["handler"], "covers": ["responsibility"], "kind": "behavior", "quote": "/**\n * \\fn PipelineHandler::match(DeviceEnumerator *enumerator)\n * \\brief Match media devices and create camera instances\n * \\param[in] enumerator The enumerator providing all media devices found in the\n * system\n *\n * This function is the main entry point of the pipeline handler. It is called\n * by the camera manager with the \\a enumerator passed as an argument. It shall\n * acquire from the \\a enumerator all the media devices it needs for a single\n * pipeline, create one or multiple Camera instances and register them with the\n * camera manager.\n *\n * If all media devices needed by the pipeline handler are found, they must all\n * be acquired by a call to MediaDevice::acquire(). This function shall then\n * create the corresponding Camera instances, store them internally, and return\n * true. Otherwise it shall not acquire any media device (or shall release all\n * the media devices is has acquired by calling MediaDevice::release()) and\n * return false.\n *\n * If multiple instances of a pipeline are available in the system, the\n * PipelineHandler class will be instantiated once per instance, and its match()\n * function called for every instance. Each call shall acquire media devices for\n * one pipeline instance, until all compatible media devices are exhausted.\n *\n * If this function returns true, a new instance of the pipeline handler will\n * be created and its match() function called.\n *\n * \\context This function is called from the CameraManager thread.\n *\n * \\return true if media devices have been acquired and camera instances\n * created, or false otherwise\n */"}, {"text": "match() 함수가 모든 파이프라인에 필요한 미디어 장치를 찾지 못하면, 어떤 미디어 장치도 확보하지 않거나 확보한 장치를 모두 해제하고 false 를 반환합니다.", "evidence": ["handler"], "covers": ["responsibility"], "kind": "behavior", "quote": "/**\n * \\fn PipelineHandler::match(DeviceEnumerator *enumerator)\n * \\brief Match media devices and create camera instances\n * \\param[in] enumerator The enumerator providing all media devices found in the\n * system\n *\n * This function is the main entry point of the pipeline handler. It is called\n * by the camera manager with the \\a enumerator passed as an argument. It shall\n * acquire from the \\a enumerator all the media devices it needs for a single\n * pipeline, create one or multiple Camera instances and register them with the\n * camera manager.\n *\n * If all media devices needed by the pipeline handler are found, they must all\n * be acquired by a call to MediaDevice::acquire(). This function shall then\n * create the corresponding Camera instances, store them internally, and return\n * true. Otherwise it shall not acquire any media device (or shall release all\n * the media devices is has acquired by calling MediaDevice::release()) and\n * return false.\n *\n * If multiple instances of a pipeline are available in the system, the\n * PipelineHandler class will be instantiated once per instance, and its match()\n * function called for every instance. Each call shall acquire media devices for\n * one pipeline instance, until all compatible media devices are exhausted.\n *\n * If this function returns true, a new instance of the pipeline handler will\n * be created and its match() function called.\n *\n * \\context This function is called from the CameraManager thread.\n *\n * \\return true if media devices have been acquired and camera instances\n * created, or false otherwise\n */"}, {"text": "acquireMediaDevice() 함수는 장치 매칭 패턴에 맞는 사용 가능한 미디어 장치를 검색하여 확보한 후, 파이프라인 핸들러가 소멸될 때 자동으로 해제되도록 처리합니다.", "evidence": ["acquisition"], "covers": ["responsibility"], "kind": "behavior", "quote": "\\brief Search and acquire a MediaDevice matching a device pattern\n * \\param[in] enumerator Enumerator containing all media devices in the system\n * \\param[in] dm Device match pattern\n *\n * Search the device \\a enumerator for an available media device matching the\n * device match pattern \\a dm. Matching media device that have previously been\n * acquired by MediaDevice::acquire() are not considered. If a match is found,\n * the media device is acquired and returned. The caller shall not release the\n * device explicitly, it will be automatically released when the pipeline\n * handler is destroyed.\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return A shared pointer to the matching MediaDevice, or nullptr if no match\n * is found\n */\nstd::shared_ptr<MediaDevice>\nPipelineHandler::acquireMediaDevice(DeviceEnumerator *enumerator,\n\t\t\t\t    const DeviceMatch &dm)\n{\n\tstd::shared_ptr<MediaDevice> media = enumerator->search(dm);\n\tif (!media)\n\t\treturn nullptr;"}, {"text": "acquireMediaDevice() 함수는 장치 확보에 실패하면 nullptr 를 반환하며, 호출자는 장치를 명시적으로 해제해서는 안 됩니다.", "evidence": ["acquisition"], "covers": ["responsibility"], "kind": "behavior", "quote": "\\brief Search and acquire a MediaDevice matching a device pattern\n * \\param[in] enumerator Enumerator containing all media devices in the system\n * \\param[in] dm Device match pattern\n *\n * Search the device \\a enumerator for an available media device matching the\n * device match pattern \\a dm. Matching media device that have previously been\n * acquired by MediaDevice::acquire() are not considered. If a match is found,\n * the media device is acquired and returned. The caller shall not release the\n * device explicitly, it will be automatically released when the pipeline\n * handler is destroyed.\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return A shared pointer to the matching MediaDevice, or nullptr if no match\n * is found\n */\nstd::shared_ptr<MediaDevice>\nPipelineHandler::acquireMediaDevice(DeviceEnumerator *enumerator,\n\t\t\t\t    const DeviceMatch &dm)\n{\n\tstd::shared_ptr<MediaDevice> media = enumerator->search(dm);\n\tif (!media)\n\t\treturn nullptr;"}], "configuration": [{"text": "generateConfiguration() 함수는 지정된 카메라에 대한 기본 설정을 생성하며, 호출자는 이 함수를 통해 원하는 사용 사례 (use-cases) 를 위한 스트림 역할 목록을 roles 매개변수에 채워 넣어야 합니다. 이 함수는 어떤 스레드에서나 호출할 수 있으며 파이프라인 핸들러의 상태 변경 없이 안전하게 실행됩니다. 요청된 역할이 충족될 경우 유효한 `CameraConfiguration` 객체를 반환하지만, 그렇지 않으면 null 포인터를 반환합니다.", "evidence": ["configuration"], "covers": ["configuration"], "kind": "behavior", "quote": "\\fn PipelineHandler::generateConfiguration()\n * \\brief Generate a camera configuration for a specified camera\n * \\param[in] camera The camera to generate a default configuration for\n * \\param[in] roles A list of stream roles\n *\n * Generate a default configuration for the \\a camera for a specified list of\n * stream roles. The caller shall populate the \\a roles with the use-cases it\n * wishes to fetch the default configuration for. The returned configuration\n * can then be examined by the caller to learn about the selected streams and\n * their default parameters.\n *\n * The intended companion to this is \\a configure() which can be used to change\n * the group of streams parameters.\n *\n * \\context This function may be called from any thread and shall be\n * \\threadsafe. It shall not modify the state of the \\a camera in the pipeline\n * handler.\n *\n * \\return A valid CameraConfiguration if the requested roles can be satisfied,\n * or a null pointer otherwise.\n */"}, {"text": "configure() 함수는 `CameraManager` 스레드에서 호출되며, 해당 카메라의 스트림 그룹을 설정된 구성에 따라 구성합니다. 이 함수를 호출하기 전에 제공된 `CameraConfiguration` 객체는 반드시 `CameraConfiguration::validate()` 를 통해 검증되었어야 하며, 파이프라인 핸들러 구현은 추가 검증을 수행하지 않고 커스텀 필드를 신뢰할 수 있습니다.", "evidence": ["configuration"], "covers": ["configuration"], "kind": "behavior", "quote": "/**\n * \\fn PipelineHandler::configure()\n * \\brief Configure a group of streams for capture\n * \\param[in] camera The camera to configure\n * \\param[in] config The camera configurations to setup\n *\n * Configure the specified group of streams for \\a camera according to the\n * configuration specified in \\a config. The intended caller of this interface\n * is the Camera class which will receive configuration to apply from the\n * application.\n *\n * The configuration is guaranteed to have been validated with\n * CameraConfiguration::validate(). The pipeline handler implementation shall\n * not perform further validation and may rely on any custom field stored in its\n * custom CameraConfiguration derived class.\n *\n * When configuring the camera the pipeline handler shall associate a Stream\n * instance to each StreamConfiguration entry in the CameraConfiguration using\n * the StreamConfiguration::setStream() function.\n *\n * \\context This function is called from the CameraManager thread.\n *\n * \\return 0 on success or a negative error code otherwise"}, {"text": "configure() 함수를 호출할 때 파이프라인 핸들러는 `CameraConfiguration` 내의 각 `StreamConfiguration` 항목에 대해 `Stream` 인스턴스를 setStream() 함수를 사용하여 연결해야 합니다. 성공 시 0 을 반환하고 실패 시 음수 오류 코드를 반환하며, 이는 실제 구현에서 발생할 수 있는 동작을 나타냅니다.", "evidence": ["configuration"], "covers": ["configuration"], "kind": "behavior", "quote": "/**\n * \\fn PipelineHandler::configure()\n * \\brief Configure a group of streams for capture\n * \\param[in] camera The camera to configure\n * \\param[in] config The camera configurations to setup\n *\n * Configure the specified group of streams for \\a camera according to the\n * configuration specified in \\a config. The intended caller of this interface\n * is the Camera class which will receive configuration to apply from the\n * application.\n *\n * The configuration is guaranteed to have been validated with\n * CameraConfiguration::validate(). The pipeline handler implementation shall\n * not perform further validation and may rely on any custom field stored in its\n * custom CameraConfiguration derived class.\n *\n * When configuring the camera the pipeline handler shall associate a Stream\n * instance to each StreamConfiguration entry in the CameraConfiguration using\n * the StreamConfiguration::setStream() function.\n *\n * \\context This function is called from the CameraManager thread.\n *\n * \\return 0 on success or a negative error code otherwise"}], "queue": [{"text": "`PipelineHandler::registerRequest()` 함수는 요청이 생성될 때 호출되어 해당 요청을 위한 일회성 초기화를 수행할 기회를 제공합니다.", "evidence": ["queue"], "covers": ["queue"], "kind": "behavior", "quote": "\\fn PipelineHandler::registerRequest()\n * \\brief Register a request for use by the pipeline handler\n * \\param[in] request The request to register\n *\n * This function is called when the request is created, and allows the pipeline\n * handler to perform any one-time initialization it requries for the request.\n */\nvoid PipelineHandler::registerRequest(Request *request)\n{\n\t/*\n\t * Connect the request prepared signal to notify the pipeline handler\n\t * when a request is ready to be processed.\n\t */\n\trequest->_d()->prepared.connect(this, [this, request]() {\n\t\tdoQueueRequests(request->_d()->camera());\n\t});\n}", "part_id": "registration"}, {"text": "`PipelineHandler::registerRequest` 함수는 요청이 준비되었음을 알리는 `prepared` 신호에 연결된 콜백에서 실제로 호출하는 함수로 `doQueueRequests`를 사용합니다.", "evidence": ["registration-code"], "covers": ["queue"], "kind": "behavior", "quote": "void PipelineHandler::registerRequest(Request *request)\n{\n\t/*\n\t * Connect the request prepared signal to notify the pipeline handler\n\t * when a request is ready to be processed.\n\t */\n\trequest->_d()->prepared.connect(this, [this, request]() {\n\t\tdoQueueRequests(request->_d()->camera());\n\t});\n}", "part_id": "prepared-signal"}, {"text": "`queueRequest` 함수는 주어진 `request` 포인터를 `data->waitingRequests_`라는 내부 목록에 추가합니다.", "evidence": ["waiting-call"], "covers": ["queue"], "kind": "behavior", "quote": "data->waitingRequests_.push(request);", "part_id": "waiting"}, {"text": "`queueRequest` 함수는 요청을 대기열에 추가할 때 `prepare` 호출에 300ms 라는 시간 인자를 전달합니다.", "evidence": ["waiting-code"], "covers": ["queue"], "kind": "behavior", "quote": "request->_d()->prepare(300ms);\n}", "part_id": "prepare-argument"}, {"text": "`Request::Private::prepare` 함수는 하드웨어 장치에 요청을 대기열로 넣기 전에 각 프레임 버퍼의 획득 펜스(acquire fence)가 신호를 보냈는지 확인하여 준비 상태를 보장합니다.", "evidence": ["prepare"], "covers": ["queue"], "kind": "behavior", "quote": "\\brief Prepare the Request to be queued to the device\n * \\param[in] timeout Optional expiration timeout\n *\n * Prepare a Request to be queued to the hardware device by ensuring it is\n * ready for the incoming memory transfers.\n *\n * This currently means waiting on each frame buffer acquire fence to be\n * signalled. An optional expiration timeout can be specified. If not all the\n * fences have been signalled correctly before the timeout expires the Request\n * is cancelled.\n *\n * The function immediately emits the prepared signal if all the prepare\n * operations have been completed synchronously. If instead the prepare\n * operations require to wait the completion of asynchronous events, such as\n * fences notifications or timer expiration, the prepared signal is emitted upon\n * the asynchronous event completion.\n *\n * As we currently only handle fences, the function emits the prepared signal\n * immediately if there are no fences to wait on. Otherwise the prepared signal\n * is emitted when all fences have been signalled or the optional timeout has\n * expired.\n *\n * If not all the fences have been correctly signalled or the optional timeout\n * has expired the Request will be cancelled and the Request::prepared signal\n * emitted.\n *\n * The intended user of this function is the PipelineHandler base class, which\n * 'prepares' a Request before queuing it to the hardware device.\n */\nvoid Request::Private::prepare(std::chrono::milliseconds timeout)\n{\n\t/* Create and connect one notifier for each synchronization fence. */\n\tfor (FrameBuffer *buffer : pending_) {\n\t\tconst Fence *fence = buffer->_d()->fence();\n\t\tif (!fence)\n\t\t\tcontinue;", "part_id": "fences"}, {"text": "`doQueueRequests` 함수는 `queuedRequests_`의 크기를 `maxQueuedRequestsDevice_`와 비교하여 큐가 가득 찼을 때 요청 처리를 중단합니다.", "evidence": ["capacity-branch"], "covers": ["queue"], "kind": "behavior", "quote": "if (data->queuedRequests_.size() == maxQueuedRequestsDevice_)\n\t\t\tbreak;", "part_id": "capacity"}, {"text": "`doQueueRequests` 함수 내부에서 `data->queuedRequests_.size() == maxQueuedRequestsDevice_` 조건이 참일 때 실행되는 제어문은 `break`입니다.", "evidence": ["capacity-branch"], "covers": ["queue"], "kind": "behavior", "quote": "if (data->queuedRequests_.size() == maxQueuedRequestsDevice_)\n\t\t\tbreak;", "part_id": "capacity-exit"}, {"text": "`PipelineHandler::doQueueRequests` 함수는 `waitingRequests_` 큐의 선두 요청을 확인하며, 해당 요청의 `_d()->prepared_` 속성이 `false`이면 즉시 `break` 문을 실행하여 while 반복을 중단합니다.", "evidence": ["iterate-code"], "covers": ["queue"], "kind": "behavior", "quote": "Request *request = data->waitingRequests_.front();\n\t\tif (!request->_d()->prepared_)\n\t\t\tbreak;", "part_id": "head-ready"}, {"text": "`doQueueRequest` 함수는 요청을 처리하는 과정에서 `data->queuedRequests_`라는 컨테이너에 `request` 객체를 추가합니다.", "evidence": ["tracking-call"], "covers": ["queue"], "kind": "behavior", "quote": "data->queuedRequests_.push_back(request);", "part_id": "submit-tracking"}, {"text": "`request->_d()->sequence_`에 저장되는 값은 `data->requestSequence_++` 연산에서 후위 증가 연산자가 적용되기 전의 기존 값입니다.", "evidence": ["sequence-assignment"], "covers": ["queue"], "kind": "behavior", "quote": "request->_d()->sequence_ = data->requestSequence_++;", "part_id": "sequence"}, {"text": "`doQueueRequest` 함수에서 `request->_d()->cancelled_` 조건이 참이면 `completeRequest(request)` 함수를 호출합니다.", "evidence": ["submit-code"], "covers": ["queue"], "kind": "behavior", "quote": "if (request->_d()->cancelled_) {\n\t\tcompleteRequest(request);\n\t\treturn;\n\t}", "part_id": "cancelled"}, {"text": "`queueRequestDevice` 함수가 장치 제출을 위해 호출되어 `ret` 변수에 결과를 저장합니다.", "evidence": ["submit-result"], "covers": ["queue"], "kind": "behavior", "quote": "int ret = queueRequestDevice(camera, request);\n\tif (ret)\n\t\tcancelRequest(request);", "part_id": "device-submit"}, {"text": "`ret` 가 0 이 아닌 경우 `queueRequestDevice` 함수에서 반환된 오류가 발생했음을 의미하며, 이때 `cancelRequest` 함수를 호출합니다.", "evidence": ["submit-result"], "covers": ["queue"], "kind": "behavior", "quote": "int ret = queueRequestDevice(camera, request);\n\tif (ret)\n\t\tcancelRequest(request);", "part_id": "device-failure"}, {"text": "`PipelineHandler::queueRequestDevice` 구현자는 요청의 매개변수가 제공된 버퍼의 프레임에 적용되도록 기기를 프로그래밍해야 합니다.", "evidence": ["queue"], "covers": ["queue"], "kind": "behavior", "quote": "/**\n * \\fn PipelineHandler::queueRequestDevice()\n * \\brief Queue a request to the device\n * \\param[in] camera The camera to queue the request to\n * \\param[in] request The request to queue\n *\n * This function queues a capture request to the device for processing. The\n * request contains a set of buffers associated with streams and a set of\n * parameters. The pipeline handler shall program the device to ensure that the\n * parameters will be applied to the frames captured in the buffers provided in\n * the request.\n *\n * \\context This function is called from the CameraManager thread.\n *\n * \\return 0 on success or a negative error code otherwise\n */", "part_id": "device-contract"}], "completion": [{"text": "`PipelineHandler::completeBuffer` 함수는 요청에 포함된 버퍼가 완료되었음을 애플리케이션에 알리고 요청의 내부 버퍼 추적을 업데이트하는 역할을 수행합니다.", "evidence": ["buffer-contract"], "covers": ["completion"], "kind": "behavior", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}", "part_id": "buffer"}, {"text": "`completeBuffer()` 함수는 마지막 버퍼가 완료되어도 요청을 자동으로 완료하지 않으며, 구현자는 반드시 `completeRequest()` 함수를 호출해야 합니다.", "evidence": ["buffer-contract"], "covers": ["completion"], "kind": "behavior", "quote": "\\brief Complete a buffer for a request\n * \\param[in] request The request the buffer belongs to\n * \\param[in] buffer The buffer that has completed\n *\n * This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().\n *\n * \\context This function shall be called from the CameraManager thread.\n *\n * \\return True if all buffers contained in the request have completed, false\n * otherwise\n */\nbool PipelineHandler::completeBuffer(Request *request, FrameBuffer *buffer)\n{\n\tCamera *camera = request->_d()->camera();\n\tcamera->bufferCompleted.emit(request, buffer);\n\treturn request->_d()->completeBuffer(buffer);\n}", "part_id": "buffer-not-request"}, {"text": "`PipelineHandler::completeRequest` 함수가 반환한 뒤 파이프라인 핸들러는 해당 요청에 접근해서는 안 됩니다.", "evidence": ["request-contract"], "covers": ["completion"], "kind": "behavior", "quote": "\\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();", "part_id": "lifetime"}, {"text": "`completeRequest` 함수는 요청이 제출된 순서대로 애플리케이션으로 반환되도록 보장합니다.", "evidence": ["ordering-contract"], "covers": ["completion"], "kind": "behavior", "quote": "This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.", "part_id": "ordering"}, {"text": "`completeRequest` 함수 내부의 `while` 루프가 큐 앞단의 요청 상태를 확인하다가 `req->status() == Request::RequestPending` 조건을 만족하면, 해당 요청에 대해 `break` 문을 실행하여 루프를 즉시 중단합니다.", "evidence": ["request-code"], "covers": ["completion"], "kind": "behavior", "quote": "while (!data->queuedRequests_.empty()) {\n\t\tRequest *req = data->queuedRequests_.front();\n\t\tif (req->status() == Request::RequestPending)\n\t\t\tbreak;", "part_id": "pending"}, {"text": "`PipelineHandler::completeRequest` 함수는 요청 완료 처리가 끝난 직후, `/* Allow any waiting requests to be queued to the pipeline. */` 주석을 달고 `doQueueRequests(camera)`를 호출합니다.", "evidence": ["request-code"], "covers": ["completion"], "kind": "behavior", "quote": "/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}", "part_id": "resume"}, {"text": "`PipelineHandler::completeRequest` 와 `PipelineHandler::completeBuffer` 함수는 호출될 때 반드시 `CameraManager` 스레드 문맥에서 실행되어야 합니다.", "evidence": ["request-contract"], "covers": ["completion"], "kind": "behavior", "quote": "\\brief Signal request completion\n * \\param[in] request The request that has completed\n *\n * The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.\n *\n * \\context This function shall be called from the CameraManager thread.\n */\nvoid PipelineHandler::completeRequest(Request *request)\n{\n\tCamera *camera = request->_d()->camera();", "part_id": "thread"}, {"text": "`PipelineHandler::cancelRequest` 함수는 요청을 취소하고 완료 상태로 전환하며, 이 과정에서 `completeRequest` 함수를 호출합니다.", "evidence": ["cancel-contract"], "covers": ["completion"], "kind": "behavior", "quote": "\\brief Cancel request and signal its completion\n * \\param[in] request The request to cancel\n *\n * This function cancels and completes the request. The same rules as for\n * completeRequest() apply.\n */\nvoid PipelineHandler::cancelRequest(Request *request)\n{\n\trequest->_d()->cancel();\n\tcompleteRequest(request);\n}", "part_id": "cancel"}], "shutdown": [{"text": "`PipelineHandler::stop` 함수는 모든 대기 중인 요청을 재배열되지 않도록 방지하기 위해 `data->waitingRequests_` 큐를 별도의 `waitingRequests` 변수로 분리합니다.", "evidence": ["stop"], "covers": ["shutdown"], "kind": "behavior", "quote": "\\brief Stop capturing from all running streams and cancel pending requests\n * \\param[in] camera The camera to stop\n *\n * This function stops capturing and processing requests immediately. All\n * pending requests are cancelled and complete immediately in an error state.\n *\n * \\context This function is called from the CameraManager thread.\n */\nvoid PipelineHandler::stop(Camera *camera)\n{\n\t/*\n\t * Take all waiting requests so that they are not requeued in response\n\t * to completeRequest() being called inside stopDevice(). Cancel them\n\t * after the device to keep them in order.\n\t */\n\tCamera::Private *data = camera->_d();\n\tstd::queue<Request *> waitingRequests;\n\twaitingRequests.swap(data->waitingRequests_);", "part_id": "detach"}, {"text": "`PipelineHandler::stop` 함수는 먼저 `waitingRequests_` 큐에 대기 중인 요청들을 분리하여 임시로 저장한 뒤, 그 다음 단계에서 호출하는 장치 정지 함수인 `stopDevice`를 실행합니다.", "evidence": ["stop"], "covers": ["shutdown"], "kind": "behavior", "quote": "\\brief Stop capturing from all running streams and cancel pending requests\n * \\param[in] camera The camera to stop\n *\n * This function stops capturing and processing requests immediately. All\n * pending requests are cancelled and complete immediately in an error state.\n *\n * \\context This function is called from the CameraManager thread.\n */\nvoid PipelineHandler::stop(Camera *camera)\n{\n\t/*\n\t * Take all waiting requests so that they are not requeued in response\n\t * to completeRequest() being called inside stopDevice(). Cancel them\n\t * after the device to keep them in order.\n\t */\n\tCamera::Private *data = camera->_d();\n\tstd::queue<Request *> waitingRequests;\n\twaitingRequests.swap(data->waitingRequests_);", "part_id": "device-call"}, {"text": "`PipelineHandler::stop` 함수 내부에서 `stopDevice` 가 반환한 뒤, 분리해 둔 대기 요청들을 하나씩 꺼내어 각각의 `_d()->cancel()` 을 통해 취소하고 바로 `doQueueRequest` 로 처리합니다.", "evidence": ["stop"], "covers": ["shutdown"], "kind": "behavior", "quote": "/*\n\t\t * Cancel all requests by marking them as cancelled and calling\n\t\t * doQueueRequest() instead of cancelRequest(). This ensures\n\t\t * that the requests get a sequence number and are temporarily\n\t\t * added to queuedRequests_ so they can be properly completed in\n\t\t * completeRequest().\n\t\t */\n\t\trequest->_d()->cancel();\n\t\tdoQueueRequest(request);\n\t}", "part_id": "pending"}, {"text": "`PipelineHandler::stopDevice` 함수는 캡처와 요청 처리를 즉시 중단해야 합니다.", "evidence": ["stop"], "covers": ["shutdown"], "kind": "behavior", "quote": "/**\n * \\fn PipelineHandler::stopDevice()\n * \\brief Stop capturing from all running streams\n * \\param[in] camera The camera to stop\n *\n * This function stops capturing and processing requests immediately. All\n * pending requests are cancelled and complete immediately in an error state.\n */", "part_id": "device-duty"}, {"text": "`PipelineHandler::stop` 함수는 마지막에 `data->queuedRequests_.empty()`와 `data->waitingRequests_.empty()`를 확인하는 두 개의 `ASSERT`를 실행합니다.", "evidence": ["stop"], "covers": ["shutdown"], "kind": "behavior", "quote": "/* Make sure no requests are pending. */\n\tASSERT(data->queuedRequests_.empty());\n\tASSERT(data->waitingRequests_.empty());", "part_id": "assertions"}, {"text": "`PipelineHandler::completeRequest` 함수가 호출되면, 마지막 버퍼가 완료되어도 요청이 자동으로 끝나는 것은 아니며, 파이프라인 핸들러는 명시적으로 `completeRequest()`를 호출해야 합니다. 이 함수 내부에서는 대기 중인 요청 목록을 확인하고, 모든 요청이 처리되었을 때 새로운 요청들을 다시 큐에 넣기 위해 `doQueueRequests(camera)`를 호출합니다.", "evidence": ["completion"], "covers": ["shutdown"], "kind": "behavior", "quote": "/* Allow any waiting requests to be queued to the pipeline. */\n\tdoQueueRequests(camera);\n}", "part_id": "reentry"}]}, "topic_inputs": {"responsibility": "a586433e26f0c75a800b7419b40bbc13b3c6fc67fe0edf860bc9d5b4a868e75e", "configuration": "8e430b42fa9f340c9f245d4b7b54be4131d4b4095b54b4f656ffaa3d51ea03b4", "queue": "77076552b77748a49ddc422695bf7fde813ff326852325f220e465c1cdc11ec2", "completion": "be23b2d22034a9a7b4c27fbbf0846a60653a84b4de5404414c7108f59f017d7f", "shutdown": "74f83ef1f6de006b278c984bcba0d58f4df476a4f6bd60174540a21123e0af32"}, "reused_topics": ["responsibility", "configuration", "queue", "completion", "shutdown"], "replayed_units": [], "generated_topics": [], "topic_agents": {"responsibility": "ollama/qwen3.5:9b", "configuration": "ollama/qwen3.5:9b", "queue": "ollama/qwen3.5:9b", "completion": "ollama/qwen3.5:9b", "shutdown": "ollama/qwen3.5:9b"}, "grounding_review": "passed", "grounding_policy": "c54006f7c90cb2af955e1ede18b761c7feb22dffa3bc37a885c019508348eba0", "body_sha256": "397143f2aa3c974fc4682ac2c288a59f4c5170c66acfc25973d3face2051b760"}
---

# Pipeline Handler

**파이프라인 구현이 지켜야 하는 구성·요청·완료·종료 계약을 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 장치 매칭과 객체 수명 절을 확인합니다. | [장치 매칭과 객체 수명](#장치-매칭과-객체-수명) |
| 구성의 입력과 검증 책임 절을 확인합니다. | [구성의 입력과 검증 책임](#구성의-입력과-검증-책임) |
| 요청 준비와 장치 큐 절을 확인합니다. | [요청 준비와 장치 큐](#요청-준비와-장치-큐) |
| 버퍼 완료와 요청 반환 절을 확인합니다. | [버퍼 완료와 요청 반환](#버퍼-완료와-요청-반환) |
| 정지와 미완료 요청 절을 확인합니다. | [정지와 미완료 요청](#정지와-미완료-요청) |

## 장치 매칭과 객체 수명

`PipelineHandler` 는 `DeviceEnumerator` 가 제공하는 미디어 장치와 지원 가능한 파이프라인을 매칭하여 해당하는 `Camera` 장치를 생성하고 관리합니다. `src/libcamera/pipeline_handler.cpp:50`

`PipelineHandler` 인스턴스는 `std::shared_ptr`< > 를 통해 참조 카운팅되며, 멤버 함수에서 'this' 포인터만 사용 가능한 코드 경로에서 새로운 공유 포인터를 생성하기 위해 `std::enable_shared_from_this`< > 를 구현합니다. `src/libcamera/pipeline_handler.cpp:50`

`PipelineHandler` 인스턴스는 수동으로 생성되어서는 안 되며, 항상 `PipelineHandlerFactoryBase::create()` 함수를 통해 생성되어야 합니다. `src/libcamera/pipeline_handler.cpp:50`

`PipelineHandler` 가 소멸될 때, 매칭된 모든 `MediaDevice` 는 순차적으로 release() 호출을 통해 해제됩니다. `src/libcamera/pipeline_handler.cpp:50`

match() 함수는 파이프라인에 필요한 모든 미디어 장치가 시스템에서 발견되면 `MediaDevice::acquire()` 를 호출하여 장치를 확보하고, 해당하는 `Camera` 인스턴스를 생성한 후 카메라 매니저에 등록합니다. `src/libcamera/pipeline_handler.cpp:50`

match() 함수가 모든 파이프라인에 필요한 미디어 장치를 찾지 못하면, 어떤 미디어 장치도 확보하지 않거나 확보한 장치를 모두 해제하고 false 를 반환합니다. `src/libcamera/pipeline_handler.cpp:50`

acquireMediaDevice() 함수는 장치 매칭 패턴에 맞는 사용 가능한 미디어 장치를 검색하여 확보한 후, 파이프라인 핸들러가 소멸될 때 자동으로 해제되도록 처리합니다. `src/libcamera/pipeline_handler.cpp:119`

acquireMediaDevice() 함수는 장치 확보에 실패하면 nullptr 를 반환하며, 호출자는 장치를 명시적으로 해제해서는 안 됩니다. `src/libcamera/pipeline_handler.cpp:119`

근거 원문: [src/libcamera/pipeline_handler.cpp:50](#source-69bfa9568cf8b5c5) · [src/libcamera/pipeline_handler.cpp:119](#source-a3caf1625bc18d64)

## 구성의 입력과 검증 책임

generateConfiguration() 함수는 지정된 카메라에 대한 기본 설정을 생성하며, 호출자는 이 함수를 통해 원하는 사용 사례 (use-cases) 를 위한 스트림 역할 목록을 roles 매개변수에 채워 넣어야 합니다. 이 함수는 어떤 스레드에서나 호출할 수 있으며 파이프라인 핸들러의 상태 변경 없이 안전하게 실행됩니다. 요청된 역할이 충족될 경우 유효한 `CameraConfiguration` 객체를 반환하지만, 그렇지 않으면 null 포인터를 반환합니다. `src/libcamera/pipeline_handler.cpp:271`

configure() 함수는 `CameraManager` 스레드에서 호출되며, 해당 카메라의 스트림 그룹을 설정된 구성에 따라 구성합니다. 이 함수를 호출하기 전에 제공된 `CameraConfiguration` 객체는 반드시 `CameraConfiguration::validate()` 를 통해 검증되었어야 하며, 파이프라인 핸들러 구현은 추가 검증을 수행하지 않고 커스텀 필드를 신뢰할 수 있습니다. `src/libcamera/pipeline_handler.cpp:271`

configure() 함수를 호출할 때 파이프라인 핸들러는 `CameraConfiguration` 내의 각 `StreamConfiguration` 항목에 대해 `Stream` 인스턴스를 setStream() 함수를 사용하여 연결해야 합니다. 성공 시 0 을 반환하고 실패 시 음수 오류 코드를 반환하며, 이는 실제 구현에서 발생할 수 있는 동작을 나타냅니다. `src/libcamera/pipeline_handler.cpp:271`

근거 원문: [src/libcamera/pipeline_handler.cpp:271](#source-8cd14a802c5b1782)

## 요청 준비와 장치 큐

`PipelineHandler::registerRequest()` 함수는 요청이 생성될 때 호출되어 해당 요청을 위한 일회성 초기화를 수행할 기회를 제공합니다. `src/libcamera/pipeline_handler.cpp:428`

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

[Mermaid 원문](pipeline-handler.queue-gates.mmd)

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

`PipelineHandler::registerRequest` 함수는 요청이 준비되었음을 알리는 `prepared` 신호에 연결된 콜백에서 실제로 호출하는 함수로 `doQueueRequests`를 사용합니다. `src/libcamera/pipeline_handler.cpp:435`

`queueRequest` 함수는 주어진 `request` 포인터를 `data->waitingRequests_`라는 내부 목록에 추가합니다. `src/libcamera/pipeline_handler.cpp:475`

`queueRequest` 함수는 요청을 대기열에 추가할 때 `prepare` 호출에 300ms 라는 시간 인자를 전달합니다. `src/libcamera/pipeline_handler.cpp:469`

`Request::Private::prepare` 함수는 하드웨어 장치에 요청을 대기열로 넣기 전에 각 프레임 버퍼의 획득 펜스(acquire fence)가 신호를 보냈는지 확인하여 준비 상태를 보장합니다. `src/libcamera/request.cpp:199`

`doQueueRequests` 함수는 `queuedRequests_`의 크기를 `maxQueuedRequestsDevice_`와 비교하여 큐가 가득 찼을 때 요청 처리를 중단합니다. `src/libcamera/pipeline_handler.cpp:513`

`doQueueRequests` 함수 내부에서 `data->queuedRequests_.size() == maxQueuedRequestsDevice_` 조건이 참일 때 실행되는 제어문은 `break`입니다. `src/libcamera/pipeline_handler.cpp:513`

`PipelineHandler::doQueueRequests` 함수는 `waitingRequests_` 큐의 선두 요청을 확인하며, 해당 요청의 `_d()->prepared_` 속성이 `false`이면 즉시 `break` 문을 실행하여 while 반복을 중단합니다. `src/libcamera/pipeline_handler.cpp:509`

`doQueueRequest` 함수는 요청을 처리하는 과정에서 `data->queuedRequests_`라는 컨테이너에 `request` 객체를 추가합니다. `src/libcamera/pipeline_handler.cpp:489`

`request->_d()->sequence_`에 저장되는 값은 `data->requestSequence_++` 연산에서 후위 증가 연산자가 적용되기 전의 기존 값입니다. `src/libcamera/pipeline_handler.cpp:491`

`doQueueRequest` 함수에서 `request->_d()->cancelled_` 조건이 참이면 `completeRequest(request)` 함수를 호출합니다. `src/libcamera/pipeline_handler.cpp:483`

`queueRequestDevice` 함수가 장치 제출을 위해 호출되어 `ret` 변수에 결과를 저장합니다. `src/libcamera/pipeline_handler.cpp:498`

`ret` 가 0 이 아닌 경우 `queueRequestDevice` 함수에서 반환된 오류가 발생했음을 의미하며, 이때 `cancelRequest` 함수를 호출합니다. `src/libcamera/pipeline_handler.cpp:498`

`PipelineHandler::queueRequestDevice` 구현자는 요청의 매개변수가 제공된 버퍼의 프레임에 적용되도록 기기를 프로그래밍해야 합니다. `src/libcamera/pipeline_handler.cpp:428`

근거 원문: [src/libcamera/pipeline_handler.cpp:428](#source-789eafedfaa7f3c5) · [src/libcamera/request.cpp:199](#source-4f52447929ee8da9) · [src/libcamera/pipeline_handler.cpp:435](#source-2e194e2fc68579c3) · [src/libcamera/pipeline_handler.cpp:469](#source-c86b50cadd8a5947) · [src/libcamera/pipeline_handler.cpp:483](#source-8bf901f3faef18e5) · [src/libcamera/pipeline_handler.cpp:509](#source-d63c9e57bcf862b0) · [src/libcamera/pipeline_handler.cpp:489](#source-ce717689071a887f) · [src/libcamera/pipeline_handler.cpp:491](#source-a8f47a79aca791ea) · [src/libcamera/pipeline_handler.cpp:475](#source-3ad79b52195fbc58) · [src/libcamera/pipeline_handler.cpp:513](#source-819fe99ec52b734f) · [src/libcamera/pipeline_handler.cpp:498](#source-1e06e477d10056b7)

## 버퍼 완료와 요청 반환

`PipelineHandler::completeBuffer` 함수는 요청에 포함된 버퍼가 완료되었음을 애플리케이션에 알리고 요청의 내부 버퍼 추적을 업데이트하는 역할을 수행합니다. `src/libcamera/pipeline_handler.cpp:547`

<!-- sdd:visual:buffer-request-completion -->
### 버퍼 완료에서 요청 반환까지

마지막 버퍼의 완료가 요청을 자동 완료하지 않습니다. 핸들러의 명시적 요청 완료 통지가 필요합니다.

```mermaid
flowchart TB
%% sdd:translations {"completeBuffer()": "completeBuffer()", "completeRequest()": "completeRequest()", "버퍼 완료 알림": "Notify buffer completion", "버퍼 추적 상태 갱신": "Update buffer completion <br/>tracking", "선두 미완료 요청 뒤의 <br/>반환은 대기": "Wait behind an incomplete <br/>head request", "제출 순서로 애플리케이션 <br/>반환": "Return to application in <br/>submission order", "후처리 뒤 구현자가 <br/>명시적으로 호출": "Handler explicitly <br/>completes after remaining <br/>work"}
  v_buffer["completeBuffer()"]
  v_remaining["버퍼 추적 상태 갱신"]
  v_request["completeRequest()"]
  v_application["제출 순서로 애플리케이션 <br/>반환"]
  v_buffer -->|"버퍼 완료 알림"| v_remaining
  v_remaining -->|"후처리 뒤 구현자가 <br/>명시적으로 호출"| v_request
  v_request -->|"선두 미완료 요청 뒤의 <br/>반환은 대기"| v_application
```

[Mermaid 원문](pipeline-handler.buffer-request-completion.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | completeBuffer() | [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) |
    | 버퍼 추적 상태 갱신 | [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) |
    | completeRequest() | [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) |
    | 제출 순서로 애플리케이션 반환 | [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) |
    | 버퍼 완료 알림 | [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) |
    | 후처리 뒤 구현자가 명시적으로 호출 | [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) |
    | 선두 미완료 요청 뒤의 반환은 대기 | [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) |
<!-- /sdd:visual:buffer-request-completion -->

`completeBuffer()` 함수는 마지막 버퍼가 완료되어도 요청을 자동으로 완료하지 않으며, 구현자는 반드시 `completeRequest()` 함수를 호출해야 합니다. `src/libcamera/pipeline_handler.cpp:547`

`PipelineHandler::completeRequest` 함수가 반환한 뒤 파이프라인 핸들러는 해당 요청에 접근해서는 안 됩니다. `src/libcamera/pipeline_handler.cpp:571`

`completeRequest` 함수는 요청이 제출된 순서대로 애플리케이션으로 반환되도록 보장합니다. `src/libcamera/pipeline_handler.cpp:578`

`completeRequest` 함수 내부의 `while` 루프가 큐 앞단의 요청 상태를 확인하다가 `req->status() == Request::RequestPending` 조건을 만족하면, 해당 요청에 대해 `break` 문을 실행하여 루프를 즉시 중단합니다. `src/libcamera/pipeline_handler.cpp:584`

`PipelineHandler::completeRequest` 함수는 요청 완료 처리가 끝난 직후, `/* Allow any waiting requests to be queued to the pipeline. */` 주석을 달고 `doQueueRequests(camera)`를 호출합니다. `src/libcamera/pipeline_handler.cpp:584`

`PipelineHandler::completeRequest` 와 `PipelineHandler::completeBuffer` 함수는 호출될 때 반드시 `CameraManager` 스레드 문맥에서 실행되어야 합니다. `src/libcamera/pipeline_handler.cpp:571`

`PipelineHandler::cancelRequest` 함수는 요청을 취소하고 완료 상태로 전환하며, 이 과정에서 `completeRequest` 함수를 호출합니다. `src/libcamera/pipeline_handler.cpp:607`

근거 원문: [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a) · [src/libcamera/pipeline_handler.cpp:547](#source-f389c6ca68ade3da) · [src/libcamera/pipeline_handler.cpp:571](#source-236c920e906cb6fd) · [src/libcamera/pipeline_handler.cpp:584](#source-b6dd86e931d905ed) · [src/libcamera/pipeline_handler.cpp:607](#source-27cb6869fd89d13d) · [src/libcamera/pipeline_handler.cpp:578](#source-16187edaf24c09f5)

## 정지와 미완료 요청

`PipelineHandler::stop` 함수는 모든 대기 중인 요청을 재배열되지 않도록 방지하기 위해 `data->waitingRequests_` 큐를 별도의 `waitingRequests` 변수로 분리합니다. `src/libcamera/pipeline_handler.cpp:359`

`PipelineHandler::stop` 함수는 먼저 `waitingRequests_` 큐에 대기 중인 요청들을 분리하여 임시로 저장한 뒤, 그 다음 단계에서 호출하는 장치 정지 함수인 `stopDevice`를 실행합니다. `src/libcamera/pipeline_handler.cpp:359`

`PipelineHandler::stop` 함수 내부에서 `stopDevice` 가 반환한 뒤, 분리해 둔 대기 요청들을 하나씩 꺼내어 각각의 `_d()->cancel()` 을 통해 취소하고 바로 `doQueueRequest` 로 처리합니다. `src/libcamera/pipeline_handler.cpp:359`

`PipelineHandler::stopDevice` 함수는 캡처와 요청 처리를 즉시 중단해야 합니다. `src/libcamera/pipeline_handler.cpp:359`

`PipelineHandler::stop` 함수는 마지막에 `data->queuedRequests_.empty()`와 `data->waitingRequests_.empty()`를 확인하는 두 개의 `ASSERT`를 실행합니다. `src/libcamera/pipeline_handler.cpp:359`

`PipelineHandler::completeRequest` 함수가 호출되면, 마지막 버퍼가 완료되어도 요청이 자동으로 끝나는 것은 아니며, 파이프라인 핸들러는 명시적으로 `completeRequest()`를 호출해야 합니다. 이 함수 내부에서는 대기 중인 요청 목록을 확인하고, 모든 요청이 처리되었을 때 새로운 요청들을 다시 큐에 넣기 위해 `doQueueRequests(camera)`를 호출합니다. `src/libcamera/pipeline_handler.cpp:547`

근거 원문: [src/libcamera/pipeline_handler.cpp:359](#source-eefd1bbecb1aad0a) · [src/libcamera/pipeline_handler.cpp:547](#source-01ad7c6605c3296a)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 핸들러는 어떤 객체와 장치를 만들고 관리합니까? | [장치 매칭과 객체 수명](#장치-매칭과-객체-수명) | 코드 근거와 설명 연결 |
    | 기본 구성과 실제 구성에서 호출자와 구현의 책임은 무엇입니까? | [구성의 입력과 검증 책임](#구성의-입력과-검증-책임) | 코드 근거와 설명 연결 |
    | 요청을 장치로 넘기는 조건과 실패 처리는 무엇입니까? | [요청 준비와 장치 큐](#요청-준비와-장치-큐) | 코드 근거와 설명 연결 |
    | 버퍼 완료, 요청 완료와 접근 가능한 수명은 어떻게 구분됩니까? | [버퍼 완료와 요청 반환](#버퍼-완료와-요청-반환) | 코드 근거와 설명 연결 |
    | 정지 중 재큐잉을 막고 대기 요청을 반환하는 방법은 무엇입니까? | [정지와 미완료 요청](#정지와-미완료-요청) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-69bfa9568cf8b5c5"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:50"
    `src/libcamera/pipeline_handler.cpp:50`에서 시작하는 발췌입니다. 종료 줄은 119이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e05278df0a06cb963fe79f772e62d4560b62df15c1411a6b49e32f7ca84d9e74`
    
    ```text
    \class PipelineHandler
     * \brief Create and manage cameras based on a set of media devices
     *
     * The PipelineHandler matches the media devices provided by a DeviceEnumerator
     * with the pipelines it supports and creates corresponding Camera devices.
     *
     * Pipeline handler instances are reference-counted through std::shared_ptr<>.
     * They implement std::enable_shared_from_this<> in order to create new
     * std::shared_ptr<> in code paths originating from member functions of the
     * PipelineHandler class where only the 'this' pointer is available.
     */
    
    /**
     * \brief Construct a PipelineHandler instance
     * \param[in] manager The camera manager
     * \param[in] maxQueuedRequestsDevice The maximum number of requests queued to
     * the device
     *
     * In order to honour the std::enable_shared_from_this<> contract,
     * PipelineHandler instances shall never be constructed manually, but always
     * through the PipelineHandlerFactoryBase::create() function.
     */
    PipelineHandler::PipelineHandler(CameraManager *manager,
    				 unsigned int maxQueuedRequestsDevice)
    	: manager_(manager), maxQueuedRequestsDevice_(maxQueuedRequestsDevice),
    	  useCount_(0)
    {
    }
    
    PipelineHandler::~PipelineHandler()
    {
    	for (std::shared_ptr<MediaDevice> &media : mediaDevices_)
    		media->release();
    }
    
    /**
     * \fn PipelineHandler::match(DeviceEnumerator *enumerator)
     * \brief Match media devices and create camera instances
     * \param[in] enumerator The enumerator providing all media devices found in the
     * system
     *
     * This function is the main entry point of the pipeline handler. It is called
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
     * If multiple instances of a pipeline are available in the system, the
     * PipelineHandler class will be instantiated once per instance, and its match()
     * function called for every instance. Each call shall acquire media devices for
     * one pipeline instance, until all compatible media devices are exhausted.
     *
     * If this function returns true, a new instance of the pipeline handler will
     * be created and its match() function called.
     *
     * \context This function is called from the CameraManager thread.
     *
     * \return true if media devices have been acquired and camera instances
     * created, or false otherwise
     */
    
    /**
     * \brief Search and acquire a MediaDevice
    ```

<a id="source-a3caf1625bc18d64"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:119"
    `src/libcamera/pipeline_handler.cpp:119`에서 시작하는 발췌입니다. 종료 줄은 271이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `379b17c52a1e97055bf78aaabd964595fb3ec506c568d112e552ed1c29235591`
    
    ```text
    \brief Search and acquire a MediaDevice matching a device pattern
     * \param[in] enumerator Enumerator containing all media devices in the system
     * \param[in] dm Device match pattern
     *
     * Search the device \a enumerator for an available media device matching the
     * device match pattern \a dm. Matching media device that have previously been
     * acquired by MediaDevice::acquire() are not considered. If a match is found,
     * the media device is acquired and returned. The caller shall not release the
     * device explicitly, it will be automatically released when the pipeline
     * handler is destroyed.
     *
     * \context This function shall be called from the CameraManager thread.
     *
     * \return A shared pointer to the matching MediaDevice, or nullptr if no match
     * is found
     */
    std::shared_ptr<MediaDevice>
    PipelineHandler::acquireMediaDevice(DeviceEnumerator *enumerator,
    				    const DeviceMatch &dm)
    {
    	std::shared_ptr<MediaDevice> media = enumerator->search(dm);
    	if (!media)
    		return nullptr;
    
    	if (!media->acquire())
    		return nullptr;
    
    	mediaDevices_.push_back(media);
    
    	return media;
    }
    
    /**
     * \brief Acquire exclusive access to the pipeline handler for the process
     *
     * This function locks all the media devices used by the pipeline to ensure
     * that no other process can access them concurrently.
     *
     * Access to a pipeline handler may be acquired recursively from within the
     * same process. Every successful acquire() call shall be matched with a
     * release() call. This allows concurrent access to the same pipeline handler
     * from different cameras within the same process.
     *
     * Pipeline handlers shall not call this function directly as the Camera class
     * handles access internally.
     *
     * \context This function is called from the CameraManager thread.
     *
     * \return True if the pipeline handler was acquired, false if another process
     * has already acquired it
     * \sa release()
     */
    bool PipelineHandler::acquire(Camera *camera)
    {
    	if (useCount_ == 0) {
    		for (std::shared_ptr<MediaDevice> &media : mediaDevices_) {
    			if (!media->lock()) {
    				unlockMediaDevices();
    				return false;
    			}
    		}
    	}
    
    	if (!acquireDevice(camera)) {
    		if (useCount_ == 0)
    			unlockMediaDevices();
    
    		return false;
    	}
    
    	++useCount_;
    	return true;
    }
    
    /**
     * \brief Release exclusive access to the pipeline handler
     * \param[in] camera The camera for which to release data
     *
     * This function releases access to the pipeline handler previously acquired by
     * a call to acquire(). Every release() call shall match a previous successful
     * acquire() call. Calling this function on a pipeline handler that hasn't been
     * acquired results in undefined behaviour.
     *
     * Pipeline handlers shall not call this function directly as the Camera class
     * handles access internally.
     *
     * \context This function is called from the CameraManager thread.
     *
     * \sa acquire()
     */
    void PipelineHandler::release(Camera *camera)
    {
    	ASSERT(useCount_);
    
    	releaseDevice(camera);
    
    	if (useCount_ == 1)
    		unlockMediaDevices();
    
    	--useCount_;
    }
    
    /**
     * \brief Acquire resources associated with this camera
     * \param[in] camera The camera for which to acquire resources
     *
     * Pipeline handlers may override this in order to get resources such as opening
     * devices and allocating buffers when a camera is acquired.
     *
     * This is used by the uvcvideo pipeline handler to delay opening /dev/video#
     * until the camera is acquired to avoid excess power consumption. The delayed
     * opening of /dev/video# is a special case because the kernel uvcvideo driver
     * powers on the USB device as soon as /dev/video# is opened. This behavior
     * should *not* be copied by other pipeline handlers.
     *
     * \context This function is called from the CameraManager thread.
     *
     * \return True on success, false on failure
     * \sa releaseDevice()
     */
    bool PipelineHandler::acquireDevice([[maybe_unused]] Camera *camera)
    {
    	return true;
    }
    
    /**
     * \brief Release resources associated with this camera
     * \param[in] camera The camera for which to release resources
     *
     * Pipeline handlers may override this in order to perform cleanup operations
     * when a camera is released, such as freeing memory.
     *
     * This is called once for every camera that is released. If there are resources
     * shared by multiple cameras then the pipeline handler must take care to not
     * release them until releaseDevice() has been called for all previously
     * acquired cameras.
     *
     * \context This function is called from the CameraManager thread.
     *
     * \sa acquireDevice()
     */
    void PipelineHandler::releaseDevice([[maybe_unused]] Camera *camera)
    {
    }
    
    void PipelineHandler::unlockMediaDevices()
    {
    	for (std::shared_ptr<MediaDevice> &media : mediaDevices_)
    		media->unlock();
    }
    
    /**
     * \fn PipelineHandler::generateConfiguration()
    ```

<a id="source-8cd14a802c5b1782"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:271"
    `src/libcamera/pipeline_handler.cpp:271`에서 시작하는 발췌입니다. 종료 줄은 315이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `56e3a59872a70fc01b1bfdea1601201880929f47ae90d7888c2cf4c080085ea6`
    
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
    
    /**
     * \fn PipelineHandler::configure()
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

<a id="source-4f52447929ee8da9"></a>

??? note "소스 근거: src/libcamera/request.cpp:199"
    `src/libcamera/request.cpp:199`에서 시작하는 발췌입니다. 종료 줄은 263이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `97d311c371577c108a7c9e936dc85fca0cbcc912ac3de743229c1d2647590bd3`
    
    ```text
    \brief Prepare the Request to be queued to the device
     * \param[in] timeout Optional expiration timeout
     *
     * Prepare a Request to be queued to the hardware device by ensuring it is
     * ready for the incoming memory transfers.
     *
     * This currently means waiting on each frame buffer acquire fence to be
     * signalled. An optional expiration timeout can be specified. If not all the
     * fences have been signalled correctly before the timeout expires the Request
     * is cancelled.
     *
     * The function immediately emits the prepared signal if all the prepare
     * operations have been completed synchronously. If instead the prepare
     * operations require to wait the completion of asynchronous events, such as
     * fences notifications or timer expiration, the prepared signal is emitted upon
     * the asynchronous event completion.
     *
     * As we currently only handle fences, the function emits the prepared signal
     * immediately if there are no fences to wait on. Otherwise the prepared signal
     * is emitted when all fences have been signalled or the optional timeout has
     * expired.
     *
     * If not all the fences have been correctly signalled or the optional timeout
     * has expired the Request will be cancelled and the Request::prepared signal
     * emitted.
     *
     * The intended user of this function is the PipelineHandler base class, which
     * 'prepares' a Request before queuing it to the hardware device.
     */
    void Request::Private::prepare(std::chrono::milliseconds timeout)
    {
    	/* Create and connect one notifier for each synchronization fence. */
    	for (FrameBuffer *buffer : pending_) {
    		const Fence *fence = buffer->_d()->fence();
    		if (!fence)
    			continue;
    
    		auto [it, inserted] = notifiers_.try_emplace(buffer, fence->fd().get(), EventNotifier::Type::Read);
    		ASSERT(inserted);
    
    		it->second.activated.connect(this, [this, buffer] {
    			notifierActivated(buffer);
    		});
    	}
    
    	if (notifiers_.empty()) {
    		emitPrepareCompleted();
    		return;
    	}
    
    	/*
    	 * In case a timeout is specified, create a timer and set it up.
    	 *
    	 * The timer must be created here instead of in the Request constructor,
    	 * in order to be bound to the pipeline handler thread.
    	 */
    	if (timeout != 0ms) {
    		timer_ = std::make_unique<Timer>();
    		timer_->timeout.connect(this, &Request::Private::timeout);
    		timer_->start(timeout);
    	}
    }
    
    /**
     * \var Request::Private::prepared
    ```

<a id="source-2e194e2fc68579c3"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:435"
    `src/libcamera/pipeline_handler.cpp:435`에서 시작하는 발췌입니다. 종료 줄은 444이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `ceadd0f83ea31d5d8a39a1673cb0e9b9b4f0f9d212cb5161241a6eec94b0c193`
    
    ```text
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
    ```

<a id="source-c86b50cadd8a5947"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:469"
    `src/libcamera/pipeline_handler.cpp:469`에서 시작하는 발췌입니다. 종료 줄은 483이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e407d584d54cee2098dd5730446a692093cc16cc54785bd294c39457e562a622`
    
    ```text
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
    ```

<a id="source-8bf901f3faef18e5"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:483"
    `src/libcamera/pipeline_handler.cpp:483`에서 시작하는 발췌입니다. 종료 줄은 504이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `6c0fefadbc69b9bb9371953979a07a38024dc18cb648266d81168f15d8e9e4fb`
    
    ```text
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
    ```

<a id="source-d63c9e57bcf862b0"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:509"
    `src/libcamera/pipeline_handler.cpp:509`에서 시작하는 발췌입니다. 종료 줄은 530이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `b2d2d134eaa639300cae5e7660d8453da545646bcc100bf640a981fa1371899d`
    
    ```text
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
    ```

<a id="source-ce717689071a887f"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:489"
    `src/libcamera/pipeline_handler.cpp:489`에서 시작하는 발췌입니다. 종료 줄은 489이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `6f7b414922ac8aa5b1145605d838f7188794abfdb44ae70d5272c3290753a50d`
    
    ```text
    data->queuedRequests_.push_back(request);
    ```

<a id="source-a8f47a79aca791ea"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:491"
    `src/libcamera/pipeline_handler.cpp:491`에서 시작하는 발췌입니다. 종료 줄은 491이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `852f648a05b063e1893e4b06b763725a1c14963c9f76c4a5b38eacf57852f05f`
    
    ```text
    request->_d()->sequence_ = data->requestSequence_++;
    ```

<a id="source-3ad79b52195fbc58"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:475"
    `src/libcamera/pipeline_handler.cpp:475`에서 시작하는 발췌입니다. 종료 줄은 475이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `1814c6100eba91f737fab4e000863c03e533260a921598e99fc69298b94f5ddb`
    
    ```text
    data->waitingRequests_.push(request);
    ```

<a id="source-819fe99ec52b734f"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:513"
    `src/libcamera/pipeline_handler.cpp:513`에서 시작하는 발췌입니다. 종료 줄은 514이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `0e91fc5bcfd16b461ea572e903ca063877d267a641ad5e6018b4b13d89723143`
    
    ```text
    if (data->queuedRequests_.size() == maxQueuedRequestsDevice_)
    			break;
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

<a id="source-f389c6ca68ade3da"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:547"
    `src/libcamera/pipeline_handler.cpp:547`에서 시작하는 발췌입니다. 종료 줄은 571이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `ef4ebb9cfbf4b1330b1023d5fa7a790ab8fb13be2793adb41c2e41f01cbf107a`
    
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
    ```

<a id="source-236c920e906cb6fd"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:571"
    `src/libcamera/pipeline_handler.cpp:571`에서 시작하는 발췌입니다. 종료 줄은 607이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `6ad80c6800e8b980c2a6146d7dcc5648de9db2b0ca408711a896c4e46a624684`
    
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
    
    /**
     * \brief Cancel request and signal its completion
    ```

<a id="source-b6dd86e931d905ed"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:584"
    `src/libcamera/pipeline_handler.cpp:584`에서 시작하는 발췌입니다. 종료 줄은 613이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `1c316a2c8c85330805c7dd48fd785dbda88c6cc8e60e9ff0b63039b0205c5577`
    
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
    
    /**
     * \brief Cancel request and signal its completion
     * \param[in] request The request to cancel
     *
     * This function cancels and completes the request. The same rules as for
     * completeRequest() apply.
     */
    void PipelineHandler::cancelRequest(Request *request)
    ```

<a id="source-27cb6869fd89d13d"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:607"
    `src/libcamera/pipeline_handler.cpp:607`에서 시작하는 발췌입니다. 종료 줄은 620이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `1fa9cc6547bd09cc36ec17572eec6ed2a69b261e1d9c9e5bd9cf58e24edd7d18`
    
    ```text
    \brief Cancel request and signal its completion
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

<a id="source-16187edaf24c09f5"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:578"
    `src/libcamera/pipeline_handler.cpp:578`에서 시작하는 발췌입니다. 종료 줄은 580이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `559a88834ae3bb13ac9f2d1844e5b87f1d863fd91b1c8ed252704bf1974adac6`
    
    ```text
    This function ensures that requests will be returned to the application in
     * submission order, the pipeline handler may call it on any complete request
     * without any ordering constraint.
    ```

<a id="source-eefd1bbecb1aad0a"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:359"
    `src/libcamera/pipeline_handler.cpp:359`에서 시작하는 발췌입니다. 종료 줄은 414이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `108b1bea5a8314ba57213d15c1e3ba01abe2b3f8a9e0e1e1281864b5492c7304`
    
    ```text
    \brief Stop capturing from all running streams and cancel pending requests
     * \param[in] camera The camera to stop
     *
     * This function stops capturing and processing requests immediately. All
     * pending requests are cancelled and complete immediately in an error state.
     *
     * \context This function is called from the CameraManager thread.
     */
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
    
    /**
     * \fn PipelineHandler::stopDevice()
     * \brief Stop capturing from all running streams
     * \param[in] camera The camera to stop
     *
     * This function stops capturing and processing requests immediately. All
     * pending requests are cancelled and complete immediately in an error state.
     */
    
    /**
     * \brief Determine if the camera has any requests pending
    ```


<!-- sdd:class-diagram -->
## 클래스 관계

화살표의 글자는 추출한 관계를 나타내며, 점선은 상속입니다. 화살표는 참조 대상 또는 기반 클래스를 향합니다. 호출 순서를 뜻하지 않습니다.

```mermaid
flowchart LR
  c0["Object"]:::context
  c1["PipelineHandler"]
  c2["PipelineHandlerFactory"]
  c3["PipelineHandlerFactoryBase"]
  c4["PipelineHandlerIPU3"]
  c5["PipelineHandlerIPU3::IPU3PipeModes"]
  c6["PipelineHandlerISI"]
  c7["PipelineHandlerISI::Pipe"]
  c8["PipelineHandlerMaliC55"]
  c9["PipelineHandlerMaliC55::(unnamed enum at src/libcamera/pipeline/mali-c55/mali-c55.cpp:712:2)"]
  c10["PipelineHandlerMaliC55::MaliC55Pipe"]
  c11["PipelineHandlerPiSP"]
  c12["PipelineHandlerRkISP1"]
  c13["PipelineHandlerUVC"]
  c14["PipelineHandlerVc4"]
  c15["PipelineHandlerVimc"]
  c16["PipelineHandlerVirtual"]
  c17["RPi::PipelineHandlerBase"]:::context
  c1 -.->|상속| c0
  c2 -.->|상속| c3
  c4 -.->|상속| c1
  c6 -.->|상속| c1
  c6 -->|필드 참조| c7
  c8 -.->|상속| c1
  c8 -->|필드 참조| c10
  c11 -.->|상속| c17
  c12 -.->|상속| c1
  c13 -.->|상속| c1
  c14 -.->|상속| c17
  c15 -.->|상속| c1
  c16 -.->|상속| c1
  classDef context fill:#fafafa,stroke:#aaa,stroke-dasharray:4 3,color:#555
```
<!-- /sdd:class-diagram -->



## 관련 클래스

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::PipelineHandler` | `include/libcamera/internal/pipeline_handler.h:34` | `libcamera::Object` | Create and manage cameras based on a set of media devices |
| `libcamera::PipelineHandlerFactory` | `include/libcamera/internal/pipeline_handler.h:144` | `libcamera::PipelineHandlerFactoryBase` | Registration of PipelineHandler classes and creation of instances |
| `libcamera::PipelineHandlerFactoryBase` | `include/libcamera/internal/pipeline_handler.h:121` | – | Base class for pipeline handler factories |
| `libcamera::PipelineHandlerIPU3` | `src/libcamera/pipeline/ipu3/ipu3.cpp:124` | `libcamera::PipelineHandler` | 확인 필요 |
| `libcamera::PipelineHandlerIPU3::IPU3PipeModes` | `src/libcamera/pipeline/ipu3/ipu3.cpp:130` | – | 확인 필요 |
| `libcamera::PipelineHandlerISI` | `src/libcamera/pipeline/imx8-isi/imx8-isi.cpp:102` | `libcamera::PipelineHandler` | 확인 필요 |
| `libcamera::PipelineHandlerISI::Pipe` | `src/libcamera/pipeline/imx8-isi/imx8-isi.cpp:129` | – | 확인 필요 |
| `libcamera::PipelineHandlerMaliC55` | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:676` | `libcamera::PipelineHandler` | 확인 필요 |
| `libcamera::PipelineHandlerMaliC55::(unnamed enum at src/libcamera/pipeline/mali-c55/mali-c55.cpp:712:2)` | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:712` | – | 확인 필요 |
| `libcamera::PipelineHandlerMaliC55::MaliC55Pipe` | `src/libcamera/pipeline/mali-c55/mali-c55.cpp:705` | – | 확인 필요 |
| `libcamera::PipelineHandlerPiSP` | `src/libcamera/pipeline/rpi/pisp/pisp.cpp:852` | `libcamera::RPi::PipelineHandlerBase` | 확인 필요 |
| `libcamera::PipelineHandlerRkISP1` | `src/libcamera/pipeline/rkisp1/rkisp1.cpp:185` | `libcamera::PipelineHandler` | 확인 필요 |
| `libcamera::PipelineHandlerUVC` | `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:81` | `libcamera::PipelineHandler` | 확인 필요 |
| `libcamera::PipelineHandlerVc4` | `src/libcamera/pipeline/rpi/vc4/vc4.cpp:141` | `libcamera::RPi::PipelineHandlerBase` | 확인 필요 |
| `libcamera::PipelineHandlerVimc` | `src/libcamera/pipeline/vimc/vimc.cpp:84` | `libcamera::PipelineHandler` | 확인 필요 |
| `libcamera::PipelineHandlerVirtual` | `src/libcamera/pipeline/virtual/virtual.cpp:81` | `libcamera::PipelineHandler` | 확인 필요 |

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `include/libcamera/internal/pipeline_handler.h`, `src/libcamera/pipeline/imx8-isi/imx8-isi.cpp`, `src/libcamera/pipeline/ipu3/ipu3.cpp`, `src/libcamera/pipeline/mali-c55/mali-c55.cpp`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp`, `src/libcamera/pipeline/rpi/pisp/pisp.cpp`, `src/libcamera/pipeline/rpi/vc4/vc4.cpp`, `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp`, `src/libcamera/pipeline/vimc/vimc.cpp`, `src/libcamera/pipeline/virtual/virtual.cpp`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/request.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `2c4b67c079`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-26 · 사람 검토 전

다음 단계: [시스템 개요](overview.md)
