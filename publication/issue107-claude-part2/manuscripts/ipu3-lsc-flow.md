---
generated_at: 2026-10-27T23:01:29+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: ipu3-lsc-flow
generation_method: facts-and-llm
evidence_fingerprint: 5951e563c34787a5bf8e4224b9873d5b13a40acbf1a2e6164398faa95dfc098a
semantic_review: human-review-required
agent: cli/claude/claude-haiku-5-5
generated_design: {"schema": 1, "input_fingerprint": "5951e563c34787a5bf8e4224b9873d5b13a40acbf1a2e6164398faa95dfc098a", "answers": {"integration": [{"text": "src/ipa/ipu3/algorithms/meson.build에서 `ipu3_ipa_algorithms` 변수는 `files()` 호출로 `af.cpp`, `agc.cpp`, `awb.cpp`, `blc.cpp`, `ccm.cpp`, `lsc.cpp`, `tone_mapping.cpp` 일곱 개 파일을 목록에 담습니다. `lsc.cpp`는 이 빌드 파일 목록에 포함되어 있습니다. 다만 이 목록에 포함되었다는 사실만으로 런타임에서 LSC 알고리즘이 실제로 활성화되는지는 확인되지 않습니다.", "evidence": ["build"], "covers": ["integration"], "kind": "behavior", "quote": "ipu3_ipa_algorithms = files([\n    'af.cpp',\n    'agc.cpp',\n    'awb.cpp',\n    'blc.cpp',\n    'ccm.cpp',\n    'lsc.cpp',\n    'tone_mapping.cpp',\n])", "part_id": "build"}, {"text": "`IPAActiveState` 구조체의 `lsc` 필드는 `ipa::lsc::ActiveState` 타입으로 선언되어 있습니다. 이 소스는 선언된 타입만 보여 주므로, `lsc` 필드가 언제 갱신되는지나 어떤 동기화로 보호되는지는 이 소스만으로 확인할 수 없습니다.", "evidence": ["context"], "covers": ["integration"], "kind": "behavior", "quote": "agc::ActiveState agc;\n\tipa::awb::ActiveState awb;\n\tipa::ccm::ActiveState ccm;\n\tipa::gamma::ActiveState gamma;\n\tipa::lsc::ActiveState lsc;\n};", "part_id": "active"}, {"text": "`IPAFrameContext` 구조체의 `lsc` 필드는 `ipa::lsc::FrameContext` 타입으로 선언되어 있습니다. 이 선언은 포인터나 참조가 아닌 `ipa::lsc::FrameContext lsc;` 형태의 멤버 변수입니다.", "evidence": ["context"], "covers": ["integration"], "kind": "behavior", "quote": "agc::FrameContext agc;\n\tipa::awb::FrameContext awb;\n\tipa::ccm::FrameContext ccm;\n\tipa::gamma::FrameContext gamma;\n\tipa::lsc::FrameContext lsc;\n};", "part_id": "frame"}, {"text": "`IPAContext` 구조체의 `frameContexts` 필드는 `FCQueue<IPAFrameContext>` 타입으로 선언되어 있습니다. 이 타입 인자 `IPAFrameContext`는 `FrameContext`를 public으로 상속한 구조체로 정의되어 있습니다.", "evidence": ["context"], "covers": ["integration"], "kind": "behavior", "quote": "FCQueue<IPAFrameContext> frameContexts;", "part_id": "queue"}], "setup": [{"text": "`Lsc::init()`은 `context.sensorInfo.activeArea`의 `width`와 `height`를 읽어 각각 `sensorWidth_`와 `sensorHeight_`에 저장합니다.", "evidence": ["setup"], "covers": ["setup"], "kind": "behavior", "quote": "/**\n * \\copydoc libcamera::ipa::Algorithm::init\n */\nint Lsc::init(IPAContext &context, const ValueNode &tuningData)\n{\n\t/*\n\t * The IPU3 lens shading block expects a table of data that isn't of a\n\t * fixed size, but rather is configurable based on 4 parameters:\n\t *\n\t * block_width_log2:\tThe log2 of the horizontal pixel count per cell\n\t * block_height_log2:\tThe log2 of the vertical pixel count per cell\n\t * width:\t\tThe number of horizontal cells\n\t * height:\t\tThe number of vertical cells\n\t *\n\t * The constructed grid should be capable of covering the image, but\n\t * ideally won't extend past the edges of the image. Fixing either set\n\t * of parameters for the algorithm as a whole is likely to result in\n\t * suboptimal situations for some sensors, so let's determine them\n\t * programmatically instead.\n\t *\n\t * What we want is the densest possible grid that ideally doesn't extend\n\t * past the edges of the image at all. The maximum grid size is 73x56,\n\t * which gives us the lower bounds on cell size. Unfortunately we can\n\t * only specify sizes in powers of two, which can have the effect of\n\t * making the grid much more coarse. For example for a 2592x1944 input\n\t * image, 2592 / 73 = 35.5...which means we need to set blockWidthLog2\n\t * to 6 (I.E. 64) and have just 40.5 (or rather 41) cells horizontally.\n\t */\n\tsensorWidth_ = context.sensorInfo.activeArea.width;\n\tsensorHeight_ = context.sensorInfo.activeArea.height;"}, {"text": "`Lsc::init()`은 `cellWidth`를 `(sensorWidth_ + kMaxNumHCells - 1) / kMaxNumHCells`로, `cellHeight`를 `(sensorHeight_ + kMaxNumVCells - 1) / kMaxNumVCells`로 올림 나눗셈하여 계산합니다. 이 소스에서 `kMaxNumHCells`는 73, `kMaxNumVCells`는 56으로 정의되어 있습니다.", "evidence": ["setup"], "covers": ["setup"], "kind": "behavior", "quote": "unsigned int cellWidth = (sensorWidth_ + kMaxNumHCells - 1) / kMaxNumHCells;\n\tunsigned int cellHeight = (sensorHeight_ + kMaxNumVCells - 1) / kMaxNumVCells;"}, {"text": "`Lsc::init()`은 `minCellWidth`를 `std::bit_ceil(cellWidth)`로, `minCellHeight`를 `std::bit_ceil(cellHeight)`로 정합니다. 따라서 셀 크기는 계산된 값 이상인 가장 작은 2의 거듭제곱으로 정해집니다.", "evidence": ["setup"], "covers": ["setup"], "kind": "behavior", "quote": "unsigned int minCellWidth = std::bit_ceil(cellWidth);\n\tunsigned int minCellHeight = std::bit_ceil(cellHeight);"}, {"text": "`Lsc::init()`은 `numHCells_`를 `(sensorWidth_ + minCellWidth - 1) / minCellWidth`로, `numVCells_`를 `(sensorHeight_ + minCellHeight - 1) / minCellHeight`로 계산합니다. 이 소스 범위에는 `numHCells_`가 `kMaxNumHCells` 이하인지 확인하는 코드가 보이지 않으므로, 샘플 수 경계를 이 소스만으로 검증된 사실로 단정할 수 없습니다.", "evidence": ["setup"], "covers": ["setup"], "kind": "behavior", "quote": "numHCells_ = (sensorWidth_ + minCellWidth - 1) / minCellWidth;\n\tnumVCells_ = (sensorHeight_ + minCellHeight - 1) / minCellHeight;"}, {"text": "`Lsc::init()`은 `lscAlgo_.init()`에 `tuningData`, `context.ctrlMap`, 그리고 `keys`로 `r`, `gr`, `gb`, `b`를 담은 설정값을 전달합니다. 이 설정에는 `numHSamples`로 `numHCells_`, `numVSamples`로 `numVCells_`, `sensorSize`로 `context.sensorInfo.activeArea.size()`가 들어가며, `Lsc::init()`은 이 호출의 반환값을 그대로 반환합니다.", "evidence": ["setup"], "covers": ["setup"], "kind": "behavior", "quote": "return lscAlgo_.init(tuningData, context.ctrlMap,\n\t\t\t     { .keys = { \"r\", \"gr\", \"gb\", \"b\" },\n\t\t\t       .numHSamples = numHCells_,\n\t\t\t       .numVSamples = numVCells_,\n\t\t\t       .sensorSize = context.sensorInfo.activeArea.size() });\n}"}, {"text": "`Lsc::configure()`은 `configInfo.sensorInfo.analogCrop`의 `width`와 `height`를 각각 `cropWidth_`와 `cropHeight_`에 저장합니다. 같은 함수는 `calculatePositions(numHCells_)`로 `xPos`를, `calculatePositions(numVCells_)`로 `yPos`를 구합니다. 이 소스 범위에서는 `cropWidth_`와 `cropHeight_`를 다시 읽는 코드가 보이지 않습니다.", "evidence": ["setup"], "covers": ["setup"], "kind": "behavior", "quote": "/**\n * \\copydoc libcamera::ipa::Algorithm::configure\n */\nint Lsc::configure(IPAContext &context, const IPAConfigInfo &configInfo)\n{\n\tcropWidth_ = configInfo.sensorInfo.analogCrop.width;\n\tcropHeight_ = configInfo.sensorInfo.analogCrop.height;\n\tstd::vector<double> xPos = calculatePositions(numHCells_);\n\tstd::vector<double> yPos = calculatePositions(numVCells_);"}, {"text": "`Lsc::calculatePositions(dimension)`은 크기가 `dimension`인 `positions`를 만들고, `i`를 0.0부터 `dimension`보다 작을 때까지 1씩 늘리면서 `positions[i]`에 `i / (dimension - 1)`을 저장합니다. `dimension`이 2 이상이면 첫 값은 0, 마지막 값은 1입니다. 이 소스에는 `dimension`이 1인 경우를 따로 처리하는 분기가 보이지 않습니다.", "evidence": ["setup"], "covers": ["setup"], "kind": "behavior", "quote": "std::vector<double> Lsc::calculatePositions(unsigned int dimension)\n{\n\tstd::vector<double> positions(dimension);\n\tfor (double i = 0.0; i < dimension; i++)\n\t\tpositions[i] = i / (dimension - 1);"}, {"text": "`Lsc::configure()`은 `context.activeState.lsc`, `configInfo.sensorInfo.analogCrop`, `xPos`, `yPos`를 `lscAlgo_.configure()`에 전달하고, 그 반환값을 그대로 반환합니다. `xPos`와 `yPos`는 앞서 `calculatePositions()`가 반환한 샘플 위치입니다.", "evidence": ["setup"], "covers": ["setup"], "kind": "behavior", "quote": "return lscAlgo_.configure(context.activeState.lsc,\n\t\t\t\t  configInfo.sensorInfo.analogCrop, xPos, yPos);\n}"}], "request": [{"text": "`Lsc::queueRequest`는 `frame`이 0이고 `controls.get(controls::LensShadingCorrectionEnable)`의 결과가 없을 때(`!lscEnable`) `frameContext.lsc.enabled`에 `true`를 씁니다. 같은 조건에서 `frameContext.lsc.update`에도 `true`를 씁니다. 함수는 그 뒤 `lscAlgo_.queueRequest(context.activeState.lsc, frameContext.lsc, controls)`를 호출하며, 이 호출에 전달되는 `frameContext.lsc`에는 `enabled`에 쓰는 값이 이미 `true`로 설정되어 있습니다.", "evidence": ["request"], "covers": ["request"], "kind": "behavior", "quote": "void Lsc::queueRequest(IPAContext &context, const uint32_t frame,\n\t\t       IPAFrameContext &frameContext,\n\t\t       const ControlList &controls)\n{\n\t/*\n\t * The base algorithm defines the LensShadingCorrectionEnable control\n\t * with a default value of true, but actually the IPU3 driver defaults\n\t * it to off. If this is the first frame, check for the control, but if\n\t * there isn't one, force it on to fulfil the advertised default.\n\t */\n\tif (frame == 0) {\n\t\tconst auto &lscEnable = controls.get(controls::LensShadingCorrectionEnable);\n\t\tif (!lscEnable) {\n\t\t\tframeContext.lsc.enabled = true;\n\t\t\tframeContext.lsc.update = true;\n\t\t}\n\t}\n\n\tlscAlgo_.queueRequest(context.activeState.lsc, frameContext.lsc, controls);\n}\n\nstatic unsigned int quantize(", "part_id": "default"}, {"text": "`Lsc::queueRequest`는 `frame`이 `0`이고 `controls`에서 `controls::LensShadingCorrectionEnable`을 가져온 결과 `lscEnable`이 비어 있을 때에만 `frameContext.lsc.update`에 `true`를 씁니다. 이 값은 같은 분기에서 `frameContext.lsc.enabled`를 `true`로 설정할 때 함께 쓰이며, 이 분기 밖에서는 이 코드가 `update`를 설정하지 않습니다.", "evidence": ["request"], "covers": ["request"], "kind": "behavior", "quote": "void Lsc::queueRequest(IPAContext &context, const uint32_t frame,\n\t\t       IPAFrameContext &frameContext,\n\t\t       const ControlList &controls)\n{\n\t/*\n\t * The base algorithm defines the LensShadingCorrectionEnable control\n\t * with a default value of true, but actually the IPU3 driver defaults\n\t * it to off. If this is the first frame, check for the control, but if\n\t * there isn't one, force it on to fulfil the advertised default.\n\t */\n\tif (frame == 0) {\n\t\tconst auto &lscEnable = controls.get(controls::LensShadingCorrectionEnable);\n\t\tif (!lscEnable) {\n\t\t\tframeContext.lsc.enabled = true;\n\t\t\tframeContext.lsc.update = true;\n\t\t}\n\t}\n\n\tlscAlgo_.queueRequest(context.activeState.lsc, frameContext.lsc, controls);\n}\n\nstatic unsigned int quantize(", "part_id": "default-update"}, {"text": "`Lsc::queueRequest` 함수는 `lscAlgo_` 객체의 `queueRequest` 메서드를 호출합니다.", "evidence": ["delegate-call"], "covers": ["request"], "kind": "behavior", "quote": "lscAlgo_.queueRequest(context.activeState.lsc, frameContext.lsc, controls);", "part_id": "delegate"}, {"text": "`Lsc::queueRequest()`에서 `lscAlgo_.queueRequest()`를 호출할 때 첫 번째 인자 `context.activeState.lsc`는 `context` 객체의 `activeState` 멤버 아래에 있는 `lsc` 값을 전달합니다. 즉, 현재 활성 상태(`activeState`)에 저장된 LSC 관련 상태를 `lscAlgo_`의 `queueRequest()`에 넘겨 처리하도록 합니다.", "evidence": ["delegate-call"], "covers": ["request"], "kind": "behavior", "quote": "lscAlgo_.queueRequest(context.activeState.lsc, frameContext.lsc, controls);", "part_id": "shared-argument"}, {"text": "`Lsc::queueRequest` 함수는 `lscAlgo_.queueRequest(context.activeState.lsc, frameContext.lsc, controls);`를 호출합니다. 이 호출의 두 번째 인자는 `frameContext.lsc`입니다. 첫 번째 인자는 `context.activeState.lsc`이고 세 번째 인자는 `controls`입니다. 두 번째 인자는 `frameContext` 객체의 `lsc` 멤버를 그대로 전달하는 표현입니다. 이 발췌에는 `lscAlgo_.queueRequest`의 매개변수 정의가 없으므로, 호출된 쪽이 이 값을 어떻게 사용하는지는 확인되지 않습니다.", "evidence": ["delegate-call"], "covers": ["request"], "kind": "behavior", "quote": "lscAlgo_.queueRequest(context.activeState.lsc, frameContext.lsc, controls);", "part_id": "frame-argument"}, {"text": "`Lsc::queueRequest`는 `lscAlgo_.queueRequest` 호출의 세 번째 인자로 `controls` 식별자를 그대로 전달합니다. 인용된 원문에는 `controls`의 선언이나 타입이 없으므로, 그 값이 무엇인지는 이 원문만으로 확인할 수 없습니다.", "evidence": ["delegate-call"], "covers": ["request"], "kind": "behavior", "quote": "lscAlgo_.queueRequest(context.activeState.lsc, frameContext.lsc, controls);", "part_id": "controls-argument"}], "prepare": [{"text": "`Lsc::prepare`는 `frameContext.lsc.update`가 `false`이고 그 안의 `frameContext.lsc.enabled`도 `false`이면 `return`으로 함수를 바로 종료합니다. 이 분기는 `params->use.acc_shd = 1` 설정과 `config` 값 기록보다 앞에서 실행되므로, 커널 드라이버가 userspace의 LSC 파라미터를 읽도록 하는 설정이 이루어지지 않습니다. `ct`와 `quantizedCt`는 이 분기 앞에서 이미 계산되지만, `lastAppliedCt_`와 `lastAppliedQuantizedCt_`는 함수 끝에서 갱신되므로 이 분기에서는 갱신되지 않습니다.", "evidence": ["prepare"], "covers": ["prepare"], "kind": "behavior", "quote": "if (!frameContext.lsc.update) {\n\t\tif (!frameContext.lsc.enabled)\n\t\t\treturn;", "part_id": "disabled-no-update"}, {"text": "`Lsc::prepare()`에서 `frameContext.lsc.update`가 `false`이고 `frameContext.lsc.enabled`가 `true`이면, `utils::abs_diff(ct, lastAppliedCt_)`가 `kColourTemperatureQuantization / 2`보다 작을 때 `return`으로 함수를 빠져나갑니다. 여기서 `ct`는 `frameContext.awb.colourTemperature`에서 읽은 원래 색온도 값이며, 양자화된 `quantizedCt`와 구분됩니다. 이 조기 반환이 일어나면 `params`를 채우는 코드와 `lastAppliedCt_` 및 `lastAppliedQuantizedCt_`를 갱신하는 코드는 실행되지 않습니다.", "evidence": ["prepare", "constants"], "covers": ["prepare"], "kind": "behavior", "quote": "/*\n\t\t * Add a threshold so that oscillations around a quantization\n\t\t * step don't lead to constant changes.\n\t\t */\n\t\tif (utils::abs_diff(ct, lastAppliedCt_) < kColourTemperatureQuantization / 2)\n\t\t\treturn;", "part_id": "ct-threshold"}, {"text": "`Lsc::prepare`에서 `frameContext.lsc.update`가 false이고 `frameContext.lsc.enabled`가 true이며 앞의 threshold 검사에서 반환되지 않은 경우, `quantizedCt`와 `lastAppliedQuantizedCt_`를 비교합니다. 두 값이 같으면 `return`으로 함수를 즉시 종료하므로 이후의 `params` 설정과 LUT 기록을 수행하지 않습니다. 두 값이 다르면 함수는 이어서 진행합니다.", "evidence": ["prepare"], "covers": ["prepare"], "kind": "behavior", "quote": "if (quantizedCt == lastAppliedQuantizedCt_)\n\t\t\treturn;\n\t}", "part_id": "quantized-same"}, {"text": "`Lsc::prepare`에서 `if (!frameContext.lsc.update)` 블록은 `update`가 false일 때만 들어갑니다. `update`가 true이면 이 블록을 건너뛰고 `params->use.acc_shd = 1;` 줄에 도달합니다. `update`가 false여도 `enabled`가 true이고, `utils::abs_diff(ct, lastAppliedCt_)`가 `kColourTemperatureQuantization / 2`보다 작지 않으며, `quantizedCt`가 `lastAppliedQuantizedCt_`와 다른 경우에는 세 early return에 걸리지 않아 이 줄에 도달합니다. 도달하면 `params->use.acc_shd`에 정수 `1`을 기록합니다. 소스 주석에 따르면 이 플래그는 커널 드라이버가 캐시된 복사본을 쓰지 않고, 사용자 공간에서 전달된 LSC 파라미터를 읽어야 함을 알려주는 역할을 합니다.", "evidence": ["prepare"], "covers": ["prepare"], "kind": "behavior", "quote": "/*\n\t * This flag tells the kernel driver that it should read the LSC params\n\t * passed from userspace instead of using its cached copy.\n\t */\n\tparams->use.acc_shd = 1;", "part_id": "upload"}, {"text": "`Lsc::prepare()`에서 `config->general.shd_enable`에 대입되는 값은 `frameContext.lsc.enabled`입니다. 인용된 코드에서 이 대입은 `if (!frameContext.lsc.enabled)` 검사와 `return`보다 앞에 있으므로, `enabled`가 `true`이든 `false`이든 인용된 범위에서는 대입이 먼저 실행됩니다. `enabled`가 `false`이면 `shd_enable`에 `false`가 대입된 뒤 `return`으로 함수를 빠져나갑니다. 다만 이 대입 앞에서 실행되는 코드는 제공된 발췌에 없으므로, 그 코드가 대입을 건너뛸 수 있는지는 확인이 필요합니다.", "evidence": ["enable-branch"], "covers": ["prepare"], "kind": "behavior", "quote": "config->general.shd_enable = frameContext.lsc.enabled;\n\n\tif (!frameContext.lsc.enabled)\n\t\treturn;", "part_id": "enable"}, {"text": "`config->general.shd_enable`에 `frameContext.lsc.enabled` 값을 대입합니다. 이후 `if (!frameContext.lsc.enabled)` 조건이 참이면, 즉 `enabled`가 false이면 `return`을 실행해 `Lsc::prepare()`에서 반환합니다. 이때 `shd_enable`에는 false가 대입된 상태입니다. `return`으로 함수가 즉시 종료되므로 이 분기 뒤의 `prepare()` 코드는 실행되지 않습니다.", "evidence": ["enable-branch"], "covers": ["prepare"], "kind": "behavior", "quote": "config->general.shd_enable = frameContext.lsc.enabled;\n\n\tif (!frameContext.lsc.enabled)\n\t\treturn;", "part_id": "disabled-exit"}, {"text": "`Lsc::prepare`는 `frameContext.lsc.enabled`가 거짓이면 `return`하므로, 그 뒤의 grid 설정은 활성 상태에서만 수행됩니다. 활성 경로에서는 `config->grid.width`에 `numHCells_`를, `config->grid.height`에 `numVCells_`를 넣습니다. `config->grid.block_width_log2`에는 `blockWidthLog2_`를, `config->grid.block_height_log2`에는 `blockHeightLog2_`를 넣습니다. `config->grid.grid_height_per_slice`는 `IPU3_UAPI_SHD_MAX_CELLS_PER_SET`을 `numHCells_`로 나눈 값으로 설정합니다.", "evidence": ["prepare"], "covers": ["prepare"], "kind": "behavior", "quote": "config->grid.width = numHCells_;\n\tconfig->grid.height = numVCells_;\n\tconfig->grid.block_width_log2 = blockWidthLog2_;\n\tconfig->grid.block_height_log2 = blockHeightLog2_;\n\tconfig->grid.grid_height_per_slice = IPU3_UAPI_SHD_MAX_CELLS_PER_SET / numHCells_;", "part_id": "grid"}, {"text": "`Lsc::prepare`에서 `frameContext.lsc.enabled`가 거짓이면 함수가 바로 반환되므로 그리드 설정은 실행되지 않습니다. 설정이 실행될 때 `polynomial_`이 참이면 `config->grid.x_start`와 `config->grid.y_start`를 모두 0으로 설정합니다. `polynomial_`이 거짓이면 `config->grid.x_start`는 `(cropWidth_ - sensorWidth_) / 2`, `config->grid.y_start`는 `(cropHeight_ - sensorHeight_) / 2`로 설정합니다.", "evidence": ["prepare"], "covers": ["prepare"], "kind": "behavior", "quote": "/*\n\t * The IPU3's documentation describes the x_start and y_start members\n\t * as follows:\n\t *\n\t * \"[X/Y] value of top left corner of sensor relative to ROI\n\t * s13, [-4096, 0], default 0, only negative values.\"\n\t *\n\t * I interpret that as allowing us to configure the cropped rectangle\n\t * relative to the full grid. That's useful if we're running the tabular\n\t * algorithm, which would otherwise apply the full grid inappropriately.\n\t * If we're running the polynomial one though the calculated grid is\n\t * probably more appropriate than a coarse application of the full grid\n\t * so let's tell the hardware not to bother correcting in that case.\n\t */\n\tif (polynomial_) {\n\t\tconfig->grid.x_start = 0;\n\t\tconfig->grid.y_start = 0;\n\t} else {\n\t\tconfig->grid.x_start = (cropWidth_ - sensorWidth_) / 2;\n\t\tconfig->grid.y_start = (cropHeight_ - sensorHeight_) / 2;\n\t}", "part_id": "crop"}, {"text": "`Lsc::prepare`는 `frameContext.lsc.enabled`가 참일 때 `config->general.gain_factor`에 `0`을 설정합니다. `enabled`가 거짓이면 `prepare`는 그 앞의 `return`에서 끝나므로 이 값을 설정하지 않습니다. 주석은 5.0을 넘는 gain이 드물다고 보아 `gain_factor`를 `0`으로 고정하고 필요하면 다시 검토한다고 적고 있습니다. 이 소스만으로는 실기기에서 주석의 해석을 확인했는지 알 수 없습니다.", "evidence": ["prepare"], "covers": ["prepare"], "kind": "behavior", "quote": "/*\n\t * Values in the LUT cease taking effect at 4096, and a value of 0.0 is\n\t * \"no correction\" rather than black. The gain factor is described by\n\t * the documentation like so:\n\t *\n\t * \"Shift calculated anti shading value. Precision u2. 0x0 - gain factor\n\t * [1, 5], means no shift interpolated value. 0x1 - gain factor [1, 9],\n\t * means shift interpolated by 1. 0x2 - gain factor [1, 17], means shift\n\t * interpolated by 2.\"\n\t *\n\t * The simplest interpretation for those pieces of information is I\n\t * think that the LUT stores 12-bit Q numbers who's represented values\n\t * depend on the gain_factor setting like so:\n\t *\n\t * 0: UQ<2, 10> representing values in range [0, 4)\n\t * 1: UQ<3, 9> representing values in range [0, 8)\n\t * 2: UQ<4, 8> representing values in range [0, 16)\n\t *\n\t * And that a base gain of 1.0 is added to those configured values. As a\n\t * gain of more than 5.0 is fairly unlikely, let's fix gain_factor to 0\n\t * for now and revisit if needed.\n\t */\n\tconfig->general.gain_factor = 0;", "part_id": "gain"}, {"text": "`Lsc::prepare`는 `config->black_level`의 `bl_r`, `bl_gr`, `bl_gb`, `bl_b` 색상 필드 네 개에 각각 `0`을 설정합니다. 이 원문에서 설정하는 값은 네 필드 모두 `0`입니다.", "evidence": ["black-levels"], "covers": ["prepare"], "kind": "behavior", "quote": "config->black_level.bl_r = 0;\n\tconfig->black_level.bl_gr = 0;\n\tconfig->black_level.bl_gb = 0;\n\tconfig->black_level.bl_b = 0;", "part_id": "black-level"}, {"text": "`Lsc::prepare()`는 `lscAlgo_.interpolateComponents()`를 호출할 때 색온도 값으로 `quantizedCt`를 전달합니다. 호출 결과는 `const auto &set`에 참조로 받습니다.", "evidence": ["interpolation"], "covers": ["prepare"], "kind": "behavior", "quote": "const auto &set = lscAlgo_.interpolateComponents(quantizedCt);", "part_id": "lut"}, {"text": "`Lsc::prepare()`에서 `lut->sets[s].r_and_gr[c].r`에는 `set.at(\"r\")[i]`를, `lut->sets[s].r_and_gr[c].gr`에는 `set.at(\"gr\")[i]`를 대입합니다. 또한 `lut->sets[s].gb_and_b[c].gb`에는 `set.at(\"gb\")[i]`를, `lut->sets[s].gb_and_b[c].b`에는 `set.at(\"b\")[i]`를 대입합니다. 즉 r과 gr 값은 같은 세트 항목의 `r_and_gr` 구조체에 함께 저장되고, gb와 b 값은 `gb_and_b` 구조체에 함께 저장됩니다.", "evidence": ["lut-writes"], "covers": ["prepare"], "kind": "behavior", "quote": "for (unsigned int s = 0; s < numSets; s++) {\n\t\tfor (unsigned int c = 0; c < cellsPerSet && i < totalCells; c++, i++) {\n\t\t\tlut->sets[s].r_and_gr[c].r = set.at(\"r\")[i];\n\t\t\tlut->sets[s].r_and_gr[c].gr = set.at(\"gr\")[i];\n\t\t\tlut->sets[s].gb_and_b[c].gb = set.at(\"gb\")[i];\n\t\t\tlut->sets[s].gb_and_b[c].b = set.at(\"b\")[i];\n\t\t}\n\t}\n\n\tlastAppliedCt_ = ct;", "part_id": "lut-channels"}, {"text": "`Lsc::prepare` 안에서 우변의 변수 `ct`가 좌변의 멤버 `lastAppliedCt_`에 대입됩니다. 이 대입문은 `prepare` 함수 범위 안에 있으며, 발췌문에서 확인되는 것은 이 대입 자체뿐입니다.", "evidence": ["stored-ct"], "covers": ["prepare"], "kind": "behavior", "quote": "lastAppliedCt_ = ct;", "part_id": "remember"}, {"text": "`Lsc::prepare()` 안의 `lastAppliedQuantizedCt_ = quantizedCt;` 대입문은 우변 식별자 `quantizedCt`의 값을 좌변 식별자 `lastAppliedQuantizedCt_`에 대입합니다. 이 발췌문에는 `lastAppliedQuantizedCt_`의 선언이 없으므로, 이 근거만으로는 해당 식별자가 멤버 변수인지 확인할 수 없습니다.", "evidence": ["stored-quantized-ct"], "covers": ["prepare"], "kind": "behavior", "quote": "lastAppliedQuantizedCt_ = quantizedCt;", "part_id": "remember-quantized"}], "metadata": [{"text": "`Lsc::process()`은 전달받은 `metadata` 인자를 `lscAlgo_.process()`의 두 번째 인자로 그대로 넘깁니다. 이때 첫 번째 인자로는 `frameContext.lsc`를 넘깁니다. 이 함수 본문에는 `metadata`에 값을 직접 쓰는 코드가 없습니다.", "evidence": ["process"], "covers": ["metadata"], "kind": "behavior", "quote": "void Lsc::process([[maybe_unused]] IPAContext &context,\n\t\t  [[maybe_unused]] const uint32_t frame,\n\t\t  IPAFrameContext &frameContext,\n\t\t  [[maybe_unused]] const ipu3_uapi_stats_3a *stats,\n\t\t  ControlList &metadata)\n{\n\tlscAlgo_.process(frameContext.lsc, metadata);\n}"}, {"text": "`lscAlgo_.process()` 내부에서 `metadata`에 어떤 값을 기록하는지와 처리 결과를 어떤 방식으로 알리는지는 제공된 소스에 나타나지 않습니다. 이 내용은 `lscAlgo_`의 구현 소스에서 확인해야 합니다.", "evidence": ["process"], "covers": ["metadata"], "kind": "limitation", "quote": "void Lsc::process([[maybe_unused]] IPAContext &context,\n\t\t  [[maybe_unused]] const uint32_t frame,\n\t\t  IPAFrameContext &frameContext,\n\t\t  [[maybe_unused]] const ipu3_uapi_stats_3a *stats,\n\t\t  ControlList &metadata)\n{\n\tlscAlgo_.process(frameContext.lsc, metadata);\n}"}]}, "topic_inputs": {"integration": "fb610a50a1c5a2849befb5c44eb987023111ca8770184de5e7be1142f274eabe", "setup": "ef020d2cbbf1421e6f866c406275dcbc5776068dac95caac823babbe302e25f7", "request": "b04c643e53f7330c736517b7f2ab6b281051b1ec1417f3795a62d0751ee79b61", "prepare": "a9367a756469892bc5e08245ca5f17cc0ba58ce7aa22f467c6e2badb792e8839", "metadata": "d4066f5b4aebd03c726d07dcb863a87c3d5a3602c822b20fc364e9375cd1f6ee"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["integration", "setup", "request", "prepare", "metadata"], "topic_agents": {"integration": "cli/claude/claude-haiku-5-5", "setup": "cli/claude/claude-haiku-5-5", "request": "cli/claude/claude-haiku-5-5", "prepare": "cli/claude/claude-haiku-5-5", "metadata": "cli/claude/claude-haiku-5-5"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "body_sha256": "0a5d6229b30fc1052a162ce3074c489584a974e34913efcd2b4a12cf445f09c8"}
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

src/ipa/ipu3/algorithms/meson.build에서 `ipu3_ipa_algorithms` 변수는 `files()` 호출로 `af.cpp`, `agc.cpp`, `awb.cpp`, `blc.cpp`, `ccm.cpp`, `lsc.cpp`, `tone_mapping.cpp` 일곱 개 파일을 목록에 담습니다. `lsc.cpp`는 이 빌드 파일 목록에 포함되어 있습니다. 다만 이 목록에 포함되었다는 사실만으로 런타임에서 LSC 알고리즘이 실제로 활성화되는지는 확인되지 않습니다. `src/ipa/ipu3/algorithms/meson.build:3`

`IPAActiveState` 구조체의 `lsc` 필드는 `ipa::lsc::ActiveState` 타입으로 선언되어 있습니다. 이 소스는 선언된 타입만 보여 주므로, `lsc` 필드가 언제 갱신되는지나 어떤 동기화로 보호되는지는 이 소스만으로 확인할 수 없습니다. `IPAFrameContext` 구조체의 `lsc` 필드는 `ipa::lsc::FrameContext` 타입으로 선언되어 있습니다. 이 선언은 포인터나 참조가 아닌 `ipa::lsc::FrameContext lsc;` 형태의 멤버 변수입니다. `src/ipa/ipu3/ipa_context.h:32`

`IPAContext` 구조체의 `frameContexts` 필드는 `FCQueue<IPAFrameContext>` 타입으로 선언되어 있습니다. 이 타입 인자 `IPAFrameContext`는 `FrameContext`를 public으로 상속한 구조체로 정의되어 있습니다. `src/ipa/ipu3/ipa_context.h:32`

근거 원문: [src/ipa/ipu3/algorithms/meson.build:3](#source-914bc0dd95a64016) · [src/ipa/ipu3/ipa_context.h:32](#source-47a8aa55a4a846f4)

## 초기화와 크롭 설정

`Lsc::init()`은 `context.sensorInfo.activeArea`의 `width`와 `height`를 읽어 각각 `sensorWidth_`와 `sensorHeight_`에 저장합니다. `Lsc::init()`은 `cellWidth`를 `(sensorWidth_ + kMaxNumHCells - 1) / kMaxNumHCells`로, `cellHeight`를 `(sensorHeight_ + kMaxNumVCells - 1) / kMaxNumVCells`로 올림 나눗셈하여 계산합니다. 이 소스에서 `kMaxNumHCells`는 73, `kMaxNumVCells`는 56으로 정의되어 있습니다. `src/ipa/ipu3/algorithms/lsc.cpp:31`

`Lsc::init()`은 `minCellWidth`를 `std::bit_ceil(cellWidth)`로, `minCellHeight`를 `std::bit_ceil(cellHeight)`로 정합니다. 따라서 셀 크기는 계산된 값 이상인 가장 작은 2의 거듭제곱으로 정해집니다. `Lsc::init()`은 `numHCells_`를 `(sensorWidth_ + minCellWidth - 1) / minCellWidth`로, `numVCells_`를 `(sensorHeight_ + minCellHeight - 1) / minCellHeight`로 계산합니다. 이 소스 범위에는 `numHCells_`가 `kMaxNumHCells` 이하인지 확인하는 코드가 보이지 않으므로, 샘플 수 경계를 이 소스만으로 검증된 사실로 단정할 수 없습니다. `src/ipa/ipu3/algorithms/lsc.cpp:31`

`Lsc::init()`은 `lscAlgo_.init()`에 `tuningData`, `context.ctrlMap`, 그리고 `keys`로 `r`, `gr`, `gb`, `b`를 담은 설정값을 전달합니다. 이 설정에는 `numHSamples`로 `numHCells_`, `numVSamples`로 `numVCells_`, `sensorSize`로 `context.sensorInfo.activeArea.size()`가 들어가며, `Lsc::init()`은 이 호출의 반환값을 그대로 반환합니다. `src/ipa/ipu3/algorithms/lsc.cpp:31`

`Lsc::configure()`은 `configInfo.sensorInfo.analogCrop`의 `width`와 `height`를 각각 `cropWidth_`와 `cropHeight_`에 저장합니다. 같은 함수는 `calculatePositions(numHCells_)`로 `xPos`를, `calculatePositions(numVCells_)`로 `yPos`를 구합니다. 이 소스 범위에서는 `cropWidth_`와 `cropHeight_`를 다시 읽는 코드가 보이지 않습니다. `src/ipa/ipu3/algorithms/lsc.cpp:31`

`Lsc::calculatePositions(dimension)`은 크기가 `dimension`인 `positions`를 만들고, `i`를 0.0부터 `dimension`보다 작을 때까지 1씩 늘리면서 `positions[i]`에 `i / (dimension - 1)`을 저장합니다. `dimension`이 2 이상이면 첫 값은 0, 마지막 값은 1입니다. 이 소스에는 `dimension`이 1인 경우를 따로 처리하는 분기가 보이지 않습니다. `src/ipa/ipu3/algorithms/lsc.cpp:31`

`Lsc::configure()`은 `context.activeState.lsc`, `configInfo.sensorInfo.analogCrop`, `xPos`, `yPos`를 `lscAlgo_.configure()`에 전달하고, 그 반환값을 그대로 반환합니다. `xPos`와 `yPos`는 앞서 `calculatePositions()`가 반환한 샘플 위치입니다. `src/ipa/ipu3/algorithms/lsc.cpp:31`

근거 원문: [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-441d18135ba28bdb)

## 첫 프레임과 요청별 제어

`Lsc::queueRequest`는 `frame`이 0이고 `controls.get(controls::LensShadingCorrectionEnable)`의 결과가 없을 때(`!lscEnable`) `frameContext.lsc.enabled`에 `true`를 씁니다. 같은 조건에서 `frameContext.lsc.update`에도 `true`를 씁니다. 함수는 그 뒤 `lscAlgo_.queueRequest(context.activeState.lsc, frameContext.lsc, controls)`를 호출하며, 이 호출에 전달되는 `frameContext.lsc`에는 `enabled`에 쓰는 값이 이미 `true`로 설정되어 있습니다. `src/ipa/ipu3/algorithms/lsc.cpp:121`

<!-- sdd:visual:lsc-request-input -->
### 요청 제어가 프레임 상태에 반영되는 곳

첫 프레임에서 활성화 제어가 없으면 광고한 기본값을 맞춥니다. 이후 공통 LSC 알고리즘에 요청 제어를 전달합니다.

```mermaid
flowchart TB
%% sdd:translations {"enabled=true, update=true": "enabled=true, update=true", "공통 LSC queueRequest()": "Common LSC queueRequest()", "기본값 적용 후 전달": "Forward after applying <br/>default", "아니오": "No", "아니오: 전달된 제어 사용": "No: use supplied control", "예": "Yes", "첫 프레임인가?": "First frame?", "활성화 제어가 없는가?": "Enable control absent?"}
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

`Lsc::queueRequest`는 `frame`이 `0`이고 `controls`에서 `controls::LensShadingCorrectionEnable`을 가져온 결과 `lscEnable`이 비어 있을 때에만 `frameContext.lsc.update`에 `true`를 씁니다. 이 값은 같은 분기에서 `frameContext.lsc.enabled`를 `true`로 설정할 때 함께 쓰이며, 이 분기 밖에서는 이 코드가 `update`를 설정하지 않습니다. `Lsc::queueRequest` 함수는 `lscAlgo_` 객체의 `queueRequest` 메서드를 호출합니다. `src/ipa/ipu3/algorithms/lsc.cpp:121`, `src/ipa/ipu3/algorithms/lsc.cpp:139`

`Lsc::queueRequest()`에서 `lscAlgo_.queueRequest()`를 호출할 때 첫 번째 인자 `context.activeState.lsc`는 `context` 객체의 `activeState` 멤버 아래에 있는 `lsc` 값을 전달합니다. 즉, 현재 활성 상태(`activeState`)에 저장된 LSC 관련 상태를 `lscAlgo_`의 `queueRequest()`에 넘겨 처리하도록 합니다. `src/ipa/ipu3/algorithms/lsc.cpp:139`

`Lsc::queueRequest` 함수는 `lscAlgo_.queueRequest(context.activeState.lsc, frameContext.lsc, controls);`를 호출합니다. 이 호출의 두 번째 인자는 `frameContext.lsc`입니다. 첫 번째 인자는 `context.activeState.lsc`이고 세 번째 인자는 `controls`입니다. 두 번째 인자는 `frameContext` 객체의 `lsc` 멤버를 그대로 전달하는 표현입니다. 이 발췌에는 `lscAlgo_.queueRequest`의 매개변수 정의가 없으므로, 호출된 쪽이 이 값을 어떻게 사용하는지는 확인되지 않습니다. `src/ipa/ipu3/algorithms/lsc.cpp:139`

`Lsc::queueRequest`는 `lscAlgo_.queueRequest` 호출의 세 번째 인자로 `controls` 식별자를 그대로 전달합니다. 인용된 원문에는 `controls`의 선언이나 타입이 없으므로, 그 값이 무엇인지는 이 원문만으로 확인할 수 없습니다. `src/ipa/ipu3/algorithms/lsc.cpp:139`

근거 원문: [src/ipa/ipu3/algorithms/lsc.cpp:121](#source-80fd6c99ec2c0ae8) · [src/ipa/ipu3/algorithms/lsc.cpp:139](#source-9a0c59def2673a45)

## 파라미터 갱신 조건

`Lsc::prepare`는 `frameContext.lsc.update`가 `false`이고 그 안의 `frameContext.lsc.enabled`도 `false`이면 `return`으로 함수를 바로 종료합니다. 이 분기는 `params->use.acc_shd = 1` 설정과 `config` 값 기록보다 앞에서 실행되므로, 커널 드라이버가 userspace의 LSC 파라미터를 읽도록 하는 설정이 이루어지지 않습니다. `ct`와 `quantizedCt`는 이 분기 앞에서 이미 계산되지만, `lastAppliedCt_`와 `lastAppliedQuantizedCt_`는 함수 끝에서 갱신되므로 이 분기에서는 갱신되지 않습니다. `src/ipa/ipu3/algorithms/lsc.cpp:142`

<!-- sdd:visual:lsc-update-gates -->
### LSC 파라미터를 갱신하는 분기

명시적 update가 있으면 색온도 생략 검사를 건너뜁니다. 갱신을 통지한 뒤 비활성 상태이면 LUT 계산은 수행하지 않습니다.

```mermaid
flowchart TB
%% sdd:translations {"lsc.enabled인가?": "lsc.enabled?", "lsc.update인가?": "lsc.update?", "use.acc_shd와 활성화 값 기록": "Write use.acc_shd and <br/>enable flag", "색온도 차이가 임계값 <br/>이상인가?": "Colour-temperature <br/>difference reaches <br/>threshold?", "아니오": "No", "양자화된 색온도가 <br/>달라졌는가?": "Quantized temperature <br/>changed?", "예": "Yes", "파라미터 갱신 없이 반환": "Return without updating <br/>parameters", "활성 상태면 LUT 계산·기록": "Compute and write LUT when <br/>enabled", "활성 상태일 때만": "Only when enabled"}
  v_update{"lsc.update인가?"}
  v_enabled{"lsc.enabled인가?"}
  v_threshold{"색온도 차이가 임계값 <br/>이상인가?"}
  v_quantized{"양자화된 색온도가 <br/>달라졌는가?"}
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

`Lsc::prepare()`에서 `frameContext.lsc.update`가 `false`이고 `frameContext.lsc.enabled`가 `true`이면, `utils::abs_diff(ct, lastAppliedCt_)`가 `kColourTemperatureQuantization / 2`보다 작을 때 `return`으로 함수를 빠져나갑니다. 여기서 `ct`는 `frameContext.awb.colourTemperature`에서 읽은 원래 색온도 값이며, 양자화된 `quantizedCt`와 구분됩니다. 이 조기 반환이 일어나면 `params`를 채우는 코드와 `lastAppliedCt_` 및 `lastAppliedQuantizedCt_`를 갱신하는 코드는 실행되지 않습니다. `src/ipa/ipu3/algorithms/lsc.cpp:142`, `src/ipa/ipu3/algorithms/lsc.cpp:31`

`Lsc::prepare`에서 `frameContext.lsc.update`가 false이고 `frameContext.lsc.enabled`가 true이며 앞의 threshold 검사에서 반환되지 않은 경우, `quantizedCt`와 `lastAppliedQuantizedCt_`를 비교합니다. 두 값이 같으면 `return`으로 함수를 즉시 종료하므로 이후의 `params` 설정과 LUT 기록을 수행하지 않습니다. 두 값이 다르면 함수는 이어서 진행합니다. `src/ipa/ipu3/algorithms/lsc.cpp:142`

`Lsc::prepare`에서 `if (!frameContext.lsc.update)` 블록은 `update`가 false일 때만 들어갑니다. `update`가 true이면 이 블록을 건너뛰고 `params->use.acc_shd = 1;` 줄에 도달합니다. `update`가 false여도 `enabled`가 true이고, `utils::abs_diff(ct, lastAppliedCt_)`가 `kColourTemperatureQuantization / 2`보다 작지 않으며, `quantizedCt`가 `lastAppliedQuantizedCt_`와 다른 경우에는 세 early return에 걸리지 않아 이 줄에 도달합니다. 도달하면 `params->use.acc_shd`에 정수 `1`을 기록합니다. 소스 주석에 따르면 이 플래그는 커널 드라이버가 캐시된 복사본을 쓰지 않고, 사용자 공간에서 전달된 LSC 파라미터를 읽어야 함을 알려주는 역할을 합니다. `src/ipa/ipu3/algorithms/lsc.cpp:142`

`Lsc::prepare()`에서 `config->general.shd_enable`에 대입되는 값은 `frameContext.lsc.enabled`입니다. 인용된 코드에서 이 대입은 `if (!frameContext.lsc.enabled)` 검사와 `return`보다 앞에 있으므로, `enabled`가 `true`이든 `false`이든 인용된 범위에서는 대입이 먼저 실행됩니다. `enabled`가 `false`이면 `shd_enable`에 `false`가 대입된 뒤 `return`으로 함수를 빠져나갑니다. 다만 이 대입 앞에서 실행되는 코드는 제공된 발췌에 없으므로, 그 코드가 대입을 건너뛸 수 있는지는 확인이 필요합니다. `src/ipa/ipu3/algorithms/lsc.cpp:182`

`config->general.shd_enable`에 `frameContext.lsc.enabled` 값을 대입합니다. 이후 `if (!frameContext.lsc.enabled)` 조건이 참이면, 즉 `enabled`가 false이면 `return`을 실행해 `Lsc::prepare()`에서 반환합니다. 이때 `shd_enable`에는 false가 대입된 상태입니다. `return`으로 함수가 즉시 종료되므로 이 분기 뒤의 `prepare()` 코드는 실행되지 않습니다. `src/ipa/ipu3/algorithms/lsc.cpp:182`

`Lsc::prepare`는 `frameContext.lsc.enabled`가 거짓이면 `return`하므로, 그 뒤의 grid 설정은 활성 상태에서만 수행됩니다. 활성 경로에서는 `config->grid.width`에 `numHCells_`를, `config->grid.height`에 `numVCells_`를 넣습니다. `config->grid.block_width_log2`에는 `blockWidthLog2_`를, `config->grid.block_height_log2`에는 `blockHeightLog2_`를 넣습니다. `config->grid.grid_height_per_slice`는 `IPU3_UAPI_SHD_MAX_CELLS_PER_SET`을 `numHCells_`로 나눈 값으로 설정합니다. `src/ipa/ipu3/algorithms/lsc.cpp:142`

`Lsc::prepare`에서 `frameContext.lsc.enabled`가 거짓이면 함수가 바로 반환되므로 그리드 설정은 실행되지 않습니다. 설정이 실행될 때 `polynomial_`이 참이면 `config->grid.x_start`와 `config->grid.y_start`를 모두 0으로 설정합니다. `polynomial_`이 거짓이면 `config->grid.x_start`는 `(cropWidth_ - sensorWidth_) / 2`, `config->grid.y_start`는 `(cropHeight_ - sensorHeight_) / 2`로 설정합니다. `src/ipa/ipu3/algorithms/lsc.cpp:142`

`Lsc::prepare`는 `frameContext.lsc.enabled`가 참일 때 `config->general.gain_factor`에 `0`을 설정합니다. `enabled`가 거짓이면 `prepare`는 그 앞의 `return`에서 끝나므로 이 값을 설정하지 않습니다. 주석은 5.0을 넘는 gain이 드물다고 보아 `gain_factor`를 `0`으로 고정하고 필요하면 다시 검토한다고 적고 있습니다. 이 소스만으로는 실기기에서 주석의 해석을 확인했는지 알 수 없습니다. `src/ipa/ipu3/algorithms/lsc.cpp:142`

`Lsc::prepare`는 `config->black_level`의 `bl_r`, `bl_gr`, `bl_gb`, `bl_b` 색상 필드 네 개에 각각 `0`을 설정합니다. 이 원문에서 설정하는 값은 네 필드 모두 `0`입니다. `Lsc::prepare()`는 `lscAlgo_.interpolateComponents()`를 호출할 때 색온도 값으로 `quantizedCt`를 전달합니다. 호출 결과는 `const auto &set`에 참조로 받습니다. `src/ipa/ipu3/algorithms/lsc.cpp:248`, `src/ipa/ipu3/algorithms/lsc.cpp:255`

`Lsc::prepare()`에서 `lut->sets[s].r_and_gr[c].r`에는 `set.at("r")[i]`를, `lut->sets[s].r_and_gr[c].gr`에는 `set.at("gr")[i]`를 대입합니다. 또한 `lut->sets[s].gb_and_b[c].gb`에는 `set.at("gb")[i]`를, `lut->sets[s].gb_and_b[c].b`에는 `set.at("b")[i]`를 대입합니다. 즉 r과 gr 값은 같은 세트 항목의 `r_and_gr` 구조체에 함께 저장되고, gb와 b 값은 `gb_and_b` 구조체에 함께 저장됩니다. `src/ipa/ipu3/algorithms/lsc.cpp:263`

`Lsc::prepare` 안에서 우변의 변수 `ct`가 좌변의 멤버 `lastAppliedCt_`에 대입됩니다. 이 대입문은 `prepare` 함수 범위 안에 있으며, 발췌문에서 확인되는 것은 이 대입 자체뿐입니다. `Lsc::prepare()` 안의 `lastAppliedQuantizedCt_ = quantizedCt;` 대입문은 우변 식별자 `quantizedCt`의 값을 좌변 식별자 `lastAppliedQuantizedCt_`에 대입합니다. 이 발췌문에는 `lastAppliedQuantizedCt_`의 선언이 없으므로, 이 근거만으로는 해당 식별자가 멤버 변수인지 확인할 수 없습니다. `src/ipa/ipu3/algorithms/lsc.cpp:272`, `src/ipa/ipu3/algorithms/lsc.cpp:273`

근거 원문: [src/ipa/ipu3/algorithms/lsc.cpp:142](#source-026024190618ffa6) · [src/ipa/ipu3/algorithms/lsc.cpp:31](#source-af2cbcaa6410fbf4) · [src/ipa/ipu3/algorithms/lsc.cpp:182](#source-2565eab3740cff67) · [src/ipa/ipu3/algorithms/lsc.cpp:248](#source-dba1ef8e8f2a8563) · [src/ipa/ipu3/algorithms/lsc.cpp:255](#source-d9cad5cb8a925660) · [src/ipa/ipu3/algorithms/lsc.cpp:263](#source-807a646dc9c1acbc) · [src/ipa/ipu3/algorithms/lsc.cpp:272](#source-8fc123f7e3c227d7) · [src/ipa/ipu3/algorithms/lsc.cpp:273](#source-bb86261a35600a17)

## 메타데이터와 확인 범위

`Lsc::process()`은 전달받은 `metadata` 인자를 `lscAlgo_.process()`의 두 번째 인자로 그대로 넘깁니다. 이때 첫 번째 인자로는 `frameContext.lsc`를 넘깁니다. 이 함수 본문에는 `metadata`에 값을 직접 쓰는 코드가 없습니다. `src/ipa/ipu3/algorithms/lsc.cpp:282`

실행 확인 항목: `lscAlgo_.process()` 내부에서 `metadata`에 어떤 값을 기록하는지와 처리 결과를 어떤 방식으로 알리는지는 제공된 소스에 나타나지 않습니다. 이 내용은 `lscAlgo_`의 구현 소스에서 확인해야 합니다. `src/ipa/ipu3/algorithms/lsc.cpp:282`

근거 원문: [src/ipa/ipu3/algorithms/lsc.cpp:282](#source-5e8cfeb51ea8c16a)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | LSC 구현 파일과 공유 상태 및 프레임별 상태는 어떻게 연결됩니까? | [빌드와 상태 연결](#빌드와-상태-연결) | 코드 근거와 설명 연결 |
    | 입력 크기에 따라 그리드와 크기 제한을 어떻게 결정합니까? | [초기화와 크롭 설정](#초기화와-크롭-설정) | 코드 근거와 설명 연결 |
    | 첫 프레임의 기본 활성화와 요청 제어는 어떤 데이터를 전달합니까? | [첫 프레임과 요청별 제어](#첫-프레임과-요청별-제어) | 코드 근거와 설명 연결 |
    | 갱신은 어떤 조건에서 수행하며 커널에 어떤 파라미터를 전달합니까? | [파라미터 갱신 조건](#파라미터-갱신-조건) | 코드 근거와 설명 연결 |
    | 프레임 처리 결과를 어떻게 통지합니까? | [메타데이터와 확인 범위](#메타데이터와-확인-범위) | 코드 근거와 설명 연결 · 실행 확인 항목 별도 |

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

<a id="source-9a0c59def2673a45"></a>

??? note "소스 근거: src/ipa/ipu3/algorithms/lsc.cpp:139"
    `src/ipa/ipu3/algorithms/lsc.cpp:139`에서 시작하는 발췌입니다. 종료 줄은 139이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `847c975cc42b6b3d3c9361d2d3d84501ee3b5fa6b9101e5158e8707299973a1f`
    
    ```text
    lscAlgo_.queueRequest(context.activeState.lsc, frameContext.lsc, controls);
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

<a id="source-2565eab3740cff67"></a>

??? note "소스 근거: src/ipa/ipu3/algorithms/lsc.cpp:182"
    `src/ipa/ipu3/algorithms/lsc.cpp:182`에서 시작하는 발췌입니다. 종료 줄은 185이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `c01350762a48814f82cd74a201743cc3a05182aca7837fdb61c61be2f23d0446`
    
    ```text
    config->general.shd_enable = frameContext.lsc.enabled;
    
    	if (!frameContext.lsc.enabled)
    		return;
    ```

<a id="source-dba1ef8e8f2a8563"></a>

??? note "소스 근거: src/ipa/ipu3/algorithms/lsc.cpp:248"
    `src/ipa/ipu3/algorithms/lsc.cpp:248`에서 시작하는 발췌입니다. 종료 줄은 251이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `0d3f67f2135ab9779d48a9c37820f7d694dcd54b8d2fdd140ded1a91ef8c505f`
    
    ```text
    config->black_level.bl_r = 0;
    	config->black_level.bl_gr = 0;
    	config->black_level.bl_gb = 0;
    	config->black_level.bl_b = 0;
    ```

<a id="source-d9cad5cb8a925660"></a>

??? note "소스 근거: src/ipa/ipu3/algorithms/lsc.cpp:255"
    `src/ipa/ipu3/algorithms/lsc.cpp:255`에서 시작하는 발췌입니다. 종료 줄은 255이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `0acd80d1672a74f03b1e8ac712a046a486d25382cfa71448f67dcf3c30edf13d`
    
    ```text
    const auto &set = lscAlgo_.interpolateComponents(quantizedCt);
    ```

<a id="source-807a646dc9c1acbc"></a>

??? note "소스 근거: src/ipa/ipu3/algorithms/lsc.cpp:263"
    `src/ipa/ipu3/algorithms/lsc.cpp:263`에서 시작하는 발췌입니다. 종료 줄은 272이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `4b7da473a595e23e82e1e8118afae2c1a044c6e1a510c1ac5e7fd1fd562be119`
    
    ```text
    for (unsigned int s = 0; s < numSets; s++) {
    		for (unsigned int c = 0; c < cellsPerSet && i < totalCells; c++, i++) {
    			lut->sets[s].r_and_gr[c].r = set.at("r")[i];
    			lut->sets[s].r_and_gr[c].gr = set.at("gr")[i];
    			lut->sets[s].gb_and_b[c].gb = set.at("gb")[i];
    			lut->sets[s].gb_and_b[c].b = set.at("b")[i];
    		}
    	}
    
    	lastAppliedCt_ = ct;
    ```

<a id="source-8fc123f7e3c227d7"></a>

??? note "소스 근거: src/ipa/ipu3/algorithms/lsc.cpp:272"
    `src/ipa/ipu3/algorithms/lsc.cpp:272`에서 시작하는 발췌입니다. 종료 줄은 272이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `8ff337801a819f86b0e1912bd37319c93fe2cfaddaa718cc2437776b20fd55b2`
    
    ```text
    lastAppliedCt_ = ct;
    ```

<a id="source-bb86261a35600a17"></a>

??? note "소스 근거: src/ipa/ipu3/algorithms/lsc.cpp:273"
    `src/ipa/ipu3/algorithms/lsc.cpp:273`에서 시작하는 발췌입니다. 종료 줄은 273이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `cf33d4637404946cb518e1bad89c7613d47f18ff75930a5af092bba468a014ed`
    
    ```text
    lastAppliedQuantizedCt_ = quantizedCt;
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
    - 검토 상태 기록일: 2026-10-28 · 사람 검토 전

다음 단계: [시스템 개요](overview.md)
