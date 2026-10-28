---
generated_at: 2026-10-28T23:09:48+00:00
source_commit: e117198c015057761bb0bbaa85f963c41ce412d7
status: ok
section: rkisp1-dewarp
generation_method: facts-and-llm
evidence_fingerprint: 650eece9c36635cbfdbabb632c59765b850d105d0048387e7f2fef5ff9366924
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "650eece9c36635cbfdbabb632c59765b850d105d0048387e7f2fef5ff9366924", "answers": {"ownership": [{"text": "`RkISP1CameraData`는 카메라별 보정값을 `std::optional<Dw100VertexMap::DewarpParams>` 타입의 멤버 `dewarpParams_`에 보관합니다. `PipelineHandlerRkISP1::configure()`는 `cameraData(camera)`로 현재 카메라의 데이터를 가져와 보정기 사용 시 메인 경로에서 `dewarper_->configure()`에 그 데이터의 `dewarpParams_`를 전달합니다.", "evidence": ["camera", "configure"], "covers": ["ownership"], "kind": "behavior", "quote": "bool canUseDewarper_;\n\tbool usesDewarper_;\n\tstd::optional<Dw100VertexMap::DewarpParams> dewarpParams_;"}, {"text": "`RkISP1CameraData::loadTuningFile()`은 보정기가 없으면 파일을 열지 않고 0을 반환합니다. 보정기가 있을 때 파일 열기에 실패하면 파일 오류를 반환하고, YAML 파싱에 실패하면 `-EINVAL`을 반환합니다. `modules`가 없거나 `Dewarp` 항목을 찾지 못하면 0을 반환합니다.", "evidence": ["load"], "covers": ["ownership"], "kind": "behavior", "quote": "if (!pipe()->dewarper_)\n\t\t/* Nothing to do without dewarper */\n\t\treturn 0;"}, {"text": "`RkISP1CameraData::loadTuningFile()`은 `modules`에서 `Dewarp` 항목을 찾으면 `loadDewarpParams()`에 해당 항목과 자신의 `dewarpParams_`를 전달합니다. 호출이 실패하면 그 반환값을 반환하고, 성공하면 `canUseDewarper_`를 `true`로 설정한 뒤 0을 반환합니다. `PipelineHandlerRkISP1::configure()`는 `canUseDewarper_`가 참이고 첫 스트림이 RAW가 아닐 때 `usesDewarper_`를 참으로 설정합니다.", "evidence": ["load", "configure"], "covers": ["ownership"], "kind": "behavior", "quote": "ret = pipe()->dewarper_->loadDewarpParams(params, dewarpParams_);\n\t\tif (ret)\n\t\t\treturn ret;"}], "parameters": [{"text": "`ConverterDW100Module::loadDewarpParams()`는 먼저 출력 optional인 `dewarpParams`를 초기화합니다. `cm`, `coefficients`, `cmNew`가 모두 없으면 보정기는 여전히 동작하며 함수는 `0`을 반환합니다. 하나라도 있으면 `cm`과 `coefficients`가 모두 필요하며, 둘 중 하나가 없으면 `-EINVAL`을 반환합니다.", "evidence": ["parameters"], "covers": ["parameters"], "kind": "behavior", "quote": "/* If nothing is provided, the dewarper is still functional */\n\tif (!cm && !coefficients && !cmNew)\n\t\treturn 0;"}, {"text": "`ConverterDW100Module::loadDewarpParams()`는 `cm`을 3×3 행렬로 읽고, `coefficients`를 실수 목록으로 읽어 설정합니다. `cm`을 행렬로 읽지 못하거나 `coefficients`가 목록이 아니면 `-EINVAL`을 반환합니다. `setCoefficients()`가 실패하면 계수가 4, 5, 8 또는 12개여야 한다는 오류를 기록하고 `-EINVAL`을 반환합니다.", "evidence": ["parameters"], "covers": ["parameters"], "kind": "behavior", "quote": "int ret = dp.setCoefficients(*coeffs);\n\tif (ret) {\n\t\tLOG(Converter, Error)\n\t\t\t<< \"Dewarp 'coefficients' must have 4, 5, 8 or 12 values\";\n\t\treturn -EINVAL;\n\t}"}, {"text": "`ConverterDW100Module::loadDewarpParams()`는 `cmNew`가 있으면 3×3 행렬로 읽으며, 읽지 못하면 `-EINVAL`을 반환합니다. `cmNew`가 없으면 `cm`을 기본값으로 사용합니다. 검사를 마친 뒤 `dp`를 `dewarpParams`에 저장하고 `0`을 반환합니다.", "evidence": ["parameters"], "covers": ["parameters"], "kind": "behavior", "quote": "dp.cmNew = *matrix;\n\t} else {\n\t\tdp.cmNew = dp.cm;\n\t}"}], "application": [{"text": "`ConverterDW100Module::configure`는 `setInputSize`에 `inputCfg.size`를 전달합니다.", "evidence": ["input-size"], "covers": ["application"], "kind": "behavior", "quote": "vertexMap.setInputSize(inputCfg.size);", "part_id": "configure"}, {"text": "`ConverterDW100Module::configure`는 `setOutputSize`에 현재 출력 설정인 `outputCfg`의 `size` 값을 전달합니다.", "evidence": ["output-size"], "covers": ["application"], "kind": "behavior", "quote": "vertexMap.setOutputSize(outputCfg.size);", "part_id": "output-size"}, {"text": "`ConverterDW100Module::configure()`는 `vertexMap.setSensorCrop()`에 `sensorCrop_` 값을 전달합니다.", "evidence": ["sensor-crop"], "covers": ["application"], "kind": "behavior", "quote": "vertexMap.setSensorCrop(sensorCrop_);", "part_id": "sensor-crop"}, {"text": "`ConverterDW100Module::configure`는 출력 스트림 반복문에서 `dewarpParams`에 값이 있으면 `vertexMap.setDewarpParams(*dewarpParams)`를 호출하여 그 값을 전달합니다.", "evidence": ["configure"], "covers": ["application"], "kind": "behavior", "quote": "if (dewarpParams)\n\t\t\tvertexMap.setDewarpParams(*dewarpParams);\n\t\tinfo.update = true;\n\t}", "part_id": "optional-params"}, {"text": "`ConverterDW100Module::updateControlInfos()`는 `hasDewarpParams_`가 참이면 `controls::LensDewarpEnable`을 지원 제어로 등록하고 최소값을 `false`, 최대값과 기본값을 `true`로 설정합니다.", "evidence": ["controls"], "covers": ["application"], "kind": "behavior", "quote": "if (hasDewarpParams_)\n\t\tcontrols[&controls::LensDewarpEnable] = ControlInfo(false, true, true);", "part_id": "support"}, {"text": "`ConverterDW100Module::setControls()`에서 `isConfigured(stream)`이 거짓이면 `return`이 함수를 즉시 종료합니다. 따라서 그 뒤의 제어값 처리와 로그 출력은 실행되지 않습니다.", "evidence": ["controls-entry"], "covers": ["application"], "kind": "behavior", "quote": "if (!isConfigured(stream))\n\t\treturn;", "part_id": "unconfigured-controls"}, {"text": "`ConverterDW100Module::setControls`는 스트림이 구성된 경우에만 제어를 처리합니다. `info.update`와 `running_`이 모두 참이고 `converter_.supportsRequests()`가 거짓이면 동적 DW100 제어 설정에 요청 지원 드라이버가 필요하다는 오류 로그를 기록합니다.", "evidence": ["controls"], "covers": ["application"], "kind": "behavior", "quote": "if (info.update && running_ && !converter_.supportsRequests())\n\t\tLOG(Converter, Error)\n\t\t\t<< \"Dynamically setting dw100 specific controls requires\"\n\t\t\t   \" a dw100 kernel driver with requests support\";\n}", "part_id": "runtime"}, {"text": "`populateMetadata`는 `isConfigured(stream)` 검사에서 스트림이 설정되지 않은 경우 바로 반환합니다.", "evidence": ["metadata"], "covers": ["application"], "kind": "behavior", "quote": "void ConverterDW100Module::populateMetadata(const Stream *stream, ControlList &meta)\n{\n\tif (!isConfigured(stream))\n\t\treturn;", "part_id": "metadata"}, {"text": "`ConverterDW100Module::populateMetadata()`는 설정된 스트림에 대해 `vertexMap.effectiveScalerCrop()`이 반환한 값을 `controls::ScalerCrop` 메타데이터에 기록합니다.", "evidence": ["crop-metadata"], "covers": ["application"], "kind": "behavior", "quote": "meta.set(controls::ScalerCrop, vertexMap.effectiveScalerCrop());", "part_id": "crop-metadata"}, {"text": "`ConverterDW100Module::populateMetadata()`는 스트림이 설정되어 있고 `hasDewarpParams_`가 참이면 `controls::LensDewarpEnable` 메타데이터에 `vertexMap.lensDewarpEnable()`의 반환값을 기록합니다.", "evidence": ["dewarp-metadata"], "covers": ["application"], "kind": "behavior", "quote": "if (hasDewarpParams_)\n\t\tmeta.set(controls::LensDewarpEnable, vertexMap.lensDewarpEnable());", "part_id": "dewarp-metadata"}]}, "topic_inputs": {"ownership": "17484a7d7e14bbb62d14f76204d7f13d2f8627c65268dff790f4938a7d14dbdb", "parameters": "f84b58f6539c18a3765e1d3a607833237ed7532c62cda4bd1665906fbb79920d", "application": "da61c4c72ac90eddb44898f45ad27cd6397dcca91becb3113318d8936994a2c7"}, "reused_topics": ["ownership", "parameters", "application"], "replayed_units": [], "generated_topics": [], "topic_agents": {"ownership": "cli/codex/gpt-6.1-terra", "parameters": "cli/codex/gpt-6.1-terra", "application": "cli/codex/gpt-6.1-terra"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "e0c429a5c80a01c34563ce00a616df89d8f75c735f8669bcbd1f75d84cce82a6", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "d4af3d834d8b1c99a6c9311612712a64112c30fa4621b375904d172f361285b8", "design_contracts": "b293a0012d1fcb6340fcaf94d481cf900212686978bc96fb118a0cdaddf3c091", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "65c405dc11cd8c43e2bce26ffbd96a47f37a784df59a4969be589ed8318f7be0", "answer_contracts": "1e0d24e0cf26ded53ecec2e5a6fbc51836bac6e17530318a9fa7cffaa936c00b", "design_response": "ce93f02b72371ed40f1b1124e78cef512baea31aa2df988db0c689f8169f783c", "design_validation": "608d2eed51e4ad5d5693fbc9b7d669ae1ba8e503f6736b62ea1ca068ce706556"}, "validation_model": "5ddbcbf91a6b516c4f71596d64b6286295bfd0cac771a7ca749ca78e25a2d752", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "f8fd5a3d8041c23fc68b93ff32b8727e98393383b5099032eb00ad0013e7611c"}, "reuse_lineage": {"source_commit": "e117198c015057761bb0bbaa85f963c41ce412d7", "body_sha256": "794b90df49bf4c27484ece6c1e8fabb3f4f5794bed05d0418d86e50da608685a", "topics": ["ownership", "parameters", "application"], "validation": "current source, contract and editorial checks; human review pending"}, "body_sha256": "794b90df49bf4c27484ece6c1e8fabb3f4f5794bed05d0418d86e50da608685a"}
---

