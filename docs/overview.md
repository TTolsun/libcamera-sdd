---
generated_at: 2026-10-24T06:27:51+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: overview
generation_method: facts-and-llm
evidence_fingerprint: 83b9bd9118b418b4b8051aad7ba876e81bc46b0d23c709c1ca8fa14c87bb85d0
semantic_review: human-review-required
agent: ollama/qwen3.5:9b
generated_design: {"schema": 1, "input_fingerprint": "83b9bd9118b418b4b8051aad7ba876e81bc46b0d23c709c1ca8fa14c87bb85d0", "answers": {"responsibility": [{"quote": "The Camera class models a camera capable of producing one or more image streams from a single image source. It provides the main interface to configuring and controlling the device, and capturing image streams. It is the central object exposed by libcamera.", "text": "`Camera` 클래스는 이미지 소스에서 하나 이상의 스트림을 생성하는 카메라를 모델링하며, 장치 구성과 제어의 주요 인터페이스 역할을 합니다.", "evidence": ["camera"], "covers": ["responsibility"], "kind": "behavior"}, {"quote": "To support the central nature of Camera objects, libcamera manages the lifetime of camera instances with std::shared_ptr<>. Instances shall be created with the create() function which returns a shared pointer. The Camera constructors and destructor are private, to prevent instances from being constructed and destroyed manually.", "text": "객체 수명은 std::shared_ptr 를 통해 관리되며, 생성은 create() 함수를 통해 이루어져야 합니다. 직접적인 생성과 소멸을 막기 위해 생성자와 파괴자는 비공개로 설정되어 있습니다.", "evidence": ["camera"], "covers": ["responsibility"], "kind": "behavior"}], "discovery": [{"quote": "The camera manager is the entry point to libcamera. It enumerates devices, associates them with pipeline managers, and provides access to the cameras in the system to applications. The manager owns all Camera objects and handles hot-plugging and hot-unplugging to manage the lifetime of cameras.", "text": "libcamera 시스템에서 장치 탐색과 카메라 등록은 `CameraManager` 가 담당합니다. 이 클래스는 모든 장치를 나열하고 파이프라인 관리자와 연결하며, 애플리케이션이 카메라에 접근할 수 있도록 합니다. 또한 카메라 객체의 소유권을 가지며 핫플러그와 핫언플러그를 처리하여 카메라의 수명을 관리합니다.", "evidence": ["manager"], "covers": ["discovery"], "kind": "behavior"}, {"quote": "This function is the main entry point of the pipeline handler. It is called by the camera manager with the \\a enumerator passed as an argument. It shall acquire from the \\a enumerator all the media devices it needs for a single pipeline, create one or multiple Camera instances and register them with the camera manager.", "text": "`PipelineHandler::match()` 함수는 파이프라인 관리자의 주요 진입점입니다. 카메라 관리자가 이 함수를 호출할 때 장치 나열기를 전달하며, 필요한 미디어 장치를 모두 확보하고 하나 이상의 카메라 인스턴스를 생성합니다. 이후 생성된 카메라 인스턴스를 카메라 관리자에게 등록하는 작업도 이 함수에서 수행됩니다.", "evidence": ["match"], "covers": ["discovery"], "kind": "behavior"}, {"quote": "If all media devices needed by the pipeline handler are found, they must all be acquired by a call to MediaDevice::acquire(). This function shall then create the corresponding Camera instances, store them internally, and return true. Otherwise it shall not acquire any media device (or shall release all the media devices is has acquired by calling MediaDevice::release()) and return false.", "text": "필요한 모든 미디어 장치를 찾았을 경우에만 `MediaDevice::acquire()` 를 호출하여 장치를 확보해야 합니다. 장치 확보가 성공하면 해당 카메라 인스턴스를 내부적으로 저장하고 true 를 반환합니다. 만약 필요한 장치를 모두 찾지 못하면 어떤 장치도 확보하지 않거나 이미 확보한 장치를 모두 해제한 뒤 false 를 반환합니다.", "evidence": ["match"], "covers": ["discovery"], "kind": "behavior"}, {"quote": "If multiple instances of a pipeline are available in the system, the PipelineHandler class will be instantiated once per instance, and its match() function called for every instance. Each call shall acquire media devices for one pipeline instance, until all compatible media devices are exhausted.", "text": "시스템에 여러 개의 파이프라인 인스턴스가 존재하면 각 인스턴스마다 `PipelineHandler` 클래스가 한 번씩 생성되고 match() 함수가 호출됩니다. 매번 호출 시에는 하나의 파이프라인 인스턴스를 위해 미디어 장치를 확보하며, 호환 가능한 모든 장치가 소진될 때까지 이 과정을 반복합니다.", "evidence": ["match"], "covers": ["discovery"], "kind": "behavior"}], "creation": [{"quote": "This function creates an empty request for the application to fill with buffers and parameters, and queue for capture.", "text": "`Camera::createRequest()` 함수는 애플리케이션이 버퍼와 파라미터를 채우고 캡처 큐에 넣을 수 있도록 빈 요청 객체를 생성합니다. 이 함수는 카메라가 Configured 또는 Running 상태일 때만 호출할 수 있으며, 실패 시 nullptr 를 반환합니다.", "evidence": ["create"], "covers": ["creation"], "kind": "behavior"}, {"quote": "The ownership of the returned request is passed to the caller, which is responsible for deleting it. The request may be deleted in the completion handler, or reused after resetting its state with Request::reuse().", "text": "생성된 요청의 소유권은 호출자에게 넘어가며, 호출자가 삭제할 책임이 있습니다. 요청은 완료 핸들러에서 삭제하거나 `Request::reuse()` 를 통해 상태를 초기화한 후 재사용할 수 있습니다.", "evidence": ["create"], "covers": ["creation"], "kind": "behavior"}, {"quote": "The \\a cookie is stored in the request and is accessible through the Request::cookie() function at any time. It is typically used by applications to map the request to an external resource in the request completion handler, and is completely opaque to libcamera.", "text": "요청에 저장된 쿠키는 언제든지 `Request::cookie()` 함수를 통해 접근할 수 있으며, 애플리케이션이 요청 완료 핸들러에서 외부 리소스와 매핑하는 데 주로 사용됩니다. 이 쿠키는 libcamera 에게는 불투명하게 처리됩니다.", "evidence": ["create"], "covers": ["creation"], "kind": "behavior"}, {"quote": "\\context This function is \\threadsafe. It may only be called when the camera is in the Configured or Running state as defined in \\ref camera_operation.", "text": "이 함수는 스레드 안전하며, 카메라가 정의된 Configured 또는 Running 상태일 때만 호출할 수 있습니다. 다른 상태에서는 호출을 시도하면 오류가 발생할 수 있습니다.", "evidence": ["create"], "covers": ["creation"], "kind": "behavior"}], "lifecycle": [{"quote": "An application needs to perform a sequence of operations on a camera before it is ready to process requests. The camera needs to be acquired and configured to prepare the camera for capture. Once started the camera can process requests until it is stopped. When an application is done with a camera, the camera needs to be released.", "text": "캡처를 시작하려면 먼저 카메라를 획득하고 설정해야 합니다. 이 단계에서 카메라가 요청을 처리할 준비가 됩니다.", "evidence": ["state"], "covers": ["lifecycle"], "kind": "behavior"}, {"quote": "An application may start and stop a camera multiple times as long as it is not released. The camera may also be reconfigured.", "text": "카메라를 해제하지 않은 상태라면 여러 번 시작하고 정지할 수 있으며, 설정을 다시 변경해도 됩니다.", "evidence": ["state"], "covers": ["lifecycle"], "kind": "behavior"}, {"quote": "process requests until it is stopped. When an application is done with a", "text": "카메라는 정지될 때까지 요청을 처리합니다. 애플리케이션이 카메라를 더 이상 필요로 하지 않으면 해제해야 합니다.", "evidence": ["state"], "covers": ["lifecycle"], "kind": "behavior"}], "request": [{"quote": "After allocating the request with createRequest(), the application shall fill it with at least one capture buffer before queuing it. Requests that contain no buffers are invalid and are rejected without being queued.", "text": "요청을 제출하기 전에 반드시 하나 이상의 캡처 버퍼를 채워야 합니다. 버퍼가 없는 요청은 무효로 간주되어 큐에 추가되지 않습니다.", "evidence": ["queue"], "covers": ["request"], "kind": "behavior"}, {"quote": "Once the request has been queued, the camera will notify its completion through the \\ref requestCompleted signal.", "text": "요청이 큐에 성공적으로 등록되면 카메라는 requestCompleted 신호를 통해 완료 상태를 알립니다.", "evidence": ["queue"], "covers": ["request"], "kind": "behavior"}, {"quote": "\\context This function is \\threadsafe. It may only be called when the camera is in the Running state as defined in \\ref camera_operation.", "text": "이 함수는 카메라가 Running 상태일 때만 호출할 수 있으며, 스레드 안전성을 보장합니다.", "evidence": ["queue"], "covers": ["request"], "kind": "behavior"}, {"quote": "\\retval -EACCES The camera is not running so requests can't be queued", "text": "카메라가 실행 중이 아니면 요청을 큐에 추가할 수 없으므로 -EACCES 오류 코드를 반환합니다.", "evidence": ["queue"], "covers": ["request"], "kind": "limitation"}], "completion": [{"quote": "This function shall be called by pipeline handlers to signal completion of the \\a buffer part of the \\a request. It notifies applications of buffer completion and updates the request's internal buffer tracking. The request is not completed automatically when the last buffer completes to give pipeline handlers a chance to perform any operation that may still be needed. They shall complete requests explicitly with completeRequest().", "text": "버퍼가 끝났다고 알리는 역할만 합니다. 이 함수는 애플리케이션에 버퍼 완료를 알려주고 요청 내부의 추적 정보를 갱신합니다.", "evidence": ["buffer"], "covers": ["completion"], "kind": "behavior"}, {"quote": "is not completed automatically when the last buffer completes to give", "text": "마지막 버퍼가 끝났다고 해서 자동으로 요청이 완료되는 것은 아닙니다. 이렇게 설계된 이유는 파이프라인 핸들러가 아직 해야 할 일이 있을 수 있기 때문입니다.", "evidence": ["buffer"], "covers": ["completion"], "kind": "behavior"}, {"quote": "needed. They shall complete requests explicitly with completeRequest().", "text": "핸들러가 필요한 작업을 모두 마친 뒤에는 반드시 completeRequest() 함수를 호출해서 요청을 명시적으로 완료해야 합니다.", "evidence": ["buffer"], "covers": ["completion"], "kind": "behavior"}], "boundary": [{"quote": "Functions that affect the camera state as defined below are generally not synchronized with each other by the Camera class. The caller is responsible for ensuring their synchronization if necessary.", "text": "카메라 상태를 변경하는 함수들은 서로 동기화되지 않습니다. 호출자가 필요한 경우 자체적으로 동기화를 보장해야 합니다.", "evidence": ["synchronization"], "covers": ["boundary"], "kind": "behavior"}, {"quote": "\\context This function shall be called from the CameraManager thread.", "text": "`PipelineHandler::completeRequest()` 는 반드시 `CameraManager` 스레드에서 호출되어야 합니다.", "evidence": ["completion"], "covers": ["boundary"], "kind": "behavior"}], "verification": [{"quote": "\\context This function may only be called when the camera is in the Configured state as defined in \\ref camera_operation, and shall be synchronized by the caller with other functions that affect the camera state.", "text": "`Camera::start()` 함수는 카메라가 설정된 상태인 경우에만 호출할 수 있습니다. 호출자는 이 함수를 다른 상태 변경 함수와 동기화해야 합니다.", "evidence": ["start"], "covers": ["verification"], "kind": "behavior"}, {"quote": "\\return 0 on success or a negative error code otherwise", "text": "성공 시 0 을 반환하며, 실패 시 음수 오류 코드를 반환합니다.", "evidence": ["start"], "covers": ["verification"], "kind": "behavior"}, {"quote": "\\todo Add documentation for camera start timings. What exactly does the camera expect the pipeline handler to do when start() is called?", "text": "카메라가 시작 타이밍에 파이프라인 핸들러에게 기대하는 정확한 동작은 아직 문서화되지 않았습니다.", "evidence": ["timing"], "covers": ["verification"], "kind": "limitation"}]}, "body_sha256": "5e53ab2bb36571463a947ad3357da6a0855963c3d9f23c8b4bf1f0eac460a4a9"}
---

