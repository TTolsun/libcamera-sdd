---
generated_at: 2026-10-28T23:09:50+00:00
source_commit: e117198c015057761bb0bbaa85f963c41ce412d7
status: ok
section: onboarding
generation_method: facts-and-llm
evidence_fingerprint: 40f9e0d8e3aab75e7b3b395701d6c471c3d570bf2bc3deb5495062fc00c7b81d
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "40f9e0d8e3aab75e7b3b395701d6c471c3d570bf2bc3deb5495062fc00c7b81d", "answers": {"try": [{"text": "cam은 기본적인 테스트에 사용할 수 있는 도구입니다.", "evidence": ["cam"], "covers": ["try"], "kind": "behavior", "quote": "The ``cam`` utility can be used for basic testing. You can list the cameras\ndetected on the system with ``cam -l``, and capture ten frames from the first\ncamera and save them to disk with ``cam -c 1 --capture=10 --file``. See\n``cam -h`` for more information about the ``cam`` tool.\n\nIn case of problems, a detailed debug log can be obtained from libcamera by\nsetting the ``LIBCAMERA_LOG_LEVELS`` environment variable:\n\n.. code::\n\n    :~$ LIBCAMERA_LOG_LEVELS=*:DEBUG cam -l", "part_id": "tool"}, {"text": "카메라 목록을 확인하려면 `cam -l`을 실행합니다. 첫 번째 카메라에서 10개 프레임을 캡처해 디스크에 저장하려면 `cam -c 1 --capture=10 --file`을 실행합니다. 문제가 있을 때 상세 디버그 로그를 얻으려면 `LIBCAMERA_LOG_LEVELS=*:DEBUG cam -l`을 실행합니다.", "evidence": ["cam"], "covers": ["try"], "kind": "limitation", "quote": "The ``cam`` utility can be used for basic testing. You can list the cameras\ndetected on the system with ``cam -l``, and capture ten frames from the first\ncamera and save them to disk with ``cam -c 1 --capture=10 --file``. See\n``cam -h`` for more information about the ``cam`` tool.\n\nIn case of problems, a detailed debug log can be obtained from libcamera by\nsetting the ``LIBCAMERA_LOG_LEVELS`` environment variable:\n\n.. code::\n\n    :~$ LIBCAMERA_LOG_LEVELS=*:DEBUG cam -l", "part_id": "steps"}], "why": [{"text": "애플리케이션은 queueRequest를 호출하기 전에 요청에 캡처 버퍼를 하나 이상 채워야 합니다. 버퍼가 없는 요청은 유효하지 않아 큐에 추가되지 않고 거부됩니다. 요청이 큐에 추가되면 카메라는 requestCompleted 시그널을 통해 완료를 알립니다.", "evidence": ["accept"], "covers": ["why"], "kind": "behavior", "quote": "This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.", "part_id": "accept"}, {"text": "파이프라인 핸들러가 completeBuffer를 호출하여 요청의 마지막 버퍼 완료를 알릴 때, 요청은 자동으로 완료되지 않습니다. 이는 파이프라인 핸들러가 여전히 필요할 수 있는 작업을 수행할 기회를 주기 위함이며, 핸들러는 completeRequest()로 요청을 명시적으로 완료해야 합니다.", "evidence": ["buffer"], "covers": ["why"], "kind": "behavior", "quote": "This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().", "part_id": "buffer"}, {"text": "요청은 제출된 순서대로 애플리케이션에 반환됩니다. 파이프라인 핸들러는 순서 제약 없이 완료된 요청에 대해 completeRequest()를 호출할 수 있습니다.", "evidence": ["order"], "covers": ["why"], "kind": "behavior", "quote": "The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.", "part_id": "order"}]}, "topic_inputs": {"try": "8802b80ead6004c1527f90cf4f115ec5e06905428f26ca4b93a5d5eb7cd96568", "why": "fd9fc1bced7bb26bbaafd1296321643b5c319e93f90aee5f0a22d695dd47b2aa"}, "reused_topics": ["try", "why"], "replayed_units": [], "generated_topics": [], "topic_agents": {"try": "cli/codex/gpt-6.1-terra", "why": "cli/codex/gpt-6.1-terra"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "e0c429a5c80a01c34563ce00a616df89d8f75c735f8669bcbd1f75d84cce82a6", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "d4af3d834d8b1c99a6c9311612712a64112c30fa4621b375904d172f361285b8", "design_contracts": "b293a0012d1fcb6340fcaf94d481cf900212686978bc96fb118a0cdaddf3c091", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "65c405dc11cd8c43e2bce26ffbd96a47f37a784df59a4969be589ed8318f7be0", "answer_contracts": "1e0d24e0cf26ded53ecec2e5a6fbc51836bac6e17530318a9fa7cffaa936c00b", "design_response": "ce93f02b72371ed40f1b1124e78cef512baea31aa2df988db0c689f8169f783c", "design_validation": "608d2eed51e4ad5d5693fbc9b7d669ae1ba8e503f6736b62ea1ca068ce706556"}, "validation_model": "5ddbcbf91a6b516c4f71596d64b6286295bfd0cac771a7ca749ca78e25a2d752", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "f8fd5a3d8041c23fc68b93ff32b8727e98393383b5099032eb00ad0013e7611c"}, "reuse_lineage": {"source_commit": "e117198c015057761bb0bbaa85f963c41ce412d7", "body_sha256": "a113fe7aaae9df4a9bbfa7b336ab9e77dea9eab306eb8643cd2eed8d7ef7341c", "topics": ["try", "why"], "validation": "current source, contract and editorial checks; human review pending"}, "body_sha256": "a113fe7aaae9df4a9bbfa7b336ab9e77dea9eab306eb8643cd2eed8d7ef7341c"}
---

