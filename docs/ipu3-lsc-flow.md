---
generated_at: 2026-10-25T08:20:42+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: ipu3-lsc-flow
generation_method: facts-and-llm
evidence_fingerprint: 1fc2ba3a6e182b8bf07200ec39b34dcac7e6a360a6470d8b69dd2e13c7a0e66a
semantic_review: human-review-required
agent: response-bundle/codex-session
generated_design: {"schema": 1, "input_fingerprint": "1fc2ba3a6e182b8bf07200ec39b34dcac7e6a360a6470d8b69dd2e13c7a0e66a", "answers": {"integration": [{"text": "IPU3 알고리즘을 나열하는 빌드 설정에는 `lsc.cpp`가 포함됩니다. 이는 빌드 대상에 포함된다는 근거이며, 실행할 때마다 보정이 활성화된다는 뜻은 아닙니다.", "covers": ["integration"], "kind": "behavior", "quote": "ipu3_ipa_algorithms = files([\n    'af.cpp',\n    'agc.cpp',\n    'awb.cpp',\n    'blc.cpp',\n    'ccm.cpp',\n    'lsc.cpp',\n    'tone_mapping.cpp',\n])", "evidence": ["build"]}, {"text": "`IPAActiveState`는 공유되는 활성 상태에 `ipa::lsc::ActiveState` 타입의 `lsc`를 둡니다. `IPAContext`는 이 활성 상태와 세션 구성, 센서 정보를 함께 보관합니다.", "covers": ["integration"], "kind": "behavior", "quote": "agc::ActiveState agc;\n\tipa::awb::ActiveState awb;\n\tipa::ccm::ActiveState ccm;\n\tipa::gamma::ActiveState gamma;\n\tipa::lsc::ActiveState lsc;\n};", "evidence": ["context"]}, {"text": "`IPAFrameContext`에는 프레임별 상태인 `ipa::lsc::FrameContext lsc`가 있습니다. `IPAContext`의 `frameContexts`는 이러한 프레임 컨텍스트를 `FCQueue`로 관리하므로 공유 활성 상태와 프레임별 상태를 구분해 읽어야 합니다.", "covers": ["integration"], "kind": "behavior", "quote": "agc::FrameContext agc;\n\tipa::awb::FrameContext awb;\n\tipa::ccm::FrameContext ccm;\n\tipa::gamma::FrameContext gamma;\n\tipa::lsc::FrameContext lsc;\n};", "evidence": ["context"]}], "setup": [{"text": "`Lsc::init()`은 센서 `activeArea`의 너비와 높이로 보정 그리드를 계산합니다. 가로 최대 73셀과 세로 최대 56셀을 기준으로 필요한 셀 크기를 올림한 뒤, `std::bit_ceil()`로 각각 다음 2의 거듭제곱 크기에 맞춥니다. 그 크기로 셀 개수와 가로·세로 크기의 log2 값을 구합니다.", "covers": ["setup"], "kind": "behavior", "quote": "/**\n * \\copydoc libcamera::ipa::Algorithm::init\n */\nint Lsc::init(IPAContext &context, const ValueNode &tuningData)\n{\n\t/*\n\t * The IPU3 lens shading block expects a table of data that isn't of a\n\t * fixed size, but rather is configurable based on 4 parameters:\n\t *\n\t * block_width_log2:\tThe log2 of the horizontal pixel count per cell\n\t * block_height_log2:\tThe log2 of the vertical pixel count per cell\n\t * width:\t\tThe number of horizontal cells\n\t * height:\t\tThe number of vertical cells\n\t *\n\t * The constructed grid should be capable of covering the image, but\n\t * ideally won't extend past the edges of the image. Fixing either set\n\t * of parameters for the algorithm as a whole is likely to result in\n\t * suboptimal situations for some sensors, so let's determine them\n\t * programmatically instead.\n\t *\n\t * What we want is the densest possible grid that ideally doesn't extend\n\t * past the edges of the image at all. The maximum grid size is 73x56,\n\t * which gives us the lower bounds on cell size. Unfortunately we can\n\t * only specify sizes in powers of two, which can have the effect of\n\t * making the grid much more coarse. For example for a 2592x1944 input\n\t * image, 2592 / 73 = 35.5...which means we need to set blockWidthLog2\n\t * to 6 (I.E. 64) and have just 40.5 (or rather 41) cells horizontally.\n\t */\n\tsensorWidth_ = context.sensorInfo.activeArea.width;\n\tsensorHeight_ = context.sensorInfo.activeArea.height;", "evidence": ["setup"]}, {"text": "`Lsc::init()`은 튜닝 데이터와 제어 정보 맵, `r`·`gr`·`gb`·`b` 키, 가로·세로 샘플 수와 센서 영역 크기를 공통 `lscAlgo_.init()`에 전달합니다. 튜닝의 `type`이 `polynomial`인지도 따로 저장합니다.", "covers": ["setup"], "kind": "behavior", "quote": "return lscAlgo_.init(tuningData, context.ctrlMap,\n\t\t\t     { .keys = { \"r\", \"gr\", \"gb\", \"b\" },\n\t\t\t       .numHSamples = numHCells_,\n\t\t\t       .numVSamples = numVCells_,\n\t\t\t       .sensorSize = context.sensorInfo.activeArea.size() });\n}", "evidence": ["setup"]}, {"text": "`Lsc::configure()`는 `analogCrop`의 너비와 높이를 저장하고 그리드 크기에 맞는 가로·세로 샘플 위치를 만듭니다. 공통 `configure()`에는 공유 LSC 상태와 전체 `analogCrop`, 두 위치 배열을 전달합니다.", "covers": ["setup"], "kind": "behavior", "quote": "/**\n * \\copydoc libcamera::ipa::Algorithm::configure\n */\nint Lsc::configure(IPAContext &context, const IPAConfigInfo &configInfo)\n{\n\tcropWidth_ = configInfo.sensorInfo.analogCrop.width;\n\tcropHeight_ = configInfo.sensorInfo.analogCrop.height;\n\tstd::vector<double> xPos = calculatePositions(numHCells_);\n\tstd::vector<double> yPos = calculatePositions(numVCells_);", "evidence": ["setup"]}, {"text": "`calculatePositions()`는 각 위치를 `i / (dimension - 1)`로 계산합니다. 샘플이 두 개 이상이면 양 끝이 0과 1인 정규화 위치가 되지만, 이 함수에는 샘플 수가 1일 때의 별도 경계 검사가 없습니다.", "covers": ["setup"], "kind": "behavior", "quote": "std::vector<double> Lsc::calculatePositions(unsigned int dimension)\n{\n\tstd::vector<double> positions(dimension);\n\tfor (double i = 0.0; i < dimension; i++)\n\t\tpositions[i] = i / (dimension - 1);", "evidence": ["setup"]}], "request": [{"text": "`Lsc::queueRequest()`는 첫 프레임인 `frame == 0`에서 `LensShadingCorrectionEnable` 제어의 포함 여부를 확인합니다. 제어가 없을 때만 해당 프레임의 `enabled`와 `update`를 모두 `true`로 설정합니다. 주석은 공통 알고리즘의 기본값이 켜짐인 반면 IPU3 드라이버 기본값은 꺼짐이어서 이 처리가 필요하다고 설명합니다.", "covers": ["request"], "kind": "behavior", "quote": "void Lsc::queueRequest(IPAContext &context, const uint32_t frame,\n\t\t       IPAFrameContext &frameContext,\n\t\t       const ControlList &controls)\n{\n\t/*\n\t * The base algorithm defines the LensShadingCorrectionEnable control\n\t * with a default value of true, but actually the IPU3 driver defaults\n\t * it to off. If this is the first frame, check for the control, but if\n\t * there isn't one, force it on to fulfil the advertised default.\n\t */\n\tif (frame == 0) {\n\t\tconst auto &lscEnable = controls.get(controls::LensShadingCorrectionEnable);\n\t\tif (!lscEnable) {\n\t\t\tframeContext.lsc.enabled = true;\n\t\t\tframeContext.lsc.update = true;\n\t\t}\n\t}", "evidence": ["request"]}, {"text": "`Lsc::queueRequest()`는 이후 공통 알고리즘에 `context.activeState.lsc`, `frameContext.lsc`, 요청의 `controls`를 전달합니다. 따라서 공유 활성 상태와 이번 프레임 상태, 제어 목록이 서로 다른 인자로 연결됩니다.", "covers": ["request"], "kind": "behavior", "quote": "lscAlgo_.queueRequest(context.activeState.lsc, frameContext.lsc, controls);\n}", "evidence": ["request"]}], "prepare": [{"text": "`Lsc::prepare()`는 프레임의 AWB 색온도를 읽고 10 단위로 양자화합니다. `quantize()`는 값을 단위 크기로 나눈 뒤 반올림하고 다시 그 단위를 곱합니다.", "covers": ["prepare"], "kind": "behavior", "quote": "/**\n * \\copydoc libcamera::ipa::Algorithm::prepare\n */\nvoid Lsc::prepare([[maybe_unused]] IPAContext &context, [[maybe_unused]] const uint32_t frame,\n\t\t  IPAFrameContext &frameContext, ipu3_uapi_params *params)\n{\n\tuint32_t ct = frameContext.awb.colourTemperature;\n\tunsigned int quantizedCt = quantize(ct, kColourTemperatureQuantization);", "evidence": ["prepare"]}, {"text": "`update`가 `false`일 때는 보정이 비활성인 경우 바로 반환합니다. 같은 분기 안에서 원래 색온도와 마지막 적용 색온도의 차이가 5보다 작거나, 양자화 색온도가 마지막 값과 같아도 반환합니다. 이 세 가지 생략 조건을 `update == true` 경로까지 확대하면 안 됩니다.", "covers": ["prepare"], "kind": "behavior", "quote": "if (!frameContext.lsc.update) {\n\t\tif (!frameContext.lsc.enabled)\n\t\t\treturn;", "evidence": ["prepare"]}, {"text": "갱신을 진행하는 `prepare()`는 먼저 `params->use.acc_shd`를 1로 설정하고 `shd_enable`에 이번 프레임의 활성 상태를 기록합니다. 비활성 상태라면 그 뒤에 반환하므로, `update == true`인 비활성화 전환도 이 플래그들을 전달합니다.", "covers": ["prepare"], "kind": "behavior", "quote": "/*\n\t * This flag tells the kernel driver that it should read the LSC params\n\t * passed from userspace instead of using its cached copy.\n\t */\n\tparams->use.acc_shd = 1;", "evidence": ["prepare"]}, {"text": "활성 경로의 `prepare()`는 계산해 둔 가로·세로 셀 수와 셀 크기의 log2 값, 슬라이스당 그리드 높이를 하드웨어 파라미터에 씁니다. 다항식 방식이면 시작 위치를 0으로, 그 외에는 크롭 크기와 센서 크기의 차이를 절반으로 나눈 값으로 설정합니다.", "covers": ["prepare"], "kind": "behavior", "quote": "config->grid.width = numHCells_;\n\tconfig->grid.height = numVCells_;\n\tconfig->grid.block_width_log2 = blockWidthLog2_;\n\tconfig->grid.block_height_log2 = blockHeightLog2_;\n\tconfig->grid.grid_height_per_slice = IPU3_UAPI_SHD_MAX_CELLS_PER_SET / numHCells_;", "evidence": ["prepare"]}, {"text": "`prepare()`는 `gain_factor`를 0으로 고정하고 이 LSC 블록의 네 채널 black level을 0으로 설정합니다. 주석은 black level 처리를 다른 파라미터 블록에서 수행한다고 설명합니다.", "covers": ["prepare"], "kind": "behavior", "quote": "/*\n\t * Values in the LUT cease taking effect at 4096, and a value of 0.0 is\n\t * \"no correction\" rather than black. The gain factor is described by\n\t * the documentation like so:\n\t *\n\t * \"Shift calculated anti shading value. Precision u2. 0x0 - gain factor\n\t * [1, 5], means no shift interpolated value. 0x1 - gain factor [1, 9],\n\t * means shift interpolated by 1. 0x2 - gain factor [1, 17], means shift\n\t * interpolated by 2.\"\n\t *\n\t * The simplest interpretation for those pieces of information is I\n\t * think that the LUT stores 12-bit Q numbers who's represented values\n\t * depend on the gain_factor setting like so:\n\t *\n\t * 0: UQ<2, 10> representing values in range [0, 4)\n\t * 1: UQ<3, 9> representing values in range [0, 8)\n\t * 2: UQ<4, 8> representing values in range [0, 16)\n\t *\n\t * And that a base gain of 1.0 is added to those configured values. As a\n\t * gain of more than 5.0 is fairly unlikely, let's fix gain_factor to 0\n\t * for now and revisit if needed.\n\t */\n\tconfig->general.gain_factor = 0;", "evidence": ["prepare"]}, {"text": "`prepare()`는 양자화 색온도로 공통 알고리즘의 `interpolateComponents()`를 호출하고, 반환된 `r`·`gr`·`gb`·`b` 값을 LUT의 각 세트에 복사합니다. 활성 경로의 기록이 끝난 뒤 원래 색온도와 양자화 색온도를 각각 `lastAppliedCt_`, `lastAppliedQuantizedCt_`에 저장합니다.", "covers": ["prepare"], "kind": "behavior", "quote": "const auto &set = lscAlgo_.interpolateComponents(quantizedCt);", "evidence": ["prepare"]}], "metadata": [{"text": "`Lsc::process()` 래퍼는 `frameContext.lsc`와 출력 `metadata`를 공통 `lscAlgo_.process()`에 전달합니다. 래퍼 자체는 `context`, 프레임 번호와 `stats`를 직접 사용하지 않으며 해당 인자에는 `maybe_unused` 속성이 붙어 있습니다.", "covers": ["metadata"], "kind": "behavior", "quote": "void Lsc::process([[maybe_unused]] IPAContext &context,\n\t\t  [[maybe_unused]] const uint32_t frame,\n\t\t  IPAFrameContext &frameContext,\n\t\t  [[maybe_unused]] const ipu3_uapi_stats_3a *stats,\n\t\t  ControlList &metadata)\n{\n\tlscAlgo_.process(frameContext.lsc, metadata);\n}", "evidence": ["process"]}, {"text": "파일 끝의 `REGISTER_IPA_ALGORITHM(Lsc, \"Lsc\")`는 `Lsc` 이름으로 알고리즘을 등록합니다. 이 등록문과 래퍼 호출만으로 실제 장치의 보정 결과나 실행 성능까지 확인할 수는 없습니다.", "covers": ["metadata"], "kind": "behavior", "quote": "REGISTER_IPA_ALGORITHM(Lsc, \"Lsc\")", "evidence": ["process"]}]}, "topic_inputs": {"integration": "5c2870e13b08e677092efdb11b938fe9a587f1310413af7e1b13999fa40c0099", "setup": "066c892daad5dfd0463add6d82a15a6e34322b3912e224a41bdb042023b0f5d5", "request": "e869929629af7a0366bcc799c95fb3ee642e4d14942348c8b13f2c927b7f6a62", "prepare": "5706aeae42c6f08f63d20bcde567cf91522cf7b5f4f574826630bb578dc89ac3", "metadata": "f1dc1606395c72f01b13460e99e965b29fbd1fa002bea1740d49fa5418e4b052"}, "reused_topics": ["integration", "setup", "request", "prepare", "metadata"], "generated_topics": [], "topic_agents": {"integration": "response-bundle/codex-session", "setup": "response-bundle/codex-session", "request": "response-bundle/codex-session", "prepare": "response-bundle/codex-session", "metadata": "response-bundle/codex-session"}, "body_sha256": "203fb1e12a4a2ba885b8040b8f48c07a9afe190840a8abfc9b7751b4782817a1"}
---

