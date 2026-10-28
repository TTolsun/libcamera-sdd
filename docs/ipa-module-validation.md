---
generated_at: 2026-10-28T23:09:53+00:00
source_commit: e117198c015057761bb0bbaa85f963c41ce412d7
status: ok
section: ipa-module-validation
generation_method: facts-and-llm
evidence_fingerprint: 42775965b4712134309d35fc05e9d660a1f099232013cfe06deedbd5e0864045
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "42775965b4712134309d35fc05e9d660a1f099232013cfe06deedbd5e0864045", "answers": {"metadata": [{"text": "ipaModuleInfo의 크기가 sizeof(`info_`)보다 작으면 또는 moduleAPIVersion이 `IPA_MODULE_API_VERSION`과 일치하지 않으면 -EINVAL을 반환합니다.", "evidence": ["info-checks"], "covers": ["metadata"], "kind": "behavior", "quote": "int IPAModule::loadIPAModuleInfo()\n{\n\tFile file{ libPath_ };\n\tif (!file.open(File::OpenModeFlag::ReadOnly)) {\n\t\tLOG(IPAModule, Error) << \"Failed to open IPA library: \"\n\t\t\t\t      << strerror(-file.error());\n\t\treturn file.error();\n\t}\n\n\tstd::span<const uint8_t> data = file.map();\n\tint ret = elfVerifyIdent(data);\n\tif (ret) {\n\t\tLOG(IPAModule, Error) << \"IPA module is not an ELF file\";\n\t\treturn ret;\n\t}\n\n\tstd::span<const uint8_t> info = elfLoadSymbol(data, \"ipaModuleInfo\");\n\tif (info.size() < sizeof(info_)) {\n\t\tLOG(IPAModule, Error) << \"IPA module has no valid info\";\n\t\treturn -EINVAL;\n\t}\n\n\tmemcpy(&info_, info.data(), sizeof(info_));\n\n\tif (info_.moduleAPIVersion != IPA_MODULE_API_VERSION) {\n\t\tLOG(IPAModule, Error) << \"IPA module API version mismatch\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * Validate the IPA module name.", "part_id": "checks"}], "signature": [{"text": "서명 파일을 열지 못하면 `loadIPAModuleInfo`는 정수 0을 반환합니다.", "evidence": ["signature-file"], "covers": ["signature"], "kind": "behavior", "quote": "/* Load the signature. Failures are not fatal. */\n\tFile sign{ libPath_ + \".sign\" };\n\tif (!sign.open(File::OpenModeFlag::ReadOnly)) {\n\t\tLOG(IPAModule, Debug)\n\t\t\t<< \"IPA module \" << libPath_ << \" is not signed\";\n\t\treturn 0;\n\t}\n\n\tdata = sign.map(0, -1, File::MapFlag::Private);", "part_id": "file-result"}]}, "topic_inputs": {"metadata": "5eccc9296eb5b459571275ea01beee7ff65d0da0bbe04662d02dfa9d3862c676", "signature": "0fea9fb5f17cc8c74bd59a3d848c11eea92c3c0c7ead3e5d0342adfd82fb7766"}, "reused_topics": ["metadata", "signature"], "replayed_units": [], "generated_topics": [], "topic_agents": {"metadata": "cli/codex/gpt-6.1-terra", "signature": "cli/codex/gpt-6.1-terra"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "e0c429a5c80a01c34563ce00a616df89d8f75c735f8669bcbd1f75d84cce82a6", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "d4af3d834d8b1c99a6c9311612712a64112c30fa4621b375904d172f361285b8", "design_contracts": "b293a0012d1fcb6340fcaf94d481cf900212686978bc96fb118a0cdaddf3c091", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "65c405dc11cd8c43e2bce26ffbd96a47f37a784df59a4969be589ed8318f7be0", "answer_contracts": "1e0d24e0cf26ded53ecec2e5a6fbc51836bac6e17530318a9fa7cffaa936c00b", "design_response": "ce93f02b72371ed40f1b1124e78cef512baea31aa2df988db0c689f8169f783c", "design_validation": "608d2eed51e4ad5d5693fbc9b7d669ae1ba8e503f6736b62ea1ca068ce706556"}, "validation_model": "5ddbcbf91a6b516c4f71596d64b6286295bfd0cac771a7ca749ca78e25a2d752", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "f8fd5a3d8041c23fc68b93ff32b8727e98393383b5099032eb00ad0013e7611c"}, "reuse_lineage": {"source_commit": "e117198c015057761bb0bbaa85f963c41ce412d7", "body_sha256": "5fc274251a6f8dd040bb76d2eb1840fc2eaa5e4a99f01d6d5706e2527f170e98", "topics": ["metadata", "signature"], "validation": "current source, contract and editorial checks; human review pending"}, "body_sha256": "5fc274251a6f8dd040bb76d2eb1840fc2eaa5e4a99f01d6d5706e2527f170e98"}
---

# IPA 모듈 정보 검사와 서명 파일 누락

**IPA 모듈 정보가 잘못된 경우와 서명 파일만 없는 경우를 구분하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 메타데이터 오류를 구분하기 절을 확인합니다. | [메타데이터 오류를 구분하기](#메타데이터-오류를-구분하기) |
| 서명 파일을 열지 못한 경우 절을 확인합니다. | [서명 파일을 열지 못한 경우](#서명-파일을-열지-못한-경우) |

## 메타데이터 오류를 구분하기

ipaModuleInfo의 크기가 sizeof(`info_`)보다 작으면 또는 moduleAPIVersion이 `IPA_MODULE_API_VERSION`과 일치하지 않으면 -EINVAL을 반환합니다. `src/libcamera/ipa_module.cpp:268`

근거 원문: [src/libcamera/ipa_module.cpp:268](#source-c87048bf1f3594a3)

## 서명 파일을 열지 못한 경우

서명 파일을 열지 못하면 `loadIPAModuleInfo`는 정수 0을 반환합니다. `src/libcamera/ipa_module.cpp:316`

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
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `e117198c01`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-29 · 사람 검토 전

다음 단계: [IPA 관리와 구현 진입점](ipa.md)
