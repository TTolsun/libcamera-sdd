---
generated_at: 2026-10-26 14:23:09+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: ipa
generation_method: facts-and-llm
evidence_fingerprint: 84611553aff2de125c4a301d56f8b196027713cb1261cbeea7f5b956cb7d641f
semantic_review: human-review-required
agent: ollama/qwen3.5:9b
generated_design:
  schema: 1
  input_fingerprint: 84611553aff2de125c4a301d56f8b196027713cb1261cbeea7f5b956cb7d641f
  answers:
    selection:
    - text: '`IPAManager::IPAManager()` 함수는 사용자 지정 경로를 먼저 확인하고, libcamera 가 설치되지 않은
        경우 빌드 디렉토리를 추가하며, 마지막으로 시스템 설치 경로를 검색합니다.'
      evidence:
      - modules
      covers:
      - selection
      kind: behavior
      quote: "/* User-specified paths take precedence. */\n\tconst auto modulePaths\
        \ =\n\t\tconfiguration.listOption({ \"ipa\", \"module_paths\" })\n\t\t\t.value_or(utils::defopt);\n\
        \tfor (const auto &dir : modulePaths) {\n\t\tif (dir.empty())\n\t\t\tcontinue;"
    - text: 사용자가 'ipa.`module_paths`' 옵션으로 경로를 지정하지 않으면 빌드 디렉토리와 시스템 설치 경로만 검색되며,
        모듈이 없으면 경고 로그가 출력됩니다.
      evidence:
      - modules
      covers:
      - selection
      kind: behavior
      quote: "if (!modulePaths.empty() && !ipaCount)\n\t\tLOG(IPAManager, Warning)\
        \ << \"No IPA found in '\"\n\t\t\t\t\t << utils::join(modulePaths, \":\")\n\
        \t\t\t\t\t << \"'\";"
    - text: '`IPAModule::match()` 함수는 모듈 이름과 버전 범위를 비교하여 일치하는지 확인하며, false 를 반환하면
        해당 모듈은 선택되지 않습니다.'
      evidence:
      - match
      covers:
      - selection
      kind: behavior
      quote: "\\brief Verify if the IPA module matches a given name\n * \\param[in]\
        \ name The IPA module name\n * \\param[in] minVersion Minimum acceptable version\
        \ of IPA module\n * \\param[in] maxVersion Maximum acceptable version of IPA\
        \ module\n *\n * This function checks if this IPA module matches the requested\
        \ \\a name\n * and the input version range.\n *\n * \\return True if the IPA\
        \ module matches, or false otherwise\n */\nbool IPAModule::match(const char\
        \ *name, uint32_t minVersion,\n\t\t      uint32_t maxVersion) const\n{\n\t\
        return info_.pipelineVersion >= minVersion &&\n\t       info_.pipelineVersion\
        \ <= maxVersion &&\n\t       !strcmp(info_.name, name);\n}"
    - text: createIPA() 함수는 module() 으로 찾은 모듈이 없으면 nullptr 를 반환하고, 프록시 생성 시 서명이 유효하지
        않으면 Isolated 실행 방식을 선택합니다.
      evidence:
      - selection
      covers:
      - selection
      kind: behavior
      quote: "template<typename T>\n\tstd::unique_ptr<T> createIPA(const char *name,\
        \ uint32_t minVersion,\n\t\t\t\t     uint32_t maxVersion)\n\t{\n\t\tIPAModule\
        \ *m = module(name, minVersion, maxVersion);\n\t\tif (!m)\n\t\t\treturn nullptr;"
    - text: 서명 검증이 실패하거나 `forceIsolation_` 가 true 일 경우 isSignatureValid() 는 false
        를 반환하고, createIPA() 는 Isolated 실행 방식을 선택합니다.
      evidence:
      - signature
      covers:
      - selection
      kind: behavior
      quote: "bool IPAManager::isSignatureValid([[maybe_unused]] IPAModule *ipa) const\n\
        {\n#if HAVE_IPA_PUBKEY\n\tif (forceIsolation_) {\n\t\tLOG(IPAManager, Debug)\n\
        \t\t\t<< \"Isolation of IPA module \" << ipa->path()\n\t\t\t<< \" forced through\
        \ configuration\";\n\t\treturn false;\n\t}"
    - text: 서명이 유효하지 않으면 createIPA() 는 Isolated 실행 방식을 선택하고, 프록시 생성이 실패하면 nullptr
        를 반환합니다.
      evidence:
      - selection
      covers:
      - selection
      kind: behavior
      quote: "if (!proxy->isValid()) {\n\t\t\tLOG(IPAManager, Error) << \"Failed to\
        \ load proxy\";\n\t\t\treturn nullptr;\n\t\t}"
    execution:
    - text: '`init-branch:0`에 포함된 템플릿 코드는 `method.mojom_name`이 `init`일 때 `ipa_`를 호출하여
        IPA 메서드를 직접 실행하는 경로를 제공합니다.'
      evidence:
      - init-branch
      covers:
      - execution
      kind: behavior
      quote: "{%- elif method.mojom_name == \"init\" %}\n\t{{ method|method_return_value\
        \ + \" _ret = \" if method|method_return_value != \"void\" -}}\n\tipa_->{{method.mojom_name}}(\n\
        \t{%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \"\
        \ if not loop.last}}\n\t{%- endfor -%}\n);"
      part_id: init
    - text: '`init` 메서드가 호출된 직후 `proxy_.moveToThread(&thread_)`가 실행되며, 이 호출에 전달되는
        스레드 객체는 `thread_`라는 변수를 가리킵니다.'
      evidence:
      - init-branch
      covers:
      - execution
      kind: behavior
      quote: proxy_.moveToThread(&thread_);
      part_id: init-move
    - text: '`start-branch:0` 인용문에 따르면 worker 스레드를 `thread_.start()` 함수로 시작한 뒤 바로
        `ThreadProxy::start`를 `ConnectionTypeBlocking` 연결 유형으로 호출합니다.'
      evidence:
      - start-branch
      covers:
      - execution
      kind: behavior
      quote: "{%- elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\
        \tthread_.start();"
      part_id: start
    - text: '`{{proxy_name}}Threaded` 클래스의 일반 동기 메서드 분기에서는 `init`, `start`, `stop`
        을 제외한 모든 호출이 `ipa_->{{method.mojom_name}}(...)` 경로를 통해 직접 호출됩니다.'
      evidence:
      - dispatch
      covers:
      - execution
      kind: behavior
      quote: "return proxy_.invokeMethod(&ThreadProxy::start, ConnectionTypeBlocking\n\
        \t{{- \", \" if method|method_param_names}}\n\t{%- for param in method|method_param_names\
        \ -%}\n\t\t{{param}}{{- \", \" if not loop.last}}\n\t{%- endfor -%}\n);\n\
        {%- elif not method|is_async %}\n\treturn ipa_->{{method.mojom_name}}(\n\t\
        {%- for param in method|method_param_names -%}\n\t\t{{param}}{{- \", \" if\
        \ not loop.last}}\n\t{%- endfor -%}\n);\n{% elif method|is_async %}\n\tASSERT(state_\
        \ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}},\
        \ ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\
        \t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}"
      part_id: sync
    - text: '`async-assert` 파일의 `{% elif method|is_async %}` 조건부 블록 내부에는 `ASSERT(state_
        == ProxyRunning);`라는 매크로 호출이 포함되어 있습니다.'
      evidence:
      - async-assert
      covers:
      - execution
      kind: behavior
      quote: ASSERT(state_ == ProxyRunning);
      part_id: async
    - text: '`Threaded` 비동기 분기의 `invokeMethod` 호출은 `method|is_async` 조건이 참일 때만 실행되며,
        이때 전달되는 연결 유형은 `ConnectionTypeQueued` 입니다.'
      evidence:
      - async-branch
      covers:
      - execution
      kind: behavior
      quote: "{% elif method|is_async %}\n\tASSERT(state_ == ProxyRunning);\n\tproxy_.invokeMethod(&ThreadProxy::{{method.mojom_name}},\
        \ ConnectionTypeQueued\n\t{%- for param in method|method_param_names -%}\n\
        \t\t, {{param}}\n\t{%- endfor -%}\n);\n{%- endif %}\n}\n{% endfor %}"
      part_id: async-dispatch
    - text: '`{{proxy_name}}Threaded` 생성자는 초기화 과정에서 `ipam->load()`를 호출하여 IPA 모듈을 로드합니다.'
      evidence:
      - threaded
      covers:
      - execution
      kind: behavior
      quote: "{{proxy_name}}Threaded::{{proxy_name}}Threaded(IPAModule *ipam, const\
        \ CameraManager &cm)\n\t: {{proxy_name}}(ipam, cm), thread_(\"{{proxy_name}}\"\
        )\n{\n\tLOG(IPAProxy, Debug)\n\t\t<< \"initializing {{module_name}} proxy\
        \ in thread: loading IPA from \"\n\t\t<< ipam->path();"
      part_id: constructor
    - text: '`Threaded` 생성자가 `createInterface`를 호출하여 IPA 인터페이스 객체를 만들지 못하면, 해당 함수는
        로그에 오류 메시지를 출력하고 즉시 반환합니다.'
      evidence:
      - ctor-interface
      covers:
      - execution
      kind: behavior
      quote: "IPAInterface *ipai = ipam->createInterface();\n\tif (!ipai) {\n\t\t\
        LOG(IPAProxy, Error)\n\t\t\t<< \"Failed to create IPA context for \" << ipam->path();\n\
        \t\treturn;"
      part_id: constructor-interface
    - text: '`{{proxy_name}}Threaded` 클래스의 생성자에서 `ipa_` 객체의 이벤트를 처리하기 위해 `this` 를
        수신 객체로, `&{{proxy_name}}Threaded::{{method.mojom_name}}Handler` 를 핸들러 메서드로
        하여 `connect` 호출을 수행합니다.'
      evidence:
      - ctor-events
      covers:
      - execution
      kind: behavior
      quote: ipa_->{{method.mojom_name}}.connect(this, &{{proxy_name}}Threaded::{{method.mojom_name}}Handler);
      part_id: constructor-events
    - text: '`{{proxy_name}}Isolated` 생성자는 `ipam->path()`와 worker 경로인 `proxyWorkerPath`를
        사용하여 `std::make_unique<IPCPipeUnixSocket>`로 IPC 연결을 만듭니다.'
      evidence:
      - isolated
      covers:
      - execution
      kind: behavior
      quote: "auto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\
        \t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\
        \t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t\
        }"
      part_id: isolated
    - text: '`{{proxy_name}}Isolated` 클래스의 생성자에서 `ipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage)`
        호출이 수행됩니다.'
      evidence:
      - isolated-valid
      covers:
      - execution
      kind: behavior
      quote: ipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage);
      part_id: isolated-valid
    - text: '`isolated-store` 함수의 `scope` 범위 내에서 실행되는 코드에서는 `ipc_` 멤버 변수에 `std::move(ipc)`를
        대입합니다.'
      evidence:
      - isolated-store
      covers:
      - execution
      kind: behavior
      quote: "ipc_ = std::move(ipc);\n\tvalid_ = true;"
      part_id: isolated-store
    - text: '`Isolated` 클래스의 생성자 함수가 실행될 때 `valid_` 멤버 변수에는 `true` 값이 대입됩니다.'
      evidence:
      - isolated-ready
      covers:
      - execution
      kind: behavior
      quote: valid_ = true;
      part_id: isolated-ready
    - text: '`IPAProxy::resolvePath` 함수는 주어진 프록시 워커 실행 파일 이름에 대한 유효한 전체 경로를 찾습니다.'
      evidence:
      - worker-path
      covers:
      - execution
      kind: behavior
      quote: "\\brief Find a valid full path for a proxy worker for a given executable\
        \ name\n * \\param[in] file File name of proxy worker executable\n *\n * A\
        \ proxy worker's executable could be found in either the global installation\n\
        \ * directory, or in the paths specified by the environment variable\n * LIBCAMERA_IPA_PROXY_PATH.\
        \ This function checks the global install directory\n * first, then LIBCAMERA_IPA_PROXY_PATH\
        \ in order, and returns the full path to\n * the proxy worker executable that\
        \ is specified by file. The proxy worker\n * executable shall have exec permission.\n\
        \ *\n * \\return The full path to the proxy worker executable, or an empty\
        \ string if\n * no valid executable path\n */\nstd::string IPAProxy::resolvePath(const\
        \ std::string &file) const\n{\n\tstd::string proxyFile = \"/\" + file;"
      part_id: worker
    - text: '`IPCPipeUnixSocket::sendSync` 함수는 호출 시 `IPCMessage` 인자와 응답을 저장할 포인터를
        받아, 내부적으로 `call` 함수를 호출하여 동기식 통신을 수행합니다.'
      evidence:
      - ipc
      covers:
      - execution
      kind: behavior
      quote: "int IPCPipeUnixSocket::sendSync(const IPCMessage &in, IPCMessage *out)\n\
        {\n\tIPCUnixSocket::Payload response;"
      part_id: ipc
    - text: '`IPCPipeUnixSocket::sendAsync` 함수는 `socket_->send(data.payload())` 호출을
        통해 소켓으로 데이터를 전송합니다.'
      evidence:
      - send-async
      covers:
      - execution
      kind: behavior
      quote: "int IPCPipeUnixSocket::sendAsync(const IPCMessage &data)\n{\n\tint ret\
        \ = socket_->send(data.payload());\n\tif (ret) {\n\t\tLOG(IPCPipe, Error)\
        \ << \"Failed to call async\";\n\t\treturn ret;\n\t}"
      part_id: ipc-async
    interface:
    - text: '`IPAIPU3Interface` 와 `IPARkISP1Interface` 는 초기화, 시작, 중지 및 구성을 위한 동기 메서드를
        제공합니다. init 은 설정 정보와 센서 정보를 받아 제어 정보를 반환하며, start 와 stop 은 각각 처리를 시작하거나 중지합니다.
        configure 는 IPU3 의 경우 단일 설정 정보를, RKISP1 의 경우 설정 정보와 스트림 구성 맵을 받아 제어 정보를 반환합니다.'
      evidence:
      - ipu3-api
      covers:
      - interface
      kind: behavior
      quote: "interface IPAIPU3Interface {\n\tinit(libcamera.IPASettings settings,\n\
        \t     libcamera.IPACameraSensorInfo sensorInfo,\n\t     libcamera.ControlInfoMap\
        \ sensorControls)\n\t\t=> (int32 ret, libcamera.ControlInfoMap ipaControls);\n\
        \tstart() => (int32 ret);\n\tstop();"
    - text: 두 인터페이스 모두 버퍼 매핑과 해제를 위한 mapBuffers 와 unmapBuffers 메서드를 공유합니다. 이 메서드는
        배열 형태의 버퍼를 매핑하거나 ID 를 기반으로 해제를 수행하며, 구체적인 구현 세부사항은 인터페이스 정의에 명시되어 있지 않습니다.
      evidence:
      - ipu3-api
      covers:
      - interface
      kind: behavior
      quote: "mapBuffers(array<libcamera.IPABuffer> buffers);\n\tunmapBuffers(array<uint32>\
        \ ids);"
    - text: '[async] queueRequest 는 프레임 번호와 제어 목록을 받아 비동기적으로 요청을 큐에 넣습니다. 이 메서드는 즉시
        처리가 완료된다는 보장을 제공하지 않으며, 실제 처리 순서와 타이밍은 구현에 따라 달라질 수 있습니다.'
      evidence:
      - ipu3-api
      covers:
      - interface
      kind: behavior
      quote: "[async] queueRequest(uint32 frame, libcamera.ControlList controls);\n\
        \t[async] computeParams(uint32 frame, uint32 bufferId);\n\t[async] processStats(uint32\
        \ frame, int64 frameTimestamp,\n\t\t\t     uint32 bufferId, libcamera.ControlList\
        \ sensorControls);\n};"
    - text: '[async] computeParams 는 프레임과 버퍼 ID 를 받아 파라미터를 계산합니다. 이 메서드는 비동기적으로 호출되며,
        완료 시점이나 실패 여부는 반환 값이나 별도의 알림을 통해 확인해야 합니다.'
      evidence:
      - ipu3-api
      covers:
      - interface
      kind: behavior
      quote: "[async] queueRequest(uint32 frame, libcamera.ControlList controls);\n\
        \t[async] computeParams(uint32 frame, uint32 bufferId);\n\t[async] processStats(uint32\
        \ frame, int64 frameTimestamp,\n\t\t\t     uint32 bufferId, libcamera.ControlList\
        \ sensorControls);\n};"
    - text: '[async] processStats 는 프레임, 타임스탬프, 버퍼 ID 와 센서 제어 목록을 받아 통계를 처리합니다. 이
        메서드는 비동기적으로 실행되며, 호출 시점과 완료 시점 사이의 관계는 명시적으로 보장되지 않습니다.'
      evidence:
      - ipu3-api
      covers:
      - interface
      kind: behavior
      quote: "[async] queueRequest(uint32 frame, libcamera.ControlList controls);\n\
        \t[async] computeParams(uint32 frame, uint32 bufferId);\n\t[async] processStats(uint32\
        \ frame, int64 frameTimestamp,\n\t\t\t     uint32 bufferId, libcamera.ControlList\
        \ sensorControls);\n};"
    - text: IPAIPU3EventInterface 는 센서 제어 설정, 파라미터 계산 완료 및 메타데이터 준비를 위한 이벤트 인터페이스를
        제공합니다. setSensorControls 는 프레임과 센서 및 렌즈 제어 목록을 받아 설정하고, paramsComputed 은 프레임
        번호만 받아 파라미터가 계산되었음을 알립니다.
      evidence:
      - ipu3-api
      covers:
      - interface
      kind: behavior
      quote: "interface IPAIPU3EventInterface {\n\tsetSensorControls(uint32 frame,\
        \ libcamera.ControlList sensorControls,\n\t\t\t  libcamera.ControlList lensControls);\n\
        \tparamsComputed(uint32 frame);\n\tmetadataReady(uint32 frame, libcamera.ControlList\
        \ metadata);\n};"
    - text: IPARkISP1EventInterface 는 RKISP1 전용 이벤트 인터페이스로, paramsComputed 은 프레임과
        사용된 바이트 수를 함께 반환합니다. setSensorControls 와 metadataReady 도 IPU3 와 유사하게 센서 제어
        설정 및 메타데이터 준비 상태를 알립니다.
      evidence:
      - rkisp1-api
      covers:
      - interface
      kind: behavior
      quote: "interface IPARkISP1EventInterface {\n\tparamsComputed(uint32 frame,\
        \ uint32 bytesused);\n\tsetSensorControls(uint32 frame, libcamera.ControlList\
        \ sensorControls);\n\tmetadataReady(uint32 frame, libcamera.ControlList metadata);\n\
        };"
    - text: EventInterface 의 메서드 호출 시점과 실제 이벤트 발생 시점은 일치하지 않을 수 있습니다. 인터페이스 정의는 실행
        타이밍을 보장하지 않으며, 비동기 메서드는 완료 상태를 별도의 알림으로 확인해야 합니다.
      evidence:
      - ipu3-api
      covers:
      - interface
      kind: limitation
      quote: "interface IPAIPU3EventInterface {\n\tsetSensorControls(uint32 frame,\
        \ libcamera.ControlList sensorControls,\n\t\t\t  libcamera.ControlList lensControls);\n\
        \tparamsComputed(uint32 frame);\n\tmetadataReady(uint32 frame, libcamera.ControlList\
        \ metadata);\n};"
    lifetime:
    - text: '`IPAModule::load()` 함수는 모듈을 로드하거나 이미 로드된 경우에만 성공하며, 유효하지 않은 모듈이나 이미 로드된
        상태에서는 `false`를 반환합니다.'
      evidence:
      - load
      covers:
      - lifetime
      kind: behavior
      quote: "\\brief Load the IPA implementation factory from the shared object\n\
        \ *\n * The IPA module shared object implements an IPAInterface object to\
        \ be used\n * by pipeline handlers. This function loads the factory function\
        \ from the\n * shared object. Later, createInterface() can be called to instantiate\
        \ the\n * IPAInterface.\n *\n * This function only needs to be called successfully\
        \ once, after which\n * createInterface() can be called as many times as IPAInterface\
        \ instances are\n * needed.\n *\n * Calling this function on an invalid module\
        \ (as returned by isValid()) is\n * an error.\n *\n * \\return True if load\
        \ was successful, or already loaded, and false otherwise\n */\nbool IPAModule::load()\n\
        {\n\tif (!valid_)\n\t\treturn false;"
    - text: '`IPAModule::createInterface()` 함수는 모듈이 로드되지 않았거나 유효하지 않은 경우 `nullptr`를
        반환하며, 성공 시 인터페이스 인스턴스를 생성합니다.'
      evidence:
      - load
      covers:
      - lifetime
      kind: behavior
      quote: "/**\n * \\brief Instantiate an IPA interface\n *\n * After loading the\
        \ IPA module with load(), this function creates an instance\n * of the IPA\
        \ module interface.\n *\n * Calling this function on a module that has not\
        \ yet been loaded, or an\n * invalid module (as returned by load() and isValid(),\
        \ respectively) is\n * an error.\n *\n * \\return The IPA interface on success,\
        \ or nullptr on error\n */\nIPAInterface *IPAModule::createInterface()\n{\n\
        \tif (!valid_ || !loaded_)\n\t\treturn nullptr;"
    - text: '`{{proxy_name}}Threaded` 프록시는 생성 시 `ipam->load()`와 `ipam->createInterface()`를
        호출하여 인터페이스를 초기화하고, 실패 시 로그를 기록한 후 초기화를 중단합니다.'
      evidence:
      - threaded
      covers:
      - lifetime
      kind: behavior
      quote: "if (!ipam->load())\n\t\treturn;"
    - text: '`{{proxy_name}}Threaded` 프록시는 `start()` 호출 시 스레드를 시작하고, `stop()` 호출 시
        상태가 `ProxyRunning`이 아닌 경우 중단하며, `ProxyStopping` 상태로 전환 후 스레드 종료와 메시지 처리를 수행합니다.'
      evidence:
      - threaded
      covers:
      - lifetime
      kind: behavior
      quote: "return {{ \"_ret\" if method|method_return_value != \"void\" }};\n{%-\
        \ elif method.mojom_name == \"start\" %}\n\tstate_ = ProxyRunning;\n\tthread_.start();"
    - text: '`{{proxy_name}}Isolated` 프록시는 생성 시 IPC 파이프를 설정하고, 종료 시 `Exit` 명령을 통해
        비동기 메시지를 전송하여 정리됩니다.'
      evidence:
      - isolated
      covers:
      - lifetime
      kind: behavior
      quote: "{{proxy_name}}Isolated::~{{proxy_name}}Isolated()\n{\n\tif (ipc_) {\n\
        \t\tIPCMessage::Header header =\n\t\t\t{ static_cast<uint32_t>({{cmd_enum_name}}::Exit),\
        \ seq_++ };\n\t\tIPCMessage msg(header);\n\t\tipc_->sendAsync(msg);\n\t}\n\
        }"
    - text: '`{{proxy_name}}Isolated` 프록시는 `configure()` 호출 시 `controlSerializer_`를
        초기화하며, 비동기 호출 시 `_ipcInputBuf`를 전송하고 결과를 디시리얼라이즈하여 반환합니다.'
      evidence:
      - isolated
      covers:
      - lifetime
      kind: behavior
      quote: "{% for method in interface_main.methods %}\n{{proxy_funcs.func_sig(proxy_name\
        \ + \"Isolated\", method)}}\n{\n{%- if method.mojom_name == \"configure\"\
        \ %}\n\tcontrolSerializer_.reset();\n{%- endif %}\n{%- set has_output = true\
        \ if method|method_param_outputs|length > 0 or method|method_return_value\
        \ != \"void\" %}\n{%- set cmd = cmd_enum_name + \"::\" + method.mojom_name|cap\
        \ %}\n\tIPCMessage::Header _header = { static_cast<uint32_t>({{cmd}}), seq_++\
        \ };\n\tIPCMessage _ipcInputBuf(_header);\n{%- if has_output %}\n\tIPCMessage\
        \ _ipcOutputBuf;\n{%- endif %}"
    errors:
    - text: '`createIPA` 함수는 모듈을 로드할 때 유효하지 않은 모듈이 반환되면 `nullptr`를 반환합니다. 또한 로딩된 후
        프록시가 유효하지 않으면 에러 로그를 출력하고 `nullptr`를 반환합니다.'
      evidence:
      - selection
      covers:
      - errors
      kind: behavior
      quote: "if (!proxy->isValid()) {\n\t\t\tLOG(IPAManager, Error) << \"Failed to\
        \ load proxy\";\n\t\t\treturn nullptr;\n\t\t}"
    - text: '`IPAModule::load` 함수는 유효하지 않은 모듈이거나 이미 로드된 경우를 처리하여 `false`를 반환하며, 공유
        객체를 열지 못하거나 심볼을 찾을 수 없으면 에러 로그를 출력하고 `dlHandle_`를 초기화한 뒤 `false`를 반환합니다.'
      evidence:
      - load
      covers:
      - errors
      kind: behavior
      quote: "dlHandle_ = dlopen(libPath_.c_str(), RTLD_LAZY);\n\tif (!dlHandle_)\
        \ {\n\t\tLOG(IPAModule, Error)\n\t\t\t<< \"Failed to open IPA module shared\
        \ object: \"\n\t\t\t<< dlerror();\n\t\treturn false;\n\t}"
    - text: '`{{proxy_name}}Isolated` 생성자는 IPC 파이프를 만들지 못하거나 연결에 실패하면 에러 로그를 출력하고
        초기화를 중단합니다.'
      evidence:
      - isolated
      covers:
      - errors
      kind: behavior
      quote: "auto ipc = std::make_unique<IPCPipeUnixSocket>(ipam->path().c_str(),\n\
        \t\t\t\t\t\t       proxyWorkerPath.c_str());\n\tif (!ipc->isConnected()) {\n\
        \t\tLOG(IPAProxy, Error) << \"Failed to create IPCPipe\";\n\t\treturn;\n\t\
        }"
    - text: '`IPCPipeUnixSocket::sendSync` 함수는 호출이 실패하면 에러 로그를 출력하고 음수 반환 값을 반환하며,
        타임아웃이 발생하면 `-ETIMEDOUT`을 반환합니다.'
      evidence:
      - ipc
      covers:
      - errors
      kind: behavior
      quote: "int ret = call(in.payload(), &response, in.header().cookie);\n\tif (ret)\
        \ {\n\t\tLOG(IPCPipe, Error) << \"Failed to call sync\";\n\t\treturn ret;\n\
        \t}"
    - text: '`IPCPipeUnixSocket::sendAsync` 함수는 소켓을 통해 메시지를 보낼 때 실패하면 에러 로그를 출력하고
        음수 반환 값을 반환합니다.'
      evidence:
      - ipc
      covers:
      - errors
      kind: behavior
      quote: "int IPCPipeUnixSocket::sendAsync(const IPCMessage &data)\n{\n\tint ret\
        \ = socket_->send(data.payload());\n\tif (ret) {\n\t\tLOG(IPCPipe, Error)\
        \ << \"Failed to call async\";\n\t\treturn ret;\n\t}"
    - text: '`IPCPipeUnixSocket::readyRead` 함수는 수신된 데이터가 헤더 크기보다 작으면 에러 로그를 출력하고,
        예상치 못한 데이터를 받으면 `recv` 신호를 방출합니다.'
      evidence:
      - ipc
      covers:
      - errors
      kind: behavior
      quote: "/* \\todo Use span to avoid the double copy when callData is found.\
        \ */\n\tif (payload.data.size() < sizeof(IPCMessage::Header)) {\n\t\tLOG(IPCPipe,\
        \ Error) << \"Not enough data received\";\n\t\treturn;\n\t}"
    - text: '`IPCPipeUnixSocket::call` 함수는 타임아웃이 발생하면 `-ETIMEDOUT`을 반환하고, 호출 실패 시
        음수 값을 반환하며, 성공하면 `0`을 반환합니다.'
      evidence:
      - ipc
      covers:
      - errors
      kind: behavior
      quote: "/* \\todo Make this less dangerous, see IPCPipe::sendSync() */\n\ttimeout.start(2000ms);\n\
        \twhile (!iter->second.done) {\n\t\tif (!timeout.isRunning()) {\n\t\t\tLOG(IPCPipe,\
        \ Error) << \"Call timeout!\";\n\t\t\tcallData_.erase(iter);\n\t\t\treturn\
        \ -ETIMEDOUT;\n\t\t}"
    tuning:
    - text: RKISP1 또는 Mali-C55 파이프라인에서 센서를 초기화할 때, 해당 센서 모델 이름을 사용하여 `.yaml` 확장자를
        가진 튜닝 파일을 찾습니다. 이 과정은 `ipa_->configurationFile()` 함수를 통해 수행되며, 첫 번째 인자로 센서
        모델과 `.yaml`을, 두 번째 인자로 `uncalibrated.yaml`을 지정합니다.
      evidence:
      - rkisp1-tuning
      - mali-c55-tuning
      covers:
      - tuning
      kind: behavior
      quote: "/* The IPA tuning file is made from the sensor name. */\n\tstd::string\
        \ ipaTuningFile =\n\t\tipa_->configurationFile(sensor_->model() + \".yaml\"\
        , \"uncalibrated.yaml\");"
    - text: 요청한 튜닝 파일이 존재하지 않으면, `IPAProxy::configurationFile()` 함수는 두 번째 인자로 전달된
        `uncalibrated.yaml` 파일을 대체로 사용합니다. 이 함수는 먼저 주어진 이름으로 파일을 찾은 뒤, 없으면 fallback
        이름으로 다시 검색합니다.
      evidence:
      - fallback
      covers:
      - tuning
      kind: behavior
      quote: "confPath = ipaConfigurationFile(ipaName, fallbackName, configPaths_);\n\
        \tLOG(IPAProxy, Warning)\n\t\t<< \"Configuration file '\" << name\n\t\t<<\
        \ \"' not found for IPA module '\" << ipaName\n\t\t<< \"', falling back to\
        \ '\" << confPath << \"'\";"
    - text: 두 번째 검색에서도 파일을 찾지 못하면, 함수는 빈 문자열을 반환하고 에러 로그를 출력합니다. 이때 `fallbackName`이
        비어있으면 추가적인 로깅 후 빈 문자열만 반환됩니다.
      evidence:
      - fallback
      covers:
      - tuning
      kind: behavior
      quote: "if (fallbackName.empty()) {\n\t\tLOG(IPAProxy, Error)\n\t\t\t<< \"Configuration\
        \ file '\" << name\n\t\t\t<< \"' not found for IPA module '\" << ipaName <<\
        \ \"'\";\n\t\treturn std::string();\n\t}"
    - text: RKISP1의 `uncalibrated.yaml` 파일에는 `Agc`, `Awb`, `BlackLevelCorrection`,
        `Ccm`, `GammaOutCorrection` 등의 알고리즘이 정의되어 있습니다. 이 목록은 실제 활성화된 알고리즘을 보장하지 않으며,
        누락된 항목이 반드시 비활성화된다는 의미는 아닙니다.
      evidence:
      - rkisp1-uncalibrated
      covers:
      - tuning
      kind: behavior
      quote: "# SPDX-License-Identifier: CC0-1.0\n%YAML 1.1\n---\nversion: 1\nalgorithms:\n\
        \  - Agc:\n  - Awb:\n  - BlackLevelCorrection:\n  - Ccm:\n  - GammaOutCorrection:\n\
        ..."
    - text: Mali-C55의 `uncalibrated.yaml` 파일에도 동일한 알고리즘 목록이 포함되어 있으며, 이는 RKISP1과 유사한
        구조를 가집니다. 이 파일들도 센서별 튜닝 정보가 없을 때 대체로 사용됩니다.
      evidence:
      - mali-c55-uncalibrated
      covers:
      - tuning
      kind: behavior
      quote: "# SPDX-License-Identifier: CC0-1.0\n%YAML 1.1\n---\nversion: 1\nalgorithms:\n\
        \  - Agc:\n  - Awb:\n  - BlackLevelCorrection:\n  - Ccm:\n..."
    dma-import:
    - text: '`createDMABufTexture2D()` 함수는 `eglImage.format_` 값을 확인하여 GL 형식에 따라 DRM
        형식을 매핑합니다. `GL_RED` 또는 `GL_LUMINANCE`인 경우 `DRM_FORMAT_R8`, `GL_RG`인 경우 `DRM_FORMAT_GR88`,
        그리고 `GL_RGBA`인 경우 `DRM_FORMAT_ARGB8888`를 각각 사용합니다.'
      evidence:
      - import
      covers:
      - dma-import
      kind: behavior
      quote: "switch (eglImage.format_) {\n\tcase GL_RED:\n\tcase GL_LUMINANCE:\n\t\
        \tdrm_format = DRM_FORMAT_R8;\n\t\tbreak;\n\tcase GL_RG:\n\t\tdrm_format =\
        \ DRM_FORMAT_GR88;\n\t\tbreak;\n\tcase GL_RGBA:\n\t\tdrm_format = DRM_FORMAT_ARGB8888;\n\
        \t\tbreak;\n\tdefault:\n\t\tLOG(eGL, Error) << \"unhandled GL format\";\n\t\
        \treturn -ENODEV;\n\t}"
      part_id: formats
    - text: '`createDMABufTexture2D()` 함수의 `switch` 문에서 기본(`default`) 분기가 실행되면, 처리되지
        않은 GL 포맷에 대해 오류 로그가 출력됩니다.'
      evidence:
      - import
      covers:
      - dma-import
      kind: behavior
      quote: "switch (eglImage.format_) {\n\tcase GL_RED:\n\tcase GL_LUMINANCE:\n\t\
        \tdrm_format = DRM_FORMAT_R8;\n\t\tbreak;\n\tcase GL_RG:\n\t\tdrm_format =\
        \ DRM_FORMAT_GR88;\n\t\tbreak;\n\tcase GL_RGBA:\n\t\tdrm_format = DRM_FORMAT_ARGB8888;\n\
        \t\tbreak;\n\tdefault:\n\t\tLOG(eGL, Error) << \"unhandled GL format\";\n\t\
        \treturn -ENODEV;\n\t}"
      part_id: unsupported
    - text: '`createDMABufTexture2D()` 함수의 `switch` 문에서 기본(`default`) 분기가 실행되면, `-ENODEV`를
        반환합니다.'
      evidence:
      - import
      covers:
      - dma-import
      kind: behavior
      quote: "switch (eglImage.format_) {\n\tcase GL_RED:\n\tcase GL_LUMINANCE:\n\t\
        \tdrm_format = DRM_FORMAT_R8;\n\t\tbreak;\n\tcase GL_RG:\n\t\tdrm_format =\
        \ DRM_FORMAT_GR88;\n\t\tbreak;\n\tcase GL_RGBA:\n\t\tdrm_format = DRM_FORMAT_ARGB8888;\n\
        \t\tbreak;\n\tdefault:\n\t\tLOG(eGL, Error) << \"unhandled GL format\";\n\t\
        \treturn -ENODEV;\n\t}"
      part_id: unsupported
    - text: '`createDMABufTexture2D()` 함수 내부에서 `eglCreateImageKHR()` 호출이 실패하여 `EGL_NO_IMAGE_KHR`를
        반환하면, 디버깅 로그에 "eglCreateImageKHR fail"라는 메시지를 출력하고 `eglImage.dmabuf_import_failed_`
        플래그를 `true`로 설정한 뒤 `-ENODEV`를 반환합니다.'
      evidence:
      - import
      covers:
      - dma-import
      kind: behavior
      quote: "if (image == EGL_NO_IMAGE_KHR) {\n\t\tLOG(eGL, Debug) << \"eglCreateImageKHR\
        \ fail\";\n\t\teglImage.dmabuf_import_failed_ = true;\n\t\treturn -ENODEV;\n\
        \t}"
      part_id: image-failure
    - text: '`createInputDMABufTexture2D()` 함수는 내부적으로 `createDMABufTexture2D()` 함수를
        호출할 때 마지막 인자로 `false` 값을 전달합니다.'
      evidence:
      - import
      covers:
      - dma-import
      kind: behavior
      quote: 'return createDMABufTexture2D(eglImage, fd, false);

        }'
      part_id: wrappers
    - text: '`createOutputDMABufTexture2D()` 함수는 내부적으로 `createDMABufTexture2D()` 함수를
        호출할 때 마지막 인자로 `true` 값을 전달합니다.'
      evidence:
      - import
      covers:
      - dma-import
      kind: behavior
      quote: 'return createDMABufTexture2D(eglImage, fd, true);

        }'
      part_id: wrappers
    - text: '`createDMABufTexture2D()` 함수는 `output` 매개변수가 참일 때만 프레임버퍼 객체 (FBO) 에 텍스처를
        연결하는 작업을 수행합니다.'
      evidence:
      - import
      covers:
      - dma-import
      kind: behavior
      quote: "if (output)\n\t\tret = attachTextureToFBO(eglImage);"
      part_id: framebuffer
    - text: '`output` 가 참인 경우 `attachTextureToFBO(eglImage)` 함수를 호출하여 연결을 완료하고 그 반환값으로
        `ret` 변수에 대입합니다.'
      evidence:
      - import
      covers:
      - dma-import
      kind: behavior
      quote: "if (output)\n\t\tret = attachTextureToFBO(eglImage);"
      part_id: framebuffer
    softisp-lsc:
    - text: 두 셰이더 모두에서 블랙 레벨 보정은 가장 먼저 수행되며, `rgb = (rgb - blacklevel) / (1.0 - blacklevel)`
        식으로 입력 색상을 센서 범위 내의 부동 소수점 값으로 변환합니다.
      evidence:
      - packed-shader
      - unpacked-shader
      covers:
      - softisp-lsc
      kind: behavior
      quote: "rgb = (rgb - blacklevel) / (1.0 - blacklevel);\n\n#if defined(APPLY_LSC)\n\
        \        /* Multiple by 4.0 for UQ<2, 6> -> float conversion:\n         *\
        \ texture2D(...) = original_float * 2^6 (quantization) * 1/2^8 (texture byte\
        \ to float)\n         * => original_float = texture2D(...) / 2^6 * 2^8 = texture2D(...)\
        \ * 2^2\n         */\n        rgb = rgb * (texture2D(lsc_tex, textureOut).rgb\
        \ * 4.0);\n#endif\n\n\t/* Apply AWB gains, and saturate each channel at sensor\
        \ range */\n\trgb = clamp(rgb * awb, vec3(0.0), vec3(1.0));\n\n\t/* Colour\
        \ Correction Matrix */\n\trgb = ccm * rgb;\n\n\t/*\n\t * Contrast\n\t * contrastExp\
        \ 0..2 contrast to 0..infinity; avoid actual infinity at tan(pi/2)\n\t */\n\
        \trgb = clamp(rgb, 0.0, 1.0);\n\trgb.r = apply_contrast(rgb.r);\n\trgb.g =\
        \ apply_contrast(rgb.g);\n\trgb.b = apply_contrast(rgb.b);\n\n\t/* Apply gamma\
        \ after colour correction */\n\trgb = pow(rgb, vec3(gamma));\n\n#if defined\
        \ (SWAP_BLUE)\n\tgl_FragColor = vec4(rgb.bgr, 1.0);\n#else\n\tgl_FragColor\
        \ = vec4(rgb, 1.0);\n#endif\n}"
    - text: '`APPLY_LSC` 조건이 정의된 경우 렌즈 음영 보정은 그 다음 단계에서 적용되며, `rgb = rgb * (texture2D(lsc_tex,
        textureOut).rgb * 4.0)` 또는 `rgb = rgb * (texture2D(lsc_tex, center.xy).rgb
        * 4.0)` 식으로 LSC 텍스처 값을 4 배로 곱해 부동 소수점 변환을 수행합니다.'
      evidence:
      - packed-shader
      covers:
      - softisp-lsc
      kind: behavior
      quote: "rgb = (rgb - blacklevel) / (1.0 - blacklevel);\n\n#if defined(APPLY_LSC)\n\
        \        /* Multiple by 4.0 for UQ<2, 6> -> float conversion:\n         *\
        \ texture2D(...) = original_float * 2^6 (quantization) * 1/2^8 (texture byte\
        \ to float)\n         * => original_float = texture2D(...) / 2^6 * 2^8 = texture2D(...)\
        \ * 2^2\n         */\n        rgb = rgb * (texture2D(lsc_tex, textureOut).rgb\
        \ * 4.0);\n#endif\n\n\t/* Apply AWB gains, and saturate each channel at sensor\
        \ range */\n\trgb = clamp(rgb * awb, vec3(0.0), vec3(1.0));\n\n\t/* Colour\
        \ Correction Matrix */\n\trgb = ccm * rgb;\n\n\t/*\n\t * Contrast\n\t * contrastExp\
        \ 0..2 contrast to 0..infinity; avoid actual infinity at tan(pi/2)\n\t */\n\
        \trgb = clamp(rgb, 0.0, 1.0);\n\trgb.r = apply_contrast(rgb.r);\n\trgb.g =\
        \ apply_contrast(rgb.g);\n\trgb.b = apply_contrast(rgb.b);\n\n\t/* Apply gamma\
        \ after colour correction */\n\trgb = pow(rgb, vec3(gamma));\n\n#if defined\
        \ (SWAP_BLUE)\n\tgl_FragColor = vec4(rgb.bgr, 1.0);\n#else\n\tgl_FragColor\
        \ = vec4(rgb, 1.0);\n#endif\n}"
    - text: '`unpacked-shader`에서는 렌즈 음영 보정을 적용할 때 `texture2D(lsc_tex, center.xy)`를
        사용하여 텍스처의 중심 좌표만 참조합니다.'
      evidence:
      - unpacked-shader
      covers:
      - softisp-lsc
      kind: behavior
      quote: "rgb = (rgb - blacklevel) / (1.0 - blacklevel);\n\n#if defined(APPLY_LSC)\n\
        \    /* Multiple by 4.0 for UQ<2, 6> -> float conversion */\n    rgb = rgb\
        \ * (texture2D(lsc_tex, center.xy).rgb * 4.0);\n#endif\n\n    /* Apply AWB\
        \ gains, and saturate each channel at sensor range */\n    rgb = clamp(rgb\
        \ * awb, vec3(0.0), vec3(1.0));\n\n    /* Colour Correction Matrix */\n  \
        \  rgb = ccm * rgb;\n\n    /*\n     * Contrast\n     */\n    rgb = clamp(rgb,\
        \ 0.0, 1.0);\n    rgb.r = apply_contrast(rgb.r);\n    rgb.g = apply_contrast(rgb.g);\n\
        \    rgb.b = apply_contrast(rgb.b);\n\n    /* Apply gamma after colour correction\
        \ */\n    rgb = pow(rgb, vec3(gamma));\n\n#if defined (SWAP_BLUE)\n    gl_FragColor\
        \ = vec4(rgb.bgr, 1.0);\n#else\n    gl_FragColor = vec4(rgb, 1.0);\n#endif\n\
        }"
    - text: 렌즈 음영 보정 이후에는 AWB 이득을 적용하고 각 채널을 센서 범위 `vec3(0.0)`에서 `vec3(1.0)`로 포화시키며,
        `rgb = clamp(rgb * awb, vec3(0.0), vec3(1.0))`를 통해 수행합니다.
      evidence:
      - packed-shader
      covers:
      - softisp-lsc
      kind: behavior
      quote: "rgb = (rgb - blacklevel) / (1.0 - blacklevel);\n\n#if defined(APPLY_LSC)\n\
        \        /* Multiple by 4.0 for UQ<2, 6> -> float conversion:\n         *\
        \ texture2D(...) = original_float * 2^6 (quantization) * 1/2^8 (texture byte\
        \ to float)\n         * => original_float = texture2D(...) / 2^6 * 2^8 = texture2D(...)\
        \ * 2^2\n         */\n        rgb = rgb * (texture2D(lsc_tex, textureOut).rgb\
        \ * 4.0);\n#endif\n\n\t/* Apply AWB gains, and saturate each channel at sensor\
        \ range */\n\trgb = clamp(rgb * awb, vec3(0.0), vec3(1.0));\n\n\t/* Colour\
        \ Correction Matrix */\n\trgb = ccm * rgb;\n\n\t/*\n\t * Contrast\n\t * contrastExp\
        \ 0..2 contrast to 0..infinity; avoid actual infinity at tan(pi/2)\n\t */\n\
        \trgb = clamp(rgb, 0.0, 1.0);\n\trgb.r = apply_contrast(rgb.r);\n\trgb.g =\
        \ apply_contrast(rgb.g);\n\trgb.b = apply_contrast(rgb.b);\n\n\t/* Apply gamma\
        \ after colour correction */\n\trgb = pow(rgb, vec3(gamma));\n\n#if defined\
        \ (SWAP_BLUE)\n\tgl_FragColor = vec4(rgb.bgr, 1.0);\n#else\n\tgl_FragColor\
        \ = vec4(rgb, 1.0);\n#endif\n}"
    - text: AWB 적용 후 색 보정 행렬 `ccm`을 곱하여 색상을 보정하고, `rgb = ccm * rgb`로 표현됩니다.
      evidence:
      - packed-shader
      covers:
      - softisp-lsc
      kind: behavior
      quote: "rgb = (rgb - blacklevel) / (1.0 - blacklevel);\n\n#if defined(APPLY_LSC)\n\
        \        /* Multiple by 4.0 for UQ<2, 6> -> float conversion:\n         *\
        \ texture2D(...) = original_float * 2^6 (quantization) * 1/2^8 (texture byte\
        \ to float)\n         * => original_float = texture2D(...) / 2^6 * 2^8 = texture2D(...)\
        \ * 2^2\n         */\n        rgb = rgb * (texture2D(lsc_tex, textureOut).rgb\
        \ * 4.0);\n#endif\n\n\t/* Apply AWB gains, and saturate each channel at sensor\
        \ range */\n\trgb = clamp(rgb * awb, vec3(0.0), vec3(1.0));\n\n\t/* Colour\
        \ Correction Matrix */\n\trgb = ccm * rgb;\n\n\t/*\n\t * Contrast\n\t * contrastExp\
        \ 0..2 contrast to 0..infinity; avoid actual infinity at tan(pi/2)\n\t */\n\
        \trgb = clamp(rgb, 0.0, 1.0);\n\trgb.r = apply_contrast(rgb.r);\n\trgb.g =\
        \ apply_contrast(rgb.g);\n\trgb.b = apply_contrast(rgb.b);\n\n\t/* Apply gamma\
        \ after colour correction */\n\trgb = pow(rgb, vec3(gamma));\n\n#if defined\
        \ (SWAP_BLUE)\n\tgl_FragColor = vec4(rgb.bgr, 1.0);\n#else\n\tgl_FragColor\
        \ = vec4(rgb, 1.0);\n#endif\n}"
    - text: 색 보정 이후에는 대비를 적용하기 위해 각 채널을 `0.0`에서 `1.0`으로 포화시키고, `apply_contrast` 함수를
        호출하여 대비를 조정합니다.
      evidence:
      - packed-shader
      covers:
      - softisp-lsc
      kind: behavior
      quote: "rgb = (rgb - blacklevel) / (1.0 - blacklevel);\n\n#if defined(APPLY_LSC)\n\
        \        /* Multiple by 4.0 for UQ<2, 6> -> float conversion:\n         *\
        \ texture2D(...) = original_float * 2^6 (quantization) * 1/2^8 (texture byte\
        \ to float)\n         * => original_float = texture2D(...) / 2^6 * 2^8 = texture2D(...)\
        \ * 2^2\n         */\n        rgb = rgb * (texture2D(lsc_tex, textureOut).rgb\
        \ * 4.0);\n#endif\n\n\t/* Apply AWB gains, and saturate each channel at sensor\
        \ range */\n\trgb = clamp(rgb * awb, vec3(0.0), vec3(1.0));\n\n\t/* Colour\
        \ Correction Matrix */\n\trgb = ccm * rgb;\n\n\t/*\n\t * Contrast\n\t * contrastExp\
        \ 0..2 contrast to 0..infinity; avoid actual infinity at tan(pi/2)\n\t */\n\
        \trgb = clamp(rgb, 0.0, 1.0);\n\trgb.r = apply_contrast(rgb.r);\n\trgb.g =\
        \ apply_contrast(rgb.g);\n\trgb.b = apply_contrast(rgb.b);\n\n\t/* Apply gamma\
        \ after colour correction */\n\trgb = pow(rgb, vec3(gamma));\n\n#if defined\
        \ (SWAP_BLUE)\n\tgl_FragColor = vec4(rgb.bgr, 1.0);\n#else\n\tgl_FragColor\
        \ = vec4(rgb, 1.0);\n#endif\n}"
    - text: 마지막으로 감마 보정을 적용하여 `rgb = pow(rgb, vec3(gamma))`로 색상을 변환하고, `SWAP_BLUE`
        조건에 따라 채널 순서를 변경하거나 그대로 출력합니다.
      evidence:
      - packed-shader
      covers:
      - softisp-lsc
      kind: behavior
      quote: "rgb = (rgb - blacklevel) / (1.0 - blacklevel);\n\n#if defined(APPLY_LSC)\n\
        \        /* Multiple by 4.0 for UQ<2, 6> -> float conversion:\n         *\
        \ texture2D(...) = original_float * 2^6 (quantization) * 1/2^8 (texture byte\
        \ to float)\n         * => original_float = texture2D(...) / 2^6 * 2^8 = texture2D(...)\
        \ * 2^2\n         */\n        rgb = rgb * (texture2D(lsc_tex, textureOut).rgb\
        \ * 4.0);\n#endif\n\n\t/* Apply AWB gains, and saturate each channel at sensor\
        \ range */\n\trgb = clamp(rgb * awb, vec3(0.0), vec3(1.0));\n\n\t/* Colour\
        \ Correction Matrix */\n\trgb = ccm * rgb;\n\n\t/*\n\t * Contrast\n\t * contrastExp\
        \ 0..2 contrast to 0..infinity; avoid actual infinity at tan(pi/2)\n\t */\n\
        \trgb = clamp(rgb, 0.0, 1.0);\n\trgb.r = apply_contrast(rgb.r);\n\trgb.g =\
        \ apply_contrast(rgb.g);\n\trgb.b = apply_contrast(rgb.b);\n\n\t/* Apply gamma\
        \ after colour correction */\n\trgb = pow(rgb, vec3(gamma));\n\n#if defined\
        \ (SWAP_BLUE)\n\tgl_FragColor = vec4(rgb.bgr, 1.0);\n#else\n\tgl_FragColor\
        \ = vec4(rgb, 1.0);\n#endif\n}"
    - text: '`softisp-interface`에서는 `IPASoftIspInterface` 인터페이스가 렌즈 음영 보정 버퍼를 전달하는
        메커니즘을 정의하지만, 실제 GPU 실행 단계나 구체적인 적용 시점은 이 문서의 선언 범위에서 설명되지 않습니다.'
      evidence:
      - softisp-interface
      covers:
      - softisp-lsc
      kind: limitation
      quote: "interface IPASoftIspInterface {\n\tinit(libcamera.IPASettings settings,\n\
        \t     libcamera.SharedFD fdStats,\n\t     libcamera.SharedFD fdParams,\n\t\
        \     libcamera.IPACameraSensorInfo sensorInfo,\n\t     libcamera.ControlInfoMap\
        \ sensorControls)\n\t\t=> (int32 ret,\n\t\t    libcamera.ControlInfoMap ipaControls,\n\
        \t\t    bool ccmEnabled, bool lscEnabled);\n\tstart() => (int32 ret);\n\t\
        stop();\n\tconfigure(IPAConfigInfo configInfo)\n\t\t=> (int32 ret, libcamera.ControlInfoMap\
        \ ipaControls);"
  topic_inputs:
    selection: f43c3fbfbeb3fe08ca6c7ac2ccf54ac201bd8c7805f4d4323f8acfee280ce49a
    execution: 2695b7ce5caf6d25e81c3f1ef7c09723c859d70a9a36ecd5666c5e05cc6df22c
    interface: 9c00456b24365248095f2940317009063a8dca9ccb6f3035cb6e1c75c0aee3f9
    lifetime: bff92a7a8e2b6f89c1a51d0d7e597f00e60a905f234038f103b1325a76f03353
    tuning: 621f9e2ee984a852db21a93c68ec98ced7290f3141b1c12a4e9ac41e4b756432
    dma-import: 195b3588bddb0390bec4482474ba5b6ccc74e60841ff4cb23c42c32270ea2289
    softisp-lsc: 48ef95264d20d3065b924d790e848e802929a4454ccfee826de5bfde3ab51176
  reused_topics:
  - selection
  - execution
  - interface
  - lifetime
  - errors
  - tuning
  - dma-import
  - softisp-lsc
  replayed_units: []
  generated_topics: []
  topic_agents:
    selection: ollama/qwen3.5:9b
    execution: ollama/qwen3.5:9b
    interface: ollama/qwen3.5:9b
    lifetime: ollama/qwen3.5:9b
    errors: ollama/qwen3.5:9b
    tuning: ollama/qwen3.5:9b
    dma-import: ollama/qwen3.5:9b
    softisp-lsc: ollama/qwen3.5:9b
  grounding_review: passed
  grounding_policy: c54006f7c90cb2af955e1ede18b761c7feb22dffa3bc37a885c019508348eba0
  body_sha256: 55cc706bc187ebe9beac0903128ac2d538443830fb2fed5d2bf3210dbf88478f
  maintenance_mode: recorded-http-answer-selection
  maintenance_lineage:
  - mode: recorded-http-answer-selection
    source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
    paragraph_layout: legacy
    maintained_at: '2026-10-26T16:55:19+00:00'
    original_page_sha256: 0168aca3d0a5e6960126144450fce443ef5051c411b7e582cddacd1f2dd3f7ee
    original_body_sha256: 0f25f1c9edc73877e508ebc2e803b83e6a293f51b6e3ee21768bb59f01346bbf
    before_input_fingerprint: 84611553aff2de125c4a301d56f8b196027713cb1261cbeea7f5b956cb7d641f
    removed_statements:
    - topic: errors
      index: 2
      sha256: 03c88723da7f082baf536577f8b384b45d9bde2382e8fb60d5b4faa758bf46cb
    removed_parts: []
    selected_statements:
      selection:
      - dd78a930745f05d99ea01992e22e5477b3156d616d2d53931ae5bc8946bf3d22
      - fda0a73bb9228df3a416fd79c7bb9c6a4162bc0a8ed254090c5ac56fa7bdf15e
      - 5b6e75675c8fa88f31491fcf89990a7a920473768b63e96118df9aa390a62ca2
      - 2bdfc18605398e7dea845a29db2e23eb47f4293a0c3a288cbf846ab110d18448
      - 7f68a38c340e1198f3a201324d78761a99102b54ad985a390a672a1011990f37
      - 6148012b6a86b04274b3cf8db33906fa4d5bbd85ee8d6716c62eaf1e5b7b6fed
      execution:
      - 01126382108ee7361aa481d3ccae8be391906966255e10fc12169e236bc05921
      - 92ebae37fd45168145a66790db4d9e04a7f9f962263594d72df62b3613bccf81
      - a44949af9c70b703a2abc24a5468f4e277af2285681c1c095fff24840863569b
      - 2e1929c7b434628f469bda5df2e8dd1b3f52827e70cbc53c429260fd8372d626
      - ee056d79201e16d8f6a182bd8ed3d39ca06cd96e9d6b038a76c39b7888492334
      - da28db5ad35a51f039c0c54323fe268556699d48937ebc5a94b2c8985d9e5482
      - 5ca9be368af427b9c371b6717231058be3c73031ced5a4030d3322f9ca57f544
      - a91a76d7c6bd26806e24ae07d9deee90eb6c4a8bf316f1cc57f8b032418d4ec1
      - 868f8ed9e8fc096972a883e7fe29ef964e5fc25a9c1d1eea82070cebfe016aec
      - 732746f9ec990c0c718fd6708b622b37564ea6bb6c0e8b566f4efc00b0b7374d
      - 2370b5eac5564d810ab5b0d54ee8c8bfd047aadf86d5bd81fdf43d3afc28dcb6
      - 8a83a298aea1f17b3318d028cc207aed26edd9e61cb505361e635078a935ca0f
      - 82e950e2eca4db09a3f3abebe7e219cc9d19440f45fc5dfe7abeda11a277a7d0
      - ab007f35de0a390edd6d68ee9627198dcf737dbe125f9a13cf8a9ed10955957d
      - 3185e3e241f0b3d2b673c57eeb96eb7104dc86cbf2a7d5654ac3cf015d9473a0
      - 8382b93cac979543d17085564d57444069cf9207cce9c6215a5710fb40821cd3
      interface:
      - 6d5ba7233ded30e250fd337be533feaf007609c67dc811984e1adcc95dcee33e
      - 12fe3e8cd82dc368c40c5f88b72ba1839c9503cedb12890875aebe27c19d1318
      - e6557a3a6a68555f29ce89fd553e0280e19fc22a0df9a7a0946992760e385904
      - 1a30c4a9d299a7c774bcc9298af5266f1e72f4ea6da1cf701a8bb0f605c540be
      - c5835a03c85afb3c8077846cb1664ab4223c7a7b397076e4cf2fc6ecb661e89e
      - 6340cb58702773320685342e0130afbbf3f304cc49d43217eb96b1ed10bc98bc
      - a97af70cd415abfa8b42c4d741aa6d2946c148ea2b32c15e6fa9c4f7fcaddeaf
      - 7e20fbc042ad30520f0817306ce16344e66ef2f60e56bbf990b168d0e65afc5c
      lifetime:
      - 5c32b48dab2fcfc09f8ffdfc24dc3f9c349264b11be1c495c98236e9418f9f34
      - 659ff88b22783a81f2a0d1809b97f6f35eab7b2443f7c3044a9607770ca6c842
      - cd7e1090065571257b37a4206f11df51f9095b03dbc95a5364785090f8a8ce04
      - fc61cfd267e8dc1c9a1b23c72a86969aec637e97d5baf10efec3aecc7495d151
      - c78c5f89ff1640871099ad5c6ce3943817222256d7b7f18fe827a29738419baf
      - 082165db2a3c706d6514917936be33dee7a4e557402dd52c9d450e92e7813897
      errors:
      - 50fa000a1268cb45fc0b7074e0d76560c50ffbeb8083e1b5d6dcbc87ee8fbf76
      - 923a74b30486240e43411cfd10e227cc884c67fa27ec124bae1ce8616d6a6890
      - 2936eb82d4a95fb2ba6c319351ae9dbcf2ee2eeea9463def995915dbab0cd7b4
      - 60da3e1b3649f1d28b2785c8985de8afb3427e22c36ac3dee2fc6bd2a37bbaee
      - 15b7c6571e9be1327059eaf478ddd1040ec1b2eac144308a9d31f721bab6011f
      - 643d2bedbe76d06b741dbf213d161ab2073f157739c9ab02989664295998075e
      - 65de1f7ed9d8ca7d08f6c2c718e21a58890674781ca5714935b447f1177672d4
      tuning:
      - d29c85a8b8325fbdb9a78bef641a2dfb0e5b15765cf99461e898a9b529477bfd
      - daa11f04604b3a46adade213c4265e983f06252eea3ecfc9a8392a953f4bbfe4
      - bdeee7aa5c6b4b49a7752ae36f2d6eb6a663afa8c55f94befe409296fd64d9df
      - b0f76dda69cad8af77a54c0dc5f1de3ed248afae9f612779d10c6d05108e2445
      - 20cf2b256f4b009cff967893182c2f5cb781bafd92fd7f456dc8a83e5c31d718
      dma-import:
      - 20ce0bfdbba75db51286808ee9e62ba825782cdaa001f1e69fae359722bd97be
      - dd9703871f20e465e91f94b402e9106dbe3aa61f3981a2e9cc38a04dcc15bedd
      - cde63ee52d53c4440670c1c8ccbd4a478ecaceba5a31f5a718a0ab55db9988a9
      - 08be87f066f83f797e4d1831145f5b0fe5a71f370230c054a15460d36d6a894a
      - 808ec6f57883277ef30fb94405586207310495fc290592ab417245a8cc1ace9d
      - e52a8f53980a8759b77e511e7526d144da00b36d7e7e2155439d0539eef87e7b
      - 8513b2b8fd8546d072edbd38615b0a3e06aa83fc6f50ce6f5fe10d201577257f
      - 64b0c5398e9a0f997afae215412b83059aa76818a9c72b9bf0cc9cd9b82e5c36
      softisp-lsc:
      - 4f56bee9b24212f7bbdcbb228043a105f4e64c7cfda85cf8c8b2985382fb4e1d
      - ddc878017e73637e578a7f2e6a259b99b923c448ebea6508e78e439cebd43073
      - 373cbf2992725da916a100c8eced4f6a4dfff1f071a7399ca08fea95d18bec68
      - c4e87ba6e9d8904718940bbf1c6f0d91ecda455024524dd8e9c05b0beec3e21d
      - 146a40a8570d61ea6876c05ba399afecdc18647bf07ec967380624bd0fc7b9f3
      - 17919044fbbc84f145de87a3ac4b8878c7efebb553fdc94f53cb15fdcfcb0bb4
      - 93e2acff5ce12cffc3fba99d937daa0bb099c2ba84ffb7954efbd4c1eaa3508a
      - 754c0893ba34bbe6dfef5ae91da8b1c728bea1e14183520a2f233733f758d71b
    original_producers:
      selection: ollama/qwen3.5:9b
      execution: ollama/qwen3.5:9b
      interface: ollama/qwen3.5:9b
      lifetime: ollama/qwen3.5:9b
      errors: ollama/qwen3.5:9b
      tuning: ollama/qwen3.5:9b
      dma-import: ollama/qwen3.5:9b
      softisp-lsc: ollama/qwen3.5:9b
    zero_model_calls: true
    human_review: pending
---

# IPA 관리와 구현 진입점

**IPA 모듈 선택, 스레드·프로세스 경계와 요청·결과 인터페이스를 구현 근거로 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 모듈 탐색과 격리 조건 절을 확인합니다. | [모듈 탐색과 격리 조건](#모듈-탐색과-격리-조건) |
| 스레드와 프로세스 경계 절을 확인합니다. | [스레드와 프로세스 경계](#스레드와-프로세스-경계) |
| 프레임 입력과 결과 인터페이스 절을 확인합니다. | [프레임 입력과 결과 인터페이스](#프레임-입력과-결과-인터페이스) |
| IPA 객체와 종료 순서 절을 확인합니다. | [IPA 객체와 종료 순서](#ipa-객체와-종료-순서) |
| 생성과 IPC 실패 절을 확인합니다. | [생성과 IPC 실패](#생성과-ipc-실패) |
| 보정 전 튜닝 파일 절을 확인합니다. | [보정 전 튜닝 파일](#보정-전-튜닝-파일) |

## 모듈 탐색과 격리 조건

`IPAManager::IPAManager()` 함수는 사용자 지정 경로를 먼저 확인하고, libcamera 가 설치되지 않은 경우 빌드 디렉토리를 추가하며, 마지막으로 시스템 설치 경로를 검색합니다. `src/libcamera/ipa_manager.cpp:107`

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

사용자가 'ipa.`module_paths`' 옵션으로 경로를 지정하지 않으면 빌드 디렉토리와 시스템 설치 경로만 검색되며, 모듈이 없으면 경고 로그가 출력됩니다. `src/libcamera/ipa_manager.cpp:107`

`IPAModule::match()` 함수는 모듈 이름과 버전 범위를 비교하여 일치하는지 확인하며, false 를 반환하면 해당 모듈은 선택되지 않습니다. `src/libcamera/ipa_module.cpp:460`

createIPA() 함수는 module() 으로 찾은 모듈이 없으면 nullptr 를 반환하고, 프록시 생성 시 서명이 유효하지 않으면 Isolated 실행 방식을 선택합니다. `include/libcamera/internal/ipa_manager.h:35`

서명 검증이 실패하거나 `forceIsolation_` 가 true 일 경우 isSignatureValid() 는 false 를 반환하고, createIPA() 는 Isolated 실행 방식을 선택합니다. `src/libcamera/ipa_manager.cpp:289`

서명이 유효하지 않으면 createIPA() 는 Isolated 실행 방식을 선택하고, 프록시 생성이 실패하면 nullptr 를 반환합니다. `include/libcamera/internal/ipa_manager.h:35`

근거 원문: [src/libcamera/ipa_manager.cpp:107](#source-7603cbafe8eef490) · [src/libcamera/ipa_module.cpp:460](#source-6e1525c1fc1aa55e) · [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) · [src/libcamera/ipa_manager.cpp:289](#source-532f8ffa194bd319)

## 스레드와 프로세스 경계

`init-branch:0`에 포함된 템플릿 코드는 `method.mojom_name`이 `init`일 때 `ipa_`를 호출하여 IPA 메서드를 직접 실행하는 경로를 제공합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:82`

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

