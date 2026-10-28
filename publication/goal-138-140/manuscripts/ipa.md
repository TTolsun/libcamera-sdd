---
generated_at: 2026-10-28T23:09:45+00:00
source_commit: e117198c015057761bb0bbaa85f963c41ce412d7
status: ok
section: ipa
generation_method: facts-and-llm
evidence_fingerprint: f301dc871d560dd4fd5ab48566ec18735205164228dadfbca051db6f06e271e5
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "f301dc871d560dd4fd5ab48566ec18735205164228dadfbca051db6f06e271e5", "answers": {"selection": [{"text": "`IPAManager::IPAManager`는 사용자 지정 `ipa.module_paths`를 먼저 살펴보고, 빈 경로는 건너뛰며 나머지 경로마다 `addDir()`를 호출합니다. 이어서 `utils::libcameraBuildPath()`가 빈 문자열이 아니면 그 경로에 `src/ipa`를 붙여 최대 깊이 2로 `addDir()`를 호출합니다. 마지막으로 설치된 시스템 경로인 `IPA_MODULE_DIR`에 대해 `addDir()`를 호출합니다.", "evidence": ["modules"], "covers": ["selection"], "kind": "behavior", "quote": "/* User-specified paths take precedence. */\n\tconst auto modulePaths =\n\t\tconfiguration.listOption({ \"ipa\", \"module_paths\" })\n\t\t\t.value_or(utils::defopt);\n\tfor (const auto &dir : modulePaths) {\n\t\tif (dir.empty())\n\t\t\tcontinue;", "part_id": "search-paths"}, {"text": "`IPAModule::match`는 `info_.pipelineVersion`이 `minVersion` 이상이고 `maxVersion` 이하이며, `info_.name`과 `name`이 일치할 때 `true`를 반환합니다. 이 조건 중 하나라도 만족하지 않으면 `false`를 반환합니다.", "evidence": ["match"], "covers": ["selection"], "kind": "behavior", "quote": "\\brief Verify if the IPA module matches a given name\n * \\param[in] name The IPA module name\n * \\param[in] minVersion Minimum acceptable version of IPA module\n * \\param[in] maxVersion Maximum acceptable version of IPA module\n *\n * This function checks if this IPA module matches the requested \\a name\n * and the input version range.\n *\n * \\return True if the IPA module matches, or false otherwise\n */\nbool IPAModule::match(const char *name, uint32_t minVersion,\n\t\t      uint32_t maxVersion) const\n{\n\treturn info_.pipelineVersion >= minVersion &&\n\t       info_.pipelineVersion <= maxVersion &&\n\t       !strcmp(info_.name, name);\n}", "part_id": "module-match"}, {"text": "`createIPA`는 먼저 `module(name, minVersion, maxVersion)`으로 모듈을 찾고, 모듈이 없으면 `nullptr`을 반환합니다. 모듈이 있으면 `isSignatureValid(m)`이 참일 때 `T::Threaded` 프록시를, 거짓일 때 `T::Isolated` 프록시를 생성합니다. 생성한 프록시의 `isValid()`가 거짓이면 오류를 기록하고 `nullptr`을 반환하며, 참이면 프록시를 반환합니다.", "evidence": ["selection"], "covers": ["selection"], "kind": "behavior", "quote": "auto proxy = [&]() -> std::unique_ptr<T> {\n\t\t\tif (isSignatureValid(m))\n\t\t\t\treturn std::make_unique<typename T::Threaded>(m, cm_);\n\t\t\telse\n\t\t\t\treturn std::make_unique<typename T::Isolated>(m, cm_);\n\t\t}();", "part_id": "proxy-selection"}, {"text": "`IPAManager::isSignatureValid`는 `HAVE_IPA_PUBKEY`가 활성화되지 않으면 `false`를 반환합니다. 활성화된 경우 `forceIsolation_`이 참이면 `false`를 반환하고, 그렇지 않으면 IPA 모듈 파일을 읽기 전용으로 엽니다. 파일을 열지 못하거나 매핑한 데이터가 비어 있으면 `false`를 반환합니다. 그 밖에는 `pubKey_.verify(data, ipa->signature())`의 결과를 기록하고 그 결과를 반환합니다.", "evidence": ["signature"], "covers": ["selection"], "kind": "behavior", "quote": "bool IPAManager::isSignatureValid([[maybe_unused]] IPAModule *ipa) const\n{\n#if HAVE_IPA_PUBKEY\n\tif (forceIsolation_) {\n\t\tLOG(IPAManager, Debug)\n\t\t\t<< \"Isolation of IPA module \" << ipa->path()\n\t\t\t<< \" forced through configuration\";\n\t\treturn false;\n\t}", "part_id": "signature"}], "execution": [{"text": "Threaded `init` 템플릿은 생성된 매개변수를 전달하여 `ipa_->init()`을 직접 호출합니다. 반환형이 `void`가 아니면 호출 결과를 `_ret`에 저장한 뒤 반환하고, `void`이면 값을 지정하지 않고 반환합니다.", "evidence": ["init-branch"], "covers": ["execution"], "kind": "behavior", "quote": "{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);", "part_id": "init"}, {"text": "`init` 분기는 IPA의 `init` 메서드를 호출한 뒤 `proxy_.moveToThread`에 `thread_` 객체의 주소인 `&thread_`를 전달합니다.", "evidence": ["init-branch"], "covers": ["execution"], "kind": "behavior", "quote": "proxy_.moveToThread(&thread_);", "part_id": "init-move"}, {"text": "Threaded `start` 템플릿 분기는 먼저 `state_`를 `ProxyRunning`으로 설정하고 `thread_.start()`를 호출합니다. 이어서 `proxy_.invokeMethod()`로 `ThreadProxy::start`를 `ConnectionTypeBlocking` 연결 유형과 템플릿의 메서드 매개변수로 호출하고 그 반환값을 반환합니다.", "evidence": ["start-branch"], "covers": ["execution"], "kind": "behavior", "quote": "{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();", "part_id": "start"}, {"text": "생성된 `Threaded` 메서드는 `init`, `start`, `stop`이 아닌 일반 동기 메서드 분기에서 `ipa_`의 같은 이름 메서드를 전달받은 매개변수로 직접 호출하고 그 반환값을 반환합니다.", "evidence": ["dispatch"], "covers": ["execution"], "kind": "behavior", "quote": "return proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}", "part_id": "sync"}, {"text": "비동기 메서드 분기에서 `ASSERT` 매크로는 `state_ == ProxyRunning` 식을 검사합니다.", "evidence": ["async-assert"], "covers": ["execution"], "kind": "behavior", "quote": "ASSERT(state_ == ProxyRunning);", "part_id": "async"}, {"text": "Threaded 비동기 분기에서 `proxy_.invokeMethod`는 `ThreadProxy` 메서드를 전달할 때 연결 유형으로 `ConnectionTypeQueued`를 사용합니다.", "evidence": ["async-branch"], "covers": ["execution"], "kind": "behavior", "quote": "{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}", "part_id": "async-dispatch"}, {"text": "`{{proxy_name}}Threaded` 생성자는 `ipam->load()`를 호출합니다. 호출 결과가 거짓이면 생성자는 즉시 반환합니다.", "evidence": ["ctor-load"], "covers": ["execution"], "kind": "behavior", "quote": "if (!ipam->load())\n\t\treturn;", "part_id": "constructor"}, {"text": "`{{proxy_name}}Threaded` 생성자는 `ipam->load()`가 성공하면 `ipam->createInterface()`를 호출합니다. 반환된 포인터가 없으면 `ipam->path()`를 포함한 오류를 기록하고 생성자에서 반환합니다.", "evidence": ["ctor-interface"], "covers": ["execution"], "kind": "behavior", "quote": "IPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;", "part_id": "constructor-interface"}, {"text": "생성된 `{{proxy_name}}Threaded` 생성자는 `ipam->load()`가 실패하거나 `ipam->createInterface()`가 null을 반환하면 연결 전에 반환합니다. 그 외에는 `ipa_`를 설정하고 `proxy_.setIPA(ipa_.get())`를 호출한 뒤, 각 IPA 이벤트의 `connect`에 수신 객체 `this`와 해당 이벤트의 `{{proxy_name}}Threaded::{{method.mojom_name}}Handler` 메서드를 전달합니다. 연결 코드는 템플릿의 `interface_event.methods` 항목마다 생성되며, 그 뒤 생성자는 `valid_`를 `true`로 설정합니다.", "evidence": ["ctor-events"], "covers": ["execution"], "kind": "behavior", "quote": "ipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);", "part_id": "constructor-events"}, {"text": "`{{proxy_name}}Isolated` 생성자는 `resolvePath(\"{{module_name}}_ipa_proxy\")`로 worker 경로를 구하고, 경로가 비어 있으면 오류를 기록한 뒤 반환합니다. 경로가 있으면 IPA 모듈 경로와 worker 경로로 `IPCPipeUnixSocket`을 생성하고, 연결되지 않았다면 오류를 기록한 뒤 반환합니다. 연결되면 `recv`를 `recvMessage`에 연결하고 IPC 객체를 `ipc_`로 이동한 뒤 `valid_`를 `true`로 설정합니다.", "evidence": ["isolated"], "covers": ["execution"], "kind": "behavior", "quote": "auto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}", "part_id": "isolated"}, {"text": "`{{proxy_name}}Isolated` 생성자는 워커 경로가 비어 있거나 IPC가 연결되지 않으면 호출 전에 반환합니다. 그 외에는 `ipc`의 `recv`를 현재 객체 `this`의 `{{proxy_name}}Isolated::recvMessage` 콜백에 `connect`로 연결합니다.", "evidence": ["isolated-valid"], "covers": ["execution"], "kind": "behavior", "quote": "ipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);", "part_id": "isolated-valid"}, {"text": "`{{proxy_name}}Isolated::{{proxy_name}}Isolated()`의 대입문은 `ipc_`를 대상으로 하고 우변에 `std::move(ipc)`를 사용합니다.", "evidence": ["isolated-store"], "covers": ["execution"], "kind": "behavior", "quote": "ipc_ = std::move(ipc);\n\tvalid_ = true;", "part_id": "isolated-store"}, {"text": "`{{proxy_name}}Isolated` 생성자는 이 코드 지점에서 `valid_`에 `true`를 대입합니다.", "evidence": ["isolated-ready"], "covers": ["execution"], "kind": "behavior", "quote": "valid_ = true;", "part_id": "isolated-ready"}, {"text": "`IPAProxy::resolvePath`는 먼저 `execPaths_`를 순서대로 확인하고 빈 디렉터리를 건너뛰며, 실행 권한이 있는 첫 번째 worker 경로를 반환합니다. 그다음 `utils::libcameraBuildPath()`가 비어 있지 않으면 해당 빌드 경로의 `src/libcamera/proxy/worker`를 확인하고, 비어 있으면 설치 디렉터리 `IPA_PROXY_DIR`을 확인합니다. 선택한 디렉터리에서 실행 권한이 있는 worker를 찾으면 그 경로를 반환하고, 찾지 못하면 빈 문자열을 반환합니다.", "evidence": ["worker-path"], "covers": ["execution"], "kind": "behavior", "quote": "/* Try paths from the configuration first. */\n\tfor (const auto &dir : execPaths_) {\n\t\tif (dir.empty())\n\t\t\tcontinue;", "part_id": "worker"}, {"text": "`IPCPipeUnixSocket::sendSync`는 입력 페이로드, 응답 저장 위치와 헤더의 쿠키로 `call`을 호출하고, 오류가 반환되면 그 값을 반환합니다. `call`은 쿠키와 응답 저장 위치, 완료 상태를 `callData_`에 삽입하려고 하며 삽입 성공 여부는 확인하지 않습니다. 메시지 전송에 실패하면 해당 반복자의 항목을 지우고 오류를 반환하며, 성공하면 2000ms 타이머를 시작하고 완료 상태가 될 때까지 현재 스레드의 이벤트를 처리하다가 시간이 끝나면 항목을 지우고 `-ETIMEDOUT`을 반환합니다. `readyRead`는 수신에 성공하고 헤더 크기 이상의 데이터에서 일치하는 쿠키를 찾으면 페이로드를 해당 응답 위치에 옮기고 완료로 표시하며, `call`은 완료 후 항목을 지우고 0을 반환하고 `sendSync`는 `out`이 있으면 응답으로 `IPCMessage`를 만들어 저장한 뒤 0을 반환합니다.", "evidence": ["ipc"], "covers": ["execution"], "kind": "behavior", "quote": "int ret = call(in.payload(), &response, in.header().cookie);\n\tif (ret) {\n\t\tLOG(IPCPipe, Error) << \"Failed to call sync\";\n\t\treturn ret;\n\t}", "part_id": "ipc"}, {"text": "`IPCPipeUnixSocket::sendAsync`는 `socket_->send`에 `data.payload()`를 전달합니다. 반환값이 0이 아니면 오류를 기록하고 그 값을 반환합니다. 반환값이 0이면 0을 반환합니다.", "evidence": ["send-async"], "covers": ["execution"], "kind": "behavior", "quote": "int IPCPipeUnixSocket::sendAsync(const IPCMessage &data)\n{\n\tint ret = socket_->send(data.payload());\n\tif (ret) {\n\t\tLOG(IPCPipe, Error) << \"Failed to call async\";\n\t\treturn ret;\n\t}", "part_id": "ipc-async"}], "interface": [{"text": "`IPAIPU3Interface`의 `[async]` 메서드 `queueRequest`는 프레임 번호 `frame`과 요청 제어 값 `controls`를 인자로 받습니다. `computeParams`는 `frame`과 `bufferId`를 받고, `processStats`는 `frame`, `frameTimestamp`, `bufferId`, `sensorControls`를 받습니다.", "evidence": ["ipu3-api"], "covers": ["interface"], "kind": "behavior", "quote": "[async] queueRequest(uint32 frame, libcamera.ControlList controls);\n\t[async] computeParams(uint32 frame, uint32 bufferId);\n\t[async] processStats(uint32 frame, int64 frameTimestamp,\n\t\t\t     uint32 bufferId, libcamera.ControlList sensorControls);\n};"}, {"text": "`IPAIPU3EventInterface`에는 `paramsComputed(frame)`과 `metadataReady(frame, metadata)`가 선언되어 있습니다. `setSensorControls`는 `frame`, `sensorControls`, `lensControls`를 인자로 받습니다.", "evidence": ["ipu3-api"], "covers": ["interface"], "kind": "behavior", "quote": "interface IPAIPU3EventInterface {\n\tsetSensorControls(uint32 frame, libcamera.ControlList sensorControls,\n\t\t\t  libcamera.ControlList lensControls);\n\tparamsComputed(uint32 frame);\n\tmetadataReady(uint32 frame, libcamera.ControlList metadata);\n};"}, {"text": "`IPARkISP1Interface`의 `[async]` 메서드 `queueRequest`는 프레임 번호 `frame`과 요청 제어 값 `reqControls`를 인자로 받습니다. `computeParams`는 `frame`과 `bufferId`를 받고, `processStats`는 `frame`, `bufferId`, `sensorControls`를 받습니다.", "evidence": ["rkisp1-api"], "covers": ["interface"], "kind": "behavior", "quote": "[async] queueRequest(uint32 frame, libcamera.ControlList reqControls);\n\t[async] computeParams(uint32 frame, uint32 bufferId);\n\t[async] processStats(uint32 frame, uint32 bufferId,\n\t\t\t     libcamera.ControlList sensorControls);\n};"}, {"text": "`IPARkISP1EventInterface`에는 `paramsComputed(frame, bytesused)`와 `metadataReady(frame, metadata)`가 선언되어 있습니다. `setSensorControls`는 `frame`과 `sensorControls`를 인자로 받습니다.", "evidence": ["rkisp1-api"], "covers": ["interface"], "kind": "behavior", "quote": "interface IPARkISP1EventInterface {\n\tparamsComputed(uint32 frame, uint32 bytesused);\n\tsetSensorControls(uint32 frame, libcamera.ControlList sensorControls);\n\tmetadataReady(uint32 frame, libcamera.ControlList metadata);\n};"}], "lifetime": [{"text": "호출자는 유효한 모듈에서 `IPAModule::load()`를 한 번 성공시킨 뒤 필요한 수만큼 `createInterface()`를 호출할 수 있습니다. 유효하지 않거나 아직 로드되지 않은 모듈에서 `createInterface()`를 호출해서는 안 됩니다. `load()`는 유효하지 않으면 `false`, 이미 로드되었으면 `true`를 반환하며, `createInterface()`는 유효하지 않거나 로드되지 않았으면 `nullptr`를 반환하고 그 외에는 `ipaCreate_()`를 호출합니다.", "evidence": ["load"], "covers": ["lifetime"], "kind": "behavior", "quote": "\\brief Load the IPA implementation factory from the shared object\n *\n * The IPA module shared object implements an IPAInterface object to be used\n * by pipeline handlers. This function loads the factory function from the\n * shared object. Later, createInterface() can be called to instantiate the\n * IPAInterface.\n *\n * This function only needs to be called successfully once, after which\n * createInterface() can be called as many times as IPAInterface instances are\n * needed.\n *\n * Calling this function on an invalid module (as returned by isValid()) is\n * an error.\n *\n * \\return True if load was successful, or already loaded, and false otherwise\n */\nbool IPAModule::load()\n{\n\tif (!valid_)\n\t\treturn false;"}, {"text": "`IPAModule::load()`는 `dlopen()`에 실패하면 `false`를 반환합니다. `ipaCreate` 심볼을 찾지 못하면 핸들을 닫고 `nullptr`로 설정한 뒤 `false`를 반환합니다. 성공하면 팩토리를 저장하고 `loaded_`를 `true`로 설정한 뒤 `true`를 반환합니다.", "evidence": ["load"], "covers": ["lifetime"], "kind": "behavior", "quote": "void *symbol = dlsym(dlHandle_, \"ipaCreate\");\n\tif (!symbol) {\n\t\tLOG(IPAModule, Error)\n\t\t\t<< \"Failed to load ipaCreate() from IPA module shared object: \"\n\t\t\t<< dlerror();\n\t\tdlclose(dlHandle_);\n\t\tdlHandle_ = nullptr;\n\t\treturn false;\n\t}"}, {"text": "`Threaded` 프록시 생성자는 `load()`가 실패하거나 `createInterface()`가 `nullptr`를 반환하면 중단합니다. 인터페이스 생성에 성공하면 이를 `unique_ptr`에 보유하고 `proxy_`에 설정한 뒤 이벤트 핸들러를 연결하고 `valid_`를 `true`로 설정합니다.", "evidence": ["threaded"], "covers": ["lifetime"], "kind": "behavior", "quote": "IPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;\n\t}"}, {"text": "`Threaded::init()`은 IPA의 `init`을 호출한 뒤 `proxy_`를 `thread_`로 옮기고 반환값이 있으면 반환합니다. `start()`는 상태를 `ProxyRunning`으로 설정하고 스레드를 시작한 뒤 `ThreadProxy::start`를 블로킹 방식으로 호출합니다. 비동기 메서드는 상태가 `ProxyRunning`인지 단언한 뒤 `ThreadProxy` 메서드를 큐에 넣어 호출합니다.", "evidence": ["threaded"], "covers": ["lifetime"], "kind": "behavior", "quote": "return proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}"}, {"text": "`Threaded::stop()`은 상태가 `ProxyStopping`이 아님을 단언하고, `ProxyRunning`이 아니면 반환합니다. 실행 중이면 상태를 `ProxyStopping`으로 바꾸고 `ThreadProxy::stop`을 블로킹 방식으로 호출한 뒤 스레드에 종료를 요청하고 기다립니다. 이어서 현재 스레드에서 이 프록시의 `InvokeMessage` 메시지를 처리하고 상태를 `ProxyStopped`로 설정합니다.", "evidence": ["thread-stop", "threaded"], "covers": ["lifetime"], "kind": "behavior", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;"}, {"text": "`Isolated` 프록시 생성자는 워커 경로를 구하지 못하거나 IPC 연결이 없으면 중단합니다. 연결되면 수신 신호를 `recvMessage`에 연결하고 IPC 객체의 소유권을 `ipc_`로 옮긴 뒤 `valid_`를 `true`로 설정합니다. 소멸자는 `ipc_`가 있으면 증가하는 시퀀스 번호를 담은 `Exit` 메시지를 비동기로 보냅니다.", "evidence": ["isolated"], "covers": ["lifetime"], "kind": "behavior", "quote": "{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}"}], "errors": [{"text": "`IPAModule::load()`는 `valid_`가 거짓이면 `false`를 반환하고, 이미 `loaded_`가 참이면 `true`를 반환합니다. 그렇지 않으면 `dlopen`으로 공유 객체를 열고, 실패하면 오류를 기록한 뒤 `false`를 반환합니다. 이어서 `dlsym`으로 `ipaCreate`를 찾으며, 실패하면 오류를 기록하고 `dlclose`를 호출한 뒤 `dlHandle_`을 `nullptr`로 설정하고 `false`를 반환합니다. 심볼을 찾으면 이를 `ipaCreate_`에 저장하고 `loaded_`를 참으로 설정한 뒤 `true`를 반환합니다.", "evidence": ["load"], "covers": ["errors"], "kind": "behavior", "quote": "void *symbol = dlsym(dlHandle_, \"ipaCreate\");\n\tif (!symbol) {\n\t\tLOG(IPAModule, Error)\n\t\t\t<< \"Failed to load ipaCreate() from IPA module shared object: \"\n\t\t\t<< dlerror();\n\t\tdlclose(dlHandle_);\n\t\tdlHandle_ = nullptr;\n\t\treturn false;\n\t}", "part_id": "module-load"}, {"text": "`IPAModule::createInterface()`는 모듈이 유효하지 않거나 로드되지 않았다면 `nullptr`을 반환합니다. 두 조건을 모두 통과하면 `ipaCreate_()`를 호출하고 그 반환값을 반환합니다.", "evidence": ["load"], "covers": ["errors"], "kind": "behavior", "quote": "/**\n * \\brief Instantiate an IPA interface\n *\n * After loading the IPA module with load(), this function creates an instance\n * of the IPA module interface.\n *\n * Calling this function on a module that has not yet been loaded, or an\n * invalid module (as returned by load() and isValid(), respectively) is\n * an error.\n *\n * \\return The IPA interface on success, or nullptr on error\n */\nIPAInterface *IPAModule::createInterface()\n{\n\tif (!valid_ || !loaded_)\n\t\treturn nullptr;", "part_id": "interface-create"}, {"text": "`IPCPipeUnixSocket::sendSync`는 입력 메시지의 페이로드와 쿠키, 응답 저장 위치를 `call`에 전달하고 반환값이 0이 아니면 오류를 기록한 뒤 그 값을 반환합니다. `call`이 성공하면 `out`이 null이 아닐 때 응답으로 만든 `IPCMessage`를 `*out`에 대입하고 0을 반환합니다.", "evidence": ["ipc"], "covers": ["errors"], "kind": "behavior", "quote": "int ret = call(in.payload(), &response, in.header().cookie);\n\tif (ret) {\n\t\tLOG(IPCPipe, Error) << \"Failed to call sync\";\n\t\treturn ret;\n\t}", "part_id": "sync-result"}, {"text": "`IPCPipeUnixSocket::call`은 `cookie`와 응답 포인터, 완료 상태 `false`로 `callData_`에 항목을 삽입하고 결과의 반복자 `iter`를 보관합니다. 소켓의 `send`에는 반복자가 아닌 `message`를 전달합니다. 송신 결과가 0이 아니면 `iter`가 가리키는 항목을 `erase`로 지우고 송신 결과를 반환합니다.", "evidence": ["ipc"], "covers": ["errors"], "kind": "behavior", "quote": "ret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}", "part_id": "sync-send"}, {"text": "`IPCPipeUnixSocket::call`은 응답 항목을 삽입한 결과의 반복자 `iter`를 사용하며, 타이머를 `2000ms`로 시작한 뒤 `iter->second.done`이 참이 될 때까지 이벤트를 처리합니다. 대기 중 타이머가 실행 중이 아니면 `callData_.erase(iter)`로 항목을 지우고 `-ETIMEDOUT`을 반환합니다. 완료되면 같은 반복자로 항목을 지우고 `0`을 반환합니다.", "evidence": ["ipc"], "covers": ["errors"], "kind": "behavior", "quote": "/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}", "part_id": "sync-timeout"}]}, "topic_inputs": {"selection": "02f51245890cd057b2965c9836287585230c3167b724547d61deaf4b1750b4db", "execution": "2ea2fbe9892c44fa66ae356d19a5ada2603321a90444851ca039897ed1dcddba", "interface": "536c441a9ef12d04f3c1fc15745b2330f6aa842164afaf8c8dde618e33b84f2e", "lifetime": "7518a1cd36c8e249e15bc96ed2a0a040030e8caf29945b22cada398974883bbc", "errors": "c45d8a244714f4507606bb895b13037b8f0237e1fbebe3b66946c825e592faf3"}, "reused_topics": ["selection", "execution", "interface", "lifetime", "errors"], "replayed_units": [], "generated_topics": [], "topic_agents": {"selection": "cli/codex/gpt-6.1-terra", "execution": "cli/codex/gpt-6.1-terra", "interface": "cli/codex/gpt-6.1-terra", "lifetime": "cli/codex/gpt-6.1-terra", "errors": "cli/codex/gpt-6.1-terra"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "e0c429a5c80a01c34563ce00a616df89d8f75c735f8669bcbd1f75d84cce82a6", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "d4af3d834d8b1c99a6c9311612712a64112c30fa4621b375904d172f361285b8", "design_contracts": "b293a0012d1fcb6340fcaf94d481cf900212686978bc96fb118a0cdaddf3c091", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "65c405dc11cd8c43e2bce26ffbd96a47f37a784df59a4969be589ed8318f7be0", "answer_contracts": "1e0d24e0cf26ded53ecec2e5a6fbc51836bac6e17530318a9fa7cffaa936c00b", "design_response": "ce93f02b72371ed40f1b1124e78cef512baea31aa2df988db0c689f8169f783c", "design_validation": "608d2eed51e4ad5d5693fbc9b7d669ae1ba8e503f6736b62ea1ca068ce706556"}, "validation_model": "5ddbcbf91a6b516c4f71596d64b6286295bfd0cac771a7ca749ca78e25a2d752", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "f8fd5a3d8041c23fc68b93ff32b8727e98393383b5099032eb00ad0013e7611c"}, "reuse_lineage": {"source_commit": "e117198c015057761bb0bbaa85f963c41ce412d7", "body_sha256": "bbd4b670e4a861642f53b90d181dfd99164b975bcba65113e0b867c4b997f8cf", "topics": ["selection", "execution", "interface", "lifetime", "errors"], "validation": "current source, contract and editorial checks; human review pending"}, "body_sha256": "bbd4b670e4a861642f53b90d181dfd99164b975bcba65113e0b867c4b997f8cf"}
---

