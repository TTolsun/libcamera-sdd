---
generated_at: 2026-11-11T17:51:40+00:00
source_commit: da6a6ed33ed0ab305f10b6f8b44736150d39cef4
status: ok
section: ipa-algorithms
generation_method: facts-and-llm
evidence_fingerprint: 4e0e0d04b32fc0f2f763c63e23eefe53e93b2e1219722a64c7692a620e56f80c
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "4e0e0d04b32fc0f2f763c63e23eefe53e93b2e1219722a64c7692a620e56f80c", "answers": {"tuning": [{"text": "RKISP1과 Mali-C55는 각각 센서 모델 이름에 `.yaml`을 붙인 파일 이름과 대체 이름 `uncalibrated.yaml`을 `IPAProxy::configurationFile()`에 전달합니다. `IPAProxy::configurationFile()`은 먼저 요청한 이름을 검색하고 경로를 찾으면 그 경로를 반환합니다. 찾지 못하고 대체 이름이 비어 있으면 빈 문자열을 반환하며, 대체 이름이 있으면 그 이름으로 검색하고 경고를 기록합니다.", "evidence": ["rkisp1-tuning", "mali-c55-tuning", "fallback"], "covers": ["tuning"], "kind": "behavior", "quote": "std::string IPAProxy::configurationFile(const std::string &name,\n\t\t\t\t\tconst std::string &fallbackName) const\n{\n\t/*\n\t * The IPA module name can be used as-is to build directory names as it\n\t * has been validated when loading the module.\n\t */\n\tconst std::string ipaName = ipam_->info().name;\n\tstd::string confPath = ipaConfigurationFile(ipaName, name, configPaths_);\n\tif (!confPath.empty()) {\n\t\tLOG(IPAProxy, Info) << \"Using tuning file \" << confPath;\n\t\treturn confPath;\n\t}"}, {"text": "두 `uncalibrated.yaml`에는 공통으로 `Agc`, `Awb`, `BlackLevelCorrection`, `Ccm`이 나열되어 있습니다. 감마 항목은 RKISP1에서 `GammaOutCorrection`, Mali-C55에서 `Gamma`입니다. Mali-C55의 알고리즘 빌드 목록에는 `gamma.cpp`가 포함되어 있으며, 이는 YAML의 `Gamma` 항목과 구분되는 빌드 목록의 내용입니다.", "evidence": ["rkisp1-uncalibrated", "mali-c55-uncalibrated", "mali-c55-algorithm-build"], "covers": ["tuning"], "kind": "behavior", "quote": "# SPDX-License-Identifier: CC0-1.0\n%YAML 1.1\n---\nversion: 1\nalgorithms:\n  - Agc:\n  - Awb:\n  - BlackLevelCorrection:\n  - Ccm:\n  - GammaOutCorrection:\n..."}], "dma-import": [{"text": "`createDMABufTexture2D()`는 `GL_RED`와 `GL_LUMINANCE`를 각각 `DRM_FORMAT_R8`에 대응합니다. `GL_RG`는 `DRM_FORMAT_GR88`에, `GL_RGBA`는 `DRM_FORMAT_ARGB8888`에 대응합니다.", "evidence": ["import"], "covers": ["dma-import"], "kind": "behavior", "quote": "switch (eglImage.format_) {\n\tcase GL_RED:\n\tcase GL_LUMINANCE:\n\t\tdrm_format = DRM_FORMAT_R8;\n\t\tbreak;\n\tcase GL_RG:\n\t\tdrm_format = DRM_FORMAT_GR88;\n\t\tbreak;\n\tcase GL_RGBA:\n\t\tdrm_format = DRM_FORMAT_ARGB8888;\n\t\tbreak;\n\tdefault:\n\t\tLOG(eGL, Error) << \"unhandled GL format\";\n\t\treturn -ENODEV;\n\t}", "part_id": "formats"}, {"text": "`createDMABufTexture2D()`의 `switch`에서 처리하지 않는 형식은 `default` 분기로 갑니다. 이 분기는 오류 수준으로 `unhandled GL format`을 로그에 기록하고 `-ENODEV`를 반환합니다. 이 분기에는 `dmabuf_import_failed_`에 값을 대입하는 코드가 없습니다.", "evidence": ["import"], "covers": ["dma-import"], "kind": "behavior", "quote": "switch (eglImage.format_) {\n\tcase GL_RED:\n\tcase GL_LUMINANCE:\n\t\tdrm_format = DRM_FORMAT_R8;\n\t\tbreak;\n\tcase GL_RG:\n\t\tdrm_format = DRM_FORMAT_GR88;\n\t\tbreak;\n\tcase GL_RGBA:\n\t\tdrm_format = DRM_FORMAT_ARGB8888;\n\t\tbreak;\n\tdefault:\n\t\tLOG(eGL, Error) << \"unhandled GL format\";\n\t\treturn -ENODEV;\n\t}", "part_id": "unsupported"}, {"text": "`createDMABufTexture2D()`는 `eglCreateImageKHR()`의 결과가 `EGL_NO_IMAGE_KHR`이면 디버그 로그에 `eglCreateImageKHR fail`을 기록합니다. 이어서 `eglImage.dmabuf_import_failed_`에 `true`를 대입하고 `-ENODEV`를 반환합니다.", "evidence": ["import"], "covers": ["dma-import"], "kind": "behavior", "quote": "if (image == EGL_NO_IMAGE_KHR) {\n\t\tLOG(eGL, Debug) << \"eglCreateImageKHR fail\";\n\t\teglImage.dmabuf_import_failed_ = true;\n\t\treturn -ENODEV;\n\t}", "part_id": "image-failure"}, {"text": "`createInputDMABufTexture2D()`는 `createDMABufTexture2D()`의 마지막 인자로 `false`를 전달합니다. `createOutputDMABufTexture2D()`는 마지막 인자로 `true`를 전달합니다.", "evidence": ["import"], "covers": ["dma-import"], "kind": "behavior", "quote": "return createDMABufTexture2D(eglImage, fd, false);\n}", "part_id": "wrappers"}, {"text": "`createDMABufTexture2D()`는 처리할 수 없는 GL 형식이거나 EGL 이미지 생성에 실패하면 앞서 `-ENODEV`를 반환합니다. 이 오류 분기에서 반환하지 않은 경로에서 `output`이 참이면 `attachTextureToFBO(eglImage)`를 호출해 텍스처를 프레임버퍼 객체에 연결하고, 그 반환값을 `ret`에 대입합니다. `output`이 거짓이면 `ret`은 초기값인 0을 유지하며, 함수는 마지막에 `ret`을 반환합니다.", "evidence": ["import"], "covers": ["dma-import"], "kind": "behavior", "quote": "if (output)\n\t\tret = attachTextureToFBO(eglImage);", "part_id": "framebuffer"}], "softisp-lsc": [{"text": "두 셰이더의 `main`은 구성된 `rgb`에서 `blacklevel`을 빼고 `1.0 - blacklevel`로 나눕니다. `APPLY_LSC`가 정의된 경우 그다음 `lsc_tex`에서 읽은 RGB 값에 `4.0`을 곱해 `rgb`에 적용합니다. packed 셰이더는 `textureOut`을, unpacked 셰이더는 `center.xy`를 텍스처 좌표로 사용하며, `4.0`은 `UQ<2, 6>` 값을 실수로 변환하는 배율입니다.", "evidence": ["packed-shader", "unpacked-shader"], "covers": ["softisp-lsc"], "kind": "behavior", "quote": "rgb = (rgb - blacklevel) / (1.0 - blacklevel);\n\n#if defined(APPLY_LSC)\n        /* Multiple by 4.0 for UQ<2, 6> -> float conversion:\n         * texture2D(...) = original_float * 2^6 (quantization) * 1/2^8 (texture byte to float)\n         * => original_float = texture2D(...) / 2^6 * 2^8 = texture2D(...) * 2^2\n         */\n        rgb = rgb * (texture2D(lsc_tex, textureOut).rgb * 4.0);\n#endif\n\n\t/* Apply AWB gains, and saturate each channel at sensor range */\n\trgb = clamp(rgb * awb, vec3(0.0), vec3(1.0));\n\n\t/* Colour Correction Matrix */\n\trgb = ccm * rgb;\n\n\t/*\n\t * Contrast\n\t * contrastExp 0..2 contrast to 0..infinity; avoid actual infinity at tan(pi/2)\n\t */\n\trgb = clamp(rgb, 0.0, 1.0);\n\trgb.r = apply_contrast(rgb.r);\n\trgb.g = apply_contrast(rgb.g);\n\trgb.b = apply_contrast(rgb.b);\n\n\t/* Apply gamma after colour correction */\n\trgb = pow(rgb, vec3(gamma));\n\n#if defined (SWAP_BLUE)\n\tgl_FragColor = vec4(rgb.bgr, 1.0);\n#else\n\tgl_FragColor = vec4(rgb, 1.0);\n#endif\n}"}, {"text": "두 셰이더의 `main`은 그다음 `awb` 이득을 곱하고 각 채널을 0과 1 사이로 제한한 뒤 `ccm` 색 보정을 적용합니다. 이어서 다시 값을 0과 1 사이로 제한하고 각 채널에 `apply_contrast`를 적용한 후 `gamma` 거듭제곱을 적용합니다.", "evidence": ["packed-shader", "unpacked-shader"], "covers": ["softisp-lsc"], "kind": "behavior", "quote": "rgb = (rgb - blacklevel) / (1.0 - blacklevel);\n\n#if defined(APPLY_LSC)\n    /* Multiple by 4.0 for UQ<2, 6> -> float conversion */\n    rgb = rgb * (texture2D(lsc_tex, center.xy).rgb * 4.0);\n#endif\n\n    /* Apply AWB gains, and saturate each channel at sensor range */\n    rgb = clamp(rgb * awb, vec3(0.0), vec3(1.0));\n\n    /* Colour Correction Matrix */\n    rgb = ccm * rgb;\n\n    /*\n     * Contrast\n     */\n    rgb = clamp(rgb, 0.0, 1.0);\n    rgb.r = apply_contrast(rgb.r);\n    rgb.g = apply_contrast(rgb.g);\n    rgb.b = apply_contrast(rgb.b);\n\n    /* Apply gamma after colour correction */\n    rgb = pow(rgb, vec3(gamma));\n\n#if defined (SWAP_BLUE)\n    gl_FragColor = vec4(rgb.bgr, 1.0);\n#else\n    gl_FragColor = vec4(rgb, 1.0);\n#endif\n}"}, {"text": "`IPASoftIspInterface.init` 선언은 `fdStats`와 `fdParams`를 인자로 받고 `lscEnabled`를 반환값으로 포함합니다. 이 선언은 이 항목들과 셰이더의 `lsc_tex` 사이의 연결을 명시하지 않습니다.", "evidence": ["softisp-interface"], "covers": ["softisp-lsc"], "kind": "behavior", "quote": "interface IPASoftIspInterface {\n\tinit(libcamera.IPASettings settings,\n\t     libcamera.SharedFD fdStats,\n\t     libcamera.SharedFD fdParams,\n\t     libcamera.IPACameraSensorInfo sensorInfo,\n\t     libcamera.ControlInfoMap sensorControls)\n\t\t=> (int32 ret,\n\t\t    libcamera.ControlInfoMap ipaControls,\n\t\t    bool ccmEnabled, bool lscEnabled);\n\tstart() => (int32 ret);\n\tstop();\n\tconfigure(IPAConfigInfo configInfo)\n\t\t=> (int32 ret, libcamera.ControlInfoMap ipaControls);"}]}, "topic_inputs": {"tuning": "9cf496eb13a2b4c11818b66650bc8bd49d88c59cc832927717c5a4a6e4c9a393", "dma-import": "a6b31253ad3982ad93e4d0dd1c6482b9553c39834bac1883ffd71a6e12f02352", "softisp-lsc": "16ca1f5eec246f4f81a03013afa2064e290c4d142fda1ecad860226e96693d73"}, "reused_topics": ["tuning", "dma-import"], "replayed_units": [], "generated_topics": ["softisp-lsc"], "topic_agents": {"tuning": "cli/codex/gpt-6.1-terra", "dma-import": "cli/codex/gpt-6.1-terra", "softisp-lsc": "cli/codex/gpt-6.1-terra"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "367d18b95f8f0d01a15ae0f4d1b70f7e13e4d0298df4215e2c449ac4905db6f9", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "d0f7ab4c48fcf52409935931eb9b93aacd48af4b19e9bb816fa496f1214fdb2f", "answer_contracts": "a39c9a8818afc47e059141d486337c0f12a7fd34319e2b6f7674fc428bc83e2b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "050c20aa2fdcceae10c6275fbb5f850f616ab5051bb67ccbcb4a204877a238d9", "explanation": "69bcaa207ef39d20f6a47ac201c3edf119f59b333e85131dea1bce85eef4006b", "design_response": "a7c199bc52bcc0e749ef01186e50bca98107473d5c82e2248712f465d02e1e69", "design_validation": "92ddb9a65c909173ff4c7cb627dff83e71c10c8258c51344ef0eb1a7a023937f"}, "validation_model": "0d1544a2ea90f295c2aed62fab60f29f7788e623a953b6f7d5089373b8b41d94", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "b87a84b1bc31079837dc4dc4527ce02c9dc2cbc3a26ff7e99e0872941d213995"}, "reuse_lineage": {"source_commit": "c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78", "body_sha256": "735147fb0cfbaf1f1fae1140122885d84ae19ee7932352133315c822725af94f", "topics": ["tuning", "dma-import"], "validation": "current source, contract and editorial checks; human review pending"}, "body_sha256": "4637662df3e4b9200ac1764e79f701122ad6697510dded790a812731dfd51cc8"}
revalidated_from: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
---

# IPA 튜닝과 소프트웨어 ISP

**튜닝 파일 경로와 소프트웨어 ISP의 렌즈 보정·입력 버퍼 연결을 코드와 대조하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| IPA 모듈 선택, 스레드·프로세스 경계와 요청·결과 인터페이스를 구현 근거로 확인하세요. | [IPA 관리와 구현 진입점](ipa.md) |

## 보정 전 튜닝 파일

RKISP1과 Mali-C55는 각각 센서 모델 이름에 `.yaml`을 붙인 파일 이름과 대체 이름 `uncalibrated.yaml`을 `IPAProxy::configurationFile()`에 전달합니다. `IPAProxy::configurationFile()`은 먼저 요청한 이름을 검색하고 경로를 찾으면 그 경로를 반환합니다. 찾지 못하고 대체 이름이 비어 있으면 빈 문자열을 반환하며, 대체 이름이 있으면 그 이름으로 검색하고 경고를 기록합니다. `src/libcamera/pipeline/rkisp1/rkisp1.cpp:406`, `src/libcamera/pipeline/mali-c55/mali-c55.cpp:468`, `src/libcamera/ipa_proxy.cpp:174`

<!-- sdd:visual:ipa-tuning-file-fallback -->
### IPA 튜닝 파일 검색 순서

```mermaid
flowchart TB
%% sdd:translations {"검색 결과 확인": "Check the result", "대체 이름으로 검색하고 경고 <br/>기록": "Look up the fallback name <br/>and log a warning", "대체 이름이 비었는가?": "Is the fallback name empty?", "아니요": "No", "예": "Yes", "오류 기록 후 빈 경로 반환": "Log an error and return an <br/>empty path", "요청 경로 반환": "Return the requested path", "요청 경로가 있는가?": "Requested path found?", "요청한 이름으로 검색": "Look up the requested name"}
  v_lookup["요청한 이름으로 검색"]
  v_found{"요청 경로가 있는가?"}
  v_requested["요청 경로 반환"]
  v_fallback{"대체 이름이 비었는가?"}
  v_missing["오류 기록 후 빈 경로 반환"]
  v_alternative["대체 이름으로 검색하고 경고 <br/>기록"]
  v_lookup -->|"검색 결과 확인"| v_found
  v_found -->|"예"| v_requested
  v_found -->|"아니요"| v_fallback
  v_fallback -->|"예"| v_missing
  v_fallback -->|"아니요"| v_alternative
```

[Mermaid 원문](ipa-algorithms.ipa-tuning-file-fallback.mmd)

??? note "그림 근거와 확인 범위"
    요청한 튜닝 파일을 찾지 못하면 어떤 조건에서 대체 이름을 검색하나요?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Look up the requested name">요청한 이름으로 검색</span> | [src/libcamera/ipa_proxy.cpp:174](#source-4000376c954f5327) |
    | <span data-sdd-label-en="Requested path found?">요청 경로가 있는가?</span> | [src/libcamera/ipa_proxy.cpp:174](#source-4000376c954f5327) |
    | <span data-sdd-label-en="Return the requested path">요청 경로 반환</span> | [src/libcamera/ipa_proxy.cpp:174](#source-4000376c954f5327) |
    | <span data-sdd-label-en="Is the fallback name empty?">대체 이름이 비었는가?</span> | [src/libcamera/ipa_proxy.cpp:174](#source-4000376c954f5327) |
    | <span data-sdd-label-en="Log an error and return an empty path">오류 기록 후 빈 경로 반환</span> | [src/libcamera/ipa_proxy.cpp:174](#source-4000376c954f5327) |
    | <span data-sdd-label-en="Look up the fallback name and log a warning">대체 이름으로 검색하고 경고 기록</span> | [src/libcamera/ipa_proxy.cpp:174](#source-4000376c954f5327) |
    | <span data-sdd-label-en="Check the result">검색 결과 확인</span> | [src/libcamera/ipa_proxy.cpp:174](#source-4000376c954f5327) |
    | <span data-sdd-label-en="Yes">예</span> | [src/libcamera/ipa_proxy.cpp:174](#source-4000376c954f5327) |
    | <span data-sdd-label-en="No">아니요</span> | [src/libcamera/ipa_proxy.cpp:174](#source-4000376c954f5327) |
    | <span data-sdd-label-en="Yes">예</span> | [src/libcamera/ipa_proxy.cpp:174](#source-4000376c954f5327) |
    | <span data-sdd-label-en="No">아니요</span> | [src/libcamera/ipa_proxy.cpp:174](#source-4000376c954f5327) |
<!-- /sdd:visual:ipa-tuning-file-fallback -->

두 `uncalibrated.yaml`에는 공통으로 `Agc`, `Awb`, `BlackLevelCorrection`, `Ccm`이 나열되어 있습니다. 감마 항목은 RKISP1에서 `GammaOutCorrection`, Mali-C55에서 `Gamma`입니다. Mali-C55의 알고리즘 빌드 목록에는 `gamma.cpp`가 포함되어 있으며, 이는 YAML의 `Gamma` 항목과 구분되는 빌드 목록의 내용입니다. `src/ipa/rkisp1/data/uncalibrated.yaml:1`, `src/ipa/mali-c55/data/uncalibrated.yaml:1`, `src/ipa/mali-c55/algorithms/meson.build:1`

근거 원문: [src/libcamera/pipeline/rkisp1/rkisp1.cpp:406](#source-a117437c7ec61db3) · [src/libcamera/pipeline/mali-c55/mali-c55.cpp:468](#source-efc0c3fc5cf7acef) · [src/libcamera/ipa_proxy.cpp:174](#source-4000376c954f5327) · [src/ipa/rkisp1/data/uncalibrated.yaml:1](#source-c3d57577d02a4dc3) · [src/ipa/mali-c55/data/uncalibrated.yaml:1](#source-2aca0607eacef985) · [src/ipa/mali-c55/algorithms/meson.build:1](#source-f8b760d0d191cbea)

## 소프트웨어 ISP 입력 버퍼의 텍스처 형식

`createDMABufTexture2D()`는 `GL_RED`와 `GL_LUMINANCE`를 각각 `DRM_FORMAT_R8`에 대응합니다. `GL_RG`는 `DRM_FORMAT_GR88`에, `GL_RGBA`는 `DRM_FORMAT_ARGB8888`에 대응합니다. `src/libcamera/egl.cpp:174`

<!-- sdd:visual:softisp-dmabuf-import-paths -->
### DMA-BUF 가져오기 분기

```mermaid
flowchart TB
%% sdd:translations {"-ENODEV 반환": "Return -ENODEV", "0 반환": "Return 0", "EGL 이미지 생성에 <br/>실패했는가?": "Did EGL image creation fail?", "GL 형식을 지원하는가?": "Is the GL format supported?", "실패 플래그 설정 후 -ENODEV <br/>반환": "Set the failure flag and <br/>return -ENODEV", "아니요": "No", "예": "Yes", "예, DRM 형식 선택": "Yes, select the DRM format", "출력 텍스처인가?": "Is this an output texture?", "프레임버퍼 연결 결과 반환": "Return the framebuffer <br/>attachment result"}
  v_format{"GL 형식을 지원하는가?"}
  v_unknown["-ENODEV 반환"]
  v_image{"EGL 이미지 생성에 <br/>실패했는가?"}
  v_failed["실패 플래그 설정 후 -ENODEV <br/>반환"]
  v_output{"출력 텍스처인가?"}
  v_attach["프레임버퍼 연결 결과 반환"]
  v_success["0 반환"]
  v_format -->|"아니요"| v_unknown
  v_format -->|"예, DRM 형식 선택"| v_image
  v_image -->|"예"| v_failed
  v_image -->|"아니요"| v_output
  v_output -->|"예"| v_attach
  v_output -->|"아니요"| v_success
```

[Mermaid 원문](ipa-algorithms.softisp-dmabuf-import-paths.mmd)

??? note "그림 근거와 확인 범위"
    GL 형식과 EGL 이미지 검사에서 각각 어떻게 실패하며, 언제 프레임버퍼를 연결하나요?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Is the GL format supported?">GL 형식을 지원하는가?</span> | [src/libcamera/egl.cpp:174](#source-8cc12a6ba8b0dced) |
    | <span data-sdd-label-en="Return -ENODEV">-ENODEV 반환</span> | [src/libcamera/egl.cpp:174](#source-8cc12a6ba8b0dced) |
    | <span data-sdd-label-en="Did EGL image creation fail?">EGL 이미지 생성에 실패했는가?</span> | [src/libcamera/egl.cpp:174](#source-8cc12a6ba8b0dced) |
    | <span data-sdd-label-en="Set the failure flag and return -ENODEV">실패 플래그 설정 후 -ENODEV 반환</span> | [src/libcamera/egl.cpp:174](#source-8cc12a6ba8b0dced) |
    | <span data-sdd-label-en="Is this an output texture?">출력 텍스처인가?</span> | [src/libcamera/egl.cpp:174](#source-8cc12a6ba8b0dced) |
    | <span data-sdd-label-en="Return the framebuffer attachment result">프레임버퍼 연결 결과 반환</span> | [src/libcamera/egl.cpp:174](#source-8cc12a6ba8b0dced) |
    | <span data-sdd-label-en="Return 0">0 반환</span> | [src/libcamera/egl.cpp:174](#source-8cc12a6ba8b0dced) |
    | <span data-sdd-label-en="No">아니요</span> | [src/libcamera/egl.cpp:174](#source-8cc12a6ba8b0dced) |
    | <span data-sdd-label-en="Yes, select the DRM format">예, DRM 형식 선택</span> | [src/libcamera/egl.cpp:174](#source-8cc12a6ba8b0dced) |
    | <span data-sdd-label-en="Yes">예</span> | [src/libcamera/egl.cpp:174](#source-8cc12a6ba8b0dced) |
    | <span data-sdd-label-en="No">아니요</span> | [src/libcamera/egl.cpp:174](#source-8cc12a6ba8b0dced) |
    | <span data-sdd-label-en="Yes">예</span> | [src/libcamera/egl.cpp:174](#source-8cc12a6ba8b0dced) |
    | <span data-sdd-label-en="No">아니요</span> | [src/libcamera/egl.cpp:174](#source-8cc12a6ba8b0dced) |
<!-- /sdd:visual:softisp-dmabuf-import-paths -->

`createDMABufTexture2D()`의 `switch`에서 처리하지 않는 형식은 `default` 분기로 갑니다. 이 분기는 오류 수준으로 `unhandled GL format`을 로그에 기록하고 `-ENODEV`를 반환합니다. 이 분기에는 `dmabuf_import_failed_`에 값을 대입하는 코드가 없습니다. `src/libcamera/egl.cpp:174`

`createDMABufTexture2D()`는 `eglCreateImageKHR()`의 결과가 `EGL_NO_IMAGE_KHR`이면 디버그 로그에 `eglCreateImageKHR fail`을 기록합니다. 이어서 `eglImage.dmabuf_import_failed_`에 `true`를 대입하고 `-ENODEV`를 반환합니다. `createInputDMABufTexture2D()`는 `createDMABufTexture2D()`의 마지막 인자로 `false`를 전달합니다. `createOutputDMABufTexture2D()`는 마지막 인자로 `true`를 전달합니다. `src/libcamera/egl.cpp:174`

`createDMABufTexture2D()`는 처리할 수 없는 GL 형식이거나 EGL 이미지 생성에 실패하면 앞서 `-ENODEV`를 반환합니다. 이 오류 분기에서 반환하지 않은 경로에서 `output`이 참이면 `attachTextureToFBO(eglImage)`를 호출해 텍스처를 프레임버퍼 객체에 연결하고, 그 반환값을 `ret`에 대입합니다. `output`이 거짓이면 `ret`은 초기값인 0을 유지하며, 함수는 마지막에 `ret`을 반환합니다. `src/libcamera/egl.cpp:174`

근거 원문: [src/libcamera/egl.cpp:174](#source-8cc12a6ba8b0dced)

## 소프트웨어 ISP 셰이더의 렌즈 음영 보정

두 셰이더의 `main`은 구성된 `rgb`에서 `blacklevel`을 빼고 `1.0 - blacklevel`로 나눕니다. `APPLY_LSC`가 정의된 경우 그다음 `lsc_tex`에서 읽은 RGB 값에 `4.0`을 곱해 `rgb`에 적용합니다. packed 셰이더는 `textureOut`을, unpacked 셰이더는 `center.xy`를 텍스처 좌표로 사용하며, `4.0`은 `UQ<2, 6>` 값을 실수로 변환하는 배율입니다. `src/libcamera/shaders/bayer_1x_packed.frag:237`, `src/libcamera/shaders/bayer_unpacked.frag:140`

<!-- sdd:visual:softisp-lsc-shader-order -->
### 셰이더의 렌즈 음영 보정 위치

```mermaid
flowchart TB
%% sdd:translations {"APPLY#95;LSC가 정의됐는가?": "Is APPLY#95;LSC defined?", "AWB 이득 곱셈과 범위 제한": "Apply AWB gains and clamp", "AWB 적용 후": "After AWB", "CCM, 범위 제한, 대비, 감마 <br/>순서": "CCM, clamp, contrast, then <br/>gamma", "lsc#95;tex의 RGB에 4.0을 곱해 <br/>적용": "Apply lsc#95;tex RGB scaled by <br/>4.0", "블랙 레벨 정규화": "Normalize the black level", "블랙 레벨 처리 후": "After black-level correction", "아니요": "No", "예": "Yes", "음영 보정 후": "After lens shading <br/>correction"}
  v_black["블랙 레벨 정규화"]
  v_condition{"APPLY#95;LSC가 정의됐는가?"}
  v_lsc["lsc#95;tex의 RGB에 4.0을 곱해 <br/>적용"]
  v_awb["AWB 이득 곱셈과 범위 제한"]
  v_color["CCM, 범위 제한, 대비, 감마 <br/>순서"]
  v_black -->|"블랙 레벨 처리 후"| v_condition
  v_condition -->|"예"| v_lsc
  v_condition -->|"아니요"| v_awb
  v_lsc -->|"음영 보정 후"| v_awb
  v_awb -->|"AWB 적용 후"| v_color
```

[Mermaid 원문](ipa-algorithms.softisp-lsc-shader-order.mmd)

??? note "그림 근거와 확인 범위"
    두 셰이더에서 어떤 조건일 때 렌즈 음영을 보정하며, 전후에는 무엇을 처리하나요?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Normalize the black level">블랙 레벨 정규화</span> | [src/libcamera/shaders/bayer_1x_packed.frag:237](#source-68d470282c445049) · [src/libcamera/shaders/bayer_unpacked.frag:140](#source-86d4a7688119bd37) |
    | <span data-sdd-label-en="Is APPLY_LSC defined?">APPLY&#95;LSC가 정의됐는가?</span> | [src/libcamera/shaders/bayer_1x_packed.frag:237](#source-68d470282c445049) · [src/libcamera/shaders/bayer_unpacked.frag:140](#source-86d4a7688119bd37) |
    | <span data-sdd-label-en="Apply lsc_tex RGB scaled by 4.0">lsc&#95;tex의 RGB에 4.0을 곱해 적용</span> | [src/libcamera/shaders/bayer_1x_packed.frag:237](#source-68d470282c445049) · [src/libcamera/shaders/bayer_unpacked.frag:140](#source-86d4a7688119bd37) |
    | <span data-sdd-label-en="Apply AWB gains and clamp">AWB 이득 곱셈과 범위 제한</span> | [src/libcamera/shaders/bayer_1x_packed.frag:237](#source-68d470282c445049) · [src/libcamera/shaders/bayer_unpacked.frag:140](#source-86d4a7688119bd37) |
    | <span data-sdd-label-en="CCM, clamp, contrast, then gamma">CCM, 범위 제한, 대비, 감마 순서</span> | [src/libcamera/shaders/bayer_1x_packed.frag:237](#source-68d470282c445049) · [src/libcamera/shaders/bayer_unpacked.frag:140](#source-86d4a7688119bd37) |
    | <span data-sdd-label-en="After black-level correction">블랙 레벨 처리 후</span> | [src/libcamera/shaders/bayer_1x_packed.frag:237](#source-68d470282c445049) · [src/libcamera/shaders/bayer_unpacked.frag:140](#source-86d4a7688119bd37) |
    | <span data-sdd-label-en="Yes">예</span> | [src/libcamera/shaders/bayer_1x_packed.frag:237](#source-68d470282c445049) · [src/libcamera/shaders/bayer_unpacked.frag:140](#source-86d4a7688119bd37) |
    | <span data-sdd-label-en="No">아니요</span> | [src/libcamera/shaders/bayer_1x_packed.frag:237](#source-68d470282c445049) · [src/libcamera/shaders/bayer_unpacked.frag:140](#source-86d4a7688119bd37) |
    | <span data-sdd-label-en="After lens shading correction">음영 보정 후</span> | [src/libcamera/shaders/bayer_1x_packed.frag:237](#source-68d470282c445049) · [src/libcamera/shaders/bayer_unpacked.frag:140](#source-86d4a7688119bd37) |
    | <span data-sdd-label-en="After AWB">AWB 적용 후</span> | [src/libcamera/shaders/bayer_1x_packed.frag:237](#source-68d470282c445049) · [src/libcamera/shaders/bayer_unpacked.frag:140](#source-86d4a7688119bd37) |
<!-- /sdd:visual:softisp-lsc-shader-order -->

두 셰이더의 `main`은 그다음 `awb` 이득을 곱하고 각 채널을 0과 1 사이로 제한한 뒤 `ccm` 색 보정을 적용합니다. 이어서 다시 값을 0과 1 사이로 제한하고 각 채널에 `apply_contrast`를 적용한 후 `gamma` 거듭제곱을 적용합니다. `IPASoftIspInterface.init` 선언은 `fdStats`와 `fdParams`를 인자로 받고 `lscEnabled`를 반환값으로 포함합니다. 이 선언은 이 항목들과 셰이더의 `lsc_tex` 사이의 연결을 명시하지 않습니다. `src/libcamera/shaders/bayer_1x_packed.frag:237`, `src/libcamera/shaders/bayer_unpacked.frag:140`, `include/libcamera/ipa/softisp.mojom:1`

근거 원문: [src/libcamera/shaders/bayer_1x_packed.frag:237](#source-68d470282c445049) · [src/libcamera/shaders/bayer_unpacked.frag:140](#source-86d4a7688119bd37) · [include/libcamera/ipa/softisp.mojom:1](#source-df8e8976167a0311)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 센서별 튜닝 파일이 없으면 어떤 파일과 알고리즘이 쓰입니까? | [보정 전 튜닝 파일](#보정-전-튜닝-파일) | 코드 근거와 설명 연결 |
    | 소프트웨어 ISP의 GPU 셰이더는 렌즈 음영 보정을 어느 단계에 적용합니까? | [소프트웨어 ISP 셰이더의 렌즈 음영 보정](#소프트웨어-isp-셰이더의-렌즈-음영-보정) | 코드 근거와 설명 연결 |
    | 소프트웨어 ISP의 입력 버퍼를 텍스처로 가져올 때 형식과 실패 처리는 어떻게 연결됩니까? | [소프트웨어 ISP 입력 버퍼의 텍스처 형식](#소프트웨어-isp-입력-버퍼의-텍스처-형식) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-a117437c7ec61db3"></a>

??? note "소스 근거: src/libcamera/pipeline/rkisp1/rkisp1.cpp:406"
    `src/libcamera/pipeline/rkisp1/rkisp1.cpp:406`에서 시작하는 발췌입니다. 종료 줄은 408이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `5085c39368b264636b7bc7386979e019ea9cd60621335cc42d1e3ad28d810c6c`
    
    ```text
    /* The IPA tuning file is made from the sensor name. */
    	std::string ipaTuningFile =
    		ipa_->configurationFile(sensor_->model() + ".yaml", "uncalibrated.yaml");
    ```

<a id="source-efc0c3fc5cf7acef"></a>

??? note "소스 근거: src/libcamera/pipeline/mali-c55/mali-c55.cpp:468"
    `src/libcamera/pipeline/mali-c55/mali-c55.cpp:468`에서 시작하는 발췌입니다. 종료 줄은 469이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `226c3c21c4b760c25b2a3323369bce67c92f92db80b9fcef19589a44af6eaa2a`
    
    ```text
    std::string ipaTuningFile = ipa_->configurationFile(sensor()->model() + ".yaml",
    							    "uncalibrated.yaml");
    ```

<a id="source-4000376c954f5327"></a>

??? note "소스 근거: src/libcamera/ipa_proxy.cpp:174"
    `src/libcamera/ipa_proxy.cpp:174`에서 시작하는 발췌입니다. 종료 줄은 199이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `6c48d1f3994c22addbc1b338c87cf7b166f9fee0f9223ecf718a254be0aa93a8`
    
    ```text
    std::string IPAProxy::configurationFile(const std::string &name,
    					const std::string &fallbackName) const
    {
    	/*
    	 * The IPA module name can be used as-is to build directory names as it
    	 * has been validated when loading the module.
    	 */
    	const std::string ipaName = ipam_->info().name;
    	std::string confPath = ipaConfigurationFile(ipaName, name, configPaths_);
    	if (!confPath.empty()) {
    		LOG(IPAProxy, Info) << "Using tuning file " << confPath;
    		return confPath;
    	}
    
    	if (fallbackName.empty()) {
    		LOG(IPAProxy, Error)
    			<< "Configuration file '" << name
    			<< "' not found for IPA module '" << ipaName << "'";
    		return std::string();
    	}
    
    	confPath = ipaConfigurationFile(ipaName, fallbackName, configPaths_);
    	LOG(IPAProxy, Warning)
    		<< "Configuration file '" << name
    		<< "' not found for IPA module '" << ipaName
    		<< "', falling back to '" << confPath << "'";
    ```

<a id="source-c3d57577d02a4dc3"></a>

??? note "소스 근거: src/ipa/rkisp1/data/uncalibrated.yaml:1"
    `src/ipa/rkisp1/data/uncalibrated.yaml:1`에서 시작하는 발췌입니다. 종료 줄은 11이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `f3e8a3a6257b7fb82f16cf5c8239901d57bcc15023908c8994dcac3714e9e648`
    
    ```text
    # SPDX-License-Identifier: CC0-1.0
    %YAML 1.1
    ---
    version: 1
    algorithms:
      - Agc:
      - Awb:
      - BlackLevelCorrection:
      - Ccm:
      - GammaOutCorrection:
    ...
    ```

<a id="source-2aca0607eacef985"></a>

??? note "소스 근거: src/ipa/mali-c55/data/uncalibrated.yaml:1"
    `src/ipa/mali-c55/data/uncalibrated.yaml:1`에서 시작하는 발췌입니다. 종료 줄은 11이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `146853b0c8245c36b27863ac10c2edcaeed14bb5624c0eb523a0b75d226199e1`
    
    ```text
    # SPDX-License-Identifier: CC0-1.0
    %YAML 1.1
    ---
    version: 1
    algorithms:
      - Agc:
      - Awb:
      - BlackLevelCorrection:
      - Ccm:
      - Gamma:
    ...
    ```

<a id="source-f8b760d0d191cbea"></a>

??? note "소스 근거: src/ipa/mali-c55/algorithms/meson.build:1"
    `src/ipa/mali-c55/algorithms/meson.build:1`에서 시작하는 발췌입니다. 종료 줄은 10이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `3928a9bc4320438e89a6a3545559afe1f9b45195e24421219df8014c30f33778`
    
    ```text
    # SPDX-License-Identifier: CC0-1.0
    
    mali_c55_ipa_algorithms = files([
        'agc.cpp',
        'awb.cpp',
        'blc.cpp',
        'ccm.cpp',
        'gamma.cpp',
        'lsc.cpp',
    ])
    ```

<a id="source-8cc12a6ba8b0dced"></a>

??? note "소스 근거: src/libcamera/egl.cpp:174"
    `src/libcamera/egl.cpp:174`에서 시작하는 발췌입니다. 종료 줄은 279이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `54972e6c423848da387112f756eb3670a3ac895a05f7cc8d3e7bb77f5cb6a570`
    
    ```text
    int eGL::createDMABufTexture2D(eGLImage &eglImage, int fd, bool output)
    {
    	EGLint drm_format;
    	int ret = 0;
    
    	assertThread();
    
    	switch (eglImage.format_) {
    	case GL_RED:
    	case GL_LUMINANCE:
    		drm_format = DRM_FORMAT_R8;
    		break;
    	case GL_RG:
    		drm_format = DRM_FORMAT_GR88;
    		break;
    	case GL_RGBA:
    		drm_format = DRM_FORMAT_ARGB8888;
    		break;
    	default:
    		LOG(eGL, Error) << "unhandled GL format";
    		return -ENODEV;
    	}
    
    	// clang-format off
    	EGLint image_attrs[] = {
    		EGL_WIDTH, (EGLint)eglImage.width_,
    		EGL_HEIGHT, (EGLint)eglImage.height_,
    		EGL_LINUX_DRM_FOURCC_EXT, drm_format,
    		EGL_DMA_BUF_PLANE0_FD_EXT, fd,
    		EGL_DMA_BUF_PLANE0_OFFSET_EXT, 0,
    		EGL_DMA_BUF_PLANE0_PITCH_EXT, (EGLint)eglImage.stride_,
    		EGL_DMA_BUF_PLANE0_MODIFIER_LO_EXT, 0,
    		EGL_DMA_BUF_PLANE0_MODIFIER_HI_EXT, 0,
    		EGL_NONE,
    	};
    	// clang-format on
    
    	EGLImageKHR image = vtable_.eglCreateImageKHR(display_, EGL_NO_CONTEXT,
    						      EGL_LINUX_DMA_BUF_EXT,
    						      NULL, image_attrs);
    
    	if (image == EGL_NO_IMAGE_KHR) {
    		LOG(eGL, Debug) << "eglCreateImageKHR fail";
    		eglImage.dmabuf_import_failed_ = true;
    		return -ENODEV;
    	}
    
    	activateBindTexture(eglImage);
    
    	// Generate texture with filter semantics
    	vtable_.glEGLImageTargetTexture2DOES(GL_TEXTURE_2D, image);
    	vtable_.eglDestroyImageKHR(display_, image);
    
    	// Nearest filtering
    	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    
    	// Wrap to edge to avoid edge artifacts
    	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
    
    	if (output)
    		ret = attachTextureToFBO(eglImage);
    
    	return ret;
    }
    
    /**
     * \brief Create an input DMA-BUF backed texture
     * \param[in,out] eglImage EGL image to associate with the DMA-BUF
     * \param[in] fd DMA-BUF file descriptor
     *
     * Creates an EGL image from a DMA-BUF file descriptor and binds it to
     * a 2D texture for use as an input texture in shaders. The texture is
     * configured with nearest filtering and clamp-to-edge wrapping.
     *
     * \return 0 on success, or -ENODEV on failure
     */
    int eGL::createInputDMABufTexture2D(eGLImage &eglImage, int fd)
    {
    	assertThread();
    
    	return createDMABufTexture2D(eglImage, fd, false);
    }
    
    /**
     * \brief Create an output DMA-BUF backed texture
     * \param[in,out] eglImage EGL image to associate with the DMA-BUF
     * \param[in] fd DMA-BUF file descriptor
     *
     * Creates an EGL image from a DMA-BUF file descriptor and binds it to
     * a 2D texture, then attaches it to a framebuffer object for use as a
     * render target. This enables zero-copy rendering directly to the
     * DMA-BUF.
     *
     * \return 0 on success, or -ENODEV on failure
     */
    int eGL::createOutputDMABufTexture2D(eGLImage &eglImage, int fd)
    {
    	assertThread();
    
    	return createDMABufTexture2D(eglImage, fd, true);
    }
    
    /**
     * \brief Create a 2D texture from a memory buffer
    ```

<a id="source-68d470282c445049"></a>

??? note "소스 근거: src/libcamera/shaders/bayer_1x_packed.frag:237"
    `src/libcamera/shaders/bayer_1x_packed.frag:237`에서 시작하는 발췌입니다. 종료 줄은 270이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `84e5be2b8bbb1a1337af23df059b5d9270e16421c945a530a8c848709f302e6a`
    
    ```text
    rgb = (rgb - blacklevel) / (1.0 - blacklevel);
    
    #if defined(APPLY_LSC)
            /* Multiple by 4.0 for UQ<2, 6> -> float conversion:
             * texture2D(...) = original_float * 2^6 (quantization) * 1/2^8 (texture byte to float)
             * => original_float = texture2D(...) / 2^6 * 2^8 = texture2D(...) * 2^2
             */
            rgb = rgb * (texture2D(lsc_tex, textureOut).rgb * 4.0);
    #endif
    
    	/* Apply AWB gains, and saturate each channel at sensor range */
    	rgb = clamp(rgb * awb, vec3(0.0), vec3(1.0));
    
    	/* Colour Correction Matrix */
    	rgb = ccm * rgb;
    
    	/*
    	 * Contrast
    	 * contrastExp 0..2 contrast to 0..infinity; avoid actual infinity at tan(pi/2)
    	 */
    	rgb = clamp(rgb, 0.0, 1.0);
    	rgb.r = apply_contrast(rgb.r);
    	rgb.g = apply_contrast(rgb.g);
    	rgb.b = apply_contrast(rgb.b);
    
    	/* Apply gamma after colour correction */
    	rgb = pow(rgb, vec3(gamma));
    
    #if defined (SWAP_BLUE)
    	gl_FragColor = vec4(rgb.bgr, 1.0);
    #else
    	gl_FragColor = vec4(rgb, 1.0);
    #endif
    }
    ```

<a id="source-86d4a7688119bd37"></a>

??? note "소스 근거: src/libcamera/shaders/bayer_unpacked.frag:140"
    `src/libcamera/shaders/bayer_unpacked.frag:140`에서 시작하는 발췌입니다. 종료 줄은 169이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `5567b6548b078d7db847d9b57eefb1799e917214787288683110d5b41510573b`
    
    ```text
    rgb = (rgb - blacklevel) / (1.0 - blacklevel);
    
    #if defined(APPLY_LSC)
        /* Multiple by 4.0 for UQ<2, 6> -> float conversion */
        rgb = rgb * (texture2D(lsc_tex, center.xy).rgb * 4.0);
    #endif
    
        /* Apply AWB gains, and saturate each channel at sensor range */
        rgb = clamp(rgb * awb, vec3(0.0), vec3(1.0));
    
        /* Colour Correction Matrix */
        rgb = ccm * rgb;
    
        /*
         * Contrast
         */
        rgb = clamp(rgb, 0.0, 1.0);
        rgb.r = apply_contrast(rgb.r);
        rgb.g = apply_contrast(rgb.g);
        rgb.b = apply_contrast(rgb.b);
    
        /* Apply gamma after colour correction */
        rgb = pow(rgb, vec3(gamma));
    
    #if defined (SWAP_BLUE)
        gl_FragColor = vec4(rgb.bgr, 1.0);
    #else
        gl_FragColor = vec4(rgb, 1.0);
    #endif
    }
    ```

<a id="source-df8e8976167a0311"></a>

??? note "소스 근거: include/libcamera/ipa/softisp.mojom:1"
    `include/libcamera/ipa/softisp.mojom:1`에서 시작하는 발췌입니다. 종료 줄은 40이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `dedbfb928f4f1cdb8e174d8104cb8cbd575fd543e9b620240984c3af4cddecdb`
    
    ```text
    /* SPDX-License-Identifier: LGPL-2.1-or-later */
    
    /*
     * \todo Document the interface and remove the related EXCLUDE_PATTERNS entry.
     */
    
    module ipa.softisp;
    
    import "include/libcamera/ipa/core.mojom";
    
    struct IPAConfigInfo {
    	libcamera.ControlInfoMap sensorControls;
    };
    
    interface IPASoftIspInterface {
    	init(libcamera.IPASettings settings,
    	     libcamera.SharedFD fdStats,
    	     libcamera.SharedFD fdParams,
    	     libcamera.IPACameraSensorInfo sensorInfo,
    	     libcamera.ControlInfoMap sensorControls)
    		=> (int32 ret,
    		    libcamera.ControlInfoMap ipaControls,
    		    bool ccmEnabled, bool lscEnabled);
    	start() => (int32 ret);
    	stop();
    	configure(IPAConfigInfo configInfo)
    		=> (int32 ret, libcamera.ControlInfoMap ipaControls);
    
    	[async] queueRequest(uint32 frame, libcamera.ControlList sensorControls);
    	[async] computeParams(uint32 frame);
    	[async] processStats(uint32 frame,
    			     uint32 bufferId,
    			     libcamera.ControlList sensorControls);
    };
    
    interface IPASoftIspEventInterface {
    	setSensorControls(libcamera.ControlList sensorControls);
    	paramsComputed(uint32 frame);
    	metadataReady(uint32 frame, libcamera.ControlList metadata);
    };
    ```


<!-- sdd:class-diagram -->
## 클래스 관계

화살표의 글자는 추출한 관계를 나타내며, 점선은 상속입니다. 화살표는 참조 대상 또는 기반 클래스를 향합니다. 호출 순서를 뜻하지 않습니다.

```mermaid
flowchart LR
  c0["IPAInterface"]:::context
  c1["IPAManager"]
  c2["IPAModule"]
  c3["IPAProxy"]
  c4["Loggable"]:::context
  c5["ipa::ipu3::IPAIPU3"]
  c6["ipa::ipu3::Module"]:::context
  c7["ipa::rkisp1::IPARkISP1"]
  c8["ipa::rkisp1::Module"]:::context
  c1 -->|필드 참조| c2
  c2 -.->|상속| c4
  c3 -.->|상속| c0
  c3 -->|필드 참조| c2
  c5 -.->|상속| c6
  c7 -.->|상속| c8
  classDef context fill:#fafafa,stroke:#aaa,stroke-dasharray:4 3,color:#555
```
<!-- /sdd:class-diagram -->



## 관련 클래스

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::IPAManager` | `include/libcamera/internal/ipa_manager.h:29` | – | Manager for IPA modules |
| `libcamera::IPAModule` | `include/libcamera/internal/ipa_module.h:21` | `libcamera::Loggable` | Wrapper around IPA module shared object |
| `libcamera::IPAProxy` | `include/libcamera/internal/ipa_proxy.h:22` | `libcamera::IPAInterface` | IPA Proxy |
| `libcamera::ipa::ipu3::IPAIPU3` | `src/ipa/ipu3/ipu3.cpp:139` | `libcamera::ipa::ipu3::Module` | The IPU3 IPA implementation |
| `libcamera::ipa::rkisp1::IPARkISP1` | `src/ipa/rkisp1/rkisp1.cpp:46` | `libcamera::ipa::rkisp1::Module` | 확인 필요 |

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `include/libcamera/internal/ipa_manager.h`, `include/libcamera/internal/ipa_module.h`, `include/libcamera/internal/ipa_proxy.h`, `include/libcamera/ipa/softisp.mojom`, `src/ipa/ipu3/ipu3.cpp`, `src/ipa/mali-c55/algorithms/meson.build`, `src/ipa/mali-c55/data/uncalibrated.yaml`, `src/ipa/rkisp1/data/uncalibrated.yaml`, `src/ipa/rkisp1/rkisp1.cpp`, `src/libcamera/egl.cpp`, `src/libcamera/ipa_manager.cpp`, `src/libcamera/ipa_module.cpp`, `src/libcamera/ipa_proxy.cpp`, `src/libcamera/pipeline/mali-c55/mali-c55.cpp`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp`, `src/libcamera/shaders/bayer_1x_packed.frag`, `src/libcamera/shaders/bayer_unpacked.frag`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `c19d05128f`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-12 · 사람 검토 전

다음 단계: [IPU3 LSC와 상태 연결](ipu3-lsc.md)