`init` 메서드가 호출된 직후 `proxy_.moveToThread(&thread_)`가 실행되며, 이 호출에 전달되는 스레드 객체는 `thread_`라는 변수를 가리킵니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:82`

`start-branch:0` 인용문에 따르면 worker 스레드를 `thread_.start()` 함수로 시작한 뒤 바로 `ThreadProxy::start`를 `ConnectionTypeBlocking` 연결 유형으로 호출합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93`

`{{proxy_name}}Threaded` 클래스의 일반 동기 메서드 분기에서는 `init`, `start`, `stop` 을 제외한 모든 호출이 `ipa_->{{method.mojom_name}}(...)` 경로를 통해 직접 호출됩니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:75`

`async-assert` 파일의 `{% elif method|is_async %}` 조건부 블록 내부에는 `ASSERT(state_ == ProxyRunning);`라는 매크로 호출이 포함되어 있습니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:110`

`Threaded` 비동기 분기의 `invokeMethod` 호출은 `method|is_async` 조건이 참일 때만 실행되며, 이때 전달되는 연결 유형은 `ConnectionTypeQueued` 입니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:109`

`{{proxy_name}}Threaded` 생성자는 초기화 과정에서 `ipam->load()`를 호출하여 IPA 모듈을 로드합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48`

`Threaded` 생성자가 `createInterface`를 호출하여 IPA 인터페이스 객체를 만들지 못하면, 해당 함수는 로그에 오류 메시지를 출력하고 즉시 반환합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:58`

`{{proxy_name}}Threaded` 클래스의 생성자에서 `ipa_` 객체의 이벤트를 처리하기 위해 `this` 를 수신 객체로, `&{{proxy_name}}Threaded::{{method.mojom_name}}Handler` 를 핸들러 메서드로 하여 `connect` 호출을 수행합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:69`

