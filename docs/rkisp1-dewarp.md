---
generated_at: 2026-10-24T08:53:45+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: rkisp1-dewarp
generation_method: facts-and-llm
evidence_fingerprint: fec1a62fa8a03b453ca7a231326ef83c5ff5e184971df95c17795f3023706c8e
semantic_review: human-review-required
agent: response-bundle/codex-session
generated_design: {"schema": 1, "input_fingerprint": "fec1a62fa8a03b453ca7a231326ef83c5ff5e184971df95c17795f3023706c8e", "answers": {"ownership": [{"text": "왜곡 보정 파라미터는 `RkISP1CameraData`의 `dewarpParams_`에 카메라별로 보관됩니다. 타입은 `std::optional<Dw100VertexMap::DewarpParams>`이며, 보정기 사용 가능 여부와 실제 사용 여부를 나타내는 두 플래그와 구분됩니다.", "covers": ["ownership"], "kind": "behavior", "quote": "bool canUseDewarper_;\n\tbool usesDewarper_;\n\tstd::optional<Dw100VertexMap::DewarpParams> dewarpParams_;", "evidence": ["camera"]}, {"text": "`loadTuningFile()`은 보정기가 없으면 파일을 읽지 않고 0을 반환합니다. 파일 열기 실패는 파일의 오류 코드를 반환하고, YAML 파싱 실패는 `-EINVAL`을 반환합니다. `modules`가 없거나 목록에 `Dewarp` 항목이 없을 때도 0을 반환합니다.", "covers": ["ownership"], "kind": "behavior", "quote": "if (!pipe()->dewarper_)\n\t\t/* Nothing to do without dewarper */\n\t\treturn 0;", "evidence": ["load"]}, {"text": "`loadTuningFile()`은 찾은 `Dewarp` 항목을 보정기의 `loadDewarpParams()`에 전달하고 결과를 이 카메라의 `dewarpParams_`에 받습니다. 오류는 그대로 반환하며, 성공하면 `canUseDewarper_`를 `true`로 설정합니다.", "covers": ["ownership"], "kind": "behavior", "quote": "ret = pipe()->dewarper_->loadDewarpParams(params, dewarpParams_);\n\t\tif (ret)\n\t\t\treturn ret;", "evidence": ["load"]}, {"text": "`PipelineHandlerRkISP1::configure()`는 현재 카메라의 보정기 사용 가능 여부와 원시 영상 출력 여부로 `usesDewarper_`를 정합니다. 보정기를 사용하는 주 경로를 구성할 때에는 현재 카메라의 `data->dewarpParams_`를 보정기의 `configure()`에 전달합니다.", "covers": ["ownership"], "kind": "behavior", "quote": "const PixelFormat &streamFormat = config->at(0).pixelFormat;\n\tconst PixelFormatInfo &info = PixelFormatInfo::info(streamFormat);\n\tisRaw_ = info.colourEncoding == PixelFormatInfo::ColourEncodingRAW;\n\tdata->usesDewarper_ = data->canUseDewarper_ && !isRaw_;", "evidence": ["configure"]}], "parameters": [{"text": "`loadDewarpParams()`는 시작할 때 출력 optional을 비웁니다. `cm`, `coefficients`, `cmNew`가 모두 없으면 비어 있는 상태로 0을 반환하므로, 입력이 전혀 없는 경우와 일부 값만 빠진 경우의 처리가 다릅니다.", "covers": ["parameters"], "kind": "behavior", "quote": "int ConverterDW100Module::loadDewarpParams(const ValueNode &params,\n\t\t\t\t\t   std::optional<Dw100VertexMap::DewarpParams> &dewarpParams)\n{\n\tDw100VertexMap::DewarpParams dp;\n\tdewarpParams.reset();", "evidence": ["parameters"]}, {"text": "일부 입력이 있으면 `cm`과 `coefficients`가 필요합니다. `cm`은 3×3 실수 행렬로 읽으며, 누락되거나 행렬로 읽을 수 없으면 `-EINVAL`을 반환합니다. `coefficients`가 없거나 실수 목록이 아니어도 같은 오류를 반환합니다.", "covers": ["parameters"], "kind": "behavior", "quote": "auto matrix = cm.get<Matrix<double, 3, 3>>();\n\tif (!matrix) {\n\t\tLOG(Converter, Error) << \"Failed to load 'cm' value\";\n\t\treturn -EINVAL;\n\t}", "evidence": ["parameters"]}, {"text": "`loadDewarpParams()`가 허용하는 왜곡 계수 개수는 4, 5, 8, 12개입니다. 제공된 `cmNew`도 3×3 실수 행렬이어야 하고, 생략했다면 `cm` 값을 사용합니다. 모든 검사를 통과한 뒤에만 완성한 파라미터를 출력 optional에 저장합니다.", "covers": ["parameters"], "kind": "behavior", "quote": "int ret = dp.setCoefficients(*coeffs);\n\tif (ret) {\n\t\tLOG(Converter, Error)\n\t\t\t<< \"Dewarp 'coefficients' must have 4, 5, 8 or 12 values\";\n\t\treturn -EINVAL;\n\t}", "evidence": ["parameters"]}], "application": [{"text": "`ConverterDW100Module::configure()`는 기존 vertex map 목록을 비우고 내부 변환기를 구성합니다. 성공하면 입력 버퍼 수와 보정 파라미터 유무를 저장하고, 출력 스트림마다 입력·출력 크기와 센서 크롭을 설정합니다. 보정 파라미터가 있으면 해당 map에 적용하며 각 스트림의 갱신 플래그를 켭니다.", "covers": ["application"], "kind": "behavior", "quote": "vertexMaps_.clear();\n\tret = converter_.configure(inputCfg, outputCfgs);\n\tif (ret)\n\t\treturn ret;", "evidence": ["configure"]}, {"text": "`updateControlInfos()`는 `ScalerCrop` 정보를 등록하고, 보정 파라미터가 있을 때만 `LensDewarpEnable`을 지원 제어 목록에 추가합니다. 이 제어의 범위는 꺼짐부터 켜짐까지이며 기본값은 켜짐입니다. 커널 requests 지원이 없으면 동적 구성이 불가능하다는 경고를 기록합니다.", "covers": ["application"], "kind": "behavior", "quote": "if (hasDewarpParams_)\n\t\tcontrols[&controls::LensDewarpEnable] = ControlInfo(false, true, true);", "evidence": ["controls"]}, {"text": "`setControls()`는 아직 구성하지 않은 스트림이면 바로 반환합니다. 구성된 스트림에서는 전달받은 `LensDewarpEnable`과 `ScalerCrop`을 map에 반영하고 갱신 플래그를 켭니다. 제어는 다음 `queueBuffers()` 호출에서 장치에 적용되는 계약입니다.", "covers": ["application"], "kind": "behavior", "quote": "/**\n * \\brief Set libcamera controls\n * \\param[in] stream The stream to update\n * \\param[in] controls The controls\n *\n * Looks up all supported controls in \\a controls and sets them on stream \\a\n * stream. The controls will be applied to the device on the next call to\n * queueBuffers().\n */\nvoid ConverterDW100Module::setControls(const Stream *stream, const ControlList &controls)\n{\n\tif (!isConfigured(stream))\n\t\treturn;", "evidence": ["controls"]}, {"text": "`setControls()`는 갱신할 내용이 있고 실행 중인데 커널 requests 지원이 없으면 오류를 기록합니다. 이 분기는 실행 중 동적 변경에 필요한 조건을 알리는 것으로, 앞서 저장한 map 값을 되돌리는 코드는 아닙니다.", "covers": ["application"], "kind": "behavior", "quote": "if (info.update && running_ && !converter_.supportsRequests())\n\t\tLOG(Converter, Error)\n\t\t\t<< \"Dynamically setting dw100 specific controls requires\"\n\t\t\t   \" a dw100 kernel driver with requests support\";\n}", "evidence": ["controls"]}, {"text": "`populateMetadata()`도 미설정 스트림이면 바로 반환합니다. 구성된 스트림에는 실제 `ScalerCrop`을 기록하고, 보정 파라미터가 있을 때만 `LensDewarpEnable` 상태를 기록합니다.", "covers": ["application"], "kind": "behavior", "quote": "void ConverterDW100Module::populateMetadata(const Stream *stream, ControlList &meta)\n{\n\tif (!isConfigured(stream))\n\t\treturn;", "evidence": ["metadata"]}, {"text": "`populateMetadata()`의 호출 계약은 `queueBuffers()` 뒤에 결과를 조회하는 것입니다. 스트림에 적용한 값과 그 뒤에 읽은 결과를 구분하는 기준입니다.", "covers": ["application"], "kind": "behavior", "quote": "/**\n * \\brief Retrieve updated metadata\n * \\param[in] stream The stream\n * \\param[in] meta The metadata list\n *\n * This function retrieves the metadata for the provided \\a stream and writes it\n * to \\a list. It shall be called after queueBuffers().\n */\nvoid ConverterDW100Module::populateMetadata(", "evidence": ["controls"]}]}, "body_sha256": "1e95ec0dc15282c902ba742f08feb80d181a661a011318e35ff9779cc4a5c543"}
revalidated_from: 7278a59eba64358bbf3d51f557506dd5b0bce5c4
---

