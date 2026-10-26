---
generated_at: 2026-10-26T13:30:14+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: ipa-module-validation
generation_method: facts-and-llm
evidence_fingerprint: ee9673275e0bd838a4d1d9097cd779a993621b88c714b97f4822b5c6ab5af73d
semantic_review: human-review-required
agent: cli/hermes/qwen3.5:9b
generated_design: {"schema": 1, "input_fingerprint": "ee9673275e0bd838a4d1d9097cd779a993621b88c714b97f4822b5c6ab5af73d", "answers": {"signature": [{"text": "서명 파일이 열리지 않으면 loadIPAModuleInfo 가 0 을 반환합니다.", "covers": ["signature"], "kind": "behavior", "quote": "/* Load the signature. Failures are not fatal. */\n\tFile sign{ libPath_ + \".sign\" };\n\tif (!sign.open(File::OpenModeFlag::ReadOnly)) {\n\t\tLOG(IPAModule, Debug)\n\t\t\t<< \"IPA module \" << libPath_ << \" is not signed\";\n\t\treturn 0;\n\t}\n\n\tdata = sign.map(0, -1, File::MapFlag::Private);", "evidence": ["signature-file"], "part_id": "file-result"}], "metadata": [{"text": "ipaModuleInfo 크기 비교는 size()가 작으면 실패하고, moduleAPIVersion 비교는 다르면 실패하여 -EINVAL를 반환합니다.", "covers": ["metadata"], "kind": "behavior", "quote": "int IPAModule::loadIPAModuleInfo()\n{\n\tFile file{ libPath_ };\n\tif (!file.open(File::OpenModeFlag::ReadOnly)) {\n\t\tLOG(IPAModule, Error) << \"Failed to open IPA library: \"\n\t\t\t\t      << strerror(-file.error());\n\t\treturn file.error();\n\t}\n\n\tstd::span<const uint8_t> data = file.map();\n\tint ret = elfVerifyIdent(data);\n\tif (ret) {\n\t\tLOG(IPAModule, Error) << \"IPA module is not an ELF file\";\n\t\treturn ret;\n\t}\n\n\tstd::span<const uint8_t> info = elfLoadSymbol(data, \"ipaModuleInfo\");\n\tif (info.size() < sizeof(info_)) {\n\t\tLOG(IPAModule, Error) << \"IPA module has no valid info\";\n\t\treturn -EINVAL;\n\t}\n\n\tmemcpy(&info_, info.data(), sizeof(info_));\n\n\tif (info_.moduleAPIVersion != IPA_MODULE_API_VERSION) {\n\t\tLOG(IPAModule, Error) << \"IPA module API version mismatch\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * Validate the IPA module name.", "evidence": ["info-checks"], "part_id": "checks"}]}, "topic_inputs": {"metadata": "14ce8c54d5dcca8e6f7ead7cf31781492b339e66255210063670c3a0d3d28d00", "signature": "5cabdb641474bd4b2ac54e2b1d9f264ed117605ad772ef75c6c4bed0800fb806"}, "reused_topics": ["signature"], "generated_topics": ["metadata"], "topic_agents": {"signature": "cli/hermes/qwen3.5:9b", "metadata": "cli/hermes/qwen3.5:9b"}, "body_sha256": "77db254e07d6a828fc2a05d0b0c7701da19013cf3b2d080328fd3a20cb04c5cd"}
---

# IPA 모듈 정보 검사와 서명 파일 누락

**IPA 모듈 정보가 잘못된 경우와 서명 파일만 없는 경우를 구분하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 메타데이터 오류를 구분하기 절을 확인합니다. | [메타데이터 오류를 구분하기](#메타데이터-오류를-구분하기) |
| 서명 파일을 열지 못한 경우 절을 확인합니다. | [서명 파일을 열지 못한 경우](#서명-파일을-열지-못한-경우) |

## 메타데이터 오류를 구분하기

ipaModuleInfo 크기 비교는 size()가 작으면 실패하고, moduleAPIVersion 비교는 다르면 실패하여 -EINVAL를 반환합니다. `src/libcamera/ipa_module.cpp:268`

근거 원문: [src/libcamera/ipa_module.cpp:268](#source-c87048bf1f3594a3)

## 서명 파일을 열지 못한 경우

서명 파일이 열리지 않으면 loadIPAModuleInfo 가 0 을 반환합니다. `src/libcamera/ipa_module.cpp:316`

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
    - 검토 상태 기록일: 2026-10-26 · 사람 검토 전

다음 단계: [IPA 관리와 구현 진입점](ipa.md)
