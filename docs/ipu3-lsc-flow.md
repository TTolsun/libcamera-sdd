---
generated_at: 2026-11-11 20:17:55+00:00
source_commit: da6a6ed33ed0ab305f10b6f8b44736150d39cef4
status: ok
section: ipu3-lsc-flow
generation_method: facts-and-llm
evidence_fingerprint: 0fddb0ddec2becb67e4ebd17672ab4cfae27fcfb27b95ff8f1e640d60f45a84a
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design:
  schema: 1
  input_fingerprint: 0fddb0ddec2becb67e4ebd17672ab4cfae27fcfb27b95ff8f1e640d60f45a84a
  answers:
    integration:
    - text: Meson의 `ipu3_ipa_algorithms` 목록은 `lsc.cpp`를 빌드 입력에 포함하며, 이 파일은 `Lsc` 클래스를
        IPU3 렌즈 음영 보정 알고리즘으로 소개합니다.
      evidence:
      - build
      - lsc-identity
      covers:
      - integration
      kind: behavior
      quote: "ipu3_ipa_algorithms = files([\n    'af.cpp',\n    'agc.cpp',\n    'awb.cpp',\n\
        \    'blc.cpp',\n    'ccm.cpp',\n    'lsc.cpp',\n    'tone_mapping.cpp',\n\
        ])"
      part_id: build
    - text: '`IPAActiveState`의 `lsc` 필드는 `ipa::lsc::ActiveState` 타입으로 선언되어 있습니다.'
      evidence:
      - context
      covers:
      - integration
      kind: behavior
      quote: "agc::ActiveState agc;\n\tipa::awb::ActiveState awb;\n\tipa::ccm::ActiveState\
        \ ccm;\n\tipa::gamma::ActiveState gamma;\n\tipa::lsc::ActiveState lsc;\n};"
      part_id: active
    - text: '`IPAFrameContext`는 `FrameContext`를 상속하며, `lsc` 필드를 `ipa::lsc::FrameContext`
        타입으로 선언합니다.'
      evidence:
      - context
      covers:
      - integration
      kind: behavior
      quote: "agc::FrameContext agc;\n\tipa::awb::FrameContext awb;\n\tipa::ccm::FrameContext\
        \ ccm;\n\tipa::gamma::FrameContext gamma;\n\tipa::lsc::FrameContext lsc;\n\
        };"
      part_id: frame
    - text: '`IPAContext`의 `frameContexts` 필드 타입은 `FCQueue<IPAFrameContext>`입니다.'
      evidence:
      - context
      covers:
      - integration
      kind: behavior
      quote: FCQueue<IPAFrameContext> frameContexts;
      part_id: queue
    setup:
    - text: '`Lsc::init()`은 센서 `activeArea`의 너비와 높이를 사용하고, 최대 가로 73개와 세로 56개 셀을 기준으로
        각 방향의 셀 크기를 올림 나눗셈으로 구합니다. 이어서 `std::bit_ceil`로 셀 크기를 2의 거듭제곱으로 올리고, 이미지 크기를
        이 셀 크기로 올림 나누어 셀 수를 정합니다. 각 블록 크기의 로그 값은 해당 셀 크기의 `std::bit_width`에서 1을 빼서
        구합니다.'
      evidence:
      - setup
      covers:
      - setup
      kind: behavior
      quote: "unsigned int cellWidth = (sensorWidth_ + kMaxNumHCells - 1) / kMaxNumHCells;\n\
        \tunsigned int cellHeight = (sensorHeight_ + kMaxNumVCells - 1) / kMaxNumVCells;"
    - text: '`Lsc::init()`은 튜닝 데이터의 `type`이 `polynomial`인지 저장합니다. 이어서 공통 알고리즘의 `lscAlgo_.init()`에
        튜닝 데이터, `context.ctrlMap`, 채널 키 `r`, `gr`, `gb`, `b`, 계산한 가로·세로 샘플 수와 센서 `activeArea`
        크기를 전달하고 그 반환값을 반환합니다.'
      evidence:
      - setup
      covers:
      - setup
      kind: behavior
      quote: "return lscAlgo_.init(tuningData, context.ctrlMap,\n\t\t\t     { .keys\
        \ = { \"r\", \"gr\", \"gb\", \"b\" },\n\t\t\t       .numHSamples = numHCells_,\n\
        \t\t\t       .numVSamples = numVCells_,\n\t\t\t       .sensorSize = context.sensorInfo.activeArea.size()\
        \ });\n}"
    - text: '`Lsc::configure()`는 `analogCrop`의 너비와 높이를 저장하고, 가로와 세로 셀 수를 각각 `calculatePositions()`에
        전달합니다. `calculatePositions()`는 각 차원에서 인덱스 `i`를 `dimension - 1`로 나눈 위치 배열을
        반환합니다. 이어서 `Lsc::configure()`는 LSC 활성 상태, `analogCrop`, 두 위치 배열을 `lscAlgo_.configure()`에
        전달하고 그 반환값을 반환합니다.'
      evidence:
      - setup
      covers:
      - setup
      kind: behavior
      quote: "/**\n * \\copydoc libcamera::ipa::Algorithm::configure\n */\nint Lsc::configure(IPAContext\
        \ &context, const IPAConfigInfo &configInfo)\n{\n\tcropWidth_ = configInfo.sensorInfo.analogCrop.width;\n\
        \tcropHeight_ = configInfo.sensorInfo.analogCrop.height;\n\tstd::vector<double>\
        \ xPos = calculatePositions(numHCells_);\n\tstd::vector<double> yPos = calculatePositions(numVCells_);"
    request:
    - text: '`Lsc::queueRequest()`는 첫 프레임에서 `LensShadingCorrectionEnable` 제어가 없으면
        `frameContext.lsc.enabled`와 `frameContext.lsc.update`에 모두 `true`를 씁니다.'
      evidence:
      - request
      covers:
      - request
      kind: behavior
      quote: "void Lsc::queueRequest(IPAContext &context, const uint32_t frame,\n\t\
        \t       IPAFrameContext &frameContext,\n\t\t       const ControlList &controls)\n\
        {\n\t/*\n\t * The base algorithm defines the LensShadingCorrectionEnable control\n\
        \t * with a default value of true, but actually the IPU3 driver defaults\n\
        \t * it to off. If this is the first frame, check for the control, but if\n\
        \t * there isn't one, force it on to fulfil the advertised default.\n\t */\n\
        \tif (frame == 0) {\n\t\tconst auto &lscEnable = controls.get(controls::LensShadingCorrectionEnable);\n\
        \t\tif (!lscEnable) {\n\t\t\tframeContext.lsc.enabled = true;\n\t\t\tframeContext.lsc.update\
        \ = true;\n\t\t}\n\t}\n\n\tlscAlgo_.queueRequest(context.activeState.lsc,\
        \ frameContext.lsc, controls);\n}\n\nstatic unsigned int quantize("
      part_id: default
    - text: '`Lsc::queueRequest`는 `lscAlgo_`의 `queueRequest`를 호출하며, 첫 번째 인자로 `context.activeState.lsc`,
        두 번째 인자로 `frameContext.lsc`, 세 번째 인자로 `controls`를 전달합니다.'
      evidence:
      - delegate-call
      covers:
      - request
      kind: behavior
      quote: lscAlgo_.queueRequest(context.activeState.lsc, frameContext.lsc, controls);
      part_id: delegate
    metadata:
    - text: '`Lsc::process()`는 `frameContext.lsc`와 `metadata`를 `lscAlgo_.process()`에
        전달합니다. 래퍼는 `stats`를 직접 사용하지 않습니다.'
      evidence:
      - process
      covers:
      - metadata
      kind: behavior
      quote: "void Lsc::process([[maybe_unused]] IPAContext &context,\n\t\t  [[maybe_unused]]\
        \ const uint32_t frame,\n\t\t  IPAFrameContext &frameContext,\n\t\t  [[maybe_unused]]\
        \ const ipu3_uapi_stats_3a *stats,\n\t\t  ControlList &metadata)\n{\n\tlscAlgo_.process(frameContext.lsc,\
        \ metadata);\n}"
    - text: 파일 끝의 `REGISTER_IPA_ALGORITHM(Lsc, "Lsc")`는 `Lsc` 알고리즘을 `"Lsc"`라는 이름으로
        등록합니다.
      evidence:
      - process
      covers:
      - metadata
      kind: behavior
      quote: REGISTER_IPA_ALGORITHM(Lsc, "Lsc")
  topic_inputs:
    integration: 62e2a1e9e429e0dd37181eff201a9bebf86b29e91824d047184951f9cb7d7ac1
    setup: b2e920d9b86f0ed6c4c9e00b4b98983f23d34508c8393105b0572a3302391252
    request: 0672dc17291bac0b76c87e1f8e2fd994593e3b7e7dd07763fc47e364735c3dbc
    metadata: 6771d3244b95b6be86103cf131cddca7e66a4da758e55d67279a8e1998a2ae45
  reused_topics:
  - integration
  - setup
  - request
  - metadata
  replayed_units: []
  generated_topics: []
  topic_agents:
    integration: cli/codex/gpt-6.1-terra
    setup: cli/codex/gpt-6.1-terra
    request: cli/codex/gpt-6.1-terra
    metadata: cli/codex/gpt-6.1-terra
  grounding_review: passed
  grounding_policy: 3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2
  validation_policy:
    manuscript: 367d18b95f8f0d01a15ae0f4d1b70f7e13e4d0298df4215e2c449ac4905db6f9
    semantic: 571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968
    duplicates: 93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38
    design_contracts: 9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0
    validate: 78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372
    reader_profiles: ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797
    contract_schema: d0f7ab4c48fcf52409935931eb9b93aacd48af4b19e9bb816fa496f1214fdb2f
    answer_contracts: a39c9a8818afc47e059141d486337c0f12a7fd34319e2b6f7674fc428bc83e2b
    reader_scope: 1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782
    product_context: 050c20aa2fdcceae10c6275fbb5f850f616ab5051bb67ccbcb4a204877a238d9
    explanation: 69bcaa207ef39d20f6a47ac201c3edf119f59b333e85131dea1bce85eef4006b
    design_response: a7c199bc52bcc0e749ef01186e50bca98107473d5c82e2248712f465d02e1e69
    design_validation: 92ddb9a65c909173ff4c7cb627dff83e71c10c8258c51344ef0eb1a7a023937f
  validation_model: 0d1544a2ea90f295c2aed62fab60f29f7788e623a953b6f7d5089373b8b41d94
  style_policy:
    fluent-korean.md: ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975
    i-have-adhd.md: 3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9
    README.md: b87a84b1bc31079837dc4dc4527ce02c9dc2cbc3a26ff7e99e0872941d213995
  reuse_lineage:
    source_commit: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
    body_sha256: 2824965a209c92f996cc06f3f8c66e02c5e02200be41fd8ce8f838d78fe0c078
    topics:
    - integration
    - setup
    - request
    - metadata
    validation: current source, contract and editorial checks; human review pending
  body_sha256: 77378d5e3459f21b3a40df6787c29e7fa576ff38493ed1f94353f8946c785711