# RKISP1 카메라별 왜곡 보정

**카메라별 보정값의 보관 위치와 설정 시점을 확인한 뒤 튜닝 입력과 커널 지원을 점검하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 카메라별 보정값의 소유권 절을 확인합니다. | [카메라별 보정값의 소유권](#카메라별-보정값의-소유권) |
| 튜닝 입력의 기본값과 오류 절을 확인합니다. | [튜닝 입력의 기본값과 오류](#튜닝-입력의-기본값과-오류) |
| 스트림 적용과 실행 확인 범위 절을 확인합니다. | [스트림 적용과 실행 확인 범위](#스트림-적용과-실행-확인-범위) |

## 카메라별 보정값의 소유권

왜곡 보정 파라미터는 `RkISP1CameraData`의 `dewarpParams_`에 카메라별로 보관됩니다. 타입은 `std::optional<Dw100VertexMap::DewarpParams>`이며, 보정기 사용 가능 여부와 실제 사용 여부를 나타내는 두 플래그와 구분됩니다. `src/libcamera/pipeline/rkisp1/rkisp1.cpp:94`

`loadTuningFile()`은 보정기가 없으면 파일을 읽지 않고 0을 반환합니다. 파일 열기 실패는 파일의 오류 코드를 반환하고, YAML 파싱 실패는 `-EINVAL`을 반환합니다. `modules`가 없거나 목록에 `Dewarp` 항목이 없을 때도 0을 반환합니다. `src/libcamera/pipeline/rkisp1/rkisp1.cpp:434`

`loadTuningFile()`은 찾은 `Dewarp` 항목을 보정기의 `loadDewarpParams()`에 전달하고 결과를 이 카메라의 `dewarpParams_`에 받습니다. 오류는 그대로 반환하며, 성공하면 `canUseDewarper_`를 `true`로 설정합니다. `src/libcamera/pipeline/rkisp1/rkisp1.cpp:434`

`PipelineHandlerRkISP1::configure()`는 현재 카메라의 보정기 사용 가능 여부와 원시 영상 출력 여부로 `usesDewarper_`를 정합니다. 보정기를 사용하는 주 경로를 구성할 때에는 현재 카메라의 `data->dewarpParams_`를 보정기의 `configure()`에 전달합니다. `src/libcamera/pipeline/rkisp1/rkisp1.cpp:914`

근거 원문: [src/libcamera/pipeline/rkisp1/rkisp1.cpp:94](#source-04546183f68b35f4) · [src/libcamera/pipeline/rkisp1/rkisp1.cpp:434](#source-af6210cb39d0385e) · [src/libcamera/pipeline/rkisp1/rkisp1.cpp:914](#source-c164eb4c00d1c1d6)

## 튜닝 입력의 기본값과 오류

`loadDewarpParams()`는 시작할 때 출력 optional을 비웁니다. `cm`, `coefficients`, `cmNew`가 모두 없으면 비어 있는 상태로 0을 반환하므로, 입력이 전혀 없는 경우와 일부 값만 빠진 경우의 처리가 다릅니다. `src/libcamera/converter/converter_dw100.cpp:105`

일부 입력이 있으면 `cm`과 `coefficients`가 필요합니다. `cm`은 3×3 실수 행렬로 읽으며, 누락되거나 행렬로 읽을 수 없으면 `-EINVAL`을 반환합니다. `coefficients`가 없거나 실수 목록이 아니어도 같은 오류를 반환합니다. `src/libcamera/converter/converter_dw100.cpp:105`

`loadDewarpParams()`가 허용하는 왜곡 계수 개수는 4, 5, 8, 12개입니다. 제공된 `cmNew`도 3×3 실수 행렬이어야 하고, 생략했다면 `cm` 값을 사용합니다. 모든 검사를 통과한 뒤에만 완성한 파라미터를 출력 optional에 저장합니다. `src/libcamera/converter/converter_dw100.cpp:105`

근거 원문: [src/libcamera/converter/converter_dw100.cpp:105](#source-eacff078bd6a9d79)

## 스트림 적용과 실행 확인 범위

`ConverterDW100Module::configure()`는 기존 vertex map 목록을 비우고 내부 변환기를 구성합니다. 성공하면 입력 버퍼 수와 보정 파라미터 유무를 저장하고, 출력 스트림마다 입력·출력 크기와 센서 크롭을 설정합니다. 보정 파라미터가 있으면 해당 map에 적용하며 각 스트림의 갱신 플래그를 켭니다. `src/libcamera/converter/converter_dw100.cpp:178`

`updateControlInfos()`는 `ScalerCrop` 정보를 등록하고, 보정 파라미터가 있을 때만 `LensDewarpEnable`을 지원 제어 목록에 추가합니다. 이 제어의 범위는 꺼짐부터 켜짐까지이며 기본값은 켜짐입니다. 커널 requests 지원이 없으면 동적 구성이 불가능하다는 경고를 기록합니다. `src/libcamera/converter/converter_dw100.cpp:369`

`setControls()`는 아직 구성하지 않은 스트림이면 바로 반환합니다. 구성된 스트림에서는 전달받은 `LensDewarpEnable`과 `ScalerCrop`을 map에 반영하고 갱신 플래그를 켭니다. 제어는 다음 `queueBuffers()` 호출에서 장치에 적용되는 계약입니다. `src/libcamera/converter/converter_dw100.cpp:369`

`setControls()`는 갱신할 내용이 있고 실행 중인데 커널 requests 지원이 없으면 오류를 기록합니다. 이 분기는 실행 중 동적 변경에 필요한 조건을 알리는 것으로, 앞서 저장한 map 값을 되돌리는 코드는 아닙니다. `src/libcamera/converter/converter_dw100.cpp:369`

`populateMetadata()`도 미설정 스트림이면 바로 반환합니다. 구성된 스트림에는 실제 `ScalerCrop`을 기록하고, 보정 파라미터가 있을 때만 `LensDewarpEnable` 상태를 기록합니다. `src/libcamera/converter/converter_dw100.cpp:434`

`populateMetadata()`의 호출 계약은 `queueBuffers()` 뒤에 결과를 조회하는 것입니다. 스트림에 적용한 값과 그 뒤에 읽은 결과를 구분하는 기준입니다. `src/libcamera/converter/converter_dw100.cpp:369`

근거 원문: [src/libcamera/converter/converter_dw100.cpp:178](#source-167e93a77fbf4931) · [src/libcamera/converter/converter_dw100.cpp:369](#source-fc0e25ddead912f1) · [src/libcamera/converter/converter_dw100.cpp:434](#source-3a4c4ed7cee81158)

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

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `include/libcamera/internal/converter.h`, `include/libcamera/internal/converter/converter_dw100.h`, `include/libcamera/internal/converter/converter_dw100_vertexmap.h`, `src/libcamera/converter.cpp`, `src/libcamera/converter/converter_dw100.cpp`, `src/libcamera/converter/converter_dw100_vertexmap.cpp`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `2c4b67c079`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-24 · 사람 검토 전

다음 단계: [Pipeline Handler](pipeline-handler.md)