`{{proxy_name}}Isolated` 생성자는 `ipam->path()`와 worker 경로인 `proxyWorkerPath`를 사용하여 `std::make_unique<IPCPipeUnixSocket>`로 IPC 연결을 만듭니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130`

`{{proxy_name}}Isolated` 클래스의 생성자에서 `ipc->recv.connect(this, &{{proxy_name}}Isolated::recvMessage)` 호출이 수행됩니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:151`

`isolated-store` 함수의 `scope` 범위 내에서 실행되는 코드에서는 `ipc_` 멤버 변수에 `std::move(ipc)`를 대입합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:153`

`Isolated` 클래스의 생성자 함수가 실행될 때 `valid_` 멤버 변수에는 `true` 값이 대입됩니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:154`

`IPAProxy::resolvePath` 함수는 주어진 프록시 워커 실행 파일 이름에 대한 유효한 전체 경로를 찾습니다. `src/libcamera/ipa_proxy.cpp:204`

`IPCPipeUnixSocket::sendSync` 함수는 호출 시 `IPCMessage` 인자와 응답을 저장할 포인터를 받아, 내부적으로 `call` 함수를 호출하여 동기식 통신을 수행합니다. `src/libcamera/ipc_pipe_unixsocket.cpp:27`

`IPCPipeUnixSocket::sendAsync` 함수는 `socket_->send(data.payload())` 호출을 통해 소켓으로 데이터를 전송합니다. `src/libcamera/ipc_pipe_unixsocket.cpp:73`

