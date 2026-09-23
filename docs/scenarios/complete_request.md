---
generated_at: 2026-09-23T16:52:51+00:00
source_commit: 279d355ef8f7a4f98bb0a3004c0f788387814506
agent: ollama/qwen3.5:4b
status: ok
section: scenarios
entry: PipelineHandler::completeRequest(Request *)
---

# 요청 완료 통지 (PipelineHandler::completeRequest)

**`PipelineHandler::completeRequest(Request *)` 에서 시작하는 호출 순서를 아래 번호대로 따라가세요.**



```mermaid
sequenceDiagram
    participant PipelineHandler
    participant Private
    participant Request
    participant request
    participant tracepoints
    participant Camera
    participant Signal
    participant PipelineHandlerIPU3
    participant IPU3CameraData
    participant PipelineHandlerRkISP1
    participant RkISP1Frames
    participant IPAProxyRkISP1Threaded
    participant IPAProxyRkISP1Isolated
    participant IPARkISP1
    participant RkISP1Path
    participant FrameBuffer
    participant PipelineHandlerUVC
    PipelineHandler->>Private: camera()
    PipelineHandler->>Private: complete()
    Private->>Private: _o()
    Private->>Request: status()
    Private->>Private: hasPendingBuffers()
    Private->>Request: toString()
    Request->>request: operator<<()
    request->>Request: sequence()
    request->>Request: status()
    request->>Request: buffers()
    request->>Request: cookie()
    Private->>tracepoints: unused()
    PipelineHandler->>Request: status()
    PipelineHandler->>Request: hasPendingBuffers()
    Request->>Private: hasPendingBuffers()
    PipelineHandler->>Camera: requestComplete()
    Camera->>Private: isAccessAllowed()
    Camera->>Signal: emit()
    PipelineHandler->>PipelineHandler: doQueueRequests()
    PipelineHandler->>PipelineHandler: doQueueRequest()
    PipelineHandler->>tracepoints: unused()
    PipelineHandler->>Private: camera()
    PipelineHandler->>PipelineHandler: completeRequest()
    PipelineHandler-->>PipelineHandlerIPU3: queueRequestDevice() [virtual 후보]
    PipelineHandlerIPU3->>PipelineHandlerIPU3: cameraData()
    PipelineHandlerIPU3->>IPU3CameraData: queuePendingRequests()
    PipelineHandler-->>PipelineHandlerRkISP1: queueRequestDevice() [virtual 후보]
    PipelineHandlerRkISP1->>PipelineHandlerRkISP1: cameraData()
    PipelineHandlerRkISP1->>RkISP1Frames: create()
    PipelineHandlerRkISP1-->>IPAProxyRkISP1Threaded: queueRequest() [virtual 후보]
    PipelineHandlerRkISP1-->>IPAProxyRkISP1Isolated: queueRequest() [virtual 후보]
    PipelineHandlerRkISP1-->>IPARkISP1: queueRequest() [virtual 후보]
    PipelineHandlerRkISP1->>Request: controls()
    PipelineHandlerRkISP1->>RkISP1Path: queueBuffer()
    PipelineHandlerRkISP1->>RkISP1Path: queueBuffer()
    PipelineHandlerRkISP1-->>IPAProxyRkISP1Threaded: computeParams() [virtual 후보]
    PipelineHandlerRkISP1-->>IPAProxyRkISP1Isolated: computeParams() [virtual 후보]
    PipelineHandlerRkISP1-->>IPARkISP1: computeParams() [virtual 후보]
    PipelineHandlerRkISP1->>FrameBuffer: cookie()
    PipelineHandler-->>PipelineHandlerUVC: queueRequestDevice() [virtual 후보]
```

그림에는 앞의 40 개 호출만 그렸습니다. 나머지 8 개는 아래 호출 순서와 `facts.json` 에서 확인하세요.

## 호출 순서

