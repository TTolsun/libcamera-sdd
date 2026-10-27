---
generated_at: 2026-10-27T01:23:22+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: onboarding
generation_method: facts-and-llm
evidence_fingerprint: d2b44ee8ee6419354654dfbfdca9d03a3db3a8f2b7a6241475d23ba5372012af
semantic_review: human-review-required
agent: cli/hermes/qwen3.5:9b-ctx64k
generated_design: {"schema": 1, "input_fingerprint": "d2b44ee8ee6419354654dfbfdca9d03a3db3a8f2b7a6241475d23ba5372012af", "answers": {"try": [{"text": "cam 도구는 기본 테스트를 위한 유틸리티로, 시스템에서 감지된 카메라를 ``cam -l`` 으로 나열하거나 첫 번째 카메라로부터 프레임 10 개를 포착하여 디스크에 저장하는 ``cam -c 1 --capture=10 --file`` 등의 동작을 확인할 수 있습니다.", "evidence": ["cam"], "covers": ["try"], "kind": "behavior", "quote": "The ``cam`` utility can be used for basic testing. You can list the cameras\ndetected on the system with ``cam -l``, and capture ten frames from the first\ncamera and save them to disk with ``cam -c 1 --capture=10 --file``. See\n``cam -h`` for more information about the ``cam`` tool.\n\nIn case of problems, a detailed debug log can be obtained from libcamera by\nsetting the ``LIBCAMERA_LOG_LEVELS`` environment variable:\n\n.. code::\n\n    :~$ LIBCAMERA_LOG_LEVELS=*:DEBUG cam -l", "part_id": "tool"}, {"text": "The ``cam`` 유틸리티로 시스템을 감지한 카메라를 나열하려면 ``cam -l``를 실행하고, 첫 번째 카메라에서 10 프레임 을 캡처하여 저장하려면 ``cam -c 1 --capture=10 --file``을 사용하며, 문제 발생 시 디버그 로그를 위해 `LIBCAMERA_LOG_LEVELS`=*:DEBUG 환경 변수를 설정한 후 ``cam -l`를 실행하는 방법을 확인할 수 있다.", "evidence": ["cam"], "covers": ["try"], "kind": "limitation", "quote": "The ``cam`` utility can be used for basic testing. You can list the cameras\ndetected on the system with ``cam -l``, and capture ten frames from the first\ncamera and save them to disk with ``cam -c 1 --capture=10 --file``. See\n``cam -h`` for more information about the ``cam`` tool.\n\nIn case of problems, a detailed debug log can be obtained from libcamera by\nsetting the ``LIBCAMERA_LOG_LEVELS`` environment variable:\n\n.. code::\n\n    :~$ LIBCAMERA_LOG_LEVELS=*:DEBUG cam -l", "part_id": "steps"}], "why": [{"text": "queueRequest()를 부르기 전에 요청에는 createRequest()로 할당하고 최소 하나의 캡처 버퍼로 채워져 있어야 하며, 큐에 넣은 뒤 완료는 requestCompleted 신호를 통해 알림을 주게 됩니다.", "evidence": ["accept"], "covers": ["why"], "kind": "behavior", "quote": "This function queues a \\a request to the camera for capture.\n *\n * After allocating the request with createRequest(), the application shall\n * fill it with at least one capture buffer before queuing it. Requests that\n * contain no buffers are invalid and are rejected without being queued.\n *\n * Once the request has been queued, the camera will notify its completion\n * through the \\ref requestCompleted signal.", "part_id": "accept"}, {"text": "요청이 자동으로 완료되지 않는 이유는 마지막 버퍼가 종료되더라도 파이프라인 핸들러가 추가로 수행해야 할 작업이 있을 수 있기 위함입니다. 대신에 파이프라인 핸들러는 명시적으로 completeRequest() 메서드를 호출하여 요청을 완료해야 합니다.", "evidence": ["buffer"], "covers": ["why"], "kind": "behavior", "quote": "This function shall be called by pipeline handlers to signal completion of\n * the \\a buffer part of the \\a request. It notifies applications of buffer\n * completion and updates the request's internal buffer tracking. The request\n * is not completed automatically when the last buffer completes to give\n * pipeline handlers a chance to perform any operation that may still be\n * needed. They shall complete requests explicitly with completeRequest().", "part_id": "buffer"}, {"text": "요청은 제출 순서대로 애플리케이션으로 반환되며, 파이프라인 핸들러는 completeRequest()를 완료된 요청에 대해 순서 제약 없이 호출할 수 있습니다.", "evidence": ["order"], "covers": ["why"], "kind": "behavior", "quote": "The pipeline handler shall call this function to notify the \\a camera that\n * the request has completed. The request is no longer managed by the pipeline\n * handler and shall not be accessed once this function returns.\n *\n * This function ensures that requests will be returned to the application in\n * submission order, the pipeline handler may call it on any complete request\n * without any ordering constraint.", "part_id": "order"}]}, "topic_inputs": {"try": "6b37009f7c4e52e055bd56a32e37d1ef078f62b419cbd099439eebd244a6cdd9", "why": "645dfc61631c461e247240dad7e82eb506cab5ac9c15e4eb9b6318256bcdff5d"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["try", "why"], "topic_agents": {"try": "cli/hermes/qwen3.5:9b-ctx64k", "why": "cli/hermes/qwen3.5:9b-ctx64k"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "body_sha256": "f1079d5347246f1cabfaf8ab5a16c9d5b78acfe3015f3d57318a71a1fc4a15a8"}
---

# 실행해 보고 설계 이유 읽기

**먼저 cam 도구로 카메라를 확인한 뒤, 요청 접수와 완료가 나뉜 이유를 소스 주석에서 읽으세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 직접 실행해 보기 절을 확인합니다. | [직접 실행해 보기](#직접-실행해-보기) |
| 요청 접수와 완료를 나눈 이유 절을 확인합니다. | [요청 접수와 완료를 나눈 이유](#요청-접수와-완료를-나눈-이유) |

## 직접 실행해 보기

cam 도구는 기본 테스트를 위한 유틸리티로, 시스템에서 감지된 카메라를 ``cam -l`` 으로 나열하거나 첫 번째 카메라로부터 프레임 10 개를 포착하여 디스크에 저장하는 ``cam -c 1 --capture=10 --file`` 등의 동작을 확인할 수 있습니다. `README.rst:107`

실행 확인 항목: The ``cam`` 유틸리티로 시스템을 감지한 카메라를 나열하려면 ``cam -l``를 실행하고, 첫 번째 카메라에서 10 프레임 을 캡처하여 저장하려면 ``cam -c 1 --capture=10 --file``을 사용하며, 문제 발생 시 디버그 로그를 위해 `LIBCAMERA_LOG_LEVELS`=*:DEBUG 환경 변수를 설정한 후 ``cam -l`를 실행하는 방법을 확인할 수 있다. `README.rst:107`

근거 원문: [README.rst:107](#source-5bc9ee57c1b6daee)

## 요청 접수와 완료를 나눈 이유

queueRequest()를 부르기 전에 요청에는 createRequest()로 할당하고 최소 하나의 캡처 버퍼로 채워져 있어야 하며, 큐에 넣은 뒤 완료는 requestCompleted 신호를 통해 알림을 주게 됩니다. 요청이 자동으로 완료되지 않는 이유는 마지막 버퍼가 종료되더라도 파이프라인 핸들러가 추가로 수행해야 할 작업이 있을 수 있기 위함입니다. 대신에 파이프라인 핸들러는 명시적으로 completeRequest() 메서드를 호출하여 요청을 완료해야 합니다. 요청은 제출 순서대로 애플리케이션으로 반환되며, 파이프라인 핸들러는 completeRequest()를 완료된 요청에 대해 순서 제약 없이 호출할 수 있습니다. `src/libcamera/camera.cpp:1311`, `src/libcamera/pipeline_handler.cpp:551`, `src/libcamera/pipeline_handler.cpp:574`

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
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `2c4b67c079`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-27 · 사람 검토 전

다음 단계: [카메라와 요청 모델](camera-model.md)
