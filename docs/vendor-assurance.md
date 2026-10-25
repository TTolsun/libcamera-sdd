---
generated_at: 2026-10-25T07:21:25+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: vendor-assurance
generation_method: facts-and-llm
evidence_fingerprint: eb2cf247d8d4dc42049ab9539e20ac389b7890967f9005310392c47eba2be0b8
semantic_review: human-review-required
agent: response-bundle/codex-session
generated_design: {"schema": 1, "input_fingerprint": "eb2cf247d8d4dc42049ab9539e20ac389b7890967f9005310392c47eba2be0b8", "answers": {"constraints": [{"text": "`CameraConfiguration::validate()`가 Valid를 반환하면 구성은 변경되지 않았습니다. Adjusted이면 유효한 구성으로 조정되었지만 스트림 파라미터가 달라지거나 스트림이 제거될 수 있으므로 호출자가 결과를 다시 확인해야 합니다. Invalid이면 유효하게 조정할 수 없는 구성입니다.", "covers": ["constraints"], "kind": "behavior", "quote": "\\fn CameraConfiguration::validate()\n * \\brief Validate and possibly adjust the camera configuration\n *\n * This function adjusts the camera configuration to the closest valid\n * configuration and returns the validation status.\n *\n * \\todo Define exactly when to return each status code. Should stream\n * parameters set to 0 by the caller be adjusted without returning Adjusted ?\n * This would potentially be useful for applications but would get in the way\n * in Camera::configure(). Do we need an extra status code to signal this ?\n *\n * \\todo Handle validation of buffers count when refactoring the buffers API.\n *\n * \\return A CameraConfiguration::Status value that describes the validation\n * status.\n * \\retval CameraConfiguration::Invalid The configuration is invalid and can't\n * be adjusted. This may only occur in extreme cases such as when the\n * configuration is empty.\n * \\retval CameraConfiguration::Adjusted The configuration has been adjusted\n * and is now valid. Parameters may have changed for any stream, and stream\n * configurations may have been removed. The caller shall check the\n * configuration carefully.\n * \\retval CameraConfiguration::Valid The configuration was already valid and\n * hasn't been adjusted.\n */", "evidence": ["validate"]}, {"text": "`PipelineHandler::generateConfiguration()`은 요청한 스트림 용도를 충족할 수 있을 때 유효한 구성을 반환하고, 충족할 수 없으면 null 포인터를 반환합니다. 따라서 요청한 용도를 그대로 지원한다고 가정하지 말고 반환된 스트림과 기본 파라미터를 확인해야 합니다.", "covers": ["constraints"], "kind": "behavior", "quote": "\\fn PipelineHandler::generateConfiguration()\n * \\brief Generate a camera configuration for a specified camera\n * \\param[in] camera The camera to generate a default configuration for\n * \\param[in] roles A list of stream roles\n *\n * Generate a default configuration for the \\a camera for a specified list of\n * stream roles. The caller shall populate the \\a roles with the use-cases it\n * wishes to fetch the default configuration for. The returned configuration\n * can then be examined by the caller to learn about the selected streams and\n * their default parameters.\n *\n * The intended companion to this is \\a configure() which can be used to change\n * the group of streams parameters.\n *\n * \\context This function may be called from any thread and shall be\n * \\threadsafe. It shall not modify the state of the \\a camera in the pipeline\n * handler.\n *\n * \\return A valid CameraConfiguration if the requested roles can be satisfied,\n * or a null pointer otherwise.\n */", "evidence": ["configuration"]}, {"text": "`PipelineHandler::configure()`는 이미 검증된 구성을 입력으로 받으며, 성공하면 0을, 실패하면 음수 오류 코드를 반환하는 계약입니다. 유효한 구성이라는 조건과 장치 구성 성공은 구분해야 합니다.", "covers": ["constraints"], "kind": "behavior", "quote": "/**\n * \\fn PipelineHandler::configure()\n * \\brief Configure a group of streams for capture\n * \\param[in] camera The camera to configure\n * \\param[in] config The camera configurations to setup\n *\n * Configure the specified group of streams for \\a camera according to the\n * configuration specified in \\a config. The intended caller of this interface\n * is the Camera class which will receive configuration to apply from the\n * application.\n *\n * The configuration is guaranteed to have been validated with\n * CameraConfiguration::validate(). The pipeline handler implementation shall\n * not perform further validation and may rely on any custom field stored in its\n * custom CameraConfiguration derived class.\n *\n * When configuring the camera the pipeline handler shall associate a Stream\n * instance to each StreamConfiguration entry in the CameraConfiguration using\n * the StreamConfiguration::setStream() function.\n *\n * \\context This function is called from the CameraManager thread.\n *\n * \\return 0 on success or a negative error code otherwise\n */", "evidence": ["configuration"]}], "measurement": [{"text": "`DebayerCpu`의 내장 벤치마크는 통계 수집과 디베이어 처리 시간을 측정합니다. 프레임 캡처와 출력 시간은 제외하므로 이 결과를 제품 전체의 촬영 지연으로 해석하면 안 됩니다.", "covers": ["measurement"], "kind": "behavior", "quote": "The DebayerCpu class has a builtin benchmark. This benchmark measures the time\nspent on processing (collecting statistics and debayering) only, it does not\nmeasure the time spent on capturing or outputting the frames.", "evidence": ["benchmark"]}, {"text": "Software ISP를 사용하는 파이프라인으로 cam이나 qcam을 실행하면 내장 벤치마크를 사용할 수 있습니다. 이는 upstream이 제공하는 측정 절차이며, 이 문서에서 대상 제품을 실행해 얻은 성능 결과는 아닙니다.", "covers": ["measurement"], "kind": "behavior", "quote": "The builtin benchmark always runs. So this can be used by simply running \"cam\"\nor \"qcam\" with a pipeline using the Software ISP.", "evidence": ["benchmark"]}]}, "topic_inputs": {"constraints": "be2c0b9c724e8f9557051d89c6df929de419c10657c13e14824da4b91b6f431a", "measurement": "8301d196b5f34bd2e342a1ddf06d1665afe994aada09ddb4100bac70d6a9c8a9"}, "reused_topics": [], "generated_topics": ["constraints", "measurement"], "topic_agents": {"constraints": "response-bundle/codex-session", "measurement": "response-bundle/codex-session"}, "body_sha256": "74f437ef83baeefa2b3671ef99b9081ed3164c10134404b59e7ca562696279da"}
---