1. `PipelineHandler` 가 `Private::camera()` 를 호출합니다. `src/libcamera/pipeline_handler.cpp:586`
2. `PipelineHandler` 가 `Private::complete()` 를 호출합니다. `src/libcamera/pipeline_handler.cpp:588`
3. `Private` 가 `Private::_o()` 를 호출합니다. `src/libcamera/request.cpp:127`
4. `Private` 가 `Request::status()` 를 호출합니다. `src/libcamera/request.cpp:129`
5. `Private` 가 `Private::hasPendingBuffers()` 를 호출합니다. `src/libcamera/request.cpp:130`
6. `Private` 가 `Request::toString()` 를 호출합니다. `src/libcamera/request.cpp:134`
7. `Request` 가 `request::operator<<()` 를 호출합니다. `src/libcamera/request.cpp:592`
8. `request` 가 `Request::sequence()` 를 호출합니다. `src/libcamera/request.cpp:609`
9. `request` 가 `Request::status()` 를 호출합니다. `src/libcamera/request.cpp:609`
10. `request` 가 `Request::buffers()` 를 호출합니다. `src/libcamera/request.cpp:610`
11. `request` 가 `Request::cookie()` 를 호출합니다. `src/libcamera/request.cpp:611`
12. `Private` 가 `tracepoints::unused()` 를 호출합니다. `src/libcamera/request.cpp:136`
13. `PipelineHandler` 가 `Request::status()` 를 호출합니다. `src/libcamera/pipeline_handler.cpp:594`
14. `PipelineHandler` 가 `Request::hasPendingBuffers()` 를 호출합니다. `src/libcamera/pipeline_handler.cpp:597`
15. `Request` 가 `Private::hasPendingBuffers()` 를 호출합니다. `src/libcamera/request.cpp:578`
16. `PipelineHandler` 가 `Camera::requestComplete()` 를 호출합니다. `src/libcamera/pipeline_handler.cpp:599`
17. `Camera` 가 `Private::isAccessAllowed()` 를 호출합니다. `src/libcamera/camera.cpp:1484`
18. `Camera` 가 `Signal::emit()` 를 호출합니다. `src/libcamera/camera.cpp:1488`
19. `PipelineHandler` 가 `PipelineHandler::doQueueRequests()` 를 호출합니다. `src/libcamera/pipeline_handler.cpp:603`
20. `PipelineHandler` 가 `PipelineHandler::doQueueRequest()` 를 호출합니다. `src/libcamera/pipeline_handler.cpp:525`
21. `PipelineHandler` 가 `tracepoints::unused()` 를 호출합니다. `src/libcamera/pipeline_handler.cpp:485`
22. `PipelineHandler` 가 `Private::camera()` 를 호출합니다. `src/libcamera/pipeline_handler.cpp:487`
23. `PipelineHandler` 가 `PipelineHandler::completeRequest()` 를 호출합니다. `src/libcamera/pipeline_handler.cpp:494`
24. `PipelineHandler` 가 `PipelineHandlerIPU3::queueRequestDevice()` 를 호출합니다. (virtual 후보) `src/libcamera/pipeline_handler.cpp:498`
25. `PipelineHandlerIPU3` 가 `PipelineHandlerIPU3::cameraData()` 를 호출합니다. `src/libcamera/pipeline/ipu3/ipu3.cpp:840`
26. `PipelineHandlerIPU3` 가 `IPU3CameraData::queuePendingRequests()` 를 호출합니다. `src/libcamera/pipeline/ipu3/ipu3.cpp:843`
27. `PipelineHandler` 가 `PipelineHandlerRkISP1::queueRequestDevice()` 를 호출합니다. (virtual 후보) `src/libcamera/pipeline_handler.cpp:498`
28. `PipelineHandlerRkISP1` 가 `PipelineHandlerRkISP1::cameraData()` 를 호출합니다. `src/libcamera/pipeline/rkisp1/rkisp1.cpp:1342`
29. `PipelineHandlerRkISP1` 가 `RkISP1Frames::create()` 를 호출합니다. `src/libcamera/pipeline/rkisp1/rkisp1.cpp:1344`
30. `PipelineHandlerRkISP1` 가 `IPAProxyRkISP1Threaded::queueRequest()` 를 호출합니다. (virtual 후보) `src/libcamera/pipeline/rkisp1/rkisp1.cpp:1348`

(이후 단계는 생략했습니다. 전체 흐름은 `facts.json` 의 `scenarios` 에 있습니다.)

표시에서 뺀 호출이 57 개 있습니다. `config/scenarios.yaml` 의 `hide` 규칙에 걸린 로깅과 접근자 호출이며, `facts.json` 에는 그대로 남아 있습니다.

## 이 흐름에서 확인할 것

`PipelineHandler::completeRequest()` 호출은 `src/libcamera/pipeline_handler.cpp:586` 에서 시작하여 `Camera::requestComplete()` 를 거쳐 다시 `PipelineHandlerIPU3::queueRequestDevice()` 와 같은 가상 함수를 통해 하위 구현체로 분기합니다. 각 단계의 메서드 정의 위치는 해당 파일과 줄 번호로 확인해야 하며, 호출 경로의 일부는 `src/libcamera/request.cpp:127` 에서 `Request::status()` 를 통해 로그 생성으로 전환된 후 다시 `PipelineHandler` 로 돌아오는 구조를 가집니다.

설계 의도나 스레드 동기화 근거가 명시되지 않았으므로, 콜백 전달 순서와 정적 추적이 끊기는 지점은 "확인 필요: 확인할 항목"으로 남겨두어야 합니다. 특히 `src/libcamera/pipeline_handler.cpp:498` 에서 호출되는 가상 함수의 실제 실행 흐름과 `facts.json` 에 남아있는 57 개의 숨겨진 호출이 전체 순서에 미치는 영향은 추가 사실 확인이 필요합니다.

??? note "근거와 검토 정보"
    - 근거 파일: `src/libcamera/camera.cpp`, `src/libcamera/pipeline/ipu3/ipu3.cpp`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/request.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `279d355ef8`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토: 2026-09-24 · ollama/qwen3.5:4b · 사람 검토 전

다음 단계: [핵심 시나리오 목록](index.md)
