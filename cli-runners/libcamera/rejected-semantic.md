---
generated_at: 2026-10-26T13:20:18+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: ipa-module-validation
generation_method: facts-and-llm
evidence_fingerprint: 0bfa5f4ca6f595999a955606e05236223851e3155567b6b3c8d6ef647f5f46cc
semantic_review: human-review-required
agent: cli/hermes/qwen3.5:9b
generated_design: {"schema": 1, "input_fingerprint": "0bfa5f4ca6f595999a955606e05236223851e3155567b6b3c8d6ef647f5f46cc", "answers": {"metadata": [{"text": "ipaModuleInfo의 크기가 sizeof(info_)보다 작을 경우 -EINVAL, moduleAPIVersion이 IPA_MODULE_API_VERSION과 다르면 -EINVAL를 반환합니다", "covers": ["metadata"], "kind": "behavior", "quote": "int IPAModule::loadIPAModuleInfo()\n{\n\tFile file{ libPath_ };\n\tif (!file.open(File::OpenModeFlag::ReadOnly)) {\n\t\tLOG(IPAModule, Error) << \"Failed to open IPA library: \"\n\t\t\t\t      << strerror(-file.error());\n\t\treturn file.error();\n\t}\n\n\tstd::span<const uint8_t> data = file.map();\n\tint ret = elfVerifyIdent(data);\n\tif (ret) {\n\t\tLOG(IPAModule, Error) << \"IPA module is not an ELF file\";\n\t\treturn ret;\n\t}\n\n\tstd::span<const uint8_t> info = elfLoadSymbol(data, \"ipaModuleInfo\");\n\tif (info.size() < sizeof(info_)) {\n\t\tLOG(IPAModule, Error) << \"IPA module has no valid info\";\n\t\treturn -EINVAL;\n\t}\n\n\tmemcpy(&info_, info.data(), sizeof(info_));\n\n\tif (info_.moduleAPIVersion != IPA_MODULE_API_VERSION) {\n\t\tLOG(IPAModule, Error) << \"IPA module API version mismatch\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * Validate the IPA module name.", "evidence": ["info-checks"], "part_id": "checks"}], "signature": [{"text": "서명 파일打开 실패 시 loadIPAModuleInfo()는 0을 반환하고, 생성자의 valid_ 플래그는 여전히 false로 설정되지 않은 상태입니다.", "covers": ["signature"], "kind": "behavior", "quote": "IPAModule::IPAModule(const std::string &libPath)\n\t: libPath_(libPath), valid_(false), loaded_(false),\n\t  dlHandle_(nullptr), ipaCreate_(nullptr)\n{\n\tif (loadIPAModuleInfo() < 0)\n\t\treturn;\n\n\tvalid_ = true;\n}\n\nIPAModule::~IPAModule()", "evidence": ["constructor"]}]}, "topic_inputs": {"metadata": "a4e7d252be3a9e7e7886d826eaa6887a6afa4f74fad34563e6f6ace620d8a4e5", "signature": "7c9c517ee50e50f3314dfec6d6e81ce338a237d4005d463aee4eed5c0e8fdcd9"}, "reused_topics": [], "generated_topics": ["metadata", "signature"], "topic_agents": {"metadata": "cli/hermes/qwen3.5:9b", "signature": "cli/hermes/qwen3.5:9b"}, "body_sha256": "2dcc1583f5153c1bec7b8c89ed186f44f91c68b3de5162b6feeb917f143954c0"}
---

# IPA 모듈 정보 검사와 서명 파일 누락