generated_visuals:
  schema: 1
  records:
    lsc-build-state-integration:
      input_fingerprint: 3da637d02ad500ec022b9059f3065e5ee9d9523f32fe13a7786cf9e5f842ac95
      draft:
        nodes:
        - id: build
          symbol: ipu3_ipa_algorithms
          label: ipu3_ipa_algorithms는 lsc.cpp를 빌드 입력으로 포함하지만, 이것만으로 요청의 LSC 활성화를 증명하지는
            않습니다.
          label_en: ipu3_ipa_algorithms includes lsc.cpp as a build input, but inclusion
            alone does not prove LSC is enabled for a request.
          shape: box
          quote_ids:
          - build:0
        - id: cpp
          symbol: cpp
          label: lsc.cpp는 빌드 목록에 포함된 소스 파일입니다.
          label_en: lsc.cpp is a source file included in the build list.
          shape: box
          quote_ids:
          - build:0
        - id: lsc
          symbol: Lsc
          label: Lsc는 IPU3 렌즈 셰이딩 보정 알고리즘입니다.
          label_en: Lsc is the IPU3 lens shading correction algorithm.
          shape: box
          quote_ids:
          - lsc-identity:0
        - id: queue
          symbol: Lsc::queueRequest
          label: Lsc::queueRequest는 IPAContext와 IPAFrameContext를 참조 인자로 받습니다.
          label_en: Lsc::queueRequest takes IPAContext and IPAFrameContext by reference.
          shape: process
          quote_ids:
          - lsc-queue:0
        - id: context
          symbol: IPAContext
          label: IPAContext는 IPAActiveState 타입의 activeState를 선언합니다.
          label_en: IPAContext declares activeState with type IPAActiveState.
          shape: box
          quote_ids:
          - context:7
          - context:8
        - id: active
          symbol: IPAActiveState
          label: IPAActiveState는 ipa::lsc::ActiveState 타입의 공유 lsc 상태를 선언합니다.
          label_en: IPAActiveState declares the shared lsc state with type ipa::lsc::ActiveState.
          shape: box
          quote_ids:
          - context:3
          - context:4
        - id: frame
          symbol: IPAFrameContext
          label: IPAFrameContext는 ipa::lsc::FrameContext 타입의 프레임 lsc 상태를 선언합니다.
          label_en: IPAFrameContext declares the frame lsc state with type ipa::lsc::FrameContext.
          shape: box
          quote_ids:
          - context:5
          - context:6
        edges:
        - from: build
          to: cpp
          label: ipu3_ipa_algorithms는 lsc.cpp를 빌드 입력으로 포함합니다.
          label_en: ipu3_ipa_algorithms includes lsc.cpp as a build input.
          condition_ref: always
          quote_ids:
          - build:0
        - from: cpp
          to: queue
          label: lsc.cpp에서 Lsc::queueRequest를 정의합니다.
          label_en: lsc.cpp defines Lsc::queueRequest.
          condition_ref: always
          quote_ids:
          - build:0
          - lsc-queue:0
        - from: lsc
          to: queue
          label: Lsc는 queueRequest 메서드를 선언합니다.
          label_en: Lsc declares the queueRequest method.
          condition_ref: always
          quote_ids:
          - lsc-api:0
          - lsc-queue:0
        - from: queue
          to: context
          label: Lsc::queueRequest는 IPAContext를 참조로 받습니다.
          label_en: Lsc::queueRequest takes IPAContext by reference.
          condition_ref: always
          quote_ids:
          - lsc-queue:0
        - from: queue
          to: frame
          label: Lsc::queueRequest는 IPAFrameContext를 참조로 받습니다.
          label_en: Lsc::queueRequest takes IPAFrameContext by reference.
          condition_ref: always
          quote_ids:
          - lsc-queue:0
        - from: context
          to: active
          label: IPAContext의 activeState는 IPAActiveState입니다.
          label_en: The activeState in IPAContext is an IPAActiveState.
          condition_ref: always
          quote_ids:
          - context:7
          - context:8
        - from: queue
          to: active
          label: Lsc::queueRequest는 context.activeState.lsc를 lscAlgo_에 전달합니다.
          label_en: Lsc::queueRequest passes context.activeState.lsc to lscAlgo_.
          condition_ref: always
          quote_ids:
          - lsc-queue:0
          - lsc-queue:1
          - context:3
          - context:4
          - context:8
        - from: frame
          to: queue
          label: Lsc::queueRequest는 frameContext.lsc를 lscAlgo_에 전달합니다.
          label_en: Lsc::queueRequest passes frameContext.lsc to lscAlgo_.
          condition_ref: always
          quote_ids:
          - lsc-queue:0
          - lsc-queue:1
          - context:5
          - context:6
      graph:
        id: lsc-build-state-integration
        topic: integration
        kind: ownership
        title: LSC 빌드와 메서드 상태 입력
        question: 빌드 목록의 lsc.cpp와 Lsc 메서드의 IPAContext·IPAFrameContext 입력, 공유 lsc 상태·프레임
          lsc 상태 선언은 어떻게 연결됩니까?
        condition_display: evidence
        nodes:
        - id: build
          label: ipu3_ipa_algorithms는 lsc.cpp를 빌드 입력으로 포함하지만, 이것만으로 요청의 LSC 활성화를 증명하지는
            않습니다.
          label_en: ipu3_ipa_algorithms includes lsc.cpp as a build input, but inclusion
            alone does not prove LSC is enabled for a request.
          shape: box
          evidence:
          - source: integration/build
            sha256: 5b34e175668b4fedb33a633567f049c2738f6368c3b4d8ac26d069e77add82c9
            quote: "ipu3_ipa_algorithms = files([\n    'af.cpp',\n    'agc.cpp',\n\
              \    'awb.cpp',\n    'blc.cpp',\n    'ccm.cpp',\n    'lsc.cpp',\n  \
              \  'tone_mapping.cpp',\n])"
        - id: cpp
          label: lsc.cpp는 빌드 목록에 포함된 소스 파일입니다.
          label_en: lsc.cpp is a source file included in the build list.
          shape: box
          evidence:
          - source: integration/build
            sha256: 5b34e175668b4fedb33a633567f049c2738f6368c3b4d8ac26d069e77add82c9
            quote: "ipu3_ipa_algorithms = files([\n    'af.cpp',\n    'agc.cpp',\n\
              \    'awb.cpp',\n    'blc.cpp',\n    'ccm.cpp',\n    'lsc.cpp',\n  \
              \  'tone_mapping.cpp',\n])"
        - id: lsc
          label: Lsc는 IPU3 렌즈 셰이딩 보정 알고리즘입니다.
          label_en: Lsc is the IPU3 lens shading correction algorithm.
          shape: box
          evidence:
          - source: integration/lsc-identity
            sha256: dc87ed5856cdb01479417f85ff58fd5c34081034ae381e3c01ca52c375ca4dfe
            quote: "\\class Lsc\n * \\brief IPU3 Lens Shading Correction algorithm\n\
              \ */"
        - id: queue
          label: Lsc::queueRequest는 IPAContext와 IPAFrameContext를 참조 인자로 받습니다.
          label_en: Lsc::queueRequest takes IPAContext and IPAFrameContext by reference.
          shape: box
          evidence:
          - source: integration/lsc-queue
            sha256: b1f8edb143aec40d4df054ceb5aae3957139b7127404bae65c85996a07801165
            quote: "void Lsc::queueRequest(IPAContext &context, const uint32_t frame,\n\
              \t\t       IPAFrameContext &frameContext,\n\t\t       const ControlList\
              \ &controls)\n{\n\t/*\n\t * The base algorithm defines the LensShadingCorrectionEnable\
              \ control\n\t * with a default value of true, but actually the IPU3\
              \ driver defaults\n\t * it to off. If this is the first frame, check\
              \ for the control, but if\n\t * there isn't one, force it on to fulfil\
              \ the advertised default.\n\t */\n\tif (frame == 0) {\n\t\tconst auto\
              \ &lscEnable = controls.get(controls::LensShadingCorrectionEnable);\n\
              \t\tif (!lscEnable) {\n\t\t\tframeContext.lsc.enabled = true;\n\t\t\t\
              frameContext.lsc.update = true;\n\t\t}\n\t}"
        - id: context
          label: IPAContext는 IPAActiveState 타입의 activeState를 선언합니다.
          label_en: IPAContext declares activeState with type IPAActiveState.
          shape: box
          evidence:
          - source: integration/context
            sha256: e373aff7c5b5e5f034637b3d9030b0fdef974614261025791afd6e3146b1108d
            quote: "struct IPAContext {\n\tIPAContext(unsigned int frameContextSize)\n\
              \t\t: frameContexts(frameContextSize)\n\t{\n\t}"
          - source: integration/context
            sha256: e373aff7c5b5e5f034637b3d9030b0fdef974614261025791afd6e3146b1108d
            quote: "IPASessionConfiguration configuration;\n\tIPACameraSensorInfo\
              \ sensorInfo;\n\tControlInfoMap sensorControls;\n\tIPAActiveState activeState;"
        - id: active
          label: IPAActiveState는 ipa::lsc::ActiveState 타입의 공유 lsc 상태를 선언합니다.
          label_en: IPAActiveState declares the shared lsc state with type ipa::lsc::ActiveState.
          shape: box
          evidence:
          - source: integration/context
            sha256: e373aff7c5b5e5f034637b3d9030b0fdef974614261025791afd6e3146b1108d
            quote: "struct IPAActiveState {\n\tstruct {\n\t\tuint32_t focus;\n\t\t\
              double maxVariance;\n\t\tbool stable;\n\t} af;"
          - source: integration/context
            sha256: e373aff7c5b5e5f034637b3d9030b0fdef974614261025791afd6e3146b1108d
            quote: "agc::ActiveState agc;\n\tipa::awb::ActiveState awb;\n\tipa::ccm::ActiveState\
              \ ccm;\n\tipa::gamma::ActiveState gamma;\n\tipa::lsc::ActiveState lsc;\n\
              };"
        - id: frame
          label: IPAFrameContext는 ipa::lsc::FrameContext 타입의 프레임 lsc 상태를 선언합니다.
          label_en: IPAFrameContext declares the frame lsc state with type ipa::lsc::FrameContext.
          shape: box
          evidence:
          - source: integration/context
            sha256: e373aff7c5b5e5f034637b3d9030b0fdef974614261025791afd6e3146b1108d
            quote: "struct IPAFrameContext : public FrameContext {\n\tstruct {\n\t\
              \tuint32_t exposure;\n\t\tdouble gain;\n\t} sensor;"
          - source: integration/context
            sha256: e373aff7c5b5e5f034637b3d9030b0fdef974614261025791afd6e3146b1108d
            quote: "agc::FrameContext agc;\n\tipa::awb::FrameContext awb;\n\tipa::ccm::FrameContext\
              \ ccm;\n\tipa::gamma::FrameContext gamma;\n\tipa::lsc::FrameContext\
              \ lsc;\n};"
        edges:
        - from: build
          to: cpp
          label: ipu3_ipa_algorithms는 lsc.cpp를 빌드 입력으로 포함합니다.
          label_en: ipu3_ipa_algorithms includes lsc.cpp as a build input.
          evidence:
          - source: integration/build
            sha256: 5b34e175668b4fedb33a633567f049c2738f6368c3b4d8ac26d069e77add82c9
            quote: "ipu3_ipa_algorithms = files([\n    'af.cpp',\n    'agc.cpp',\n\
              \    'awb.cpp',\n    'blc.cpp',\n    'ccm.cpp',\n    'lsc.cpp',\n  \
              \  'tone_mapping.cpp',\n])"
        - from: cpp
          to: queue
          label: lsc.cpp에서 Lsc::queueRequest를 정의합니다.
          label_en: lsc.cpp defines Lsc::queueRequest.
          evidence:
          - source: integration/build
            sha256: 5b34e175668b4fedb33a633567f049c2738f6368c3b4d8ac26d069e77add82c9
            quote: "ipu3_ipa_algorithms = files([\n    'af.cpp',\n    'agc.cpp',\n\
              \    'awb.cpp',\n    'blc.cpp',\n    'ccm.cpp',\n    'lsc.cpp',\n  \
              \  'tone_mapping.cpp',\n])"
          - source: integration/lsc-queue
            sha256: b1f8edb143aec40d4df054ceb5aae3957139b7127404bae65c85996a07801165
            quote: "void Lsc::queueRequest(IPAContext &context, const uint32_t frame,\n\
              \t\t       IPAFrameContext &frameContext,\n\t\t       const ControlList\
              \ &controls)\n{\n\t/*\n\t * The base algorithm defines the LensShadingCorrectionEnable\
              \ control\n\t * with a default value of true, but actually the IPU3\
              \ driver defaults\n\t * it to off. If this is the first frame, check\
              \ for the control, but if\n\t * there isn't one, force it on to fulfil\
              \ the advertised default.\n\t */\n\tif (frame == 0) {\n\t\tconst auto\
              \ &lscEnable = controls.get(controls::LensShadingCorrectionEnable);\n\
              \t\tif (!lscEnable) {\n\t\t\tframeContext.lsc.enabled = true;\n\t\t\t\
              frameContext.lsc.update = true;\n\t\t}\n\t}"
        - from: lsc
          to: queue
          label: Lsc는 queueRequest 메서드를 선언합니다.
          label_en: Lsc declares the queueRequest method.
          evidence:
          - source: integration/lsc-api
            sha256: 94a832d5031c9a3e51ddf0fd9811921872d9239c63cca648e3da06f9c62039d4
            quote: "class Lsc : public Algorithm\n{\npublic:\n\tint init(IPAContext\
              \ &context, const ValueNode &tuningData) override;\n\tvoid queueRequest(IPAContext\
              \ &context, const uint32_t frame,\n\t\t\t  IPAFrameContext &frameContext,\n\
              \t\t\t  const ControlList &controls) override;\n\tint configure(IPAContext\
              \ &context, const IPAConfigInfo &configInfo) override;\n\tvoid prepare(IPAContext\
              \ &context, const uint32_t frame,\n\t\t     IPAFrameContext &frameContext,\n\
              \t\t     ipu3_uapi_params *params) override;\n\tvoid process(IPAContext\
              \ &context, const uint32_t frame,\n\t\t     IPAFrameContext &frameContext,\n\
              \t\t     const ipu3_uapi_stats_3a *stats,\n\t\t     ControlList &metadata)\
              \ override;"
          - source: integration/lsc-queue
            sha256: b1f8edb143aec40d4df054ceb5aae3957139b7127404bae65c85996a07801165
            quote: "void Lsc::queueRequest(IPAContext &context, const uint32_t frame,\n\
              \t\t       IPAFrameContext &frameContext,\n\t\t       const ControlList\
              \ &controls)\n{\n\t/*\n\t * The base algorithm defines the LensShadingCorrectionEnable\
              \ control\n\t * with a default value of true, but actually the IPU3\
              \ driver defaults\n\t * it to off. If this is the first frame, check\
              \ for the control, but if\n\t * there isn't one, force it on to fulfil\
              \ the advertised default.\n\t */\n\tif (frame == 0) {\n\t\tconst auto\
              \ &lscEnable = controls.get(controls::LensShadingCorrectionEnable);\n\
              \t\tif (!lscEnable) {\n\t\t\tframeContext.lsc.enabled = true;\n\t\t\t\
              frameContext.lsc.update = true;\n\t\t}\n\t}"
        - from: queue
          to: context
          label: Lsc::queueRequest는 IPAContext를 참조로 받습니다.
          label_en: Lsc::queueRequest takes IPAContext by reference.
          evidence:
          - source: integration/lsc-queue
            sha256: b1f8edb143aec40d4df054ceb5aae3957139b7127404bae65c85996a07801165
            quote: "void Lsc::queueRequest(IPAContext &context, const uint32_t frame,\n\
              \t\t       IPAFrameContext &frameContext,\n\t\t       const ControlList\
              \ &controls)\n{\n\t/*\n\t * The base algorithm defines the LensShadingCorrectionEnable\
              \ control\n\t * with a default value of true, but actually the IPU3\
              \ driver defaults\n\t * it to off. If this is the first frame, check\
              \ for the control, but if\n\t * there isn't one, force it on to fulfil\
              \ the advertised default.\n\t */\n\tif (frame == 0) {\n\t\tconst auto\
              \ &lscEnable = controls.get(controls::LensShadingCorrectionEnable);\n\
              \t\tif (!lscEnable) {\n\t\t\tframeContext.lsc.enabled = true;\n\t\t\t\
              frameContext.lsc.update = true;\n\t\t}\n\t}"
        - from: queue
          to: frame
          label: Lsc::queueRequest는 IPAFrameContext를 참조로 받습니다.
          label_en: Lsc::queueRequest takes IPAFrameContext by reference.
          evidence:
          - source: integration/lsc-queue
            sha256: b1f8edb143aec40d4df054ceb5aae3957139b7127404bae65c85996a07801165
            quote: "void Lsc::queueRequest(IPAContext &context, const uint32_t frame,\n\
              \t\t       IPAFrameContext &frameContext,\n\t\t       const ControlList\
              \ &controls)\n{\n\t/*\n\t * The base algorithm defines the LensShadingCorrectionEnable\
              \ control\n\t * with a default value of true, but actually the IPU3\
              \ driver defaults\n\t * it to off. If this is the first frame, check\
              \ for the control, but if\n\t * there isn't one, force it on to fulfil\
              \ the advertised default.\n\t */\n\tif (frame == 0) {\n\t\tconst auto\
              \ &lscEnable = controls.get(controls::LensShadingCorrectionEnable);\n\
              \t\tif (!lscEnable) {\n\t\t\tframeContext.lsc.enabled = true;\n\t\t\t\
              frameContext.lsc.update = true;\n\t\t}\n\t}"
        - from: context
          to: active
          label: IPAContext의 activeState는 IPAActiveState입니다.
          label_en: The activeState in IPAContext is an IPAActiveState.
          evidence:
          - source: integration/context
            sha256: e373aff7c5b5e5f034637b3d9030b0fdef974614261025791afd6e3146b1108d
            quote: "struct IPAContext {\n\tIPAContext(unsigned int frameContextSize)\n\
              \t\t: frameContexts(frameContextSize)\n\t{\n\t}"
          - source: integration/context
            sha256: e373aff7c5b5e5f034637b3d9030b0fdef974614261025791afd6e3146b1108d
            quote: "IPASessionConfiguration configuration;\n\tIPACameraSensorInfo\
              \ sensorInfo;\n\tControlInfoMap sensorControls;\n\tIPAActiveState activeState;"
        - from: queue
          to: active
          label: Lsc::queueRequest는 context.activeState.lsc를 lscAlgo_에 전달합니다.
          label_en: Lsc::queueRequest passes context.activeState.lsc to lscAlgo_.
          evidence:
          - source: integration/lsc-queue
            sha256: b1f8edb143aec40d4df054ceb5aae3957139b7127404bae65c85996a07801165
            quote: "void Lsc::queueRequest(IPAContext &context, const uint32_t frame,\n\
              \t\t       IPAFrameContext &frameContext,\n\t\t       const ControlList\
              \ &controls)\n{\n\t/*\n\t * The base algorithm defines the LensShadingCorrectionEnable\
              \ control\n\t * with a default value of true, but actually the IPU3\
              \ driver defaults\n\t * it to off. If this is the first frame, check\
              \ for the control, but if\n\t * there isn't one, force it on to fulfil\
              \ the advertised default.\n\t */\n\tif (frame == 0) {\n\t\tconst auto\
              \ &lscEnable = controls.get(controls::LensShadingCorrectionEnable);\n\
              \t\tif (!lscEnable) {\n\t\t\tframeContext.lsc.enabled = true;\n\t\t\t\
              frameContext.lsc.update = true;\n\t\t}\n\t}"
          - source: integration/lsc-queue
            sha256: b1f8edb143aec40d4df054ceb5aae3957139b7127404bae65c85996a07801165
            quote: 'lscAlgo_.queueRequest(context.activeState.lsc, frameContext.lsc,
              controls);

              }'
          - source: integration/context
            sha256: e373aff7c5b5e5f034637b3d9030b0fdef974614261025791afd6e3146b1108d
            quote: "struct IPAActiveState {\n\tstruct {\n\t\tuint32_t focus;\n\t\t\
              double maxVariance;\n\t\tbool stable;\n\t} af;"
          - source: integration/context
            sha256: e373aff7c5b5e5f034637b3d9030b0fdef974614261025791afd6e3146b1108d
            quote: "agc::ActiveState agc;\n\tipa::awb::ActiveState awb;\n\tipa::ccm::ActiveState\
              \ ccm;\n\tipa::gamma::ActiveState gamma;\n\tipa::lsc::ActiveState lsc;\n\
              };"
          - source: integration/context
            sha256: e373aff7c5b5e5f034637b3d9030b0fdef974614261025791afd6e3146b1108d
            quote: "IPASessionConfiguration configuration;\n\tIPACameraSensorInfo\
              \ sensorInfo;\n\tControlInfoMap sensorControls;\n\tIPAActiveState activeState;"
        - from: frame
          to: queue
          label: Lsc::queueRequest는 frameContext.lsc를 lscAlgo_에 전달합니다.
          label_en: Lsc::queueRequest passes frameContext.lsc to lscAlgo_.
          evidence:
          - source: integration/lsc-queue
            sha256: b1f8edb143aec40d4df054ceb5aae3957139b7127404bae65c85996a07801165
            quote: "void Lsc::queueRequest(IPAContext &context, const uint32_t frame,\n\
              \t\t       IPAFrameContext &frameContext,\n\t\t       const ControlList\
              \ &controls)\n{\n\t/*\n\t * The base algorithm defines the LensShadingCorrectionEnable\
              \ control\n\t * with a default value of true, but actually the IPU3\
              \ driver defaults\n\t * it to off. If this is the first frame, check\
              \ for the control, but if\n\t * there isn't one, force it on to fulfil\
              \ the advertised default.\n\t */\n\tif (frame == 0) {\n\t\tconst auto\
              \ &lscEnable = controls.get(controls::LensShadingCorrectionEnable);\n\
              \t\tif (!lscEnable) {\n\t\t\tframeContext.lsc.enabled = true;\n\t\t\t\
              frameContext.lsc.update = true;\n\t\t}\n\t}"
          - source: integration/lsc-queue
            sha256: b1f8edb143aec40d4df054ceb5aae3957139b7127404bae65c85996a07801165
            quote: 'lscAlgo_.queueRequest(context.activeState.lsc, frameContext.lsc,
              controls);

              }'
          - source: integration/context
            sha256: e373aff7c5b5e5f034637b3d9030b0fdef974614261025791afd6e3146b1108d
            quote: "struct IPAFrameContext : public FrameContext {\n\tstruct {\n\t\
              \tuint32_t exposure;\n\t\tdouble gain;\n\t} sensor;"
          - source: integration/context
            sha256: e373aff7c5b5e5f034637b3d9030b0fdef974614261025791afd6e3146b1108d
            quote: "agc::FrameContext agc;\n\tipa::awb::FrameContext awb;\n\tipa::ccm::FrameContext\
              \ ccm;\n\tipa::gamma::FrameContext gamma;\n\tipa::lsc::FrameContext\
              \ lsc;\n};"
        producer: cli/codex/gpt-6.1-terra
      producer: cli/codex/gpt-6.1-terra
      generation_commit: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
      citation_binding_policy: identifier-and-guard-boundaries-v2
      reused: true
  body_sha256: 77378d5e3459f21b3a40df6787c29e7fa576ff38493ed1f94353f8946c785711