# 실행해 보고 설계 이유 읽기

**먼저 cam 도구로 카메라를 확인한 뒤, 요청 접수와 완료가 나뉜 이유를 소스 주석에서 읽으세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 직접 실행해 보기 절을 확인합니다. | [직접 실행해 보기](#직접-실행해-보기) |
| 요청 접수와 완료를 나눈 이유 절을 확인합니다. | [요청 접수와 완료를 나눈 이유](#요청-접수와-완료를-나눈-이유) |

## 직접 실행해 보기

cam은 기본적인 테스트에 사용할 수 있는 도구입니다. `README.rst:107`

실행 확인 항목: 카메라 목록을 확인하려면 `cam -l`을 실행합니다. 첫 번째 카메라에서 10개 프레임을 캡처해 디스크에 저장하려면 `cam -c 1 --capture=10 --file`을 실행합니다. 문제가 있을 때 상세 디버그 로그를 얻으려면 `LIBCAMERA_LOG_LEVELS=*:DEBUG cam -l`을 실행합니다. `README.rst:107`

근거 원문: [README.rst:107](#source-5bc9ee57c1b6daee)

## 요청 접수와 완료를 나눈 이유

애플리케이션은 queueRequest를 호출하기 전에 요청에 캡처 버퍼를 하나 이상 채워야 합니다. 버퍼가 없는 요청은 유효하지 않아 큐에 추가되지 않고 거부됩니다. 요청이 큐에 추가되면 카메라는 requestCompleted 시그널을 통해 완료를 알립니다. `src/libcamera/camera.cpp:1311`

파이프라인 핸들러가 completeBuffer를 호출하여 요청의 마지막 버퍼 완료를 알릴 때, 요청은 자동으로 완료되지 않습니다. 이는 파이프라인 핸들러가 여전히 필요할 수 있는 작업을 수행할 기회를 주기 위함이며, 핸들러는 completeRequest()로 요청을 명시적으로 완료해야 합니다. 요청은 제출된 순서대로 애플리케이션에 반환됩니다. 파이프라인 핸들러는 순서 제약 없이 완료된 요청에 대해 completeRequest()를 호출할 수 있습니다. `src/libcamera/pipeline_handler.cpp:551`, `src/libcamera/pipeline_handler.cpp:574`

근거 원문: [src/libcamera/camera.cpp:1311](#source-a697a2ba4de7965c) · [src/libcamera/pipeline_handler.cpp:551](#source-9bd7c9fb9847e336) · [src/libcamera/pipeline_handler.cpp:574](#source-77cb263c0a63392c)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 카메라를 직접 확인해 보려면 무엇을 실행합니까? | [직접 실행해 보기](#직접-실행해-보기) | 코드 근거와 설명 연결 · 실행 확인 항목 별도 |
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
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `e117198c01`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-29 · 사람 검토 전

다음 단계: [카메라와 요청 모델](camera-model.md)