# 시스템 개요

**카메라 탐색, 요청 생성과 완료의 책임을 구분한 뒤 수정할 패키지를 찾으세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 수정할 책임 경계를 찾습니다. | [컴포넌트별 책임](#컴포넌트별-책임) |
| 요청과 결과가 지나는 경계를 확인합니다. | [요청 제출과 완료](#요청-제출과-완료) |
| 전체 클래스와 패키지를 찾습니다. | [구성 요소 색인](component-index.md) |

## 컴포넌트별 책임

`Camera` 클래스는 이미지 소스에서 하나 이상의 스트림을 생성하는 카메라를 모델링하며, 장치 구성과 제어의 주요 인터페이스 역할을 합니다. `src/libcamera/camera.cpp:758`

객체 수명은 std::shared_ptr 를 통해 관리되며, 생성은 create() 함수를 통해 이루어져야 합니다. 직접적인 생성과 소멸을 막기 위해 생성자와 파괴자는 비공개로 설정되어 있습니다. `src/libcamera/camera.cpp:758`

근거 원문: [src/libcamera/camera.cpp:758](#source-6c066281dcce33d6)

## 탐색과 파이프라인 선택

libcamera 시스템에서 장치 탐색과 카메라 등록은 `CameraManager` 가 담당합니다. 이 클래스는 모든 장치를 나열하고 파이프라인 관리자와 연결하며, 애플리케이션이 카메라에 접근할 수 있도록 합니다. 또한 카메라 객체의 소유권을 가지며 핫플러그와 핫언플러그를 처리하여 카메라의 수명을 관리합니다. `src/libcamera/camera_manager.cpp:283`

`PipelineHandler::match()` 함수는 파이프라인 관리자의 주요 진입점입니다. 카메라 관리자가 이 함수를 호출할 때 장치 나열기를 전달하며, 필요한 미디어 장치를 모두 확보하고 하나 이상의 카메라 인스턴스를 생성합니다. 이후 생성된 카메라 인스턴스를 카메라 관리자에게 등록하는 작업도 이 함수에서 수행됩니다. `src/libcamera/pipeline_handler.cpp:86`

필요한 모든 미디어 장치를 찾았을 경우에만 `MediaDevice::acquire()` 를 호출하여 장치를 확보해야 합니다. 장치 확보가 성공하면 해당 카메라 인스턴스를 내부적으로 저장하고 true 를 반환합니다. 만약 필요한 장치를 모두 찾지 못하면 어떤 장치도 확보하지 않거나 이미 확보한 장치를 모두 해제한 뒤 false 를 반환합니다. `src/libcamera/pipeline_handler.cpp:86`

시스템에 여러 개의 파이프라인 인스턴스가 존재하면 각 인스턴스마다 `PipelineHandler` 클래스가 한 번씩 생성되고 match() 함수가 호출됩니다. 매번 호출 시에는 하나의 파이프라인 인스턴스를 위해 미디어 장치를 확보하며, 호환 가능한 모든 장치가 소진될 때까지 이 과정을 반복합니다. `src/libcamera/pipeline_handler.cpp:86`

근거 원문: [src/libcamera/camera_manager.cpp:283](#source-916045c55b34387b) · [src/libcamera/pipeline_handler.cpp:86](#source-5bbd41c1e725138c)

## 요청 생성과 소유권

`Camera::createRequest()` 함수는 애플리케이션이 버퍼와 파라미터를 채우고 캡처 큐에 넣을 수 있도록 빈 요청 객체를 생성합니다. 이 함수는 카메라가 Configured 또는 Running 상태일 때만 호출할 수 있으며, 실패 시 nullptr 를 반환합니다. `src/libcamera/camera.cpp:1243`

생성된 요청의 소유권은 호출자에게 넘어가며, 호출자가 삭제할 책임이 있습니다. 요청은 완료 핸들러에서 삭제하거나 `Request::reuse()` 를 통해 상태를 초기화한 후 재사용할 수 있습니다. `src/libcamera/camera.cpp:1243`

요청에 저장된 쿠키는 언제든지 `Request::cookie()` 함수를 통해 접근할 수 있으며, 애플리케이션이 요청 완료 핸들러에서 외부 리소스와 매핑하는 데 주로 사용됩니다. 이 쿠키는 libcamera 에게는 불투명하게 처리됩니다. `src/libcamera/camera.cpp:1243`

이 함수는 스레드 안전하며, 카메라가 정의된 Configured 또는 Running 상태일 때만 호출할 수 있습니다. 다른 상태에서는 호출을 시도하면 오류가 발생할 수 있습니다. `src/libcamera/camera.cpp:1243`

근거 원문: [src/libcamera/camera.cpp:1243](#source-d61960ed2545ba78)

## 캡처 세션의 상태와 자원

캡처를 시작하려면 먼저 카메라를 획득하고 설정해야 합니다. 이 단계에서 카메라가 요청을 처리할 준비가 됩니다. `src/libcamera/camera.cpp:769`

카메라를 해제하지 않은 상태라면 여러 번 시작하고 정지할 수 있으며, 설정을 다시 변경해도 됩니다. `src/libcamera/camera.cpp:769`

카메라는 정지될 때까지 요청을 처리합니다. 애플리케이션이 카메라를 더 이상 필요로 하지 않으면 해제해야 합니다. `src/libcamera/camera.cpp:769`

근거 원문: [src/libcamera/camera.cpp:769](#source-04f354bc331ec5c1)

## 요청 제출과 완료

요청을 제출하기 전에 반드시 하나 이상의 캡처 버퍼를 채워야 합니다. 버퍼가 없는 요청은 무효로 간주되어 큐에 추가되지 않습니다. `src/libcamera/camera.cpp:1308`

요청이 큐에 성공적으로 등록되면 카메라는 requestCompleted 신호를 통해 완료 상태를 알립니다. `src/libcamera/camera.cpp:1308`

이 함수는 카메라가 Running 상태일 때만 호출할 수 있으며, 스레드 안전성을 보장합니다. `src/libcamera/camera.cpp:1308`

실행 확인 항목: 카메라가 실행 중이 아니면 요청을 큐에 추가할 수 없으므로 -EACCES 오류 코드를 반환합니다. `src/libcamera/camera.cpp:1308`

근거 원문: [src/libcamera/camera.cpp:1308](#source-2f880c124115c9c4)

## 버퍼 완료와 요청 완료

버퍼가 끝났다고 알리는 역할만 합니다. 이 함수는 애플리케이션에 버퍼 완료를 알려주고 요청 내부의 추적 정보를 갱신합니다. `src/libcamera/pipeline_handler.cpp:547`

마지막 버퍼가 끝났다고 해서 자동으로 요청이 완료되는 것은 아닙니다. 이렇게 설계된 이유는 파이프라인 핸들러가 아직 해야 할 일이 있을 수 있기 때문입니다. `src/libcamera/pipeline_handler.cpp:547`

핸들러가 필요한 작업을 모두 마친 뒤에는 반드시 completeRequest() 함수를 호출해서 요청을 명시적으로 완료해야 합니다. `src/libcamera/pipeline_handler.cpp:547`

근거 원문: [src/libcamera/pipeline_handler.cpp:547](#source-ca3f659653ce3f6a)

## 스레드 경계와 동기화

카메라 상태를 변경하는 함수들은 서로 동기화되지 않습니다. 호출자가 필요한 경우 자체적으로 동기화를 보장해야 합니다. `src/libcamera/camera.cpp:780`

`PipelineHandler::completeRequest()` 는 반드시 `CameraManager` 스레드에서 호출되어야 합니다. `src/libcamera/pipeline_handler.cpp:571`

근거 원문: [src/libcamera/camera.cpp:780](#source-33ababe2a4780075) · [src/libcamera/pipeline_handler.cpp:571](#source-7ac40780a56ae3a9)

## 정적 근거의 확인 범위

`Camera::start()` 함수는 카메라가 설정된 상태인 경우에만 호출할 수 있습니다. 호출자는 이 함수를 다른 상태 변경 함수와 동기화해야 합니다. `src/libcamera/camera.cpp:1383`

성공 시 0 을 반환하며, 실패 시 음수 오류 코드를 반환합니다. `src/libcamera/camera.cpp:1383`

실행 확인 항목: 카메라가 시작 타이밍에 파이프라인 핸들러에게 기대하는 정확한 동작은 아직 문서화되지 않았습니다. `src/libcamera/camera.cpp:755`

근거 원문: [src/libcamera/camera.cpp:1383](#source-9fe53bb2bee0d8b7) · [src/libcamera/camera.cpp:755](#source-6874d2b69bd02915)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | Camera는 어떤 공개 기능과 객체 수명 계약을 제공합니까? | [컴포넌트별 책임](#컴포넌트별-책임) | 코드 근거와 설명 연결 |
    | 장치 탐색과 파이프라인 매칭·카메라 등록은 누가 담당합니까? | [탐색과 파이프라인 선택](#탐색과-파이프라인-선택) | 코드 근거와 설명 연결 |
    | 요청 생성의 조건과 소유권·재사용 계약은 무엇입니까? | [요청 생성과 소유권](#요청-생성과-소유권) | 코드 근거와 설명 연결 |
    | 캡처를 준비하고 반복하고 끝내는 순서는 무엇입니까? | [캡처 세션의 상태와 자원](#캡처-세션의-상태와-자원) | 코드 근거와 설명 연결 |
    | 요청을 어떤 조건으로 제출하고 완료를 어떻게 통지받습니까? | [요청 제출과 완료](#요청-제출과-완료) | 코드 근거와 설명 연결 · 실행 확인 항목 별도 |
    | 버퍼 완료와 요청 완료는 어떻게 구분합니까? | [버퍼 완료와 요청 완료](#버퍼-완료와-요청-완료) | 코드 근거와 설명 연결 |
    | 상태 변경의 동기화 책임과 요청 완료의 실행 스레드는 무엇입니까? | [스레드 경계와 동기화](#스레드-경계와-동기화) | 코드 근거와 설명 연결 |
    | 시작 API의 명시된 계약과 아직 문서화되지 않은 타이밍은 무엇입니까? | [정적 근거의 확인 범위](#정적-근거의-확인-범위) | 코드 근거와 설명 연결 · 실행 확인 항목 별도 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-6c066281dcce33d6"></a>

??? note "소스 근거: src/libcamera/camera.cpp:758"
    `src/libcamera/camera.cpp:758`에서 시작하는 발췌입니다. 종료 줄은 769이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e77cee469b7c57430e4bd4b0f08493289c46b57549873521c476df388d591dc2`
    
    ```text
    The Camera class models a camera capable of producing one or more image
     * streams from a single image source. It provides the main interface to
     * configuring and controlling the device, and capturing image streams. It is
     * the central object exposed by libcamera.
     *
     * To support the central nature of Camera objects, libcamera manages the
     * lifetime of camera instances with std::shared_ptr<>. Instances shall be
     * created with the create() function which returns a shared pointer. The
     * Camera constructors and destructor are private, to prevent instances from
     * being constructed and destroyed manually.
     *
     * \section camera_operation
    ```

<a id="source-916045c55b34387b"></a>

??? note "소스 근거: src/libcamera/camera_manager.cpp:283"
    `src/libcamera/camera_manager.cpp:283`에서 시작하는 발췌입니다. 종료 줄은 288이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `ee52fb95672da1e50c86c11ccd1bcc37539110a6489fcb685ce073e2cd923809`
    
    ```text
    The camera manager is the entry point to libcamera. It enumerates devices,
     * associates them with pipeline managers, and provides access to the cameras
     * in the system to applications. The manager owns all Camera objects and
     * handles hot-plugging and hot-unplugging to manage the lifetime of cameras.
     *
     * To interact with libcamera,
    ```

<a id="source-5bbd41c1e725138c"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:86"
    `src/libcamera/pipeline_handler.cpp:86`에서 시작하는 발췌입니다. 종료 줄은 119이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `7dde6563cf6bda32f38f4c1fb3ef0443502432236a0222d4f811b3fa71f3fc05`
    
    ```text
    \fn PipelineHandler::match(DeviceEnumerator *enumerator)
     * \brief Match media devices and create camera instances
     * \param[in] enumerator The enumerator providing all media devices found in the
     * system
     *
     * This function is the main entry point of the pipeline handler. It is called
     * by the camera manager with the \a enumerator passed as an argument. It shall
     * acquire from the \a enumerator all the media devices it needs for a single
     * pipeline, create one or multiple Camera instances and register them with the
     * camera manager.
     *
     * If all media devices needed by the pipeline handler are found, they must all
     * be acquired by a call to MediaDevice::acquire(). This function shall then
     * create the corresponding Camera instances, store them internally, and return
     * true. Otherwise it shall not acquire any media device (or shall release all
     * the media devices is has acquired by calling MediaDevice::release()) and
     * return false.
     *
     * If multiple instances of a pipeline are available in the system, the
     * PipelineHandler class will be instantiated once per instance, and its match()
     * function called for every instance. Each call shall acquire media devices for
     * one pipeline instance, until all compatible media devices are exhausted.
     *
     * If this function returns true, a new instance of the pipeline handler will
     * be created and its match() function called.
     *
     * \context This function is called from the CameraManager thread.
     *
     * \return true if media devices have been acquired and camera instances
     * created, or false otherwise
     */
    
    /**
     * \brief Search and acquire a MediaDevice
    ```

<a id="source-d61960ed2545ba78"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1243"
    `src/libcamera/camera.cpp:1243`에서 시작하는 발췌입니다. 종료 줄은 1263이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e71b8c0bea6263314881525ebf4714628591079745c9453624d3f4c3dffe31d0`
    
    ```text
    \brief Create a request object for the camera
     * \param[in] cookie Opaque cookie for application use
     *
     * This function creates an empty request for the application to fill with
     * buffers and parameters, and queue for capture.
     *
     * The \a cookie is stored in the request and is accessible through the
     * Request::cookie() function at any time. It is typically used by applications
     * to map the request to an external resource in the request completion
     * handler, and is completely opaque to libcamera.
     *
     * The ownership of the returned request is passed to the caller, which is
     * responsible for deleting it. The request may be deleted in the completion
     * handler, or reused after resetting its state with Request::reuse().
     *
     * \context This function is \threadsafe. It may only be called when the camera
     * is in the Configured or Running state as defined in \ref camera_operation.
     *
     * \return A pointer to the newly created request, or nullptr on error
     */
    std::unique_ptr<Request> Camera::createRequest
    ```

<a id="source-04f354bc331ec5c1"></a>

??? note "소스 근거: src/libcamera/camera.cpp:769"
    `src/libcamera/camera.cpp:769`에서 시작하는 발췌입니다. 종료 줄은 780이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `73164878543e86e16cf4e3197648ec4e79819beaad2f1c8754260715f65b8333`
    
    ```text
    \section camera_operation Operating the Camera
     *
     * An application needs to perform a sequence of operations on a camera before
     * it is ready to process requests. The camera needs to be acquired and
     * configured to prepare the camera for capture. Once started the camera can
     * process requests until it is stopped. When an application is done with a
     * camera, the camera needs to be released.
     *
     * An application may start and stop a camera multiple times as long as it is
     * not released. The camera may also be reconfigured.
     *
     * Functions that affect the camera state
    ```

<a id="source-2f880c124115c9c4"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1308"
    `src/libcamera/camera.cpp:1308`에서 시작하는 발췌입니다. 종료 줄은 1330이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `b24af43d2f808f81b527cf4ee8915451be675f43f877bac5e6edfe69ff3739d6`
    
    ```text
    \brief Queue a request to the camera
     * \param[in] request The request to queue to the camera
     *
     * This function queues a \a request to the camera for capture.
     *
     * After allocating the request with createRequest(), the application shall
     * fill it with at least one capture buffer before queuing it. Requests that
     * contain no buffers are invalid and are rejected without being queued.
     *
     * Once the request has been queued, the camera will notify its completion
     * through the \ref requestCompleted signal.
     *
     * \context This function is \threadsafe. It may only be called when the camera
     * is in the Running state as defined in \ref camera_operation.
     *
     * \return 0 on success or a negative error code otherwise
     * \retval -ENODEV The camera has been disconnected from the system
     * \retval -EACCES The camera is not running so requests can't be queued
     * \retval -EXDEV The request does not belong to this camera
     * \retval -EINVAL The request is invalid
     * \retval -ENOMEM No buffer memory was available to handle the request
     */
    int Camera::queueRequest
    ```

<a id="source-ca3f659653ce3f6a"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:547"
    `src/libcamera/pipeline_handler.cpp:547`에서 시작하는 발췌입니다. 종료 줄은 563이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `49b0139e3f0f620c0a3c044caf699179753dddf1b896d48de417c338bbae6a22`
    
    ```text
    \brief Complete a buffer for a request
     * \param[in] request The request the buffer belongs to
     * \param[in] buffer The buffer that has completed
     *
     * This function shall be called by pipeline handlers to signal completion of
     * the \a buffer part of the \a request. It notifies applications of buffer
     * completion and updates the request's internal buffer tracking. The request
     * is not completed automatically when the last buffer completes to give
     * pipeline handlers a chance to perform any operation that may still be
     * needed. They shall complete requests explicitly with completeRequest().
     *
     * \context This function shall be called from the CameraManager thread.
     *
     * \return True if all buffers contained in the request have completed, false
     * otherwise
     */
    bool PipelineHandler::completeBuffer
    ```

<a id="source-33ababe2a4780075"></a>

??? note "소스 근거: src/libcamera/camera.cpp:780"
    `src/libcamera/camera.cpp:780`에서 시작하는 발췌입니다. 종료 줄은 784이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `943831ed5cf08179455c41bd83a649d74d2a4a2d53f153cfa83dbeff179c2bf6`
    
    ```text
    Functions that affect the camera state as defined below are generally not
     * synchronized with each other by the Camera class. The caller is responsible
     * for ensuring their synchronization if necessary.
     *
     * \subsection Camera States
    ```

<a id="source-7ac40780a56ae3a9"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:571"
    `src/libcamera/pipeline_handler.cpp:571`에서 시작하는 발췌입니다. 종료 줄은 584이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `25903b4c6a305017b96bfe9117fe2b7b917b51fbeb2fd21139700b1fbf6a4fe2`
    
    ```text
    \brief Signal request completion
     * \param[in] request The request that has completed
     *
     * The pipeline handler shall call this function to notify the \a camera that
     * the request has completed. The request is no longer managed by the pipeline
     * handler and shall not be accessed once this function returns.
     *
     * This function ensures that requests will be returned to the application in
     * submission order, the pipeline handler may call it on any complete request
     * without any ordering constraint.
     *
     * \context This function shall be called from the CameraManager thread.
     */
    void PipelineHandler::completeRequest
    ```

<a id="source-9fe53bb2bee0d8b7"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1383"
    `src/libcamera/camera.cpp:1383`에서 시작하는 발췌입니다. 종료 줄은 1400이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `3b6dec3d3372dc891ac15cca8f5c578ab56f76a0321a113a64f10a25f830283d`
    
    ```text
    \brief Start capture from camera
     * \param[in] controls Controls to be applied before starting the Camera
     *
     * Start the camera capture session, optionally providing a list of controls to
     * apply before starting. Once the camera is started the application can queue
     * requests to the camera to process and return to the application until the
     * capture session is terminated with \a stop().
     *
     * \context This function may only be called when the camera is in the
     * Configured state as defined in \ref camera_operation, and shall be
     * synchronized by the caller with other functions that affect the camera
     * state.
     *
     * \return 0 on success or a negative error code otherwise
     * \retval -ENODEV The camera has been disconnected from the system
     * \retval -EACCES The camera is not in a state where it can be started
     */
    int Camera::start
    ```

<a id="source-6874d2b69bd02915"></a>

??? note "소스 근거: src/libcamera/camera.cpp:755"
    `src/libcamera/camera.cpp:755`에서 시작하는 발췌입니다. 종료 줄은 758이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `fe1cde84836279cf75402cca5392d528cc43c3eff36066e3beb4822b75329a46`
    
    ```text
    \todo Add documentation for camera start timings. What exactly does the
     * camera expect the pipeline handler to do when start() is called?
     *
     * The Camera class models a camera
    ```


<!-- sdd:class-diagram -->
## 클래스 관계

화살표의 글자는 추출한 관계를 나타내며, 점선은 상속입니다. 화살표는 참조 대상 또는 기반 클래스를 향합니다. 호출 순서를 뜻하지 않습니다.

```mermaid
flowchart LR
  c0["Camera"]
  c1["CameraManager"]
  c2["Extensible"]:::context
  c3["IPAManager"]
  c4["Object"]:::context
  c5["PipelineHandler"]
  c6["Request"]
  c0 -.->|상속| c2
  c0 -.->|상속| c4
  c1 -.->|상속| c2
  c1 -.->|상속| c4
  c3 -->|필드 참조| c1
  c5 -->|필드 참조| c0
  c5 -->|필드 참조| c1
  c5 -.->|상속| c4
  c6 -.->|상속| c2
  classDef context fill:#fafafa,stroke:#aaa,stroke-dasharray:4 3,color:#555
```
<!-- /sdd:class-diagram -->



## 코드를 처음 읽는 순서

1. 진입점 `Camera::queueRequest(Request *)`의 입력 검사와 반환 조건을 확인합니다.
2. [요청 제출 (Camera::queueRequest)](scenarios/queue_request.md)에서 주요 호출과 추적 경계를 확인합니다.
3. 예약된 호출과 완료 통지를 구분하고, 실행 스레드는 연결 코드와 대조합니다.

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `include/libcamera/camera.h`, `include/libcamera/camera_manager.h`, `include/libcamera/internal/ipa_manager.h`, `include/libcamera/internal/pipeline_handler.h`, `include/libcamera/request.h`, `src/libcamera/base/log.cpp`, `src/libcamera/camera.cpp`, `src/libcamera/camera_manager.cpp`, `src/libcamera/controls.cpp`, `src/libcamera/ipa_manager.cpp`, `src/libcamera/pipeline_handler.cpp`, `src/libcamera/request.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `2c4b67c079`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-24 · 사람 검토 전

다음 단계: [카메라와 요청 모델](camera-model.md)