**IPA 모듈 정보가 잘못된 경우와 서명 파일만 없는 경우를 구분하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 메타데이터 오류를 구분하기 절을 확인합니다. | [메타데이터 오류를 구분하기](#메타데이터-오류를-구분하기) |
| 서명 파일 누락과 유효성 판정 절을 확인합니다. | [서명 파일 누락과 유효성 판정](#서명-파일-누락과-유효성-판정) |

## 메타데이터 오류를 구분하기

ipaModuleInfo의 크기가 sizeof(info_)보다 작을 경우 -EINVAL, moduleAPIVersion이 IPA_MODULE_API_VERSION과 다르면 -EINVAL를 반환합니다 `src/libcamera/ipa_module.cpp:268`

근거 원문: [src/libcamera/ipa_module.cpp:268](#source-c87048bf1f3594a3)

## 서명 파일 누락과 유효성 판정

서명 파일打开 실패 시 loadIPAModuleInfo()는 0을 반환하고, 생성자의 valid_ 플래그는 여전히 false로 설정되지 않은 상태입니다. `src/libcamera/ipa_module.cpp:252`

근거 원문: [src/libcamera/ipa_module.cpp:316](#source-c7597f31f03901e3) · [src/libcamera/ipa_module.cpp:252](#source-d3245717ff316f92)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 모듈 정보 크기와 API 버전 검사에 실패하면 어떻게 반환합니까? | [메타데이터 오류를 구분하기](#메타데이터-오류를-구분하기) | 코드 근거와 설명 연결 |
    | 서명 파일을 열지 못하면 어떤 값을 반환하며 이 값은 생성자의 valid_ 설정에 어떤 영향을 줍니까? | [서명 파일 누락과 유효성 판정](#서명-파일-누락과-유효성-판정) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-c87048bf1f3594a3"></a>

??? note "소스 근거: src/libcamera/ipa_module.cpp:268"
    `src/libcamera/ipa_module.cpp:268`에서 시작하는 발췌입니다. 종료 줄은 298이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `561e1321cc43c1bd56b25929c7934942beae3b0dfb6dd720780a7c0b1d777ca1`
    
    ```text
    int IPAModule::loadIPAModuleInfo()
    {
    	File file{ libPath_ };
    	if (!file.open(File::OpenModeFlag::ReadOnly)) {
    		LOG(IPAModule, Error) << "Failed to open IPA library: "
    				      << strerror(-file.error());
    		return file.error();
    	}
    
    	std::span<const uint8_t> data = file.map();
    	int ret = elfVerifyIdent(data);
    	if (ret) {
    		LOG(IPAModule, Error) << "IPA module is not an ELF file";
    		return ret;
    	}
    
    	std::span<const uint8_t> info = elfLoadSymbol(data, "ipaModuleInfo");
    	if (info.size() < sizeof(info_)) {
    		LOG(IPAModule, Error) << "IPA module has no valid info";
    		return -EINVAL;
    	}
    
    	memcpy(&info_, info.data(), sizeof(info_));
    
    	if (info_.moduleAPIVersion != IPA_MODULE_API_VERSION) {
    		LOG(IPAModule, Error) << "IPA module API version mismatch";
    		return -EINVAL;
    	}
    
    	/*
    	 * Validate the IPA module name.
    ```

<a id="source-c7597f31f03901e3"></a>

??? note "소스 근거: src/libcamera/ipa_module.cpp:316"
    `src/libcamera/ipa_module.cpp:316`에서 시작하는 발췌입니다. 종료 줄은 324이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `c0494d982bf733894dac25a5c0221b855cddc703b1ba2094bdddac72c0329caa`
    
    ```text
    /* Load the signature. Failures are not fatal. */
    	File sign{ libPath_ + ".sign" };
    	if (!sign.open(File::OpenModeFlag::ReadOnly)) {
    		LOG(IPAModule, Debug)
    			<< "IPA module " << libPath_ << " is not signed";
    		return 0;
    	}
    
    	data = sign.map(0, -1, File::MapFlag::Private);
    ```

<a id="source-d3245717ff316f92"></a>

??? note "소스 근거: src/libcamera/ipa_module.cpp:252"
    `src/libcamera/ipa_module.cpp:252`에서 시작하는 발췌입니다. 종료 줄은 262이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `09a21eb423f761e05b1a05d4254eddaea262b3cdf628770d0213b24d30ee0e3d`
    
    ```text
    IPAModule::IPAModule(const std::string &libPath)
    	: libPath_(libPath), valid_(false), loaded_(false),
    	  dlHandle_(nullptr), ipaCreate_(nullptr)
    {
    	if (loadIPAModuleInfo() < 0)
    		return;
    
    	valid_ = true;
    }
    
    IPAModule::~IPAModule()
    ```

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `src/libcamera/ipa_module.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `2c4b67c079`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-26 · 사람 검토 전

다음 단계: [IPA 관리와 구현 진입점](ipa.md)