근거 원문: [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) · [src/libcamera/ipa_proxy.cpp:204](#source-59a673fb7c43c0e0) · [src/libcamera/ipc_pipe_unixsocket.cpp:27](#source-f0268126d3f8c2bc) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:75](#source-542f7efc12af7917) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:93](#source-7670edf527118b0e) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:109](#source-f6afc431ed47a72a) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:82](#source-9d9c3049e90e4238) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:110](#source-b37be3b88abeaa94) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:55](#source-60c70cd011db2353) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:58](#source-7a0e7fe87df98a33) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:69](#source-927a8955b49d31d4) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:151](#source-c41c960fc2b2e4ff) · [src/libcamera/ipc_pipe_unixsocket.cpp:73](#source-6fafe97ae651cb83) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:153](#source-30b0ddcb59876f61) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:154](#source-4add57ac70567634)

## 프레임 입력과 결과 인터페이스

`IPAIPU3Interface` 와 `IPARkISP1Interface` 는 초기화, 시작, 중지 및 구성을 위한 동기 메서드를 제공합니다. init 은 설정 정보와 센서 정보를 받아 제어 정보를 반환하며, start 와 stop 은 각각 처리를 시작하거나 중지합니다. configure 는 IPU3 의 경우 단일 설정 정보를, RKISP1 의 경우 설정 정보와 스트림 구성 맵을 받아 제어 정보를 반환합니다. `include/libcamera/ipa/ipu3.mojom:19`

두 인터페이스 모두 버퍼 매핑과 해제를 위한 mapBuffers 와 unmapBuffers 메서드를 공유합니다. 이 메서드는 배열 형태의 버퍼를 매핑하거나 ID 를 기반으로 해제를 수행하며, 구체적인 구현 세부사항은 인터페이스 정의에 명시되어 있지 않습니다. `include/libcamera/ipa/ipu3.mojom:19`

[async] queueRequest 는 프레임 번호와 제어 목록을 받아 비동기적으로 요청을 큐에 넣습니다. 이 메서드는 즉시 처리가 완료된다는 보장을 제공하지 않으며, 실제 처리 순서와 타이밍은 구현에 따라 달라질 수 있습니다. `include/libcamera/ipa/ipu3.mojom:19`

[async] computeParams 는 프레임과 버퍼 ID 를 받아 파라미터를 계산합니다. 이 메서드는 비동기적으로 호출되며, 완료 시점이나 실패 여부는 반환 값이나 별도의 알림을 통해 확인해야 합니다. `include/libcamera/ipa/ipu3.mojom:19`

[async] processStats 는 프레임, 타임스탬프, 버퍼 ID 와 센서 제어 목록을 받아 통계를 처리합니다. 이 메서드는 비동기적으로 실행되며, 호출 시점과 완료 시점 사이의 관계는 명시적으로 보장되지 않습니다. `include/libcamera/ipa/ipu3.mojom:19`

IPAIPU3EventInterface 는 센서 제어 설정, 파라미터 계산 완료 및 메타데이터 준비를 위한 이벤트 인터페이스를 제공합니다. setSensorControls 는 프레임과 센서 및 렌즈 제어 목록을 받아 설정하고, paramsComputed 은 프레임 번호만 받아 파라미터가 계산되었음을 알립니다. `include/libcamera/ipa/ipu3.mojom:19`

IPARkISP1EventInterface 는 RKISP1 전용 이벤트 인터페이스로, paramsComputed 은 프레임과 사용된 바이트 수를 함께 반환합니다. setSensorControls 와 metadataReady 도 IPU3 와 유사하게 센서 제어 설정 및 메타데이터 준비 상태를 알립니다. `include/libcamera/ipa/rkisp1.mojom:17`

실행 확인 항목: EventInterface 의 메서드 호출 시점과 실제 이벤트 발생 시점은 일치하지 않을 수 있습니다. 인터페이스 정의는 실행 타이밍을 보장하지 않으며, 비동기 메서드는 완료 상태를 별도의 알림으로 확인해야 합니다. `include/libcamera/ipa/ipu3.mojom:19`

근거 원문: [include/libcamera/ipa/ipu3.mojom:19](#source-5a4a0da4800968a4) · [include/libcamera/ipa/rkisp1.mojom:17](#source-7a01de2477d6466e)

## IPA 객체와 종료 순서

`IPAModule::load()` 함수는 모듈을 로드하거나 이미 로드된 경우에만 성공하며, 유효하지 않은 모듈이나 이미 로드된 상태에서는 `false`를 반환합니다. `src/libcamera/ipa_module.cpp:390`

`IPAModule::createInterface()` 함수는 모듈이 로드되지 않았거나 유효하지 않은 경우 `nullptr`를 반환하며, 성공 시 인터페이스 인스턴스를 생성합니다. `src/libcamera/ipa_module.cpp:390`

`{{proxy_name}}Threaded` 프록시는 생성 시 `ipam->load()`와 `ipam->createInterface()`를 호출하여 인터페이스를 초기화하고, 실패 시 로그를 기록한 후 초기화를 중단합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48`

`{{proxy_name}}Threaded` 프록시는 `start()` 호출 시 스레드를 시작하고, `stop()` 호출 시 상태가 `ProxyRunning`이 아닌 경우 중단하며, `ProxyStopping` 상태로 전환 후 스레드 종료와 메시지 처리를 수행합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48`

`{{proxy_name}}Isolated` 프록시는 생성 시 IPC 파이프를 설정하고, 종료 시 `Exit` 명령을 통해 비동기 메시지를 전송하여 정리됩니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130`

`{{proxy_name}}Isolated` 프록시는 `configure()` 호출 시 `controlSerializer_`를 초기화하며, 비동기 호출 시 `_ipcInputBuf`를 전송하고 결과를 디시리얼라이즈하여 반환합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130`

근거 원문: [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:48](#source-c7fd6e52f2c537b5) · [utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl:25](#source-eb8f57d7452822da) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66)

## 생성과 IPC 실패

`createIPA` 함수는 모듈을 로드할 때 유효하지 않은 모듈이 반환되면 `nullptr`를 반환합니다. 또한 로딩된 후 프록시가 유효하지 않으면 에러 로그를 출력하고 `nullptr`를 반환합니다. `include/libcamera/internal/ipa_manager.h:35`

`IPAModule::load` 함수는 유효하지 않은 모듈이거나 이미 로드된 경우를 처리하여 `false`를 반환하며, 공유 객체를 열지 못하거나 심볼을 찾을 수 없으면 에러 로그를 출력하고 `dlHandle_`를 초기화한 뒤 `false`를 반환합니다. `src/libcamera/ipa_module.cpp:390`

`{{proxy_name}}Isolated` 생성자는 IPC 파이프를 만들지 못하거나 연결에 실패하면 에러 로그를 출력하고 초기화를 중단합니다. `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130`

`IPCPipeUnixSocket::sendSync` 함수는 호출이 실패하면 에러 로그를 출력하고 음수 반환 값을 반환하며, 타임아웃이 발생하면 `-ETIMEDOUT`을 반환합니다. `src/libcamera/ipc_pipe_unixsocket.cpp:27`

`IPCPipeUnixSocket::sendAsync` 함수는 소켓을 통해 메시지를 보낼 때 실패하면 에러 로그를 출력하고 음수 반환 값을 반환합니다. `src/libcamera/ipc_pipe_unixsocket.cpp:27`

`IPCPipeUnixSocket::readyRead` 함수는 수신된 데이터가 헤더 크기보다 작으면 에러 로그를 출력하고, 예상치 못한 데이터를 받으면 `recv` 신호를 방출합니다. `src/libcamera/ipc_pipe_unixsocket.cpp:27`

`IPCPipeUnixSocket::call` 함수는 타임아웃이 발생하면 `-ETIMEDOUT`을 반환하고, 호출 실패 시 음수 값을 반환하며, 성공하면 `0`을 반환합니다. `src/libcamera/ipc_pipe_unixsocket.cpp:27`

근거 원문: [include/libcamera/internal/ipa_manager.h:35](#source-2a1bbbc8623a516f) · [src/libcamera/ipa_module.cpp:390](#source-fadefbb962b2fc44) · [utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl:130](#source-9ff6047b0a70ce66) · [src/libcamera/ipc_pipe_unixsocket.cpp:27](#source-f0268126d3f8c2bc)

## 보정 전 튜닝 파일

RKISP1 또는 Mali-C55 파이프라인에서 센서를 초기화할 때, 해당 센서 모델 이름을 사용하여 `.yaml` 확장자를 가진 튜닝 파일을 찾습니다. 이 과정은 `ipa_->configurationFile()` 함수를 통해 수행되며, 첫 번째 인자로 센서 모델과 `.yaml`을, 두 번째 인자로 `uncalibrated.yaml`을 지정합니다. `src/libcamera/pipeline/rkisp1/rkisp1.cpp:406`, `src/libcamera/pipeline/mali-c55/mali-c55.cpp:468`

요청한 튜닝 파일이 존재하지 않으면, `IPAProxy::configurationFile()` 함수는 두 번째 인자로 전달된 `uncalibrated.yaml` 파일을 대체로 사용합니다. 이 함수는 먼저 주어진 이름으로 파일을 찾은 뒤, 없으면 fallback 이름으로 다시 검색합니다. `src/libcamera/ipa_proxy.cpp:174`

두 번째 검색에서도 파일을 찾지 못하면, 함수는 빈 문자열을 반환하고 에러 로그를 출력합니다. 이때 `fallbackName`이 비어있으면 추가적인 로깅 후 빈 문자열만 반환됩니다. `src/libcamera/ipa_proxy.cpp:174`

RKISP1의 `uncalibrated.yaml` 파일에는 `Agc`, `Awb`, `BlackLevelCorrection`, `Ccm`, `GammaOutCorrection` 등의 알고리즘이 정의되어 있습니다. 이 목록은 실제 활성화된 알고리즘을 보장하지 않으며, 누락된 항목이 반드시 비활성화된다는 의미는 아닙니다. `src/ipa/rkisp1/data/uncalibrated.yaml:1`

Mali-C55의 `uncalibrated.yaml` 파일에도 동일한 알고리즘 목록이 포함되어 있으며, 이는 RKISP1과 유사한 구조를 가집니다. 이 파일들도 센서별 튜닝 정보가 없을 때 대체로 사용됩니다. `src/ipa/mali-c55/data/uncalibrated.yaml:1`

근거 원문: [src/libcamera/pipeline/rkisp1/rkisp1.cpp:406](#source-a117437c7ec61db3) · [src/libcamera/pipeline/mali-c55/mali-c55.cpp:468](#source-efc0c3fc5cf7acef) · [src/libcamera/ipa_proxy.cpp:174](#source-4000376c954f5327) · [src/ipa/rkisp1/data/uncalibrated.yaml:1](#source-c3d57577d02a4dc3) · [src/ipa/mali-c55/data/uncalibrated.yaml:1](#source-9146c9052851a10f)

## 소프트웨어 ISP 입력 버퍼의 텍스처 형식

`createDMABufTexture2D()` 함수는 `eglImage.format_` 값을 확인하여 GL 형식에 따라 DRM 형식을 매핑합니다. `GL_RED` 또는 `GL_LUMINANCE`인 경우 `DRM_FORMAT_R8`, `GL_RG`인 경우 `DRM_FORMAT_GR88`, 그리고 `GL_RGBA`인 경우 `DRM_FORMAT_ARGB8888`를 각각 사용합니다. `src/libcamera/egl.cpp:174`

`createDMABufTexture2D()` 함수의 `switch` 문에서 기본(`default`) 분기가 실행되면, 처리되지 않은 GL 포맷에 대해 오류 로그가 출력됩니다. `src/libcamera/egl.cpp:174`

`createDMABufTexture2D()` 함수의 `switch` 문에서 기본(`default`) 분기가 실행되면, `-ENODEV`를 반환합니다. `src/libcamera/egl.cpp:174`

`createDMABufTexture2D()` 함수 내부에서 `eglCreateImageKHR()` 호출이 실패하여 `EGL_NO_IMAGE_KHR`를 반환하면, 디버깅 로그에 "eglCreateImageKHR fail"라는 메시지를 출력하고 `eglImage.dmabuf_import_failed_` 플래그를 `true`로 설정한 뒤 `-ENODEV`를 반환합니다. `src/libcamera/egl.cpp:174`

`createInputDMABufTexture2D()` 함수는 내부적으로 `createDMABufTexture2D()` 함수를 호출할 때 마지막 인자로 `false` 값을 전달합니다. `src/libcamera/egl.cpp:174`

`createOutputDMABufTexture2D()` 함수는 내부적으로 `createDMABufTexture2D()` 함수를 호출할 때 마지막 인자로 `true` 값을 전달합니다. `src/libcamera/egl.cpp:174`

`createDMABufTexture2D()` 함수는 `output` 매개변수가 참일 때만 프레임버퍼 객체 (FBO) 에 텍스처를 연결하는 작업을 수행합니다. `src/libcamera/egl.cpp:174`

`output` 가 참인 경우 `attachTextureToFBO(eglImage)` 함수를 호출하여 연결을 완료하고 그 반환값으로 `ret` 변수에 대입합니다. `src/libcamera/egl.cpp:174`

근거 원문: [src/libcamera/egl.cpp:174](#source-8cc12a6ba8b0dced)

## 소프트웨어 ISP 셰이더의 렌즈 음영 보정

두 셰이더 모두에서 블랙 레벨 보정은 가장 먼저 수행되며, `rgb = (rgb - blacklevel) / (1.0 - blacklevel)` 식으로 입력 색상을 센서 범위 내의 부동 소수점 값으로 변환합니다. `src/libcamera/shaders/bayer_1x_packed.frag:237`, `src/libcamera/shaders/bayer_unpacked.frag:140`

`APPLY_LSC` 조건이 정의된 경우 렌즈 음영 보정은 그 다음 단계에서 적용되며, `rgb = rgb * (texture2D(lsc_tex, textureOut).rgb * 4.0)` 또는 `rgb = rgb * (texture2D(lsc_tex, center.xy).rgb * 4.0)` 식으로 LSC 텍스처 값을 4 배로 곱해 부동 소수점 변환을 수행합니다. `src/libcamera/shaders/bayer_1x_packed.frag:237`

`unpacked-shader`에서는 렌즈 음영 보정을 적용할 때 `texture2D(lsc_tex, center.xy)`를 사용하여 텍스처의 중심 좌표만 참조합니다. `src/libcamera/shaders/bayer_unpacked.frag:140`

렌즈 음영 보정 이후에는 AWB 이득을 적용하고 각 채널을 센서 범위 `vec3(0.0)`에서 `vec3(1.0)`로 포화시키며, `rgb = clamp(rgb * awb, vec3(0.0), vec3(1.0))`를 통해 수행합니다. `src/libcamera/shaders/bayer_1x_packed.frag:237`

AWB 적용 후 색 보정 행렬 `ccm`을 곱하여 색상을 보정하고, `rgb = ccm * rgb`로 표현됩니다. `src/libcamera/shaders/bayer_1x_packed.frag:237`

색 보정 이후에는 대비를 적용하기 위해 각 채널을 `0.0`에서 `1.0`으로 포화시키고, `apply_contrast` 함수를 호출하여 대비를 조정합니다. `src/libcamera/shaders/bayer_1x_packed.frag:237`

마지막으로 감마 보정을 적용하여 `rgb = pow(rgb, vec3(gamma))`로 색상을 변환하고, `SWAP_BLUE` 조건에 따라 채널 순서를 변경하거나 그대로 출력합니다. `src/libcamera/shaders/bayer_1x_packed.frag:237`

실행 확인 항목: `softisp-interface`에서는 `IPASoftIspInterface` 인터페이스가 렌즈 음영 보정 버퍼를 전달하는 메커니즘을 정의하지만, 실제 GPU 실행 단계나 구체적인 적용 시점은 이 문서의 선언 범위에서 설명되지 않습니다. `include/libcamera/ipa/softisp.mojom:1`

근거 원문: [src/libcamera/shaders/bayer_1x_packed.frag:237](#source-68d470282c445049) · [src/libcamera/shaders/bayer_unpacked.frag:140](#source-86d4a7688119bd37) · [include/libcamera/ipa/softisp.mojom:1](#source-df8e8976167a0311)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 어떤 IPA 모듈과 실행 방식이 선택됩니까? | [모듈 탐색과 격리 조건](#모듈-탐색과-격리-조건) | 코드 근거와 설명 연결 |
    | 동기 호출과 비동기 호출은 어디에서 실행됩니까? | [스레드와 프로세스 경계](#스레드와-프로세스-경계) | 코드 근거와 설명 연결 |
    | 파이프라인과 알고리즘은 어떤 입력과 결과를 주고받습니까? | [프레임 입력과 결과 인터페이스](#프레임-입력과-결과-인터페이스) | 코드 근거와 설명 연결 · 실행 확인 항목 별도 |
    | 인터페이스를 만들고 비동기 처리를 끝내는 계약은 무엇입니까? | [IPA 객체와 종료 순서](#ipa-객체와-종료-순서) | 코드 근거와 설명 연결 |
    | 모듈 생성과 IPC 오류는 어떻게 관찰됩니까? | [생성과 IPC 실패](#생성과-ipc-실패) | 코드 근거와 설명 연결 |
    | 센서별 튜닝 파일이 없으면 어떤 파일과 알고리즘이 쓰입니까? | [보정 전 튜닝 파일](#보정-전-튜닝-파일) | 코드 근거와 설명 연결 |
    | 소프트웨어 ISP의 GPU 셰이더는 렌즈 음영 보정을 어느 단계에 적용합니까? | [소프트웨어 ISP 셰이더의 렌즈 음영 보정](#소프트웨어-isp-셰이더의-렌즈-음영-보정) | 코드 근거와 설명 연결 · 실행 확인 항목 별도 |
    | 소프트웨어 ISP의 입력 버퍼를 텍스처로 가져올 때 형식과 실패 처리는 어떻게 연결됩니까? | [소프트웨어 ISP 입력 버퍼의 텍스처 형식](#소프트웨어-isp-입력-버퍼의-텍스처-형식) | 코드 근거와 설명 연결 |

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

<a id="source-a117437c7ec61db3"></a>

??? note "소스 근거: src/libcamera/pipeline/rkisp1/rkisp1.cpp:406"
    `src/libcamera/pipeline/rkisp1/rkisp1.cpp:406`에서 시작하는 발췌입니다. 종료 줄은 408이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `5085c39368b264636b7bc7386979e019ea9cd60621335cc42d1e3ad28d810c6c`
    
    ```text
    /* The IPA tuning file is made from the sensor name. */
    	std::string ipaTuningFile =
    		ipa_->configurationFile(sensor_->model() + ".yaml", "uncalibrated.yaml");
    ```

<a id="source-efc0c3fc5cf7acef"></a>

??? note "소스 근거: src/libcamera/pipeline/mali-c55/mali-c55.cpp:468"
    `src/libcamera/pipeline/mali-c55/mali-c55.cpp:468`에서 시작하는 발췌입니다. 종료 줄은 469이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `226c3c21c4b760c25b2a3323369bce67c92f92db80b9fcef19589a44af6eaa2a`
    
    ```text
    std::string ipaTuningFile = ipa_->configurationFile(sensor()->model() + ".yaml",
    							    "uncalibrated.yaml");
    ```

<a id="source-4000376c954f5327"></a>

??? note "소스 근거: src/libcamera/ipa_proxy.cpp:174"
    `src/libcamera/ipa_proxy.cpp:174`에서 시작하는 발췌입니다. 종료 줄은 199이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `6c48d1f3994c22addbc1b338c87cf7b166f9fee0f9223ecf718a254be0aa93a8`
    
    ```text
    std::string IPAProxy::configurationFile(const std::string &name,
    					const std::string &fallbackName) const
    {
    	/*
    	 * The IPA module name can be used as-is to build directory names as it
    	 * has been validated when loading the module.
    	 */
    	const std::string ipaName = ipam_->info().name;
    	std::string confPath = ipaConfigurationFile(ipaName, name, configPaths_);
    	if (!confPath.empty()) {
    		LOG(IPAProxy, Info) << "Using tuning file " << confPath;
    		return confPath;
    	}
    
    	if (fallbackName.empty()) {
    		LOG(IPAProxy, Error)
    			<< "Configuration file '" << name
    			<< "' not found for IPA module '" << ipaName << "'";
    		return std::string();
    	}
    
    	confPath = ipaConfigurationFile(ipaName, fallbackName, configPaths_);
    	LOG(IPAProxy, Warning)
    		<< "Configuration file '" << name
    		<< "' not found for IPA module '" << ipaName
    		<< "', falling back to '" << confPath << "'";
    ```

<a id="source-c3d57577d02a4dc3"></a>

??? note "소스 근거: src/ipa/rkisp1/data/uncalibrated.yaml:1"
    `src/ipa/rkisp1/data/uncalibrated.yaml:1`에서 시작하는 발췌입니다. 종료 줄은 11이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `f3e8a3a6257b7fb82f16cf5c8239901d57bcc15023908c8994dcac3714e9e648`
    
    ```text
    # SPDX-License-Identifier: CC0-1.0
    %YAML 1.1
    ---
    version: 1
    algorithms:
      - Agc:
      - Awb:
      - BlackLevelCorrection:
      - Ccm:
      - GammaOutCorrection:
    ...
    ```

<a id="source-9146c9052851a10f"></a>

??? note "소스 근거: src/ipa/mali-c55/data/uncalibrated.yaml:1"
    `src/ipa/mali-c55/data/uncalibrated.yaml:1`에서 시작하는 발췌입니다. 종료 줄은 10이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `532d8234c4d0a6d5429c8a8f8df85d151b0701e965fb7372abc71fe70d2bed82`
    
    ```text
    # SPDX-License-Identifier: CC0-1.0
    %YAML 1.1
    ---
    version: 1
    algorithms:
      - Agc:
      - Awb:
      - BlackLevelCorrection:
      - Ccm:
    ...
    ```

<a id="source-8cc12a6ba8b0dced"></a>

??? note "소스 근거: src/libcamera/egl.cpp:174"
    `src/libcamera/egl.cpp:174`에서 시작하는 발췌입니다. 종료 줄은 279이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `54972e6c423848da387112f756eb3670a3ac895a05f7cc8d3e7bb77f5cb6a570`
    
    ```text
    int eGL::createDMABufTexture2D(eGLImage &eglImage, int fd, bool output)
    {
    	EGLint drm_format;
    	int ret = 0;
    
    	assertThread();
    
    	switch (eglImage.format_) {
    	case GL_RED:
    	case GL_LUMINANCE:
    		drm_format = DRM_FORMAT_R8;
    		break;
    	case GL_RG:
    		drm_format = DRM_FORMAT_GR88;
    		break;
    	case GL_RGBA:
    		drm_format = DRM_FORMAT_ARGB8888;
    		break;
    	default:
    		LOG(eGL, Error) << "unhandled GL format";
    		return -ENODEV;
    	}
    
    	// clang-format off
    	EGLint image_attrs[] = {
    		EGL_WIDTH, (EGLint)eglImage.width_,
    		EGL_HEIGHT, (EGLint)eglImage.height_,
    		EGL_LINUX_DRM_FOURCC_EXT, drm_format,
    		EGL_DMA_BUF_PLANE0_FD_EXT, fd,
    		EGL_DMA_BUF_PLANE0_OFFSET_EXT, 0,
    		EGL_DMA_BUF_PLANE0_PITCH_EXT, (EGLint)eglImage.stride_,
    		EGL_DMA_BUF_PLANE0_MODIFIER_LO_EXT, 0,
    		EGL_DMA_BUF_PLANE0_MODIFIER_HI_EXT, 0,
    		EGL_NONE,
    	};
    	// clang-format on
    
    	EGLImageKHR image = vtable_.eglCreateImageKHR(display_, EGL_NO_CONTEXT,
    						      EGL_LINUX_DMA_BUF_EXT,
    						      NULL, image_attrs);
    
    	if (image == EGL_NO_IMAGE_KHR) {
    		LOG(eGL, Debug) << "eglCreateImageKHR fail";
    		eglImage.dmabuf_import_failed_ = true;
    		return -ENODEV;
    	}
    
    	activateBindTexture(eglImage);
    
    	// Generate texture with filter semantics
    	vtable_.glEGLImageTargetTexture2DOES(GL_TEXTURE_2D, image);
    	vtable_.eglDestroyImageKHR(display_, image);
    
    	// Nearest filtering
    	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    
    	// Wrap to edge to avoid edge artifacts
    	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
    
    	if (output)
    		ret = attachTextureToFBO(eglImage);
    
    	return ret;
    }
    
    /**
     * \brief Create an input DMA-BUF backed texture
     * \param[in,out] eglImage EGL image to associate with the DMA-BUF
     * \param[in] fd DMA-BUF file descriptor
     *
     * Creates an EGL image from a DMA-BUF file descriptor and binds it to
     * a 2D texture for use as an input texture in shaders. The texture is
     * configured with nearest filtering and clamp-to-edge wrapping.
     *
     * \return 0 on success, or -ENODEV on failure
     */
    int eGL::createInputDMABufTexture2D(eGLImage &eglImage, int fd)
    {
    	assertThread();
    
    	return createDMABufTexture2D(eglImage, fd, false);
    }
    
    /**
     * \brief Create an output DMA-BUF backed texture
     * \param[in,out] eglImage EGL image to associate with the DMA-BUF
     * \param[in] fd DMA-BUF file descriptor
     *
     * Creates an EGL image from a DMA-BUF file descriptor and binds it to
     * a 2D texture, then attaches it to a framebuffer object for use as a
     * render target. This enables zero-copy rendering directly to the
     * DMA-BUF.
     *
     * \return 0 on success, or -ENODEV on failure
     */
    int eGL::createOutputDMABufTexture2D(eGLImage &eglImage, int fd)
    {
    	assertThread();
    
    	return createDMABufTexture2D(eglImage, fd, true);
    }
    
    /**
     * \brief Create a 2D texture from a memory buffer
    ```

<a id="source-68d470282c445049"></a>

??? note "소스 근거: src/libcamera/shaders/bayer_1x_packed.frag:237"
    `src/libcamera/shaders/bayer_1x_packed.frag:237`에서 시작하는 발췌입니다. 종료 줄은 270이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `84e5be2b8bbb1a1337af23df059b5d9270e16421c945a530a8c848709f302e6a`
    
    ```text
    rgb = (rgb - blacklevel) / (1.0 - blacklevel);
    
    #if defined(APPLY_LSC)
            /* Multiple by 4.0 for UQ<2, 6> -> float conversion:
             * texture2D(...) = original_float * 2^6 (quantization) * 1/2^8 (texture byte to float)
             * => original_float = texture2D(...) / 2^6 * 2^8 = texture2D(...) * 2^2
             */
            rgb = rgb * (texture2D(lsc_tex, textureOut).rgb * 4.0);
    #endif
    
    	/* Apply AWB gains, and saturate each channel at sensor range */
    	rgb = clamp(rgb * awb, vec3(0.0), vec3(1.0));
    
    	/* Colour Correction Matrix */
    	rgb = ccm * rgb;
    
    	/*
    	 * Contrast
    	 * contrastExp 0..2 contrast to 0..infinity; avoid actual infinity at tan(pi/2)
    	 */
    	rgb = clamp(rgb, 0.0, 1.0);
    	rgb.r = apply_contrast(rgb.r);
    	rgb.g = apply_contrast(rgb.g);
    	rgb.b = apply_contrast(rgb.b);
    
    	/* Apply gamma after colour correction */
    	rgb = pow(rgb, vec3(gamma));
    
    #if defined (SWAP_BLUE)
    	gl_FragColor = vec4(rgb.bgr, 1.0);
    #else
    	gl_FragColor = vec4(rgb, 1.0);
    #endif
    }
    ```

<a id="source-86d4a7688119bd37"></a>

??? note "소스 근거: src/libcamera/shaders/bayer_unpacked.frag:140"
    `src/libcamera/shaders/bayer_unpacked.frag:140`에서 시작하는 발췌입니다. 종료 줄은 169이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `5567b6548b078d7db847d9b57eefb1799e917214787288683110d5b41510573b`
    
    ```text
    rgb = (rgb - blacklevel) / (1.0 - blacklevel);
    
    #if defined(APPLY_LSC)
        /* Multiple by 4.0 for UQ<2, 6> -> float conversion */
        rgb = rgb * (texture2D(lsc_tex, center.xy).rgb * 4.0);
    #endif
    
        /* Apply AWB gains, and saturate each channel at sensor range */
        rgb = clamp(rgb * awb, vec3(0.0), vec3(1.0));
    
        /* Colour Correction Matrix */
        rgb = ccm * rgb;
    
        /*
         * Contrast
         */
        rgb = clamp(rgb, 0.0, 1.0);
        rgb.r = apply_contrast(rgb.r);
        rgb.g = apply_contrast(rgb.g);
        rgb.b = apply_contrast(rgb.b);
    
        /* Apply gamma after colour correction */
        rgb = pow(rgb, vec3(gamma));
    
    #if defined (SWAP_BLUE)
        gl_FragColor = vec4(rgb.bgr, 1.0);
    #else
        gl_FragColor = vec4(rgb, 1.0);
    #endif
    }
    ```

<a id="source-df8e8976167a0311"></a>

??? note "소스 근거: include/libcamera/ipa/softisp.mojom:1"
    `include/libcamera/ipa/softisp.mojom:1`에서 시작하는 발췌입니다. 종료 줄은 40이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `dedbfb928f4f1cdb8e174d8104cb8cbd575fd543e9b620240984c3af4cddecdb`
    
    ```text
    /* SPDX-License-Identifier: LGPL-2.1-or-later */
    
    /*
     * \todo Document the interface and remove the related EXCLUDE_PATTERNS entry.
     */
    
    module ipa.softisp;
    
    import "include/libcamera/ipa/core.mojom";
    
    struct IPAConfigInfo {
    	libcamera.ControlInfoMap sensorControls;
    };
    
    interface IPASoftIspInterface {
    	init(libcamera.IPASettings settings,
    	     libcamera.SharedFD fdStats,
    	     libcamera.SharedFD fdParams,
    	     libcamera.IPACameraSensorInfo sensorInfo,
    	     libcamera.ControlInfoMap sensorControls)
    		=> (int32 ret,
    		    libcamera.ControlInfoMap ipaControls,
    		    bool ccmEnabled, bool lscEnabled);
    	start() => (int32 ret);
    	stop();
    	configure(IPAConfigInfo configInfo)
    		=> (int32 ret, libcamera.ControlInfoMap ipaControls);
    
    	[async] queueRequest(uint32 frame, libcamera.ControlList sensorControls);
    	[async] computeParams(uint32 frame);
    	[async] processStats(uint32 frame,
    			     uint32 bufferId,
    			     libcamera.ControlList sensorControls);
    };
    
    interface IPASoftIspEventInterface {
    	setSensorControls(libcamera.ControlList sensorControls);
    	paramsComputed(uint32 frame);
    	metadataReady(uint32 frame, libcamera.ControlList metadata);
    };
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
  c6["ipa::ipu3::IPAIPU3Interface"]:::context
  c7["ipa::ipu3::Module"]:::context
  c8["ipa::rkisp1::IPARkISP1"]
  c9["ipa::rkisp1::IPARkISP1Interface"]:::context
  c10["ipa::rkisp1::Module"]:::context
  c1 -->|필드 참조| c2
  c2 -.->|상속| c4
  c3 -.->|상속| c0
  c3 -->|필드 참조| c2
  c5 -.->|상속| c6
  c5 -.->|상속| c7
  c8 -.->|상속| c9
  c8 -.->|상속| c10
  classDef context fill:#fafafa,stroke:#aaa,stroke-dasharray:4 3,color:#555
```
<!-- /sdd:class-diagram -->



## 관련 클래스

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::IPAManager` | `include/libcamera/internal/ipa_manager.h:29` | – | Manager for IPA modules |
| `libcamera::IPAModule` | `include/libcamera/internal/ipa_module.h:21` | `libcamera::Loggable` | Wrapper around IPA module shared object |
| `libcamera::IPAProxy` | `include/libcamera/internal/ipa_proxy.h:22` | `libcamera::IPAInterface` | IPA Proxy |
| `libcamera::ipa::ipu3::IPAIPU3` | `src/ipa/ipu3/ipu3.cpp:139` | `libcamera::ipa::ipu3::IPAIPU3Interface`, `libcamera::ipa::ipu3::Module` | The IPU3 IPA implementation |
| `libcamera::ipa::rkisp1::IPARkISP1` | `src/ipa/rkisp1/rkisp1.cpp:46` | `libcamera::ipa::rkisp1::IPARkISP1Interface`, `libcamera::ipa::rkisp1::Module` | 확인 필요 |

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `include/libcamera/internal/ipa_manager.h`, `include/libcamera/internal/ipa_module.h`, `include/libcamera/internal/ipa_proxy.h`, `include/libcamera/ipa/ipu3.mojom`, `include/libcamera/ipa/rkisp1.mojom`, `include/libcamera/ipa/softisp.mojom`, `src/ipa/ipu3/ipu3.cpp`, `src/ipa/mali-c55/data/uncalibrated.yaml`, `src/ipa/rkisp1/data/uncalibrated.yaml`, `src/ipa/rkisp1/rkisp1.cpp`, `src/libcamera/egl.cpp`, `src/libcamera/ipa_manager.cpp`, `src/libcamera/ipa_module.cpp`, `src/libcamera/ipa_proxy.cpp`, `src/libcamera/ipc_pipe_unixsocket.cpp`, `src/libcamera/pipeline/mali-c55/mali-c55.cpp`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp`, `src/libcamera/shaders/bayer_1x_packed.frag`, `src/libcamera/shaders/bayer_unpacked.frag`, `utils/codegen/ipc/generators/libcamera_templates/module_ipa_proxy.cpp.tmpl`, `utils/codegen/ipc/generators/libcamera_templates/proxy_functions.tmpl`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `2c4b67c079`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-27 · 사람 검토 전

다음 단계: [IPU3 LSC와 상태 연결](ipu3-lsc.md)