# IPU3 LSC의 설정과 프레임 처리

**LSC를 수정할 때는 초기 그리드 설정, 요청별 활성화 상태, 색온도에 따른 파라미터 갱신 조건을 차례로 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 빌드와 상태 연결 절을 확인합니다. | [빌드와 상태 연결](#빌드와-상태-연결) |
| 초기화와 크롭 설정 절을 확인합니다. | [초기화와 크롭 설정](#초기화와-크롭-설정) |
| 첫 프레임과 요청별 제어 절을 확인합니다. | [첫 프레임과 요청별 제어](#첫-프레임과-요청별-제어) |
| 파라미터 갱신 조건 절을 확인합니다. | [파라미터 갱신 조건](#파라미터-갱신-조건) |
| 메타데이터와 확인 범위 절을 확인합니다. | [메타데이터와 확인 범위](#메타데이터와-확인-범위) |

## 빌드와 상태 연결

IPU3 알고리즘을 나열하는 빌드 설정에는 `lsc.cpp`가 포함됩니다. 이는 빌드 대상에 포함된다는 근거이며, 실행할 때마다 보정이 활성화된다는 뜻은 아닙니다. `src/ipa/ipu3/algorithms/meson.build:3`

`IPAActiveState`는 공유되는 활성 상태에 `ipa::lsc::ActiveState` 타입의 `lsc`를 둡니다. `IPAContext`는 이 활성 상태와 세션 구성, 센서 정보를 함께 보관합니다. `src/ipa/ipu3/ipa_context.h:32`

`IPAFrameContext`에는 프레임별 상태인 `ipa::lsc::FrameContext lsc`가 있습니다. `IPAContext`의 `frameContexts`는 이러한 프레임 컨텍스트를 `FCQueue`로 관리하므로 공유 활성 상태와 프레임별 상태를 구분해 읽어야 합니다. `src/ipa/ipu3/ipa_context.h:32`

근거 원문: [src/ipa/ipu3/algorithms/meson.build:3](#source-914bc0dd95a64016) · [src/ipa/ipu3/ipa_context.h:32](#source-47a8aa55a4a846f4)

## 초기화와 크롭 설정

`Lsc::init()`은 센서 `activeArea`의 너비와 높이로 보정 그리드를 계산합니다. 가로 최대 73셀과 세로 최대 56셀을 기준으로 필요한 셀 크기를 올림한 뒤, `std::bit_ceil()`로 각각 다음 2의 거듭제곱 크기에 맞춥니다. 그 크기로 셀 개수와 가로·세로 크기의 log2 값을 구합니다. `src/ipa/ipu3/algorithms/lsc.cpp:31`

`Lsc::init()`은 튜닝 데이터와 제어 정보 맵, `r`·`gr`·`gb`·`b` 키, 가로·세로 샘플 수와 센서 영역 크기를 공통 `lscAlgo_.init()`에 전달합니다. 튜닝의 `type`이 `polynomial`인지도 따로 저장합니다. `src/ipa/ipu3/algorithms/lsc.cpp:31`

`Lsc::configure()`는 `analogCrop`의 너비와 높이를 저장하고 그리드 크기에 맞는 가로·세로 샘플 위치를 만듭니다. 공통 `configure()`에는 공유 LSC 상태와 전체 `analogCrop`, 두 위치 배열을 전달합니다. `src/ipa/ipu3/algorithms/lsc.cpp:31`

`calculatePositions()`는 각 위치를 `i / (dimension - 1)`로 계산합니다. 샘플이 두 개 이상이면 양 끝이 0과 1인 정규화 위치가 되지만, 이 함수에는 샘플 수가 1일 때의 별도 경계 검사가 없습니다. `src/ipa/ipu3/algorithms/lsc.cpp:31`

근거 원문: [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb)

## 첫 프레임과 요청별 제어

`Lsc::queueRequest()`는 첫 프레임인 `frame == 0`에서 `LensShadingCorrectionEnable` 제어의 포함 여부를 확인합니다. 제어가 없을 때만 해당 프레임의 `enabled`와 `update`를 모두 `true`로 설정합니다. 주석은 공통 알고리즘의 기본값이 켜짐인 반면 IPU3 드라이버 기본값은 꺼짐이어서 이 처리가 필요하다고 설명합니다. `src/ipa/ipu3/algorithms/lsc.cpp:121`

<!-- sdd:visual:lsc-request-input -->
### 요청 제어가 프레임 상태에 반영되는 곳

첫 프레임에서 활성화 제어가 없으면 광고한 기본값을 맞춥니다. 이후 공통 LSC 알고리즘에 요청 제어를 전달합니다.

```mermaid
flowchart TB
%% sdd:translations {"enabled=true, update=true": "enabled=true, update=true", "공통 LSC queueRequest()": "Common LSC queueRequest()", "기본값 적용 후 전달": "Forward after applying default", "아니오": "No", "아니오: 전달된 제어 사용": "No: use supplied control", "예": "Yes", "첫 프레임인가?": "First frame?", "활성화 제어가 없는가?": "Enable control absent?"}
  v_first{"첫 프레임인가?"}
  v_control{"활성화 제어가 없는가?"}
  v_default["enabled=true, update=true"]
  v_common["공통 LSC queueRequest()"]
  v_first -->|"예"| v_control
  v_first -->|"아니오"| v_common
  v_control -->|"예"| v_default
  v_control -->|"아니오: 전달된 제어 사용"| v_common
  v_default -->|"기본값 적용 후 전달"| v_common
```

[Mermaid 원문](ipu3-lsc-flow.lsc-request-input.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | 첫 프레임인가? | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
    | 활성화 제어가 없는가? | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
    | enabled=true, update=true | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
    | 공통 LSC queueRequest() | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
    | 예 | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
    | 아니오 | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
    | 예 | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
    | 아니오: 전달된 제어 사용 | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
    | 기본값 적용 후 전달 | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
<!-- /sdd:visual:lsc-request-input -->

`Lsc::queueRequest()`는 이후 공통 알고리즘에 `context.activeState.lsc`, `frameContext.lsc`, 요청의 `controls`를 전달합니다. 따라서 공유 활성 상태와 이번 프레임 상태, 제어 목록이 서로 다른 인자로 연결됩니다. `src/ipa/ipu3/algorithms/lsc.cpp:121`

근거 원문: [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8)

## 파라미터 갱신 조건

`Lsc::prepare()`는 프레임의 AWB 색온도를 읽고 10 단위로 양자화합니다. `quantize()`는 값을 단위 크기로 나눈 뒤 반올림하고 다시 그 단위를 곱합니다. `src/ipa/ipu3/algorithms/lsc.cpp:142`

<!-- sdd:visual:lsc-update-gates -->
### LSC 파라미터를 갱신하는 분기

명시적 update가 있으면 색온도 생략 검사를 건너뜁니다. 갱신을 통지한 뒤 비활성 상태이면 LUT 계산은 수행하지 않습니다.

```mermaid
flowchart TB
%% sdd:translations {"lsc.enabled인가?": "lsc.enabled?", "lsc.update인가?": "lsc.update?", "use.acc_shd와 활성화 값 기록": "Write use.acc_shd and enable flag", "색온도 차이가 임계값 이상인가?": "Colour-temperature difference reaches threshold?", "아니오": "No", "양자화된 색온도가 달라졌는가?": "Quantized temperature changed?", "예": "Yes", "파라미터 갱신 없이 반환": "Return without updating parameters", "활성 상태면 LUT 계산·기록": "Compute and write LUT when enabled", "활성 상태일 때만": "Only when enabled"}
  v_update{"lsc.update인가?"}
  v_enabled{"lsc.enabled인가?"}
  v_threshold{"색온도 차이가 임계값 이상인가?"}
  v_quantized{"양자화된 색온도가 달라졌는가?"}
  v_skip["파라미터 갱신 없이 반환"]
  v_notify["use.acc_shd와 활성화 값 기록"]
  v_lut["활성 상태면 LUT 계산·기록"]
  v_update -->|"예"| v_notify
  v_update -->|"아니오"| v_enabled
  v_enabled -->|"아니오"| v_skip
  v_enabled -->|"예"| v_threshold
  v_threshold -->|"아니오"| v_skip
  v_threshold -->|"예"| v_quantized
  v_quantized -->|"아니오"| v_skip
  v_quantized -->|"예"| v_notify
  v_notify -->|"활성 상태일 때만"| v_lut
```

[Mermaid 원문](ipu3-lsc-flow.lsc-update-gates.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | lsc.update인가? | [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) |
    | lsc.enabled인가? | [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) |
    | 색온도 차이가 임계값 이상인가? | [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) |
    | 양자화된 색온도가 달라졌는가? | [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) |
    | 파라미터 갱신 없이 반환 | [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) |
    | use.acc_shd와 활성화 값 기록 | [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) |
    | 활성 상태면 LUT 계산·기록 | [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) |
    | 예 | [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) |
    | 아니오 | [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) |
    | 아니오 | [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) |
    | 예 | [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) |
    | 아니오 | [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) |
    | 예 | [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) |
    | 아니오 | [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) |
    | 예 | [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) |
    | 활성 상태일 때만 | [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) |
<!-- /sdd:visual:lsc-update-gates -->

`update`가 `false`일 때는 보정이 비활성인 경우 바로 반환합니다. 같은 분기 안에서 원래 색온도와 마지막 적용 색온도의 차이가 5보다 작거나, 양자화 색온도가 마지막 값과 같아도 반환합니다. 이 세 가지 생략 조건을 `update == true` 경로까지 확대하면 안 됩니다. `src/ipa/ipu3/algorithms/lsc.cpp:142`

갱신을 진행하는 `prepare()`는 먼저 `params->use.acc_shd`를 1로 설정하고 `shd_enable`에 이번 프레임의 활성 상태를 기록합니다. 비활성 상태라면 그 뒤에 반환하므로, `update == true`인 비활성화 전환도 이 플래그들을 전달합니다. `src/ipa/ipu3/algorithms/lsc.cpp:142`

활성 경로의 `prepare()`는 계산해 둔 가로·세로 셀 수와 셀 크기의 log2 값, 슬라이스당 그리드 높이를 하드웨어 파라미터에 씁니다. 다항식 방식이면 시작 위치를 0으로, 그 외에는 크롭 크기와 센서 크기의 차이를 절반으로 나눈 값으로 설정합니다. `src/ipa/ipu3/algorithms/lsc.cpp:142`

`prepare()`는 `gain_factor`를 0으로 고정하고 이 LSC 블록의 네 채널 black level을 0으로 설정합니다. 주석은 black level 처리를 다른 파라미터 블록에서 수행한다고 설명합니다. `src/ipa/ipu3/algorithms/lsc.cpp:142`

`prepare()`는 양자화 색온도로 공통 알고리즘의 `interpolateComponents()`를 호출하고, 반환된 `r`·`gr`·`gb`·`b` 값을 LUT의 각 세트에 복사합니다. 활성 경로의 기록이 끝난 뒤 원래 색온도와 양자화 색온도를 각각 `lastAppliedCt_`, `lastAppliedQuantizedCt_`에 저장합니다. `src/ipa/ipu3/algorithms/lsc.cpp:142`

근거 원문: [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) · [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-af2cbcaa6410fbf4)

## 메타데이터와 확인 범위

`Lsc::process()` 래퍼는 `frameContext.lsc`와 출력 `metadata`를 공통 `lscAlgo_.process()`에 전달합니다. 래퍼 자체는 `context`, 프레임 번호와 `stats`를 직접 사용하지 않으며 해당 인자에는 `maybe_unused` 속성이 붙어 있습니다. `src/ipa/ipu3/algorithms/lsc.cpp:282`

파일 끝의 `REGISTER_IPA_ALGORITHM(Lsc, "Lsc")`는 `Lsc` 이름으로 알고리즘을 등록합니다. 이 등록문과 래퍼 호출만으로 실제 장치의 보정 결과나 실행 성능까지 확인할 수는 없습니다. `src/ipa/ipu3/algorithms/lsc.cpp:282`

근거 원문: [src/ipa/ipu3/algorithms/lsc.cpp:282](#source-5e8cfeb51ea8c16a)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | LSC 구현 파일과 공유 상태 및 프레임별 상태는 어떻게 연결됩니까? | [빌드와 상태 연결](#빌드와-상태-연결) | 코드 근거와 설명 연결 |
    | 입력 크기에 따라 그리드와 크기 제한을 어떻게 결정합니까? | [초기화와 크롭 설정](#초기화와-크롭-설정) | 코드 근거와 설명 연결 |
    | 첫 프레임의 기본 활성화와 요청 제어는 어떤 데이터를 전달합니까? | [첫 프레임과 요청별 제어](#첫-프레임과-요청별-제어) | 코드 근거와 설명 연결 |
    | 갱신은 어떤 조건에서 수행하며 커널에 어떤 파라미터를 전달합니까? | [파라미터 갱신 조건](#파라미터-갱신-조건) | 코드 근거와 설명 연결 |
    | 프레임 처리 결과를 어떻게 통지합니까? | [메타데이터와 확인 범위](#메타데이터와-확인-범위) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-914bc0dd95a64016"></a>

??? note "소스 근거: src/ipa/ipu3/algorithms/meson.build:3"
    `src/ipa/ipu3/algorithms/meson.build:3`에서 시작하는 발췌입니다. 종료 줄은 11이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `5b34e175668b4fedb33a633567f049c2738f6368c3b4d8ac26d069e77add82c9`
    
    ```text
    ipu3_ipa_algorithms = files([
        'af.cpp',
        'agc.cpp',
        'awb.cpp',
        'blc.cpp',
        'ccm.cpp',
        'lsc.cpp',
        'tone_mapping.cpp',
    ])
    ```

<a id="source-47a8aa55a4a846f4"></a>

??? note "소스 근거: src/ipa/ipu3/ipa_context.h:32"
    `src/ipa/ipu3/ipa_context.h:32`에서 시작하는 발췌입니다. 종료 줄은 91이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e373aff7c5b5e5f034637b3d9030b0fdef974614261025791afd6e3146b1108d`
    
    ```text
    struct IPASessionConfiguration {
    	struct {
    		ipu3_uapi_grid_config bdsGrid;
    		Size bdsOutputSize;
    		uint32_t stride;
    	} grid;
    
    	struct {
    		ipu3_uapi_grid_config afGrid;
    	} af;
    
    	agc::Session agc;
    };
    
    struct IPAActiveState {
    	struct {
    		uint32_t focus;
    		double maxVariance;
    		bool stable;
    	} af;
    
    	agc::ActiveState agc;
    	ipa::awb::ActiveState awb;
    	ipa::ccm::ActiveState ccm;
    	ipa::gamma::ActiveState gamma;
    	ipa::lsc::ActiveState lsc;
    };
    
    struct IPAFrameContext : public FrameContext {
    	struct {
    		uint32_t exposure;
    		double gain;
    	} sensor;
    
    	agc::FrameContext agc;
    	ipa::awb::FrameContext awb;
    	ipa::ccm::FrameContext ccm;
    	ipa::gamma::FrameContext gamma;
    	ipa::lsc::FrameContext lsc;
    };
    
    struct IPAContext {
    	IPAContext(unsigned int frameContextSize)
    		: frameContexts(frameContextSize)
    	{
    	}
    
    	IPASessionConfiguration configuration;
    	IPACameraSensorInfo sensorInfo;
    	ControlInfoMap sensorControls;
    	IPAActiveState activeState;
    
    	FCQueue<IPAFrameContext> frameContexts;
    
    	std::unique_ptr<CameraSensorHelper> camHelper;
    
    	ControlInfoMap::Map ctrlMap;
    };
    
    } /* namespace ipa::ipu3 */
    ```

<a id="source-441d18135ba28bdb"></a>

??? note "소스 근거: src/ipa/ipu3/algorithms/lsc.cpp:31"
    `src/ipa/ipu3/algorithms/lsc.cpp:31`에서 시작하는 발췌입니다. 종료 줄은 121이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `b4b73b83ec5f1caeb1e654f00aace0f49abf402b43c0ff6bd30528176ea8a566`
    
    ```text
    static constexpr unsigned int kMaxNumHCells = 73;
    static constexpr unsigned int kMaxNumVCells = 56;
    static constexpr int kColourTemperatureQuantization = 10;
    
    /**
     * \copydoc libcamera::ipa::Algorithm::init
     */
    int Lsc::init(IPAContext &context, const ValueNode &tuningData)
    {
    	/*
    	 * The IPU3 lens shading block expects a table of data that isn't of a
    	 * fixed size, but rather is configurable based on 4 parameters:
    	 *
    	 * block_width_log2:	The log2 of the horizontal pixel count per cell
    	 * block_height_log2:	The log2 of the vertical pixel count per cell
    	 * width:		The number of horizontal cells
    	 * height:		The number of vertical cells
    	 *
    	 * The constructed grid should be capable of covering the image, but
    	 * ideally won't extend past the edges of the image. Fixing either set
    	 * of parameters for the algorithm as a whole is likely to result in
    	 * suboptimal situations for some sensors, so let's determine them
    	 * programmatically instead.
    	 *
    	 * What we want is the densest possible grid that ideally doesn't extend
    	 * past the edges of the image at all. The maximum grid size is 73x56,
    	 * which gives us the lower bounds on cell size. Unfortunately we can
    	 * only specify sizes in powers of two, which can have the effect of
    	 * making the grid much more coarse. For example for a 2592x1944 input
    	 * image, 2592 / 73 = 35.5...which means we need to set blockWidthLog2
    	 * to 6 (I.E. 64) and have just 40.5 (or rather 41) cells horizontally.
    	 */
    	sensorWidth_ = context.sensorInfo.activeArea.width;
    	sensorHeight_ = context.sensorInfo.activeArea.height;
    
    	unsigned int cellWidth = (sensorWidth_ + kMaxNumHCells - 1) / kMaxNumHCells;
    	unsigned int cellHeight = (sensorHeight_ + kMaxNumVCells - 1) / kMaxNumVCells;
    
    	unsigned int minCellWidth = std::bit_ceil(cellWidth);
    	unsigned int minCellHeight = std::bit_ceil(cellHeight);
    
    	numHCells_ = (sensorWidth_ + minCellWidth - 1) / minCellWidth;
    	numVCells_ = (sensorHeight_ + minCellHeight - 1) / minCellHeight;
    
    	blockWidthLog2_ = std::bit_width(minCellWidth) - 1;
    	blockHeightLog2_ = std::bit_width(minCellHeight) - 1;
    
    	LOG(IPU3Lsc, Debug) << "Calculated Grid configuration: "
    			    << numHCells_ << "x" << numVCells_ << " cells of "
    			    << minCellWidth << "x" << minCellHeight << " pixels";
    
    	/*
    	 * We need to know if we're running the polynomial algorithm or not as
    	 * things will behave slightly differently.
    	 */
    	polynomial_ = tuningData["type"].get<std::string>() == "polynomial";
    
    	return lscAlgo_.init(tuningData, context.ctrlMap,
    			     { .keys = { "r", "gr", "gb", "b" },
    			       .numHSamples = numHCells_,
    			       .numVSamples = numVCells_,
    			       .sensorSize = context.sensorInfo.activeArea.size() });
    }
    
    std::vector<double> Lsc::calculatePositions(unsigned int dimension)
    {
    	std::vector<double> positions(dimension);
    	for (double i = 0.0; i < dimension; i++)
    		positions[i] = i / (dimension - 1);
    
    	return positions;
    }
    
    /**
     * \copydoc libcamera::ipa::Algorithm::configure
     */
    int Lsc::configure(IPAContext &context, const IPAConfigInfo &configInfo)
    {
    	cropWidth_ = configInfo.sensorInfo.analogCrop.width;
    	cropHeight_ = configInfo.sensorInfo.analogCrop.height;
    	std::vector<double> xPos = calculatePositions(numHCells_);
    	std::vector<double> yPos = calculatePositions(numVCells_);
    
    	return lscAlgo_.configure(context.activeState.lsc,
    				  configInfo.sensorInfo.analogCrop, xPos, yPos);
    }
    
    /**
     * \copydoc libcamera::ipa::Algorithm::queueRequest
     */
    void Lsc::queueRequest(
    ```

<a id="source-80fd6c99ec2c0ae8"></a>

??? note "소스 근거: src/ipa/ipu3/algorithms/lsc.cpp:121"
    `src/ipa/ipu3/algorithms/lsc.cpp:121`에서 시작하는 발췌입니다. 종료 줄은 142이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `550c83f35d2a4d5218ac10731fe8650d8446e262841f2dd80a54e9238c7da287`
    
    ```text
    void Lsc::queueRequest(IPAContext &context, const uint32_t frame,
    		       IPAFrameContext &frameContext,
    		       const ControlList &controls)
    {
    	/*
    	 * The base algorithm defines the LensShadingCorrectionEnable control
    	 * with a default value of true, but actually the IPU3 driver defaults
    	 * it to off. If this is the first frame, check for the control, but if
    	 * there isn't one, force it on to fulfil the advertised default.
    	 */
    	if (frame == 0) {
    		const auto &lscEnable = controls.get(controls::LensShadingCorrectionEnable);
    		if (!lscEnable) {
    			frameContext.lsc.enabled = true;
    			frameContext.lsc.update = true;
    		}
    	}
    
    	lscAlgo_.queueRequest(context.activeState.lsc, frameContext.lsc, controls);
    }
    
    static unsigned int quantize(
    ```

<a id="source-026024190618ffa6"></a>

??? note "소스 근거: src/ipa/ipu3/algorithms/lsc.cpp:142"
    `src/ipa/ipu3/algorithms/lsc.cpp:142`에서 시작하는 발췌입니다. 종료 줄은 282이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `1d11fc7397b377f682d4fab45d12dd20480e554176aae94ba2708a5f8f747268`
    
    ```text
    static unsigned int quantize(unsigned int value, unsigned int step)
    {
    	return std::lround(value / static_cast<double>(step)) * step;
    }
    
    /**
     * \copydoc libcamera::ipa::Algorithm::prepare
     */
    void Lsc::prepare([[maybe_unused]] IPAContext &context, [[maybe_unused]] const uint32_t frame,
    		  IPAFrameContext &frameContext, ipu3_uapi_params *params)
    {
    	uint32_t ct = frameContext.awb.colourTemperature;
    	unsigned int quantizedCt = quantize(ct, kColourTemperatureQuantization);
    
    	if (!frameContext.lsc.update) {
    		if (!frameContext.lsc.enabled)
    			return;
    
    		/*
    		 * Add a threshold so that oscillations around a quantization
    		 * step don't lead to constant changes.
    		 */
    		if (utils::abs_diff(ct, lastAppliedCt_) < kColourTemperatureQuantization / 2)
    			return;
    
    		if (quantizedCt == lastAppliedQuantizedCt_)
    			return;
    	}
    
    	/*
    	 * This flag tells the kernel driver that it should read the LSC params
    	 * passed from userspace instead of using its cached copy.
    	 */
    	params->use.acc_shd = 1;
    
    	/*
    	 * Pass the enabled flag. If we're not enabled, we can then just bail
    	 * out.
    	 */
    	ipu3_uapi_shd_config_static *config = &params->acc_param.shd.shd;
    	config->general.shd_enable = frameContext.lsc.enabled;
    
    	if (!frameContext.lsc.enabled)
    		return;
    
    	config->grid.width = numHCells_;
    	config->grid.height = numVCells_;
    	config->grid.block_width_log2 = blockWidthLog2_;
    	config->grid.block_height_log2 = blockHeightLog2_;
    	config->grid.grid_height_per_slice = IPU3_UAPI_SHD_MAX_CELLS_PER_SET / numHCells_;
    
    	/*
    	 * The IPU3's documentation describes the x_start and y_start members
    	 * as follows:
    	 *
    	 * "[X/Y] value of top left corner of sensor relative to ROI
    	 * s13, [-4096, 0], default 0, only negative values."
    	 *
    	 * I interpret that as allowing us to configure the cropped rectangle
    	 * relative to the full grid. That's useful if we're running the tabular
    	 * algorithm, which would otherwise apply the full grid inappropriately.
    	 * If we're running the polynomial one though the calculated grid is
    	 * probably more appropriate than a coarse application of the full grid
    	 * so let's tell the hardware not to bother correcting in that case.
    	 */
    	if (polynomial_) {
    		config->grid.x_start = 0;
    		config->grid.y_start = 0;
    	} else {
    		config->grid.x_start = (cropWidth_ - sensorWidth_) / 2;
    		config->grid.y_start = (cropHeight_ - sensorHeight_) / 2;
    	}
    
    	/* No idea what this is, but the docs say it should be set as so */
    	config->general.init_set_vrt_offst_ul =
    		config->grid.y_start >> (config->grid.block_height_log2 %
    					 config->grid.grid_height_per_slice);
    
    	/*
    	 * Values in the LUT cease taking effect at 4096, and a value of 0.0 is
    	 * "no correction" rather than black. The gain factor is described by
    	 * the documentation like so:
    	 *
    	 * "Shift calculated anti shading value. Precision u2. 0x0 - gain factor
    	 * [1, 5], means no shift interpolated value. 0x1 - gain factor [1, 9],
    	 * means shift interpolated by 1. 0x2 - gain factor [1, 17], means shift
    	 * interpolated by 2."
    	 *
    	 * The simplest interpretation for those pieces of information is I
    	 * think that the LUT stores 12-bit Q numbers who's represented values
    	 * depend on the gain_factor setting like so:
    	 *
    	 * 0: UQ<2, 10> representing values in range [0, 4)
    	 * 1: UQ<3, 9> representing values in range [0, 8)
    	 * 2: UQ<4, 8> representing values in range [0, 16)
    	 *
    	 * And that a base gain of 1.0 is added to those configured values. As a
    	 * gain of more than 5.0 is fairly unlikely, let's fix gain_factor to 0
    	 * for now and revisit if needed.
    	 */
    	config->general.gain_factor = 0;
    
    	/*
    	 * Disable the black level settings here - we do that through another
    	 * parameters block.
    	 */
    	config->black_level.bl_r = 0;
    	config->black_level.bl_gr = 0;
    	config->black_level.bl_gb = 0;
    	config->black_level.bl_b = 0;
    
    	ipu3_uapi_shd_lut *lut = &params->acc_param.shd.shd_lut;
    
    	const auto &set = lscAlgo_.interpolateComponents(quantizedCt);
    
    	unsigned int totalCells = numHCells_ * numVCells_;
    	unsigned int cellsPerSet = numHCells_ * config->grid.grid_height_per_slice;
    	unsigned int numSets = (numHCells_ + config->grid.grid_height_per_slice - 1) /
    			       config->grid.grid_height_per_slice;
    	unsigned int i = 0;
    
    	for (unsigned int s = 0; s < numSets; s++) {
    		for (unsigned int c = 0; c < cellsPerSet && i < totalCells; c++, i++) {
    			lut->sets[s].r_and_gr[c].r = set.at("r")[i];
    			lut->sets[s].r_and_gr[c].gr = set.at("gr")[i];
    			lut->sets[s].gb_and_b[c].gb = set.at("gb")[i];
    			lut->sets[s].gb_and_b[c].b = set.at("b")[i];
    		}
    	}
    
    	lastAppliedCt_ = ct;
    	lastAppliedQuantizedCt_ = quantizedCt;
    	LOG(IPU3Lsc, Debug)
    		<< "ct is " << ct << ", quantized to "
    		<< quantizedCt;
    }
    
    /**
     * \copydoc libcamera::ipa::Algorithm::process
     */
    void Lsc::process(
    ```

<a id="source-af2cbcaa6410fbf4"></a>

??? note "소스 근거: src/ipa/ipu3/algorithms/lsc.cpp:31"
    `src/ipa/ipu3/algorithms/lsc.cpp:31`에서 시작하는 발췌입니다. 종료 줄은 38이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `7807718b4ae9327f1ca428627d2b00f59ba38ced03261465ee8c79312ea27833`
    
    ```text
    static constexpr unsigned int kMaxNumHCells = 73;
    static constexpr unsigned int kMaxNumVCells = 56;
    static constexpr int kColourTemperatureQuantization = 10;
    
    /**
     * \copydoc libcamera::ipa::Algorithm::init
     */
    int Lsc::init(
    ```

<a id="source-5e8cfeb51ea8c16a"></a>

??? note "소스 근거: src/ipa/ipu3/algorithms/lsc.cpp:282"
    `src/ipa/ipu3/algorithms/lsc.cpp:282`에서 시작하는 발췌입니다. 종료 줄은 291이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e1411dc6710e62f774ea84588792a3f6fd547beb3442bc7cc49495eb19dff05e`
    
    ```text
    void Lsc::process([[maybe_unused]] IPAContext &context,
    		  [[maybe_unused]] const uint32_t frame,
    		  IPAFrameContext &frameContext,
    		  [[maybe_unused]] const ipu3_uapi_stats_3a *stats,
    		  ControlList &metadata)
    {
    	lscAlgo_.process(frameContext.lsc, metadata);
    }
    
    REGISTER_IPA_ALGORITHM(Lsc, "Lsc")
    ```


<!-- sdd:class-diagram -->
## 클래스 관계

화살표의 글자는 추출한 관계를 나타내며, 점선은 상속입니다. 화살표는 참조 대상 또는 기반 클래스를 향합니다. 호출 순서를 뜻하지 않습니다.

```mermaid
flowchart LR
  c0["ipa::FrameContext"]:::context
  c1["ipa::LscAlgorithm"]
  c2["ipa::LscAlgorithmBase"]:::context
  c3["ipa::ipu3::Algorithm"]:::context
  c4["ipa::ipu3::IPAActiveState"]
  c5["ipa::ipu3::IPAContext"]
  c6["ipa::ipu3::IPAFrameContext"]
  c7["ipa::ipu3::algorithms::Lsc"]
  c8["ipa::lsc::ActiveState"]
  c9["ipa::lsc::FrameContext"]
  c1 -.->|상속| c2
  c4 -->|필드 참조| c8
  c5 -->|필드 참조| c4
  c6 -.->|상속| c0
  c6 -->|필드 참조| c9
  c7 -->|필드 참조| c1
  c7 -.->|상속| c3
  classDef context fill:#fafafa,stroke:#aaa,stroke-dasharray:4 3,color:#555
```
<!-- /sdd:class-diagram -->



## 관련 클래스

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::ipa::LscAlgorithm` | `src/ipa/libipa/lsc.h:78` | `libcamera::ipa::LscAlgorithmBase` | libIPA LSC algorithm implementation |
| `libcamera::ipa::ipu3::IPAActiveState` | `src/ipa/ipu3/ipa_context.h:46` | – | The active state of the IPA algorithms |
| `libcamera::ipa::ipu3::IPAContext` | `src/ipa/ipu3/ipa_context.h:73` | – | Global IPA context data shared between all algorithms |
| `libcamera::ipa::ipu3::IPAFrameContext` | `src/ipa/ipu3/ipa_context.h:60` | `libcamera::ipa::FrameContext` | IPU3-specific FrameContext |
| `libcamera::ipa::ipu3::algorithms::Lsc` | `src/ipa/ipu3/algorithms/lsc.h:21` | `libcamera::ipa::ipu3::Algorithm` | IPU3 Lens Shading Correction algorithm |
| `libcamera::ipa::lsc::ActiveState` | `src/ipa/libipa/lsc.h:27` | – | The LSC active state |
| `libcamera::ipa::lsc::FrameContext` | `src/ipa/libipa/lsc.h:31` | – | 확인 필요 |

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `src/ipa/ipu3/algorithms/lsc.cpp`, `src/ipa/ipu3/algorithms/lsc.h`, `src/ipa/ipu3/algorithms/meson.build`, `src/ipa/ipu3/ipa_context.h`, `src/ipa/libipa/lsc.h`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `2c4b67c079`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-25 · 사람 검토 전

다음 단계: [시스템 개요](overview.md)