managed_visual_refresh:
- schema: 1
  source_commit: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
  original_manuscript_sha256: 15f7771d185149ad7f726e18b2fd71e240fe6c22b4a006531f8178e9f70f1815
  previous_body_sha256: 3be6af987e2552a25c466176ac256def12d2a7c1238d5f2953d7ee8f43638ad1
  body_sha256: 77378d5e3459f21b3a40df6787c29e7fa576ff38493ed1f94353f8946c785711
  visual_definitions_sha256: 75e4598f1076630009d3edf60709f39ee6aac33793b904f762895e83d8e7f147
  unchanged_native_records_sha256: 5ddce223ae0e7b220d5442b7bf9516a7311fdef7d2cfb601e05e1796ab132d58
  preserved_outside_body_sha256: 752366abad176448a93ff173408194cb91e5ea54a22753cfa62b2756f2e69030
  owned_edit_regions:
  - original_start_byte: 1869
    original_end_byte: 10485
    original_sha256: cf57dd6d85d521b29e56706b54a5b1568003f981b3cd5311dd1ddc3d3f6d0076
    replacement_sha256: cf57dd6d85d521b29e56706b54a5b1568003f981b3cd5311dd1ddc3d3f6d0076
    visual_ids:
    - lsc-build-state-integration
  - original_start_byte: 11354
    original_end_byte: 18679
    original_sha256: f43e5866b5b44f6c92c5707d416f31b026cb186d5fff5500930683df76ddf388
    replacement_sha256: 1f2357862da9d493b97155106ba1f03c7d8044c9df9a5328e22782ce28f4a3d1
    visual_ids:
    - item-setup
  - original_start_byte: 20096
    original_end_byte: 23448
    original_sha256: c2b91a0ca28cb095d7c40951a7e46ba925ea16ceed6dbf1530f0797067dc0976
    replacement_sha256: c2b91a0ca28cb095d7c40951a7e46ba925ea16ceed6dbf1530f0797067dc0976
    visual_ids:
    - lsc-request-input
  added_visuals: []
  scope: Configured figure reassembly only; figure authorship remains per visual
  new_inference: false
  semantic_approval: false
  human_review: unchanged
