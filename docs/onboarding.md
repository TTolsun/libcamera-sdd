---
generated_at: 2026-10-29T22:35:49+00:00
source_commit: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61
status: ok
section: onboarding
generation_method: facts-and-llm
evidence_fingerprint: 87424992956beb9f6d59f825944a1136a38c1acb800575d2fa4c87daf994a388
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "87424992956beb9f6d59f825944a1136a38c1acb800575d2fa4c87daf994a388", "answers": {"why": [{"text": "애플리케이션은 queueRequest를 호출하기 전에 createRequest()로 할당한 요청에 캡처 버퍼를 하나 이상 채워야 합니다. 버퍼가 없는 요청은 유효하지 않아 큐에 추가되지 않고 거부됩니다. 요청이 큐에 추가되면 카메라는 requestCompleted 시그널로 완료를 알립니다.", "evidence": ["accept"], "covers": ["why"], "kind": "behavior", "quote": "This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.", "part_id": "accept"}, {"text": "마지막 버퍼가 완료될 때 요청은 자동으로 완료되지 않습니다. 이는 파이프라인 핸들러가 아직 필요할 수 있는 작업을 수행할 기회를 주기 위함입니다. 파이프라인 핸들러는 completeRequest()로 요청을 명시적으로 완료해야 합니다.", "evidence": ["buffer"], "covers": ["why"], "kind": "behavior", "quote": "This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().", "part_id": "buffer"}, {"text": "요청은 제출된 순서대로 애플리케이션에 반환됩니다. 파이프라인 핸들러는 완료된 요청에 대해 순서 제약 없이 completeRequest()를 호출할 수 있습니다.", "evidence": ["order"], "covers": ["why"], "kind": "behavior", "quote": "The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.", "part_id": "order"}], "try": [{"text": "시스템에서 감지된 카메라 목록은 `cam -l`로 확인할 수 있습니다. 첫 번째 카메라에서 10프레임을 캡처하여 디스크에 저장하려면 `cam -c 1 --capture=10 --file`을 사용합니다. 문제가 발생하면 `LIBCAMERA_LOG_LEVELS=*:DEBUG cam -l`로 환경 변수를 설정하여 libcamera의 상세 디버그 로그를 얻을 수 있습니다.", "evidence": ["cam"], "covers": ["try"], "kind": "behavior", "quote": "The ``cam`` utility can be used for basic testing. You can list the cameras\ndetected on the system with ``cam -l``, and capture ten frames from the first\ncamera and save them to disk with ``cam -c 1 --capture=10 --file``. See\n``cam -h`` for more information about the ``cam`` tool.\n\nIn case of problems, a detailed debug log can be obtained from libcamera by\nsetting the ``LIBCAMERA_LOG_LEVELS`` environment variable:\n\n.. code::\n\n    :~$ LIBCAMERA_LOG_LEVELS=*:DEBUG cam -l", "part_id": "steps"}]}, "topic_inputs": {"try": "d7d7d3736a0ed8f6bfbb63f700649fbb2ef1fc04bddb5f557bd8a6a91b56120a", "why": "2119187716441f258076ccc30f1d1ce0754983bc39b893268615955aa30067eb"}, "reused_topics": ["why"], "replayed_units": [], "generated_topics": ["try"], "topic_agents": {"why": "cli/codex/gpt-6.1-terra", "try": "cli/codex/gpt-6.1-terra"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "e0c429a5c80a01c34563ce00a616df89d8f75c735f8669bcbd1f75d84cce82a6", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "1f0355f74c3b70d713c7a9b7d42598279476819e3a7af472259871135a4d799d", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "fecc4ee78a481139776e562c164c0da9a3e5edf0a64a72be1d1c8feddee3cd08", "answer_contracts": "1e0d24e0cf26ded53ecec2e5a6fbc51836bac6e17530318a9fa7cffaa936c00b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "9db4d42a710b4a71a7d2bb16f69db06926409281dc1a200c796e77d5deaa25a0", "design_response": "74ebb2d21768d6bdd4ef7611c1c539526a7e72e6a58604c82e8305003d24f8b7", "design_validation": "b8133c78a8eb42fd5194c2756bb649b396ec54b40c49b72544bdbbcaf3366c57"}, "validation_model": "44197615786b818e4d9150110e74bef6772ea4f261a58d27ac12f379abaeb439", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "f8fd5a3d8041c23fc68b93ff32b8727e98393383b5099032eb00ad0013e7611c"}, "reuse_lineage": {"source_commit": "212c689fcf2450bbfbaab25c7472895ac277b5d6", "body_sha256": "b6531682ae06681333693d1cfec5518beb2cc2ea95bdb5aaaf35a91b6cef8e6f", "topics": ["why"], "validation": "current source, contract and editorial checks; human review pending"}, "body_sha256": "b479c7c570044efad8ef8eb3f078a7c8f2f66f787b1c52633a930fcfe0125861"}
revalidated_from: 212c689fcf2450bbfbaab25c7472895ac277b5d6
---

# 실행해 보고 설계 이유 읽기

**먼저 cam 도구로 카메라를 확인한 뒤, 요청 접수와 완료가 나뉜 이유를 소스 주석에서 읽으세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 시스템에서 감지된 카메라 목록은 `cam -l`로 확인할 수 있습니다. | [직접 실행해 보기](#직접-실행해-보기) |
| 애플리케이션은 queueRequest를 호출하기 전에 createRequest()로 할당한 요청에 캡처 버퍼를 하나 이상 채워야 합니다. | [요청 접수와 완료를 나눈 이유](#요청-접수와-완료를-나눈-이유) |

## 직접 실행해 보기

시스템에서 감지된 카메라 목록은 `cam -l`로 확인할 수 있습니다. 첫 번째 카메라에서 10프레임을 캡처하여 디스크에 저장하려면 `cam -c 1 --capture=10 --file`을 사용합니다. 문제가 발생하면 `LIBCAMERA_LOG_LEVELS=*:DEBUG cam -l`로 환경 변수를 설정하여 libcamera의 상세 디버그 로그를 얻을 수 있습니다. `README.rst:107`

근거 원문: [README.rst:107](#source-5bc9ee57c1b6daee)

## 요청 접수와 완료를 나눈 이유

애플리케이션은 queueRequest를 호출하기 전에 createRequest()로 할당한 요청에 캡처 버퍼를 하나 이상 채워야 합니다. 버퍼가 없는 요청은 유효하지 않아 큐에 추가되지 않고 거부됩니다. 요청이 큐에 추가되면 카메라는 requestCompleted 시그널로 완료를 알립니다. `src/libcamera/camera.cpp:1311`

마지막 버퍼가 완료될 때 요청은 자동으로 완료되지 않습니다. 이는 파이프라인 핸들러가 아직 필요할 수 있는 작업을 수행할 기회를 주기 위함입니다. 파이프라인 핸들러는 completeRequest()로 요청을 명시적으로 완료해야 합니다. `src/libcamera/pipeline_handler.cpp:551`

요청은 제출된 순서대로 애플리케이션에 반환됩니다. 파이프라인 핸들러는 완료된 요청에 대해 순서 제약 없이 completeRequest()를 호출할 수 있습니다. `src/libcamera/pipeline_handler.cpp:574`

근거 원문: [src/libcamera/camera.cpp:1311](#source-a697a2ba4de7965c) · [src/libcamera/pipeline_handler.cpp:551](#source-9bd7c9fb9847e336) · [src/libcamera/pipeline_handler.cpp:574](#source-77cb263c0a63392c)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 카메라를 직접 확인해 보려면 무엇을 실행합니까? | [직접 실행해 보기](#직접-실행해-보기) | 코드 근거와 설명 연결 |
    | 요청 접수와 완료 통지가 별도 단계인 이유 중 소스가 직접 밝힌 것은 무엇입니까? | [요청 접수와 완료를 나눈 이유](#요청-접수와-완료를-나눈-이유) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-5bc9ee57c1b6daee"></a>

??? note "소스 근거: README.rst:107"
    `README.rst:107`에서 시작하는 발췌입니다. 종료 줄은 117이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `c35f23844229f0b6dc8411bca6eea313eb05f11d9b9a4524f5375c921b09afc4`
    
    ```text
    The ``cam`` utility can be used for basic testing. You can list the cameras
    detected on the system with ``cam -l``, and capture ten frames from the first
    camera and save them to disk with ``cam -c 1 --capture=10 --file``. See
    ``cam -h`` for more information about the ``cam`` tool.
    
    In case of problems, a detailed debug log can be obtained from libcamera by
    setting the ``LIBCAMERA_LOG_LEVELS`` environment variable:
    
    .. code::
    
        :~$ LIBCAMERA_LOG_LEVELS=*:DEBUG cam -l
    ```

<a id="source-a697a2ba4de7965c"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1311"
    `src/libcamera/camera.cpp:1311`에서 시작하는 발췌입니다. 종료 줄은 1318이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e28ed33dec85a5e783457be419afac5b7c646b588c24bc311d46265b1ae7f37a`
    
    ```text
    This function queues a \a request to the camera for capture.
     *
     * After allocating the request with createRequest(), the application shall
     * fill it with at least one capture buffer before queuing it. Requests that
     * contain no buffers are invalid and are rejected without being queued.
     *
     * Once the request has been queued, the camera will notify its completion
     * through the \ref requestCompleted signal.
    ```

<a id="source-9bd7c9fb9847e336"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:551"
    `src/libcamera/pipeline_handler.cpp:551`에서 시작하는 발췌입니다. 종료 줄은 556이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `dc60b6f028df4f7341facfcbd3ebade17f81bb4d2e72ce580ba93c7a1c449b42`
    
    ```text
    This function shall be called by pipeline handlers to signal completion of
     * the \a buffer part of the \a request. It notifies applications of buffer
     * completion and updates the request's internal buffer tracking. The request
     * is not completed automatically when the last buffer completes to give
     * pipeline handlers a chance to perform any operation that may still be
     * needed. They shall complete requests explicitly with completeRequest().
    ```

<a id="source-77cb263c0a63392c"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:574"
    `src/libcamera/pipeline_handler.cpp:574`에서 시작하는 발췌입니다. 종료 줄은 580이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `5df554f7462852344c1f8f25dd3bf2f16f22ab34e3f96d948d54ec44baca7217`
    
    ```text
    The pipeline handler shall call this function to notify the \a camera that
     * the request has completed. The request is no longer managed by the pipeline
     * handler and shall not be accessed once this function returns.
     *
     * This function ensures that requests will be returned to the application in
     * submission order, the pipeline handler may call it on any complete request
     * without any ordering constraint.
    ```

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `README.rst`, `include/libcamera/camera.h`, `include/libcamera/internal/pipeline_handler.h`, `include/libcamera/request.h`, `src/libcamera/camera.cpp`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/request.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `212c689fcf`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-30 · 사람 검토 전

다음 단계: [카메라와 요청 모델](camera-model.md)