# 지원 범위와 검증

**지원 조건과 구성 제약을 확인하고 제품 도입 전에 검증할 범위를 정하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| libcamera 제품 개요에서 필요한 내용을 확인합니다. | [libcamera 제품 개요](vendor-overview.md) |
| 연동 가이드에서 필요한 내용을 확인합니다. | [연동 가이드](vendor-integration.md) |
| 장치별 파이프라인을 구현합니다. | [Pipeline Handler](pipeline-handler.md) |

## 지원 조건과 제약

`CameraConfiguration::validate()`가 Valid를 반환하면 구성은 변경되지 않았습니다. Adjusted이면 유효한 구성으로 조정되었지만 스트림 파라미터가 달라지거나 스트림이 제거될 수 있으므로 호출자가 결과를 다시 확인해야 합니다. Invalid이면 유효하게 조정할 수 없는 구성입니다. `src/libcamera/camera.cpp:323`

`PipelineHandler::generateConfiguration()`은 요청한 스트림 용도를 충족할 수 있을 때 유효한 구성을 반환하고, 충족할 수 없으면 null 포인터를 반환합니다. 따라서 요청한 용도를 그대로 지원한다고 가정하지 말고 반환된 스트림과 기본 파라미터를 확인해야 합니다. `src/libcamera/pipeline_handler.cpp:271`

`PipelineHandler::configure()`는 이미 검증된 구성을 입력으로 받으며, 성공하면 0을, 실패하면 음수 오류 코드를 반환하는 계약입니다. 유효한 구성이라는 조건과 장치 구성 성공은 구분해야 합니다. `src/libcamera/pipeline_handler.cpp:271`