revalidated_from: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
---

# IPU3 LSC의 설정과 프레임 처리

**LSC를 수정할 때는 초기 그리드 설정, 요청별 활성화 상태, 색온도에 따른 파라미터 갱신 조건을 차례로 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 빌드와 상태 연결의 조건과 근거를 대조하세요. | [빌드와 상태 연결](#빌드와-상태-연결) |
| 초기화와 크롭 설정의 조건과 근거를 대조하세요. | [초기화와 크롭 설정](#초기화와-크롭-설정) |
| 첫 프레임과 요청별 제어의 조건과 근거를 대조하세요. | [첫 프레임과 요청별 제어](#첫-프레임과-요청별-제어) |
| <a id="파라미터-갱신-조건"></a>파라미터 갱신 조건의 조건과 근거를 대조하세요. | [IPU3 렌즈 보정 테이블 준비](ipu3-lsc-prepare.md#파라미터-갱신-조건) |
| 메타데이터와 확인 범위의 조건과 근거를 대조하세요. | [메타데이터와 확인 범위](#메타데이터와-확인-범위) |
| <a id="lsc-파라미터를-갱신하는-분기"></a>“LSC 파라미터를 갱신하는 분기” 그림을 확인하세요. | [IPU3 렌즈 보정 테이블 준비](ipu3-lsc-prepare.md#lsc-파라미터를-갱신하는-분기) |

## 빌드와 상태 연결

Meson의 `ipu3_ipa_algorithms` 목록은 `lsc.cpp`를 빌드 입력에 포함하며, 이 파일은 `Lsc` 클래스를 IPU3 렌즈 음영 보정 알고리즘으로 소개합니다. `IPAActiveState`의 `lsc` 필드는 `ipa::lsc::ActiveState` 타입으로 선언되어 있습니다. `IPAFrameContext`는 `FrameContext`를 상속하며, `lsc` 필드를 `ipa::lsc::FrameContext` 타입으로 선언합니다. `IPAContext`의 `frameContexts` 필드 타입은 `FCQueue<IPAFrameContext>`입니다. `src/ipa/ipu3/algorithms/meson.build:3`, `src/ipa/ipu3/algorithms/lsc.cpp:25`, `src/ipa/ipu3/ipa_context.h:32`

<!-- sdd:visual:lsc-build-state-integration -->
### LSC 빌드와 메서드 상태 입력

```mermaid
flowchart TB
%% sdd:translations {"IPAActiveState는 <br/>ipa::lsc::ActiveState <br/>타입의 공유 lsc 상태를 <br/>선언합니다.": "IPAActiveState declares the <br/>shared lsc state with type <br/>ipa::lsc::ActiveState.", "IPAContext는 IPAActiveState <br/>타입의 activeState를 <br/>선언합니다.": "IPAContext declares <br/>activeState with type <br/>IPAActiveState.", "IPAContext의 activeState는 <br/>IPAActiveState입니다.": "The activeState in <br/>IPAContext is an <br/>IPAActiveState.", "IPAFrameContext는 <br/>ipa::lsc::FrameContext <br/>타입의 프레임 lsc 상태를 <br/>선언합니다.": "IPAFrameContext declares <br/>the frame lsc state with <br/>type ipa::lsc::FrameContext.", "Lsc::queueRequest는 <br/>IPAContext를 참조로 <br/>받습니다.": "Lsc::queueRequest takes <br/>IPAContext by reference.", "Lsc::queueRequest는 <br/>IPAContext와 <br/>IPAFrameContext를 참조 <br/>인자로 받습니다.": "Lsc::queueRequest takes <br/>IPAContext and <br/>IPAFrameContext by <br/>reference.", "Lsc::queueRequest는 <br/>IPAFrameContext를 참조로 <br/>받습니다.": "Lsc::queueRequest takes <br/>IPAFrameContext by <br/>reference.", "Lsc::queueRequest는 <br/>context.activeState.lsc를 <br/>lscAlgo#95;에 전달합니다.": "Lsc::queueRequest passes <br/>context.activeState.lsc to <br/>lscAlgo#95;.", "Lsc::queueRequest는 <br/>frameContext.lsc를 <br/>lscAlgo#95;에 전달합니다.": "Lsc::queueRequest passes <br/>frameContext.lsc to <br/>lscAlgo#95;.", "Lsc는 IPU3 렌즈 셰이딩 보정 <br/>알고리즘입니다.": "Lsc is the IPU3 lens <br/>shading correction <br/>algorithm.", "Lsc는 queueRequest 메서드를 <br/>선언합니다.": "Lsc declares the <br/>queueRequest method.", "ipu3#95;ipa#95;algorithms는 <br/>lsc.cpp를 빌드 입력으로 <br/>포함하지만, 이것만으로 <br/>요청의 LSC 활성화를 <br/>증명하지는 않습니다.": "ipu3#95;ipa#95;algorithms <br/>includes lsc.cpp as a build <br/>input, but inclusion alone <br/>does not prove LSC is <br/>enabled for a request.", "ipu3#95;ipa#95;algorithms는 <br/>lsc.cpp를 빌드 입력으로 <br/>포함합니다.": "ipu3#95;ipa#95;algorithms <br/>includes lsc.cpp as a build <br/>input.", "lsc.cpp는 빌드 목록에 <br/>포함된 소스 파일입니다.": "lsc.cpp is a source file <br/>included in the build list.", "lsc.cpp에서 <br/>Lsc::queueRequest를 <br/>정의합니다.": "lsc.cpp defines <br/>Lsc::queueRequest."}
  v_build["ipu3#95;ipa#95;algorithms는 <br/>lsc.cpp를 빌드 입력으로 <br/>포함하지만, 이것만으로 <br/>요청의 LSC 활성화를 <br/>증명하지는 않습니다."]
  v_cpp["lsc.cpp는 빌드 목록에 <br/>포함된 소스 파일입니다."]
  v_lsc["Lsc는 IPU3 렌즈 셰이딩 보정 <br/>알고리즘입니다."]
  v_queue["Lsc::queueRequest는 <br/>IPAContext와 <br/>IPAFrameContext를 참조 <br/>인자로 받습니다."]
  v_context["IPAContext는 IPAActiveState <br/>타입의 activeState를 <br/>선언합니다."]
  v_active["IPAActiveState는 <br/>ipa::lsc::ActiveState <br/>타입의 공유 lsc 상태를 <br/>선언합니다."]
  v_frame["IPAFrameContext는 <br/>ipa::lsc::FrameContext <br/>타입의 프레임 lsc 상태를 <br/>선언합니다."]
  v_build -->|"ipu3#95;ipa#95;algorithms는 <br/>lsc.cpp를 빌드 입력으로 <br/>포함합니다."| v_cpp
  v_cpp -->|"lsc.cpp에서 <br/>Lsc::queueRequest를 <br/>정의합니다."| v_queue
  v_lsc -->|"Lsc는 queueRequest 메서드를 <br/>선언합니다."| v_queue
  v_queue -->|"Lsc::queueRequest는 <br/>IPAContext를 참조로 <br/>받습니다."| v_context
  v_queue -->|"Lsc::queueRequest는 <br/>IPAFrameContext를 참조로 <br/>받습니다."| v_frame
  v_context -->|"IPAContext의 activeState는 <br/>IPAActiveState입니다."| v_active
  v_queue -->|"Lsc::queueRequest는 <br/>context.activeState.lsc를 <br/>lscAlgo#95;에 전달합니다."| v_active
  v_frame -->|"Lsc::queueRequest는 <br/>frameContext.lsc를 <br/>lscAlgo#95;에 전달합니다."| v_queue
```

[Mermaid 원문](ipu3-lsc-flow.lsc-build-state-integration.mmd)

??? note "그림 근거와 확인 범위"
    빌드 목록의 lsc.cpp와 Lsc 메서드의 IPAContext·IPAFrameContext 입력, 공유 lsc 상태·프레임 lsc 상태 선언은 어떻게 연결됩니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="ipu3_ipa_algorithms includes lsc.cpp as a build input, but inclusion alone does not prove LSC is enabled for a request.">ipu3&#95;ipa&#95;algorithms는 lsc.cpp를 빌드 입력으로 포함하지만, 이것만으로 요청의 LSC 활성화를 증명하지는 않습니다.</span> | [src/ipa/ipu3/algorithms/meson.build:3](#source-914bc0dd95a64016) |
    | <span data-sdd-label-en="lsc.cpp is a source file included in the build list.">lsc.cpp는 빌드 목록에 포함된 소스 파일입니다.</span> | [src/ipa/ipu3/algorithms/meson.build:3](#source-914bc0dd95a64016) |
    | <span data-sdd-label-en="Lsc is the IPU3 lens shading correction algorithm.">Lsc는 IPU3 렌즈 셰이딩 보정 알고리즘입니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:25](#source-724bb41a4f6f5bae) |
    | <span data-sdd-label-en="Lsc::queueRequest takes IPAContext and IPAFrameContext by reference.">Lsc::queueRequest는 IPAContext와 IPAFrameContext를 참조 인자로 받습니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-fb65fafe64a3b61f) |
    | <span data-sdd-label-en="IPAContext declares activeState with type IPAActiveState.">IPAContext는 IPAActiveState 타입의 activeState를 선언합니다.</span> | [src/ipa/ipu3/ipa_context.h:32](#source-47a8aa55a4a846f4) |
    | <span data-sdd-label-en="IPAActiveState declares the shared lsc state with type ipa::lsc::ActiveState.">IPAActiveState는 ipa::lsc::ActiveState 타입의 공유 lsc 상태를 선언합니다.</span> | [src/ipa/ipu3/ipa_context.h:32](#source-47a8aa55a4a846f4) |
    | <span data-sdd-label-en="IPAFrameContext declares the frame lsc state with type ipa::lsc::FrameContext.">IPAFrameContext는 ipa::lsc::FrameContext 타입의 프레임 lsc 상태를 선언합니다.</span> | [src/ipa/ipu3/ipa_context.h:32](#source-47a8aa55a4a846f4) |
    | <span data-sdd-label-en="ipu3_ipa_algorithms includes lsc.cpp as a build input.">ipu3&#95;ipa&#95;algorithms는 lsc.cpp를 빌드 입력으로 포함합니다.</span> | [src/ipa/ipu3/algorithms/meson.build:3](#source-914bc0dd95a64016) |
    | <span data-sdd-label-en="lsc.cpp defines Lsc::queueRequest.">lsc.cpp에서 Lsc::queueRequest를 정의합니다.</span> | [src/ipa/ipu3/algorithms/meson.build:3](#source-914bc0dd95a64016) · [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-fb65fafe64a3b61f) |
    | <span data-sdd-label-en="Lsc declares the queueRequest method.">Lsc는 queueRequest 메서드를 선언합니다.</span> | [src/ipa/ipu3/algorithms/lsc.h:21](#source-1c0b8c6b923ea225) · [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-fb65fafe64a3b61f) |
    | <span data-sdd-label-en="Lsc::queueRequest takes IPAContext by reference.">Lsc::queueRequest는 IPAContext를 참조로 받습니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-fb65fafe64a3b61f) |
    | <span data-sdd-label-en="Lsc::queueRequest takes IPAFrameContext by reference.">Lsc::queueRequest는 IPAFrameContext를 참조로 받습니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-fb65fafe64a3b61f) |
    | <span data-sdd-label-en="The activeState in IPAContext is an IPAActiveState.">IPAContext의 activeState는 IPAActiveState입니다.</span> | [src/ipa/ipu3/ipa_context.h:32](#source-47a8aa55a4a846f4) |
    | <span data-sdd-label-en="Lsc::queueRequest passes context.activeState.lsc to lscAlgo_.">Lsc::queueRequest는 context.activeState.lsc를 lscAlgo&#95;에 전달합니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-fb65fafe64a3b61f) · [src/ipa/ipu3/ipa_context.h:32](#source-47a8aa55a4a846f4) |
    | <span data-sdd-label-en="Lsc::queueRequest passes frameContext.lsc to lscAlgo_.">Lsc::queueRequest는 frameContext.lsc를 lscAlgo&#95;에 전달합니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-fb65fafe64a3b61f) · [src/ipa/ipu3/ipa_context.h:32](#source-47a8aa55a4a846f4) |
<!-- /sdd:visual:lsc-build-state-integration -->

근거 원문: [src/ipa/ipu3/algorithms/meson.build:3](#source-914bc0dd95a64016) · [src/ipa/ipu3/ipa_context.h:32](#source-47a8aa55a4a846f4) · [src/ipa/ipu3/algorithms/lsc.cpp:25](#source-724bb41a4f6f5bae) · [src/ipa/ipu3/algorithms/lsc.h:21](#source-1c0b8c6b923ea225) · [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-fb65fafe64a3b61f)

## 초기화와 크롭 설정

`Lsc::init()`은 센서 `activeArea`의 너비와 높이를 사용하고, 최대 가로 73개와 세로 56개 셀을 기준으로 각 방향의 셀 크기를 올림 나눗셈으로 구합니다. 이어서 `std::bit_ceil`로 셀 크기를 2의 거듭제곱으로 올리고, 이미지 크기를 이 셀 크기로 올림 나누어 셀 수를 정합니다. 각 블록 크기의 로그 값은 해당 셀 크기의 `std::bit_width`에서 1을 빼서 구합니다. `src/ipa/ipu3/algorithms/lsc.cpp:31`

<!-- sdd:visual:item-setup -->
### 초기화와 크롭 설정의 관계와 경계

```mermaid
flowchart TB
%% sdd:translations {"Lsc의 init과 configure가 <br/>그리드의 셀 수를 공유합니다.": "Lsc init and configure use <br/>the same grid cell counts.", "configure에서 analogCrop의 <br/>너비와 높이를 먼저 <br/>저장합니다.": "configure first stores the <br/>width and height of <br/>analogCrop.", "init에서 센서 활성 영역의 <br/>너비와 높이를 읽습니다.": "init reads the width and <br/>height of the sensor active <br/>area.", "init의 처리입니다.": "This is the init path.", "가로 셀 수로 xPos를 <br/>구합니다. 각 위치는 i를 셀 <br/>수에서 1을 뺀 값으로 <br/>나눕니다.": "Compute xPos using the <br/>horizontal cell count. Each <br/>position is i divided by <br/>#40;the cell count minus one#41;.", "가로 위치 다음에 세로 <br/>위치를 구합니다.": "Compute the vertical <br/>positions after the <br/>horizontal ones.", "가로와 세로에 적용되는 식의 <br/>경계입니다.": "This formula boundary <br/>applies to both axes.", "계산한 셀 수를 전달합니다.": "Pass the computed cell <br/>counts.", "공통 configure에 활성 상태, <br/>analogCrop, xPos, yPos를 <br/>넘기고 그 반환값을 <br/>반환합니다.": "Pass active state, <br/>analogCrop, xPos and yPos <br/>to the common configure and <br/>return its result.", "두 위치 벡터와 analogCrop을 <br/>전달합니다.": "Pass both position vectors <br/>and analogCrop.", "두 축의 하한에 적용합니다.": "Round both lower bounds.", "별도 configure의 처리입니다.": "This is the separate <br/>configure path.", "셀 수가 0이면 반복하지 않고 <br/>1이면 식의 분모가 0입니다.": "A cell count of 0 skips the <br/>loop. A count of 1 gives a <br/>zero denominator.", "셀 수를 공통 init에 <br/>전달하고 그 반환값을 <br/>반환합니다.": "Pass the cell counts to the <br/>common init and return its <br/>result.", "셀 크기를 2의 거듭제곱으로 <br/>올림한 뒤 축별 셀 수를 <br/>계산합니다.": "Round cell sizes up to <br/>powers of two, then compute <br/>the cell count on each axis.", "이어서 세로 셀 수로 같은 <br/>방식의 yPos를 구합니다.": "Then compute yPos the same <br/>way using the vertical cell <br/>count.", "크롭 크기를 저장한 뒤 <br/>계산합니다.": "Compute after storing the <br/>crop size.", "활성 영역에서 셀 크기 <br/>하한을 구합니다.": "Compute the cell size lower <br/>bounds from the active area.", "활성 영역의 너비와 높이를 <br/>각각 최대 셀 수 73과 56으로 <br/>올림 나눗셈합니다.": "Ceiling-divide the active <br/>width by 73 and the active <br/>height by 56."}
  v_methods["Lsc의 init과 configure가 <br/>그리드의 셀 수를 공유합니다."]
  v_sensor["init에서 센서 활성 영역의 <br/>너비와 높이를 읽습니다."]
  v_minimum["활성 영역의 너비와 높이를 <br/>각각 최대 셀 수 73과 56으로 <br/>올림 나눗셈합니다."]
  v_grid["셀 크기를 2의 거듭제곱으로 <br/>올림한 뒤 축별 셀 수를 <br/>계산합니다."]
  v_init["셀 수를 공통 init에 <br/>전달하고 그 반환값을 <br/>반환합니다."]
  v_crop["configure에서 analogCrop의 <br/>너비와 높이를 먼저 <br/>저장합니다."]
  v_x["가로 셀 수로 xPos를 <br/>구합니다. 각 위치는 i를 셀 <br/>수에서 1을 뺀 값으로 <br/>나눕니다."]
  v_y["이어서 세로 셀 수로 같은 <br/>방식의 yPos를 구합니다."]
  v_formula-limit["셀 수가 0이면 반복하지 않고 <br/>1이면 식의 분모가 0입니다."]
  v_configure["공통 configure에 활성 상태, <br/>analogCrop, xPos, yPos를 <br/>넘기고 그 반환값을 <br/>반환합니다."]
  v_methods -->|"init의 처리입니다."| v_sensor
  v_sensor -->|"활성 영역에서 셀 크기 <br/>하한을 구합니다."| v_minimum
  v_minimum -->|"두 축의 하한에 적용합니다."| v_grid
  v_grid -->|"계산한 셀 수를 전달합니다."| v_init
  v_methods -->|"별도 configure의 처리입니다."| v_crop
  v_crop -->|"크롭 크기를 저장한 뒤 <br/>계산합니다."| v_x
  v_x -->|"가로 위치 다음에 세로 <br/>위치를 구합니다."| v_y
  v_x -->|"가로와 세로에 적용되는 식의 <br/>경계입니다."| v_formula-limit
  v_y -->|"두 위치 벡터와 analogCrop을 <br/>전달합니다."| v_configure
```

[Mermaid 원문](ipu3-lsc-flow.item-setup.mmd)

??? note "그림 근거와 확인 범위"
    센서 활성 영역과 셀 수 제한으로 그리드를 계산한 뒤 그 결과를 크롭 설정에 어떻게 전달하는가?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Lsc init and configure use the same grid cell counts.">Lsc의 init과 configure가 그리드의 셀 수를 공유합니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="init reads the width and height of the sensor active area.">init에서 센서 활성 영역의 너비와 높이를 읽습니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="Ceiling-divide the active width by 73 and the active height by 56.">활성 영역의 너비와 높이를 각각 최대 셀 수 73과 56으로 올림 나눗셈합니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="Round cell sizes up to powers of two, then compute the cell count on each axis.">셀 크기를 2의 거듭제곱으로 올림한 뒤 축별 셀 수를 계산합니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="Pass the cell counts to the common init and return its result.">셀 수를 공통 init에 전달하고 그 반환값을 반환합니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="configure first stores the width and height of analogCrop.">configure에서 analogCrop의 너비와 높이를 먼저 저장합니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="Compute xPos using the horizontal cell count. Each position is i divided by (the cell count minus one).">가로 셀 수로 xPos를 구합니다. 각 위치는 i를 셀 수에서 1을 뺀 값으로 나눕니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="Then compute yPos the same way using the vertical cell count.">이어서 세로 셀 수로 같은 방식의 yPos를 구합니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="A cell count of 0 skips the loop. A count of 1 gives a zero denominator.">셀 수가 0이면 반복하지 않고 1이면 식의 분모가 0입니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="Pass active state, analogCrop, xPos and yPos to the common configure and return its result.">공통 configure에 활성 상태, analogCrop, xPos, yPos를 넘기고 그 반환값을 반환합니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="This is the init path.">init의 처리입니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="Compute the cell size lower bounds from the active area.">활성 영역에서 셀 크기 하한을 구합니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="Round both lower bounds.">두 축의 하한에 적용합니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="Pass the computed cell counts.">계산한 셀 수를 전달합니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="This is the separate configure path.">별도 configure의 처리입니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="Compute after storing the crop size.">크롭 크기를 저장한 뒤 계산합니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="Compute the vertical positions after the horizontal ones.">가로 위치 다음에 세로 위치를 구합니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="This formula boundary applies to both axes.">가로와 세로에 적용되는 식의 경계입니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
    | <span data-sdd-label-en="Pass both position vectors and analogCrop.">두 위치 벡터와 analogCrop을 전달합니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb) |
<!-- /sdd:visual:item-setup -->

`Lsc::init()`은 튜닝 데이터의 `type`이 `polynomial`인지 저장합니다. 이어서 공통 알고리즘의 `lscAlgo_.init()`에 튜닝 데이터, `context.ctrlMap`, 채널 키 `r`, `gr`, `gb`, `b`, 계산한 가로·세로 샘플 수와 센서 `activeArea` 크기를 전달하고 그 반환값을 반환합니다. `src/ipa/ipu3/algorithms/lsc.cpp:31`

`Lsc::configure()`는 `analogCrop`의 너비와 높이를 저장하고, 가로와 세로 셀 수를 각각 `calculatePositions()`에 전달합니다. `calculatePositions()`는 각 차원에서 인덱스 `i`를 `dimension - 1`로 나눈 위치 배열을 반환합니다. 이어서 `Lsc::configure()`는 LSC 활성 상태, `analogCrop`, 두 위치 배열을 `lscAlgo_.configure()`에 전달하고 그 반환값을 반환합니다. `src/ipa/ipu3/algorithms/lsc.cpp:31`

근거 원문: [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb)

## 첫 프레임과 요청별 제어

`Lsc::queueRequest()`는 첫 프레임에서 `LensShadingCorrectionEnable` 제어가 없으면 `frameContext.lsc.enabled`와 `frameContext.lsc.update`에 모두 `true`를 씁니다. `Lsc::queueRequest`는 `lscAlgo_`의 `queueRequest`를 호출하며, 첫 번째 인자로 `context.activeState.lsc`, 두 번째 인자로 `frameContext.lsc`, 세 번째 인자로 `controls`를 전달합니다. `src/ipa/ipu3/algorithms/lsc.cpp:121`, `src/ipa/ipu3/algorithms/lsc.cpp:139`

<!-- sdd:visual:lsc-request-input -->
### 요청 제어가 프레임 상태에 반영되는 곳

```mermaid
flowchart TB
%% sdd:translations {"enabled#61;true, update#61;true": "enabled#61;true, update#61;true", "기본값 적용 후 전달": "Forward after applying <br/>default", "아니오": "No", "아니오: 공통 호출로 진행": "No: continue to the common <br/>call", "예": "Yes", "첫 프레임인가?": "First frame?", "활성 상태 <br/>context.activeState.lsc, <br/>프레임 상태 <br/>frameContext.lsc와 <br/>controls를 공통 LSC <br/>queueRequest#40;#41;에 전달합니다.": "Pass active state <br/>context.activeState.lsc, <br/>frame state <br/>frameContext.lsc, and <br/>controls to the common LSC <br/>queueRequest#40;#41;.", "활성화 제어가 없는가?": "Enable control absent?"}
  v_first{"첫 프레임인가?"}
  v_control{"활성화 제어가 없는가?"}
  v_default["enabled#61;true, update#61;true"]
  v_common["활성 상태 <br/>context.activeState.lsc, <br/>프레임 상태 <br/>frameContext.lsc와 <br/>controls를 공통 LSC <br/>queueRequest#40;#41;에 전달합니다."]
  v_first -->|"예"| v_control
  v_first -->|"아니오"| v_common
  v_control -->|"예"| v_default
  v_control -->|"아니오: 공통 호출로 진행"| v_common
  v_default -->|"기본값 적용 후 전달"| v_common
```

[Mermaid 원문](ipu3-lsc-flow.lsc-request-input.mmd)

??? note "그림 근거와 확인 범위"
    첫 프레임에서 활성화 제어가 없으면 광고한 기본값을 맞춥니다. 이후 공통 LSC 알고리즘에 요청 제어를 전달합니다.
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="First frame?">첫 프레임인가?</span> | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
    | <span data-sdd-label-en="Enable control absent?">활성화 제어가 없는가?</span> | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
    | <span data-sdd-label-en="enabled=true, update=true">enabled=true, update=true</span> | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
    | <span data-sdd-label-en="Pass active state context.activeState.lsc, frame state frameContext.lsc, and controls to the common LSC queueRequest().">활성 상태 context.activeState.lsc, 프레임 상태 frameContext.lsc와 controls를 공통 LSC queueRequest&#40;&#41;에 전달합니다.</span> | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
    | <span data-sdd-label-en="Yes">예</span> | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
    | <span data-sdd-label-en="No">아니오</span> | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
    | <span data-sdd-label-en="Yes">예</span> | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
    | <span data-sdd-label-en="No: continue to the common call">아니오: 공통 호출로 진행</span> | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
    | <span data-sdd-label-en="Forward after applying default">기본값 적용 후 전달</span> | [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) |
<!-- /sdd:visual:lsc-request-input -->

근거 원문: [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) · [src/ipa/ipu3/algorithms/lsc.cpp:139](#source-9a0c59def2673a45)

## 메타데이터와 확인 범위

`Lsc::process()`는 `frameContext.lsc`와 `metadata`를 `lscAlgo_.process()`에 전달합니다. 래퍼는 `stats`를 직접 사용하지 않습니다. 파일 끝의 `REGISTER_IPA_ALGORITHM(Lsc, "Lsc")`는 `Lsc` 알고리즘을 `"Lsc"`라는 이름으로 등록합니다. `src/ipa/ipu3/algorithms/lsc.cpp:282`

근거 원문: [src/ipa/ipu3/algorithms/lsc.cpp:282](#source-5e8cfeb51ea8c16a)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | LSC 구현 파일과 공유 상태 및 프레임별 상태는 어떻게 연결됩니까? | [빌드와 상태 연결](#빌드와-상태-연결) | 코드 근거와 설명 연결 |
    | 입력 크기에 따라 그리드와 크기 제한을 어떻게 결정합니까? | [초기화와 크롭 설정](#초기화와-크롭-설정) | 코드 근거와 설명 연결 |
    | 첫 프레임의 기본 활성화와 요청 제어는 어떤 데이터를 전달합니까? | [첫 프레임과 요청별 제어](#첫-프레임과-요청별-제어) | 코드 근거와 설명 연결 |
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

<a id="source-724bb41a4f6f5bae"></a>

??? note "소스 근거: src/ipa/ipu3/algorithms/lsc.cpp:25"
    `src/ipa/ipu3/algorithms/lsc.cpp:25`에서 시작하는 발췌입니다. 종료 줄은 27이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `dc87ed5856cdb01479417f85ff58fd5c34081034ae381e3c01ca52c375ca4dfe`
    
    ```text
    \class Lsc
     * \brief IPU3 Lens Shading Correction algorithm
     */
    ```

<a id="source-1c0b8c6b923ea225"></a>

??? note "소스 근거: src/ipa/ipu3/algorithms/lsc.h:21"
    `src/ipa/ipu3/algorithms/lsc.h:21`에서 시작하는 발췌입니다. 종료 줄은 56이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `94a832d5031c9a3e51ddf0fd9811921872d9239c63cca648e3da06f9c62039d4`
    
    ```text
    class Lsc : public Algorithm
    {
    public:
    	int init(IPAContext &context, const ValueNode &tuningData) override;
    	void queueRequest(IPAContext &context, const uint32_t frame,
    			  IPAFrameContext &frameContext,
    			  const ControlList &controls) override;
    	int configure(IPAContext &context, const IPAConfigInfo &configInfo) override;
    	void prepare(IPAContext &context, const uint32_t frame,
    		     IPAFrameContext &frameContext,
    		     ipu3_uapi_params *params) override;
    	void process(IPAContext &context, const uint32_t frame,
    		     IPAFrameContext &frameContext,
    		     const ipu3_uapi_stats_3a *stats,
    		     ControlList &metadata) override;
    
    private:
    	std::vector<double> calculatePositions(unsigned int dimension);
    
    	unsigned int numHCells_;
    	unsigned int numVCells_;
    	unsigned int blockWidthLog2_;
    	unsigned int blockHeightLog2_;
    
    	unsigned int lastAppliedCt_;
    	unsigned int lastAppliedQuantizedCt_;
    
    	unsigned int sensorWidth_;
    	unsigned int sensorHeight_;
    	unsigned int cropWidth_;
    	unsigned int cropHeight_;
    
    	bool polynomial_;
    
    	LscAlgorithm<UQ<2, 10>> lscAlgo_;
    };
    ```

<a id="source-fb65fafe64a3b61f"></a>

??? note "소스 근거: src/ipa/ipu3/algorithms/lsc.cpp:121"
    `src/ipa/ipu3/algorithms/lsc.cpp:121`에서 시작하는 발췌입니다. 종료 줄은 140이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `b1f8edb143aec40d4df054ceb5aae3957139b7127404bae65c85996a07801165`
    
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

<a id="source-9a0c59def2673a45"></a>

??? note "소스 근거: src/ipa/ipu3/algorithms/lsc.cpp:139"
    `src/ipa/ipu3/algorithms/lsc.cpp:139`에서 시작하는 발췌입니다. 종료 줄은 139이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `847c975cc42b6b3d3c9361d2d3d84501ee3b5fa6b9101e5158e8707299973a1f`
    
    ```text
    lscAlgo_.queueRequest(context.activeState.lsc, frameContext.lsc, controls);
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
| `libcamera::ipa::LscAlgorithm` | `src/ipa/libipa/lsc.h:79` | `libcamera::ipa::LscAlgorithmBase` | libIPA LSC algorithm implementation |
| `libcamera::ipa::ipu3::IPAActiveState` | `src/ipa/ipu3/ipa_context.h:46` | – | The active state of the IPA algorithms |
| `libcamera::ipa::ipu3::IPAContext` | `src/ipa/ipu3/ipa_context.h:73` | – | Global IPA context data shared between all algorithms |
| `libcamera::ipa::ipu3::IPAFrameContext` | `src/ipa/ipu3/ipa_context.h:60` | `libcamera::ipa::FrameContext` | IPU3-specific FrameContext |
| `libcamera::ipa::ipu3::algorithms::Lsc` | `src/ipa/ipu3/algorithms/lsc.h:21` | `libcamera::ipa::ipu3::Algorithm` | IPU3 Lens Shading Correction algorithm |
| `libcamera::ipa::lsc::ActiveState` | `src/ipa/libipa/lsc.h:28` | – | The LSC active state |
| `libcamera::ipa::lsc::FrameContext` | `src/ipa/libipa/lsc.h:32` | – | 확인 필요 |

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `src/ipa/ipu3/algorithms/lsc.cpp`, `src/ipa/ipu3/algorithms/lsc.h`, `src/ipa/ipu3/algorithms/meson.build`, `src/ipa/ipu3/ipa_context.h`, `src/ipa/libipa/lsc.h`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `c19d05128f`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-12 · 사람 검토 전

다음 단계: [IPU3 렌즈 보정 테이블 준비](ipu3-lsc-prepare.md)
