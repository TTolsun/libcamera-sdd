<!-- system -->
제공된 소스만 사용하여 한국어 기술 문서를 작성합니다. 질문의 각 조건에 답하세요. 원문에 없는 보장이나 이유를 추가하지 마세요. 의무(must/shall), 가능성(may), 부정을 그대로 유지하세요.

<!-- user -->
근거:
{"info-checks": [{"text": "int IPAModule::loadIPAModuleInfo()\n{\n\tFile file{ libPath_ };\n\tif (!file.open(File::OpenModeFlag::ReadOnly)) {\n\t\tLOG(IPAModule, Error) << \"Failed to open IPA library: \"\n\t\t\t\t      << strerror(-file.error());\n\t\treturn file.error();\n\t}\n\n\tstd::span<const uint8_t> data = file.map();\n\tint ret = elfVerifyIdent(data);\n\tif (ret) {\n\t\tLOG(IPAModule, Error) << \"IPA module is not an ELF file\";\n\t\treturn ret;\n\t}\n\n\tstd::span<const uint8_t> info = elfLoadSymbol(data, \"ipaModuleInfo\");\n\tif (info.size() < sizeof(info_)) {\n\t\tLOG(IPAModule, Error) << \"IPA module has no valid info\";\n\t\treturn -EINVAL;\n\t}\n\n\tmemcpy(&info_, info.data(), sizeof(info_));\n\n\tif (info_.moduleAPIVersion != IPA_MODULE_API_VERSION) {\n\t\tLOG(IPAModule, Error) << \"IPA module API version mismatch\";\n\t\treturn -EINVAL;\n\t}\n\n\t/*\n\t * Validate the IPA module name.", "quote_id": "info-checks:0"}]}
질문: IPAModule::loadIPAModuleInfo는 ipaModuleInfo의 크기가 sizeof(info_)보다 작거나 moduleAPIVersion이 IPA_MODULE_API_VERSION과 다르면 어떤 int 오류 코드를 반환합니까? 두 실패 조건과 반환값을 함께 한 문장으로 설명하세요. 반환 타입이나 템플릿을 추정하지 마세요.
작성 조건: [종결어미] 1행 "ipaModuleInfo의 크기가 sizeof(info_)보다 작을 경우 -EINVAL, moduleAPI…": 모든 문장은 "~합니다", "~입니다" 로 끝냅니다. "~한다", "~이다", "~함", "~없음" 같은 형태로 끝내지 않습니다.
질문의 모든 조건을 근거에서 다시 확인하세요.
출력: {"statements": [{"text": "질문의 모든 조건에 답하는 한 문단. 여러 문장을 써도 됩니다.", "quote_id": "직접 근거의 구절 ID", "covers": ["metadata"], "kind": "behavior"}]} 형식의 JSON만 반환하세요.