근거 원문: [src/libcamera/camera.cpp:323](#source-cb5242e98ac1e72c) · [src/libcamera/pipeline_handler.cpp:271](#source-c81d81d5cce53ab8)

## 성능 근거를 읽는 기준

`DebayerCpu`의 내장 벤치마크는 통계 수집과 디베이어 처리 시간을 측정합니다. 프레임 캡처와 출력 시간은 제외하므로 이 결과를 제품 전체의 촬영 지연으로 해석하면 안 됩니다. `Documentation/software-isp-benchmarking.rst:15`

Software ISP를 사용하는 파이프라인으로 cam이나 qcam을 실행하면 내장 벤치마크를 사용할 수 있습니다. 이는 upstream이 제공하는 측정 절차이며, 이 문서에서 대상 제품을 실행해 얻은 성능 결과는 아닙니다. `Documentation/software-isp-benchmarking.rst:15`

근거 원문: [Documentation/software-isp-benchmarking.rst:15](#source-9c8139bcb89eab5b)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 지원 전제와 제약은 무엇이며 별도 검증할 항목은 무엇입니까? | [지원 조건과 제약](#지원-조건과-제약) | 코드 근거와 설명 연결 |
    | 참고 벤치마크가 측정하는 범위와 별도 제품 검증 범위는 무엇입니까? | [성능 근거를 읽는 기준](#성능-근거를-읽는-기준) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-cb5242e98ac1e72c"></a>

??? note "소스 근거: src/libcamera/camera.cpp:323"
    `src/libcamera/camera.cpp:323`에서 시작하는 발췌입니다. 종료 줄은 350이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `a6c84f68e53cafd0f2721ee7eee586981059b62a93378a48235f86ffaa0a8fce`
    
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
     */
    
    /**
     * \brief Retrieve a reference to a stream configuration
    ```

<a id="source-c81d81d5cce53ab8"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:271"
    `src/libcamera/pipeline_handler.cpp:271`에서 시작하는 발췌입니다. 종료 줄은 319이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `5284e6062c894a77328b372676c42c1c97a4a01f9b2dccc4d09c83b2578b0e20`
    
    ```text
    \fn PipelineHandler::generateConfiguration()
     * \brief Generate a camera configuration for a specified camera
     * \param[in] camera The camera to generate a default configuration for
     * \param[in] roles A list of stream roles
     *
     * Generate a default configuration for the \a camera for a specified list of
     * stream roles. The caller shall populate the \a roles with the use-cases it
     * wishes to fetch the default configuration for. The returned configuration
     * can then be examined by the caller to learn about the selected streams and
     * their default parameters.
     *
     * The intended companion to this is \a configure() which can be used to change
     * the group of streams parameters.
     *
     * \context This function may be called from any thread and shall be
     * \threadsafe. It shall not modify the state of the \a camera in the pipeline
     * handler.
     *
     * \return A valid CameraConfiguration if the requested roles can be satisfied,
     * or a null pointer otherwise.
     */
    
    /**
     * \fn PipelineHandler::configure()
     * \brief Configure a group of streams for capture
     * \param[in] camera The camera to configure
     * \param[in] config The camera configurations to setup
     *
     * Configure the specified group of streams for \a camera according to the
     * configuration specified in \a config. The intended caller of this interface
     * is the Camera class which will receive configuration to apply from the
     * application.
     *
     * The configuration is guaranteed to have been validated with
     * CameraConfiguration::validate(). The pipeline handler implementation shall
     * not perform further validation and may rely on any custom field stored in its
     * custom CameraConfiguration derived class.
     *
     * When configuring the camera the pipeline handler shall associate a Stream
     * instance to each StreamConfiguration entry in the CameraConfiguration using
     * the StreamConfiguration::setStream() function.
     *
     * \context This function is called from the CameraManager thread.
     *
     * \return 0 on success or a negative error code otherwise
     */
    
    /**
     * \fn PipelineHandler::exportFrameBuffers()
    ```

<a id="source-9c8139bcb89eab5b"></a>

??? note "소스 근거: Documentation/software-isp-benchmarking.rst:15"
    `Documentation/software-isp-benchmarking.rst:15`에서 시작하는 발췌입니다. 종료 줄은 22이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `01df160bfdc79d4dd48c5e5316a7f3744ea6333454ab939c474cf739490984a3`
    
    ```text
    The DebayerCpu class has a builtin benchmark. This benchmark measures the time
    spent on processing (collecting statistics and debayering) only, it does not
    measure the time spent on capturing or outputting the frames.
    
    The builtin benchmark always runs. So this can be used by simply running "cam"
    or "qcam" with a pipeline using the Software ISP.
    
    When it runs it will skip
    ```


<!-- sdd:class-diagram -->
## 클래스 관계

화살표의 글자는 추출한 관계를 나타내며, 점선은 상속입니다. 화살표는 참조 대상 또는 기반 클래스를 향합니다. 호출 순서를 뜻하지 않습니다.

```mermaid
flowchart LR
  c0["Camera"]
  c1["Extensible"]:::context
  c2["IPAManager"]
  c3["Object"]:::context
  c4["PipelineHandler"]
  c5["PipelineHandlerIPU3"]
  c6["PipelineHandlerRkISP1"]
  c0 -.->|상속| c1
  c0 -.->|상속| c3
  c4 -->|필드 참조| c0
  c4 -.->|상속| c3
  c5 -.->|상속| c4
  c6 -->|필드 참조| c0
  c6 -.->|상속| c4
  classDef context fill:#fafafa,stroke:#aaa,stroke-dasharray:4 3,color:#555
```
<!-- /sdd:class-diagram -->

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `Documentation/software-isp-benchmarking.rst`, `include/libcamera/camera.h`, `include/libcamera/internal/ipa_manager.h`, `include/libcamera/internal/pipeline_handler.h`, `src/libcamera/camera.cpp`, `src/libcamera/ipa_manager.cpp`, `src/libcamera/pipeline/ipu3/ipu3.cpp`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp`, `src/libcamera/pipeline_handler.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `2c4b67c079`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-25 · 사람 검토 전

다음 단계: [요청 처리와 문제 진단](request-lifecycle.md)
