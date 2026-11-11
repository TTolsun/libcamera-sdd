---
generated_at: 2026-11-11T21:03:20+00:00
source_commit: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
status: ok
section: ipa
generation_method: facts-and-llm
evidence_fingerprint: 6bd9a797391703f61c06ff13e345ac89208f335d48d64e3db999648e07205d70
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "6bd9a797391703f61c06ff13e345ac89208f335d48d64e3db999648e07205d70", "answers": {"selection": [{"text": "`IPAManager::IPAManager`는 사용자가 지정한 `ipa.module_paths`를 우선 검색하며, 빈 경로는 건너뛰고 나머지 경로마다 `addDir()`을 호출합니다. 지정된 경로 목록이 비어 있지 않지만 IPA를 하나도 찾지 못하면 경고를 기록합니다. 이어서 `utils::libcameraBuildPath()`가 빈 문자열이 아니면 그 경로에 `src/ipa`를 붙여 최대 깊이 2로 `addDir()`을 호출합니다. 마지막으로 설치된 시스템 경로 `IPA_MODULE_DIR`에 `addDir()`을 호출하고, 전체 검색에서 IPA를 하나도 찾지 못하면 경고를 기록합니다.", "evidence": ["modules"], "covers": ["selection"], "kind": "behavior", "quote": "/* User-specified paths take precedence. */\n\tconst auto modulePaths =\n\t\tconfiguration.listOption({ \"ipa\", \"module_paths\" })\n\t\t\t.value_or(utils::defopt);\n\tfor (const auto &dir : modulePaths) {\n\t\tif (dir.empty())\n\t\t\tcontinue;", "part_id": "search-paths"}, {"text": "`IPAModule::match`는 `info_.pipelineVersion`이 `minVersion` 이상이고 `maxVersion` 이하이며, `info_.name`과 `name`을 비교한 `strcmp`의 결과가 0이면 `true`를 반환합니다. 이 조건 중 하나라도 만족하지 않으면 `false`를 반환합니다.", "evidence": ["match"], "covers": ["selection"], "kind": "behavior", "quote": "\\brief Verify if the IPA module matches a given name\n * \\param[in] name The IPA module name\n * \\param[in] minVersion Minimum acceptable version of IPA module\n * \\param[in] maxVersion Maximum acceptable version of IPA module\n *\n * This function checks if this IPA module matches the requested \\a name\n * and the input version range.\n *\n * \\return True if the IPA module matches, or false otherwise\n */\nbool IPAModule::match(const char *name, uint32_t minVersion,\n\t\t      uint32_t maxVersion) const\n{\n\treturn info_.pipelineVersion >= minVersion &&\n\t       info_.pipelineVersion <= maxVersion &&\n\t       !strcmp(info_.name, name);\n}", "part_id": "module-match"}, {"text": "`createIPA`는 먼저 `module(name, minVersion, maxVersion)`으로 모듈을 검색하고, 모듈이 없으면 `nullptr`을 반환합니다. 모듈이 있으면 `isSignatureValid(m)`이 참일 때 `T::Threaded` 프록시를, 거짓일 때 `T::Isolated` 프록시를 생성합니다. 생성한 프록시의 `isValid()`가 거짓이면 오류를 기록하고 `nullptr`을 반환하며, 참이면 프록시를 반환합니다.", "evidence": ["selection"], "covers": ["selection"], "kind": "behavior", "quote": "auto proxy = [&]() -> std::unique_ptr<T> {\n\t\t\tif (isSignatureValid(m))\n\t\t\t\treturn std::make_unique<typename T::Threaded>(m, cm_);\n\t\t\telse\n\t\t\t\treturn std::make_unique<typename T::Isolated>(m, cm_);\n\t\t}();", "part_id": "proxy-selection"}, {"text": "`IPAManager::isSignatureValid`는 `HAVE_IPA_PUBKEY`가 활성화되지 않으면 `false`를 반환합니다. 활성화된 경우 `forceIsolation_`이 참이면 `false`를 반환하고, 그렇지 않으면 IPA 모듈 파일을 읽기 전용으로 엽니다. 파일을 열지 못하거나 파일 매핑 결과가 비어 있으면 `false`를 반환합니다. 두 단계를 통과하면 매핑된 데이터와 IPA 서명을 `pubKey_.verify`에 전달하고, 검사 결과를 로그에 기록한 뒤 그 결과를 반환합니다.", "evidence": ["signature"], "covers": ["selection"], "kind": "behavior", "quote": "bool IPAManager::isSignatureValid([[maybe_unused]] IPAModule *ipa) const\n{\n#if HAVE_IPA_PUBKEY\n\tif (forceIsolation_) {\n\t\tLOG(IPAManager, Debug)\n\t\t\t<< \"Isolation of IPA module \" << ipa->path()\n\t\t\t<< \" forced through configuration\";\n\t\treturn false;\n\t}", "part_id": "signature"}], "execution": [{"text": "Threaded `init` 템플릿은 전달된 매개변수로 `ipa_->init()`을 직접 호출합니다. 반환형이 `void`가 아니면 호출 결과를 `_ret`에 저장하고 반환하며, `void`이면 값을 반환하지 않습니다.", "evidence": ["init-branch"], "covers": ["execution"], "kind": "behavior", "quote": "{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);", "part_id": "init"}, {"text": "`init` 분기에서는 IPA 메서드를 호출한 뒤 `proxy_.moveToThread`에 스레드 객체 `thread_`의 주소를 전달합니다.", "evidence": ["init-branch"], "covers": ["execution"], "kind": "behavior", "quote": "proxy_.moveToThread(&thread_);", "part_id": "init-move"}, {"text": "Threaded `start` 템플릿 분기는 `state_`를 `ProxyRunning`으로 설정한 뒤 `thread_.start()`를 호출해 worker 스레드를 시작합니다. 이어서 `proxy_.invokeMethod()`로 `ThreadProxy::start`를 `ConnectionTypeBlocking` 연결 유형과 생성된 매개변수로 호출하고 그 반환값을 반환합니다.", "evidence": ["start-branch"], "covers": ["execution"], "kind": "behavior", "quote": "{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();", "part_id": "start"}, {"text": "`{{proxy_name}}Threaded`의 메서드에서 `init`, `start`, `stop`을 제외한 일반 동기 분기는 전달받은 인자로 `ipa_`의 같은 이름의 메서드를 직접 호출하고 그 반환값을 반환합니다.", "evidence": ["dispatch"], "covers": ["execution"], "kind": "behavior", "quote": "return proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}", "part_id": "sync"}, {"text": "비동기 메서드 분기는 `ASSERT` 매크로에 검사식 `state_ == ProxyRunning`을 전달합니다. 검사식이 거짓이면 `ASSERT`는 `Fatal` 수준의 오류 메시지를 기록하고 프로그램 실행을 중단합니다. `log.h`를 포함하기 전에 `NDEBUG`가 정의되어 있으면 `ASSERT`는 코드를 생성하지 않습니다.", "evidence": ["async-branch", "assert-contract"], "covers": ["execution"], "kind": "behavior", "quote": "{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}", "part_id": "async"}, {"text": "Threaded 비동기 분기에서 `proxy_.invokeMethod`는 `ThreadProxy` 메서드를 전달할 때 연결 유형으로 `ConnectionTypeQueued`를 사용합니다.", "evidence": ["async-branch"], "covers": ["execution"], "kind": "behavior", "quote": "{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}", "part_id": "async-dispatch"}, {"text": "`{{proxy_name}}Threaded` 생성자는 `ipam->load()`를 호출합니다. `load()`가 거짓을 반환하면 생성자에서 즉시 반환합니다.", "evidence": ["ctor-load"], "covers": ["execution"], "kind": "behavior", "quote": "if (!ipam->load())\n\t\treturn;", "part_id": "constructor"}, {"text": "`Threaded` 생성자는 `load()`가 성공한 경우에만 `createInterface()`를 호출합니다. 반환된 포인터가 없으면 `ipam->path()`를 포함한 오류를 기록하고 반환합니다. 포인터가 있으면 인터페이스를 `unique_ptr`로 소유하고 `proxy_.setIPA(ipa_.get())`에 포인터를 넘깁니다. 이어서 각 이벤트를 수신 객체 `this`의 해당 `Handler` 메서드에 `connect`하고 `valid_`를 `true`로 설정합니다.", "evidence": ["threaded"], "covers": ["execution"], "kind": "behavior", "quote": "IPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;\n\t}", "part_id": "constructor-interface"}, {"text": "`{{proxy_name}}Isolated` 생성자는 `resolvePath(\"{{module_name}}_ipa_proxy\")`로 워커 경로를 찾고, 경로가 비어 있으면 오류를 기록하고 반환합니다. 이어서 `IPCPipeUnixSocket`을 `ipam->path().c_str()`와 `proxyWorkerPath.c_str()` 인자로 생성하며, `isConnected()`가 거짓이면 오류를 기록하고 반환합니다. 연결에 성공하면 `recv.connect`에 수신 객체 `this`와 콜백 `&{{proxy_name}}Isolated::recvMessage`를 연결하고, `std::move`로 `ipc`의 소유권을 `ipc_`에 옮긴 뒤 `valid_`에 `true`를 저장합니다.", "evidence": ["isolated"], "covers": ["execution"], "kind": "behavior", "quote": "auto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}", "part_id": "isolated"}, {"text": "`IPAProxy::resolvePath`는 먼저 `execPaths_`를 순서대로 살펴보며 빈 디렉터리는 건너뛰고, `file`을 붙인 경로에 실행 권한이 있으면 그 경로를 반환합니다. 이후 `utils::libcameraBuildPath()`가 빈 문자열이 아니면 빌드 디렉터리의 `src/libcamera/proxy/worker`를 확인하고, 빈 문자열이면 설치 디렉터리 `IPA_PROXY_DIR`을 확인합니다. 선택한 디렉터리에서 실행 권한이 있는 경로를 찾으면 그 경로를 반환하고, 찾지 못하면 빈 문자열을 반환합니다.", "evidence": ["worker-path"], "covers": ["execution"], "kind": "behavior", "quote": "/* Try paths from the configuration first. */\n\tfor (const auto &dir : execPaths_) {\n\t\tif (dir.empty())\n\t\t\tcontinue;", "part_id": "worker"}, {"text": "`readyRead`는 소켓에서 페이로드를 수신하다가 오류가 나면 로그를 남기고 반환합니다. 수신한 데이터가 `IPCMessage::Header`보다 짧아도 로그를 남기고 반환합니다. 그다음 메시지의 `cookie`로 `callData_`에서 대기 항목을 찾고, 일치하는 항목이 있으면 페이로드를 응답으로 이동한 뒤 `done`을 `true`로 설정하고 반환합니다.", "evidence": ["receive-only"], "covers": ["execution"], "kind": "behavior", "quote": "auto callData = callData_.find(ipcMessage.header().cookie);\n\tif (callData != callData_.end()) {\n\t\t*callData->second.response = std::move(payload);\n\t\tcallData->second.done = true;\n\t\treturn;\n\t}", "part_id": "ipc"}, {"text": "`IPCPipeUnixSocket::sendAsync`는 `data.payload()`를 `socket_->send`로 전송하고 반환값을 `ret`에 저장합니다. `ret`이 0이 아니면 오류를 기록하고 `ret`을 반환합니다. 그렇지 않으면 0을 반환합니다.", "evidence": ["send-async"], "covers": ["execution"], "kind": "behavior", "quote": "int IPCPipeUnixSocket::sendAsync(const IPCMessage &data)\n{\n\tint ret = socket_->send(data.payload());\n\tif (ret) {\n\t\tLOG(IPCPipe, Error) << \"Failed to call async\";\n\t\treturn ret;\n\t}", "part_id": "ipc-async"}], "interface": [{"text": "`IPAIPU3Interface`는 `[async]` 메서드로 `queueRequest(frame, controls)`, `computeParams(frame, bufferId)`, `processStats(frame, frameTimestamp, bufferId, sensorControls)`를 선언합니다.", "evidence": ["ipu3-api"], "covers": ["interface"], "kind": "behavior", "quote": "[async] queueRequest(uint32 frame, libcamera.ControlList controls);\n\t[async] computeParams(uint32 frame, uint32 bufferId);\n\t[async] processStats(uint32 frame, int64 frameTimestamp,\n\t\t\t     uint32 bufferId, libcamera.ControlList sensorControls);\n};"}, {"text": "`IPAIPU3EventInterface`는 `paramsComputed(frame)`, `metadataReady(frame, metadata)`, `setSensorControls(frame, sensorControls, lensControls)`를 선언합니다.", "evidence": ["ipu3-api"], "covers": ["interface"], "kind": "behavior", "quote": "interface IPAIPU3EventInterface {\n\tsetSensorControls(uint32 frame, libcamera.ControlList sensorControls,\n\t\t\t  libcamera.ControlList lensControls);\n\tparamsComputed(uint32 frame);\n\tmetadataReady(uint32 frame, libcamera.ControlList metadata);\n};"}, {"text": "`IPARkISP1Interface`는 `[async]` 메서드로 `queueRequest(frame, reqControls)`, `computeParams(frame, bufferId)`, `processStats(frame, bufferId, sensorControls)`를 선언합니다.", "evidence": ["rkisp1-api"], "covers": ["interface"], "kind": "behavior", "quote": "[async] queueRequest(uint32 frame, libcamera.ControlList reqControls);\n\t[async] computeParams(uint32 frame, uint32 bufferId);\n\t[async] processStats(uint32 frame, uint32 bufferId,\n\t\t\t     libcamera.ControlList sensorControls);\n};"}, {"text": "`IPARkISP1EventInterface`는 `paramsComputed(frame, bytesused)`, `metadataReady(frame, metadata)`, `setSensorControls(frame, sensorControls)`를 선언합니다.", "evidence": ["rkisp1-api"], "covers": ["interface"], "kind": "behavior", "quote": "interface IPARkISP1EventInterface {\n\tparamsComputed(uint32 frame, uint32 bytesused);\n\tsetSensorControls(uint32 frame, libcamera.ControlList sensorControls);\n\tmetadataReady(uint32 frame, libcamera.ControlList metadata);\n};"}], "lifetime": [{"text": "호출자는 유효한 모듈에서 `load()`를 한 번 성공한 뒤 필요한 `IPAInterface` 인스턴스 수만큼 `createInterface()`를 호출할 수 있습니다.", "evidence": ["load"], "covers": ["lifetime"], "kind": "behavior", "quote": "\\brief Load the IPA implementation factory from the shared object\n *\n * The IPA module shared object implements an IPAInterface object to be used\n * by pipeline handlers. This function loads the factory function from the\n * shared object. Later, createInterface() can be called to instantiate the\n * IPAInterface.\n *\n * This function only needs to be called successfully once, after which\n * createInterface() can be called as many times as IPAInterface instances are\n * needed.\n *\n * Calling this function on an invalid module (as returned by isValid()) is\n * an error.\n *\n * \\return True if load was successful, or already loaded, and false otherwise\n */\nbool IPAModule::load()\n{\n\tif (!valid_)\n\t\treturn false;"}, {"text": "Threaded 프록시의 `stop`은 먼저 상태가 `ProxyStopping`이 아닌지 단언하고, `ProxyRunning`이 아니면 반환합니다. 실행 중이면 상태를 `ProxyStopping`으로 바꾸고 `ThreadProxy::stop`을 `ConnectionTypeBlocking`으로 호출한 다음 `thread_.exit()`와 `thread_.wait()`를 순서대로 호출합니다. 이어 현재 스레드에서 이 프록시의 `InvokeMessage`를 디스패치하고 상태를 `ProxyStopped`로 바꿉니다.", "evidence": ["thread-stop", "threaded"], "covers": ["lifetime"], "kind": "behavior", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;"}, {"text": "Isolated 프록시의 소멸자는 `ipc_`가 있으면 `Exit` 명령과 증가 전의 `seq_` 값으로 헤더를 만들고, 해당 메시지를 `sendAsync()`로 보냅니다.", "evidence": ["isolated-dtor-only"], "covers": ["lifetime"], "kind": "behavior", "quote": "{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}"}], "errors": [{"text": "`IPAModule::load()`는 `valid_`가 거짓이면 `false`를 반환하고, 이미 `loaded_`이면 `true`를 반환합니다. 이어서 `dlopen`이 실패하면 오류를 기록하고 `false`를 반환합니다. `dlsym`으로 `ipaCreate`를 찾지 못하면 오류를 기록하고 `dlclose`로 핸들을 닫은 뒤 `dlHandle_`을 `nullptr`로 설정하고 `false`를 반환합니다. 심벌을 찾으면 `ipaCreate_`에 팩토리를 저장하고 `loaded_`를 `true`로 설정한 뒤 `true`를 반환합니다.", "evidence": ["load"], "covers": ["errors"], "kind": "behavior", "quote": "\\brief Load the IPA implementation factory from the shared object\n *\n * The IPA module shared object implements an IPAInterface object to be used\n * by pipeline handlers. This function loads the factory function from the\n * shared object. Later, createInterface() can be called to instantiate the\n * IPAInterface.\n *\n * This function only needs to be called successfully once, after which\n * createInterface() can be called as many times as IPAInterface instances are\n * needed.\n *\n * Calling this function on an invalid module (as returned by isValid()) is\n * an error.\n *\n * \\return True if load was successful, or already loaded, and false otherwise\n */\nbool IPAModule::load()\n{\n\tif (!valid_)\n\t\treturn false;", "part_id": "module-load"}, {"text": "`IPAModule::createInterface()`는 모듈이 유효하지 않거나 로드되지 않았으면 `nullptr`을 반환합니다. 두 조건을 모두 통과하면 `ipaCreate_()`를 호출하고 그 반환값을 반환합니다.", "evidence": ["interface-only"], "covers": ["errors"], "kind": "behavior", "quote": "IPAInterface *IPAModule::createInterface()\n{\n\tif (!valid_ || !loaded_)\n\t\treturn nullptr;", "part_id": "interface-create"}, {"text": "`IPCPipeUnixSocket::sendSync`는 입력 페이로드, 응답 저장 위치, 입력 헤더의 쿠키로 `call`을 호출하고 반환값을 검사합니다. 반환값이 0이 아니면 오류를 기록하고 그 값을 그대로 반환합니다. 성공하면 `out`이 널이 아닐 때 응답으로 만든 `IPCMessage`를 `out`에 저장하고 0을 반환합니다.", "evidence": ["sync-wrapper"], "covers": ["errors"], "kind": "behavior", "quote": "int ret = call(in.payload(), &response, in.header().cookie);\n\tif (ret) {\n\t\tLOG(IPCPipe, Error) << \"Failed to call sync\";\n\t\treturn ret;\n\t}", "part_id": "sync-result"}, {"text": "`IPCPipeUnixSocket::call`은 `cookie`를 키로 하고 `response`와 `false`를 값으로 하여 `callData_`에 삽입을 시도합니다. 이 함수는 삽입 성공 여부를 검사하지 않고 결과의 `first` 필드를 `iter`로 사용하여 해당 항목을 가리킵니다. 소켓의 `send`에는 반복자가 아닌 `message`를 전달하며, 송신이 실패하면 `erase`로 `iter`가 가리키는 항목을 지우고 송신의 반환값을 반환합니다.", "evidence": ["sync-call"], "covers": ["errors"], "kind": "behavior", "quote": "ret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}", "part_id": "sync-send"}, {"text": "`IPCPipeUnixSocket::call`은 타이머를 `2000ms`로 시작하고 항목의 `done`이 참이 될 때까지 기다립니다. 대기 중 타이머가 실행 중이면 현재 스레드의 이벤트 디스패처에서 `processEvents()`를 호출합니다. 타이머가 만료되면 `erase`로 항목을 지우고 `-ETIMEDOUT`을 반환합니다. `done`이 참이 되어 정상 완료되면 항목을 `erase`로 지우고 0을 반환합니다.", "evidence": ["sync-call"], "covers": ["errors"], "kind": "behavior", "quote": "/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}", "part_id": "sync-timeout"}]}, "topic_inputs": {"selection": "ccc3ffb33a923bf94f705e96b7c7ab1f4621a33ae0ba27996ff1bb96ea0bd2d7", "execution": "f2e54776e1825aea23bd96b2f97c2bfefa4892dbdedf35dd9094972947f53bd6", "interface": "61103b4e788aae4a5eb9b73a2c4feba248da91fded8677f7e34b668d764a5145", "lifetime": "7b69b4bbb50416bd396dc91cac5a61245071e3223ebdaf7f18683459edfb043d", "errors": "472a1074408769c0a37748408a09c09cea522a17a9c2965d711896308e19a086"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["selection", "execution", "interface", "lifetime", "errors"], "topic_agents": {"selection": "cli/codex/gpt-6.1-terra", "execution": "cli/codex/gpt-6.1-terra", "interface": "cli/codex/gpt-6.1-terra", "lifetime": "cli/codex/gpt-6.1-terra", "errors": "cli/codex/gpt-6.1-terra"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "367d18b95f8f0d01a15ae0f4d1b70f7e13e4d0298df4215e2c449ac4905db6f9", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "d0f7ab4c48fcf52409935931eb9b93aacd48af4b19e9bb816fa496f1214fdb2f", "answer_contracts": "a39c9a8818afc47e059141d486337c0f12a7fd34319e2b6f7674fc428bc83e2b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "050c20aa2fdcceae10c6275fbb5f850f616ab5051bb67ccbcb4a204877a238d9", "explanation": "69bcaa207ef39d20f6a47ac201c3edf119f59b333e85131dea1bce85eef4006b", "design_response": "a7c199bc52bcc0e749ef01186e50bca98107473d5c82e2248712f465d02e1e69", "design_validation": "92ddb9a65c909173ff4c7cb627dff83e71c10c8258c51344ef0eb1a7a023937f"}, "validation_model": "db6c5bf57ead3ade75be2621f553363aac6222c51b55401a5bcb2b7116c69a06", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "b87a84b1bc31079837dc4dc4527ce02c9dc2cbc3a26ff7e99e0872941d213995"}, "checkpoint_units": [{"checkpoint": "0a3158b55de93bc2ab3ce85ac471dbaf069b1e8c2dae1a596f3dfceec87fa834.json", "topic": "selection", "part": "search-paths", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/001.receipt.json", "bca74b4f358141cfb035b84f56816a3b/002.receipt.json"]}, {"checkpoint": "9cbabe46b7d6a1983bf2a4de03bbf137c0866f32261c4ca013fe950be9c9a814.json", "topic": "selection", "part": "module-match", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/003.receipt.json", "bca74b4f358141cfb035b84f56816a3b/004.receipt.json"]}, {"checkpoint": "2054949adbdc02e9eadc65b9d1e481fb661ee46c7ad9af0b68e8dbc13d63d28e.json", "topic": "selection", "part": "proxy-selection", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/005.receipt.json", "bca74b4f358141cfb035b84f56816a3b/006.receipt.json"]}, {"checkpoint": "c3ba4cc84ee50d0ee60969e0419a5e7e40822c76b70cfb1d7041bd0f5212bac4.json", "topic": "selection", "part": "signature", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/007.receipt.json", "bca74b4f358141cfb035b84f56816a3b/008.receipt.json"]}, {"checkpoint": "e3ec1499c7542f65fd1346f79944e8e2f54ee430a8a24fd6f1a96d7a99223577.json", "topic": "execution", "part": "init", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/009.receipt.json", "bca74b4f358141cfb035b84f56816a3b/010.receipt.json"]}, {"checkpoint": "7e6fff82984744b784591457ec5255dfea01d68ec79a3f782f6731cb2da42ba0.json", "topic": "execution", "part": "init-move", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/011.receipt.json", "bca74b4f358141cfb035b84f56816a3b/012.receipt.json"]}, {"checkpoint": "47feae35bb0cb11d53c9698a377691e25cc980074545f41aca8764770fe8fe7b.json", "topic": "execution", "part": "start", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/013.receipt.json", "bca74b4f358141cfb035b84f56816a3b/014.receipt.json"]}, {"checkpoint": "e8d523c2fe8ddcc60332b359a8984d075ff1c9ef33787b0dac9a51e9d9d4d627.json", "topic": "execution", "part": "sync", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/015.receipt.json", "bca74b4f358141cfb035b84f56816a3b/016.receipt.json"]}, {"checkpoint": "04cc048a315545057be52b4d31a7aa3a09c87bd60d257147989ab1195dd55232.json", "topic": "execution", "part": "async", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["a28e4ac763bb49c6b220cd43599dfaf9/001.receipt.json", "a28e4ac763bb49c6b220cd43599dfaf9/002.receipt.json"]}, {"checkpoint": "0b018738d0579429f9bcb71675da54cdd59e06d0d9b9968ff5ecd01eb0aa0d0d.json", "topic": "execution", "part": "async-dispatch", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/019.receipt.json", "bca74b4f358141cfb035b84f56816a3b/020.receipt.json"]}, {"checkpoint": "012dd4bf852396422a9282de5f2efc9b807dee7b0134daa440d194ab58e7b743.json", "topic": "execution", "part": "constructor", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/021.receipt.json", "bca74b4f358141cfb035b84f56816a3b/022.receipt.json"]}, {"checkpoint": "1b8648f9108d5e958933625844708b573f1bd5801c01bb9273d5a181496e3b2f.json", "topic": "execution", "part": "constructor-interface", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["a28e4ac763bb49c6b220cd43599dfaf9/003.receipt.json", "a28e4ac763bb49c6b220cd43599dfaf9/004.receipt.json"]}, {"checkpoint": "350f079a31238cb96ffebba17f43728b564edfa323da24ad463f60edf8d9f803.json", "topic": "execution", "part": "isolated", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["a28e4ac763bb49c6b220cd43599dfaf9/005.receipt.json", "a28e4ac763bb49c6b220cd43599dfaf9/006.receipt.json"]}, {"checkpoint": "6745269b4e8e3f37aa6101ea5a6dfe777fe98b603abf199219289fc1b5ff9ccc.json", "topic": "execution", "part": "worker", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/028.receipt.json", "bca74b4f358141cfb035b84f56816a3b/029.receipt.json", "bca74b4f358141cfb035b84f56816a3b/030.receipt.json"]}, {"checkpoint": "d222cefe66955b04e22b2df28a2c85791561142be767fc3f86bf03b95ec552e4.json", "topic": "execution", "part": "ipc", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/031.receipt.json", "bca74b4f358141cfb035b84f56816a3b/032.receipt.json"]}, {"checkpoint": "21b0fc86ea57c8fb989fd98160f00b1491a228f87dba22aa4b2ed80c9ed866a9.json", "topic": "execution", "part": "ipc-async", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/033.receipt.json", "bca74b4f358141cfb035b84f56816a3b/034.receipt.json"]}, {"checkpoint": "4614a2ee267450bc2a2dcb94293bd27c539f98cdb0e71cfb4bc74b64b63eb959.json", "topic": "interface", "part": null, "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/035.receipt.json", "bca74b4f358141cfb035b84f56816a3b/036.receipt.json"]}, {"checkpoint": "ac82000a9f100b24a081f01f9e3e2540e1629bcc0cce6ccf945fd2661a91e805.json", "topic": "lifetime", "part": null, "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/037.receipt.json", "bca74b4f358141cfb035b84f56816a3b/038.receipt.json"]}, {"checkpoint": "16b1e25f5de2da1f282bc9f67ddd2c766410ce3ae4e13e33c353a697029a1d7a.json", "topic": "errors", "part": "module-load", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/039.receipt.json", "bca74b4f358141cfb035b84f56816a3b/040.receipt.json"]}, {"checkpoint": "7fd168a432d2448aca45fed34f62e4e3982a8e4ae0dcad010117439d6b0e9652.json", "topic": "errors", "part": "interface-create", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/041.receipt.json", "bca74b4f358141cfb035b84f56816a3b/042.receipt.json"]}, {"checkpoint": "cc84fed9e39b48be16c7bfcf9f4e5731dbeb02626b412567c08c871aaee324a8.json", "topic": "errors", "part": "sync-result", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/043.receipt.json", "bca74b4f358141cfb035b84f56816a3b/044.receipt.json"]}, {"checkpoint": "ba1f1668a94d58bb959c9ea4c8103564146db95c4335e94fa017cd76b3762499.json", "topic": "errors", "part": "sync-send", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/045.receipt.json", "bca74b4f358141cfb035b84f56816a3b/046.receipt.json"]}, {"checkpoint": "ea9641dde5aaf8c18bc0ad72d38463e652ed162cd0b9baf11367362fb07a1bce.json", "topic": "errors", "part": "sync-timeout", "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["bca74b4f358141cfb035b84f56816a3b/047.receipt.json", "bca74b4f358141cfb035b84f56816a3b/048.receipt.json"]}], "body_sha256": "184387e60c8396c9b9c13e8478ad7b16ee00b3cd6440e011d70cec827edce129"}
generated_visuals: {"schema": 1, "records": {"interface-creation-outcomes": {"input_fingerprint": "913a45200c3497e98b8f129011e89259ce5173b2379f74de9de69e14838676ba", "draft": {"nodes": [{"id": "load", "symbol": "load", "label": "생성자가 ipam의 load를 호출하고 결과를 확인합니다.", "label_en": "The constructor calls load on ipam and checks the result.", "shape": "decision", "quote_ids": ["threaded:0"]}, {"id": "load_return", "symbol": "return", "label": "생성자가 즉시 반환합니다.", "label_en": "The constructor returns immediately.", "shape": "box", "quote_ids": ["threaded:0"]}, {"id": "interface", "symbol": "createInterface", "label": "생성자가 createInterface를 호출하고 ipai를 확인합니다.", "label_en": "The constructor calls createInterface and checks ipai.", "shape": "decision", "quote_ids": ["threaded:0"]}, {"id": "error_return", "symbol": "LOG", "label": "생성자가 오류를 기록하고 반환합니다.", "label_en": "The constructor logs an error and returns.", "shape": "box", "quote_ids": ["threaded:0"]}, {"id": "own", "symbol": "ipa_", "label": "ipa_가 변환한 인터페이스를 std::unique_ptr로 소유합니다.", "label_en": "ipa_ owns the cast interface through a std::unique_ptr.", "shape": "process", "quote_ids": ["threaded:0"]}, {"id": "pointer", "symbol": "setIPA", "label": "생성자가 ipa_.get()의 포인터를 proxy_.setIPA에 넘깁니다.", "label_en": "The constructor passes the pointer from ipa_.get() to proxy_.setIPA.", "shape": "process", "quote_ids": ["threaded:0"]}, {"id": "events", "symbol": "connect", "label": "생성자가 각 인터페이스 이벤트를 this의 해당 Handler에 connect로 연결합니다.", "label_en": "The constructor uses connect to link each interface event to its corresponding Handler on this.", "shape": "process", "quote_ids": ["threaded:0"]}, {"id": "valid", "symbol": "valid_", "label": "생성자가 valid_에 true를 저장하고 정상적으로 마칩니다.", "label_en": "The constructor stores true in valid_ and finishes normally.", "shape": "box", "quote_ids": ["threaded:0"]}], "edges": [{"from": "load", "to": "load_return", "label": "조건이 참이면 즉시 반환합니다.", "label_en": "If the condition is true, the constructor returns immediately.", "condition_ref": "c1:true", "quote_ids": ["threaded:0"]}, {"from": "load", "to": "interface", "label": "조건이 거짓이면 createInterface를 호출합니다.", "label_en": "If the condition is false, the constructor calls createInterface.", "condition_ref": "c1:false", "quote_ids": ["threaded:0"]}, {"from": "interface", "to": "error_return", "label": "조건이 참이면 오류를 기록하고 반환합니다.", "label_en": "If the condition is true, the constructor logs an error and returns.", "condition_ref": "c0:true", "quote_ids": ["threaded:0"]}, {"from": "interface", "to": "own", "label": "조건이 거짓이면 ipa_가 인터페이스를 소유합니다.", "label_en": "If the condition is false, ipa_ owns the interface.", "condition_ref": "c0:false", "quote_ids": ["threaded:0"]}, {"from": "own", "to": "pointer", "label": "소유한 인터페이스의 포인터를 setIPA에 넘깁니다.", "label_en": "The constructor passes a pointer to the owned interface to setIPA.", "condition_ref": "always", "quote_ids": ["threaded:0"]}, {"from": "pointer", "to": "events", "label": "setIPA가 정상적으로 반환하면 각 이벤트를 연결합니다.", "label_en": "After setIPA returns normally, the constructor connects each event.", "condition_ref": "always", "quote_ids": ["threaded:0"]}, {"from": "events", "to": "valid", "label": "이벤트 연결을 마치면 valid_에 true를 저장합니다.", "label_en": "After connecting the events, the constructor stores true in valid_.", "condition_ref": "always", "quote_ids": ["threaded:0"]}]}, "graph": {"id": "interface-creation-outcomes", "topic": "execution", "kind": "flow", "title": "Threaded 생성자의 인터페이스 유지", "question": "Threaded 생성자는 load와 createInterface 결과에 따라 언제 반환하며 인터페이스를 어떻게 보유·연결합니까?", "condition_display": "inline", "nodes": [{"id": "load", "label": "생성자가 ipam의 load를 호출하고 결과를 확인합니다.", "label_en": "The constructor calls load on ipam and checks the result.", "shape": "decision", "evidence": [{"source": "execution/threaded", "sha256": "af4b12c81ffee2e9979c01a7e7eb188f5568d258ba03e522b60a3608dc226abd", "quote": "{{proxy_name}}Threaded::{{proxy_name}}Threaded(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm), thread_(\"{{proxy_name}}\")\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in thread: loading IPA from \"\n\t\t<< ipam->path();\n\n\tif (!ipam->load())\n\t\treturn;\n\n\tIPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;\n\t}\n\n\tipa_ = std::unique_ptr<{{interface_name}}>(static_cast<{{interface_name}} *>(ipai));\n\tproxy_.setIPA(ipa_.get());\n\n{% for method in interface_event.methods %}\n\tipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);\n{%- endfor %}\n\n\tvalid_ = true;\n}\n\n{{proxy_name}}Threaded::~{{proxy_name}}Threaded() = default;\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method)}}\n{\n{%- if method.mojom_name == \"stop\" %}\n\t{{proxy_funcs.stop_thread_body()}}\n{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n\n\tproxy_.moveToThread(&thread_);\n\n\treturn {{ \"_ret\" if method|method_return_value != \"void\" }};\n{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();\n\n\treturn proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}\n\n{% for method in interface_event.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method, \"Handler\")}}\n{\n\tASSERT(state_ != ProxyStopped);\n\t{{method.mojom_name}}.emit({{method.parameters|params_comma_sep}});\n}\n{% endfor %}\n\n/* ========================================================================== */"}]}, {"id": "load_return", "label": "생성자가 즉시 반환합니다.", "label_en": "The constructor returns immediately.", "shape": "box", "evidence": [{"source": "execution/threaded", "sha256": "af4b12c81ffee2e9979c01a7e7eb188f5568d258ba03e522b60a3608dc226abd", "quote": "{{proxy_name}}Threaded::{{proxy_name}}Threaded(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm), thread_(\"{{proxy_name}}\")\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in thread: loading IPA from \"\n\t\t<< ipam->path();\n\n\tif (!ipam->load())\n\t\treturn;\n\n\tIPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;\n\t}\n\n\tipa_ = std::unique_ptr<{{interface_name}}>(static_cast<{{interface_name}} *>(ipai));\n\tproxy_.setIPA(ipa_.get());\n\n{% for method in interface_event.methods %}\n\tipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);\n{%- endfor %}\n\n\tvalid_ = true;\n}\n\n{{proxy_name}}Threaded::~{{proxy_name}}Threaded() = default;\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method)}}\n{\n{%- if method.mojom_name == \"stop\" %}\n\t{{proxy_funcs.stop_thread_body()}}\n{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n\n\tproxy_.moveToThread(&thread_);\n\n\treturn {{ \"_ret\" if method|method_return_value != \"void\" }};\n{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();\n\n\treturn proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}\n\n{% for method in interface_event.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method, \"Handler\")}}\n{\n\tASSERT(state_ != ProxyStopped);\n\t{{method.mojom_name}}.emit({{method.parameters|params_comma_sep}});\n}\n{% endfor %}\n\n/* ========================================================================== */"}]}, {"id": "interface", "label": "생성자가 createInterface를 호출하고 ipai를 확인합니다.", "label_en": "The constructor calls createInterface and checks ipai.", "shape": "decision", "evidence": [{"source": "execution/threaded", "sha256": "af4b12c81ffee2e9979c01a7e7eb188f5568d258ba03e522b60a3608dc226abd", "quote": "{{proxy_name}}Threaded::{{proxy_name}}Threaded(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm), thread_(\"{{proxy_name}}\")\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in thread: loading IPA from \"\n\t\t<< ipam->path();\n\n\tif (!ipam->load())\n\t\treturn;\n\n\tIPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;\n\t}\n\n\tipa_ = std::unique_ptr<{{interface_name}}>(static_cast<{{interface_name}} *>(ipai));\n\tproxy_.setIPA(ipa_.get());\n\n{% for method in interface_event.methods %}\n\tipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);\n{%- endfor %}\n\n\tvalid_ = true;\n}\n\n{{proxy_name}}Threaded::~{{proxy_name}}Threaded() = default;\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method)}}\n{\n{%- if method.mojom_name == \"stop\" %}\n\t{{proxy_funcs.stop_thread_body()}}\n{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n\n\tproxy_.moveToThread(&thread_);\n\n\treturn {{ \"_ret\" if method|method_return_value != \"void\" }};\n{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();\n\n\treturn proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}\n\n{% for method in interface_event.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method, \"Handler\")}}\n{\n\tASSERT(state_ != ProxyStopped);\n\t{{method.mojom_name}}.emit({{method.parameters|params_comma_sep}});\n}\n{% endfor %}\n\n/* ========================================================================== */"}]}, {"id": "error_return", "label": "생성자가 오류를 기록하고 반환합니다.", "label_en": "The constructor logs an error and returns.", "shape": "box", "evidence": [{"source": "execution/threaded", "sha256": "af4b12c81ffee2e9979c01a7e7eb188f5568d258ba03e522b60a3608dc226abd", "quote": "{{proxy_name}}Threaded::{{proxy_name}}Threaded(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm), thread_(\"{{proxy_name}}\")\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in thread: loading IPA from \"\n\t\t<< ipam->path();\n\n\tif (!ipam->load())\n\t\treturn;\n\n\tIPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;\n\t}\n\n\tipa_ = std::unique_ptr<{{interface_name}}>(static_cast<{{interface_name}} *>(ipai));\n\tproxy_.setIPA(ipa_.get());\n\n{% for method in interface_event.methods %}\n\tipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);\n{%- endfor %}\n\n\tvalid_ = true;\n}\n\n{{proxy_name}}Threaded::~{{proxy_name}}Threaded() = default;\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method)}}\n{\n{%- if method.mojom_name == \"stop\" %}\n\t{{proxy_funcs.stop_thread_body()}}\n{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n\n\tproxy_.moveToThread(&thread_);\n\n\treturn {{ \"_ret\" if method|method_return_value != \"void\" }};\n{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();\n\n\treturn proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}\n\n{% for method in interface_event.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method, \"Handler\")}}\n{\n\tASSERT(state_ != ProxyStopped);\n\t{{method.mojom_name}}.emit({{method.parameters|params_comma_sep}});\n}\n{% endfor %}\n\n/* ========================================================================== */"}]}, {"id": "own", "label": "ipa_가 변환한 인터페이스를 std::unique_ptr로 소유합니다.", "label_en": "ipa_ owns the cast interface through a std::unique_ptr.", "shape": "box", "evidence": [{"source": "execution/threaded", "sha256": "af4b12c81ffee2e9979c01a7e7eb188f5568d258ba03e522b60a3608dc226abd", "quote": "{{proxy_name}}Threaded::{{proxy_name}}Threaded(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm), thread_(\"{{proxy_name}}\")\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in thread: loading IPA from \"\n\t\t<< ipam->path();\n\n\tif (!ipam->load())\n\t\treturn;\n\n\tIPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;\n\t}\n\n\tipa_ = std::unique_ptr<{{interface_name}}>(static_cast<{{interface_name}} *>(ipai));\n\tproxy_.setIPA(ipa_.get());\n\n{% for method in interface_event.methods %}\n\tipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);\n{%- endfor %}\n\n\tvalid_ = true;\n}\n\n{{proxy_name}}Threaded::~{{proxy_name}}Threaded() = default;\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method)}}\n{\n{%- if method.mojom_name == \"stop\" %}\n\t{{proxy_funcs.stop_thread_body()}}\n{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n\n\tproxy_.moveToThread(&thread_);\n\n\treturn {{ \"_ret\" if method|method_return_value != \"void\" }};\n{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();\n\n\treturn proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}\n\n{% for method in interface_event.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method, \"Handler\")}}\n{\n\tASSERT(state_ != ProxyStopped);\n\t{{method.mojom_name}}.emit({{method.parameters|params_comma_sep}});\n}\n{% endfor %}\n\n/* ========================================================================== */"}]}, {"id": "pointer", "label": "생성자가 ipa_.get()의 포인터를 proxy_.setIPA에 넘깁니다.", "label_en": "The constructor passes the pointer from ipa_.get() to proxy_.setIPA.", "shape": "box", "evidence": [{"source": "execution/threaded", "sha256": "af4b12c81ffee2e9979c01a7e7eb188f5568d258ba03e522b60a3608dc226abd", "quote": "{{proxy_name}}Threaded::{{proxy_name}}Threaded(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm), thread_(\"{{proxy_name}}\")\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in thread: loading IPA from \"\n\t\t<< ipam->path();\n\n\tif (!ipam->load())\n\t\treturn;\n\n\tIPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;\n\t}\n\n\tipa_ = std::unique_ptr<{{interface_name}}>(static_cast<{{interface_name}} *>(ipai));\n\tproxy_.setIPA(ipa_.get());\n\n{% for method in interface_event.methods %}\n\tipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);\n{%- endfor %}\n\n\tvalid_ = true;\n}\n\n{{proxy_name}}Threaded::~{{proxy_name}}Threaded() = default;\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method)}}\n{\n{%- if method.mojom_name == \"stop\" %}\n\t{{proxy_funcs.stop_thread_body()}}\n{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n\n\tproxy_.moveToThread(&thread_);\n\n\treturn {{ \"_ret\" if method|method_return_value != \"void\" }};\n{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();\n\n\treturn proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}\n\n{% for method in interface_event.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method, \"Handler\")}}\n{\n\tASSERT(state_ != ProxyStopped);\n\t{{method.mojom_name}}.emit({{method.parameters|params_comma_sep}});\n}\n{% endfor %}\n\n/* ========================================================================== */"}]}, {"id": "events", "label": "생성자가 각 인터페이스 이벤트를 this의 해당 Handler에 connect로 연결합니다.", "label_en": "The constructor uses connect to link each interface event to its corresponding Handler on this.", "shape": "box", "evidence": [{"source": "execution/threaded", "sha256": "af4b12c81ffee2e9979c01a7e7eb188f5568d258ba03e522b60a3608dc226abd", "quote": "{{proxy_name}}Threaded::{{proxy_name}}Threaded(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm), thread_(\"{{proxy_name}}\")\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in thread: loading IPA from \"\n\t\t<< ipam->path();\n\n\tif (!ipam->load())\n\t\treturn;\n\n\tIPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;\n\t}\n\n\tipa_ = std::unique_ptr<{{interface_name}}>(static_cast<{{interface_name}} *>(ipai));\n\tproxy_.setIPA(ipa_.get());\n\n{% for method in interface_event.methods %}\n\tipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);\n{%- endfor %}\n\n\tvalid_ = true;\n}\n\n{{proxy_name}}Threaded::~{{proxy_name}}Threaded() = default;\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method)}}\n{\n{%- if method.mojom_name == \"stop\" %}\n\t{{proxy_funcs.stop_thread_body()}}\n{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n\n\tproxy_.moveToThread(&thread_);\n\n\treturn {{ \"_ret\" if method|method_return_value != \"void\" }};\n{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();\n\n\treturn proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}\n\n{% for method in interface_event.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method, \"Handler\")}}\n{\n\tASSERT(state_ != ProxyStopped);\n\t{{method.mojom_name}}.emit({{method.parameters|params_comma_sep}});\n}\n{% endfor %}\n\n/* ========================================================================== */"}]}, {"id": "valid", "label": "생성자가 valid_에 true를 저장하고 정상적으로 마칩니다.", "label_en": "The constructor stores true in valid_ and finishes normally.", "shape": "box", "evidence": [{"source": "execution/threaded", "sha256": "af4b12c81ffee2e9979c01a7e7eb188f5568d258ba03e522b60a3608dc226abd", "quote": "{{proxy_name}}Threaded::{{proxy_name}}Threaded(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm), thread_(\"{{proxy_name}}\")\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in thread: loading IPA from \"\n\t\t<< ipam->path();\n\n\tif (!ipam->load())\n\t\treturn;\n\n\tIPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;\n\t}\n\n\tipa_ = std::unique_ptr<{{interface_name}}>(static_cast<{{interface_name}} *>(ipai));\n\tproxy_.setIPA(ipa_.get());\n\n{% for method in interface_event.methods %}\n\tipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);\n{%- endfor %}\n\n\tvalid_ = true;\n}\n\n{{proxy_name}}Threaded::~{{proxy_name}}Threaded() = default;\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method)}}\n{\n{%- if method.mojom_name == \"stop\" %}\n\t{{proxy_funcs.stop_thread_body()}}\n{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n\n\tproxy_.moveToThread(&thread_);\n\n\treturn {{ \"_ret\" if method|method_return_value != \"void\" }};\n{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();\n\n\treturn proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}\n\n{% for method in interface_event.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method, \"Handler\")}}\n{\n\tASSERT(state_ != ProxyStopped);\n\t{{method.mojom_name}}.emit({{method.parameters|params_comma_sep}});\n}\n{% endfor %}\n\n/* ========================================================================== */"}]}], "edges": [{"from": "load", "to": "load_return", "label": "조건이 참이면 즉시 반환합니다. · !ipam->load() [true]", "label_en": "If the condition is true, the constructor returns immediately. · !ipam->load() [true]", "evidence": [{"source": "execution/threaded", "sha256": "af4b12c81ffee2e9979c01a7e7eb188f5568d258ba03e522b60a3608dc226abd", "quote": "{{proxy_name}}Threaded::{{proxy_name}}Threaded(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm), thread_(\"{{proxy_name}}\")\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in thread: loading IPA from \"\n\t\t<< ipam->path();\n\n\tif (!ipam->load())\n\t\treturn;\n\n\tIPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;\n\t}\n\n\tipa_ = std::unique_ptr<{{interface_name}}>(static_cast<{{interface_name}} *>(ipai));\n\tproxy_.setIPA(ipa_.get());\n\n{% for method in interface_event.methods %}\n\tipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);\n{%- endfor %}\n\n\tvalid_ = true;\n}\n\n{{proxy_name}}Threaded::~{{proxy_name}}Threaded() = default;\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method)}}\n{\n{%- if method.mojom_name == \"stop\" %}\n\t{{proxy_funcs.stop_thread_body()}}\n{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n\n\tproxy_.moveToThread(&thread_);\n\n\treturn {{ \"_ret\" if method|method_return_value != \"void\" }};\n{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();\n\n\treturn proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}\n\n{% for method in interface_event.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method, \"Handler\")}}\n{\n\tASSERT(state_ != ProxyStopped);\n\t{{method.mojom_name}}.emit({{method.parameters|params_comma_sep}});\n}\n{% endfor %}\n\n/* ========================================================================== */"}]}, {"from": "load", "to": "interface", "label": "조건이 거짓이면 createInterface를 호출합니다. · !ipam->load() [false]", "label_en": "If the condition is false, the constructor calls createInterface. · !ipam->load() [false]", "evidence": [{"source": "execution/threaded", "sha256": "af4b12c81ffee2e9979c01a7e7eb188f5568d258ba03e522b60a3608dc226abd", "quote": "{{proxy_name}}Threaded::{{proxy_name}}Threaded(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm), thread_(\"{{proxy_name}}\")\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in thread: loading IPA from \"\n\t\t<< ipam->path();\n\n\tif (!ipam->load())\n\t\treturn;\n\n\tIPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;\n\t}\n\n\tipa_ = std::unique_ptr<{{interface_name}}>(static_cast<{{interface_name}} *>(ipai));\n\tproxy_.setIPA(ipa_.get());\n\n{% for method in interface_event.methods %}\n\tipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);\n{%- endfor %}\n\n\tvalid_ = true;\n}\n\n{{proxy_name}}Threaded::~{{proxy_name}}Threaded() = default;\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method)}}\n{\n{%- if method.mojom_name == \"stop\" %}\n\t{{proxy_funcs.stop_thread_body()}}\n{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n\n\tproxy_.moveToThread(&thread_);\n\n\treturn {{ \"_ret\" if method|method_return_value != \"void\" }};\n{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();\n\n\treturn proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}\n\n{% for method in interface_event.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method, \"Handler\")}}\n{\n\tASSERT(state_ != ProxyStopped);\n\t{{method.mojom_name}}.emit({{method.parameters|params_comma_sep}});\n}\n{% endfor %}\n\n/* ========================================================================== */"}]}, {"from": "interface", "to": "error_return", "label": "조건이 참이면 오류를 기록하고 반환합니다. · !ipai [true]", "label_en": "If the condition is true, the constructor logs an error and returns. · !ipai [true]", "evidence": [{"source": "execution/threaded", "sha256": "af4b12c81ffee2e9979c01a7e7eb188f5568d258ba03e522b60a3608dc226abd", "quote": "{{proxy_name}}Threaded::{{proxy_name}}Threaded(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm), thread_(\"{{proxy_name}}\")\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in thread: loading IPA from \"\n\t\t<< ipam->path();\n\n\tif (!ipam->load())\n\t\treturn;\n\n\tIPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;\n\t}\n\n\tipa_ = std::unique_ptr<{{interface_name}}>(static_cast<{{interface_name}} *>(ipai));\n\tproxy_.setIPA(ipa_.get());\n\n{% for method in interface_event.methods %}\n\tipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);\n{%- endfor %}\n\n\tvalid_ = true;\n}\n\n{{proxy_name}}Threaded::~{{proxy_name}}Threaded() = default;\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method)}}\n{\n{%- if method.mojom_name == \"stop\" %}\n\t{{proxy_funcs.stop_thread_body()}}\n{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n\n\tproxy_.moveToThread(&thread_);\n\n\treturn {{ \"_ret\" if method|method_return_value != \"void\" }};\n{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();\n\n\treturn proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}\n\n{% for method in interface_event.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method, \"Handler\")}}\n{\n\tASSERT(state_ != ProxyStopped);\n\t{{method.mojom_name}}.emit({{method.parameters|params_comma_sep}});\n}\n{% endfor %}\n\n/* ========================================================================== */"}]}, {"from": "interface", "to": "own", "label": "조건이 거짓이면 ipa_가 인터페이스를 소유합니다. · !ipai [false]", "label_en": "If the condition is false, ipa_ owns the interface. · !ipai [false]", "evidence": [{"source": "execution/threaded", "sha256": "af4b12c81ffee2e9979c01a7e7eb188f5568d258ba03e522b60a3608dc226abd", "quote": "{{proxy_name}}Threaded::{{proxy_name}}Threaded(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm), thread_(\"{{proxy_name}}\")\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in thread: loading IPA from \"\n\t\t<< ipam->path();\n\n\tif (!ipam->load())\n\t\treturn;\n\n\tIPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;\n\t}\n\n\tipa_ = std::unique_ptr<{{interface_name}}>(static_cast<{{interface_name}} *>(ipai));\n\tproxy_.setIPA(ipa_.get());\n\n{% for method in interface_event.methods %}\n\tipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);\n{%- endfor %}\n\n\tvalid_ = true;\n}\n\n{{proxy_name}}Threaded::~{{proxy_name}}Threaded() = default;\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method)}}\n{\n{%- if method.mojom_name == \"stop\" %}\n\t{{proxy_funcs.stop_thread_body()}}\n{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n\n\tproxy_.moveToThread(&thread_);\n\n\treturn {{ \"_ret\" if method|method_return_value != \"void\" }};\n{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();\n\n\treturn proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}\n\n{% for method in interface_event.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method, \"Handler\")}}\n{\n\tASSERT(state_ != ProxyStopped);\n\t{{method.mojom_name}}.emit({{method.parameters|params_comma_sep}});\n}\n{% endfor %}\n\n/* ========================================================================== */"}]}, {"from": "own", "to": "pointer", "label": "소유한 인터페이스의 포인터를 setIPA에 넘깁니다.", "label_en": "The constructor passes a pointer to the owned interface to setIPA.", "evidence": [{"source": "execution/threaded", "sha256": "af4b12c81ffee2e9979c01a7e7eb188f5568d258ba03e522b60a3608dc226abd", "quote": "{{proxy_name}}Threaded::{{proxy_name}}Threaded(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm), thread_(\"{{proxy_name}}\")\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in thread: loading IPA from \"\n\t\t<< ipam->path();\n\n\tif (!ipam->load())\n\t\treturn;\n\n\tIPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;\n\t}\n\n\tipa_ = std::unique_ptr<{{interface_name}}>(static_cast<{{interface_name}} *>(ipai));\n\tproxy_.setIPA(ipa_.get());\n\n{% for method in interface_event.methods %}\n\tipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);\n{%- endfor %}\n\n\tvalid_ = true;\n}\n\n{{proxy_name}}Threaded::~{{proxy_name}}Threaded() = default;\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method)}}\n{\n{%- if method.mojom_name == \"stop\" %}\n\t{{proxy_funcs.stop_thread_body()}}\n{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n\n\tproxy_.moveToThread(&thread_);\n\n\treturn {{ \"_ret\" if method|method_return_value != \"void\" }};\n{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();\n\n\treturn proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}\n\n{% for method in interface_event.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method, \"Handler\")}}\n{\n\tASSERT(state_ != ProxyStopped);\n\t{{method.mojom_name}}.emit({{method.parameters|params_comma_sep}});\n}\n{% endfor %}\n\n/* ========================================================================== */"}]}, {"from": "pointer", "to": "events", "label": "setIPA가 정상적으로 반환하면 각 이벤트를 연결합니다.", "label_en": "After setIPA returns normally, the constructor connects each event.", "evidence": [{"source": "execution/threaded", "sha256": "af4b12c81ffee2e9979c01a7e7eb188f5568d258ba03e522b60a3608dc226abd", "quote": "{{proxy_name}}Threaded::{{proxy_name}}Threaded(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm), thread_(\"{{proxy_name}}\")\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in thread: loading IPA from \"\n\t\t<< ipam->path();\n\n\tif (!ipam->load())\n\t\treturn;\n\n\tIPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;\n\t}\n\n\tipa_ = std::unique_ptr<{{interface_name}}>(static_cast<{{interface_name}} *>(ipai));\n\tproxy_.setIPA(ipa_.get());\n\n{% for method in interface_event.methods %}\n\tipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);\n{%- endfor %}\n\n\tvalid_ = true;\n}\n\n{{proxy_name}}Threaded::~{{proxy_name}}Threaded() = default;\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method)}}\n{\n{%- if method.mojom_name == \"stop\" %}\n\t{{proxy_funcs.stop_thread_body()}}\n{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n\n\tproxy_.moveToThread(&thread_);\n\n\treturn {{ \"_ret\" if method|method_return_value != \"void\" }};\n{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();\n\n\treturn proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}\n\n{% for method in interface_event.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method, \"Handler\")}}\n{\n\tASSERT(state_ != ProxyStopped);\n\t{{method.mojom_name}}.emit({{method.parameters|params_comma_sep}});\n}\n{% endfor %}\n\n/* ========================================================================== */"}]}, {"from": "events", "to": "valid", "label": "이벤트 연결을 마치면 valid_에 true를 저장합니다.", "label_en": "After connecting the events, the constructor stores true in valid_.", "evidence": [{"source": "execution/threaded", "sha256": "af4b12c81ffee2e9979c01a7e7eb188f5568d258ba03e522b60a3608dc226abd", "quote": "{{proxy_name}}Threaded::{{proxy_name}}Threaded(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm), thread_(\"{{proxy_name}}\")\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in thread: loading IPA from \"\n\t\t<< ipam->path();\n\n\tif (!ipam->load())\n\t\treturn;\n\n\tIPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\t\treturn;\n\t}\n\n\tipa_ = std::unique_ptr<{{interface_name}}>(static_cast<{{interface_name}} *>(ipai));\n\tproxy_.setIPA(ipa_.get());\n\n{% for method in interface_event.methods %}\n\tipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);\n{%- endfor %}\n\n\tvalid_ = true;\n}\n\n{{proxy_name}}Threaded::~{{proxy_name}}Threaded() = default;\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method)}}\n{\n{%- if method.mojom_name == \"stop\" %}\n\t{{proxy_funcs.stop_thread_body()}}\n{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n\n\tproxy_.moveToThread(&thread_);\n\n\treturn {{ \"_ret\" if method|method_return_value != \"void\" }};\n{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();\n\n\treturn proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}}, ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}\n\n{% for method in interface_event.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Threaded\", method, \"Handler\")}}\n{\n\tASSERT(state_ != ProxyStopped);\n\t{{method.mojom_name}}.emit({{method.parameters|params_comma_sep}});\n}\n{% endfor %}\n\n/* ========================================================================== */"}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78", "citation_binding_policy": "identifier-and-guard-boundaries-v2", "reused": true}, "isolated-constructor-connection": {"input_fingerprint": "52b8c636584c6156119eb4a2a6db1826c57611df8d0748d8e5c436f62c8cc2c5", "draft": {"nodes": [{"id": "resolve", "symbol": "resolvePath", "label": "resolvePath에 \"{{module_name}}_ipa_proxy\"를 전달해 worker 경로를 찾습니다.", "label_en": "Pass \"{{module_name}}_ipa_proxy\" to resolvePath to find the worker path.", "shape": "process", "quote_ids": ["isolated:0"]}, {"id": "path_check", "symbol": "proxyWorkerPath", "label": "proxyWorkerPath가 비었는지 검사합니다.", "label_en": "Check whether proxyWorkerPath is empty.", "shape": "decision", "quote_ids": ["isolated:0"]}, {"id": "path_failure", "symbol": "LOG", "label": "worker 경로를 찾지 못했다는 오류 로그를 남기고 반환합니다.", "label_en": "Log the failure to get the worker path and return.", "shape": "process", "quote_ids": ["isolated:0"]}, {"id": "create", "symbol": "IPCPipeUnixSocket", "label": "IPCPipeUnixSocket에 모듈 경로와 worker 경로를 전달합니다.", "label_en": "Pass the module path and worker path to IPCPipeUnixSocket.", "shape": "process", "quote_ids": ["isolated:0"]}, {"id": "connection_check", "symbol": "isConnected", "label": "isConnected로 연결 여부를 검사합니다.", "label_en": "Check the connection with isConnected.", "shape": "decision", "quote_ids": ["isolated:0"]}, {"id": "connection_failure", "symbol": "LOG", "label": "IPCPipe를 만들지 못했다는 별도의 오류 로그를 남기고 반환합니다.", "label_en": "Log a separate error for the failure to create IPCPipe and return.", "shape": "process", "quote_ids": ["isolated:0"]}, {"id": "connect", "symbol": "connect", "label": "recv.connect에 this와 &{{proxy_name}}Isolated::recvMessage를 연결합니다.", "label_en": "Connect recv using this and &{{proxy_name}}Isolated::recvMessage.", "shape": "process", "quote_ids": ["isolated:0"]}, {"id": "transfer", "symbol": "std::move", "label": "std::move(ipc)로 연결의 소유권을 ipc_에 옮깁니다.", "label_en": "Transfer ownership of the connection to ipc_ with std::move(ipc).", "shape": "process", "quote_ids": ["isolated:0"]}, {"id": "valid", "symbol": "valid_", "label": "valid_에 true를 저장합니다.", "label_en": "Store true in valid_.", "shape": "process", "quote_ids": ["isolated:0"]}], "edges": [{"from": "resolve", "to": "path_check", "label": "찾은 경로를 검사합니다.", "label_en": "Check the resolved path.", "condition_ref": "always", "quote_ids": ["isolated:0"]}, {"from": "path_check", "to": "path_failure", "label": "경로가 비어 있으면 오류를 처리합니다.", "label_en": "Handle the error if the path is empty.", "condition_ref": "c3:true", "quote_ids": ["isolated:0"]}, {"from": "path_check", "to": "create", "label": "경로가 비어 있지 않으면 IPCPipeUnixSocket을 만듭니다.", "label_en": "Create IPCPipeUnixSocket if the path is not empty.", "condition_ref": "c3:false", "quote_ids": ["isolated:0"]}, {"from": "create", "to": "connection_check", "label": "생성한 ipc의 연결 여부를 검사합니다.", "label_en": "Check the connection of the created ipc.", "condition_ref": "always", "quote_ids": ["isolated:0"]}, {"from": "connection_check", "to": "connection_failure", "label": "연결되지 않았으면 오류를 처리합니다.", "label_en": "Handle the error if it is not connected.", "condition_ref": "c0:true", "quote_ids": ["isolated:0"]}, {"from": "connection_check", "to": "connect", "label": "연결된 것으로 검사되면 수신 핸들러를 연결합니다.", "label_en": "Connect the receive handler if the check reports a connection.", "condition_ref": "c0:false", "quote_ids": ["isolated:0"]}, {"from": "connect", "to": "transfer", "label": "수신 핸들러를 연결한 뒤 소유권을 옮깁니다.", "label_en": "Transfer ownership after connecting the receive handler.", "condition_ref": "always", "quote_ids": ["isolated:0"]}, {"from": "transfer", "to": "valid", "label": "소유권을 옮긴 뒤 valid_를 설정합니다.", "label_en": "Set valid_ after transferring ownership.", "condition_ref": "always", "quote_ids": ["isolated:0"]}]}, "graph": {"id": "isolated-constructor-connection", "topic": "execution", "kind": "flow", "title": "격리 IPA 프록시의 연결 분기와 IPC 소유권", "question": "Isolated 생성자는 worker 경로와 IPC 연결의 실패를 어떻게 처리하고, 성공한 연결의 소유권을 어떻게 옮깁니까?", "condition_display": "inline", "nodes": [{"id": "resolve", "label": "resolvePath에 \"{{module_name}}_ipa_proxy\"를 전달해 worker 경로를 찾습니다.", "label_en": "Pass \"{{module_name}}_ipa_proxy\" to resolvePath to find the worker path.", "shape": "box", "evidence": [{"source": "execution/isolated", "sha256": "dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744", "quote": "{{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm),\n\t  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in isolation: loading IPA from \"\n\t\t<< ipam->path();\n\n\tconst std::string proxyWorkerPath = resolvePath(\"{{module_name}}_ipa_proxy\");\n\tif (proxyWorkerPath.empty()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to get proxy worker path\";\n\t\treturn;\n\t}\n\n\tauto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}\n\n\tipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);\n\n\tipc_ = std::move(ipc);\n\tvalid_ = true;\n}\n\n{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\" %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage _ipcOutputBuf;\n{%- endif %}\n\n{{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}\n\n{% if method|is_async %}\n\tint _ret = ipc_->sendAsync(_ipcInputBuf);\n{%- else %}\n\tint _ret = ipc_->sendSync(_ipcInputBuf\n{{- \", &_ipcOutputBuf\" if has_output -}}\n);\n{%- endif %}\n\tif (_ret < 0) {\n\t\tLOG(IPAProxy, Error) << \"Failed to call {{method.mojom_name}}: \" << _ret;\n{%- if method|method_return_value != \"void\" %}\n\t\treturn static_cast<{{method|method_return_value}}>(_ret);\n{%- else %}\n\t\treturn;\n{%- endif %}\n\t}\n{% if method|method_return_value != \"void\" %}\n\t{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);\n\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}\n\n\treturn _retValue;\n\n{% elif method|method_param_outputs|length > 0 %}\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}\n{% endif -%}\n}\n\n{% endfor %}\n\nvoid {{proxy_name}}Isolated::recvMessage("}]}, {"id": "path_check", "label": "proxyWorkerPath가 비었는지 검사합니다.", "label_en": "Check whether proxyWorkerPath is empty.", "shape": "decision", "evidence": [{"source": "execution/isolated", "sha256": "dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744", "quote": "{{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm),\n\t  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in isolation: loading IPA from \"\n\t\t<< ipam->path();\n\n\tconst std::string proxyWorkerPath = resolvePath(\"{{module_name}}_ipa_proxy\");\n\tif (proxyWorkerPath.empty()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to get proxy worker path\";\n\t\treturn;\n\t}\n\n\tauto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}\n\n\tipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);\n\n\tipc_ = std::move(ipc);\n\tvalid_ = true;\n}\n\n{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\" %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage _ipcOutputBuf;\n{%- endif %}\n\n{{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}\n\n{% if method|is_async %}\n\tint _ret = ipc_->sendAsync(_ipcInputBuf);\n{%- else %}\n\tint _ret = ipc_->sendSync(_ipcInputBuf\n{{- \", &_ipcOutputBuf\" if has_output -}}\n);\n{%- endif %}\n\tif (_ret < 0) {\n\t\tLOG(IPAProxy, Error) << \"Failed to call {{method.mojom_name}}: \" << _ret;\n{%- if method|method_return_value != \"void\" %}\n\t\treturn static_cast<{{method|method_return_value}}>(_ret);\n{%- else %}\n\t\treturn;\n{%- endif %}\n\t}\n{% if method|method_return_value != \"void\" %}\n\t{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);\n\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}\n\n\treturn _retValue;\n\n{% elif method|method_param_outputs|length > 0 %}\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}\n{% endif -%}\n}\n\n{% endfor %}\n\nvoid {{proxy_name}}Isolated::recvMessage("}]}, {"id": "path_failure", "label": "worker 경로를 찾지 못했다는 오류 로그를 남기고 반환합니다.", "label_en": "Log the failure to get the worker path and return.", "shape": "box", "evidence": [{"source": "execution/isolated", "sha256": "dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744", "quote": "{{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm),\n\t  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in isolation: loading IPA from \"\n\t\t<< ipam->path();\n\n\tconst std::string proxyWorkerPath = resolvePath(\"{{module_name}}_ipa_proxy\");\n\tif (proxyWorkerPath.empty()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to get proxy worker path\";\n\t\treturn;\n\t}\n\n\tauto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}\n\n\tipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);\n\n\tipc_ = std::move(ipc);\n\tvalid_ = true;\n}\n\n{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\" %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage _ipcOutputBuf;\n{%- endif %}\n\n{{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}\n\n{% if method|is_async %}\n\tint _ret = ipc_->sendAsync(_ipcInputBuf);\n{%- else %}\n\tint _ret = ipc_->sendSync(_ipcInputBuf\n{{- \", &_ipcOutputBuf\" if has_output -}}\n);\n{%- endif %}\n\tif (_ret < 0) {\n\t\tLOG(IPAProxy, Error) << \"Failed to call {{method.mojom_name}}: \" << _ret;\n{%- if method|method_return_value != \"void\" %}\n\t\treturn static_cast<{{method|method_return_value}}>(_ret);\n{%- else %}\n\t\treturn;\n{%- endif %}\n\t}\n{% if method|method_return_value != \"void\" %}\n\t{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);\n\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}\n\n\treturn _retValue;\n\n{% elif method|method_param_outputs|length > 0 %}\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}\n{% endif -%}\n}\n\n{% endfor %}\n\nvoid {{proxy_name}}Isolated::recvMessage("}]}, {"id": "create", "label": "IPCPipeUnixSocket에 모듈 경로와 worker 경로를 전달합니다.", "label_en": "Pass the module path and worker path to IPCPipeUnixSocket.", "shape": "box", "evidence": [{"source": "execution/isolated", "sha256": "dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744", "quote": "{{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm),\n\t  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in isolation: loading IPA from \"\n\t\t<< ipam->path();\n\n\tconst std::string proxyWorkerPath = resolvePath(\"{{module_name}}_ipa_proxy\");\n\tif (proxyWorkerPath.empty()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to get proxy worker path\";\n\t\treturn;\n\t}\n\n\tauto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}\n\n\tipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);\n\n\tipc_ = std::move(ipc);\n\tvalid_ = true;\n}\n\n{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\" %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage _ipcOutputBuf;\n{%- endif %}\n\n{{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}\n\n{% if method|is_async %}\n\tint _ret = ipc_->sendAsync(_ipcInputBuf);\n{%- else %}\n\tint _ret = ipc_->sendSync(_ipcInputBuf\n{{- \", &_ipcOutputBuf\" if has_output -}}\n);\n{%- endif %}\n\tif (_ret < 0) {\n\t\tLOG(IPAProxy, Error) << \"Failed to call {{method.mojom_name}}: \" << _ret;\n{%- if method|method_return_value != \"void\" %}\n\t\treturn static_cast<{{method|method_return_value}}>(_ret);\n{%- else %}\n\t\treturn;\n{%- endif %}\n\t}\n{% if method|method_return_value != \"void\" %}\n\t{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);\n\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}\n\n\treturn _retValue;\n\n{% elif method|method_param_outputs|length > 0 %}\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}\n{% endif -%}\n}\n\n{% endfor %}\n\nvoid {{proxy_name}}Isolated::recvMessage("}]}, {"id": "connection_check", "label": "isConnected로 연결 여부를 검사합니다.", "label_en": "Check the connection with isConnected.", "shape": "decision", "evidence": [{"source": "execution/isolated", "sha256": "dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744", "quote": "{{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm),\n\t  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in isolation: loading IPA from \"\n\t\t<< ipam->path();\n\n\tconst std::string proxyWorkerPath = resolvePath(\"{{module_name}}_ipa_proxy\");\n\tif (proxyWorkerPath.empty()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to get proxy worker path\";\n\t\treturn;\n\t}\n\n\tauto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}\n\n\tipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);\n\n\tipc_ = std::move(ipc);\n\tvalid_ = true;\n}\n\n{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\" %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage _ipcOutputBuf;\n{%- endif %}\n\n{{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}\n\n{% if method|is_async %}\n\tint _ret = ipc_->sendAsync(_ipcInputBuf);\n{%- else %}\n\tint _ret = ipc_->sendSync(_ipcInputBuf\n{{- \", &_ipcOutputBuf\" if has_output -}}\n);\n{%- endif %}\n\tif (_ret < 0) {\n\t\tLOG(IPAProxy, Error) << \"Failed to call {{method.mojom_name}}: \" << _ret;\n{%- if method|method_return_value != \"void\" %}\n\t\treturn static_cast<{{method|method_return_value}}>(_ret);\n{%- else %}\n\t\treturn;\n{%- endif %}\n\t}\n{% if method|method_return_value != \"void\" %}\n\t{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);\n\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}\n\n\treturn _retValue;\n\n{% elif method|method_param_outputs|length > 0 %}\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}\n{% endif -%}\n}\n\n{% endfor %}\n\nvoid {{proxy_name}}Isolated::recvMessage("}]}, {"id": "connection_failure", "label": "IPCPipe를 만들지 못했다는 별도의 오류 로그를 남기고 반환합니다.", "label_en": "Log a separate error for the failure to create IPCPipe and return.", "shape": "box", "evidence": [{"source": "execution/isolated", "sha256": "dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744", "quote": "{{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm),\n\t  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in isolation: loading IPA from \"\n\t\t<< ipam->path();\n\n\tconst std::string proxyWorkerPath = resolvePath(\"{{module_name}}_ipa_proxy\");\n\tif (proxyWorkerPath.empty()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to get proxy worker path\";\n\t\treturn;\n\t}\n\n\tauto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}\n\n\tipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);\n\n\tipc_ = std::move(ipc);\n\tvalid_ = true;\n}\n\n{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\" %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage _ipcOutputBuf;\n{%- endif %}\n\n{{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}\n\n{% if method|is_async %}\n\tint _ret = ipc_->sendAsync(_ipcInputBuf);\n{%- else %}\n\tint _ret = ipc_->sendSync(_ipcInputBuf\n{{- \", &_ipcOutputBuf\" if has_output -}}\n);\n{%- endif %}\n\tif (_ret < 0) {\n\t\tLOG(IPAProxy, Error) << \"Failed to call {{method.mojom_name}}: \" << _ret;\n{%- if method|method_return_value != \"void\" %}\n\t\treturn static_cast<{{method|method_return_value}}>(_ret);\n{%- else %}\n\t\treturn;\n{%- endif %}\n\t}\n{% if method|method_return_value != \"void\" %}\n\t{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);\n\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}\n\n\treturn _retValue;\n\n{% elif method|method_param_outputs|length > 0 %}\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}\n{% endif -%}\n}\n\n{% endfor %}\n\nvoid {{proxy_name}}Isolated::recvMessage("}]}, {"id": "connect", "label": "recv.connect에 this와 &{{proxy_name}}Isolated::recvMessage를 연결합니다.", "label_en": "Connect recv using this and &{{proxy_name}}Isolated::recvMessage.", "shape": "box", "evidence": [{"source": "execution/isolated", "sha256": "dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744", "quote": "{{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm),\n\t  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in isolation: loading IPA from \"\n\t\t<< ipam->path();\n\n\tconst std::string proxyWorkerPath = resolvePath(\"{{module_name}}_ipa_proxy\");\n\tif (proxyWorkerPath.empty()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to get proxy worker path\";\n\t\treturn;\n\t}\n\n\tauto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}\n\n\tipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);\n\n\tipc_ = std::move(ipc);\n\tvalid_ = true;\n}\n\n{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\" %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage _ipcOutputBuf;\n{%- endif %}\n\n{{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}\n\n{% if method|is_async %}\n\tint _ret = ipc_->sendAsync(_ipcInputBuf);\n{%- else %}\n\tint _ret = ipc_->sendSync(_ipcInputBuf\n{{- \", &_ipcOutputBuf\" if has_output -}}\n);\n{%- endif %}\n\tif (_ret < 0) {\n\t\tLOG(IPAProxy, Error) << \"Failed to call {{method.mojom_name}}: \" << _ret;\n{%- if method|method_return_value != \"void\" %}\n\t\treturn static_cast<{{method|method_return_value}}>(_ret);\n{%- else %}\n\t\treturn;\n{%- endif %}\n\t}\n{% if method|method_return_value != \"void\" %}\n\t{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);\n\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}\n\n\treturn _retValue;\n\n{% elif method|method_param_outputs|length > 0 %}\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}\n{% endif -%}\n}\n\n{% endfor %}\n\nvoid {{proxy_name}}Isolated::recvMessage("}]}, {"id": "transfer", "label": "std::move(ipc)로 연결의 소유권을 ipc_에 옮깁니다.", "label_en": "Transfer ownership of the connection to ipc_ with std::move(ipc).", "shape": "box", "evidence": [{"source": "execution/isolated", "sha256": "dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744", "quote": "{{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm),\n\t  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in isolation: loading IPA from \"\n\t\t<< ipam->path();\n\n\tconst std::string proxyWorkerPath = resolvePath(\"{{module_name}}_ipa_proxy\");\n\tif (proxyWorkerPath.empty()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to get proxy worker path\";\n\t\treturn;\n\t}\n\n\tauto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}\n\n\tipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);\n\n\tipc_ = std::move(ipc);\n\tvalid_ = true;\n}\n\n{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\" %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage _ipcOutputBuf;\n{%- endif %}\n\n{{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}\n\n{% if method|is_async %}\n\tint _ret = ipc_->sendAsync(_ipcInputBuf);\n{%- else %}\n\tint _ret = ipc_->sendSync(_ipcInputBuf\n{{- \", &_ipcOutputBuf\" if has_output -}}\n);\n{%- endif %}\n\tif (_ret < 0) {\n\t\tLOG(IPAProxy, Error) << \"Failed to call {{method.mojom_name}}: \" << _ret;\n{%- if method|method_return_value != \"void\" %}\n\t\treturn static_cast<{{method|method_return_value}}>(_ret);\n{%- else %}\n\t\treturn;\n{%- endif %}\n\t}\n{% if method|method_return_value != \"void\" %}\n\t{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);\n\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}\n\n\treturn _retValue;\n\n{% elif method|method_param_outputs|length > 0 %}\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}\n{% endif -%}\n}\n\n{% endfor %}\n\nvoid {{proxy_name}}Isolated::recvMessage("}]}, {"id": "valid", "label": "valid_에 true를 저장합니다.", "label_en": "Store true in valid_.", "shape": "box", "evidence": [{"source": "execution/isolated", "sha256": "dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744", "quote": "{{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm),\n\t  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in isolation: loading IPA from \"\n\t\t<< ipam->path();\n\n\tconst std::string proxyWorkerPath = resolvePath(\"{{module_name}}_ipa_proxy\");\n\tif (proxyWorkerPath.empty()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to get proxy worker path\";\n\t\treturn;\n\t}\n\n\tauto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}\n\n\tipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);\n\n\tipc_ = std::move(ipc);\n\tvalid_ = true;\n}\n\n{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\" %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage _ipcOutputBuf;\n{%- endif %}\n\n{{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}\n\n{% if method|is_async %}\n\tint _ret = ipc_->sendAsync(_ipcInputBuf);\n{%- else %}\n\tint _ret = ipc_->sendSync(_ipcInputBuf\n{{- \", &_ipcOutputBuf\" if has_output -}}\n);\n{%- endif %}\n\tif (_ret < 0) {\n\t\tLOG(IPAProxy, Error) << \"Failed to call {{method.mojom_name}}: \" << _ret;\n{%- if method|method_return_value != \"void\" %}\n\t\treturn static_cast<{{method|method_return_value}}>(_ret);\n{%- else %}\n\t\treturn;\n{%- endif %}\n\t}\n{% if method|method_return_value != \"void\" %}\n\t{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);\n\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}\n\n\treturn _retValue;\n\n{% elif method|method_param_outputs|length > 0 %}\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}\n{% endif -%}\n}\n\n{% endfor %}\n\nvoid {{proxy_name}}Isolated::recvMessage("}]}], "edges": [{"from": "resolve", "to": "path_check", "label": "찾은 경로를 검사합니다.", "label_en": "Check the resolved path.", "evidence": [{"source": "execution/isolated", "sha256": "dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744", "quote": "{{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm),\n\t  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in isolation: loading IPA from \"\n\t\t<< ipam->path();\n\n\tconst std::string proxyWorkerPath = resolvePath(\"{{module_name}}_ipa_proxy\");\n\tif (proxyWorkerPath.empty()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to get proxy worker path\";\n\t\treturn;\n\t}\n\n\tauto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}\n\n\tipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);\n\n\tipc_ = std::move(ipc);\n\tvalid_ = true;\n}\n\n{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\" %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage _ipcOutputBuf;\n{%- endif %}\n\n{{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}\n\n{% if method|is_async %}\n\tint _ret = ipc_->sendAsync(_ipcInputBuf);\n{%- else %}\n\tint _ret = ipc_->sendSync(_ipcInputBuf\n{{- \", &_ipcOutputBuf\" if has_output -}}\n);\n{%- endif %}\n\tif (_ret < 0) {\n\t\tLOG(IPAProxy, Error) << \"Failed to call {{method.mojom_name}}: \" << _ret;\n{%- if method|method_return_value != \"void\" %}\n\t\treturn static_cast<{{method|method_return_value}}>(_ret);\n{%- else %}\n\t\treturn;\n{%- endif %}\n\t}\n{% if method|method_return_value != \"void\" %}\n\t{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);\n\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}\n\n\treturn _retValue;\n\n{% elif method|method_param_outputs|length > 0 %}\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}\n{% endif -%}\n}\n\n{% endfor %}\n\nvoid {{proxy_name}}Isolated::recvMessage("}]}, {"from": "path_check", "to": "path_failure", "label": "경로가 비어 있으면 오류를 처리합니다. · proxyWorkerPath.empty() [true]", "label_en": "Handle the error if the path is empty. · proxyWorkerPath.empty() [true]", "evidence": [{"source": "execution/isolated", "sha256": "dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744", "quote": "{{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm),\n\t  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in isolation: loading IPA from \"\n\t\t<< ipam->path();\n\n\tconst std::string proxyWorkerPath = resolvePath(\"{{module_name}}_ipa_proxy\");\n\tif (proxyWorkerPath.empty()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to get proxy worker path\";\n\t\treturn;\n\t}\n\n\tauto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}\n\n\tipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);\n\n\tipc_ = std::move(ipc);\n\tvalid_ = true;\n}\n\n{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\" %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage _ipcOutputBuf;\n{%- endif %}\n\n{{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}\n\n{% if method|is_async %}\n\tint _ret = ipc_->sendAsync(_ipcInputBuf);\n{%- else %}\n\tint _ret = ipc_->sendSync(_ipcInputBuf\n{{- \", &_ipcOutputBuf\" if has_output -}}\n);\n{%- endif %}\n\tif (_ret < 0) {\n\t\tLOG(IPAProxy, Error) << \"Failed to call {{method.mojom_name}}: \" << _ret;\n{%- if method|method_return_value != \"void\" %}\n\t\treturn static_cast<{{method|method_return_value}}>(_ret);\n{%- else %}\n\t\treturn;\n{%- endif %}\n\t}\n{% if method|method_return_value != \"void\" %}\n\t{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);\n\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}\n\n\treturn _retValue;\n\n{% elif method|method_param_outputs|length > 0 %}\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}\n{% endif -%}\n}\n\n{% endfor %}\n\nvoid {{proxy_name}}Isolated::recvMessage("}]}, {"from": "path_check", "to": "create", "label": "경로가 비어 있지 않으면 IPCPipeUnixSocket을 만듭니다. · proxyWorkerPath.empty() [false]", "label_en": "Create IPCPipeUnixSocket if the path is not empty. · proxyWorkerPath.empty() [false]", "evidence": [{"source": "execution/isolated", "sha256": "dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744", "quote": "{{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm),\n\t  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in isolation: loading IPA from \"\n\t\t<< ipam->path();\n\n\tconst std::string proxyWorkerPath = resolvePath(\"{{module_name}}_ipa_proxy\");\n\tif (proxyWorkerPath.empty()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to get proxy worker path\";\n\t\treturn;\n\t}\n\n\tauto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}\n\n\tipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);\n\n\tipc_ = std::move(ipc);\n\tvalid_ = true;\n}\n\n{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\" %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage _ipcOutputBuf;\n{%- endif %}\n\n{{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}\n\n{% if method|is_async %}\n\tint _ret = ipc_->sendAsync(_ipcInputBuf);\n{%- else %}\n\tint _ret = ipc_->sendSync(_ipcInputBuf\n{{- \", &_ipcOutputBuf\" if has_output -}}\n);\n{%- endif %}\n\tif (_ret < 0) {\n\t\tLOG(IPAProxy, Error) << \"Failed to call {{method.mojom_name}}: \" << _ret;\n{%- if method|method_return_value != \"void\" %}\n\t\treturn static_cast<{{method|method_return_value}}>(_ret);\n{%- else %}\n\t\treturn;\n{%- endif %}\n\t}\n{% if method|method_return_value != \"void\" %}\n\t{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);\n\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}\n\n\treturn _retValue;\n\n{% elif method|method_param_outputs|length > 0 %}\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}\n{% endif -%}\n}\n\n{% endfor %}\n\nvoid {{proxy_name}}Isolated::recvMessage("}]}, {"from": "create", "to": "connection_check", "label": "생성한 ipc의 연결 여부를 검사합니다.", "label_en": "Check the connection of the created ipc.", "evidence": [{"source": "execution/isolated", "sha256": "dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744", "quote": "{{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm),\n\t  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in isolation: loading IPA from \"\n\t\t<< ipam->path();\n\n\tconst std::string proxyWorkerPath = resolvePath(\"{{module_name}}_ipa_proxy\");\n\tif (proxyWorkerPath.empty()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to get proxy worker path\";\n\t\treturn;\n\t}\n\n\tauto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}\n\n\tipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);\n\n\tipc_ = std::move(ipc);\n\tvalid_ = true;\n}\n\n{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\" %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage _ipcOutputBuf;\n{%- endif %}\n\n{{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}\n\n{% if method|is_async %}\n\tint _ret = ipc_->sendAsync(_ipcInputBuf);\n{%- else %}\n\tint _ret = ipc_->sendSync(_ipcInputBuf\n{{- \", &_ipcOutputBuf\" if has_output -}}\n);\n{%- endif %}\n\tif (_ret < 0) {\n\t\tLOG(IPAProxy, Error) << \"Failed to call {{method.mojom_name}}: \" << _ret;\n{%- if method|method_return_value != \"void\" %}\n\t\treturn static_cast<{{method|method_return_value}}>(_ret);\n{%- else %}\n\t\treturn;\n{%- endif %}\n\t}\n{% if method|method_return_value != \"void\" %}\n\t{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);\n\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}\n\n\treturn _retValue;\n\n{% elif method|method_param_outputs|length > 0 %}\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}\n{% endif -%}\n}\n\n{% endfor %}\n\nvoid {{proxy_name}}Isolated::recvMessage("}]}, {"from": "connection_check", "to": "connection_failure", "label": "연결되지 않았으면 오류를 처리합니다. · !ipc->isConnected() [true]", "label_en": "Handle the error if it is not connected. · !ipc->isConnected() [true]", "evidence": [{"source": "execution/isolated", "sha256": "dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744", "quote": "{{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm),\n\t  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in isolation: loading IPA from \"\n\t\t<< ipam->path();\n\n\tconst std::string proxyWorkerPath = resolvePath(\"{{module_name}}_ipa_proxy\");\n\tif (proxyWorkerPath.empty()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to get proxy worker path\";\n\t\treturn;\n\t}\n\n\tauto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}\n\n\tipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);\n\n\tipc_ = std::move(ipc);\n\tvalid_ = true;\n}\n\n{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\" %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage _ipcOutputBuf;\n{%- endif %}\n\n{{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}\n\n{% if method|is_async %}\n\tint _ret = ipc_->sendAsync(_ipcInputBuf);\n{%- else %}\n\tint _ret = ipc_->sendSync(_ipcInputBuf\n{{- \", &_ipcOutputBuf\" if has_output -}}\n);\n{%- endif %}\n\tif (_ret < 0) {\n\t\tLOG(IPAProxy, Error) << \"Failed to call {{method.mojom_name}}: \" << _ret;\n{%- if method|method_return_value != \"void\" %}\n\t\treturn static_cast<{{method|method_return_value}}>(_ret);\n{%- else %}\n\t\treturn;\n{%- endif %}\n\t}\n{% if method|method_return_value != \"void\" %}\n\t{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);\n\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}\n\n\treturn _retValue;\n\n{% elif method|method_param_outputs|length > 0 %}\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}\n{% endif -%}\n}\n\n{% endfor %}\n\nvoid {{proxy_name}}Isolated::recvMessage("}]}, {"from": "connection_check", "to": "connect", "label": "연결된 것으로 검사되면 수신 핸들러를 연결합니다. · !ipc->isConnected() [false]", "label_en": "Connect the receive handler if the check reports a connection. · !ipc->isConnected() [false]", "evidence": [{"source": "execution/isolated", "sha256": "dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744", "quote": "{{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm),\n\t  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in isolation: loading IPA from \"\n\t\t<< ipam->path();\n\n\tconst std::string proxyWorkerPath = resolvePath(\"{{module_name}}_ipa_proxy\");\n\tif (proxyWorkerPath.empty()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to get proxy worker path\";\n\t\treturn;\n\t}\n\n\tauto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}\n\n\tipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);\n\n\tipc_ = std::move(ipc);\n\tvalid_ = true;\n}\n\n{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\" %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage _ipcOutputBuf;\n{%- endif %}\n\n{{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}\n\n{% if method|is_async %}\n\tint _ret = ipc_->sendAsync(_ipcInputBuf);\n{%- else %}\n\tint _ret = ipc_->sendSync(_ipcInputBuf\n{{- \", &_ipcOutputBuf\" if has_output -}}\n);\n{%- endif %}\n\tif (_ret < 0) {\n\t\tLOG(IPAProxy, Error) << \"Failed to call {{method.mojom_name}}: \" << _ret;\n{%- if method|method_return_value != \"void\" %}\n\t\treturn static_cast<{{method|method_return_value}}>(_ret);\n{%- else %}\n\t\treturn;\n{%- endif %}\n\t}\n{% if method|method_return_value != \"void\" %}\n\t{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);\n\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}\n\n\treturn _retValue;\n\n{% elif method|method_param_outputs|length > 0 %}\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}\n{% endif -%}\n}\n\n{% endfor %}\n\nvoid {{proxy_name}}Isolated::recvMessage("}]}, {"from": "connect", "to": "transfer", "label": "수신 핸들러를 연결한 뒤 소유권을 옮깁니다.", "label_en": "Transfer ownership after connecting the receive handler.", "evidence": [{"source": "execution/isolated", "sha256": "dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744", "quote": "{{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm),\n\t  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in isolation: loading IPA from \"\n\t\t<< ipam->path();\n\n\tconst std::string proxyWorkerPath = resolvePath(\"{{module_name}}_ipa_proxy\");\n\tif (proxyWorkerPath.empty()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to get proxy worker path\";\n\t\treturn;\n\t}\n\n\tauto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}\n\n\tipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);\n\n\tipc_ = std::move(ipc);\n\tvalid_ = true;\n}\n\n{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\" %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage _ipcOutputBuf;\n{%- endif %}\n\n{{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}\n\n{% if method|is_async %}\n\tint _ret = ipc_->sendAsync(_ipcInputBuf);\n{%- else %}\n\tint _ret = ipc_->sendSync(_ipcInputBuf\n{{- \", &_ipcOutputBuf\" if has_output -}}\n);\n{%- endif %}\n\tif (_ret < 0) {\n\t\tLOG(IPAProxy, Error) << \"Failed to call {{method.mojom_name}}: \" << _ret;\n{%- if method|method_return_value != \"void\" %}\n\t\treturn static_cast<{{method|method_return_value}}>(_ret);\n{%- else %}\n\t\treturn;\n{%- endif %}\n\t}\n{% if method|method_return_value != \"void\" %}\n\t{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);\n\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}\n\n\treturn _retValue;\n\n{% elif method|method_param_outputs|length > 0 %}\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}\n{% endif -%}\n}\n\n{% endfor %}\n\nvoid {{proxy_name}}Isolated::recvMessage("}]}, {"from": "transfer", "to": "valid", "label": "소유권을 옮긴 뒤 valid_를 설정합니다.", "label_en": "Set valid_ after transferring ownership.", "evidence": [{"source": "execution/isolated", "sha256": "dd0ba6e352ffacd6c27c6ff5bb447af14838d75ca6aed8d056855ec442a97744", "quote": "{{proxy_name}}Isolated::{{proxy_name}}Isolated(IPAModule *ipam, const CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm),\n\t  controlSerializer_(ControlSerializer::Role::Proxy), seq_(0)\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy in isolation: loading IPA from \"\n\t\t<< ipam->path();\n\n\tconst std::string proxyWorkerPath = resolvePath(\"{{module_name}}_ipa_proxy\");\n\tif (proxyWorkerPath.empty()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to get proxy worker path\";\n\t\treturn;\n\t}\n\n\tauto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t}\n\n\tipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);\n\n\tipc_ = std::move(ipc);\n\tvalid_ = true;\n}\n\n{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}\n\n{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\" %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true if method|method_param_outputs|length > 0 or method|method_return_value != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage _ipcOutputBuf;\n{%- endif %}\n\n{{proxy_funcs.serialize_call(method|method_param_inputs, '_ipcInputBuf.data()', '_ipcInputBuf.fds()')}}\n\n{% if method|is_async %}\n\tint _ret = ipc_->sendAsync(_ipcInputBuf);\n{%- else %}\n\tint _ret = ipc_->sendSync(_ipcInputBuf\n{{- \", &_ipcOutputBuf\" if has_output -}}\n);\n{%- endif %}\n\tif (_ret < 0) {\n\t\tLOG(IPAProxy, Error) << \"Failed to call {{method.mojom_name}}: \" << _ret;\n{%- if method|method_return_value != \"void\" %}\n\t\treturn static_cast<{{method|method_return_value}}>(_ret);\n{%- else %}\n\t\treturn;\n{%- endif %}\n\t}\n{% if method|method_return_value != \"void\" %}\n\t{{method|method_return_value}} _retValue = IPADataSerializer<{{method|method_return_value}}>::deserialize(_ipcOutputBuf.data(), 0);\n\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()', init_offset = method|method_return_value|byte_width|int)}}\n\n\treturn _retValue;\n\n{% elif method|method_param_outputs|length > 0 %}\n{{proxy_funcs.deserialize_call(method|method_param_outputs, '_ipcOutputBuf.data()', '_ipcOutputBuf.fds()')}}\n{% endif -%}\n}\n\n{% endfor %}\n\nvoid {{proxy_name}}Isolated::recvMessage("}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78", "citation_binding_policy": "identifier-and-guard-boundaries-v2", "reused": false}, "threaded-stop-order": {"input_fingerprint": "9fac0d7e5b5c5abaac01d433fb1443bf9319eb645af9520164e42a50c2c65346", "draft": {"nodes": [{"id": "assert", "symbol": "ASSERT", "label": "먼저 ASSERT로 state_가 ProxyStopping이 아닌지 확인합니다.", "label_en": "First, ASSERT checks that state_ is not ProxyStopping.", "shape": "process", "quote_ids": ["thread-stop:0"]}, {"id": "check", "symbol": "state_", "label": "ASSERT 뒤에서 state_가 ProxyRunning이 아닌지 검사합니다.", "label_en": "After ASSERT, check whether state_ is not ProxyRunning.", "shape": "decision", "quote_ids": ["thread-stop:0"]}, {"id": "return", "symbol": "return", "label": "조건이 참이면 즉시 반환합니다.", "label_en": "If the condition is true, return immediately.", "shape": "box", "quote_ids": ["thread-stop:0"]}, {"id": "stopping", "symbol": "ProxyStopping", "label": "조건이 거짓이면 state_를 ProxyStopping으로 설정합니다.", "label_en": "If the condition is false, set state_ to ProxyStopping.", "shape": "process", "quote_ids": ["thread-stop:0"]}, {"id": "invoke", "symbol": "invokeMethod", "label": "proxy_의 invokeMethod로 ThreadProxy::stop을 ConnectionTypeBlocking으로 동기 호출합니다.", "label_en": "Call ThreadProxy::stop synchronously through proxy_'s invokeMethod with ConnectionTypeBlocking.", "shape": "process", "quote_ids": ["thread-stop:0"]}, {"id": "exit", "symbol": "exit", "label": "동기 호출이 정상 반환하면 thread_의 exit를 호출합니다.", "label_en": "When the synchronous call returns normally, call exit on thread_.", "shape": "process", "quote_ids": ["thread-stop:0"]}, {"id": "wait", "symbol": "wait", "label": "thread_의 wait를 호출해 스레드 종료를 기다립니다.", "label_en": "Call wait on thread_ to wait for the thread to finish.", "shape": "process", "quote_ids": ["thread-stop:0"]}, {"id": "dispatch", "symbol": "dispatchMessages", "label": "현재 스레드에서 dispatchMessages를 호출해 this와 Message::Type::InvokeMessage를 대상으로 메시지를 처리합니다.", "label_en": "Call dispatchMessages on the current thread to process messages for this and Message::Type::InvokeMessage.", "shape": "process", "quote_ids": ["thread-stop:0"]}, {"id": "stopped", "symbol": "ProxyStopped", "label": "dispatchMessages가 정상 반환하면 state_를 ProxyStopped로 갱신합니다.", "label_en": "When dispatchMessages returns normally, update state_ to ProxyStopped.", "shape": "process", "quote_ids": ["thread-stop:0"]}], "edges": [{"from": "assert", "to": "check", "label": "ASSERT 뒤에 별도의 상태 검사가 나옵니다.", "label_en": "A separate state check follows ASSERT.", "condition_ref": "always", "quote_ids": ["thread-stop:0"]}, {"from": "check", "to": "return", "label": "조건이 참이면 즉시 반환합니다.", "label_en": "If the condition is true, return immediately.", "condition_ref": "c2:true", "quote_ids": ["thread-stop:0"]}, {"from": "check", "to": "stopping", "label": "조건이 거짓이면 정지를 진행합니다.", "label_en": "If the condition is false, proceed with stopping.", "condition_ref": "c2:false", "quote_ids": ["thread-stop:0"]}, {"from": "stopping", "to": "invoke", "label": "상태를 설정한 뒤 동기 호출합니다.", "label_en": "After setting the state, make the synchronous call.", "condition_ref": "always", "quote_ids": ["thread-stop:0"]}, {"from": "invoke", "to": "exit", "label": "호출이 정상 반환하면 exit를 호출합니다.", "label_en": "When the call returns normally, call exit.", "condition_ref": "always", "quote_ids": ["thread-stop:0"]}, {"from": "exit", "to": "wait", "label": "exit가 정상 반환하면 wait를 호출합니다.", "label_en": "When exit returns normally, call wait.", "condition_ref": "always", "quote_ids": ["thread-stop:0"]}, {"from": "wait", "to": "dispatch", "label": "wait가 정상 반환하면 메시지를 처리합니다.", "label_en": "When wait returns normally, dispatch messages.", "condition_ref": "always", "quote_ids": ["thread-stop:0"]}, {"from": "dispatch", "to": "stopped", "label": "메시지 처리가 정상 반환하면 상태를 갱신합니다.", "label_en": "When message dispatch returns normally, update the state.", "condition_ref": "always", "quote_ids": ["thread-stop:0"]}]}, "graph": {"id": "threaded-stop-order", "topic": "lifetime", "kind": "flow", "title": "Threaded 정지의 상태와 순서", "question": "Threaded stop은 어떤 상태 검사와 동기 호출 및 스레드 종료 순서로 ProxyStopped가 됩니까?", "condition_display": "inline", "nodes": [{"id": "assert", "label": "먼저 ASSERT로 state_가 ProxyStopping이 아닌지 확인합니다.", "label_en": "First, ASSERT checks that state_ is not ProxyStopping.", "shape": "box", "evidence": [{"source": "lifetime/thread-stop", "sha256": "40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;\n\n\tstate_ = ProxyStopping;\n\n\tproxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);\n\n\tthread_.exit();\n\tthread_.wait();\n\n\tThread::current()->dispatchMessages(Message::Type::InvokeMessage, this);\n\n\tstate_ = ProxyStopped;\n{%- endmacro -%}"}]}, {"id": "check", "label": "ASSERT 뒤에서 state_가 ProxyRunning이 아닌지 검사합니다.", "label_en": "After ASSERT, check whether state_ is not ProxyRunning.", "shape": "decision", "evidence": [{"source": "lifetime/thread-stop", "sha256": "40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;\n\n\tstate_ = ProxyStopping;\n\n\tproxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);\n\n\tthread_.exit();\n\tthread_.wait();\n\n\tThread::current()->dispatchMessages(Message::Type::InvokeMessage, this);\n\n\tstate_ = ProxyStopped;\n{%- endmacro -%}"}]}, {"id": "return", "label": "조건이 참이면 즉시 반환합니다.", "label_en": "If the condition is true, return immediately.", "shape": "box", "evidence": [{"source": "lifetime/thread-stop", "sha256": "40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;\n\n\tstate_ = ProxyStopping;\n\n\tproxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);\n\n\tthread_.exit();\n\tthread_.wait();\n\n\tThread::current()->dispatchMessages(Message::Type::InvokeMessage, this);\n\n\tstate_ = ProxyStopped;\n{%- endmacro -%}"}]}, {"id": "stopping", "label": "조건이 거짓이면 state_를 ProxyStopping으로 설정합니다.", "label_en": "If the condition is false, set state_ to ProxyStopping.", "shape": "box", "evidence": [{"source": "lifetime/thread-stop", "sha256": "40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;\n\n\tstate_ = ProxyStopping;\n\n\tproxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);\n\n\tthread_.exit();\n\tthread_.wait();\n\n\tThread::current()->dispatchMessages(Message::Type::InvokeMessage, this);\n\n\tstate_ = ProxyStopped;\n{%- endmacro -%}"}]}, {"id": "invoke", "label": "proxy_의 invokeMethod로 ThreadProxy::stop을 ConnectionTypeBlocking으로 동기 호출합니다.", "label_en": "Call ThreadProxy::stop synchronously through proxy_'s invokeMethod with ConnectionTypeBlocking.", "shape": "box", "evidence": [{"source": "lifetime/thread-stop", "sha256": "40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;\n\n\tstate_ = ProxyStopping;\n\n\tproxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);\n\n\tthread_.exit();\n\tthread_.wait();\n\n\tThread::current()->dispatchMessages(Message::Type::InvokeMessage, this);\n\n\tstate_ = ProxyStopped;\n{%- endmacro -%}"}]}, {"id": "exit", "label": "동기 호출이 정상 반환하면 thread_의 exit를 호출합니다.", "label_en": "When the synchronous call returns normally, call exit on thread_.", "shape": "box", "evidence": [{"source": "lifetime/thread-stop", "sha256": "40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;\n\n\tstate_ = ProxyStopping;\n\n\tproxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);\n\n\tthread_.exit();\n\tthread_.wait();\n\n\tThread::current()->dispatchMessages(Message::Type::InvokeMessage, this);\n\n\tstate_ = ProxyStopped;\n{%- endmacro -%}"}]}, {"id": "wait", "label": "thread_의 wait를 호출해 스레드 종료를 기다립니다.", "label_en": "Call wait on thread_ to wait for the thread to finish.", "shape": "box", "evidence": [{"source": "lifetime/thread-stop", "sha256": "40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;\n\n\tstate_ = ProxyStopping;\n\n\tproxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);\n\n\tthread_.exit();\n\tthread_.wait();\n\n\tThread::current()->dispatchMessages(Message::Type::InvokeMessage, this);\n\n\tstate_ = ProxyStopped;\n{%- endmacro -%}"}]}, {"id": "dispatch", "label": "현재 스레드에서 dispatchMessages를 호출해 this와 Message::Type::InvokeMessage를 대상으로 메시지를 처리합니다.", "label_en": "Call dispatchMessages on the current thread to process messages for this and Message::Type::InvokeMessage.", "shape": "box", "evidence": [{"source": "lifetime/thread-stop", "sha256": "40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;\n\n\tstate_ = ProxyStopping;\n\n\tproxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);\n\n\tthread_.exit();\n\tthread_.wait();\n\n\tThread::current()->dispatchMessages(Message::Type::InvokeMessage, this);\n\n\tstate_ = ProxyStopped;\n{%- endmacro -%}"}]}, {"id": "stopped", "label": "dispatchMessages가 정상 반환하면 state_를 ProxyStopped로 갱신합니다.", "label_en": "When dispatchMessages returns normally, update state_ to ProxyStopped.", "shape": "box", "evidence": [{"source": "lifetime/thread-stop", "sha256": "40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;\n\n\tstate_ = ProxyStopping;\n\n\tproxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);\n\n\tthread_.exit();\n\tthread_.wait();\n\n\tThread::current()->dispatchMessages(Message::Type::InvokeMessage, this);\n\n\tstate_ = ProxyStopped;\n{%- endmacro -%}"}]}], "edges": [{"from": "assert", "to": "check", "label": "ASSERT 뒤에 별도의 상태 검사가 나옵니다.", "label_en": "A separate state check follows ASSERT.", "evidence": [{"source": "lifetime/thread-stop", "sha256": "40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;\n\n\tstate_ = ProxyStopping;\n\n\tproxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);\n\n\tthread_.exit();\n\tthread_.wait();\n\n\tThread::current()->dispatchMessages(Message::Type::InvokeMessage, this);\n\n\tstate_ = ProxyStopped;\n{%- endmacro -%}"}]}, {"from": "check", "to": "return", "label": "조건이 참이면 즉시 반환합니다. · state_ != ProxyRunning [true]", "label_en": "If the condition is true, return immediately. · state_ != ProxyRunning [true]", "evidence": [{"source": "lifetime/thread-stop", "sha256": "40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;\n\n\tstate_ = ProxyStopping;\n\n\tproxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);\n\n\tthread_.exit();\n\tthread_.wait();\n\n\tThread::current()->dispatchMessages(Message::Type::InvokeMessage, this);\n\n\tstate_ = ProxyStopped;\n{%- endmacro -%}"}]}, {"from": "check", "to": "stopping", "label": "조건이 거짓이면 정지를 진행합니다. · state_ != ProxyRunning [false]", "label_en": "If the condition is false, proceed with stopping. · state_ != ProxyRunning [false]", "evidence": [{"source": "lifetime/thread-stop", "sha256": "40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;\n\n\tstate_ = ProxyStopping;\n\n\tproxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);\n\n\tthread_.exit();\n\tthread_.wait();\n\n\tThread::current()->dispatchMessages(Message::Type::InvokeMessage, this);\n\n\tstate_ = ProxyStopped;\n{%- endmacro -%}"}]}, {"from": "stopping", "to": "invoke", "label": "상태를 설정한 뒤 동기 호출합니다.", "label_en": "After setting the state, make the synchronous call.", "evidence": [{"source": "lifetime/thread-stop", "sha256": "40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;\n\n\tstate_ = ProxyStopping;\n\n\tproxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);\n\n\tthread_.exit();\n\tthread_.wait();\n\n\tThread::current()->dispatchMessages(Message::Type::InvokeMessage, this);\n\n\tstate_ = ProxyStopped;\n{%- endmacro -%}"}]}, {"from": "invoke", "to": "exit", "label": "호출이 정상 반환하면 exit를 호출합니다.", "label_en": "When the call returns normally, call exit.", "evidence": [{"source": "lifetime/thread-stop", "sha256": "40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;\n\n\tstate_ = ProxyStopping;\n\n\tproxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);\n\n\tthread_.exit();\n\tthread_.wait();\n\n\tThread::current()->dispatchMessages(Message::Type::InvokeMessage, this);\n\n\tstate_ = ProxyStopped;\n{%- endmacro -%}"}]}, {"from": "exit", "to": "wait", "label": "exit가 정상 반환하면 wait를 호출합니다.", "label_en": "When exit returns normally, call wait.", "evidence": [{"source": "lifetime/thread-stop", "sha256": "40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;\n\n\tstate_ = ProxyStopping;\n\n\tproxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);\n\n\tthread_.exit();\n\tthread_.wait();\n\n\tThread::current()->dispatchMessages(Message::Type::InvokeMessage, this);\n\n\tstate_ = ProxyStopped;\n{%- endmacro -%}"}]}, {"from": "wait", "to": "dispatch", "label": "wait가 정상 반환하면 메시지를 처리합니다.", "label_en": "When wait returns normally, dispatch messages.", "evidence": [{"source": "lifetime/thread-stop", "sha256": "40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;\n\n\tstate_ = ProxyStopping;\n\n\tproxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);\n\n\tthread_.exit();\n\tthread_.wait();\n\n\tThread::current()->dispatchMessages(Message::Type::InvokeMessage, this);\n\n\tstate_ = ProxyStopped;\n{%- endmacro -%}"}]}, {"from": "dispatch", "to": "stopped", "label": "메시지 처리가 정상 반환하면 상태를 갱신합니다.", "label_en": "When message dispatch returns normally, update the state.", "evidence": [{"source": "lifetime/thread-stop", "sha256": "40789903a76fad82ef27bf4ecd2c79ed2c47d0e0ad9d6583fba12e9cf072884b", "quote": "{%- macro stop_thread_body() -%}\n\tASSERT(state_ != ProxyStopping);\n\tif (state_ != ProxyRunning)\n\t\treturn;\n\n\tstate_ = ProxyStopping;\n\n\tproxy_.invokeMethod(&ThreadProxy::stop, ConnectionTypeBlocking);\n\n\tthread_.exit();\n\tthread_.wait();\n\n\tThread::current()->dispatchMessages(Message::Type::InvokeMessage, this);\n\n\tstate_ = ProxyStopped;\n{%- endmacro -%}"}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78", "citation_binding_policy": "identifier-and-guard-boundaries-v2", "reused": true}, "isolated-destructor-guard": {"input_fingerprint": "60dc2d0834003d7bca851b52ce6acc7310ab46b9e1fe92429c33120052648906", "draft": {"nodes": [{"id": "check", "symbol": "if", "label": "Isolated 소멸자는 ipc_가 있는지 확인합니다.", "label_en": "The Isolated destructor checks whether ipc_ is present.", "shape": "decision", "quote_ids": ["isolated-dtor-only:0"]}, {"id": "send", "symbol": "sendAsync", "label": "Exit와 seq_++로 header를 만들고 msg를 구성한 뒤 ipc_->sendAsync(msg)를 호출합니다. 반환값은 검사하지 않습니다.", "label_en": "It builds header with Exit and seq_++, constructs msg, and calls ipc_->sendAsync(msg). It does not check the return value.", "shape": "process", "quote_ids": ["isolated-dtor-only:0"]}, {"id": "end", "symbol": "Isolated", "label": "Isolated 소멸자는 메시지 구성과 sendAsync 호출을 건너뛰고 본문을 마칩니다. return 문장은 없습니다.", "label_en": "The Isolated destructor skips message construction and the sendAsync call, then reaches the end of its body. There is no return statement.", "shape": "box", "quote_ids": ["isolated-dtor-only:0"]}], "edges": [{"from": "check", "to": "send", "label": "조건이 참이면 Exit 메시지 전송을 시도합니다.", "label_en": "If the condition is true, it attempts to send the Exit message.", "condition_ref": "c0:true", "quote_ids": ["isolated-dtor-only:0"]}, {"from": "check", "to": "end", "label": "조건이 거짓이면 if 본문을 건너뜁니다.", "label_en": "If the condition is false, it skips the if body.", "condition_ref": "c0:false", "quote_ids": ["isolated-dtor-only:0"]}]}, "graph": {"id": "isolated-destructor-guard", "topic": "lifetime", "kind": "flow", "title": "Isolated 소멸자의 IPC 분기", "question": "Isolated 소멸자는 ipc_가 없으면 어떤 구문을 건너뛰며, 있으면 어떤 Exit 전송을 시도합니까?", "condition_display": "inline", "nodes": [{"id": "check", "label": "Isolated 소멸자는 ipc_가 있는지 확인합니다.", "label_en": "The Isolated destructor checks whether ipc_ is present.", "shape": "decision", "evidence": [{"source": "lifetime/isolated-dtor-only", "sha256": "134a6b2cd3ed0e858c49bb1f3872af60ba1d44b3a32e60f2d2d0642a68865851", "quote": "{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}"}]}, {"id": "send", "label": "Exit와 seq_++로 header를 만들고 msg를 구성한 뒤 ipc_->sendAsync(msg)를 호출합니다. 반환값은 검사하지 않습니다.", "label_en": "It builds header with Exit and seq_++, constructs msg, and calls ipc_->sendAsync(msg). It does not check the return value.", "shape": "box", "evidence": [{"source": "lifetime/isolated-dtor-only", "sha256": "134a6b2cd3ed0e858c49bb1f3872af60ba1d44b3a32e60f2d2d0642a68865851", "quote": "{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}"}]}, {"id": "end", "label": "Isolated 소멸자는 메시지 구성과 sendAsync 호출을 건너뛰고 본문을 마칩니다. return 문장은 없습니다.", "label_en": "The Isolated destructor skips message construction and the sendAsync call, then reaches the end of its body. There is no return statement.", "shape": "box", "evidence": [{"source": "lifetime/isolated-dtor-only", "sha256": "134a6b2cd3ed0e858c49bb1f3872af60ba1d44b3a32e60f2d2d0642a68865851", "quote": "{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}"}]}], "edges": [{"from": "check", "to": "send", "label": "조건이 참이면 Exit 메시지 전송을 시도합니다. · ipc_ [true]", "label_en": "If the condition is true, it attempts to send the Exit message. · ipc_ [true]", "evidence": [{"source": "lifetime/isolated-dtor-only", "sha256": "134a6b2cd3ed0e858c49bb1f3872af60ba1d44b3a32e60f2d2d0642a68865851", "quote": "{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}"}]}, {"from": "check", "to": "end", "label": "조건이 거짓이면 if 본문을 건너뜁니다. · ipc_ [false]", "label_en": "If the condition is false, it skips the if body. · ipc_ [false]", "evidence": [{"source": "lifetime/isolated-dtor-only", "sha256": "134a6b2cd3ed0e858c49bb1f3872af60ba1d44b3a32e60f2d2d0642a68865851", "quote": "{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n}"}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78", "citation_binding_policy": "identifier-and-guard-boundaries-v2", "reused": true}, "module-load-error-branches": {"input_fingerprint": "4a374fe185ccba0cb22b2fafe2744e6e494eb158565db8a870434413d303db8e", "draft": {"nodes": [{"id": "valid", "symbol": "if", "label": "!valid_는 모듈이 유효하지 않다는 뜻인가요? 유효하지 않은 모듈에서 호출하면 오류입니다.", "label_en": "Does !valid_ mean the module is invalid? Calling this on an invalid module is an error.", "shape": "decision", "quote_ids": ["load:0"]}, {"id": "invalid", "symbol": "return", "label": "false를 반환합니다.", "label_en": "Return false.", "shape": "box", "quote_ids": ["load:0"]}, {"id": "loaded", "symbol": "if", "label": "loaded_는 모듈이 이미 로드되었다는 뜻인가요?", "label_en": "Does loaded_ mean the module is already loaded?", "shape": "decision", "quote_ids": ["load:1"]}, {"id": "already", "symbol": "return", "label": "true를 반환합니다.", "label_en": "Return true.", "shape": "box", "quote_ids": ["load:1"]}, {"id": "open", "symbol": "if", "label": "dlopen으로 얻은 dlHandle_에 대해 !dlHandle_는 열기 실패를 뜻하나요?", "label_en": "For dlHandle_ obtained by dlopen, does !dlHandle_ mean opening failed?", "shape": "decision", "quote_ids": ["load:2"]}, {"id": "open_failure", "symbol": "return", "label": "오류를 기록하고 false를 반환합니다.", "label_en": "Log the error and return false.", "shape": "box", "quote_ids": ["load:2"]}, {"id": "lookup", "symbol": "if", "label": "dlsym으로 얻은 symbol에 대해 !symbol은 심볼 탐색 실패를 뜻하나요?", "label_en": "For symbol obtained by dlsym, does !symbol mean the symbol lookup failed?", "shape": "decision", "quote_ids": ["load:3"]}, {"id": "lookup_failure", "symbol": "return", "label": "오류를 기록하고 dlclose로 dlHandle_을 닫은 뒤 nullptr로 설정하고 false를 반환합니다.", "label_en": "Log the error, close dlHandle_ with dlclose, set it to nullptr, and return false.", "shape": "box", "quote_ids": ["load:3"]}, {"id": "success", "symbol": "symbol", "label": "symbol로 ipaCreate_를 설정하고 loaded_를 true로 설정한 뒤 true를 반환합니다.", "label_en": "Set ipaCreate_ from symbol, set loaded_ to true, and return true.", "shape": "process", "quote_ids": ["load:3", "load:4", "load:5", "load:6"]}], "edges": [{"from": "valid", "to": "invalid", "label": "참이면 false를 반환합니다.", "label_en": "If true, return false.", "condition_ref": "c2:true", "quote_ids": ["load:0"]}, {"from": "valid", "to": "loaded", "label": "거짓이면 이미 로드되었는지 확인합니다.", "label_en": "If false, check whether it is already loaded.", "condition_ref": "c2:false", "quote_ids": ["load:0", "load:1"]}, {"from": "loaded", "to": "already", "label": "참이면 true를 반환합니다.", "label_en": "If true, return true.", "condition_ref": "c4:true", "quote_ids": ["load:1"]}, {"from": "loaded", "to": "open", "label": "거짓이면 dlopen으로 공유 객체를 엽니다.", "label_en": "If false, open the shared object with dlopen.", "condition_ref": "c4:false", "quote_ids": ["load:1", "load:2"]}, {"from": "open", "to": "open_failure", "label": "참이면 오류를 기록하고 false를 반환합니다.", "label_en": "If true, log the error and return false.", "condition_ref": "c0:true", "quote_ids": ["load:2"]}, {"from": "open", "to": "lookup", "label": "거짓이면 dlsym으로 ipaCreate를 찾습니다.", "label_en": "If false, look up ipaCreate with dlsym.", "condition_ref": "c0:false", "quote_ids": ["load:2", "load:3"]}, {"from": "lookup", "to": "lookup_failure", "label": "참이면 핸들을 정리하고 false를 반환합니다.", "label_en": "If true, clean up the handle and return false.", "condition_ref": "c1:true", "quote_ids": ["load:3"]}, {"from": "lookup", "to": "success", "label": "거짓이면 팩터리를 설정합니다.", "label_en": "If false, set the factory.", "condition_ref": "c1:false", "quote_ids": ["load:3", "load:4", "load:5", "load:6"]}]}, "graph": {"id": "module-load-error-branches", "topic": "errors", "kind": "flow", "title": "모듈 로드의 성공과 실패 반환", "question": "IPAModule::load는 기존 상태, dlopen과 dlsym 결과에 따라 어떤 값을 반환하고 무엇을 정리합니까?", "condition_display": "evidence", "nodes": [{"id": "valid", "label": "!valid_는 모듈이 유효하지 않다는 뜻인가요? 유효하지 않은 모듈에서 호출하면 오류입니다.", "label_en": "Does !valid_ mean the module is invalid? Calling this on an invalid module is an error.", "shape": "decision", "evidence": [{"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "\\brief Load the IPA implementation factory from the shared object\n *\n * The IPA module shared object implements an IPAInterface object to be used\n * by pipeline handlers. This function loads the factory function from the\n * shared object. Later, createInterface() can be called to instantiate the\n * IPAInterface.\n *\n * This function only needs to be called successfully once, after which\n * createInterface() can be called as many times as IPAInterface instances are\n * needed.\n *\n * Calling this function on an invalid module (as returned by isValid()) is\n * an error.\n *\n * \\return True if load was successful, or already loaded, and false otherwise\n */\nbool IPAModule::load()\n{\n\tif (!valid_)\n\t\treturn false;"}]}, {"id": "invalid", "label": "false를 반환합니다.", "label_en": "Return false.", "shape": "box", "evidence": [{"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "\\brief Load the IPA implementation factory from the shared object\n *\n * The IPA module shared object implements an IPAInterface object to be used\n * by pipeline handlers. This function loads the factory function from the\n * shared object. Later, createInterface() can be called to instantiate the\n * IPAInterface.\n *\n * This function only needs to be called successfully once, after which\n * createInterface() can be called as many times as IPAInterface instances are\n * needed.\n *\n * Calling this function on an invalid module (as returned by isValid()) is\n * an error.\n *\n * \\return True if load was successful, or already loaded, and false otherwise\n */\nbool IPAModule::load()\n{\n\tif (!valid_)\n\t\treturn false;"}]}, {"id": "loaded", "label": "loaded_는 모듈이 이미 로드되었다는 뜻인가요?", "label_en": "Does loaded_ mean the module is already loaded?", "shape": "decision", "evidence": [{"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "if (loaded_)\n\t\treturn true;"}]}, {"id": "already", "label": "true를 반환합니다.", "label_en": "Return true.", "shape": "box", "evidence": [{"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "if (loaded_)\n\t\treturn true;"}]}, {"id": "open", "label": "dlopen으로 얻은 dlHandle_에 대해 !dlHandle_는 열기 실패를 뜻하나요?", "label_en": "For dlHandle_ obtained by dlopen, does !dlHandle_ mean opening failed?", "shape": "decision", "evidence": [{"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "dlHandle_ = dlopen(libPath_.c_str(), RTLD_LAZY);\n\tif (!dlHandle_) {\n\t\tLOG(IPAModule, Error)\n\t\t\t<< \"Failed to open IPA module shared object: \"\n\t\t\t<< dlerror();\n\t\treturn false;\n\t}"}]}, {"id": "open_failure", "label": "오류를 기록하고 false를 반환합니다.", "label_en": "Log the error and return false.", "shape": "box", "evidence": [{"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "dlHandle_ = dlopen(libPath_.c_str(), RTLD_LAZY);\n\tif (!dlHandle_) {\n\t\tLOG(IPAModule, Error)\n\t\t\t<< \"Failed to open IPA module shared object: \"\n\t\t\t<< dlerror();\n\t\treturn false;\n\t}"}]}, {"id": "lookup", "label": "dlsym으로 얻은 symbol에 대해 !symbol은 심볼 탐색 실패를 뜻하나요?", "label_en": "For symbol obtained by dlsym, does !symbol mean the symbol lookup failed?", "shape": "decision", "evidence": [{"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "void *symbol = dlsym(dlHandle_, \"ipaCreate\");\n\tif (!symbol) {\n\t\tLOG(IPAModule, Error)\n\t\t\t<< \"Failed to load ipaCreate() from IPA module shared object: \"\n\t\t\t<< dlerror();\n\t\tdlclose(dlHandle_);\n\t\tdlHandle_ = nullptr;\n\t\treturn false;\n\t}"}]}, {"id": "lookup_failure", "label": "오류를 기록하고 dlclose로 dlHandle_을 닫은 뒤 nullptr로 설정하고 false를 반환합니다.", "label_en": "Log the error, close dlHandle_ with dlclose, set it to nullptr, and return false.", "shape": "box", "evidence": [{"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "void *symbol = dlsym(dlHandle_, \"ipaCreate\");\n\tif (!symbol) {\n\t\tLOG(IPAModule, Error)\n\t\t\t<< \"Failed to load ipaCreate() from IPA module shared object: \"\n\t\t\t<< dlerror();\n\t\tdlclose(dlHandle_);\n\t\tdlHandle_ = nullptr;\n\t\treturn false;\n\t}"}]}, {"id": "success", "label": "symbol로 ipaCreate_를 설정하고 loaded_를 true로 설정한 뒤 true를 반환합니다.", "label_en": "Set ipaCreate_ from symbol, set loaded_ to true, and return true.", "shape": "box", "evidence": [{"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "void *symbol = dlsym(dlHandle_, \"ipaCreate\");\n\tif (!symbol) {\n\t\tLOG(IPAModule, Error)\n\t\t\t<< \"Failed to load ipaCreate() from IPA module shared object: \"\n\t\t\t<< dlerror();\n\t\tdlclose(dlHandle_);\n\t\tdlHandle_ = nullptr;\n\t\treturn false;\n\t}"}, {"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "ipaCreate_ = reinterpret_cast<IPAIntfFactory>(symbol);"}, {"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "loaded_ = true;"}, {"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "return true;\n}"}]}], "edges": [{"from": "valid", "to": "invalid", "label": "참이면 false를 반환합니다. · !valid_ [true]", "label_en": "If true, return false. · !valid_ [true]", "evidence": [{"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "\\brief Load the IPA implementation factory from the shared object\n *\n * The IPA module shared object implements an IPAInterface object to be used\n * by pipeline handlers. This function loads the factory function from the\n * shared object. Later, createInterface() can be called to instantiate the\n * IPAInterface.\n *\n * This function only needs to be called successfully once, after which\n * createInterface() can be called as many times as IPAInterface instances are\n * needed.\n *\n * Calling this function on an invalid module (as returned by isValid()) is\n * an error.\n *\n * \\return True if load was successful, or already loaded, and false otherwise\n */\nbool IPAModule::load()\n{\n\tif (!valid_)\n\t\treturn false;"}]}, {"from": "valid", "to": "loaded", "label": "거짓이면 이미 로드되었는지 확인합니다. · !valid_ [false]", "label_en": "If false, check whether it is already loaded. · !valid_ [false]", "evidence": [{"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "\\brief Load the IPA implementation factory from the shared object\n *\n * The IPA module shared object implements an IPAInterface object to be used\n * by pipeline handlers. This function loads the factory function from the\n * shared object. Later, createInterface() can be called to instantiate the\n * IPAInterface.\n *\n * This function only needs to be called successfully once, after which\n * createInterface() can be called as many times as IPAInterface instances are\n * needed.\n *\n * Calling this function on an invalid module (as returned by isValid()) is\n * an error.\n *\n * \\return True if load was successful, or already loaded, and false otherwise\n */\nbool IPAModule::load()\n{\n\tif (!valid_)\n\t\treturn false;"}, {"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "if (loaded_)\n\t\treturn true;"}]}, {"from": "loaded", "to": "already", "label": "참이면 true를 반환합니다. · loaded_ [true]", "label_en": "If true, return true. · loaded_ [true]", "evidence": [{"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "if (loaded_)\n\t\treturn true;"}]}, {"from": "loaded", "to": "open", "label": "거짓이면 dlopen으로 공유 객체를 엽니다. · loaded_ [false]", "label_en": "If false, open the shared object with dlopen. · loaded_ [false]", "evidence": [{"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "if (loaded_)\n\t\treturn true;"}, {"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "dlHandle_ = dlopen(libPath_.c_str(), RTLD_LAZY);\n\tif (!dlHandle_) {\n\t\tLOG(IPAModule, Error)\n\t\t\t<< \"Failed to open IPA module shared object: \"\n\t\t\t<< dlerror();\n\t\treturn false;\n\t}"}]}, {"from": "open", "to": "open_failure", "label": "참이면 오류를 기록하고 false를 반환합니다. · !dlHandle_ [true]", "label_en": "If true, log the error and return false. · !dlHandle_ [true]", "evidence": [{"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "dlHandle_ = dlopen(libPath_.c_str(), RTLD_LAZY);\n\tif (!dlHandle_) {\n\t\tLOG(IPAModule, Error)\n\t\t\t<< \"Failed to open IPA module shared object: \"\n\t\t\t<< dlerror();\n\t\treturn false;\n\t}"}]}, {"from": "open", "to": "lookup", "label": "거짓이면 dlsym으로 ipaCreate를 찾습니다. · !dlHandle_ [false]", "label_en": "If false, look up ipaCreate with dlsym. · !dlHandle_ [false]", "evidence": [{"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "dlHandle_ = dlopen(libPath_.c_str(), RTLD_LAZY);\n\tif (!dlHandle_) {\n\t\tLOG(IPAModule, Error)\n\t\t\t<< \"Failed to open IPA module shared object: \"\n\t\t\t<< dlerror();\n\t\treturn false;\n\t}"}, {"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "void *symbol = dlsym(dlHandle_, \"ipaCreate\");\n\tif (!symbol) {\n\t\tLOG(IPAModule, Error)\n\t\t\t<< \"Failed to load ipaCreate() from IPA module shared object: \"\n\t\t\t<< dlerror();\n\t\tdlclose(dlHandle_);\n\t\tdlHandle_ = nullptr;\n\t\treturn false;\n\t}"}]}, {"from": "lookup", "to": "lookup_failure", "label": "참이면 핸들을 정리하고 false를 반환합니다. · !symbol [true]", "label_en": "If true, clean up the handle and return false. · !symbol [true]", "evidence": [{"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "void *symbol = dlsym(dlHandle_, \"ipaCreate\");\n\tif (!symbol) {\n\t\tLOG(IPAModule, Error)\n\t\t\t<< \"Failed to load ipaCreate() from IPA module shared object: \"\n\t\t\t<< dlerror();\n\t\tdlclose(dlHandle_);\n\t\tdlHandle_ = nullptr;\n\t\treturn false;\n\t}"}]}, {"from": "lookup", "to": "success", "label": "거짓이면 팩터리를 설정합니다. · !symbol [false]", "label_en": "If false, set the factory. · !symbol [false]", "evidence": [{"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "void *symbol = dlsym(dlHandle_, \"ipaCreate\");\n\tif (!symbol) {\n\t\tLOG(IPAModule, Error)\n\t\t\t<< \"Failed to load ipaCreate() from IPA module shared object: \"\n\t\t\t<< dlerror();\n\t\tdlclose(dlHandle_);\n\t\tdlHandle_ = nullptr;\n\t\treturn false;\n\t}"}, {"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "ipaCreate_ = reinterpret_cast<IPAIntfFactory>(symbol);"}, {"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "loaded_ = true;"}, {"source": "errors/load", "sha256": "a1e13344bfc27e191c6c24c682f3a088446d42c99b9497c6e831ab1b97b55619", "quote": "return true;\n}"}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78", "citation_binding_policy": "identifier-and-guard-boundaries-v2", "reused": true}, "synchronous-ipc-outcomes": {"input_fingerprint": "8669516d24c353e962262846c96df34e6eae00f2cce235c452d21000ed43293c", "draft": {"nodes": [{"id": "insert", "symbol": "insert", "label": "callData_.insert는 cookie를 키로, {response, false}를 값으로 삽입하려고 시도합니다.", "label_en": "callData_.insert attempts to insert cookie as the key and {response, false} as the value.", "shape": "process", "quote_ids": ["sync-call:0"]}, {"id": "iter", "symbol": "iter", "label": "result.first를 iter로 사용하며 result.second는 검사하지 않습니다. cookie가 이미 있으면 iter는 기존 항목을 가리킬 수 있습니다.", "label_en": "Use result.first as iter; do not test result.second. An existing cookie can make iter reference an existing entry.", "shape": "process", "quote_ids": ["sync-call:0"]}, {"id": "send", "symbol": "send", "label": "socket_의 send가 message를 보내고 결과를 ret에 저장합니다.", "label_en": "The send method of socket_ sends message and stores the result in ret.", "shape": "process", "quote_ids": ["sync-call:0"]}, {"id": "ret", "symbol": "ret", "label": "ret가 0이 아닌지 확인합니다.", "label_en": "Check whether ret is nonzero.", "shape": "decision", "quote_ids": ["sync-call:0"]}, {"id": "send_failure", "symbol": "erase", "label": "callData_의 erase가 iter 항목을 지운 뒤 ret를 반환합니다.", "label_en": "The erase method of callData_ removes the iter entry, then the function returns ret.", "shape": "process", "quote_ids": ["sync-call:0"]}, {"id": "start", "symbol": "start", "label": "timeout의 start가 2000ms 타이머를 시작합니다.", "label_en": "The start method of timeout starts a 2000ms timer.", "shape": "process", "quote_ids": ["sync-call:0"]}, {"id": "done", "symbol": "done", "label": "iter 항목의 done을 확인합니다.", "label_en": "Check done in the iter entry.", "shape": "decision", "quote_ids": ["sync-call:0"]}, {"id": "timer", "symbol": "isRunning", "label": "timeout의 isRunning으로 타이머가 실행 중인지 확인합니다.", "label_en": "Check whether the timer is running using the isRunning method of timeout.", "shape": "decision", "quote_ids": ["sync-call:0"]}, {"id": "timed_out", "symbol": "ETIMEDOUT", "label": "타임아웃을 기록하고 callData_에서 iter 항목을 지운 뒤 -ETIMEDOUT을 반환합니다.", "label_en": "Log the timeout, erase the iter entry from callData_, and return -ETIMEDOUT.", "shape": "process", "quote_ids": ["sync-call:0"]}, {"id": "events", "symbol": "processEvents", "label": "현재 스레드의 eventDispatcher가 processEvents를 실행합니다.", "label_en": "The eventDispatcher of the current thread runs processEvents.", "shape": "process", "quote_ids": ["sync-call:0"]}, {"id": "success", "symbol": "return", "label": "callData_에서 iter 항목을 지운 뒤 0을 반환합니다.", "label_en": "Erase the iter entry from callData_ and return 0.", "shape": "process", "quote_ids": ["sync-call:0"]}], "edges": [{"from": "insert", "to": "iter", "label": "삽입 시도 결과에서 반복자를 선택합니다.", "label_en": "Select the iterator from the insertion attempt result.", "condition_ref": "always", "quote_ids": ["sync-call:0"]}, {"from": "iter", "to": "send", "label": "선택한 뒤 message를 보냅니다.", "label_en": "Send message after the selection.", "condition_ref": "always", "quote_ids": ["sync-call:0"]}, {"from": "send", "to": "ret", "label": "송신 결과를 확인합니다.", "label_en": "Check the send result.", "condition_ref": "always", "quote_ids": ["sync-call:0"]}, {"from": "ret", "to": "send_failure", "label": "송신 결과가 0이 아니면 정리하고 반환합니다.", "label_en": "If the send result is nonzero, clean up and return.", "condition_ref": "c2:true", "quote_ids": ["sync-call:0"]}, {"from": "ret", "to": "start", "label": "송신 결과가 0이면 타이머를 시작합니다.", "label_en": "If the send result is zero, start the timer.", "condition_ref": "c2:false", "quote_ids": ["sync-call:0"]}, {"from": "start", "to": "done", "label": "타이머를 시작한 뒤 done을 확인합니다.", "label_en": "Check done after starting the timer.", "condition_ref": "always", "quote_ids": ["sync-call:0"]}, {"from": "done", "to": "timer", "label": "done이 false이면 타이머를 확인합니다.", "label_en": "If done is false, check the timer.", "condition_ref": "c0:true", "quote_ids": ["sync-call:0"]}, {"from": "done", "to": "success", "label": "done이 true이면 정리하고 반환합니다.", "label_en": "If done is true, clean up and return.", "condition_ref": "c0:false", "quote_ids": ["sync-call:0"]}, {"from": "timer", "to": "timed_out", "label": "타이머가 실행 중이 아니면 타임아웃을 처리합니다.", "label_en": "If the timer is not running, handle the timeout.", "condition_ref": "c1:true", "quote_ids": ["sync-call:0"]}, {"from": "timer", "to": "events", "label": "타이머가 실행 중이면 이벤트를 처리합니다.", "label_en": "If the timer is running, process events.", "condition_ref": "c1:false", "quote_ids": ["sync-call:0"]}, {"from": "events", "to": "done", "label": "이벤트를 처리한 뒤 done을 다시 확인합니다.", "label_en": "Check done again after processing events.", "condition_ref": "always", "quote_ids": ["sync-call:0"]}]}, "graph": {"id": "synchronous-ipc-outcomes", "topic": "errors", "kind": "flow", "title": "동기 call의 송신·대기·정리", "question": "call은 쿠키 항목 삽입 시도, 송신 결과와 done·타이머 상태에 따라 무엇을 정리하고 반환합니까?", "condition_display": "inline", "nodes": [{"id": "insert", "label": "callData_.insert는 cookie를 키로, {response, false}를 값으로 삽입하려고 시도합니다.", "label_en": "callData_.insert attempts to insert cookie as the key and {response, false} as the value.", "shape": "box", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"id": "iter", "label": "result.first를 iter로 사용하며 result.second는 검사하지 않습니다. cookie가 이미 있으면 iter는 기존 항목을 가리킬 수 있습니다.", "label_en": "Use result.first as iter; do not test result.second. An existing cookie can make iter reference an existing entry.", "shape": "box", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"id": "send", "label": "socket_의 send가 message를 보내고 결과를 ret에 저장합니다.", "label_en": "The send method of socket_ sends message and stores the result in ret.", "shape": "box", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"id": "ret", "label": "ret가 0이 아닌지 확인합니다.", "label_en": "Check whether ret is nonzero.", "shape": "decision", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"id": "send_failure", "label": "callData_의 erase가 iter 항목을 지운 뒤 ret를 반환합니다.", "label_en": "The erase method of callData_ removes the iter entry, then the function returns ret.", "shape": "box", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"id": "start", "label": "timeout의 start가 2000ms 타이머를 시작합니다.", "label_en": "The start method of timeout starts a 2000ms timer.", "shape": "box", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"id": "done", "label": "iter 항목의 done을 확인합니다.", "label_en": "Check done in the iter entry.", "shape": "decision", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"id": "timer", "label": "timeout의 isRunning으로 타이머가 실행 중인지 확인합니다.", "label_en": "Check whether the timer is running using the isRunning method of timeout.", "shape": "decision", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"id": "timed_out", "label": "타임아웃을 기록하고 callData_에서 iter 항목을 지운 뒤 -ETIMEDOUT을 반환합니다.", "label_en": "Log the timeout, erase the iter entry from callData_, and return -ETIMEDOUT.", "shape": "box", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"id": "events", "label": "현재 스레드의 eventDispatcher가 processEvents를 실행합니다.", "label_en": "The eventDispatcher of the current thread runs processEvents.", "shape": "box", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"id": "success", "label": "callData_에서 iter 항목을 지운 뒤 0을 반환합니다.", "label_en": "Erase the iter entry from callData_ and return 0.", "shape": "box", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}], "edges": [{"from": "insert", "to": "iter", "label": "삽입 시도 결과에서 반복자를 선택합니다.", "label_en": "Select the iterator from the insertion attempt result.", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"from": "iter", "to": "send", "label": "선택한 뒤 message를 보냅니다.", "label_en": "Send message after the selection.", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"from": "send", "to": "ret", "label": "송신 결과를 확인합니다.", "label_en": "Check the send result.", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"from": "ret", "to": "send_failure", "label": "송신 결과가 0이 아니면 정리하고 반환합니다. · ret [true]", "label_en": "If the send result is nonzero, clean up and return. · ret [true]", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"from": "ret", "to": "start", "label": "송신 결과가 0이면 타이머를 시작합니다. · ret [false]", "label_en": "If the send result is zero, start the timer. · ret [false]", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"from": "start", "to": "done", "label": "타이머를 시작한 뒤 done을 확인합니다.", "label_en": "Check done after starting the timer.", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"from": "done", "to": "timer", "label": "done이 false이면 타이머를 확인합니다. · !iter->second.done [true]", "label_en": "If done is false, check the timer. · !iter->second.done [true]", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"from": "done", "to": "success", "label": "done이 true이면 정리하고 반환합니다. · !iter->second.done [false]", "label_en": "If done is true, clean up and return. · !iter->second.done [false]", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"from": "timer", "to": "timed_out", "label": "타이머가 실행 중이 아니면 타임아웃을 처리합니다. · !timeout.isRunning() [true]", "label_en": "If the timer is not running, handle the timeout. · !timeout.isRunning() [true]", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"from": "timer", "to": "events", "label": "타이머가 실행 중이면 이벤트를 처리합니다. · !timeout.isRunning() [false]", "label_en": "If the timer is running, process events. · !timeout.isRunning() [false]", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}, {"from": "events", "to": "done", "label": "이벤트를 처리한 뒤 done을 다시 확인합니다.", "label_en": "Check done again after processing events.", "evidence": [{"source": "errors/sync-call", "sha256": "c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79", "quote": "int IPCPipeUnixSocket::call(const IPCUnixSocket::Payload &message,\n\t\t\t    IPCUnixSocket::Payload *response, uint32_t cookie)\n{\n\tTimer timeout;\n\tint ret;\n\n\tconst auto result = callData_.insert({ cookie, { response, false } });\n\tconst auto &iter = result.first;\n\n\tret = socket_->send(message);\n\tif (ret) {\n\t\tcallData_.erase(iter);\n\t\treturn ret;\n\t}\n\n\t/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe, Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn -ETIMEDOUT;\n\t\t}\n\n\t\tThread::current()->eventDispatcher()->processEvents();\n\t}\n\n\tcallData_.erase(iter);\n\n\treturn 0;\n}"}]}], "producer": "cli/codex/gpt-6.1-terra"}, "producer": "cli/codex/gpt-6.1-terra", "generation_commit": "c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78", "citation_binding_policy": "identifier-and-guard-boundaries-v2", "reused": true}}, "body_sha256": "184387e60c8396c9b9c13e8478ad7b16ee00b3cd6440e011d70cec827edce129"}
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

`IPAManager::IPAManager`는 사용자가 지정한 `ipa.module_paths`를 우선 검색하며, 빈 경로는 건너뛰고 나머지 경로마다 `addDir()`을 호출합니다. 지정된 경로 목록이 비어 있지 않지만 IPA를 하나도 찾지 못하면 경고를 기록합니다. 이어서 `utils::libcameraBuildPath()`가 빈 문자열이 아니면 그 경로에 `src/ipa`를 붙여 최대 깊이 2로 `addDir()`을 호출합니다. 마지막으로 설치된 시스템 경로 `IPA_MODULE_DIR`에 `addDir()`을 호출하고, 전체 검색에서 IPA를 하나도 찾지 못하면 경고를 기록합니다. `src/libcamera/ipa_manager.cpp:107`

<!-- sdd:visual:proxy-selection -->
### IPA 모듈 선택과 실행 경계

```mermaid
flowchart TB
%% sdd:translations {"Isolated 프록시": "Isolated proxy", "Threaded 프록시": "Threaded proxy", "false": "false", "isSignatureValid#40;m#41;?": "isSignatureValid#40;m#41;?", "nullptr: 생성 실패": "nullptr: creation failed", "true": "true", "생성 후 검사": "Check after construction", "아니오": "No", "예": "Yes", "이름·버전의 모듈이 있는가?": "Module matching name and <br/>version?", "프록시 반환": "Return proxy", "프록시가 유효한가?": "Is the proxy valid?"}
  v_module{"이름·버전의 모듈이 있는가?"}
  v_signature{"isSignatureValid#40;m#41;?"}
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
    모듈 선택, 서명 판정, 프록시 유효성의 분기를 구분하세요. 서명 판정의 구성 조건은 이어지는 설명에서 확인합니다.
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Module matching name and version?">이름·버전의 모듈이 있는가?</span> | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | <span data-sdd-label-en="isSignatureValid(m)?">isSignatureValid&#40;m&#41;?</span> | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | <span data-sdd-label-en="Threaded proxy">Threaded 프록시</span> | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | <span data-sdd-label-en="Isolated proxy">Isolated 프록시</span> | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | <span data-sdd-label-en="Is the proxy valid?">프록시가 유효한가?</span> | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | <span data-sdd-label-en="nullptr: creation failed">nullptr: 생성 실패</span> | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | <span data-sdd-label-en="Return proxy">프록시 반환</span> | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | <span data-sdd-label-en="No">아니오</span> | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | <span data-sdd-label-en="Yes">예</span> | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | <span data-sdd-label-en="true">true</span> | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | <span data-sdd-label-en="false">false</span> | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | <span data-sdd-label-en="Check after construction">생성 후 검사</span> | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | <span data-sdd-label-en="Check after construction">생성 후 검사</span> | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | <span data-sdd-label-en="No">아니오</span> | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
    | <span data-sdd-label-en="Yes">예</span> | [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) |
<!-- /sdd:visual:proxy-selection -->

`IPAModule::match`는 `info_.pipelineVersion`이 `minVersion` 이상이고 `maxVersion` 이하이며, `info_.name`과 `name`을 비교한 `strcmp`의 결과가 0이면 `true`를 반환합니다. 이 조건 중 하나라도 만족하지 않으면 `false`를 반환합니다. `src/libcamera/ipa_module.cpp:460`

`createIPA`는 먼저 `module(name, minVersion, maxVersion)`으로 모듈을 검색하고, 모듈이 없으면 `nullptr`을 반환합니다. 모듈이 있으면 `isSignatureValid(m)`이 참일 때 `T::Threaded` 프록시를, 거짓일 때 `T::Isolated` 프록시를 생성합니다. 생성한 프록시의 `isValid()`가 거짓이면 오류를 기록하고 `nullptr`을 반환하며, 참이면 프록시를 반환합니다. `include/libcamera/internal/ipa_manager.h:35`

`IPAManager::isSignatureValid`는 `HAVE_IPA_PUBKEY`가 활성화되지 않으면 `false`를 반환합니다. 활성화된 경우 `forceIsolation_`이 참이면 `false`를 반환하고, 그렇지 않으면 IPA 모듈 파일을 읽기 전용으로 엽니다. 파일을 열지 못하거나 파일 매핑 결과가 비어 있으면 `false`를 반환합니다. 두 단계를 통과하면 매핑된 데이터와 IPA 서명을 `pubKey_.verify`에 전달하고, 검사 결과를 로그에 기록한 뒤 그 결과를 반환합니다. `src/libcamera/ipa_manager.cpp:289`

근거 원문: [src/libcamera/ipa_manager.cpp:107](#source-7603cbafe8eef490) · [src/libcamera/ipa_module.cpp:460](#source-6e1525c1fc1aa55e) · [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) · [src/libcamera/ipa_manager.cpp:289](#source-532f8ffa194bd319)

## 스레드와 프로세스 경계

Threaded `init` 템플릿은 전달된 매개변수로 `ipa_->init()`을 직접 호출합니다. 반환형이 `void`가 아니면 호출 결과를 `_ret`에 저장하고 반환하며, `void`이면 값을 반환하지 않습니다. `init` 분기에서는 IPA 메서드를 호출한 뒤 `proxy_.moveToThread`에 스레드 객체 `thread_`의 주소를 전달합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:82`

<!-- sdd:visual:threaded-init-start -->
### Threaded init와 start의 호출 맥락

```mermaid
flowchart TB
%% sdd:translations {"Threaded 템플릿은 <br/>인터페이스에 해당 메서드가 <br/>있으면 init과 start를 <br/>각각의 분기로 생성합니다.": "The Threaded template <br/>generates separate init and <br/>start branches when those <br/>methods exist in the <br/>interface.", "init은 ipa#95;의 init 메서드를 <br/>직접 호출합니다.": "init directly calls the <br/>init method on ipa#95;.", "invokeMethod가 정상 <br/>복귀하면 그 결과를 <br/>반환합니다.": "It returns the result after <br/>invokeMethod returns <br/>normally.", "proxy#95;.moveToThread#40;#38;thread#95;<br/>#41;를 호출합니다.": "Call <br/>proxy#95;.moveToThread#40;#38;thread#95;<br/>#41;.", "proxy#95;의 invokeMethod가 <br/>ThreadProxy::start를 <br/>ConnectionTypeBlocking으로 <br/>호출합니다.": "invokeMethod on proxy#95; <br/>calls ThreadProxy::start <br/>with ConnectionTypeBlocking.", "start는 invokeMethod의 <br/>결과를 반환합니다.": "start returns the result of <br/>invokeMethod.", "start는 state#95;에 <br/>ProxyRunning을 저장합니다.": "start stores ProxyRunning <br/>in state#95;.", "start는 먼저 상태를 <br/>저장합니다.": "start first stores the <br/>state.", "start는 별도의 시작 경로를 <br/>실행합니다.": "start runs a separate <br/>startup path.", "thread#95;.start#40;#41;를 <br/>호출합니다.": "Call thread#95;.start#40;#41;.", "thread#95;.start가 정상 <br/>복귀하면 Blocking 호출을 <br/>수행합니다.": "After thread#95;.start returns <br/>normally, it makes the <br/>Blocking call.", "반환형이 void가 아니면 직접 <br/>호출한 결과를 반환하고, <br/>void이면 값 없이 반환합니다.": "It returns the direct call <br/>result for a non-void <br/>return type, or returns <br/>without a value for void.", "상태를 저장한 뒤 호출합니다.": "Make the call after storing <br/>the state.", "이동 호출이 정상 복귀하면 <br/>반환합니다.": "It returns after the move <br/>call returns normally.", "직접 호출이 정상 복귀하면 <br/>다음 호출로 이어집니다.": "Continue after the direct <br/>call returns normally.", "해당 메서드가 있으면 init <br/>분기를 생성합니다.": "It generates the init <br/>branch when the method <br/>exists.", "해당 메서드가 있으면 start <br/>분기를 생성합니다.": "It generates the start <br/>branch when the method <br/>exists."}
  v_threaded["Threaded 템플릿은 <br/>인터페이스에 해당 메서드가 <br/>있으면 init과 start를 <br/>각각의 분기로 생성합니다."]
  v_init["init은 ipa#95;의 init 메서드를 <br/>직접 호출합니다."]
  v_move["proxy#95;.moveToThread#40;#38;thread#95;<br/>#41;를 호출합니다."]
  v_init_return["반환형이 void가 아니면 직접 <br/>호출한 결과를 반환하고, <br/>void이면 값 없이 반환합니다."]
  v_start["start는 별도의 시작 경로를 <br/>실행합니다."]
  v_state["start는 state#95;에 <br/>ProxyRunning을 저장합니다."]
  v_thread["thread#95;.start#40;#41;를 <br/>호출합니다."]
  v_invoke["proxy#95;의 invokeMethod가 <br/>ThreadProxy::start를 <br/>ConnectionTypeBlocking으로 <br/>호출합니다."]
  v_start_return["start는 invokeMethod의 <br/>결과를 반환합니다."]
  v_threaded -->|"해당 메서드가 있으면 init <br/>분기를 생성합니다."| v_init
  v_threaded -->|"해당 메서드가 있으면 start <br/>분기를 생성합니다."| v_start
  v_init -->|"직접 호출이 정상 복귀하면 <br/>다음 호출로 이어집니다."| v_move
  v_move -->|"이동 호출이 정상 복귀하면 <br/>반환합니다."| v_init_return
  v_start -->|"start는 먼저 상태를 <br/>저장합니다."| v_state
  v_state -->|"상태를 저장한 뒤 호출합니다."| v_thread
  v_thread -->|"thread#95;.start가 정상 <br/>복귀하면 Blocking 호출을 <br/>수행합니다."| v_invoke
  v_invoke -->|"invokeMethod가 정상 <br/>복귀하면 그 결과를 <br/>반환합니다."| v_start_return
```

[Mermaid 원문](ipa.threaded-init-start.mmd)

??? note "그림 근거와 확인 범위"
    Threaded init와 start는 각각 직접 호출·스레드 이동·작업 스레드 시작·Blocking 호출과 반환을 어떻게 구성합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="The Threaded template generates separate init and start branches when those methods exist in the interface.">Threaded 템플릿은 인터페이스에 해당 메서드가 있으면 init과 start를 각각의 분기로 생성합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | <span data-sdd-label-en="init directly calls the init method on ipa_.">init은 ipa&#95;의 init 메서드를 직접 호출합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:82](#source-9d9c3049e90e4238) |
    | <span data-sdd-label-en="Call proxy_.moveToThread(&amp;thread_).">proxy&#95;.moveToThread&#40;&amp;thread&#95;&#41;를 호출합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:82](#source-9d9c3049e90e4238) |
    | <span data-sdd-label-en="It returns the direct call result for a non-void return type, or returns without a value for void.">반환형이 void가 아니면 직접 호출한 결과를 반환하고, void이면 값 없이 반환합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:82](#source-9d9c3049e90e4238) |
    | <span data-sdd-label-en="start runs a separate startup path.">start는 별도의 시작 경로를 실행합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93](#source-7670edf527118b0e) |
    | <span data-sdd-label-en="start stores ProxyRunning in state_.">start는 state&#95;에 ProxyRunning을 저장합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93](#source-7670edf527118b0e) |
    | <span data-sdd-label-en="Call thread_.start().">thread&#95;.start&#40;&#41;를 호출합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93](#source-7670edf527118b0e) |
    | <span data-sdd-label-en="invokeMethod on proxy_ calls ThreadProxy::start with ConnectionTypeBlocking.">proxy&#95;의 invokeMethod가 ThreadProxy::start를 ConnectionTypeBlocking으로 호출합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93](#source-7670edf527118b0e) |
    | <span data-sdd-label-en="start returns the result of invokeMethod.">start는 invokeMethod의 결과를 반환합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93](#source-7670edf527118b0e) |
    | <span data-sdd-label-en="It generates the init branch when the method exists.">해당 메서드가 있으면 init 분기를 생성합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:82](#source-9d9c3049e90e4238) |
    | <span data-sdd-label-en="It generates the start branch when the method exists.">해당 메서드가 있으면 start 분기를 생성합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93](#source-7670edf527118b0e) |
    | <span data-sdd-label-en="Continue after the direct call returns normally.">직접 호출이 정상 복귀하면 다음 호출로 이어집니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:82](#source-9d9c3049e90e4238) |
    | <span data-sdd-label-en="It returns after the move call returns normally.">이동 호출이 정상 복귀하면 반환합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:82](#source-9d9c3049e90e4238) |
    | <span data-sdd-label-en="start first stores the state.">start는 먼저 상태를 저장합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93](#source-7670edf527118b0e) |
    | <span data-sdd-label-en="Make the call after storing the state.">상태를 저장한 뒤 호출합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93](#source-7670edf527118b0e) |
    | <span data-sdd-label-en="After thread_.start returns normally, it makes the Blocking call.">thread&#95;.start가 정상 복귀하면 Blocking 호출을 수행합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93](#source-7670edf527118b0e) |
    | <span data-sdd-label-en="It returns the result after invokeMethod returns normally.">invokeMethod가 정상 복귀하면 그 결과를 반환합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93](#source-7670edf527118b0e) |
<!-- /sdd:visual:threaded-init-start -->

<!-- sdd:visual:interface-creation-outcomes -->
### Threaded 생성자의 인터페이스 유지

```mermaid
flowchart TB
%% sdd:translations {"ipa#95;가 변환한 인터페이스를 <br/>std::unique#95;ptr로 <br/>소유합니다.": "ipa#95; owns the cast <br/>interface through a <br/>std::unique#95;ptr.", "setIPA가 정상적으로 <br/>반환하면 각 이벤트를 <br/>연결합니다.": "After setIPA returns <br/>normally, the constructor <br/>connects each event.", "생성자가 createInterface를 <br/>호출하고 ipai를 확인합니다.": "The constructor calls <br/>createInterface and checks <br/>ipai.", "생성자가 ipa#95;.get#40;#41;의 <br/>포인터를 proxy#95;.setIPA에 <br/>넘깁니다.": "The constructor passes the <br/>pointer from ipa#95;.get#40;#41; to <br/>proxy#95;.setIPA.", "생성자가 ipam의 load를 <br/>호출하고 결과를 확인합니다.": "The constructor calls load <br/>on ipam and checks the <br/>result.", "생성자가 valid#95;에 true를 <br/>저장하고 정상적으로 <br/>마칩니다.": "The constructor stores true <br/>in valid#95; and finishes <br/>normally.", "생성자가 각 인터페이스 <br/>이벤트를 this의 해당 <br/>Handler에 connect로 <br/>연결합니다.": "The constructor uses <br/>connect to link each <br/>interface event to its <br/>corresponding Handler on <br/>this.", "생성자가 오류를 기록하고 <br/>반환합니다.": "The constructor logs an <br/>error and returns.", "생성자가 즉시 반환합니다.": "The constructor returns <br/>immediately.", "소유한 인터페이스의 <br/>포인터를 setIPA에 넘깁니다.": "The constructor passes a <br/>pointer to the owned <br/>interface to setIPA.", "이벤트 연결을 마치면 <br/>valid#95;에 true를 저장합니다.": "After connecting the <br/>events, the constructor <br/>stores true in valid#95;.", "조건이 거짓이면 <br/>createInterface를 <br/>호출합니다. · #33;ipam-#62;load#40;#41; <br/>#91;false#93;": "If the condition is false, <br/>the constructor calls <br/>createInterface. · <br/>#33;ipam-#62;load#40;#41; #91;false#93;", "조건이 거짓이면 ipa#95;가 <br/>인터페이스를 소유합니다. · <br/>#33;ipai #91;false#93;": "If the condition is false, <br/>ipa#95; owns the interface. · <br/>#33;ipai #91;false#93;", "조건이 참이면 오류를 <br/>기록하고 반환합니다. · <br/>#33;ipai #91;true#93;": "If the condition is true, <br/>the constructor logs an <br/>error and returns. · #33;ipai <br/>#91;true#93;", "조건이 참이면 즉시 <br/>반환합니다. · #33;ipam-#62;load#40;#41; <br/>#91;true#93;": "If the condition is true, <br/>the constructor returns <br/>immediately. · <br/>#33;ipam-#62;load#40;#41; #91;true#93;"}
  v_load{"생성자가 ipam의 load를 <br/>호출하고 결과를 확인합니다."}
  v_load_return["생성자가 즉시 반환합니다."]
  v_interface{"생성자가 createInterface를 <br/>호출하고 ipai를 확인합니다."}
  v_error_return["생성자가 오류를 기록하고 <br/>반환합니다."]
  v_own["ipa#95;가 변환한 인터페이스를 <br/>std::unique#95;ptr로 <br/>소유합니다."]
  v_pointer["생성자가 ipa#95;.get#40;#41;의 <br/>포인터를 proxy#95;.setIPA에 <br/>넘깁니다."]
  v_events["생성자가 각 인터페이스 <br/>이벤트를 this의 해당 <br/>Handler에 connect로 <br/>연결합니다."]
  v_valid["생성자가 valid#95;에 true를 <br/>저장하고 정상적으로 <br/>마칩니다."]
  v_load -->|"조건이 참이면 즉시 <br/>반환합니다. · #33;ipam-#62;load#40;#41; <br/>#91;true#93;"| v_load_return
  v_load -->|"조건이 거짓이면 <br/>createInterface를 <br/>호출합니다. · #33;ipam-#62;load#40;#41; <br/>#91;false#93;"| v_interface
  v_interface -->|"조건이 참이면 오류를 <br/>기록하고 반환합니다. · <br/>#33;ipai #91;true#93;"| v_error_return
  v_interface -->|"조건이 거짓이면 ipa#95;가 <br/>인터페이스를 소유합니다. · <br/>#33;ipai #91;false#93;"| v_own
  v_own -->|"소유한 인터페이스의 <br/>포인터를 setIPA에 넘깁니다."| v_pointer
  v_pointer -->|"setIPA가 정상적으로 <br/>반환하면 각 이벤트를 <br/>연결합니다."| v_events
  v_events -->|"이벤트 연결을 마치면 <br/>valid#95;에 true를 저장합니다."| v_valid
```

[Mermaid 원문](ipa.interface-creation-outcomes.mmd)

??? note "그림 근거와 확인 범위"
    Threaded 생성자는 load와 createInterface 결과에 따라 언제 반환하며 인터페이스를 어떻게 보유·연결합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="The constructor calls load on ipam and checks the result.">생성자가 ipam의 load를 호출하고 결과를 확인합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | <span data-sdd-label-en="The constructor returns immediately.">생성자가 즉시 반환합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | <span data-sdd-label-en="The constructor calls createInterface and checks ipai.">생성자가 createInterface를 호출하고 ipai를 확인합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | <span data-sdd-label-en="The constructor logs an error and returns.">생성자가 오류를 기록하고 반환합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | <span data-sdd-label-en="ipa_ owns the cast interface through a std::unique_ptr.">ipa&#95;가 변환한 인터페이스를 std::unique&#95;ptr로 소유합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | <span data-sdd-label-en="The constructor passes the pointer from ipa_.get() to proxy_.setIPA.">생성자가 ipa&#95;.get&#40;&#41;의 포인터를 proxy&#95;.setIPA에 넘깁니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | <span data-sdd-label-en="The constructor uses connect to link each interface event to its corresponding Handler on this.">생성자가 각 인터페이스 이벤트를 this의 해당 Handler에 connect로 연결합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | <span data-sdd-label-en="The constructor stores true in valid_ and finishes normally.">생성자가 valid&#95;에 true를 저장하고 정상적으로 마칩니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | <span data-sdd-label-en="If the condition is true, the constructor returns immediately. · !ipam-&gt;load() [true]">조건이 참이면 즉시 반환합니다. · &#33;ipam-&gt;load&#40;&#41; &#91;true&#93;</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | <span data-sdd-label-en="If the condition is false, the constructor calls createInterface. · !ipam-&gt;load() [false]">조건이 거짓이면 createInterface를 호출합니다. · &#33;ipam-&gt;load&#40;&#41; &#91;false&#93;</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | <span data-sdd-label-en="If the condition is true, the constructor logs an error and returns. · !ipai [true]">조건이 참이면 오류를 기록하고 반환합니다. · &#33;ipai &#91;true&#93;</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | <span data-sdd-label-en="If the condition is false, ipa_ owns the interface. · !ipai [false]">조건이 거짓이면 ipa&#95;가 인터페이스를 소유합니다. · &#33;ipai &#91;false&#93;</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | <span data-sdd-label-en="The constructor passes a pointer to the owned interface to setIPA.">소유한 인터페이스의 포인터를 setIPA에 넘깁니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | <span data-sdd-label-en="After setIPA returns normally, the constructor connects each event.">setIPA가 정상적으로 반환하면 각 이벤트를 연결합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
    | <span data-sdd-label-en="After connecting the events, the constructor stores true in valid_.">이벤트 연결을 마치면 valid&#95;에 true를 저장합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) |
<!-- /sdd:visual:interface-creation-outcomes -->

<!-- sdd:visual:isolated-constructor-connection -->
### 격리 IPA 프록시의 연결 분기와 IPC 소유권

```mermaid
flowchart TB
%% sdd:translations {"IPCPipeUnixSocket에 모듈 <br/>경로와 worker 경로를 <br/>전달합니다.": "Pass the module path and <br/>worker path to <br/>IPCPipeUnixSocket.", "IPCPipe를 만들지 못했다는 <br/>별도의 오류 로그를 남기고 <br/>반환합니다.": "Log a separate error for <br/>the failure to create <br/>IPCPipe and return.", "isConnected로 연결 여부를 <br/>검사합니다.": "Check the connection with <br/>isConnected.", "proxyWorkerPath가 비었는지 <br/>검사합니다.": "Check whether <br/>proxyWorkerPath is empty.", "recv.connect에 this와 <br/>#38;{{proxy#95;name}}Isolated::<br/>recvMessage를 연결합니다.": "Connect recv using this and <br/>#38;{{proxy#95;name}}Isolated::<br/>recvMessage.", "resolvePath에 <br/>#34;{{module#95;name}}#95;ipa#95;proxy#34;<br/>를 전달해 worker 경로를 <br/>찾습니다.": "Pass <br/>#34;{{module#95;name}}#95;ipa#95;proxy#34; <br/>to resolvePath to find the <br/>worker path.", "std::move#40;ipc#41;로 연결의 <br/>소유권을 ipc#95;에 옮깁니다.": "Transfer ownership of the <br/>connection to ipc#95; with <br/>std::move#40;ipc#41;.", "valid#95;에 true를 저장합니다.": "Store true in valid#95;.", "worker 경로를 찾지 못했다는 <br/>오류 로그를 남기고 <br/>반환합니다.": "Log the failure to get the <br/>worker path and return.", "경로가 비어 있으면 오류를 <br/>처리합니다. · <br/>proxyWorkerPath.empty#40;#41; <br/>#91;true#93;": "Handle the error if the <br/>path is empty. · <br/>proxyWorkerPath.empty#40;#41; <br/>#91;true#93;", "경로가 비어 있지 않으면 <br/>IPCPipeUnixSocket을 <br/>만듭니다. · <br/>proxyWorkerPath.empty#40;#41; <br/>#91;false#93;": "Create IPCPipeUnixSocket if <br/>the path is not empty. · <br/>proxyWorkerPath.empty#40;#41; <br/>#91;false#93;", "생성한 ipc의 연결 여부를 <br/>검사합니다.": "Check the connection of the <br/>created ipc.", "소유권을 옮긴 뒤 valid#95;를 <br/>설정합니다.": "Set valid#95; after <br/>transferring ownership.", "수신 핸들러를 연결한 뒤 <br/>소유권을 옮깁니다.": "Transfer ownership after <br/>connecting the receive <br/>handler.", "연결되지 않았으면 오류를 <br/>처리합니다. · <br/>#33;ipc-#62;isConnected#40;#41; #91;true#93;": "Handle the error if it is <br/>not connected. · <br/>#33;ipc-#62;isConnected#40;#41; #91;true#93;", "연결된 것으로 검사되면 수신 <br/>핸들러를 연결합니다. · <br/>#33;ipc-#62;isConnected#40;#41; #91;false#93;": "Connect the receive handler <br/>if the check reports a <br/>connection. · <br/>#33;ipc-#62;isConnected#40;#41; #91;false#93;", "찾은 경로를 검사합니다.": "Check the resolved path."}
  v_resolve["resolvePath에 <br/>#34;{{module#95;name}}#95;ipa#95;proxy#34;<br/>를 전달해 worker 경로를 <br/>찾습니다."]
  v_path_check{"proxyWorkerPath가 비었는지 <br/>검사합니다."}
  v_path_failure["worker 경로를 찾지 못했다는 <br/>오류 로그를 남기고 <br/>반환합니다."]
  v_create["IPCPipeUnixSocket에 모듈 <br/>경로와 worker 경로를 <br/>전달합니다."]
  v_connection_check{"isConnected로 연결 여부를 <br/>검사합니다."}
  v_connection_failure["IPCPipe를 만들지 못했다는 <br/>별도의 오류 로그를 남기고 <br/>반환합니다."]
  v_connect["recv.connect에 this와 <br/>#38;{{proxy#95;name}}Isolated::<br/>recvMessage를 연결합니다."]
  v_transfer["std::move#40;ipc#41;로 연결의 <br/>소유권을 ipc#95;에 옮깁니다."]
  v_valid["valid#95;에 true를 저장합니다."]
  v_resolve -->|"찾은 경로를 검사합니다."| v_path_check
  v_path_check -->|"경로가 비어 있으면 오류를 <br/>처리합니다. · <br/>proxyWorkerPath.empty#40;#41; <br/>#91;true#93;"| v_path_failure
  v_path_check -->|"경로가 비어 있지 않으면 <br/>IPCPipeUnixSocket을 <br/>만듭니다. · <br/>proxyWorkerPath.empty#40;#41; <br/>#91;false#93;"| v_create
  v_create -->|"생성한 ipc의 연결 여부를 <br/>검사합니다."| v_connection_check
  v_connection_check -->|"연결되지 않았으면 오류를 <br/>처리합니다. · <br/>#33;ipc-#62;isConnected#40;#41; #91;true#93;"| v_connection_failure
  v_connection_check -->|"연결된 것으로 검사되면 수신 <br/>핸들러를 연결합니다. · <br/>#33;ipc-#62;isConnected#40;#41; #91;false#93;"| v_connect
  v_connect -->|"수신 핸들러를 연결한 뒤 <br/>소유권을 옮깁니다."| v_transfer
  v_transfer -->|"소유권을 옮긴 뒤 valid#95;를 <br/>설정합니다."| v_valid
```

[Mermaid 원문](ipa.isolated-constructor-connection.mmd)

??? note "그림 근거와 확인 범위"
    Isolated 생성자는 worker 경로와 IPC 연결의 실패를 어떻게 처리하고, 성공한 연결의 소유권을 어떻게 옮깁니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Pass &quot;{{module_name}}_ipa_proxy&quot; to resolvePath to find the worker path.">resolvePath에 &quot;{{module&#95;name}}&#95;ipa&#95;proxy&quot;를 전달해 worker 경로를 찾습니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | <span data-sdd-label-en="Check whether proxyWorkerPath is empty.">proxyWorkerPath가 비었는지 검사합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | <span data-sdd-label-en="Log the failure to get the worker path and return.">worker 경로를 찾지 못했다는 오류 로그를 남기고 반환합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | <span data-sdd-label-en="Pass the module path and worker path to IPCPipeUnixSocket.">IPCPipeUnixSocket에 모듈 경로와 worker 경로를 전달합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | <span data-sdd-label-en="Check the connection with isConnected.">isConnected로 연결 여부를 검사합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | <span data-sdd-label-en="Log a separate error for the failure to create IPCPipe and return.">IPCPipe를 만들지 못했다는 별도의 오류 로그를 남기고 반환합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | <span data-sdd-label-en="Connect recv using this and &amp;{{proxy_name}}Isolated::recvMessage.">recv.connect에 this와 &amp;{{proxy&#95;name}}Isolated::recvMessage를 연결합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | <span data-sdd-label-en="Transfer ownership of the connection to ipc_ with std::move(ipc).">std::move&#40;ipc&#41;로 연결의 소유권을 ipc&#95;에 옮깁니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | <span data-sdd-label-en="Store true in valid_.">valid&#95;에 true를 저장합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | <span data-sdd-label-en="Check the resolved path.">찾은 경로를 검사합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | <span data-sdd-label-en="Handle the error if the path is empty. · proxyWorkerPath.empty() [true]">경로가 비어 있으면 오류를 처리합니다. · proxyWorkerPath.empty&#40;&#41; &#91;true&#93;</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | <span data-sdd-label-en="Create IPCPipeUnixSocket if the path is not empty. · proxyWorkerPath.empty() [false]">경로가 비어 있지 않으면 IPCPipeUnixSocket을 만듭니다. · proxyWorkerPath.empty&#40;&#41; &#91;false&#93;</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | <span data-sdd-label-en="Check the connection of the created ipc.">생성한 ipc의 연결 여부를 검사합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | <span data-sdd-label-en="Handle the error if it is not connected. · !ipc-&gt;isConnected() [true]">연결되지 않았으면 오류를 처리합니다. · &#33;ipc-&gt;isConnected&#40;&#41; &#91;true&#93;</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | <span data-sdd-label-en="Connect the receive handler if the check reports a connection. · !ipc-&gt;isConnected() [false]">연결된 것으로 검사되면 수신 핸들러를 연결합니다. · &#33;ipc-&gt;isConnected&#40;&#41; &#91;false&#93;</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | <span data-sdd-label-en="Transfer ownership after connecting the receive handler.">수신 핸들러를 연결한 뒤 소유권을 옮깁니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
    | <span data-sdd-label-en="Set valid_ after transferring ownership.">소유권을 옮긴 뒤 valid&#95;를 설정합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) |
<!-- /sdd:visual:isolated-constructor-connection -->

Threaded `start` 템플릿 분기는 `state_`를 `ProxyRunning`으로 설정한 뒤 `thread_.start()`를 호출해 worker 스레드를 시작합니다. 이어서 `proxy_.invokeMethod()`로 `ThreadProxy::start`를 `ConnectionTypeBlocking` 연결 유형과 생성된 매개변수로 호출하고 그 반환값을 반환합니다. `{{proxy_name}}Threaded`의 메서드에서 `init`, `start`, `stop`을 제외한 일반 동기 분기는 전달받은 인자로 `ipa_`의 같은 이름의 메서드를 직접 호출하고 그 반환값을 반환합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93`, `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:75`

비동기 메서드 분기는 `ASSERT` 매크로에 검사식 `state_ == ProxyRunning`을 전달합니다. 검사식이 거짓이면 `ASSERT`는 `Fatal` 수준의 오류 메시지를 기록하고 프로그램 실행을 중단합니다. `log.h`를 포함하기 전에 `NDEBUG`가 정의되어 있으면 `ASSERT`는 코드를 생성하지 않습니다. Threaded 비동기 분기에서 `proxy_.invokeMethod`는 `ThreadProxy` 메서드를 전달할 때 연결 유형으로 `ConnectionTypeQueued`를 사용합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:109`, `src/libcamera/base/log.cpp:1044`

`{{proxy_name}}Threaded` 생성자는 `ipam->load()`를 호출합니다. `load()`가 거짓을 반환하면 생성자에서 즉시 반환합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:55`

`Threaded` 생성자는 `load()`가 성공한 경우에만 `createInterface()`를 호출합니다. 반환된 포인터가 없으면 `ipam->path()`를 포함한 오류를 기록하고 반환합니다. 포인터가 있으면 인터페이스를 `unique_ptr`로 소유하고 `proxy_.setIPA(ipa_.get())`에 포인터를 넘깁니다. 이어서 각 이벤트를 수신 객체 `this`의 해당 `Handler` 메서드에 `connect`하고 `valid_`를 `true`로 설정합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48`

`{{proxy_name}}Isolated` 생성자는 `resolvePath("{{module_name}}_ipa_proxy")`로 워커 경로를 찾고, 경로가 비어 있으면 오류를 기록하고 반환합니다. 이어서 `IPCPipeUnixSocket`을 `ipam->path().c_str()`와 `proxyWorkerPath.c_str()` 인자로 생성하며, `isConnected()`가 거짓이면 오류를 기록하고 반환합니다. 연결에 성공하면 `recv.connect`에 수신 객체 `this`와 콜백 `&{{proxy_name}}Isolated::recvMessage`를 연결하고, `std::move`로 `ipc`의 소유권을 `ipc_`에 옮긴 뒤 `valid_`에 `true`를 저장합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130`

`IPAProxy::resolvePath`는 먼저 `execPaths_`를 순서대로 살펴보며 빈 디렉터리는 건너뛰고, `file`을 붙인 경로에 실행 권한이 있으면 그 경로를 반환합니다. 이후 `utils::libcameraBuildPath()`가 빈 문자열이 아니면 빌드 디렉터리의 `src/libcamera/proxy/worker`를 확인하고, 빈 문자열이면 설치 디렉터리 `IPA_PROXY_DIR`을 확인합니다. 선택한 디렉터리에서 실행 권한이 있는 경로를 찾으면 그 경로를 반환하고, 찾지 못하면 빈 문자열을 반환합니다. `src/libcamera/ipa_proxy.cpp:204`

`readyRead`는 소켓에서 페이로드를 수신하다가 오류가 나면 로그를 남기고 반환합니다. 수신한 데이터가 `IPCMessage::Header`보다 짧아도 로그를 남기고 반환합니다. 그다음 메시지의 `cookie`로 `callData_`에서 대기 항목을 찾고, 일치하는 항목이 있으면 페이로드를 응답으로 이동한 뒤 `done`을 `true`로 설정하고 반환합니다. `src/libcamera/ipc_pipe_unixsocket.cpp:84`

`IPCPipeUnixSocket::sendAsync`는 `data.payload()`를 `socket_->send`로 전송하고 반환값을 `ret`에 저장합니다. `ret`이 0이 아니면 오류를 기록하고 `ret`을 반환합니다. 그렇지 않으면 0을 반환합니다. `src/libcamera/ipc_pipe_unixsocket.cpp:73`

근거 원문: [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) · [src/libcamera/ipa_proxy.cpp:204](#source-59a673fb7c43c0e0) · [src/libcamera/ipc_pipe_unixsocket.cpp:27](#source-f0268126d3f8c2bc) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:75](#source-542f7efc12af7917) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93](#source-7670edf527118b0e) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:109](#source-f6afc431ed47a72a) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:82](#source-9d9c3049e90e4238) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:55](#source-60c70cd011db2353) · [src/libcamera/ipc_pipe_unixsocket.cpp:73](#source-6fafe97ae651cb83) · [src/libcamera/ipc_pipe_unixsocket.cpp:84](#source-7f9e84d5315c5882) · [src/libcamera/base/log.cpp:1044](#source-bae93ab8b66697ce)

## 프레임 입력과 결과 인터페이스

`IPAIPU3Interface`는 `[async]` 메서드로 `queueRequest(frame, controls)`, `computeParams(frame, bufferId)`, `processStats(frame, frameTimestamp, bufferId, sensorControls)`를 선언합니다. `IPAIPU3EventInterface`는 `paramsComputed(frame)`, `metadataReady(frame, metadata)`, `setSensorControls(frame, sensorControls, lensControls)`를 선언합니다. `include/libcamera/ipa/ipu3.mojom:19`

`IPARkISP1Interface`는 `[async]` 메서드로 `queueRequest(frame, reqControls)`, `computeParams(frame, bufferId)`, `processStats(frame, bufferId, sensorControls)`를 선언합니다. `IPARkISP1EventInterface`는 `paramsComputed(frame, bytesused)`, `metadataReady(frame, metadata)`, `setSensorControls(frame, sensorControls)`를 선언합니다. `include/libcamera/ipa/rkisp1.mojom:17`

근거 원문: [include/libcamera/ipa/ipu3.mojom:19](#source-5a4a0da4800968a4) · [include/libcamera/ipa/rkisp1.mojom:17](#source-7a01de2477d6466e)

## IPA 객체와 종료 순서

호출자는 유효한 모듈에서 `load()`를 한 번 성공한 뒤 필요한 `IPAInterface` 인스턴스 수만큼 `createInterface()`를 호출할 수 있습니다. Threaded 프록시의 `stop`은 먼저 상태가 `ProxyStopping`이 아닌지 단언하고, `ProxyRunning`이 아니면 반환합니다. 실행 중이면 상태를 `ProxyStopping`으로 바꾸고 `ThreadProxy::stop`을 `ConnectionTypeBlocking`으로 호출한 다음 `thread_.exit()`와 `thread_.wait()`를 순서대로 호출합니다. 이어 현재 스레드에서 이 프록시의 `InvokeMessage`를 디스패치하고 상태를 `ProxyStopped`로 바꿉니다. `src/libcamera/ipa_module.cpp:390`, `utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25`, `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48`

<!-- sdd:visual:threaded-stop-order -->
### Threaded 정지의 상태와 순서

```mermaid
flowchart TB
%% sdd:translations {"ASSERT 뒤에 별도의 상태 <br/>검사가 나옵니다.": "A separate state check <br/>follows ASSERT.", "ASSERT 뒤에서 state#95;가 <br/>ProxyRunning이 아닌지 <br/>검사합니다.": "After ASSERT, check whether <br/>state#95; is not ProxyRunning.", "dispatchMessages가 정상 <br/>반환하면 state#95;를 <br/>ProxyStopped로 갱신합니다.": "When dispatchMessages <br/>returns normally, update <br/>state#95; to ProxyStopped.", "exit가 정상 반환하면 wait를 <br/>호출합니다.": "When exit returns normally, <br/>call wait.", "proxy#95;의 invokeMethod로 <br/>ThreadProxy::stop을 <br/>ConnectionTypeBlocking으로 <br/>동기 호출합니다.": "Call ThreadProxy::stop <br/>synchronously through <br/>proxy#95;#39;s invokeMethod with <br/>ConnectionTypeBlocking.", "thread#95;의 wait를 호출해 <br/>스레드 종료를 기다립니다.": "Call wait on thread#95; to <br/>wait for the thread to <br/>finish.", "wait가 정상 반환하면 <br/>메시지를 처리합니다.": "When wait returns normally, <br/>dispatch messages.", "동기 호출이 정상 반환하면 <br/>thread#95;의 exit를 호출합니다.": "When the synchronous call <br/>returns normally, call exit <br/>on thread#95;.", "먼저 ASSERT로 state#95;가 <br/>ProxyStopping이 아닌지 <br/>확인합니다.": "First, ASSERT checks that <br/>state#95; is not ProxyStopping.", "메시지 처리가 정상 반환하면 <br/>상태를 갱신합니다.": "When message dispatch <br/>returns normally, update <br/>the state.", "상태를 설정한 뒤 동기 <br/>호출합니다.": "After setting the state, <br/>make the synchronous call.", "조건이 거짓이면 state#95;를 <br/>ProxyStopping으로 <br/>설정합니다.": "If the condition is false, <br/>set state#95; to ProxyStopping.", "조건이 거짓이면 정지를 <br/>진행합니다. · state#95; #33;#61; <br/>ProxyRunning #91;false#93;": "If the condition is false, <br/>proceed with stopping. · <br/>state#95; #33;#61; ProxyRunning <br/>#91;false#93;", "조건이 참이면 즉시 <br/>반환합니다.": "If the condition is true, <br/>return immediately.", "조건이 참이면 즉시 <br/>반환합니다. · state#95; #33;#61; <br/>ProxyRunning #91;true#93;": "If the condition is true, <br/>return immediately. · <br/>state#95; #33;#61; ProxyRunning <br/>#91;true#93;", "현재 스레드에서 <br/>dispatchMessages를 호출해 <br/>this와 <br/>Message::Type::<br/>InvokeMessage를 대상으로 <br/>메시지를 처리합니다.": "Call dispatchMessages on <br/>the current thread to <br/>process messages for this <br/>and <br/>Message::Type::<br/>InvokeMessage.", "호출이 정상 반환하면 exit를 <br/>호출합니다.": "When the call returns <br/>normally, call exit."}
  v_assert["먼저 ASSERT로 state#95;가 <br/>ProxyStopping이 아닌지 <br/>확인합니다."]
  v_check{"ASSERT 뒤에서 state#95;가 <br/>ProxyRunning이 아닌지 <br/>검사합니다."}
  v_return["조건이 참이면 즉시 <br/>반환합니다."]
  v_stopping["조건이 거짓이면 state#95;를 <br/>ProxyStopping으로 <br/>설정합니다."]
  v_invoke["proxy#95;의 invokeMethod로 <br/>ThreadProxy::stop을 <br/>ConnectionTypeBlocking으로 <br/>동기 호출합니다."]
  v_exit["동기 호출이 정상 반환하면 <br/>thread#95;의 exit를 호출합니다."]
  v_wait["thread#95;의 wait를 호출해 <br/>스레드 종료를 기다립니다."]
  v_dispatch["현재 스레드에서 <br/>dispatchMessages를 호출해 <br/>this와 <br/>Message::Type::<br/>InvokeMessage를 대상으로 <br/>메시지를 처리합니다."]
  v_stopped["dispatchMessages가 정상 <br/>반환하면 state#95;를 <br/>ProxyStopped로 갱신합니다."]
  v_assert -->|"ASSERT 뒤에 별도의 상태 <br/>검사가 나옵니다."| v_check
  v_check -->|"조건이 참이면 즉시 <br/>반환합니다. · state#95; #33;#61; <br/>ProxyRunning #91;true#93;"| v_return
  v_check -->|"조건이 거짓이면 정지를 <br/>진행합니다. · state#95; #33;#61; <br/>ProxyRunning #91;false#93;"| v_stopping
  v_stopping -->|"상태를 설정한 뒤 동기 <br/>호출합니다."| v_invoke
  v_invoke -->|"호출이 정상 반환하면 exit를 <br/>호출합니다."| v_exit
  v_exit -->|"exit가 정상 반환하면 wait를 <br/>호출합니다."| v_wait
  v_wait -->|"wait가 정상 반환하면 <br/>메시지를 처리합니다."| v_dispatch
  v_dispatch -->|"메시지 처리가 정상 반환하면 <br/>상태를 갱신합니다."| v_stopped
```

[Mermaid 원문](ipa.threaded-stop-order.mmd)

??? note "그림 근거와 확인 범위"
    Threaded stop은 어떤 상태 검사와 동기 호출 및 스레드 종료 순서로 ProxyStopped가 됩니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="First, ASSERT checks that state_ is not ProxyStopping.">먼저 ASSERT로 state&#95;가 ProxyStopping이 아닌지 확인합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) |
    | <span data-sdd-label-en="After ASSERT, check whether state_ is not ProxyRunning.">ASSERT 뒤에서 state&#95;가 ProxyRunning이 아닌지 검사합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) |
    | <span data-sdd-label-en="If the condition is true, return immediately.">조건이 참이면 즉시 반환합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) |
    | <span data-sdd-label-en="If the condition is false, set state_ to ProxyStopping.">조건이 거짓이면 state&#95;를 ProxyStopping으로 설정합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) |
    | <span data-sdd-label-en="Call ThreadProxy::stop synchronously through proxy_&#x27;s invokeMethod with ConnectionTypeBlocking.">proxy&#95;의 invokeMethod로 ThreadProxy::stop을 ConnectionTypeBlocking으로 동기 호출합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) |
    | <span data-sdd-label-en="When the synchronous call returns normally, call exit on thread_.">동기 호출이 정상 반환하면 thread&#95;의 exit를 호출합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) |
    | <span data-sdd-label-en="Call wait on thread_ to wait for the thread to finish.">thread&#95;의 wait를 호출해 스레드 종료를 기다립니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) |
    | <span data-sdd-label-en="Call dispatchMessages on the current thread to process messages for this and Message::Type::InvokeMessage.">현재 스레드에서 dispatchMessages를 호출해 this와 Message::Type::InvokeMessage를 대상으로 메시지를 처리합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) |
    | <span data-sdd-label-en="When dispatchMessages returns normally, update state_ to ProxyStopped.">dispatchMessages가 정상 반환하면 state&#95;를 ProxyStopped로 갱신합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) |
    | <span data-sdd-label-en="A separate state check follows ASSERT.">ASSERT 뒤에 별도의 상태 검사가 나옵니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) |
    | <span data-sdd-label-en="If the condition is true, return immediately. · state_ != ProxyRunning [true]">조건이 참이면 즉시 반환합니다. · state&#95; &#33;= ProxyRunning &#91;true&#93;</span> | [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) |
    | <span data-sdd-label-en="If the condition is false, proceed with stopping. · state_ != ProxyRunning [false]">조건이 거짓이면 정지를 진행합니다. · state&#95; &#33;= ProxyRunning &#91;false&#93;</span> | [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) |
    | <span data-sdd-label-en="After setting the state, make the synchronous call.">상태를 설정한 뒤 동기 호출합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) |
    | <span data-sdd-label-en="When the call returns normally, call exit.">호출이 정상 반환하면 exit를 호출합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) |
    | <span data-sdd-label-en="When exit returns normally, call wait.">exit가 정상 반환하면 wait를 호출합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) |
    | <span data-sdd-label-en="When wait returns normally, dispatch messages.">wait가 정상 반환하면 메시지를 처리합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) |
    | <span data-sdd-label-en="When message dispatch returns normally, update the state.">메시지 처리가 정상 반환하면 상태를 갱신합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) |
<!-- /sdd:visual:threaded-stop-order -->

<!-- sdd:visual:isolated-destructor-guard -->
### Isolated 소멸자의 IPC 분기

```mermaid
flowchart TB
%% sdd:translations {"Exit와 seq#95;++로 header를 <br/>만들고 msg를 구성한 뒤 <br/>ipc#95;-#62;sendAsync#40;msg#41;를 <br/>호출합니다. 반환값은 <br/>검사하지 않습니다.": "It builds header with Exit <br/>and seq#95;++, constructs msg, <br/>and calls <br/>ipc#95;-#62;sendAsync#40;msg#41;. It <br/>does not check the return <br/>value.", "Isolated 소멸자는 ipc#95;가 <br/>있는지 확인합니다.": "The Isolated destructor <br/>checks whether ipc#95; is <br/>present.", "Isolated 소멸자는 메시지 <br/>구성과 sendAsync 호출을 <br/>건너뛰고 본문을 마칩니다. <br/>return 문장은 없습니다.": "The Isolated destructor <br/>skips message construction <br/>and the sendAsync call, <br/>then reaches the end of its <br/>body. There is no return <br/>statement.", "조건이 거짓이면 if 본문을 <br/>건너뜁니다. · ipc#95; #91;false#93;": "If the condition is false, <br/>it skips the if body. · <br/>ipc#95; #91;false#93;", "조건이 참이면 Exit 메시지 <br/>전송을 시도합니다. · ipc#95; <br/>#91;true#93;": "If the condition is true, <br/>it attempts to send the <br/>Exit message. · ipc#95; #91;true#93;"}
  v_check{"Isolated 소멸자는 ipc#95;가 <br/>있는지 확인합니다."}
  v_send["Exit와 seq#95;++로 header를 <br/>만들고 msg를 구성한 뒤 <br/>ipc#95;-#62;sendAsync#40;msg#41;를 <br/>호출합니다. 반환값은 <br/>검사하지 않습니다."]
  v_end["Isolated 소멸자는 메시지 <br/>구성과 sendAsync 호출을 <br/>건너뛰고 본문을 마칩니다. <br/>return 문장은 없습니다."]
  v_check -->|"조건이 참이면 Exit 메시지 <br/>전송을 시도합니다. · ipc#95; <br/>#91;true#93;"| v_send
  v_check -->|"조건이 거짓이면 if 본문을 <br/>건너뜁니다. · ipc#95; #91;false#93;"| v_end
```

[Mermaid 원문](ipa.isolated-destructor-guard.mmd)

??? note "그림 근거와 확인 범위"
    Isolated 소멸자는 ipc_가 없으면 어떤 구문을 건너뛰며, 있으면 어떤 Exit 전송을 시도합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="The Isolated destructor checks whether ipc_ is present.">Isolated 소멸자는 ipc&#95;가 있는지 확인합니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:157](#source-a230ed3065e7523d) |
    | <span data-sdd-label-en="It builds header with Exit and seq_++, constructs msg, and calls ipc_-&gt;sendAsync(msg). It does not check the return value.">Exit와 seq&#95;++로 header를 만들고 msg를 구성한 뒤 ipc&#95;-&gt;sendAsync&#40;msg&#41;를 호출합니다. 반환값은 검사하지 않습니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:157](#source-a230ed3065e7523d) |
    | <span data-sdd-label-en="The Isolated destructor skips message construction and the sendAsync call, then reaches the end of its body. There is no return statement.">Isolated 소멸자는 메시지 구성과 sendAsync 호출을 건너뛰고 본문을 마칩니다. return 문장은 없습니다.</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:157](#source-a230ed3065e7523d) |
    | <span data-sdd-label-en="If the condition is true, it attempts to send the Exit message. · ipc_ [true]">조건이 참이면 Exit 메시지 전송을 시도합니다. · ipc&#95; &#91;true&#93;</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:157](#source-a230ed3065e7523d) |
    | <span data-sdd-label-en="If the condition is false, it skips the if body. · ipc_ [false]">조건이 거짓이면 if 본문을 건너뜁니다. · ipc&#95; &#91;false&#93;</span> | [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:157](#source-a230ed3065e7523d) |
<!-- /sdd:visual:isolated-destructor-guard -->

Isolated 프록시의 소멸자는 `ipc_`가 있으면 `Exit` 명령과 증가 전의 `seq_` 값으로 헤더를 만들고, 해당 메시지를 `sendAsync()`로 보냅니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:157`

근거 원문: [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) · [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:157](#source-a230ed3065e7523d)

## 생성과 IPC 실패

`IPAModule::load()`는 `valid_`가 거짓이면 `false`를 반환하고, 이미 `loaded_`이면 `true`를 반환합니다. 이어서 `dlopen`이 실패하면 오류를 기록하고 `false`를 반환합니다. `dlsym`으로 `ipaCreate`를 찾지 못하면 오류를 기록하고 `dlclose`로 핸들을 닫은 뒤 `dlHandle_`을 `nullptr`로 설정하고 `false`를 반환합니다. 심벌을 찾으면 `ipaCreate_`에 팩토리를 저장하고 `loaded_`를 `true`로 설정한 뒤 `true`를 반환합니다. `src/libcamera/ipa_module.cpp:390`

<!-- sdd:visual:module-load-error-branches -->
### 모듈 로드의 성공과 실패 반환

```mermaid
flowchart TB
%% sdd:translations {"#33;valid#95;는 모듈이 유효하지 <br/>않다는 뜻인가요? 유효하지 <br/>않은 모듈에서 호출하면 <br/>오류입니다.": "Does #33;valid#95; mean the <br/>module is invalid? Calling <br/>this on an invalid module <br/>is an error.", "dlopen으로 얻은 dlHandle#95;에 <br/>대해 #33;dlHandle#95;는 열기 <br/>실패를 뜻하나요?": "For dlHandle#95; obtained by <br/>dlopen, does #33;dlHandle#95; <br/>mean opening failed?", "dlsym으로 얻은 symbol에 <br/>대해 #33;symbol은 심볼 탐색 <br/>실패를 뜻하나요?": "For symbol obtained by <br/>dlsym, does #33;symbol mean <br/>the symbol lookup failed?", "false를 반환합니다.": "Return false.", "loaded#95;는 모듈이 이미 <br/>로드되었다는 뜻인가요?": "Does loaded#95; mean the <br/>module is already loaded?", "symbol로 ipaCreate#95;를 <br/>설정하고 loaded#95;를 true로 <br/>설정한 뒤 true를 반환합니다.": "Set ipaCreate#95; from symbol, <br/>set loaded#95; to true, and <br/>return true.", "true를 반환합니다.": "Return true.", "거짓이면 dlopen으로 공유 <br/>객체를 엽니다. #91;false#93;": "If false, open the shared <br/>object with dlopen. #91;false#93;", "거짓이면 dlsym으로 <br/>ipaCreate를 찾습니다. <br/>#91;false#93;": "If false, look up ipaCreate <br/>with dlsym. #91;false#93;", "거짓이면 이미 로드되었는지 <br/>확인합니다. #91;false#93;": "If false, check whether it <br/>is already loaded. #91;false#93;", "거짓이면 팩터리를 <br/>설정합니다. #91;false#93;": "If false, set the factory. <br/>#91;false#93;", "오류를 기록하고 dlclose로 <br/>dlHandle#95;을 닫은 뒤 <br/>nullptr로 설정하고 false를 <br/>반환합니다.": "Log the error, close <br/>dlHandle#95; with dlclose, set <br/>it to nullptr, and return <br/>false.", "오류를 기록하고 false를 <br/>반환합니다.": "Log the error and return <br/>false.", "참이면 false를 반환합니다. <br/>#91;true#93;": "If true, return false. <br/>#91;true#93;", "참이면 true를 반환합니다. <br/>#91;true#93;": "If true, return true. #91;true#93;", "참이면 오류를 기록하고 <br/>false를 반환합니다. #91;true#93;": "If true, log the error and <br/>return false. #91;true#93;", "참이면 핸들을 정리하고 <br/>false를 반환합니다. #91;true#93;": "If true, clean up the <br/>handle and return false. <br/>#91;true#93;"}
  v_valid{"#33;valid#95;는 모듈이 유효하지 <br/>않다는 뜻인가요? 유효하지 <br/>않은 모듈에서 호출하면 <br/>오류입니다."}
  v_invalid["false를 반환합니다."]
  v_loaded{"loaded#95;는 모듈이 이미 <br/>로드되었다는 뜻인가요?"}
  v_already["true를 반환합니다."]
  v_open{"dlopen으로 얻은 dlHandle#95;에 <br/>대해 #33;dlHandle#95;는 열기 <br/>실패를 뜻하나요?"}
  v_open_failure["오류를 기록하고 false를 <br/>반환합니다."]
  v_lookup{"dlsym으로 얻은 symbol에 <br/>대해 #33;symbol은 심볼 탐색 <br/>실패를 뜻하나요?"}
  v_lookup_failure["오류를 기록하고 dlclose로 <br/>dlHandle#95;을 닫은 뒤 <br/>nullptr로 설정하고 false를 <br/>반환합니다."]
  v_success["symbol로 ipaCreate#95;를 <br/>설정하고 loaded#95;를 true로 <br/>설정한 뒤 true를 반환합니다."]
  v_valid -->|"참이면 false를 반환합니다. <br/>#91;true#93;"| v_invalid
  v_valid -->|"거짓이면 이미 로드되었는지 <br/>확인합니다. #91;false#93;"| v_loaded
  v_loaded -->|"참이면 true를 반환합니다. <br/>#91;true#93;"| v_already
  v_loaded -->|"거짓이면 dlopen으로 공유 <br/>객체를 엽니다. #91;false#93;"| v_open
  v_open -->|"참이면 오류를 기록하고 <br/>false를 반환합니다. #91;true#93;"| v_open_failure
  v_open -->|"거짓이면 dlsym으로 <br/>ipaCreate를 찾습니다. <br/>#91;false#93;"| v_lookup
  v_lookup -->|"참이면 핸들을 정리하고 <br/>false를 반환합니다. #91;true#93;"| v_lookup_failure
  v_lookup -->|"거짓이면 팩터리를 <br/>설정합니다. #91;false#93;"| v_success
```

[Mermaid 원문](ipa.module-load-error-branches.mmd)

??? note "그림 근거와 확인 범위"
    IPAModule::load는 기존 상태, dlopen과 dlsym 결과에 따라 어떤 값을 반환하고 무엇을 정리합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Does !valid_ mean the module is invalid? Calling this on an invalid module is an error.">&#33;valid&#95;는 모듈이 유효하지 않다는 뜻인가요? 유효하지 않은 모듈에서 호출하면 오류입니다.</span> | [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) |
    | <span data-sdd-label-en="Return false.">false를 반환합니다.</span> | [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) |
    | <span data-sdd-label-en="Does loaded_ mean the module is already loaded?">loaded&#95;는 모듈이 이미 로드되었다는 뜻인가요?</span> | [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) |
    | <span data-sdd-label-en="Return true.">true를 반환합니다.</span> | [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) |
    | <span data-sdd-label-en="For dlHandle_ obtained by dlopen, does !dlHandle_ mean opening failed?">dlopen으로 얻은 dlHandle&#95;에 대해 &#33;dlHandle&#95;는 열기 실패를 뜻하나요?</span> | [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) |
    | <span data-sdd-label-en="Log the error and return false.">오류를 기록하고 false를 반환합니다.</span> | [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) |
    | <span data-sdd-label-en="For symbol obtained by dlsym, does !symbol mean the symbol lookup failed?">dlsym으로 얻은 symbol에 대해 &#33;symbol은 심볼 탐색 실패를 뜻하나요?</span> | [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) |
    | <span data-sdd-label-en="Log the error, close dlHandle_ with dlclose, set it to nullptr, and return false.">오류를 기록하고 dlclose로 dlHandle&#95;을 닫은 뒤 nullptr로 설정하고 false를 반환합니다.</span> | [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) |
    | <span data-sdd-label-en="Set ipaCreate_ from symbol, set loaded_ to true, and return true.">symbol로 ipaCreate&#95;를 설정하고 loaded&#95;를 true로 설정한 뒤 true를 반환합니다.</span> | [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) |
    | <span data-sdd-label-en="If true, return false. · !valid_ [true]">참이면 false를 반환합니다. · &#33;valid&#95; &#91;true&#93;</span> | [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) |
    | <span data-sdd-label-en="If false, check whether it is already loaded. · !valid_ [false]">거짓이면 이미 로드되었는지 확인합니다. · &#33;valid&#95; &#91;false&#93;</span> | [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) |
    | <span data-sdd-label-en="If true, return true. · loaded_ [true]">참이면 true를 반환합니다. · loaded&#95; &#91;true&#93;</span> | [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) |
    | <span data-sdd-label-en="If false, open the shared object with dlopen. · loaded_ [false]">거짓이면 dlopen으로 공유 객체를 엽니다. · loaded&#95; &#91;false&#93;</span> | [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) |
    | <span data-sdd-label-en="If true, log the error and return false. · !dlHandle_ [true]">참이면 오류를 기록하고 false를 반환합니다. · &#33;dlHandle&#95; &#91;true&#93;</span> | [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) |
    | <span data-sdd-label-en="If false, look up ipaCreate with dlsym. · !dlHandle_ [false]">거짓이면 dlsym으로 ipaCreate를 찾습니다. · &#33;dlHandle&#95; &#91;false&#93;</span> | [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) |
    | <span data-sdd-label-en="If true, clean up the handle and return false. · !symbol [true]">참이면 핸들을 정리하고 false를 반환합니다. · &#33;symbol &#91;true&#93;</span> | [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) |
    | <span data-sdd-label-en="If false, set the factory. · !symbol [false]">거짓이면 팩터리를 설정합니다. · &#33;symbol &#91;false&#93;</span> | [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) |
<!-- /sdd:visual:module-load-error-branches -->

<!-- sdd:visual:synchronous-ipc-outcomes -->
### 동기 call의 송신·대기·정리

```mermaid
flowchart TB
%% sdd:translations {"callData#95;.insert는 cookie를 <br/>키로, {response, false}를 <br/>값으로 삽입하려고 <br/>시도합니다.": "callData#95;.insert attempts <br/>to insert cookie as the key <br/>and {response, false} as <br/>the value.", "callData#95;에서 iter 항목을 <br/>지운 뒤 0을 반환합니다.": "Erase the iter entry from <br/>callData#95; and return 0.", "callData#95;의 erase가 iter <br/>항목을 지운 뒤 ret를 <br/>반환합니다.": "The erase method of <br/>callData#95; removes the iter <br/>entry, then the function <br/>returns ret.", "done이 false이면 타이머를 <br/>확인합니다. · <br/>#33;iter-#62;second.done #91;true#93;": "If done is false, check the <br/>timer. · #33;iter-#62;second.done <br/>#91;true#93;", "done이 true이면 정리하고 <br/>반환합니다. · <br/>#33;iter-#62;second.done #91;false#93;": "If done is true, clean up <br/>and return. · <br/>#33;iter-#62;second.done #91;false#93;", "iter 항목의 done을 <br/>확인합니다.": "Check done in the iter <br/>entry.", "result.first를 iter로 <br/>사용하며 result.second는 <br/>검사하지 않습니다. cookie가 <br/>이미 있으면 iter는 기존 <br/>항목을 가리킬 수 있습니다.": "Use result.first as iter; <br/>do not test result.second. <br/>An existing cookie can make <br/>iter reference an existing <br/>entry.", "ret가 0이 아닌지 확인합니다.": "Check whether ret is <br/>nonzero.", "socket#95;의 send가 message를 <br/>보내고 결과를 ret에 <br/>저장합니다.": "The send method of socket#95; <br/>sends message and stores <br/>the result in ret.", "timeout의 isRunning으로 <br/>타이머가 실행 중인지 <br/>확인합니다.": "Check whether the timer is <br/>running using the isRunning <br/>method of timeout.", "timeout의 start가 2000ms <br/>타이머를 시작합니다.": "The start method of timeout <br/>starts a 2000ms timer.", "삽입 시도 결과에서 반복자를 <br/>선택합니다.": "Select the iterator from <br/>the insertion attempt <br/>result.", "선택한 뒤 message를 <br/>보냅니다.": "Send message after the <br/>selection.", "송신 결과가 0이 아니면 <br/>정리하고 반환합니다. · ret <br/>#91;true#93;": "If the send result is <br/>nonzero, clean up and <br/>return. · ret #91;true#93;", "송신 결과가 0이면 타이머를 <br/>시작합니다. · ret #91;false#93;": "If the send result is zero, <br/>start the timer. · ret <br/>#91;false#93;", "송신 결과를 확인합니다.": "Check the send result.", "이벤트를 처리한 뒤 done을 <br/>다시 확인합니다.": "Check done again after <br/>processing events.", "타이머가 실행 중이 아니면 <br/>타임아웃을 처리합니다. · <br/>#33;timeout.isRunning#40;#41; #91;true#93;": "If the timer is not <br/>running, handle the <br/>timeout. · <br/>#33;timeout.isRunning#40;#41; #91;true#93;", "타이머가 실행 중이면 <br/>이벤트를 처리합니다. · <br/>#33;timeout.isRunning#40;#41; #91;false#93;": "If the timer is running, <br/>process events. · <br/>#33;timeout.isRunning#40;#41; #91;false#93;", "타이머를 시작한 뒤 done을 <br/>확인합니다.": "Check done after starting <br/>the timer.", "타임아웃을 기록하고 <br/>callData#95;에서 iter 항목을 <br/>지운 뒤 -ETIMEDOUT을 <br/>반환합니다.": "Log the timeout, erase the <br/>iter entry from callData#95;, <br/>and return -ETIMEDOUT.", "현재 스레드의 <br/>eventDispatcher가 <br/>processEvents를 실행합니다.": "The eventDispatcher of the <br/>current thread runs <br/>processEvents."}
  v_insert["callData#95;.insert는 cookie를 <br/>키로, {response, false}를 <br/>값으로 삽입하려고 <br/>시도합니다."]
  v_iter["result.first를 iter로 <br/>사용하며 result.second는 <br/>검사하지 않습니다. cookie가 <br/>이미 있으면 iter는 기존 <br/>항목을 가리킬 수 있습니다."]
  v_send["socket#95;의 send가 message를 <br/>보내고 결과를 ret에 <br/>저장합니다."]
  v_ret{"ret가 0이 아닌지 확인합니다."}
  v_send_failure["callData#95;의 erase가 iter <br/>항목을 지운 뒤 ret를 <br/>반환합니다."]
  v_start["timeout의 start가 2000ms <br/>타이머를 시작합니다."]
  v_done{"iter 항목의 done을 <br/>확인합니다."}
  v_timer{"timeout의 isRunning으로 <br/>타이머가 실행 중인지 <br/>확인합니다."}
  v_timed_out["타임아웃을 기록하고 <br/>callData#95;에서 iter 항목을 <br/>지운 뒤 -ETIMEDOUT을 <br/>반환합니다."]
  v_events["현재 스레드의 <br/>eventDispatcher가 <br/>processEvents를 실행합니다."]
  v_success["callData#95;에서 iter 항목을 <br/>지운 뒤 0을 반환합니다."]
  v_insert -->|"삽입 시도 결과에서 반복자를 <br/>선택합니다."| v_iter
  v_iter -->|"선택한 뒤 message를 <br/>보냅니다."| v_send
  v_send -->|"송신 결과를 확인합니다."| v_ret
  v_ret -->|"송신 결과가 0이 아니면 <br/>정리하고 반환합니다. · ret <br/>#91;true#93;"| v_send_failure
  v_ret -->|"송신 결과가 0이면 타이머를 <br/>시작합니다. · ret #91;false#93;"| v_start
  v_start -->|"타이머를 시작한 뒤 done을 <br/>확인합니다."| v_done
  v_done -->|"done이 false이면 타이머를 <br/>확인합니다. · <br/>#33;iter-#62;second.done #91;true#93;"| v_timer
  v_done -->|"done이 true이면 정리하고 <br/>반환합니다. · <br/>#33;iter-#62;second.done #91;false#93;"| v_success
  v_timer -->|"타이머가 실행 중이 아니면 <br/>타임아웃을 처리합니다. · <br/>#33;timeout.isRunning#40;#41; #91;true#93;"| v_timed_out
  v_timer -->|"타이머가 실행 중이면 <br/>이벤트를 처리합니다. · <br/>#33;timeout.isRunning#40;#41; #91;false#93;"| v_events
  v_events -->|"이벤트를 처리한 뒤 done을 <br/>다시 확인합니다."| v_done
```

[Mermaid 원문](ipa.synchronous-ipc-outcomes.mmd)

??? note "그림 근거와 확인 범위"
    call은 쿠키 항목 삽입 시도, 송신 결과와 done·타이머 상태에 따라 무엇을 정리하고 반환합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="callData_.insert attempts to insert cookie as the key and {response, false} as the value.">callData&#95;.insert는 cookie를 키로, {response, false}를 값으로 삽입하려고 시도합니다.</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="Use result.first as iter; do not test result.second. An existing cookie can make iter reference an existing entry.">result.first를 iter로 사용하며 result.second는 검사하지 않습니다. cookie가 이미 있으면 iter는 기존 항목을 가리킬 수 있습니다.</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="The send method of socket_ sends message and stores the result in ret.">socket&#95;의 send가 message를 보내고 결과를 ret에 저장합니다.</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="Check whether ret is nonzero.">ret가 0이 아닌지 확인합니다.</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="The erase method of callData_ removes the iter entry, then the function returns ret.">callData&#95;의 erase가 iter 항목을 지운 뒤 ret를 반환합니다.</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="The start method of timeout starts a 2000ms timer.">timeout의 start가 2000ms 타이머를 시작합니다.</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="Check done in the iter entry.">iter 항목의 done을 확인합니다.</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="Check whether the timer is running using the isRunning method of timeout.">timeout의 isRunning으로 타이머가 실행 중인지 확인합니다.</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="Log the timeout, erase the iter entry from callData_, and return -ETIMEDOUT.">타임아웃을 기록하고 callData&#95;에서 iter 항목을 지운 뒤 -ETIMEDOUT을 반환합니다.</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="The eventDispatcher of the current thread runs processEvents.">현재 스레드의 eventDispatcher가 processEvents를 실행합니다.</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="Erase the iter entry from callData_ and return 0.">callData&#95;에서 iter 항목을 지운 뒤 0을 반환합니다.</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="Select the iterator from the insertion attempt result.">삽입 시도 결과에서 반복자를 선택합니다.</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="Send message after the selection.">선택한 뒤 message를 보냅니다.</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="Check the send result.">송신 결과를 확인합니다.</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="If the send result is nonzero, clean up and return. · ret [true]">송신 결과가 0이 아니면 정리하고 반환합니다. · ret &#91;true&#93;</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="If the send result is zero, start the timer. · ret [false]">송신 결과가 0이면 타이머를 시작합니다. · ret &#91;false&#93;</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="Check done after starting the timer.">타이머를 시작한 뒤 done을 확인합니다.</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="If done is false, check the timer. · !iter-&gt;second.done [true]">done이 false이면 타이머를 확인합니다. · &#33;iter-&gt;second.done &#91;true&#93;</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="If done is true, clean up and return. · !iter-&gt;second.done [false]">done이 true이면 정리하고 반환합니다. · &#33;iter-&gt;second.done &#91;false&#93;</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="If the timer is not running, handle the timeout. · !timeout.isRunning() [true]">타이머가 실행 중이 아니면 타임아웃을 처리합니다. · &#33;timeout.isRunning&#40;&#41; &#91;true&#93;</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="If the timer is running, process events. · !timeout.isRunning() [false]">타이머가 실행 중이면 이벤트를 처리합니다. · &#33;timeout.isRunning&#40;&#41; &#91;false&#93;</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
    | <span data-sdd-label-en="Check done again after processing events.">이벤트를 처리한 뒤 done을 다시 확인합니다.</span> | [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) |
<!-- /sdd:visual:synchronous-ipc-outcomes -->

`IPAModule::createInterface()`는 모듈이 유효하지 않거나 로드되지 않았으면 `nullptr`을 반환합니다. 두 조건을 모두 통과하면 `ipaCreate_()`를 호출하고 그 반환값을 반환합니다. `src/libcamera/ipa_module.cpp:451`

`IPCPipeUnixSocket::sendSync`는 입력 페이로드, 응답 저장 위치, 입력 헤더의 쿠키로 `call`을 호출하고 반환값을 검사합니다. 반환값이 0이 아니면 오류를 기록하고 그 값을 그대로 반환합니다. 성공하면 `out`이 널이 아닐 때 응답으로 만든 `IPCMessage`를 `out`에 저장하고 0을 반환합니다. `src/libcamera/ipc_pipe_unixsocket.cpp:57`

`IPCPipeUnixSocket::call`은 `cookie`를 키로 하고 `response`와 `false`를 값으로 하여 `callData_`에 삽입을 시도합니다. 이 함수는 삽입 성공 여부를 검사하지 않고 결과의 `first` 필드를 `iter`로 사용하여 해당 항목을 가리킵니다. 소켓의 `send`에는 반복자가 아닌 `message`를 전달하며, 송신이 실패하면 `erase`로 `iter`가 가리키는 항목을 지우고 송신의 반환값을 반환합니다. `src/libcamera/ipc_pipe_unixsocket.cpp:112`

`IPCPipeUnixSocket::call`은 타이머를 `2000ms`로 시작하고 항목의 `done`이 참이 될 때까지 기다립니다. 대기 중 타이머가 실행 중이면 현재 스레드의 이벤트 디스패처에서 `processEvents()`를 호출합니다. 타이머가 만료되면 `erase`로 항목을 지우고 `-ETIMEDOUT`을 반환합니다. `done`이 참이 되어 정상 완료되면 항목을 `erase`로 지우고 0을 반환합니다. `src/libcamera/ipc_pipe_unixsocket.cpp:112`

근거 원문: [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) · [src/libcamera/ipc_pipe_unixsocket.cpp:27](#source-f0268126d3f8c2bc) · [src/libcamera/ipc_pipe_unixsocket.cpp:112](#source-651cf5a1cd2457ca) · [src/libcamera/ipc_pipe_unixsocket.cpp:57](#source-bd92cc1dba99926f) · [src/libcamera/ipa_module.cpp:451](#source-0ea8ec769af3a9cd)

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

<a id="source-60c70cd011db2353"></a>

??? note "소스 근거: utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:55"
    `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:55`에서 시작하는 발췌입니다. 종료 줄은 56이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `487c09c1385700711ded6c5037d3c9d4d59b576e401dd378775c6d567c6b4dbe`
    
    ```text
    if (!ipam->load())
    		return;
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

<a id="source-7f9e84d5315c5882"></a>

??? note "소스 근거: src/libcamera/ipc_pipe_unixsocket.cpp:84"
    `src/libcamera/ipc_pipe_unixsocket.cpp:84`에서 시작하는 발췌입니다. 종료 줄은 110이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `80db6c393d9adc09ed40ff8c4bf122abf5125ad8a36129134bcfd3b3fc3496d1`
    
    ```text
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

<a id="source-a230ed3065e7523d"></a>

??? note "소스 근거: utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:157"
    `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:157`에서 시작하는 발췌입니다. 종료 줄은 165이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `134a6b2cd3ed0e858c49bb1f3872af60ba1d44b3a32e60f2d2d0642a68865851`
    
    ```text
    {{proxy_name}}Isolated::~{{proxy_name}}Isolated()
    {
    	if (ipc_) {
    		IPCMessage::Header header =
    			{ static_cast<uint32_t>({{cmd_enum_name}}::Exit), seq_++ };
    		IPCMessage msg(header);
    		ipc_->sendAsync(msg);
    	}
    }
    ```

<a id="source-651cf5a1cd2457ca"></a>

??? note "소스 근거: src/libcamera/ipc_pipe_unixsocket.cpp:112"
    `src/libcamera/ipc_pipe_unixsocket.cpp:112`에서 시작하는 발췌입니다. 종료 줄은 142이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `c3014bf1773367a6cee381806d3e8c9d090d5422393863e184b6a0bd97b0ec79`
    
    ```text
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
    ```

<a id="source-bd92cc1dba99926f"></a>

??? note "소스 근거: src/libcamera/ipc_pipe_unixsocket.cpp:57"
    `src/libcamera/ipc_pipe_unixsocket.cpp:57`에서 시작하는 발췌입니다. 종료 줄은 71이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `de13fb892859dee920a0aa332f3f6fbb4c8c01caf5500efc8e43567b0f9a49ee`
    
    ```text
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
    ```

<a id="source-0ea8ec769af3a9cd"></a>

??? note "소스 근거: src/libcamera/ipa_module.cpp:451"
    `src/libcamera/ipa_module.cpp:451`에서 시작하는 발췌입니다. 종료 줄은 457이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `cc474ffc04763317d9b3d0f3b2a6a5fb3319eba3c6883c0e71ab952df7c94fbf`
    
    ```text
    IPAInterface *IPAModule::createInterface()
    {
    	if (!valid_ || !loaded_)
    		return nullptr;
    
    	return ipaCreate_();
    }
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
    - 근거 파일: `include/libcamera/internal/ipa_manager.h`, `include/libcamera/internal/ipa_module.h`, `include/libcamera/internal/ipa_proxy.h`, `include/libcamera/ipa/ipu3.mojom`, `include/libcamera/ipa/rkisp1.mojom`, `src/ipa/ipu3/ipu3.cpp`, `src/ipa/rkisp1/rkisp1.cpp`, `src/libcamera/base/log.cpp`, `src/libcamera/ipa_manager.cpp`, `src/libcamera/ipa_module.cpp`, `src/libcamera/ipa_proxy.cpp`, `src/libcamera/ipc_pipe_unixsocket.cpp`, `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl`, `utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `c19d05128f`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-12 · 사람 검토 전

다음 단계: [IPA 튜닝과 소프트웨어 ISP](ipa-algorithms.md)
