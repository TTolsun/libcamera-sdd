---
generated_at: 2026-10-27T12:55:27+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: ipa-module-validation
generation_method: facts-and-llm
evidence_fingerprint: ee9673275e0bd838a4d1d9097cd779a993621b88c714b97f4822b5c6ab5af73d
semantic_review: human-review-required
agent: cli/claude/claude-haiku-5-5
generated_design: {"schema": 1, "input_fingerprint": "ee9673275e0bd838a4d1d9097cd779a993621b88c714b97f4822b5c6ab5af73d", "answers": {"metadata": [{"text": "`IPAModule::loadIPAModuleInfo`에서 ipaModuleInfo의 크기(info.size())가 sizeof(`info_`)보다 작으면 유효한 정보가 없는 것으로 보고 -EINVAL을 반환하고, `info_`.moduleAPIVersion이 `IPA_MODULE_API_VERSION`과 같지 않으면 API 버전 불일치로 보고 -EINVAL을 반환합니다.", "evidence": ["info-checks"], "covers": ["metadata"], "kind": "behavior", "quote": "int IPAModule::loadIPAModuleInfo()\n{\n\tFile file{ libPath_ };\n\tif (!file.open(File::OpenModeFlag::ReadOnly)) {\n\t\tLOG(IPAModule, Error) << \"Failed to open IPA library: \"\n\t\t\t\t      << strerror(-file.error());\n\t\treturn file.error();\n\t}\n\n\tstd::span<const uint8_t> data = file.map();\n\tint ret = elfVerifyIdent(data);\n\tif (ret) {\n\t\tLOG(IPAModule, Error) << \"IPA module is not an ELF file\";\n\t\treturn ret;\n\t}\n\n\tstd::span<const uint8_t> info = elfLoadSymbol(data, \"ipaModuleInfo\");\n\tif (info.size() < sizeof(info_)) {\n\t\tLOG(IPAModule, Error) << \"IPA module has no valid info\";\n\t\treturn -EINVAL;\n\t}\n\n\tmemcpy(&info_, info.data(), sizeof(info_));\n\n\tif (info_.moduleAPIVersion != IPA_MODULE_API_VERSION) {\n\t\tLOG(IPAModule, Error) << \"IPA module API version mismatch\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * Validate the IPA module name.", "part_id": "checks"}], "signature": [{"text": "발췌문에는 `loadIPAModuleInfo`의 이름과 반환 타입이 없으므로, 서명 파일 열기에 실패하면 발췌된 코드가 `LOG(IPAModule, Debug)`로 'is not signed' 로그를 남긴 뒤 `return 0;`을 실행해 정수 `0`을 반환한다는 것까지만 근거로 확인됩니다.", "evidence": ["signature-file"], "covers": ["signature"], "kind": "behavior", "quote": "/* Load the signature. Failures are not fatal. */\n\tFile sign{ libPath_ + \".sign\" };\n\tif (!sign.open(File::OpenModeFlag::ReadOnly)) {\n\t\tLOG(IPAModule, Debug)\n\t\t\t<< \"IPA module \" << libPath_ << \" is not signed\";\n\t\treturn 0;\n\t}\n\n\tdata = sign.map(0, -1, File::MapFlag::Private);", "part_id": "file-result"}]}, "topic_inputs": {"metadata": "db011cd0c5bc4c4dacdf253faf5e7c64c1b2c520dd2481aea4e94540334087ba", "signature": "399a2b1877f00f8262d178ac3c5ea6efeb90bc4525d50adb92d3355d6c701d3e"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["metadata", "signature"], "topic_agents": {"metadata": "cli/claude/claude-haiku-5-5", "signature": "cli/claude/claude-haiku-5-5"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "body_sha256": "895d864e588433ce875ab4921eec86b13edd1bb606654771ce593af46bcc2c35"}
---

# IPA 모듈 정보 검사와 서명 파일 누락

**IPA 모듈 정보가 잘못된 경우와 서명 파일만 없는 경우를 구분하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 메타데이터 오류를 구분하기 절을 확인합니다. | [메타데이터 오류를 구분하기](#메타데이터-오류를-구분하기) |
| 서명 파일을 열지 못한 경우 절을 확인합니다. | [서명 파일을 열지 못한 경우](#서명-파일을-열지-못한-경우) |

## 메타데이터 오류를 구분하기

`IPAModule::loadIPAModuleInfo`에서 ipaModuleInfo의 크기(info.size())가 sizeof(`info_`)보다 작으면 유효한 정보가 없는 것으로 보고 -EINVAL을 반환하고, `info_`.moduleAPIVersion이 `IPA_MODULE_API_VERSION`과 같지 않으면 API 버전 불일치로 보고 -EINVAL을 반환합니다. `src/libcamera/ipa_module.cpp:268`

근거 원문: [src/libcamera/ipa_module.cpp:268](#source-c87048bf1f3594a3)

## 서명 파일을 열지 못한 경우

발췌문에는 `loadIPAModuleInfo`의 이름과 반환 타입이 없으므로, 서명 파일 열기에 실패하면 발췌된 코드가 `LOG(IPAModule, Debug)`로 'is not signed' 로그를 남긴 뒤 `return 0;`을 실행해 정수 `0`을 반환한다는 것까지만 근거로 확인됩니다. `src/libcamera/ipa_module.cpp:316`

근거 원문: [src/libcamera/ipa_module.cpp:316](#source-c7597f31f03901e3)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 모듈 정보 크기와 API 버전 검사에 실패하면 어떻게 반환합니까? | [메타데이터 오류를 구분하기](#메타데이터-오류를-구분하기) | 코드 근거와 설명 연결 |
    | 서명 파일을 열지 못하면 loadIPAModuleInfo는 어떤 값을 반환합니까? | [서명 파일을 열지 못한 경우](#서명-파일을-열지-못한-경우) | 코드 근거와 설명 연결 |

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

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `src/libcamera/ipa_module.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `2c4b67c079`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-27 · 사람 검토 전

다음 단계: [IPA 관리와 구현 진입점](ipa.md)
