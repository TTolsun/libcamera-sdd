---
generated_at: 2026-11-12T18:09:45+00:00
source_commit: da6a6ed33ed0ab305f10b6f8b44736150d39cef4
status: ok
section: colour-temperature
generation_method: facts-and-llm
evidence_fingerprint: 0043ede032d493861c1a137eb865aba99681446e4ffdc1a607a9fb930c5dc90b
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "0043ede032d493861c1a137eb865aba99681446e4ffdc1a607a9fb930c5dc90b", "answers": {"temperature": [{"text": "`ColourTemperature`은 `inout` 제어값으로 프레임의 색온도를 켈빈 단위로 나타내며, 요청에는 AWB가 비활성화된 경우에만 적용할 수 있습니다. 프레임 처리에 사용한 `ColourTemperature`은 메타데이터에 보고됩니다. 요청에 `ColourTemperature`을 설정하고 `ColourGains`를 설정하지 않으면 구현체는 지정된 색온도를 바탕으로 `ColourGains`를 계산하고 설정해야 합니다. `ColourTemperature`이 직접 설정되거나 `ColourGains` 설정을 통해 간접적으로 설정되고 `ColourCorrectionMatrix`가 설정되지 않으면, `ColourCorrectionMatrix`는 `ColourTemperature`을 바탕으로 갱신됩니다.", "evidence": ["contract"], "covers": ["temperature"], "kind": "behavior", "quote": "If ColourTemperature is set in a request but ColourGains is not, the\n        implementation shall calculate and set the ColourGains based on the\n        given ColourTemperature. If ColourTemperature is set (either directly,\n        or indirectly by setting ColourGains) but ColourCorrectionMatrix is not,\n        the ColourCorrectionMatrix is updated based on the ColourTemperature."}, {"text": "Raspberry Pi IPA의 요청 처리 코드는 `ColourTemperature`이 있으면 모노 센서에서 해당 제어값을 조용히 무시합니다. AWB 알고리즘을 찾지 못하면 경고를 기록하고 해당 처리를 끝냅니다. 그 외에는 AWB 알고리즘의 `setColourTemperature()`를 호출한 뒤 `awbEnabled_`를 `false`로 설정하여 AWB를 수동 모드로 전환합니다. 메타데이터 처리 코드는 `awb.status`가 있으면 그 상태의 `temperatureK`를 `ColourTemperature` 메타데이터로 설정합니다.", "evidence": ["rpi-request", "rpi-metadata"], "covers": ["temperature"], "kind": "behavior", "quote": "const auto colourTemperature = controls.get(controls::ColourTemperature);\n\tif (colourTemperature)\n\t\tdo {\n\t\t\t/* Silently ignore this control for a mono sensor. */\n\t\t\tif (monoSensor_)\n\t\t\t\tbreak;"}]}, "topic_inputs": {"temperature": "039b971e752649f862f0b0ea673546bade7c64f7c950475ed080229f0c443e86"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["temperature"], "topic_agents": {"temperature": "cli/codex/gpt-6.1-terra"}, "grounding_review": "not-run", "grounding_policy": null, "validation_policy": {"manuscript": "367d18b95f8f0d01a15ae0f4d1b70f7e13e4d0298df4215e2c449ac4905db6f9", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "d0f7ab4c48fcf52409935931eb9b93aacd48af4b19e9bb816fa496f1214fdb2f", "answer_contracts": "a39c9a8818afc47e059141d486337c0f12a7fd34319e2b6f7674fc428bc83e2b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "050c20aa2fdcceae10c6275fbb5f850f616ab5051bb67ccbcb4a204877a238d9", "explanation": "69bcaa207ef39d20f6a47ac201c3edf119f59b333e85131dea1bce85eef4006b", "design_response": "a7c199bc52bcc0e749ef01186e50bca98107473d5c82e2248712f465d02e1e69", "design_validation": "a4edf8364d73d169c3f10ecbadf487a8a4dc10328622d07578b281eae810c3aa"}, "validation_model": "6b7aae9af4e7134c45a7e4de99b4506b5f11d903223aeedf15dcfc1564877a5e", "style_policy": {"README.md": "b87a84b1bc31079837dc4dc4527ce02c9dc2cbc3a26ff7e99e0872941d213995", "fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9"}, "body_sha256": "6ca948a88d60be4ed8849450a1d8d0b55f7506dd5cdbe27e4875c887b5e365d5"}
---

# 색온도 요청과 메타데이터를 구분하기

**색온도 값을 요청에 넣는 조건과 실제 프레임의 메타데이터가 나타내는 값을 확인하세요.**



## ColourTemperature 요청과 결과

`ColourTemperature`은 `inout` 제어값으로 프레임의 색온도를 켈빈 단위로 나타내며, 요청에는 AWB가 비활성화된 경우에만 적용할 수 있습니다. 프레임 처리에 사용한 `ColourTemperature`은 메타데이터에 보고됩니다. 요청에 `ColourTemperature`을 설정하고 `ColourGains`를 설정하지 않으면 구현체는 지정된 색온도를 바탕으로 `ColourGains`를 계산하고 설정해야 합니다. `ColourTemperature`이 직접 설정되거나 `ColourGains` 설정을 통해 간접적으로 설정되고 `ColourCorrectionMatrix`가 설정되지 않으면, `ColourCorrectionMatrix`는 `ColourTemperature`을 바탕으로 갱신됩니다. `src/libcamera/control_ids_core.yaml:603`

<!-- sdd:visual:rpi-awb-branches -->
### Raspberry Pi의 색온도 요청 분기

```mermaid
flowchart TB
%% sdd:translations {"값을 무시함": "Value ignored", "경고를 기록하고 적용을 <br/>건너뜀": "Warning logged and <br/>application skipped", "모노 센서": "Monochrome sensor", "색온도를 전달하고 AWB를 <br/>수동으로 전환": "Set temperature and switch <br/>AWB to manual", "요청에 ColourTemperature가 <br/>있음": "Request contains <br/>ColourTemperature", "컬러 센서에 AWB 알고리즘이 <br/>없음": "Colour sensor without AWB <br/>algorithm", "컬러 센서에 AWB 알고리즘이 <br/>있음": "Colour sensor with AWB <br/>algorithm"}
  v_request["요청에 ColourTemperature가 <br/>있음"]
  v_mono["값을 무시함"]
  v_missing["경고를 기록하고 적용을 <br/>건너뜀"]
  v_manual["색온도를 전달하고 AWB를 <br/>수동으로 전환"]
  v_request -->|"모노 센서"| v_mono
  v_request -->|"컬러 센서에 AWB 알고리즘이 <br/>없음"| v_missing
  v_request -->|"컬러 센서에 AWB 알고리즘이 <br/>있음"| v_manual
```

[Mermaid 원문](colour-temperature.rpi-awb-branches.mmd)

??? note "그림 근거와 확인 범위"
    Raspberry Pi IPA는 색온도 값을 받으면 언제 적용합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Request contains ColourTemperature">요청에 ColourTemperature가 있음</span> | [src/ipa/rpi/common/ipa_base.cpp:922](#source-89a050db0c9f481c) |
    | <span data-sdd-label-en="Value ignored">값을 무시함</span> | [src/ipa/rpi/common/ipa_base.cpp:922](#source-89a050db0c9f481c) |
    | <span data-sdd-label-en="Warning logged and application skipped">경고를 기록하고 적용을 건너뜀</span> | [src/ipa/rpi/common/ipa_base.cpp:922](#source-89a050db0c9f481c) |
    | <span data-sdd-label-en="Set temperature and switch AWB to manual">색온도를 전달하고 AWB를 수동으로 전환</span> | [src/ipa/rpi/common/ipa_base.cpp:922](#source-89a050db0c9f481c) |
    | <span data-sdd-label-en="Monochrome sensor">모노 센서</span> | [src/ipa/rpi/common/ipa_base.cpp:922](#source-89a050db0c9f481c) |
    | <span data-sdd-label-en="Colour sensor without AWB algorithm">컬러 센서에 AWB 알고리즘이 없음</span> | [src/ipa/rpi/common/ipa_base.cpp:922](#source-89a050db0c9f481c) |
    | <span data-sdd-label-en="Colour sensor with AWB algorithm">컬러 센서에 AWB 알고리즘이 있음</span> | [src/ipa/rpi/common/ipa_base.cpp:922](#source-89a050db0c9f481c) |
<!-- /sdd:visual:rpi-awb-branches -->

Raspberry Pi IPA의 요청 처리 코드는 `ColourTemperature`이 있으면 모노 센서에서 해당 제어값을 조용히 무시합니다. AWB 알고리즘을 찾지 못하면 경고를 기록하고 해당 처리를 끝냅니다. 그 외에는 AWB 알고리즘의 `setColourTemperature()`를 호출한 뒤 `awbEnabled_`를 `false`로 설정하여 AWB를 수동 모드로 전환합니다. 메타데이터 처리 코드는 `awb.status`가 있으면 그 상태의 `temperatureK`를 `ColourTemperature` 메타데이터로 설정합니다. `src/ipa/rpi/common/ipa_base.cpp:922`, `src/ipa/rpi/common/ipa_base.cpp:1556`

근거 원문: [src/libcamera/control_ids_core.yaml:603](#source-d3108f17b82d0b49) · [src/ipa/rpi/common/ipa_base.cpp:922](#source-89a050db0c9f481c) · [src/ipa/rpi/common/ipa_base.cpp:1556](#source-b162436961ceca50)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | ColourTemperature의 inout 방향이 요청 입력과 프레임 메타데이터에서 무엇을 의미합니까? AWB 조건, 함께 지정하지 않은 ColourGains와 ColourCorrectionMatrix 처리, Raspberry Pi IPA가 요청 값을 건너뛰거나 적용하는 조건을 설명하세요. | [ColourTemperature 요청과 결과](#colourtemperature-요청과-결과) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-d3108f17b82d0b49"></a>

??? note "소스 근거: src/libcamera/control_ids_core.yaml:603"
    `src/libcamera/control_ids_core.yaml:603`에서 시작하는 발췌입니다. 종료 줄은 624이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `88d918f272cfe013114d36d9fe244120ed99ec7bc21a01e5235d403a752d2580`
    
    ```text
      - ColourTemperature:
          type: int32_t
          direction: inout
          description: |
            ColourTemperature of the frame, in kelvin.
    
            ColourTemperature can only be applied in a Request when the AWB is
            disabled.
    
            If ColourTemperature is set in a request but ColourGains is not, the
            implementation shall calculate and set the ColourGains based on the
            given ColourTemperature. If ColourTemperature is set (either directly,
            or indirectly by setting ColourGains) but ColourCorrectionMatrix is not,
            the ColourCorrectionMatrix is updated based on the ColourTemperature.
    
            The ColourTemperature used to process the frame is reported in metadata.
    
            \sa AwbEnable
            \sa ColourCorrectionMatrix
            \sa ColourGains
    
      - Saturation:
    ```

<a id="source-89a050db0c9f481c"></a>

??? note "소스 근거: src/ipa/rpi/common/ipa_base.cpp:922"
    `src/ipa/rpi/common/ipa_base.cpp:922`에서 시작하는 발췌입니다. 종료 줄은 945이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `76ca45fd660615f583ca4502c7c3dcce4cc95ca517f86ad4038ed57bb8188505`
    
    ```text
    const auto colourTemperature = controls.get(controls::ColourTemperature);
    	if (colourTemperature)
    		do {
    			/* Silently ignore this control for a mono sensor. */
    			if (monoSensor_)
    				break;
    
    			auto temperatureK = *colourTemperature;
    			RPiController::AwbAlgorithm *awb = dynamic_cast<RPiController::AwbAlgorithm *>(
    				controller_.getAlgorithm("awb"));
    			if (!awb) {
    				LOG(IPARPI, Warning)
    					<< "Could not set COLOUR_TEMPERATURE - no AWB algorithm";
    				break;
    			}
    
    			awb->setColourTemperature(temperatureK);
    			awbEnabled_ = false; /* doing this puts AWB into manual mode */
    
    			/* This metadata will get reported back automatically. */
    			break;
    		} while (false);
    
    	/* Iterate over controls */
    ```

<a id="source-b162436961ceca50"></a>

??? note "소스 근거: src/ipa/rpi/common/ipa_base.cpp:1556"
    `src/ipa/rpi/common/ipa_base.cpp:1556`에서 시작하는 발췌입니다. 종료 줄은 1563이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `67b7df55c1cbd610014091a35a5074aaf3adb72628b0a47ea55fa32902e41c28`
    
    ```text
    AwbStatus *awbStatus = rpiMetadata.getLocked<AwbStatus>("awb.status");
    	if (awbStatus) {
    		libcameraMetadata_.set(controls::ColourGains, { static_cast<float>(awbStatus->gainR),
    								static_cast<float>(awbStatus->gainB) });
    		libcameraMetadata_.set(controls::ColourTemperature, awbStatus->temperatureK);
    	}
    
    	BlackLevelStatus *blackLevelStatus
    ```

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `src/ipa/rpi/common/ipa_base.cpp`, `src/libcamera/control_ids_core.yaml`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `da6a6ed33e`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-13 · 사람 검토 전

다음 단계: [관련 소스와 설명](https://github.com/TTolsun/libcamera-sdd/blob/da6a6ed33ed0ab305f10b6f8b44736150d39cef4/src/libcamera/control_ids_core.yaml#L603)