# RKISP1 카메라별 왜곡 보정

**카메라별 보정값의 보관 위치와 설정 시점을 확인한 뒤 튜닝 입력과 커널 지원을 점검하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 카메라별 보정값의 소유권 절을 확인합니다. | [카메라별 보정값의 소유권](#카메라별-보정값의-소유권) |
| 튜닝 입력의 기본값과 오류 절을 확인합니다. | [튜닝 입력의 기본값과 오류](#튜닝-입력의-기본값과-오류) |
| 스트림 적용과 실행 확인 범위 절을 확인합니다. | [스트림 적용과 실행 확인 범위](#스트림-적용과-실행-확인-범위) |

## 카메라별 보정값의 소유권

`RkISP1CameraData`는 카메라별 보정값을 `std::optional<Dw100VertexMap::DewarpParams>` 타입의 멤버 `dewarpParams_`에 보관합니다. `PipelineHandlerRkISP1::configure()`는 `cameraData(camera)`로 현재 카메라의 데이터를 가져와 보정기 사용 시 메인 경로에서 `dewarper_->configure()`에 그 데이터의 `dewarpParams_`를 전달합니다. `src/libcamera/pipeline/rkisp1/rkisp1.cpp:94`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp:914`

<!-- sdd:visual:per-camera-parameters -->
### 보정값은 카메라별로 저장하고 구성 때 전달

보정값의 저장 위치와 전달을 표시합니다. 전역 보정값을 모든 카메라가 공유한다고 해석하지 마세요.

```mermaid
flowchart TB
%% sdd:translations {"RkISP1CameraData::dewarpPara<br/>ms_": "RkISP1CameraData::dewarpPara<br/>ms_", "cameraData(camera)로 선택": "Select with <br/>cameraData(camera)", "dewarper_-&gt;configure()": "dewarper_-&gt;configure()", "loadDewarpParams()가 저장": "loadDewarpParams() stores <br/>parameters", "usesDewarper_인 mainPath <br/>구성": "Configure mainPath when <br/>usesDewarper_", "튜닝 파일의 Dewarp 항목": "Dewarp entry in tuning file", "현재 카메라의 CameraData": "Current camera CameraData"}
  v_tuning["튜닝 파일의 Dewarp 항목"]
  v_camera["RkISP1CameraData::dewarpPara<br/>ms_"]
  v_configure["현재 카메라의 CameraData"]
  v_converter["dewarper_-&gt;configure()"]
  v_tuning -->|"loadDewarpParams()가 저장"| v_camera
  v_camera -->|"cameraData(camera)로 선택"| v_configure
  v_configure -->|"usesDewarper_인 mainPath <br/>구성"| v_converter
```

[Mermaid 원문](rkisp1-dewarp.per-camera-parameters.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | 튜닝 파일의 Dewarp 항목 | [src/libcamera/pipeline/rkisp1/rkisp1.cpp:434](#source-af6210cb39d0385e) |
    | RkISP1CameraData::dewarpParams_ | [src/libcamera/pipeline/rkisp1/rkisp1.cpp:94](#source-04546183f68b35f4) |
    | 현재 카메라의 CameraData | [src/libcamera/pipeline/rkisp1/rkisp1.cpp:914](#source-c164eb4c00d1c1d6) |
    | dewarper_-&gt;configure() | [src/libcamera/pipeline/rkisp1/rkisp1.cpp:914](#source-c164eb4c00d1c1d6) |
    | loadDewarpParams()가 저장 | [src/libcamera/pipeline/rkisp1/rkisp1.cpp:434](#source-af6210cb39d0385e) |
    | cameraData(camera)로 선택 | [src/libcamera/pipeline/rkisp1/rkisp1.cpp:914](#source-c164eb4c00d1c1d6) |
    | usesDewarper_인 mainPath 구성 | [src/libcamera/pipeline/rkisp1/rkisp1.cpp:914](#source-c164eb4c00d1c1d6) |
<!-- /sdd:visual:per-camera-parameters -->

`RkISP1CameraData::loadTuningFile()`은 보정기가 없으면 파일을 열지 않고 0을 반환합니다. 보정기가 있을 때 파일 열기에 실패하면 파일 오류를 반환하고, YAML 파싱에 실패하면 `-EINVAL`을 반환합니다. `modules`가 없거나 `Dewarp` 항목을 찾지 못하면 0을 반환합니다. `src/libcamera/pipeline/rkisp1/rkisp1.cpp:434`

`RkISP1CameraData::loadTuningFile()`은 `modules`에서 `Dewarp` 항목을 찾으면 `loadDewarpParams()`에 해당 항목과 자신의 `dewarpParams_`를 전달합니다. 호출이 실패하면 그 반환값을 반환하고, 성공하면 `canUseDewarper_`를 `true`로 설정한 뒤 0을 반환합니다. `PipelineHandlerRkISP1::configure()`는 `canUseDewarper_`가 참이고 첫 스트림이 RAW가 아닐 때 `usesDewarper_`를 참으로 설정합니다. `src/libcamera/pipeline/rkisp1/rkisp1.cpp:434`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp:914`

근거 원문: [src/libcamera/pipeline/rkisp1/rkisp1.cpp:94](#source-04546183f68b35f4) · [src/libcamera/pipeline/rkisp1/rkisp1.cpp:434](#source-af6210cb39d0385e) · [src/libcamera/pipeline/rkisp1/rkisp1.cpp:914](#source-c164eb4c00d1c1d6)

## 튜닝 입력의 기본값과 오류

`ConverterDW100Module::loadDewarpParams()`는 먼저 출력 optional인 `dewarpParams`를 초기화합니다. `cm`, `coefficients`, `cmNew`가 모두 없으면 보정기는 여전히 동작하며 함수는 `0`을 반환합니다. 하나라도 있으면 `cm`과 `coefficients`가 모두 필요하며, 둘 중 하나가 없으면 `-EINVAL`을 반환합니다. `src/libcamera/converter/converter_dw100.cpp:105`

<!-- sdd:visual:dewarp-input-branches -->
### 보정 파라미터의 기본값과 입력 오류

입력이 없는 경우와 일부만 잘못 제공한 경우를 구분하세요. 성공 반환만으로 보정값이 저장됐다고 판단하면 안 됩니다.

```mermaid
flowchart TB
%% sdd:translations {"-EINVAL 반환": "Return -EINVAL", "0 반환, optional은 비어 있음": "Return 0 with empty optional", "cmNew 기본값 적용 후 저장": "Apply cmNew default and <br/>store", "cm·coefficients·cmNew가 <br/>모두 없는가?": "Are cm, coefficients and <br/>cmNew all absent?", "아니오: 필수 입력 검사": "No: validate required input", "예: 별도 보정값 없음": "Yes: no explicit parameters", "유효, cmNew가 있으면 별도 <br/>검증": "Valid; also validate cmNew <br/>when provided", "필수 입력 누락·잘못된 형식": "Missing or malformed <br/>required input", "필수 행렬·계수가 유효한가?": "Required matrix and <br/>coefficients valid?"}
  v_empty{"cm·coefficients·cmNew가 <br/>모두 없는가?"}
  v_default["0 반환, optional은 비어 있음"]
  v_valid{"필수 행렬·계수가 유효한가?"}
  v_error["-EINVAL 반환"]
  v_store["cmNew 기본값 적용 후 저장"]
  v_empty -->|"예: 별도 보정값 없음"| v_default
  v_empty -->|"아니오: 필수 입력 검사"| v_valid
  v_valid -->|"필수 입력 누락·잘못된 형식"| v_error
  v_valid -->|"유효, cmNew가 있으면 별도 <br/>검증"| v_store
```

[Mermaid 원문](rkisp1-dewarp.dewarp-input-branches.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | cm·coefficients·cmNew가 모두 없는가? | [src/libcamera/converter/converter_dw100.cpp:105](#source-eacff078bd6a9d79) |
    | 0 반환, optional은 비어 있음 | [src/libcamera/converter/converter_dw100.cpp:105](#source-eacff078bd6a9d79) |
    | 필수 행렬·계수가 유효한가? | [src/libcamera/converter/converter_dw100.cpp:105](#source-eacff078bd6a9d79) |
    | -EINVAL 반환 | [src/libcamera/converter/converter_dw100.cpp:105](#source-eacff078bd6a9d79) |
    | cmNew 기본값 적용 후 저장 | [src/libcamera/converter/converter_dw100.cpp:105](#source-eacff078bd6a9d79) |
    | 예: 별도 보정값 없음 | [src/libcamera/converter/converter_dw100.cpp:105](#source-eacff078bd6a9d79) |
    | 아니오: 필수 입력 검사 | [src/libcamera/converter/converter_dw100.cpp:105](#source-eacff078bd6a9d79) |
    | 필수 입력 누락·잘못된 형식 | [src/libcamera/converter/converter_dw100.cpp:105](#source-eacff078bd6a9d79) |
    | 유효, cmNew가 있으면 별도 검증 | [src/libcamera/converter/converter_dw100.cpp:105](#source-eacff078bd6a9d79) |
<!-- /sdd:visual:dewarp-input-branches -->

`ConverterDW100Module::loadDewarpParams()`는 `cm`을 3×3 행렬로 읽고, `coefficients`를 실수 목록으로 읽어 설정합니다. `cm`을 행렬로 읽지 못하거나 `coefficients`가 목록이 아니면 `-EINVAL`을 반환합니다. `setCoefficients()`가 실패하면 계수가 4, 5, 8 또는 12개여야 한다는 오류를 기록하고 `-EINVAL`을 반환합니다. `src/libcamera/converter/converter_dw100.cpp:105`

`ConverterDW100Module::loadDewarpParams()`는 `cmNew`가 있으면 3×3 행렬로 읽으며, 읽지 못하면 `-EINVAL`을 반환합니다. `cmNew`가 없으면 `cm`을 기본값으로 사용합니다. 검사를 마친 뒤 `dp`를 `dewarpParams`에 저장하고 `0`을 반환합니다. `src/libcamera/converter/converter_dw100.cpp:105`

근거 원문: [src/libcamera/converter/converter_dw100.cpp:105](#source-eacff078bd6a9d79)

## 스트림 적용과 실행 확인 범위

`ConverterDW100Module::configure`는 `setInputSize`에 `inputCfg.size`를 전달합니다. `ConverterDW100Module::configure`는 `setOutputSize`에 현재 출력 설정인 `outputCfg`의 `size` 값을 전달합니다. `ConverterDW100Module::configure()`는 `vertexMap.setSensorCrop()`에 `sensorCrop_` 값을 전달합니다. `ConverterDW100Module::configure`는 출력 스트림 반복문에서 `dewarpParams`에 값이 있으면 `vertexMap.setDewarpParams(*dewarpParams)`를 호출하여 그 값을 전달합니다. `src/libcamera/converter/converter_dw100.cpp:197`, `src/libcamera/converter/converter_dw100.cpp:198`, `src/libcamera/converter/converter_dw100.cpp:199`, `src/libcamera/converter/converter_dw100.cpp:178`

`ConverterDW100Module::updateControlInfos()`는 `hasDewarpParams_`가 참이면 `controls::LensDewarpEnable`을 지원 제어로 등록하고 최소값을 `false`, 최대값과 기본값을 `true`로 설정합니다. `ConverterDW100Module::setControls()`에서 `isConfigured(stream)`이 거짓이면 `return`이 함수를 즉시 종료합니다. 따라서 그 뒤의 제어값 처리와 로그 출력은 실행되지 않습니다. `src/libcamera/converter/converter_dw100.cpp:369`, `src/libcamera/converter/converter_dw100.cpp:402`

`ConverterDW100Module::setControls`는 스트림이 구성된 경우에만 제어를 처리합니다. `info.update`와 `running_`이 모두 참이고 `converter_.supportsRequests()`가 거짓이면 동적 DW100 제어 설정에 요청 지원 드라이버가 필요하다는 오류 로그를 기록합니다. `populateMetadata`는 `isConfigured(stream)` 검사에서 스트림이 설정되지 않은 경우 바로 반환합니다. `ConverterDW100Module::populateMetadata()`는 설정된 스트림에 대해 `vertexMap.effectiveScalerCrop()`이 반환한 값을 `controls::ScalerCrop` 메타데이터에 기록합니다. `src/libcamera/converter/converter_dw100.cpp:369`, `src/libcamera/converter/converter_dw100.cpp:434`, `src/libcamera/converter/converter_dw100.cpp:441`

`ConverterDW100Module::populateMetadata()`는 스트림이 설정되어 있고 `hasDewarpParams_`가 참이면 `controls::LensDewarpEnable` 메타데이터에 `vertexMap.lensDewarpEnable()`의 반환값을 기록합니다. `src/libcamera/converter/converter_dw100.cpp:443`

근거 원문: [src/libcamera/converter/converter_dw100.cpp:178](#source-167e93a77fbf4931) · [src/libcamera/converter/converter_dw100.cpp:369](#source-fc0e25ddead912f1) · [src/libcamera/converter/converter_dw100.cpp:434](#source-3a4c4ed7cee81158) · [src/libcamera/converter/converter_dw100.cpp:197](#source-fff6050000b728bd) · [src/libcamera/converter/converter_dw100.cpp:198](#source-a6496a0f6db3636a) · [src/libcamera/converter/converter_dw100.cpp:199](#source-a92725ea0f81f8d7) · [src/libcamera/converter/converter_dw100.cpp:402](#source-ec47236059d2723f) · [src/libcamera/converter/converter_dw100.cpp:441](#source-6fc7fca6e9842fbd) · [src/libcamera/converter/converter_dw100.cpp:443](#source-aebf4a59ba423b05)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 여러 카메라의 보정값이 섞이지 않도록 누가 값을 보관하고 전달합니까? | [카메라별 보정값의 소유권](#카메라별-보정값의-소유권) | 코드 근거와 설명 연결 |
    | 보정값이 없거나 일부만 있을 때 어떤 결과를 반환합니까? | [튜닝 입력의 기본값과 오류](#튜닝-입력의-기본값과-오류) | 코드 근거와 설명 연결 |
    | 보정값은 어느 스트림에 적용되고 어떤 실행 조건을 따로 확인해야 합니까? | [스트림 적용과 실행 확인 범위](#스트림-적용과-실행-확인-범위) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-04546183f68b35f4"></a>

??? note "소스 근거: src/libcamera/pipeline/rkisp1/rkisp1.cpp:94"
    `src/libcamera/pipeline/rkisp1/rkisp1.cpp:94`에서 시작하는 발췌입니다. 종료 줄은 142이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `4c9387123443d958220746e355a9e93b30dca2bb4a32b4f4020c938e1a699de1`
    
    ```text
    class RkISP1CameraData : public Camera::Private
    {
    public:
    	RkISP1CameraData(PipelineHandler *pipe, RkISP1MainPath *mainPath,
    			 RkISP1SelfPath *selfPath)
    		: Camera::Private(pipe), frame_(0), frameInfo_(pipe),
    		  mainPath_(mainPath), selfPath_(selfPath),
    		  canUseDewarper_(false), usesDewarper_(false)
    	{
    	}
    
    	PipelineHandlerRkISP1 *pipe();
    	const PipelineHandlerRkISP1 *pipe() const;
    	int loadIPA(unsigned int hwRevision, uint32_t supportedBlocks);
    
    	Stream mainPathStream_;
    	Stream selfPathStream_;
    	std::unique_ptr<CameraSensor> sensor_;
    	std::unique_ptr<DelayedControls> delayedCtrls_;
    	unsigned int frame_;
    	std::vector<IPABuffer> ipaBuffers_;
    	RkISP1Frames frameInfo_;
    
    	RkISP1MainPath *mainPath_;
    	RkISP1SelfPath *selfPath_;
    
    	std::unique_ptr<ipa::rkisp1::IPAProxyRkISP1> ipa_;
    
    	ControlInfoMap ipaControls_;
    
    	/*
    	 * All entities in the pipeline, from the camera sensor to the RKISP1.
    	 */
    	MediaPipeline pipe_;
    
    	bool canUseDewarper_;
    	bool usesDewarper_;
    	std::optional<Dw100VertexMap::DewarpParams> dewarpParams_;
    
    private:
    	void paramsComputed(unsigned int frame, unsigned int bytesused);
    	void setSensorControls(unsigned int frame,
    			       const ControlList &sensorControls);
    
    	void metadataReady(unsigned int frame, const ControlList &metadata);
    	int loadTuningFile(const std::string &file);
    };
    
    class RkISP1CameraConfiguration :
    ```

<a id="source-af6210cb39d0385e"></a>

??? note "소스 근거: src/libcamera/pipeline/rkisp1/rkisp1.cpp:434"
    `src/libcamera/pipeline/rkisp1/rkisp1.cpp:434`에서 시작하는 발췌입니다. 종료 줄은 479이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `d0fb5eb90b4c6d0df3e90cff142c95b4f7daeddb6d483a4272a5fb07d7dd3fec`
    
    ```text
    int RkISP1CameraData::loadTuningFile(const std::string &path)
    {
    	int ret;
    
    	if (!pipe()->dewarper_)
    		/* Nothing to do without dewarper */
    		return 0;
    
    	LOG(RkISP1, Debug) << "Load tuning file " << path;
    
    	File file(path);
    	if (!file.open(File::OpenModeFlag::ReadOnly)) {
    		ret = file.error();
    		LOG(RkISP1, Error)
    			<< "Failed to open tuning file "
    			<< path << ": " << strerror(-ret);
    		return ret;
    	}
    
    	std::unique_ptr<ValueNode> data = YamlParser::parse(file);
    	if (!data)
    		return -EINVAL;
    
    	if (!data->contains("modules"))
    		return 0;
    
    	const auto &modules = (*data)["modules"].asList();
    	for (const auto &module : modules) {
    		const auto &params = module["Dewarp"];
    		if (!params)
    			continue;
    
    		ret = pipe()->dewarper_->loadDewarpParams(params, dewarpParams_);
    		if (ret)
    			return ret;
    
    		LOG(RkISP1, Info) << "Dw100 dewarper initialized";
    
    		canUseDewarper_ = true;
    		return 0;
    	}
    
    	return 0;
    }
    
    void RkISP1CameraData::paramsComputed(
    ```

<a id="source-c164eb4c00d1c1d6"></a>

??? note "소스 근거: src/libcamera/pipeline/rkisp1/rkisp1.cpp:914"
    `src/libcamera/pipeline/rkisp1/rkisp1.cpp:914`에서 시작하는 발췌입니다. 종료 줄은 1122이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `85e3aef5f0b623538bedbd13a895c0a08ada48616ab1e9ee8fe1a87882b67ee6`
    
    ```text
    int PipelineHandlerRkISP1::configure(Camera *camera, CameraConfiguration *c)
    {
    	RkISP1CameraConfiguration *config =
    		static_cast<RkISP1CameraConfiguration *>(c);
    	RkISP1CameraData *data = cameraData(camera);
    	CameraSensor *sensor = data->sensor_.get();
    	int ret;
    
    	ret = initLinks(camera, *config);
    	if (ret)
    		return ret;
    
    	const PixelFormat &streamFormat = config->at(0).pixelFormat;
    	const PixelFormatInfo &info = PixelFormatInfo::info(streamFormat);
    	isRaw_ = info.colourEncoding == PixelFormatInfo::ColourEncodingRAW;
    	data->usesDewarper_ = data->canUseDewarper_ && !isRaw_;
    
    	Transform transform = config->combinedTransform();
    	bool transposeAfterIsp = false;
    	if (data->usesDewarper_) {
    		if (!!(transform & Transform::Transpose))
    			transposeAfterIsp = true;
    		transform = Transform::Identity;
    	}
    
    	/*
    	 * Configure the format on the sensor output and propagate it through
    	 * the pipeline.
    	 */
    	V4L2SubdeviceFormat format = config->sensorFormat();
    	LOG(RkISP1, Debug) << "Configuring sensor with " << format;
    
    	if (config->sensorConfig)
    		ret = sensor->applyConfiguration(*config->sensorConfig,
    						 transform,
    						 &format);
    	else
    		ret = sensor->setFormat(&format, transform);
    
    	if (ret < 0)
    		return ret;
    
    	LOG(RkISP1, Debug) << "Sensor configured with " << format;
    
    	/* Propagate format through the internal media pipeline up to the ISP */
    	ret = data->pipe_.configure(sensor, &format);
    	if (ret < 0)
    		return ret;
    
    	LOG(RkISP1, Debug) << "Configuring ISP with : " << format;
    	ret = isp_->setFormat(0, &format);
    	if (ret < 0)
    		return ret;
    
    	Rectangle inputCrop(0, 0, format.size);
    	ret = isp_->setSelection(0, V4L2_SEL_TGT_CROP, &inputCrop);
    	if (ret < 0)
    		return ret;
    
    	LOG(RkISP1, Debug)
    		<< "ISP input pad configured with " << format
    		<< " crop " << inputCrop;
    
    	Rectangle outputCrop = inputCrop;
    
    	/* YUYV8_2X8 is required on the ISP source path pad for YUV output. */
    	if (!isRaw_)
    		format.code = MEDIA_BUS_FMT_YUYV8_2X8;
    
    	/*
    	 * On devices without DUAL_CROP (like the imx8mp) cropping needs to be
    	 * done on the ISP/IS output.
    	 *
    	 * If the dewarper is used, the cropping shall be done by the dewarper.
    	 */
    	if (media_->hwRevision() == RKISP1_V_IMX8MP) {
    		/* imx8mp has only a single path. */
    		const auto &cfg = config->at(0);
    		/*
    		 * If the dewarper is used, all cropping including aspect ratio
    		 * preservation shall be done there. To ensure that the output
    		 * format provided by the ISP is supported by the dewarper, a
    		 * minimal crop still needs to be applied on the ISP output.
    		 *
    		 * \todo It might be possible to allocate bigger buffers
    		 * (aligned to 8 pixels) with a stride matching format.size for
    		 * the ISP. The not-filled border could later be ignored by the
    		 * dewarper. This way we could skip the minimal crop here and
    		 * the MaximumScalerCrop would always match the isp output.
    		 */
    		Size ispCrop;
    		if (data->usesDewarper_)
    			ispCrop = dewarper_->adjustInputSize(cfg.pixelFormat,
    							     format.size);
    		else
    			ispCrop = format.size.boundedToAspectRatio(cfg.size)
    					  .alignedUpTo(2, 2);
    
    		outputCrop = ispCrop.centeredTo(Rectangle(format.size).center());
    		format.size = ispCrop;
    	}
    
    	LOG(RkISP1, Debug)
    		<< "Configuring ISP output pad with " << format
    		<< " crop " << outputCrop;
    
    	ret = isp_->setSelection(2, V4L2_SEL_TGT_CROP, &outputCrop);
    	if (ret < 0)
    		return ret;
    
    	format.colorSpace = config->at(0).colorSpace;
    	ret = isp_->setFormat(2, &format);
    	if (ret < 0)
    		return ret;
    
    	LOG(RkISP1, Debug)
    		<< "ISP output pad configured with " << format
    		<< " crop " << outputCrop;
    
    	IPACameraSensorInfo sensorInfo;
    	ret = data->sensor_->sensorInfo(&sensorInfo);
    	if (ret)
    		return ret;
    
    	/* Apply the actual sensor crop for proper dewarp map calculation. */
    	Rectangle sensorCrop = outputCrop.transformedBetween(
    		inputCrop, sensorInfo.analogCrop);
    	if (data->usesDewarper_)
    		dewarper_->setSensorCrop(sensorCrop);
    	data->properties_.set(properties::ScalerCropMaximum, sensorCrop);
    
    	std::map<unsigned int, IPAStream> streamConfig;
    
    	for (const StreamConfiguration &cfg : *config) {
    		if (cfg.stream() == &data->mainPathStream_) {
    			/*
    			 * To allow for digital zoom, scaling down should happen
    			 * in the dewarper, instead of the resizer. Configure
    			 * the isp output to the same size as the sensor output.
    			 */
    			StreamConfiguration ispCfg = cfg;
    			if (data->usesDewarper_) {
    				ispCfg.bufferCount = kRkISP1MinBufferCount;
    				ispCfg.size = format.size;
    				ispCfg.stride =
    					PixelFormatInfo::info(ispCfg.pixelFormat)
    						.stride(ispCfg.size.width, 0);
    
    				ret = dewarper_->configure(ispCfg, { cfg }, data->dewarpParams_);
    				if (ret)
    					return ret;
    
    				dewarper_->setTransform(cfg.stream(), config->combinedTransform());
    				/*
    				 * Apply a default scaler crop that keeps the
    				 * aspect ratio.
    				 */
    				Size size = cfg.size;
    				if (transposeAfterIsp)
    					size.transpose();
    				size = sensorCrop.size().boundedToAspectRatio(size);
    
    				ControlList ctrls;
    				ctrls.set(controls::ScalerCrop, size.centeredTo(sensorCrop.center()));
    				dewarper_->setControls(cfg.stream(), ctrls);
    			}
    
    			ret = mainPath_.configure(ispCfg, format);
    			streamConfig[0] = IPAStream(cfg.pixelFormat,
    						    cfg.size);
    		} else if (hasSelfPath_) {
    			ret = selfPath_.configure(cfg, format);
    			streamConfig[1] = IPAStream(cfg.pixelFormat,
    						    cfg.size);
    		} else {
    			return -ENODEV;
    		}
    
    		if (ret)
    			return ret;
    	}
    
    	V4L2DeviceFormat paramFormat;
    	paramFormat.fourcc = V4L2PixelFormat(V4L2_META_FMT_RK_ISP1_EXT_PARAMS);
    	ret = param_->setFormat(&paramFormat);
    	if (ret)
    		return ret;
    
    	V4L2DeviceFormat statFormat;
    	statFormat.fourcc = V4L2PixelFormat(V4L2_META_FMT_RK_ISP1_STAT_3A);
    	ret = stat_->setFormat(&statFormat);
    	if (ret)
    		return ret;
    
    	/* Inform IPA of stream configuration and sensor controls. */
    	ipa::rkisp1::IPAConfigInfo ipaConfig{ sensorInfo,
    					      data->sensor_->controls(),
    					      paramFormat.fourcc };
    
    	ret = data->ipa_->configure(ipaConfig, streamConfig, &data->ipaControls_);
    	if (ret) {
    		LOG(RkISP1, Error) << "failed configuring IPA (" << ret << ")";
    		return ret;
    	}
    
    	return updateControls(data);
    }
    
    int PipelineHandlerRkISP1::exportFrameBuffers(
    ```

<a id="source-eacff078bd6a9d79"></a>

??? note "소스 근거: src/libcamera/converter/converter_dw100.cpp:105"
    `src/libcamera/converter/converter_dw100.cpp:105`에서 시작하는 발췌입니다. 종료 줄은 178이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `5e4f1317cd9611173e6e5b1fa350ab26f28500656037c812909008604ebfb091`
    
    ```text
    int ConverterDW100Module::loadDewarpParams(const ValueNode &params,
    					   std::optional<Dw100VertexMap::DewarpParams> &dewarpParams)
    {
    	Dw100VertexMap::DewarpParams dp;
    	dewarpParams.reset();
    
    	auto &cm = params["cm"];
    	auto &coefficients = params["coefficients"];
    	auto &cmNew = params["cmNew"];
    
    	/* If nothing is provided, the dewarper is still functional */
    	if (!cm && !coefficients && !cmNew)
    		return 0;
    
    	if (!cm) {
    		LOG(Converter, Error) << "Dewarp parameters are missing 'cm' value";
    		return -EINVAL;
    	}
    
    	auto matrix = cm.get<Matrix<double, 3, 3>>();
    	if (!matrix) {
    		LOG(Converter, Error) << "Failed to load 'cm' value";
    		return -EINVAL;
    	}
    
    	dp.cm = *matrix;
    
    	if (!coefficients) {
    		LOG(Converter, Error) << "Dewarp parameters are missing 'coefficients' value";
    		return -EINVAL;
    	}
    
    	const auto coeffs = coefficients.get<std::vector<double>>();
    	if (!coeffs) {
    		LOG(Converter, Error) << "Dewarp parameters 'coefficients' value is not a list";
    		return -EINVAL;
    	}
    
    	int ret = dp.setCoefficients(*coeffs);
    	if (ret) {
    		LOG(Converter, Error)
    			<< "Dewarp 'coefficients' must have 4, 5, 8 or 12 values";
    		return -EINVAL;
    	}
    
    	if (cmNew) {
    		matrix = cmNew.get<Matrix<double, 3, 3>>();
    		if (!matrix) {
    			LOG(Converter, Error) << "Failed to load 'cmNew' value";
    			return -EINVAL;
    		}
    
    		dp.cmNew = *matrix;
    	} else {
    		dp.cmNew = dp.cm;
    	}
    
    	dewarpParams = dp;
    
    	return 0;
    }
    
    /**
     * \brief Configure a the dw100 converter module
     * \param[in] inputCfg Input stream configuration
     * \param[in] outputCfgs A list of output stream configurations
     * \param[in] dewarpParams The lens dewarp parameters to apply
     *
     * Configures the converter for the given input and output stream configurations
     * and an optional set of dewarp parameters.
     *
     * \return 0 on success or a negative error code otherwise
     */
    int ConverterDW100Module::configure(
    ```

<a id="source-167e93a77fbf4931"></a>

??? note "소스 근거: src/libcamera/converter/converter_dw100.cpp:178"
    `src/libcamera/converter/converter_dw100.cpp:178`에서 시작하는 발췌입니다. 종료 줄은 212이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `b517243a55de2dab95250c687c7f2aab9fd32b4ed115e3b65b8878daa39b0bc8`
    
    ```text
    int ConverterDW100Module::configure(const StreamConfiguration &inputCfg,
    				    const std::vector<std::reference_wrapper<const StreamConfiguration>>
    					    &outputCfgs,
    				    const std::optional<Dw100VertexMap::DewarpParams> &dewarpParams)
    {
    	int ret;
    
    	vertexMaps_.clear();
    	ret = converter_.configure(inputCfg, outputCfgs);
    	if (ret)
    		return ret;
    
    	inputBufferCount_ = inputCfg.bufferCount;
    	hasDewarpParams_ = dewarpParams.has_value();
    
    	for (auto &ref : outputCfgs) {
    		const auto &outputCfg = ref.get();
    		auto &info = vertexMaps_[outputCfg.stream()];
    		auto &vertexMap = info.map;
    		vertexMap.setInputSize(inputCfg.size);
    		vertexMap.setOutputSize(outputCfg.size);
    		vertexMap.setSensorCrop(sensorCrop_);
    
    		if (dewarpParams)
    			vertexMap.setDewarpParams(*dewarpParams);
    		info.update = true;
    	}
    
    	return 0;
    }
    
    /**
     * \copydoc libcamera::V4L2M2MConverter::isConfigured
     */
    bool ConverterDW100Module::isConfigured(
    ```

<a id="source-fc0e25ddead912f1"></a>

??? note "소스 근거: src/libcamera/converter/converter_dw100.cpp:369"
    `src/libcamera/converter/converter_dw100.cpp:369`에서 시작하는 발췌입니다. 종료 줄은 434이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `aa6937cbf814f9c7bf5c1dfab84e4d5e0fa96ace063b360484f3858066454e02`
    
    ```text
    void ConverterDW100Module::updateControlInfos(const Stream *stream, ControlInfoMap::Map &controls)
    {
    	ControlValue scalerCropDefault = sensorCrop_;
    
    	if (isConfigured(stream)) {
    		auto &info = vertexMaps_[stream];
    		info.map.applyLimits();
    		scalerCropDefault = info.map.effectiveScalerCrop();
    	}
    
    	controls[&controls::ScalerCrop] = ControlInfo(Rectangle(sensorCrop_.x, sensorCrop_.y, 1, 1),
    						      sensorCrop_, sensorCrop_);
    
    	if (hasDewarpParams_)
    		controls[&controls::LensDewarpEnable] = ControlInfo(false, true, true);
    
    	if (!converter_.supportsRequests())
    		LOG(Converter, Warning)
    			<< "dw100 kernel driver has no requests support."
    			   " Dynamic configuration is not possible.";
    }
    
    /**
     * \brief Set libcamera controls
     * \param[in] stream The stream to update
     * \param[in] controls The controls
     *
     * Looks up all supported controls in \a controls and sets them on stream \a
     * stream. The controls will be applied to the device on the next call to
     * queueBuffers().
     */
    void ConverterDW100Module::setControls(const Stream *stream, const ControlList &controls)
    {
    	if (!isConfigured(stream))
    		return;
    
    	auto &info = vertexMaps_[stream];
    	auto &vertexMap = info.map;
    
    	const auto &lensDewarpEnable = controls.get(controls::LensDewarpEnable);
    	if (lensDewarpEnable) {
    		vertexMap.setLensDewarpEnable(*lensDewarpEnable);
    		info.update = true;
    	}
    
    	const auto &crop = controls.get(controls::ScalerCrop);
    	if (crop) {
    		vertexMap.setScalerCrop(*crop);
    		info.update = true;
    	}
    
    	if (info.update && running_ && !converter_.supportsRequests())
    		LOG(Converter, Error)
    			<< "Dynamically setting dw100 specific controls requires"
    			   " a dw100 kernel driver with requests support";
    }
    
    /**
     * \brief Retrieve updated metadata
     * \param[in] stream The stream
     * \param[in] meta The metadata list
     *
     * This function retrieves the metadata for the provided \a stream and writes it
     * to \a list. It shall be called after queueBuffers().
     */
    void ConverterDW100Module::populateMetadata(
    ```

<a id="source-3a4c4ed7cee81158"></a>

??? note "소스 근거: src/libcamera/converter/converter_dw100.cpp:434"
    `src/libcamera/converter/converter_dw100.cpp:434`에서 시작하는 발췌입니다. 종료 줄은 465이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `37f3f992d5270f1f7309de486064df8a88ceebdafa81963ddb49872b7e674ecb`
    
    ```text
    void ConverterDW100Module::populateMetadata(const Stream *stream, ControlList &meta)
    {
    	if (!isConfigured(stream))
    		return;
    
    	auto &vertexMap = vertexMaps_[stream].map;
    
    	meta.set(controls::ScalerCrop, vertexMap.effectiveScalerCrop());
    
    	if (hasDewarpParams_)
    		meta.set(controls::LensDewarpEnable, vertexMap.lensDewarpEnable());
    }
    
    /**
     * \var ConverterDW100Module::inputBufferReady
     * \brief A signal emitted when the input frame buffer completes
     */
    
    /**
     * \var ConverterDW100Module::outputBufferReady
     * \brief A signal emitted on each frame buffer completion of the output queue
     */
    
    /**
     * \brief Set sensor crop rectangle
     * \param[in] rect The crop rectangle
     *
     * Set the sensor crop rectangle to \a rect. This rectangle describes the area
     * covered by the input buffers in sensor coordinates. It is used internally
     * to handle the ScalerCrop control and related metadata.
     */
    void ConverterDW100Module::setSensorCrop(
    ```

<a id="source-fff6050000b728bd"></a>

??? note "소스 근거: src/libcamera/converter/converter_dw100.cpp:197"
    `src/libcamera/converter/converter_dw100.cpp:197`에서 시작하는 발췌입니다. 종료 줄은 197이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `79a73838f65043686ff00e9decb65d5e058c110f8f633815a213b06858cad86c`
    
    ```text
    vertexMap.setInputSize(inputCfg.size);
    ```

<a id="source-a6496a0f6db3636a"></a>

??? note "소스 근거: src/libcamera/converter/converter_dw100.cpp:198"
    `src/libcamera/converter/converter_dw100.cpp:198`에서 시작하는 발췌입니다. 종료 줄은 198이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `ff8b08a01f0408c265812b9f25f000f48aa90b693ea8464759f4ad5c955cd742`
    
    ```text
    vertexMap.setOutputSize(outputCfg.size);
    ```

<a id="source-a92725ea0f81f8d7"></a>

??? note "소스 근거: src/libcamera/converter/converter_dw100.cpp:199"
    `src/libcamera/converter/converter_dw100.cpp:199`에서 시작하는 발췌입니다. 종료 줄은 199이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `a9ebf143a526bae7de1baeb9b3e16dbddd4e3b5a9ff2db059bfc1d9f3f5cf3ae`
    
    ```text
    vertexMap.setSensorCrop(sensorCrop_);
    ```

<a id="source-ec47236059d2723f"></a>

??? note "소스 근거: src/libcamera/converter/converter_dw100.cpp:402"
    `src/libcamera/converter/converter_dw100.cpp:402`에서 시작하는 발췌입니다. 종료 줄은 403이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `c5040e533831af4e7c96d2886389921009cc952c3969afe51bc33668cfcd0045`
    
    ```text
    if (!isConfigured(stream))
    		return;
    ```

<a id="source-6fc7fca6e9842fbd"></a>

??? note "소스 근거: src/libcamera/converter/converter_dw100.cpp:441"
    `src/libcamera/converter/converter_dw100.cpp:441`에서 시작하는 발췌입니다. 종료 줄은 441이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `0cae7e4a2d9a50beb66d4df9242bb3a720e325445dc4575db4c9b7d4e05126dd`
    
    ```text
    meta.set(controls::ScalerCrop, vertexMap.effectiveScalerCrop());
    ```

<a id="source-aebf4a59ba423b05"></a>

??? note "소스 근거: src/libcamera/converter/converter_dw100.cpp:443"
    `src/libcamera/converter/converter_dw100.cpp:443`에서 시작하는 발췌입니다. 종료 줄은 444이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `d8b9be0d0d3aa6f450f0317006eb47a5a4564b58869a63257194c410a34c9dd9`
    
    ```text
    if (hasDewarpParams_)
    		meta.set(controls::LensDewarpEnable, vertexMap.lensDewarpEnable());
    ```

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `include/libcamera/internal/converter.h`, `include/libcamera/internal/converter/converter_dw100.h`, `include/libcamera/internal/converter/converter_dw100_vertexmap.h`, `src/libcamera/converter.cpp`, `src/libcamera/converter/converter_dw100.cpp`, `src/libcamera/converter/converter_dw100_vertexmap.cpp`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `e117198c01`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-29 · 사람 검토 전

다음 단계: [Pipeline Handler](pipeline-handler.md)