# IPA 관리와 구현 진입점

**IPA 모듈 선택, 스레드·프로세스 경계와 요청·결과 인터페이스를 구현 근거로 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 모듈 탐색과 격리 조건의 조건과 근거를 대조하세요. | [모듈 탐색과 격리 조건](#모듈-탐색과-격리-조건) |
| 스레드와 프로세스 경계의 조건과 근거를 대조하세요. | [스레드와 프로세스 경계](#스레드와-프로세스-경계) |
| 프레임 입력과 결과 인터페이스의 조건과 근거를 대조하세요. | [프레임 입력과 결과 인터페이스](#프레임-입력과-결과-인터페이스) |
| IPA 객체와 종료 순서의 조건과 근거를 대조하세요. | [IPA 객체와 종료 순서](#ipa-객체와-종료-순서) |
| 생성과 IPC 실패의 조건과 근거를 대조하세요. | [생성과 IPC 실패](#생성과-ipc-실패) |
| <a id="보정-전-튜닝-파일"></a>보정 전 튜닝 파일의 조건과 근거를 대조하세요. | [IPA 튜닝과 소프트웨어 ISP](ipa-algorithms.md#보정-전-튜닝-파일) |
| <a id="소프트웨어-isp-입력-버퍼의-텍스처-형식"></a>소프트웨어 ISP 입력 버퍼의 텍스처 형식의 조건과 근거를 대조하세요. | [IPA 튜닝과 소프트웨어 ISP](ipa-algorithms.md#소프트웨어-isp-입력-버퍼의-텍스처-형식) |
| <a id="소프트웨어-isp-셰이더의-렌즈-음영-보정"></a>소프트웨어 ISP 셰이더의 렌즈 음영 보정의 조건과 근거를 대조하세요. | [IPA 튜닝과 소프트웨어 ISP](ipa-algorithms.md#소프트웨어-isp-셰이더의-렌즈-음영-보정) |

## 모듈 탐색과 격리 조건

`IPAManager::IPAManager`는 사용자 지정 `ipa.module_paths`를 먼저 살펴보고, 빈 경로는 건너뛰며 나머지 경로마다 `addDir()`를 호출합니다. 이어서 `utils::libcameraBuildPath()`가 빈 문자열이 아니면 그 경로에 `src/ipa`를 붙여 최대 깊이 2로 `addDir()`를 호출합니다. 마지막으로 설치된 시스템 경로인 `IPA_MODULE_DIR`에 대해 `addDir()`를 호출합니다. `src/libcamera/ipa_manager.cpp:107`

<!-- sdd:visual:proxy-selection -->
### IPA 모듈 선택과 실행 경계

모듈 선택, 서명 판정, 프록시 유효성의 분기를 구분하세요. 서명 판정의 구성 조건은 이어지는 설명에서 확인합니다.

```mermaid
flowchart TB
%% sdd:translations {"Isolated 프록시": "Isolated proxy", "Threaded 프록시": "Threaded proxy", "false": "false", "isSignatureValid(m)?": "isSignatureValid(m)?", "nullptr: 생성 실패": "nullptr: creation failed", "true": "true", "생성 후 검사": "Check after construction", "아니오": "No", "예": "Yes", "이름·버전의 모듈이 있는가?": "Module matching name and <br/>version?", "프록시 반환": "Return proxy", "프록시가 유효한가?": "Is the proxy valid?"}
  v_module{"이름·버전의 모듈이 있는가?"}
  v_signature{"isSignatureValid(m)?"}
  v_threaded["Threaded 프록시"]
  v_isolated["Isolated 프록시"]
  v_valid{"프록시가 유효한가?"}
  v_failure["nullptr: 생성 실패"]
  v_success["프록시 반환"]
  v_module -->|"아니오"| v_failure
  v_module -->|"예"| v_signature
  v_signature -->|"true"| v_threaded
  v_signature -->|"false"| v_isolated
  v_threaded -->|"생성 후 검사"| v_valid
  v_isolated -->|"생성 후 검사"| v_valid
  v_valid -->|"아니오"| v_failure
  v_valid -->|"예"| v_success
```

[Mermaid 원문](ipa.proxy-selection.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | 이름·버전의 모듈이 있는가? | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | isSignatureValid(m)? | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | Threaded 프록시 | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | Isolated 프록시 | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | 프록시가 유효한가? | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | nullptr: 생성 실패 | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | 프록시 반환 | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | 아니오 | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | 예 | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | true | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | false | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | 생성 후 검사 | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | 생성 후 검사 | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | 아니오 | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | 예 | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
<!-- /sdd:visual:proxy-selection -->

`IPAModule::match`는 `info_.pipelineVersion`이 `minVersion` 이상이고 `maxVersion` 이하이며, `info_.name`과 `name`이 일치할 때 `true`를 반환합니다. 이 조건 중 하나라도 만족하지 않으면 `false`를 반환합니다. `src/libcamera/ipa_module.cpp:460`

`createIPA`는 먼저 `module(name, minVersion, maxVersion)`으로 모듈을 찾고, 모듈이 없으면 `nullptr`을 반환합니다. 모듈이 있으면 `isSignatureValid(m)`이 참일 때 `T::Threaded` 프록시를, 거짓일 때 `T::Isolated` 프록시를 생성합니다. 생성한 프록시의 `isValid()`가 거짓이면 오류를 기록하고 `nullptr`을 반환하며, 참이면 프록시를 반환합니다. `include/libcamera/internal/ipa_manager.h:35`

`IPAManager::isSignatureValid`는 `HAVE_IPA_PUBKEY`가 활성화되지 않으면 `false`를 반환합니다. 활성화된 경우 `forceIsolation_`이 참이면 `false`를 반환하고, 그렇지 않으면 IPA 모듈 파일을 읽기 전용으로 엽니다. 파일을 열지 못하거나 매핑한 데이터가 비어 있으면 `false`를 반환합니다. 그 밖에는 `pubKey_.verify(data, ipa->signature())`의 결과를 기록하고 그 결과를 반환합니다. `src/libcamera/ipa_manager.cpp:289`

근거 원문: [src/libcamera/ipa_manager.cpp:107](#source-7603cbafe8eef490) · [src/libcamera/ipa_module.cpp:460](#source-6e1525c1fc1aa55e) · [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) · [src/libcamera/ipa_manager.cpp:289](#source-532f8ffa194bd319)

## 스레드와 프로세스 경계

Threaded `init` 템플릿은 생성된 매개변수를 전달하여 `ipa_->init()`을 직접 호출합니다. 반환형이 `void`가 아니면 호출 결과를 `_ret`에 저장한 뒤 반환하고, `void`이면 값을 지정하지 않고 반환합니다. `init` 분기는 IPA의 `init` 메서드를 호출한 뒤 `proxy_.moveToThread`에 `thread_` 객체의 주소인 `&thread_`를 전달합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:82`

<!-- sdd:visual:execution-boundaries -->
### 스레드 호출과 IPC 호출의 경계

Threaded와 Isolated는 대체 경로입니다. 각 API가 동기인지 비동기인지는 인터페이스 선언에 따라 달라집니다.

```mermaid
flowchart TB
%% sdd:translations {"IPC로 worker와 통신": "Communicate with worker <br/>over IPC", "Isolated 프록시": "Isolated proxy", "Threaded 프록시": "Threaded proxy", "is_async 메서드": "is_async methods", "비동기 메서드는 작업 <br/>스레드로 예약": "Queue asynchronous methods <br/>to worker thread", "선언에 따라 sendAsync 또는 <br/>sendSync": "sendAsync or sendSync per <br/>declaration"}
  v_threaded["Threaded 프록시"]
  v_thread["비동기 메서드는 작업 <br/>스레드로 예약"]
  v_isolated["Isolated 프록시"]
  v_ipc["IPC로 worker와 통신"]
  v_threaded -->|"is_async 메서드"| v_thread
  v_isolated -->|"선언에 따라 sendAsync 또는 <br/>sendSync"| v_ipc
```

[Mermaid 원문](ipa.execution-boundaries.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | Threaded 프록시 | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | 비동기 메서드는 작업 스레드로 예약 | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | Isolated 프록시 | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | IPC로 worker와 통신 | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | is_async 메서드 | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | 선언에 따라 sendAsync 또는 sendSync | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
<!-- /sdd:visual:execution-boundaries -->

Threaded `start` 템플릿 분기는 먼저 `state_`를 `ProxyRunning`으로 설정하고 `thread_.start()`를 호출합니다. 이어서 `proxy_.invokeMethod()`로 `ThreadProxy::start`를 `ConnectionTypeBlocking` 연결 유형과 템플릿의 메서드 매개변수로 호출하고 그 반환값을 반환합니다. 생성된 `Threaded` 메서드는 `init`, `start`, `stop`이 아닌 일반 동기 메서드 분기에서 `ipa_`의 같은 이름 메서드를 전달받은 매개변수로 직접 호출하고 그 반환값을 반환합니다. 비동기 메서드 분기에서 `ASSERT` 매크로는 `state_ == ProxyRunning` 식을 검사합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93`, `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:75`, `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:110`

Threaded 비동기 분기에서 `proxy_.invokeMethod`는 `ThreadProxy` 메서드를 전달할 때 연결 유형으로 `ConnectionTypeQueued`를 사용합니다. `{{proxy_name}}Threaded` 생성자는 `ipam->load()`를 호출합니다. 호출 결과가 거짓이면 생성자는 즉시 반환합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:109`, `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:55`

`{{proxy_name}}Threaded` 생성자는 `ipam->load()`가 성공하면 `ipam->createInterface()`를 호출합니다. 반환된 포인터가 없으면 `ipam->path()`를 포함한 오류를 기록하고 생성자에서 반환합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:58`

생성된 `{{proxy_name}}Threaded` 생성자는 `ipam->load()`가 실패하거나 `ipam->createInterface()`가 null을 반환하면 연결 전에 반환합니다. 그 외에는 `ipa_`를 설정하고 `proxy_.setIPA(ipa_.get())`를 호출한 뒤, 각 IPA 이벤트의 `connect`에 수신 객체 `this`와 해당 이벤트의 `{{proxy_name}}Threaded::{{method.mojom_name}}Handler` 메서드를 전달합니다. 연결 코드는 템플릿의 `interface_event.methods` 항목마다 생성되며, 그 뒤 생성자는 `valid_`를 `true`로 설정합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:69`

`{{proxy_name}}Isolated` 생성자는 `resolvePath("{{module_name}}_ipa_proxy")`로 worker 경로를 구하고, 경로가 비어 있으면 오류를 기록한 뒤 반환합니다. 경로가 있으면 IPA 모듈 경로와 worker 경로로 `IPCPipeUnixSocket`을 생성하고, 연결되지 않았다면 오류를 기록한 뒤 반환합니다. 연결되면 `recv`를 `recvMessage`에 연결하고 IPC 객체를 `ipc_`로 이동한 뒤 `valid_`를 `true`로 설정합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130`

`{{proxy_name}}Isolated` 생성자는 워커 경로가 비어 있거나 IPC가 연결되지 않으면 호출 전에 반환합니다. 그 외에는 `ipc`의 `recv`를 현재 객체 `this`의 `{{proxy_name}}Isolated::recvMessage` 콜백에 `connect`로 연결합니다. `{{proxy_name}}Isolated::{{proxy_name}}Isolated()`의 대입문은 `ipc_`를 대상으로 하고 우변에 `std::move(ipc)`를 사용합니다. `{{proxy_name}}Isolated` 생성자는 이 코드 지점에서 `valid_`에 `true`를 대입합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:151`, `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:153`, `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:154`

`IPAProxy::resolvePath`는 먼저 `execPaths_`를 순서대로 확인하고 빈 디렉터리를 건너뛰며, 실행 권한이 있는 첫 번째 worker 경로를 반환합니다. 그다음 `utils::libcameraBuildPath()`가 비어 있지 않으면 해당 빌드 경로의 `src/libcamera/proxy/worker`를 확인하고, 비어 있으면 설치 디렉터리 `IPA_PROXY_DIR`을 확인합니다. 선택한 디렉터리에서 실행 권한이 있는 worker를 찾으면 그 경로를 반환하고, 찾지 못하면 빈 문자열을 반환합니다. `src/libcamera/ipa_proxy.cpp:204`

`IPCPipeUnixSocket::sendSync`는 입력 페이로드, 응답 저장 위치와 헤더의 쿠키로 `call`을 호출하고, 오류가 반환되면 그 값을 반환합니다. `call`은 쿠키와 응답 저장 위치, 완료 상태를 `callData_`에 삽입하려고 하며 삽입 성공 여부는 확인하지 않습니다. 메시지 전송에 실패하면 해당 반복자의 항목을 지우고 오류를 반환하며, 성공하면 2000ms 타이머를 시작하고 완료 상태가 될 때까지 현재 스레드의 이벤트를 처리하다가 시간이 끝나면 항목을 지우고 `-ETIMEDOUT`을 반환합니다. `readyRead`는 수신에 성공하고 헤더 크기 이상의 데이터에서 일치하는 쿠키를 찾으면 페이로드를 해당 응답 위치에 옮기고 완료로 표시하며, `call`은 완료 후 항목을 지우고 0을 반환하고 `sendSync`는 `out`이 있으면 응답으로 `IPCMessage`를 만들어 저장한 뒤 0을 반환합니다. `src/libcamera/ipc_pipe_unixsocket.cpp:27`

`IPCPipeUnixSocket::sendAsync`는 `socket_->send`에 `data.payload()`를 전달합니다. 반환값이 0이 아니면 오류를 기록하고 그 값을 반환합니다. 반환값이 0이면 0을 반환합니다. `src/libcamera/ipc_pipe_unixsocket.cpp:73`

근거 원문: [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) · [src/libcamera/ipa_proxy.cpp:204](#source-59a673fb7c43c0e0) · [src/libcamera/ipc_pipe_unixsocket.cpp:27](#source-f0268126d3f8c2bc) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:75](#source-542f7efc12af7917) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93](#source-7670edf527118b0e) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:109](#source-f6afc431ed47a72a) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:82](#source-9d9c3049e90e4238) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:110](#source-b37be3b88abeaa94) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:55](#source-60c70cd011db2353) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:58](#source-7a0e7fe87df98a33) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:69](#source-927a8955b49d31d4) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:151](#source-c41c960fc2b2e4ff) · [src/libcamera/ipc_pipe_unixsocket.cpp:73](#source-6fafe97ae651cb83) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:153](#source-30b0ddcb59876f61) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:154](#source-4add57ac70567634)

## 프레임 입력과 결과 인터페이스

`IPAIPU3Interface`의 `[async]` 메서드 `queueRequest`는 프레임 번호 `frame`과 요청 제어 값 `controls`를 인자로 받습니다. `computeParams`는 `frame`과 `bufferId`를 받고, `processStats`는 `frame`, `frameTimestamp`, `bufferId`, `sensorControls`를 받습니다. `IPAIPU3EventInterface`에는 `paramsComputed(frame)`과 `metadataReady(frame, metadata)`가 선언되어 있습니다. `setSensorControls`는 `frame`, `sensorControls`, `lensControls`를 인자로 받습니다. `include/libcamera/ipa/ipu3.mojom:19`

`IPARkISP1Interface`의 `[async]` 메서드 `queueRequest`는 프레임 번호 `frame`과 요청 제어 값 `reqControls`를 인자로 받습니다. `computeParams`는 `frame`과 `bufferId`를 받고, `processStats`는 `frame`, `bufferId`, `sensorControls`를 받습니다. `IPARkISP1EventInterface`에는 `paramsComputed(frame, bytesused)`와 `metadataReady(frame, metadata)`가 선언되어 있습니다. `setSensorControls`는 `frame`과 `sensorControls`를 인자로 받습니다. `include/libcamera/ipa/rkisp1.mojom:17`

근거 원문: [include/libcamera/ipa/ipu3.mojom:19](#source-5a4a0da4800968a4) · [include/libcamera/ipa/rkisp1.mojom:17](#source-7a01de2477d6466e)

## IPA 객체와 종료 순서

호출자는 유효한 모듈에서 `IPAModule::load()`를 한 번 성공시킨 뒤 필요한 수만큼 `createInterface()`를 호출할 수 있습니다. 유효하지 않거나 아직 로드되지 않은 모듈에서 `createInterface()`를 호출해서는 안 됩니다. `load()`는 유효하지 않으면 `false`, 이미 로드되었으면 `true`를 반환하며, `createInterface()`는 유효하지 않거나 로드되지 않았으면 `nullptr`를 반환하고 그 외에는 `ipaCreate_()`를 호출합니다. `src/libcamera/ipa_module.cpp:390`

`IPAModule::load()`는 `dlopen()`에 실패하면 `false`를 반환합니다. `ipaCreate` 심볼을 찾지 못하면 핸들을 닫고 `nullptr`로 설정한 뒤 `false`를 반환합니다. 성공하면 팩토리를 저장하고 `loaded_`를 `true`로 설정한 뒤 `true`를 반환합니다. `src/libcamera/ipa_module.cpp:390`

`Threaded` 프록시 생성자는 `load()`가 실패하거나 `createInterface()`가 `nullptr`를 반환하면 중단합니다. 인터페이스 생성에 성공하면 이를 `unique_ptr`에 보유하고 `proxy_`에 설정한 뒤 이벤트 핸들러를 연결하고 `valid_`를 `true`로 설정합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48`

`Threaded::init()`은 IPA의 `init`을 호출한 뒤 `proxy_`를 `thread_`로 옮기고 반환값이 있으면 반환합니다. `start()`는 상태를 `ProxyRunning`으로 설정하고 스레드를 시작한 뒤 `ThreadProxy::start`를 블로킹 방식으로 호출합니다. 비동기 메서드는 상태가 `ProxyRunning`인지 단언한 뒤 `ThreadProxy` 메서드를 큐에 넣어 호출합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48`

`Threaded::stop()`은 상태가 `ProxyStopping`이 아님을 단언하고, `ProxyRunning`이 아니면 반환합니다. 실행 중이면 상태를 `ProxyStopping`으로 바꾸고 `ThreadProxy::stop`을 블로킹 방식으로 호출한 뒤 스레드에 종료를 요청하고 기다립니다. 이어서 현재 스레드에서 이 프록시의 `InvokeMessage` 메시지를 처리하고 상태를 `ProxyStopped`로 설정합니다. `utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25`, `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48`

`Isolated` 프록시 생성자는 워커 경로를 구하지 못하거나 IPC 연결이 없으면 중단합니다. 연결되면 수신 신호를 `recvMessage`에 연결하고 IPC 객체의 소유권을 `ipc_`로 옮긴 뒤 `valid_`를 `true`로 설정합니다. 소멸자는 `ipc_`가 있으면 증가하는 시퀀스 번호를 담은 `Exit` 메시지를 비동기로 보냅니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130`

근거 원문: [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) · [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66)

## 생성과 IPC 실패

`IPAModule::load()`는 `valid_`가 거짓이면 `false`를 반환하고, 이미 `loaded_`가 참이면 `true`를 반환합니다. 그렇지 않으면 `dlopen`으로 공유 객체를 열고, 실패하면 오류를 기록한 뒤 `false`를 반환합니다. 이어서 `dlsym`으로 `ipaCreate`를 찾으며, 실패하면 오류를 기록하고 `dlclose`를 호출한 뒤 `dlHandle_`을 `nullptr`로 설정하고 `false`를 반환합니다. 심볼을 찾으면 이를 `ipaCreate_`에 저장하고 `loaded_`를 참으로 설정한 뒤 `true`를 반환합니다. `src/libcamera/ipa_module.cpp:390`

`IPAModule::createInterface()`는 모듈이 유효하지 않거나 로드되지 않았다면 `nullptr`을 반환합니다. 두 조건을 모두 통과하면 `ipaCreate_()`를 호출하고 그 반환값을 반환합니다. `IPCPipeUnixSocket::sendSync`는 입력 메시지의 페이로드와 쿠키, 응답 저장 위치를 `call`에 전달하고 반환값이 0이 아니면 오류를 기록한 뒤 그 값을 반환합니다. `call`이 성공하면 `out`이 null이 아닐 때 응답으로 만든 `IPCMessage`를 `*out`에 대입하고 0을 반환합니다. `src/libcamera/ipa_module.cpp:390`, `src/libcamera/ipc_pipe_unixsocket.cpp:27`

`IPCPipeUnixSocket::call`은 `cookie`와 응답 포인터, 완료 상태 `false`로 `callData_`에 항목을 삽입하고 결과의 반복자 `iter`를 보관합니다. 소켓의 `send`에는 반복자가 아닌 `message`를 전달합니다. 송신 결과가 0이 아니면 `iter`가 가리키는 항목을 `erase`로 지우고 송신 결과를 반환합니다. `src/libcamera/ipc_pipe_unixsocket.cpp:27`

`IPCPipeUnixSocket::call`은 응답 항목을 삽입한 결과의 반복자 `iter`를 사용하며, 타이머를 `2000ms`로 시작한 뒤 `iter->second.done`이 참이 될 때까지 이벤트를 처리합니다. 대기 중 타이머가 실행 중이 아니면 `callData_.erase(iter)`로 항목을 지우고 `-ETIMEDOUT`을 반환합니다. 완료되면 같은 반복자로 항목을 지우고 `0`을 반환합니다. `src/libcamera/ipc_pipe_unixsocket.cpp:27`

근거 원문: [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) · [src/libcamera/ipc_pipe_unixsocket.cpp:27](#source-f0268126d3f8c2bc)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 어떤 IPA 모듈과 실행 방식이 선택됩니까? | [모듈 탐색과 격리 조건](#모듈-탐색과-격리-조건) | 코드 근거와 설명 연결 |
    | 동기 호출과 비동기 호출은 어디에서 실행됩니까? | [스레드와 프로세스 경계](#스레드와-프로세스-경계) | 코드 근거와 설명 연결 |
    | 파이프라인과 알고리즘은 어떤 입력과 결과를 주고받습니까? | [프레임 입력과 결과 인터페이스](#프레임-입력과-결과-인터페이스) | 코드 근거와 설명 연결 |
    | 인터페이스를 만들고 비동기 처리를 끝내는 계약은 무엇입니까? | [IPA 객체와 종료 순서](#ipa-객체와-종료-순서) | 코드 근거와 설명 연결 |
    | 모듈 생성과 IPC 오류는 어떻게 관찰됩니까? | [생성과 IPC 실패](#생성과-ipc-실패) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-7603cbafe8eef490"></a>

??? note "소스 근거: src/libcamera/ipa_manager.cpp:107"
    `src/libcamera/ipa_manager.cpp:107`에서 시작하는 발췌입니다. 종료 줄은 162이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `ed1b15d5743b434eb29e34ba981de978ff4dd9bcb186859e4800931a525e766c`
    
    ```text
    IPAManager::IPAManager(const CameraManager &cm)
    	: cm_(cm)
    {
    	const GlobalConfiguration &configuration = cm._d()->configuration();
    
    #if HAVE_IPA_PUBKEY
    	if (!pubKey_.isValid())
    		LOG(IPAManager, Warning) << "Public key not valid";
    
    	forceIsolation_ = configuration.option<bool>({ "ipa", "force_isolation" })
    				       .value_or(false);
    #endif
    
    	unsigned int ipaCount = 0;
    
    	/* User-specified paths take precedence. */
    	const auto modulePaths =
    		configuration.listOption({ "ipa", "module_paths" })
    			.value_or(utils::defopt);
    	for (const auto &dir : modulePaths) {
    		if (dir.empty())
    			continue;
    
    		ipaCount += addDir(dir.c_str());
    	}
    
    	if (!modulePaths.empty() && !ipaCount)
    		LOG(IPAManager, Warning) << "No IPA found in '"
    					 << utils::join(modulePaths, ":")
    					 << "'";
    
    	/*
    	 * When libcamera is used before it is installed, load IPAs from the
    	 * same build directory as the libcamera library itself.
    	 */
    	std::string root = utils::libcameraBuildPath();
    	if (!root.empty()) {
    		std::string ipaBuildPath = root + "src/ipa";
    		constexpr int maxDepth = 2;
    
    		LOG(IPAManager, Info)
    			<< "libcamera is not installed. Adding '"
    			<< ipaBuildPath << "' to the IPA search path";
    
    		ipaCount += addDir(ipaBuildPath.c_str(), maxDepth);
    	}
    
    	/* Finally try to load IPAs from the installed system path. */
    	ipaCount += addDir(IPA_MODULE_DIR);
    
    	if (!ipaCount)
    		LOG(IPAManager, Warning)
    			<< "No IPA found in '" IPA_MODULE_DIR "'";
    }
    
    IPAManager::~IPAManager() = default;
    ```

<a id="source-6e1525c1fc1aa55e"></a>

??? note "소스 근거: src/libcamera/ipa_module.cpp:460"
    `src/libcamera/ipa_module.cpp:460`에서 시작하는 발췌입니다. 종료 줄은 478이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `99940db9ea353ad0d8282b7c2148578f4c6054d785ef7aaf690d522b52bafb5b`
    
    ```text
    \brief Verify if the IPA module matches a given name
     * \param[in] name The IPA module name
     * \param[in] minVersion Minimum acceptable version of IPA module
     * \param[in] maxVersion Maximum acceptable version of IPA module
     *
     * This function checks if this IPA module matches the requested \a name
     * and the input version range.
     *
     * \return True if the IPA module matches, or false otherwise
     */
    bool IPAModule::match(const char *name, uint32_t minVersion,
    		      uint32_t maxVersion) const
    {
    	return info_.pipelineVersion >= minVersion &&
    	       info_.pipelineVersion <= maxVersion &&
    	       !strcmp(info_.name, name);
    }
    
    std::string IPAModule::logPrefix()
    ```

<a id="source-2a1bbbc8623a516f"></a>

??? note "소스 근거: include/libcamera/internal/ipa_manager.h:35"
    `include/libcamera/internal/ipa_manager.h:35`에서 시작하는 발췌입니다. 종료 줄은 58이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e0bd5192ea24a8b39d3df7b7b93c8b17614663a0144f6dd0741d410fa321d458`
    
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
    
    #if HAVE_IPA_PUBKEY
    ```

<a id="source-532f8ffa194bd319"></a>

??? note "소스 근거: src/libcamera/ipa_manager.cpp:289"
    `src/libcamera/ipa_manager.cpp:289`에서 시작하는 발췌입니다. 종료 줄은 319이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `f657ce54df77453510108b02060166edd7506c982d13d3e4868fadee4065a677`
    
    ```text
    bool IPAManager::isSignatureValid([[maybe_unused]] IPAModule *ipa) const
    {
    #if HAVE_IPA_PUBKEY
    	if (forceIsolation_) {
    		LOG(IPAManager, Debug)
    			<< "Isolation of IPA module " << ipa->path()
    			<< " forced through configuration";
    		return false;
    	}
    
    	File file{ ipa->path() };
    	if (!file.open(File::OpenModeFlag::ReadOnly))
    		return false;
    
    	std::span<uint8_t> data = file.map();
    	if (data.empty())
    		return false;
    
    	bool valid = pubKey_.verify(data, ipa->signature());
    
    	LOG(IPAManager, Debug)
    		<< "IPA module " << ipa->path() << " signature is "
    		<< (valid ? "valid" : "not valid");
    
    	return valid;
    #else
    	return false;
    #endif
    }
    
    } /* namespace libcamera */
    ```

<a id="source-c7fd6e52f2c537b5"></a>

??? note "소스 근거: utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48"
    `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48`에서 시작하는 발췌입니다. 종료 줄은 128이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `af4b12c81ffee2e9979c01a7e7eb188f5568d258ba03e522b60a3608dc226abd`
    
    ```text
    {{proxy_name}}Threaded::{{proxy_name}}Threaded(IPAModule *ipam, const CameraManager &cm)
    	: {{proxy_name}}(ipam, cm), thread_("{{proxy_name}}")
    {
    	LOG(IPAProxy, Debug)
    		<< "initializing {{module_name}} proxy in thread: loading IPA from "
    		<< ipam->path();
    
    	if (!ipam->load())
    		return;
    
    	IPAInterface *ipai = ipam->createInterface();
    	if (!ipai) {
    		LOG(IPAProxy, Error)
    			<< "Failed to create IPA context for " << ipam->path();
    		return;
    	}
    
    	ipa_ = std::unique_ptr<{{interface_name}}>(static_cast<{{interface_name}} *>(ipai));
    	proxy_.setIPA(ipa_.get());
    
    {% for method in interface_event.methods %}
    	ipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);
    {%- endfor %}
    
    	valid_ = true;
    }
    
    {{proxy_name}}Threaded::~{{proxy_name}}Threaded() = default;
    
    {% for method in interface_main.methods %}
    {{proxy_funcs.func_sig(proxy_name + "Threaded", method)}}
    {
    {%- if method.mojom_name == "stop" %}
    	{{proxy_funcs.stop_thread_body()}}
    {%- elif method.mojom_name == "init" %}
    	{{ method|method_return_value + " _ret = " if method|method_return_value != "void" -}}
    	ipa_->{{method.mojom_name}}(
    	{%- for param in method|method_param_names -%}
    		{{param}}{{- ", " if not loop.last}}
    	{%- endfor -%}
    );
    
    	proxy_.moveToThread(&thread_);
    
    	return {{ "_ret" if method|method_return_value != "void" }};
    {%- elif method.mojom_name == "start" %}
    	state_ = ProxyRunning;
    	thread_.start();
    
    	return proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking
    	{{- ", " if method|method_param_names}}
    	{%- for param in method|method_param_names -%}
    		{{param}}{{- ", " if not loop.last}}
    	{%- endfor -%}
    );
    {%- elif not method|is_async %}
    	return ipa_->{{method.mojom_name}}(
    	{%- for param in method|method_param_names -%}
    		{{param}}{{- ", " if not loop.last}}
    	{%- endfor -%}
    );
    {% elif method|is_async %}
    	ASSERT(state_ == ProxyRunning);
    	proxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued
    	{%- for param in method|method_param_names -%}
    		, {{param}}
    	{%- endfor -%}
    );
    {%- endif %}
    }
    {% endfor %}
    
    {% for method in interface_event.methods %}
    {{proxy_funcs.func_sig(proxy_name + "Threaded", method, "Handler")}}
    {
    	ASSERT(state_ != ProxyStopped);
    	{{method.mojom_name}}.emit({{method.parameters|params_comma_sep}});
    }
    {% endfor %}
    
    /* ========================================================================== */
    ```

<a id="source-9ff6047b0a70ce66"></a>

??? note "소스 근거: utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130"
    `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130`에서 시작하는 발췌입니다. 종료 줄은 212이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744`
    
    ```text
    {{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)
    	: {{proxy_name}}(ipam, cm),
    	  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)
    {
    	LOG(IPAProxy, Debug)
    		<< "initializing {{module_name}} proxy in isolation: loading IPA from "
    		<< ipam->path();
    
    	const std::string proxyWorkerPath = resolvePath("{{module_name}}_ipa_proxy");
    	if (proxyWorkerPath.empty()) {
    		LOG(IPAProxy, Error) << "Failed to get proxy worker path";
    		return;
    	}
    
    	auto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),
    						       proxyWorkerPath.c_str());
    	if (!ipc->isConnected()) {
    		LOG(IPAProxy, Error) << "Failed to create IPCPipe";
    		return;
    	}
    
    	ipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);
    
    	ipc_ = std::move(ipc);
    	valid_ = true;
    }
    
    {{proxy_name}}Isolated::~{{proxy_name}}Isolated()
    {
    	if (ipc_) {
    		IPCMessage::Header header =
    			{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };
    		IPCMessage msg(header);
    		ipc_->sendAsync(msg);
    	}
    }
    
    {% for method in interface_main.methods %}
    {{proxy_funcs.func_sig(proxy_name + "Isolated", method)}}
    {
    {%- if method.mojom_name == "configure" %}
    	controlSerializer_.reset();
    {%- endif %}
    {%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != "void" %}
    {%- set cmd = cmd_enum_name + "::" + method.mojom_name|cap %}
    	IPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };
    	IPCMessage _ipcInputBuf(_header);
    {%- if has_output %}
    	IPCMessage _ipcOutputBuf;
    {%- endif %}
    
    {{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}
    
    {% if method|is_async %}
    	int _ret = ipc_->sendAsync(_ipcInputBuf);
    {%- else %}
    	int _ret = ipc_->sendSync(_ipcInputBuf
    {{- ", &_ipcOutputBuf" if has_output -}}
    );
    {%- endif %}
    	if (_ret < 0) {
    		LOG(IPAProxy, Error) << "Failed to call {{method.mojom_name}}: " << _ret;
    {%- if method|method_return_value != "void" %}
    		return static_cast<{{method|method_return_value}}>(_ret);
    {%- else %}
    		return;
    {%- endif %}
    	}
    {% if method|method_return_value != "void" %}
    	{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);
    
    {{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}
    
    	return _retValue;
    
    {% elif method|method_param_outputs|length > 0 %}
    {{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}
    {% endif -%}
    }
    
    {% endfor %}
    
    void {{proxy_name}}Isolated::recvMessage(
    ```

<a id="source-59a673fb7c43c0e0"></a>

??? note "소스 근거: src/libcamera/ipa_proxy.cpp:204"
    `src/libcamera/ipa_proxy.cpp:204`에서 시작하는 발췌입니다. 종료 줄은 261이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `8cbcadf7036cdb391f4c48af8562cb637752242f9564f1118c949a62df9dbd77`
    
    ```text
    \brief Find a valid full path for a proxy worker for a given executable name
     * \param[in] file File name of proxy worker executable
     *
     * A proxy worker's executable could be found in either the global installation
     * directory, or in the paths specified by the environment variable
     * LIBCAMERA_IPA_PROXY_PATH. This function checks the global install directory
     * first, then LIBCAMERA_IPA_PROXY_PATH in order, and returns the full path to
     * the proxy worker executable that is specified by file. The proxy worker
     * executable shall have exec permission.
     *
     * \return The full path to the proxy worker executable, or an empty string if
     * no valid executable path
     */
    std::string IPAProxy::resolvePath(const std::string &file) const
    {
    	std::string proxyFile = "/" + file;
    
    	/* Try paths from the configuration first. */
    	for (const auto &dir : execPaths_) {
    		if (dir.empty())
    			continue;
    
    		std::string proxyPath = dir + proxyFile;
    		if (!access(proxyPath.c_str(), X_OK))
    			return proxyPath;
    	}
    
    	/*
    	 * When libcamera is used before it is installed, load proxy workers
    	 * from the same build directory as the libcamera directory itself.
    	 * This requires identifying the path of the libcamera.so, and
    	 * referencing a relative path for the proxy workers from that point.
    	 */
    	std::string root = utils::libcameraBuildPath();
    	if (!root.empty()) {
    		std::string ipaProxyDir = root + "src/libcamera/proxy/worker";
    
    		LOG(IPAProxy, Info)
    			<< "libcamera is not installed. Loading proxy workers from '"
    			<< ipaProxyDir << "'";
    
    		std::string proxyPath = ipaProxyDir + proxyFile;
    		if (!access(proxyPath.c_str(), X_OK))
    			return proxyPath;
    
    		return std::string();
    	}
    
    	/* Else try finding the exec target from the install directory. */
    	std::string proxyPath = std::string(IPA_PROXY_DIR) + proxyFile;
    	if (!access(proxyPath.c_str(), X_OK))
    		return proxyPath;
    
    	return std::string();
    }
    
    /**
     * \var IPAProxy::valid_
    ```

<a id="source-f0268126d3f8c2bc"></a>

??? note "소스 근거: src/libcamera/ipc_pipe_unixsocket.cpp:27"
    `src/libcamera/ipc_pipe_unixsocket.cpp:27`에서 시작하는 발췌입니다. 종료 줄은 144이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `0abe488ceae72cca0a5b96c7223ffc4cc412ab18f94765fd7f001dc450544f40`
    
    ```text
    IPCPipeUnixSocket::IPCPipeUnixSocket(const char *ipaModulePath,
    				     const char *ipaProxyWorkerPath)
    	: IPCPipe()
    {
    	socket_ = std::make_unique<IPCUnixSocket>();
    	UniqueFD fd = socket_->create();
    	if (!fd.isValid()) {
    		LOG(IPCPipe, Error) << "Failed to create socket";
    		return;
    	}
    	socket_->readyRead.connect(this, &IPCPipeUnixSocket::readyRead);
    
    	std::array args{ std::string(ipaModulePath), std::to_string(fd.get()) };
    	std::array fds{ fd.get() };
    
    	proc_ = std::make_unique<Process>();
    	int ret = proc_->start(ipaProxyWorkerPath, args, fds);
    	if (ret) {
    		LOG(IPCPipe, Error)
    			<< "Failed to start proxy worker process";
    		return;
    	}
    
    	connected_ = true;
    }
    
    IPCPipeUnixSocket::~IPCPipeUnixSocket()
    {
    }
    
    int IPCPipeUnixSocket::sendSync(const IPCMessage &in, IPCMessage *out)
    {
    	IPCUnixSocket::Payload response;
    
    	int ret = call(in.payload(), &response, in.header().cookie);
    	if (ret) {
    		LOG(IPCPipe, Error) << "Failed to call sync";
    		return ret;
    	}
    
    	if (out)
    		*out = IPCMessage(response);
    
    	return 0;
    }
    
    int IPCPipeUnixSocket::sendAsync(const IPCMessage &data)
    {
    	int ret = socket_->send(data.payload());
    	if (ret) {
    		LOG(IPCPipe, Error) << "Failed to call async";
    		return ret;
    	}
    
    	return 0;
    }
    
    void IPCPipeUnixSocket::readyRead()
    {
    	IPCUnixSocket::Payload payload;
    	int ret = socket_->receive(&payload);
    	if (ret) {
    		LOG(IPCPipe, Error) << "Receive message failed" << ret;
    		return;
    	}
    
    	/* \todo Use span to avoid the double copy when callData is found. */
    	if (payload.data.size() < sizeof(IPCMessage::Header)) {
    		LOG(IPCPipe, Error) << "Not enough data received";
    		return;
    	}
    
    	IPCMessage ipcMessage(payload);
    
    	auto callData = callData_.find(ipcMessage.header().cookie);
    	if (callData != callData_.end()) {
    		*callData->second.response = std::move(payload);
    		callData->second.done = true;
    		return;
    	}
    
    	/* Received unexpected data, this means it's a call from the IPA. */
    	recv.emit(ipcMessage);
    }
    
    int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,
    			    IPCUnixSocket::Payload *response, uint32_t cookie)
    {
    	Timer timeout;
    	int ret;
    
    	const auto result = callData_.insert({ cookie, { response, false } });
    	const auto &iter = result.first;
    
    	ret = socket_->send(message);
    	if (ret) {
    		callData_.erase(iter);
    		return ret;
    	}
    
    	/* \todo Make this less dangerous, see IPCPipe::sendSync() */
    	timeout.start(2000ms);
    	while (!iter->second.done) {
    		if (!timeout.isRunning()) {
    			LOG(IPCPipe, Error) << "Call timeout!";
    			callData_.erase(iter);
    			return -ETIMEDOUT;
    		}
    
    		Thread::current()->eventDispatcher()->processEvents();
    	}
    
    	callData_.erase(iter);
    
    	return 0;
    }
    
    } /* namespace libcamera */
    ```

<a id="source-542f7efc12af7917"></a>

??? note "소스 근거: utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:75"
    `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:75`에서 시작하는 발췌입니다. 종료 줄은 128이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `229171bf11ad25715f66dce8118661d411ecb495b15b82548f9f9a8369e0fa0c`
    
    ```text
    {{proxy_name}}Threaded::~{{proxy_name}}Threaded() = default;
    
    {% for method in interface_main.methods %}
    {{proxy_funcs.func_sig(proxy_name + "Threaded", method)}}
    {
    {%- if method.mojom_name == "stop" %}
    	{{proxy_funcs.stop_thread_body()}}
    {%- elif method.mojom_name == "init" %}
    	{{ method|method_return_value + " _ret = " if method|method_return_value != "void" -}}
    	ipa_->{{method.mojom_name}}(
    	{%- for param in method|method_param_names -%}
    		{{param}}{{- ", " if not loop.last}}
    	{%- endfor -%}
    );
    
    	proxy_.moveToThread(&thread_);
    
    	return {{ "_ret" if method|method_return_value != "void" }};
    {%- elif method.mojom_name == "start" %}
    	state_ = ProxyRunning;
    	thread_.start();
    
    	return proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking
    	{{- ", " if method|method_param_names}}
    	{%- for param in method|method_param_names -%}
    		{{param}}{{- ", " if not loop.last}}
    	{%- endfor -%}
    );
    {%- elif not method|is_async %}
    	return ipa_->{{method.mojom_name}}(
    	{%- for param in method|method_param_names -%}
    		{{param}}{{- ", " if not loop.last}}
    	{%- endfor -%}
    );
    {% elif method|is_async %}
    	ASSERT(state_ == ProxyRunning);
    	proxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued
    	{%- for param in method|method_param_names -%}
    		, {{param}}
    	{%- endfor -%}
    );
    {%- endif %}
    }
    {% endfor %}
    
    {% for method in interface_event.methods %}
    {{proxy_funcs.func_sig(proxy_name + "Threaded", method, "Handler")}}
    {
    	ASSERT(state_ != ProxyStopped);
    	{{method.mojom_name}}.emit({{method.parameters|params_comma_sep}});
    }
    {% endfor %}
    
    /* ========================================================================== */
    ```

<a id="source-7670edf527118b0e"></a>

??? note "소스 근거: utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93"
    `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93`에서 시작하는 발췌입니다. 종료 줄은 103이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `6d84fe1343442ab9a1a6b0a70cb1d00c03d0ed1af36ac3cfb8fe739590f517e1`
    
    ```text
    {%- elif method.mojom_name == "start" %}
    	state_ = ProxyRunning;
    	thread_.start();
    
    	return proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking
    	{{- ", " if method|method_param_names}}
    	{%- for param in method|method_param_names -%}
    		{{param}}{{- ", " if not loop.last}}
    	{%- endfor -%}
    );
    {%- elif not method|is_async %}
    ```

<a id="source-f6afc431ed47a72a"></a>

??? note "소스 근거: utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:109"
    `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:109`에서 시작하는 발췌입니다. 종료 줄은 118이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `9bffd86ebff514f6f8f34878e0f5b845ba9a15ccfc50b967619c8e9a9c90651d`
    
    ```text
    {% elif method|is_async %}
    	ASSERT(state_ == ProxyRunning);
    	proxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued
    	{%- for param in method|method_param_names -%}
    		, {{param}}
    	{%- endfor -%}
    );
    {%- endif %}
    }
    {% endfor %}
    ```

<a id="source-9d9c3049e90e4238"></a>

??? note "소스 근거: utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:82"
    `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:82`에서 시작하는 발췌입니다. 종료 줄은 93이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `19c6c157aeb7f5b049df673ccd1c2792c2675800d870838db244a21f359738b9`
    
    ```text
    {%- elif method.mojom_name == "init" %}
    	{{ method|method_return_value + " _ret = " if method|method_return_value != "void" -}}
    	ipa_->{{method.mojom_name}}(
    	{%- for param in method|method_param_names -%}
    		{{param}}{{- ", " if not loop.last}}
    	{%- endfor -%}
    );
    
    	proxy_.moveToThread(&thread_);
    
    	return {{ "_ret" if method|method_return_value != "void" }};
    {%- elif method.mojom_name == "start" %}
    ```

<a id="source-b37be3b88abeaa94"></a>

??? note "소스 근거: utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:110"
    `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:110`에서 시작하는 발췌입니다. 종료 줄은 110이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `907e9f99409f5dcd13b06745e069a05a81b9fb1a21617232a4cb060e2d9c3bdd`
    
    ```text
    ASSERT(state_ == ProxyRunning);
    ```

<a id="source-60c70cd011db2353"></a>

??? note "소스 근거: utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:55"
    `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:55`에서 시작하는 발췌입니다. 종료 줄은 56이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `487c09c1385700711ded6c5037d3c9d4d59b576e401dd378775c6d567c6b4dbe`
    
    ```text
    if (!ipam->load())
    		return;
    ```

<a id="source-7a0e7fe87df98a33"></a>

??? note "소스 근거: utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:58"
    `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:58`에서 시작하는 발췌입니다. 종료 줄은 62이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `cdee49f4fce36694cff46c542c33cb7f1cd7ba1adc2dab4b01fffb12578b85bc`
    
    ```text
    IPAInterface *ipai = ipam->createInterface();
    	if (!ipai) {
    		LOG(IPAProxy, Error)
    			<< "Failed to create IPA context for " << ipam->path();
    		return;
    ```

<a id="source-927a8955b49d31d4"></a>

??? note "소스 근거: utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:69"
    `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:69`에서 시작하는 발췌입니다. 종료 줄은 69이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `0cec3d8da87151d56561b06770b67b9710e096c7c405e1ceb50dc4b3de79f200`
    
    ```text
    ipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);
    ```

<a id="source-c41c960fc2b2e4ff"></a>

??? note "소스 근거: utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:151"
    `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:151`에서 시작하는 발췌입니다. 종료 줄은 151이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `872cbd408f61ee3a0da2ff0a4fe78884d33175d38205d6648529651cd604f884`
    
    ```text
    ipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);
    ```

<a id="source-6fafe97ae651cb83"></a>

??? note "소스 근거: src/libcamera/ipc_pipe_unixsocket.cpp:73"
    `src/libcamera/ipc_pipe_unixsocket.cpp:73`에서 시작하는 발췌입니다. 종료 줄은 84이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `81f2c0648cc4ae69f0049dd2aef8d25e3fc1bc498706a15d41d76db29c865f61`
    
    ```text
    int IPCPipeUnixSocket::sendAsync(const IPCMessage &data)
    {
    	int ret = socket_->send(data.payload());
    	if (ret) {
    		LOG(IPCPipe, Error) << "Failed to call async";
    		return ret;
    	}
    
    	return 0;
    }
    
    void IPCPipeUnixSocket::readyRead()
    ```

<a id="source-30b0ddcb59876f61"></a>

??? note "소스 근거: utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:153"
    `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:153`에서 시작하는 발췌입니다. 종료 줄은 154이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `cb93fde36a35c51dac44f4da886ede9b356e45a1f80027fb12b75e65613de02b`
    
    ```text
    ipc_ = std::move(ipc);
    	valid_ = true;
    ```

<a id="source-4add57ac70567634"></a>

??? note "소스 근거: utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:154"
    `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:154`에서 시작하는 발췌입니다. 종료 줄은 154이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `8f2f30f0378b3737fdf2f7bd7717a59769665fcd1bbf6eeae8d0a2b1fe2e953f`
    
    ```text
    valid_ = true;
    ```

<a id="source-5a4a0da4800968a4"></a>

??? note "소스 근거: include/libcamera/ipa/ipu3.mojom:19"
    `include/libcamera/ipa/ipu3.mojom:19`에서 시작하는 발췌입니다. 종료 줄은 44이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `f1969299336634cdd04e42402648a452126032a25540ad5c78bd2c804362a381`
    
    ```text
    interface IPAIPU3Interface {
    	init(libcamera.IPASettings settings,
    	     libcamera.IPACameraSensorInfo sensorInfo,
    	     libcamera.ControlInfoMap sensorControls)
    		=> (int32 ret, libcamera.ControlInfoMap ipaControls);
    	start() => (int32 ret);
    	stop();
    
    	configure(IPAConfigInfo configInfo)
    		=> (int32 ret, libcamera.ControlInfoMap ipaControls);
    
    	mapBuffers(array<libcamera.IPABuffer> buffers);
    	unmapBuffers(array<uint32> ids);
    
    	[async] queueRequest(uint32 frame, libcamera.ControlList controls);
    	[async] computeParams(uint32 frame, uint32 bufferId);
    	[async] processStats(uint32 frame, int64 frameTimestamp,
    			     uint32 bufferId, libcamera.ControlList sensorControls);
    };
    
    interface IPAIPU3EventInterface {
    	setSensorControls(uint32 frame, libcamera.ControlList sensorControls,
    			  libcamera.ControlList lensControls);
    	paramsComputed(uint32 frame);
    	metadataReady(uint32 frame, libcamera.ControlList metadata);
    };
    ```

<a id="source-7a01de2477d6466e"></a>

??? note "소스 근거: include/libcamera/ipa/rkisp1.mojom:17"
    `include/libcamera/ipa/rkisp1.mojom:17`에서 시작하는 발췌입니다. 종료 줄은 43이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `32d657315ff8eac800254f0a5d39462d55bb4b0ef6ee5717930f3d3b8504162b`
    
    ```text
    interface IPARkISP1Interface {
    	init(libcamera.IPASettings settings,
    	     uint32 hwRevision, uint32 supportedBlocks,
    	     libcamera.IPACameraSensorInfo sensorInfo,
    	     libcamera.ControlInfoMap sensorControls)
    		=> (int32 ret, libcamera.ControlInfoMap ipaControls);
    	start() => (int32 ret);
    	stop();
    
    	configure(IPAConfigInfo configInfo,
    		  map<uint32, libcamera.IPAStream> streamConfig)
    		=> (int32 ret, libcamera.ControlInfoMap ipaControls);
    
    	mapBuffers(array<libcamera.IPABuffer> buffers);
    	unmapBuffers(array<uint32> ids);
    
    	[async] queueRequest(uint32 frame, libcamera.ControlList reqControls);
    	[async] computeParams(uint32 frame, uint32 bufferId);
    	[async] processStats(uint32 frame, uint32 bufferId,
    			     libcamera.ControlList sensorControls);
    };
    
    interface IPARkISP1EventInterface {
    	paramsComputed(uint32 frame, uint32 bytesused);
    	setSensorControls(uint32 frame, libcamera.ControlList sensorControls);
    	metadataReady(uint32 frame, libcamera.ControlList metadata);
    };
    ```

<a id="source-fadefbb962b2fc44"></a>

??? note "소스 근거: src/libcamera/ipa_module.cpp:390"
    `src/libcamera/ipa_module.cpp:390`에서 시작하는 발췌입니다. 종료 줄은 460이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619`
    
    ```text
    \brief Load the IPA implementation factory from the shared object
     *
     * The IPA module shared object implements an IPAInterface object to be used
     * by pipeline handlers. This function loads the factory function from the
     * shared object. Later, createInterface() can be called to instantiate the
     * IPAInterface.
     *
     * This function only needs to be called successfully once, after which
     * createInterface() can be called as many times as IPAInterface instances are
     * needed.
     *
     * Calling this function on an invalid module (as returned by isValid()) is
     * an error.
     *
     * \return True if load was successful, or already loaded, and false otherwise
     */
    bool IPAModule::load()
    {
    	if (!valid_)
    		return false;
    
    	if (loaded_)
    		return true;
    
    	dlHandle_ = dlopen(libPath_.c_str(), RTLD_LAZY);
    	if (!dlHandle_) {
    		LOG(IPAModule, Error)
    			<< "Failed to open IPA module shared object: "
    			<< dlerror();
    		return false;
    	}
    
    	void *symbol = dlsym(dlHandle_, "ipaCreate");
    	if (!symbol) {
    		LOG(IPAModule, Error)
    			<< "Failed to load ipaCreate() from IPA module shared object: "
    			<< dlerror();
    		dlclose(dlHandle_);
    		dlHandle_ = nullptr;
    		return false;
    	}
    
    	ipaCreate_ = reinterpret_cast<IPAIntfFactory>(symbol);
    
    	loaded_ = true;
    
    	return true;
    }
    
    /**
     * \brief Instantiate an IPA interface
     *
     * After loading the IPA module with load(), this function creates an instance
     * of the IPA module interface.
     *
     * Calling this function on a module that has not yet been loaded, or an
     * invalid module (as returned by load() and isValid(), respectively) is
     * an error.
     *
     * \return The IPA interface on success, or nullptr on error
     */
    IPAInterface *IPAModule::createInterface()
    {
    	if (!valid_ || !loaded_)
    		return nullptr;
    
    	return ipaCreate_();
    }
    
    /**
     * \brief Verify if the IPA module matches
    ```

<a id="source-eb8f57d7452822da"></a>

??? note "소스 근거: utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25"
    `utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25`에서 시작하는 발췌입니다. 종료 줄은 40이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b`
    
    ```text
    {%- macro stop_thread_body() -%}
    	ASSERT(state_ != ProxyStopping);
    	if (state_ != ProxyRunning)
    		return;
    
    	state_ = ProxyStopping;
    
    	proxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);
    
    	thread_.exit();
    	thread_.wait();
    
    	Thread::current()->dispatchMessages(Message::Type::InvokeMessage, this);
    
    	state_ = ProxyStopped;
    {%- endmacro -%}
    ```


<!-- sdd:class-diagram -->
## 클래스 관계

화살표의 글자는 추출한 관계를 나타내며, 점선은 상속입니다. 화살표는 참조 대상 또는 기반 클래스를 향합니다. 호출 순서를 뜻하지 않습니다.

```mermaid
flowchart LR
  c0["IPAInterface"]:::context
  c1["IPAManager"]
  c2["IPAModule"]
  c3["IPAProxy"]
  c4["Loggable"]:::context
  c5["ipa::ipu3::IPAIPU3"]
  c6["ipa::ipu3::Module"]:::context
  c7["ipa::rkisp1::IPARkISP1"]
  c8["ipa::rkisp1::Module"]:::context
  c1 -->|필드 참조| c2
  c2 -.->|상속| c4
  c3 -.->|상속| c0
  c3 -->|필드 참조| c2
  c5 -.->|상속| c6
  c7 -.->|상속| c8
  classDef context fill:#fafafa,stroke:#aaa,stroke-dasharray:4 3,color:#555
```
<!-- /sdd:class-diagram -->



## 관련 클래스

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::IPAManager` | `include/libcamera/internal/ipa_manager.h:29` | – | Manager for IPA modules |
| `libcamera::IPAModule` | `include/libcamera/internal/ipa_module.h:21` | `libcamera::Loggable` | Wrapper around IPA module shared object |
| `libcamera::IPAProxy` | `include/libcamera/internal/ipa_proxy.h:22` | `libcamera::IPAInterface` | IPA Proxy |
| `libcamera::ipa::ipu3::IPAIPU3` | `src/ipa/ipu3/ipu3.cpp:139` | `libcamera::ipa::ipu3::Module` | The IPU3 IPA implementation |
| `libcamera::ipa::rkisp1::IPARkISP1` | `src/ipa/rkisp1/rkisp1.cpp:46` | `libcamera::ipa::rkisp1::Module` | 확인 필요 |

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `include/libcamera/internal/ipa_manager.h`, `include/libcamera/internal/ipa_module.h`, `include/libcamera/internal/ipa_proxy.h`, `include/libcamera/ipa/ipu3.mojom`, `include/libcamera/ipa/rkisp1.mojom`, `src/ipa/ipu3/ipu3.cpp`, `src/ipa/rkisp1/rkisp1.cpp`, `src/libcamera/ipa_manager.cpp`, `src/libcamera/ipa_module.cpp`, `src/libcamera/ipa_proxy.cpp`, `src/libcamera/ipc_pipe_unixsocket.cpp`, `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl`, `utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `e117198c01`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-29 · 사람 검토 전

다음 단계: [IPA 튜닝과 소프트웨어 ISP](ipa-algorithms.md)
