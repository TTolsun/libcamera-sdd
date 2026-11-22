---
generated_at: 2026-11-22T17:38:44+00:00
source_commit: adfa719f8ed67d18fd8a0739fc088a1f8b9e7252
status: ok
section: uvc-viewfinder-configuration
generation_method: facts-and-llm
evidence_fingerprint: 47169a645a6da1d6d2bd53aa3c9a992ca3a88b5976d389f0a822e305f1e0eef2
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "47169a645a6da1d6d2bd53aa3c9a992ca3a88b5976d389f0a822e305f1e0eef2", "answers": {"uvc-viewfinder": [{"text": "예제 앱은 `Viewfinder` 스트림 한 개를 요청하고 크기를 640×480으로 설정합니다. 앱은 변경한 구성을 카메라에 적용하기 전에 `validate()`로 검증해야 하며, 지원하지 않는 값은 가장 가까운 지원 값으로 조정됩니다. 예제 코드는 반환값을 사용하지 않고 `toString()`으로 구성을 출력하지만, 호출자는 상태를 확인해야 하며 `Adjusted`이면 스트림이 빠졌는지와 남은 스트림의 크기와 픽셀 포맷 등 매개변수가 바뀌었는지 구성 전체를 살펴 수용 여부를 결정해야 합니다. `Invalid`는 구성을 유효하게 조정할 수 없다는 뜻이며, `Valid`는 구성이 이미 유효하여 조정되지 않았다는 뜻입니다.", "evidence": ["app-default", "app-request", "app-validated-output", "validation-contract"], "covers": ["uvc-viewfinder"], "kind": "behavior", "quote": "If an application changes any parameters, it must validate the configuration\nbefore applying it to the camera using the ``CameraConfiguration::validate()``\nfunction. If the new values are not supported by the ``Camera`` device, the\nvalidation process adjusts the parameters to what it considers to be the closest\nsupported values.", "part_id": "app-validation"}, {"text": "`Camera::configure`는 접근 검사에서 음수 오류가 나면 이를 반환하고, 스트림 연결을 초기화한 뒤 재검증 결과가 `Valid`가 아니면 `-EINVAL`을 반환합니다. `UVCCameraConfiguration::validate`는 지원하지 않는 픽셀 포맷을 목록의 첫 값으로 바꾸고, 선택한 포맷의 크기 목록에서 첫 값으로 시작해 요청 크기보다 큰 값이 나오기 전까지 크기를 갱신한 뒤 `tryFormat`으로 시험하며 실패하면 `Invalid`를 반환합니다. `PipelineHandlerUVC::configure`는 포맷과 크기를 `setFormat`으로 장치에 적용하고, 호출에 실패하면 그 오류를 그대로 반환합니다. 호출이 성공한 뒤 반환된 크기 또는 `FourCC`가 재검증을 통과한 구성과 다르면 `-EINVAL`을 반환하며, 처음 요청한 크기가 640×480인 경우에도 비교 기준은 재검증을 통과한 구성입니다.", "evidence": ["camera-configure", "uvc-validate", "uvc-configure", "v4l2-configure"], "covers": ["uvc-viewfinder"], "kind": "behavior", "quote": "if (format.size != cfg.size ||\n\t    format.fourcc != data->video_->toV4L2PixelFormat(cfg.pixelFormat))\n\t\treturn -EINVAL;", "part_id": "device-apply"}, {"text": "`UVCCameraConfiguration::validate()`는 `tryFormat`이 성공하면 첫 평면의 `bpl`과 `size`를 각각 `cfg.stride`와 `cfg.frameSize`에 쓰고, `colorSpace`가 다르면 반환된 값으로 바꾸어 `Adjusted`로 표시합니다. `PipelineHandlerUVC::configure()`는 `setFormat`이 성공한 뒤 크기와 FourCC만 비교하며, `stride`, `frameSize`, `colorSpace`는 그 결과와 비교하거나 덮어쓰지 않습니다. UVC가 `cfg`에 스트림을 연결하면 `Camera::configure()`는 검증된 `cfg`를 활성 스트림에 복사하며, 성공 뒤 `Stream::configuration()`은 이 활성 설정을 반환합니다. 특정 장치의 실제 값은 이 소스만으로 정할 수 없습니다.", "evidence": ["uvc-validate", "uvc-configure", "camera-configure", "app-stream"], "covers": ["uvc-viewfinder"], "kind": "behavior", "quote": "cfg.stride = format.planes[0].bpl;\n\tcfg.frameSize = format.planes[0].size;", "part_id": "active-values"}]}, "topic_inputs": {"uvc-viewfinder": "260ce8cb8580117a74fccf1bf3772b5be838cf8fc02fdba3bb95400d0fe6f3b7"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["uvc-viewfinder"], "topic_agents": {"uvc-viewfinder": "cli/codex/gpt-6.1-terra"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "367d18b95f8f0d01a15ae0f4d1b70f7e13e4d0298df4215e2c449ac4905db6f9", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "434377186c836fa9d0ea02f9e7b91f624da454b0602ec710fa2993ed69fe1e38", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "431db4b3b3c833fc43b72b53cdce2f89ac9a0b9820d80e73e991b86c44e2def5", "answer_contracts": "a39c9a8818afc47e059141d486337c0f12a7fd34319e2b6f7674fc428bc83e2b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "050c20aa2fdcceae10c6275fbb5f850f616ab5051bb67ccbcb4a204877a238d9", "explanation": "69bcaa207ef39d20f6a47ac201c3edf119f59b333e85131dea1bce85eef4006b", "design_response": "75bc218537312e8668e52aed9d6e4b214ba73fd77b90b5f87698a54187eacbbc", "design_validation": "c6102dcac1aabb437612d92870bd35551cf7990a4eaca52bfe3d9cd17697d330"}, "validation_model": "86c4e3d0d9ea368df6df9ac2535d21f0fd2f83f210acd6f3c16da880e9e9f033", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "b87a84b1bc31079837dc4dc4527ce02c9dc2cbc3a26ff7e99e0872941d213995"}, "checkpoint_units": [{"checkpoint": "fcdbbc0f82b0ec797dadf0f464ad035aea640fec612dfa622dd863cf0554a899.json", "topic": "uvc-viewfinder", "part": "app-validation", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["6c1ad49275b0469cb19da9582524b6ea/001.receipt.json", "6c1ad49275b0469cb19da9582524b6ea/002.receipt.json"]}, {"checkpoint": "71cf1c9c00d7411ce817f159b5c0f9bb7e877acb26514d37dfa5fb72b98ef505.json", "topic": "uvc-viewfinder", "part": "device-apply", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["7accf3bc1cb44224a5e3113d9fca8489/005.receipt.json", "7accf3bc1cb44224a5e3113d9fca8489/006.receipt.json", "7accf3bc1cb44224a5e3113d9fca8489/007.receipt.json", "7accf3bc1cb44224a5e3113d9fca8489/008.receipt.json"]}, {"checkpoint": "f947d165cd1bac3af21b414f409e2abcab4d09cb093dbd132b96dc6f6d0f898f.json", "topic": "uvc-viewfinder", "part": "active-values", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["7accf3bc1cb44224a5e3113d9fca8489/009.receipt.json", "7accf3bc1cb44224a5e3113d9fca8489/010.receipt.json"]}], "body_sha256": "62c8c622ea5ba4c1b9b4931b3f8a4a79f7b916bd9bea9eaa5c75af41b0c4b884"}
---

# USB UVC 뷰파인더 스트림 구성

**USB UVC 뷰파인더 하나를 요청하는 예로, 소스에서 앱의 검증 결과와 장치 적용 시의 크기·FourCC 비교를 따라가세요.**



## 요청한 640×480 뷰파인더는 어디에서 달라지나요?

예제 앱은 `Viewfinder` 스트림 한 개를 요청하고 크기를 640×480으로 설정합니다. 앱은 변경한 구성을 카메라에 적용하기 전에 `validate()`로 검증해야 하며, 지원하지 않는 값은 가장 가까운 지원 값으로 조정됩니다. 예제 코드는 반환값을 사용하지 않고 `toString()`으로 구성을 출력하지만, 호출자는 상태를 확인해야 하며 `Adjusted`이면 스트림이 빠졌는지와 남은 스트림의 크기와 픽셀 포맷 등 매개변수가 바뀌었는지 구성 전체를 살펴 수용 여부를 결정해야 합니다. `Invalid`는 구성을 유효하게 조정할 수 없다는 뜻이며, `Valid`는 구성이 이미 유효하여 조정되지 않았다는 뜻입니다. `Documentation/guides/application-developer.rst:167`, `Documentation/guides/application-developer.rst:195`, `Documentation/guides/application-developer.rst:222`, `src/libcamera/camera.cpp:323`

<!-- sdd:visual:uvc-viewfinder-format-checks -->
### UVC 뷰파인더의 구성 검증과 장치 적용

```mermaid
flowchart TB
%% sdd:translations {"Adjusted": "Adjusted", "Camera::configure 재검증": "Camera::configure <br/>revalidates", "Invalid": "Invalid", "Invalid 또는 Adjusted": "Invalid or Adjusted", "UVC가 setFormat 호출": "UVC calls setFormat", "UVC에서 -EINVAL": "UVC returns -EINVAL", "Valid": "Valid", "검증 구성을 복사한 Stream을 <br/>앱에서 확인": "App reads the Stream#39;s <br/>copied validation <br/>configuration", "공통 검증에서 -EINVAL": "Common validation returns <br/>-EINVAL", "반환 크기와 FourCC가 일치?": "Do the returned size and <br/>FourCC match?", "변경값 거절": "Decline changes", "변경값 수용": "Accept changes", "불일치": "Mismatch", "성공": "Success", "앱이 validate 호출": "App calls validate", "오류": "Error", "일치": "Match", "장치 적용 오류 전달": "Forward the format-setting <br/>error", "호출자가 변경값 수용 여부 <br/>판단": "Caller decides whether to <br/>accept changes", "호출자가 적용을 진행하지 <br/>않음": "Caller stops before applying"}
  v_validate{"앱이 validate 호출"}
  v_inspect["호출자가 변경값 수용 여부 <br/>판단"]
  v_stop["호출자가 적용을 진행하지 <br/>않음"]
  v_gate{"Camera::configure 재검증"}
  v_reject["공통 검증에서 -EINVAL"]
  v_apply{"UVC가 setFormat 호출"}
  v_error["장치 적용 오류 전달"]
  v_compare{"반환 크기와 FourCC가 일치?"}
  v_mismatch["UVC에서 -EINVAL"]
  v_linked["검증 구성을 복사한 Stream을 <br/>앱에서 확인"]
  v_validate -->|"Adjusted"| v_inspect
  v_validate -->|"Invalid"| v_stop
  v_validate -->|"Valid"| v_gate
  v_inspect -->|"변경값 수용"| v_gate
  v_inspect -->|"변경값 거절"| v_stop
  v_gate -->|"Valid"| v_apply
  v_gate -->|"Invalid 또는 Adjusted"| v_reject
  v_apply -->|"오류"| v_error
  v_apply -->|"성공"| v_compare
  v_compare -->|"불일치"| v_mismatch
  v_compare -->|"일치"| v_linked
```

<span data-sdd-label-en="The official guide example calls validate and prints the configuration. The accept and decline branches show decisions for the caller. UVC stores stride, frameSize, and colorSpace from tryFormat in the configuration. After setFormat succeeds, it compares only the size and FourCC.">공식 가이드 예제는 validate를 호출하고 구성을 출력합니다. 그림의 수용·거절은 호출자가 할 판단입니다. UVC는 tryFormat에서 얻은 stride·frameSize·colorSpace를 구성에 저장하고, setFormat 성공 뒤에는 크기와 FourCC만 비교합니다.</span> <a data-sdd-caption-source="true" href="https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/Documentation/guides/application-developer.rst#L228"><code>application-developer.rst:228</code></a> · <a data-sdd-caption-source="true" href="https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/camera.cpp#L343"><code>camera.cpp:343</code></a> · <a data-sdd-caption-source="true" href="https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline/uvcvideo/uvcvideo.cpp#L220"><code>uvcvideo.cpp:220</code></a> · <a data-sdd-caption-source="true" href="https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline/uvcvideo/uvcvideo.cpp#L224"><code>uvcvideo.cpp:224</code></a> · <a data-sdd-caption-source="true" href="https://github.com/TTolsun/libcamera-sdd/blob/adfa719f8ed67d18fd8a0739fc088a1f8b9e7252/src/libcamera/pipeline/uvcvideo/uvcvideo.cpp#L275"><code>uvcvideo.cpp:275</code></a>

[Mermaid 원문](uvc-viewfinder-configuration.uvc-viewfinder-format-checks.mmd)

??? note "그림 근거와 확인 범위"
    어디에서 값을 다시 확인하고 어디에서 오류로 반환합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="App calls validate">앱이 validate 호출</span> | [Documentation/guides/application-developer.rst:222](#source-b7102b06d767f1b8) |
    | <span data-sdd-label-en="Caller decides whether to accept changes">호출자가 변경값 수용 여부 판단</span> | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
    | <span data-sdd-label-en="Caller stops before applying">호출자가 적용을 진행하지 않음</span> | [src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:139](#source-f9631255f305fb92) · [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
    | <span data-sdd-label-en="Camera::configure revalidates">Camera::configure 재검증</span> | [src/libcamera/camera.cpp:1191](#source-603af0dd7fa357d0) |
    | <span data-sdd-label-en="Common validation returns -EINVAL">공통 검증에서 -EINVAL</span> | [src/libcamera/camera.cpp:1191](#source-603af0dd7fa357d0) |
    | <span data-sdd-label-en="UVC calls setFormat">UVC가 setFormat 호출</span> | [src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:261](#source-be07a7077dd3d924) · [src/libcamera/v4l2_videodevice.cpp:849](#source-c073a10f1abc63b6) |
    | <span data-sdd-label-en="Forward the format-setting error">장치 적용 오류 전달</span> | [src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:261](#source-be07a7077dd3d924) |
    | <span data-sdd-label-en="Do the returned size and FourCC match?">반환 크기와 FourCC가 일치?</span> | [src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:261](#source-be07a7077dd3d924) |
    | <span data-sdd-label-en="UVC returns -EINVAL">UVC에서 -EINVAL</span> | [src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:261](#source-be07a7077dd3d924) |
    | <span data-sdd-label-en="App reads the Stream&#x27;s copied validation configuration">검증 구성을 복사한 Stream을 앱에서 확인</span> | [src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:261](#source-be07a7077dd3d924) · [src/libcamera/camera.cpp:1191](#source-603af0dd7fa357d0) · [src/libcamera/stream.cpp:483](#source-d8739fc139164c42) |
    | <span data-sdd-label-en="Adjusted">Adjusted</span> | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
    | <span data-sdd-label-en="Invalid">Invalid</span> | [src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:139](#source-f9631255f305fb92) |
    | <span data-sdd-label-en="Valid">Valid</span> | [src/libcamera/camera.cpp:1191](#source-603af0dd7fa357d0) |
    | <span data-sdd-label-en="Accept changes">변경값 수용</span> | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) · [src/libcamera/camera.cpp:1191](#source-603af0dd7fa357d0) |
    | <span data-sdd-label-en="Decline changes">변경값 거절</span> | [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) |
    | <span data-sdd-label-en="Valid">Valid</span> | [src/libcamera/camera.cpp:1191](#source-603af0dd7fa357d0) · [src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:261](#source-be07a7077dd3d924) |
    | <span data-sdd-label-en="Invalid or Adjusted">Invalid 또는 Adjusted</span> | [src/libcamera/camera.cpp:1191](#source-603af0dd7fa357d0) |
    | <span data-sdd-label-en="Error">오류</span> | [src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:261](#source-be07a7077dd3d924) |
    | <span data-sdd-label-en="Success">성공</span> | [src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:261](#source-be07a7077dd3d924) |
    | <span data-sdd-label-en="Mismatch">불일치</span> | [src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:261](#source-be07a7077dd3d924) |
    | <span data-sdd-label-en="Match">일치</span> | [src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:261](#source-be07a7077dd3d924) · [src/libcamera/camera.cpp:1191](#source-603af0dd7fa357d0) |
<!-- /sdd:visual:uvc-viewfinder-format-checks -->

`Camera::configure`는 접근 검사에서 음수 오류가 나면 이를 반환하고, 스트림 연결을 초기화한 뒤 재검증 결과가 `Valid`가 아니면 `-EINVAL`을 반환합니다. `UVCCameraConfiguration::validate`는 지원하지 않는 픽셀 포맷을 목록의 첫 값으로 바꾸고, 선택한 포맷의 크기 목록에서 첫 값으로 시작해 요청 크기보다 큰 값이 나오기 전까지 크기를 갱신한 뒤 `tryFormat`으로 시험하며 실패하면 `Invalid`를 반환합니다. `PipelineHandlerUVC::configure`는 포맷과 크기를 `setFormat`으로 장치에 적용하고, 호출에 실패하면 그 오류를 그대로 반환합니다. 호출이 성공한 뒤 반환된 크기 또는 `FourCC`가 재검증을 통과한 구성과 다르면 `-EINVAL`을 반환하며, 처음 요청한 크기가 640×480인 경우에도 비교 기준은 재검증을 통과한 구성입니다. `src/libcamera/camera.cpp:1191`, `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:139`, `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:261`, `src/libcamera/v4l2_videodevice.cpp:849`

`UVCCameraConfiguration::validate()`는 `tryFormat`이 성공하면 첫 평면의 `bpl`과 `size`를 각각 `cfg.stride`와 `cfg.frameSize`에 쓰고, `colorSpace`가 다르면 반환된 값으로 바꾸어 `Adjusted`로 표시합니다. `PipelineHandlerUVC::configure()`는 `setFormat`이 성공한 뒤 크기와 FourCC만 비교하며, `stride`, `frameSize`, `colorSpace`는 그 결과와 비교하거나 덮어쓰지 않습니다. UVC가 `cfg`에 스트림을 연결하면 `Camera::configure()`는 검증된 `cfg`를 활성 스트림에 복사하며, 성공 뒤 `Stream::configuration()`은 이 활성 설정을 반환합니다. 특정 장치의 실제 값은 이 소스만으로 정할 수 없습니다. `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:139`, `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:261`, `src/libcamera/camera.cpp:1191`, `src/libcamera/stream.cpp:483`

근거 원문: [Documentation/guides/application-developer.rst:167](#source-fa38f671a1d155da) · [Documentation/guides/application-developer.rst:195](#source-8e1f5d84ca64a38b) · [Documentation/guides/application-developer.rst:222](#source-b7102b06d767f1b8) · [src/libcamera/camera.cpp:323](#source-2b31e92e3fb3f083) · [src/libcamera/camera.cpp:1191](#source-603af0dd7fa357d0) · [src/libcamera/stream.cpp:483](#source-d8739fc139164c42) · [src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:139](#source-f9631255f305fb92) · [src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:237](#source-472189bfe0703702) · [src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:261](#source-be07a7077dd3d924) · [src/libcamera/v4l2_videodevice.cpp:849](#source-c073a10f1abc63b6)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | USB UVC에 뷰파인더 스트림 하나를 640×480으로 요청하면 앱과 장치에서 어떤 값을 확인합니까? | [요청한 640×480 뷰파인더는 어디에서 달라지나요?](#요청한-640480-뷰파인더는-어디에서-달라지나요) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-fa38f671a1d155da"></a>

??? note "소스 근거: Documentation/guides/application-developer.rst:167"
    `Documentation/guides/application-developer.rst:167`에서 시작하는 발췌입니다. 종료 줄은 185이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `4c979423c6366a0c6d46d9b4254987ba40da86687ebd4c225c51a12952d2b8ff`
    
    ```text
    In the example application, create a new configuration variable and use the
    ``Camera::generateConfiguration`` function to produce a ``CameraConfiguration``
    for the single ``StreamRole::Viewfinder`` role.
    
    .. code:: cpp
    
       std::unique_ptr<CameraConfiguration> config = camera->generateConfiguration( { StreamRole::Viewfinder } );
    
    The generated ``CameraConfiguration`` has a ``StreamConfiguration`` instance for
    each ``StreamRole`` the application requested. Each of these has a default size
    and format that the camera assigned, and a list of supported pixel formats and
    sizes.
    
    The code below accesses the first and only ``StreamConfiguration`` item in the
    ``CameraConfiguration`` and outputs its parameters to standard output.
    
    .. code:: cpp
    
       StreamConfiguration &streamConfig = config->at(0);
    ```

<a id="source-8e1f5d84ca64a38b"></a>

??? note "소스 근거: Documentation/guides/application-developer.rst:195"
    `Documentation/guides/application-developer.rst:195`에서 시작하는 발췌입니다. 종료 줄은 211이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `8622777258c395784a04059b948b8ba00f3e130df6260b7002adb2d5b5f36ddd`
    
    ```text
    With an initialized ``CameraConfiguration``, an application can make changes to
    the parameters it contains, for example, to change the width and height, use the
    following code:
    
    .. code:: cpp
    
       streamConfig.size.width = 640;
       streamConfig.size.height = 480;
    
    If an application changes any parameters, it must validate the configuration
    before applying it to the camera using the ``CameraConfiguration::validate()``
    function. If the new values are not supported by the ``Camera`` device, the
    validation process adjusts the parameters to what it considers to be the closest
    supported values.
    
    The ``validate`` function returns a :doxy-pub:`CameraConfiguration::Status`
    which applications shall check to see if the Pipeline Handler adjusted the
    ```

<a id="source-b7102b06d767f1b8"></a>

??? note "소스 근거: Documentation/guides/application-developer.rst:222"
    `Documentation/guides/application-developer.rst:222`에서 시작하는 발췌입니다. 종료 줄은 239이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `7341104156eb8e07b967545a6776a355789e5e9d9006370cd378478c7f657b7b`
    
    ```text
    For this example application, the code below prints the adjusted values to
    standard out.
    
    .. code:: cpp
    
       config->validate();
       std::cout << "Validated viewfinder configuration is: " << streamConfig.toString() << std::endl;
    
    For example, the output might be something like
    
       ``Validated viewfinder configuration is: 320x240-MJPEG``
    
    A validated ``CameraConfiguration`` can bet given to the ``Camera`` device to be
    applied to the system.
    
    .. code:: cpp
    
       camera->configure(config.get());
    ```

<a id="source-2b31e92e3fb3f083"></a>

??? note "소스 근거: src/libcamera/camera.cpp:323"
    `src/libcamera/camera.cpp:323`에서 시작하는 발췌입니다. 종료 줄은 346이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `86bf9109257512866bf70a5d42cd3da29c70d851d871f0e496058141ba377623`
    
    ```text
    \fn CameraConfiguration::validate()
     * \brief Validate and possibly adjust the camera configuration
     *
     * This function adjusts the camera configuration to the closest valid
     * configuration and returns the validation status.
     *
     * \todo Define exactly when to return each status code. Should stream
     * parameters set to 0 by the caller be adjusted without returning Adjusted ?
     * This would potentially be useful for applications but would get in the way
     * in Camera::configure(). Do we need an extra status code to signal this ?
     *
     * \todo Handle validation of buffers count when refactoring the buffers API.
     *
     * \return A CameraConfiguration::Status value that describes the validation
     * status.
     * \retval CameraConfiguration::Invalid The configuration is invalid and can't
     * be adjusted. This may only occur in extreme cases such as when the
     * configuration is empty.
     * \retval CameraConfiguration::Adjusted The configuration has been adjusted
     * and is now valid. Parameters may have changed for any stream, and stream
     * configurations may have been removed. The caller shall check the
     * configuration carefully.
     * \retval CameraConfiguration::Valid The configuration was already valid and
     * hasn't been adjusted.
    ```

<a id="source-603af0dd7fa357d0"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1191"
    `src/libcamera/camera.cpp:1191`에서 시작하는 발췌입니다. 종료 줄은 1240이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `ff6ceda14768503bdfe753d462853457743d5b46a80e0808a97375632403cd36`
    
    ```text
    int Camera::configure(CameraConfiguration *config)
    {
    	Private *const d = _d();
    
    	int ret = d->isAccessAllowed(Private::CameraAcquired,
    				     Private::CameraConfigured);
    	if (ret < 0)
    		return ret;
    
    	for (auto &cfg : *config)
    		cfg.setStream(nullptr);
    
    	if (config->validate() != CameraConfiguration::Valid) {
    		LOG(Camera, Error)
    			<< "Can't configure camera with invalid configuration";
    		return -EINVAL;
    	}
    
    	std::ostringstream msg("configuring streams:", std::ios_base::ate);
    
    	for (unsigned int index = 0; index < config->size(); ++index) {
    		StreamConfiguration &cfg = config->at(index);
    		msg << " (" << index << ") " << cfg.toString();
    	}
    
    	LOG(Camera, Info) << msg.str();
    
    	ret = d->pipe_->invokeMethod(&PipelineHandler::configure,
    				     ConnectionTypeBlocking, this, config);
    	if (ret)
    		return ret;
    
    	d->activeStreams_.clear();
    	for (const StreamConfiguration &cfg : *config) {
    		Stream *stream = cfg.stream();
    		if (!stream) {
    			LOG(Camera, Fatal)
    				<< "Pipeline handler failed to update stream configuration";
    			d->activeStreams_.clear();
    			return -EINVAL;
    		}
    
    		stream->configuration_ = cfg;
    		d->activeStreams_.insert(stream);
    	}
    
    	d->setState(Private::CameraConfigured);
    
    	return 0;
    }
    ```

<a id="source-d8739fc139164c42"></a>

??? note "소스 근거: src/libcamera/stream.cpp:483"
    `src/libcamera/stream.cpp:483`에서 시작하는 발췌입니다. 종료 줄은 485이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `3eb085cd58d1f1912392208e4a1fd6526d5fefdf597defc79f3a718152203a35`
    
    ```text
    \fn Stream::configuration()
     * \brief Retrieve the active configuration of the stream
     * \return The active configuration of the stream
    ```

<a id="source-f9631255f305fb92"></a>

??? note "소스 근거: src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:139"
    `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:139`에서 시작하는 발췌입니다. 종료 줄은 228이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `0aa2dad19ebf8758da23af411ff5e8983d194b5566eb48902b915288aceb52e4`
    
    ```text
    CameraConfiguration::Status UVCCameraConfiguration::validate()
    {
    	Status status = Valid;
    
    	if (config_.empty())
    		return Invalid;
    
    	if (sensorConfig)
    		return Invalid;
    
    	if (orientation != Orientation::Rotate0) {
    		orientation = Orientation::Rotate0;
    		status = Adjusted;
    	}
    
    	/* Cap the number of entries to the available streams. */
    	if (config_.size() > 1) {
    		config_.resize(1);
    		status = Adjusted;
    	}
    
    	StreamConfiguration &cfg = config_[0];
    	const StreamFormats &formats = cfg.formats();
    	const PixelFormat pixelFormat = cfg.pixelFormat;
    	const Size size = cfg.size;
    
    	const std::vector<PixelFormat> pixelFormats = formats.pixelformats();
    	auto iter = std::find(pixelFormats.begin(), pixelFormats.end(), pixelFormat);
    	if (iter == pixelFormats.end()) {
    		cfg.pixelFormat = pixelFormats.front();
    		LOG(UVC, Debug)
    			<< "Adjusting pixel format from " << pixelFormat
    			<< " to " << cfg.pixelFormat;
    		status = Adjusted;
    	}
    
    	const std::vector<Size> &formatSizes = formats.sizes(cfg.pixelFormat);
    	cfg.size = formatSizes.front();
    	for (const Size &formatsSize : formatSizes) {
    		if (formatsSize > size)
    			break;
    
    		cfg.size = formatsSize;
    	}
    
    	if (cfg.size != size) {
    		LOG(UVC, Debug)
    			<< "Adjusting size from " << size << " to " << cfg.size;
    		status = Adjusted;
    	}
    
    	cfg.bufferCount = 4;
    
    	V4L2DeviceFormat format;
    	format.fourcc = data_->video_->toV4L2PixelFormat(cfg.pixelFormat);
    	format.size = cfg.size;
    
    	/*
    	 * For power-consumption reasons video_ is closed when the camera is not
    	 * acquired. Open it here if necessary.
    	 */
    	{
    		bool opened = false;
    
    		MutexLocker locker(data_->openLock_);
    
    		if (!data_->video_->isOpen()) {
    			int ret = data_->video_->open();
    			if (ret)
    				return Invalid;
    
    			opened = true;
    		}
    
    		int ret = data_->video_->tryFormat(&format);
    		if (opened)
    			data_->video_->close();
    		if (ret)
    			return Invalid;
    	}
    
    	cfg.stride = format.planes[0].bpl;
    	cfg.frameSize = format.planes[0].size;
    
    	if (cfg.colorSpace != format.colorSpace) {
    		cfg.colorSpace = format.colorSpace;
    		status = Adjusted;
    	}
    
    	return status;
    ```

<a id="source-472189bfe0703702"></a>

??? note "소스 근거: src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:237"
    `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:237`에서 시작하는 발췌입니다. 종료 줄은 259이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `22b1012c12a6a470a68df096c8e06de88ceadb99939282daea8ffddfb98d7f9e`
    
    ```text
    PipelineHandlerUVC::generateConfiguration(Camera *camera,
    					  std::span<const StreamRole> roles)
    {
    	UVCCameraData *data = cameraData(camera);
    	std::unique_ptr<CameraConfiguration> config =
    		std::make_unique<UVCCameraConfiguration>(data);
    
    	if (roles.empty())
    		return config;
    
    	StreamFormats formats(data->formats_);
    	StreamConfiguration cfg(formats);
    
    	cfg.pixelFormat = formats.pixelformats().front();
    	cfg.size = formats.sizes(cfg.pixelFormat).back();
    	cfg.bufferCount = 4;
    
    	config->addConfiguration(cfg);
    
    	config->validate();
    
    	return config;
    }
    ```

<a id="source-be07a7077dd3d924"></a>

??? note "소스 근거: src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:261"
    `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:261`에서 시작하는 발췌입니다. 종료 줄은 282이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `826ac6a4484d5becacb65c669f4f122fadbbc0e92e1f128d67490a07a33ec0cb`
    
    ```text
    int PipelineHandlerUVC::configure(Camera *camera, CameraConfiguration *config)
    {
    	UVCCameraData *data = cameraData(camera);
    	StreamConfiguration &cfg = config->at(0);
    	int ret;
    
    	V4L2DeviceFormat format;
    	format.fourcc = data->video_->toV4L2PixelFormat(cfg.pixelFormat);
    	format.size = cfg.size;
    
    	ret = data->video_->setFormat(&format);
    	if (ret)
    		return ret;
    
    	if (format.size != cfg.size ||
    	    format.fourcc != data->video_->toV4L2PixelFormat(cfg.pixelFormat))
    		return -EINVAL;
    
    	cfg.setStream(&data->stream_);
    
    	return 0;
    }
    ```

<a id="source-c073a10f1abc63b6"></a>

??? note "소스 근거: src/libcamera/v4l2_videodevice.cpp:849"
    `src/libcamera/v4l2_videodevice.cpp:849`에서 시작하는 발췌입니다. 종료 줄은 887이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `9af0934ba2b90c413087e374e9b67b49768f06adeb723a56ce45abe73a8814c9`
    
    ```text
    \brief Configure an image format on the V4L2 video device
     * \param[inout] format The image format to apply to the video device
     *
     * Apply the supplied \a format to the video device, and return the actually
     * applied format parameters, as \ref V4L2VideoDevice::getFormat would do.
     *
     * \return 0 on success or a negative error code otherwise
     */
    int V4L2VideoDevice::setFormat(V4L2DeviceFormat *format)
    {
    	int ret;
    
    	switch (bufferType_) {
    	case V4L2_BUF_TYPE_VIDEO_CAPTURE:
    	case V4L2_BUF_TYPE_VIDEO_OUTPUT:
    		ret = trySetFormatSingleplane(format, true);
    		break;
    	case V4L2_BUF_TYPE_VIDEO_CAPTURE_MPLANE:
    	case V4L2_BUF_TYPE_VIDEO_OUTPUT_MPLANE:
    		ret = trySetFormatMultiplane(format, true);
    		break;
    	case V4L2_BUF_TYPE_META_CAPTURE:
    	case V4L2_BUF_TYPE_META_OUTPUT:
    		ret = trySetFormatMeta(format, true);
    		break;
    	default:
    		ret = -EINVAL;
    		break;
    	}
    
    	/* Cache the set format on success. */
    	if (ret)
    		return ret;
    
    	format_ = *format;
    	formatInfo_ = &PixelFormatInfo::info(format_.fourcc);
    
    	return 0;
    }
    ```

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `Documentation/guides/application-developer.rst`, `src/libcamera/camera.cpp`, `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp`, `src/libcamera/stream.cpp`, `src/libcamera/v4l2_videodevice.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `adfa719f8e`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-23 · 사람 검토 전

다음 단계: [시스템 개요](../overview.md)
