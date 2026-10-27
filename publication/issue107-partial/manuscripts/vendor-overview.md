---
generated_at: 2026-10-27T00:53:30+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: vendor-overview
generation_method: facts-and-llm
evidence_fingerprint: 04c9a33369a1f4ac2eb82dee6c29fa458e105e321c6a0841eb9eaa1672b7a5d0
semantic_review: human-review-required
agent: response-bundle/claude-haiku-5-5-subagent-high
generated_design: {"schema": 1, "input_fingerprint": "04c9a33369a1f4ac2eb82dee6c29fa458e105e321c6a0841eb9eaa1672b7a5d0", "answers": {"value": [{"text": "`libcamera`는 `Linux`, `Android`, `ChromeOS`를 위한 오픈 소스 복잡한 카메라 지원 라이브러리입니다. 이 라이브러리는 `Linux` 커널 장치 드라이버와 연동하고, 개발자에게 직관적인 API를 제공하여 `Linux` 시스템에서 복잡한 카메라로 이미지를 캡처하는 과정의 복잡성을 단순화합니다.", "evidence": ["what"], "covers": ["value"], "kind": "behavior", "quote": "libcamera is an open source complex camera support library for Linux, Android\nand ChromeOS. The library interfaces with Linux kernel device drivers and\nprovides an intuitive API to developers in order to simplify the complexity\ninvolved in capturing images from complex cameras on Linux systems.", "part_id": "what"}, {"text": "커널 드라이버를 활용해 동작하는 카메라 스택을 구성하는 책임은 사용자 공간에 있으며, 이는 공통 아키텍처나 애플리케이션 개발자용 API 없이 벤더마다 따로 구현되는 경우가 일반적입니다. 특히 하드웨어 파이프라인의 차이와 커널 API에서 그 차이가 표현되는 방식을 고려하면, 맞춤형 처리가 자주 필요해져 작업의 복잡성이 크게 늘어납니다.", "evidence": ["problem"], "covers": ["value"], "kind": "behavior", "quote": "The usage of these drivers to provide a functioning camera stack is a\nresponsibility that lies in userspace, and is commonly implemented separately\nby vendors without a common architecture or API for application developers. This\nadds a lot of complexity to the task, particularly when considering that the\ndifferences in hardware pipelines and their representation in the kernel's APIs\noften necessitate bespoke handling.", "part_id": "problem"}, {"text": "`libcamera`는 `Linux` 기반 시스템에 완전한 카메라 스택을 제공하며, 커널 API를 통해 카메라에서 원하는 결과를 얻는 데 필요한 하드웨어 구성과 이미지 제어 알고리즘의 설정을 추상화합니다. 이 작업들을 개발자에게 단순하고 일관된 방법으로 줄입니다.", "evidence": ["for"], "covers": ["value"], "kind": "behavior", "quote": "libcamera provides a complete camera stack for Linux-based systems to abstract\nthe configuration of hardware and image control algorithms required to obtain\ndesirable results from the camera through the kernel's APIs, reducing those\noperations to a simple and consistent method for developers. In short instead of\nhaving to deal with this:", "part_id": "easier"}, {"text": "카메라 스택의 가장 아래 계층에서 커널 드라이버는 카메라 하드웨어를 제어하며, `Linux` 커널의 `V4L2` 계열 API인 `Media Controller API`, `V4L2 Video Device API`, `V4L2 Subdev API`를 통해 낮은 수준의 인터페이스를 사용자 공간에 노출합니다.", "evidence": ["stack"], "covers": ["value"], "kind": "behavior", "quote": "* The kernel drivers control the camera hardware and expose a\n  low-level interface to userspace through the Linux kernel V4L2\n  family of APIs (Media Controller API, V4L2 Video Device API and\n  V4L2 Subdev API).", "part_id": "layers"}, {"text": "그 위의 `libcamera` 프레임워크는 스택의 핵심 부분입니다. 핵심 구성요소인 `libcamera`에서 카메라 장치의 모든 제어를 처리하고, 상위 계층에 네이티브 `C++` API를 제공합니다. 선택적 언어 바인딩을 사용하면 다른 프로그래밍 언어에서도 `libcamera`와 연동할 수 있습니다.", "evidence": ["stack"], "covers": ["value"], "kind": "behavior", "quote": "* The libcamera framework is the core part of the stack. It\n  handles all control of the camera devices in its core component,\n  libcamera, and exposes a native C++ API to upper layers. Optional\n  language bindings allow interfacing to libcamera from other\n  programming languages.", "part_id": "layers"}, {"text": "`libcamera` 어댑테이션은 다른 프레임워크에서 `libcamera`와 연결되는 구성요소를 가리키는 포괄 용어입니다. 대표 예로 `V4L2` 호환성 계층, `gstreamer libcamera` 요소, `libcamera` 기반 `Android` 카메라 HAL 구현이 있습니다.", "evidence": ["stack"], "covers": ["value"], "kind": "behavior", "quote": "* The libcamera adaptation is an umbrella term designating the\n  components that interface to libcamera in other frameworks.\n  Notable examples are a V4L2 compatibility layer, a gstreamer\n  libcamera element, and an Android camera HAL implementation based\n  on libcamera.", "part_id": "layers"}, {"text": "애플리케이션과 상위 프레임워크는 `libcamera` 프레임워크 또는 `libcamera` 어댑테이션을 기반으로 하며, `libcamera` 프로젝트의 범위 밖에 있습니다.", "evidence": ["stack"], "covers": ["value"], "kind": "behavior", "quote": "* The applications and upper level frameworks are based on the\n  libcamera framework or libcamera adaptation, and are outside of\n  the scope of the libcamera project.", "part_id": "layers"}], "support": [{"text": "`libcamera`는 전용 파이프라인 핸들러를 갖춘 하드웨어 플랫폼으로 Arm `Mali-C55`, Intel `IPU3`(`ipu3`), NXP `i.MX8MP`(`imx8-isi`와 `rkisp1`), `RaspberryPi` 3, 4, zero(`rpi/vc4`), Rockchip `RK3399`(`rkisp1`)를 지원합니다.", "evidence": ["platforms"], "covers": ["support"], "kind": "behavior", "quote": "- Arm Mali-C55\n   - Intel IPU3 (ipu3)\n   - NXP i.MX8MP (imx8-isi and rkisp1)\n   - RaspberryPi 3, 4 and zero (rpi/vc4)\n   - Rockchip RK3399 (rkisp1)", "part_id": "dedicated"}, {"text": "`libcamera`는 이와 별도로 일반 플랫폼 지원 대상으로 USB 비디오 장치 클래스 카메라(`uvcvideo`), `iMX7`, `IPU6`, Allwinner `Sun6i`(`simple`), 테스트 사용 사례를 위한 가상 미디어 컨트롤러 드라이버(`vimc`)를 제공합니다.", "evidence": ["platforms"], "covers": ["support"], "kind": "behavior", "quote": "- USB video device class cameras (uvcvideo)\n   - iMX7, IPU6, Allwinner Sun6i (simple)\n   - Virtual media controller driver for test use cases (vimc)", "part_id": "generic"}, {"text": "`meson_options.txt`의 `pipelines` 옵션은 빌드할 파이프라인 핸들러를 선택합니다. 값이 `auto`이면 대상 아키텍처에 적용 가능한 모든 파이프라인이 빌드되고, 값이 `all`이면 모든 파이프라인이 빌드됩니다. 두 값을 함께 선택하면 `all`이 우선합니다.", "evidence": ["pipelines"], "covers": ["support"], "kind": "behavior", "quote": "option('pipelines',\n        type : 'array',\n        value : ['auto'],\n        choices : [\n            'all',\n            'auto',\n            'imx8-isi',\n            'ipu3',\n            'mali-c55',\n            'rkisp1',\n            'rpi/pisp',\n            'rpi/vc4',\n            'simple',\n            'uvcvideo',\n            'vimc',\n            'virtual'\n        ],\n        description : 'Select which pipeline handlers to build. If this is set to \"auto\", all the pipelines applicable to the target architecture will be built. If this is set to \"all\", all the pipelines will be built. If both are selected then \"all\" will take precedence.')", "part_id": "build"}], "capabilities": [{"text": "`Camera` 클래스는 단일 이미지 소스에서 하나 이상의 이미지 스트림을 생성할 수 있는 카메라를 모델링합니다. 이 클래스는 장치를 구성하고 제어하며 이미지 스트림을 캡처하는 주요 인터페이스를 제공하고, `libcamera`가 노출하는 중심 객체입니다.", "evidence": ["camera"], "covers": ["capabilities"], "kind": "behavior", "quote": "\\class Camera\n * \\brief Camera device\n *\n * \\todo Add documentation for camera start timings. What exactly does the\n * camera expect the pipeline handler to do when start() is called?\n *\n * The Camera class models a camera capable of producing one or more image\n * streams from a single image source. It provides the main interface to\n * configuring and controlling the device, and capturing image streams. It is\n * the central object exposed by libcamera.\n *\n * To support the central nature of Camera objects, libcamera manages the\n * lifetime of camera instances with std::shared_ptr<>. Instances shall be\n * created with the create() function which returns a shared pointer. The\n * Camera constructors and destructor are private, to prevent instances from\n * being constructed and destroyed manually.\n *\n * \\section camera_operation Operating the Camera\n *\n * An application needs to perform a sequence of operations on a camera before\n * it is ready to process requests. The camera needs to be acquired and\n * configured to prepare the camera for capture. Once started the camera can\n * process requests until it is stopped. When an application is done with a\n * camera, the camera needs to be released.\n *\n * An application may start and stop a camera multiple times as long as it is\n * not released. The camera may also be reconfigured.\n *\n * Functions that affect the camera state as defined below are generally not\n * synchronized with each other by the Camera class. The caller is responsible\n * for ensuring their synchronization if necessary.\n *\n * \\subsection Camera States", "part_id": "camera"}, {"text": "파이프라인 핸들러는 필요한 미디어 장치를 시스템에 존재하는 장치와 맞추는 책임을 지며, 필요한 장치를 모두 획득할 수 있게 되면 대응하는 `Camera` 인스턴스를 생성해야 합니다. `libcamera`가 지원하는 각 파이프라인은 파이프라인 핸들러 구현으로 뒷받침되어야 하고, `PipelineHandler`의 모든 하위 클래스는 `REGISTER_PIPELINE_HANDLER()` 매크로를 사용해 `libcamera`에 등록해야 합니다.", "evidence": ["handler"], "covers": ["capabilities"], "kind": "behavior", "quote": "\\file pipeline_handler.h\n * \\brief Create pipelines and cameras from a set of media devices\n *\n * Each pipeline supported by libcamera needs to be backed by a pipeline\n * handler implementation that operate on a set of media devices. The pipeline\n * handler is responsible for matching the media devices it requires with the\n * devices present in the system, and once all those devices can be acquired,\n * create corresponding Camera instances.\n *\n * Every subclass of PipelineHandler shall be registered with libcamera using\n * the REGISTER_PIPELINE_HANDLER() macro.\n */", "part_id": "hardware"}], "benefits": [{"text": "`PipelineHandler::queueRequest()`는 전달받은 요청을 내부 대기 목록에 추가합니다. 이 목록은 순회되며, 파이프라인 핸들러로 넘길 수 있게 준비된 요청이 최대 `maxQueuedRequestsDevice_`개까지 이 함수를 호출한 순서대로 전달됩니다.", "evidence": ["queue"], "covers": ["benefits"], "kind": "behavior", "quote": "\\fn PipelineHandler::queueRequest()\n * \\brief Queue a request\n * \\param[in] request The request to queue\n *\n * This function queues a capture request to the pipeline handler for\n * processing. The request is first added to the internal list of waiting\n * requests which have to be prepared to make sure they are ready for being\n * queued to the pipeline handler.\n *\n * The queue of waiting requests is iterated and up to \\a\n * maxQueuedRequestsDevice_ prepared requests are passed to the pipeline handler\n * in the same order they have been queued by calling this function.", "part_id": "queue"}, {"text": "요청이 준비 단계에서 실패하거나, 파이프라인 핸들러가 요청을 하드웨어 큐에 등록하는 데 실패하면 그 `Request`는 취소됩니다.", "evidence": ["failure"], "covers": ["benefits"], "kind": "behavior", "quote": "If a Request fails during the preparation phase or if the pipeline handler\n * fails in queuing the request to the hardware the request is cancelled.", "part_id": "failure"}, {"text": "큐에 넣은 요청을 추적하면, 파이프라인 핸들러가 `stop()`으로 정지될 때 모든 요청의 자동 완료가 보장됩니다. 요청 완료는 파이프라인 핸들러가 `completeRequest()` 함수로 통지해야 합니다.", "evidence": ["completion"], "covers": ["benefits"], "kind": "behavior", "quote": "Keeping track of queued requests ensures automatic completion of all requests\n * when the pipeline handler is stopped with stop(). Request completion shall be\n * signalled by the pipeline handler using the completeRequest() function.", "part_id": "completion"}], "queue-limit": [{"text": "`PipelineHandler` 생성자 선언에서 `maxQueuedRequestsDevice`의 기본값은 `32`입니다.", "evidence": ["default"], "covers": ["queue-limit"], "kind": "behavior", "quote": "PipelineHandler(CameraManager *manager,\n\t\t\tunsigned int maxQueuedRequestsDevice = 32);\n\tvirtual ~PipelineHandler();", "part_id": "default"}, {"text": "`maxQueuedRequestsDevice_`가 제한하는 요청 수는 파이프라인 핸들러가 기저 하드웨어에 큐잉하는 요청, 즉 장치 큐에 해당하며, 나머지 요청은 내부 대기 큐에 남아 나중 단계에서 큐잉됩니다.", "evidence": ["queue"], "covers": ["queue-limit"], "kind": "behavior", "quote": "\\var PipelineHandler::maxQueuedRequestsDevice_\n * \\brief The maximum number of requests the pipeline handler shall queue to the\n * device\n *\n * maxQueuedRequestsDevice_ limits the number of request that the\n * pipeline handler shall queue to the underlying hardware, in order to\n * saturate the pipeline with requests. The application may choose to queue\n * as many requests as it desires, however only maxQueuedRequestsDevice_\n * requests will be queued to the hardware at a given point in time. The\n * remaining requests will be kept waiting in the internal waiting\n * queue, to be queued at a later stage.\n */", "part_id": "queue"}, {"text": "애플리케이션은 원하는 만큼 요청을 큐에 넣을 수 있지만, 하드웨어에는 한 시점에 `maxQueuedRequestsDevice_`개의 요청만 큐잉되며 나머지 요청은 내부 대기 큐에서 기다렸다가 나중 단계에 큐잉됩니다.", "evidence": ["queue"], "covers": ["queue-limit"], "kind": "behavior", "quote": "\\var PipelineHandler::maxQueuedRequestsDevice_\n * \\brief The maximum number of requests the pipeline handler shall queue to the\n * device\n *\n * maxQueuedRequestsDevice_ limits the number of request that the\n * pipeline handler shall queue to the underlying hardware, in order to\n * saturate the pipeline with requests. The application may choose to queue\n * as many requests as it desires, however only maxQueuedRequestsDevice_\n * requests will be queued to the hardware at a given point in time. The\n * remaining requests will be kept waiting in the internal waiting\n * queue, to be queued at a later stage.\n */", "part_id": "waiting"}]}, "topic_inputs": {"value": "d66ad5527f5fc26c7fbdaeab2def5eb9aaaf17a3d80403b94e0dffcedecc797f", "support": "a191a3e4db9cdcb25c2932dccbd01aaca54ef542c3f4bb715cacd5b813ffd194", "capabilities": "b3e2c55ed6bdafb9810f6b931098782e5a1ca7e2392aaa008512c0dc3657b4b7", "benefits": "c7d02b2061b5cd7542190d3635aad4f8d881fcab74bbba0e78ada4abc4868dd8", "queue-limit": "21044552fba70df9f415610923dfa0ebfd33583be04abe1de630079f3073d811"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["value", "support", "capabilities", "benefits", "queue-limit"], "topic_agents": {"value": "response-bundle/claude-haiku-5-5-subagent-high", "support": "response-bundle/claude-haiku-5-5-subagent-high", "capabilities": "response-bundle/claude-haiku-5-5-subagent-high", "benefits": "response-bundle/claude-haiku-5-5-subagent-high", "queue-limit": "response-bundle/claude-haiku-5-5-subagent-high"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "body_sha256": "b088031063425b661bc57e60880b19caab8fa6980ad7f537edbb7b3d82fc8f83"}
---

# libcamera 제품 개요

**제품이 무엇이고 어디까지 지원하는지, 공통 설계가 구현자에게 해 주는 일을 확인하고 도입할 범위를 판단하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 연동 순서와 구현 책임을 확인하고 설정·요청·정지 계약을 적용하세요. | [연동 가이드](vendor-integration.md) |
| 지원 조건과 구성 제약을 확인하고 제품 도입 전에 검증할 범위를 정하세요. | [지원 범위와 검증](vendor-assurance.md) |
| 파이프라인 구현이 지켜야 하는 구성·요청·완료·종료 계약을 확인하세요. | [Pipeline Handler](pipeline-handler.md) |

## 무엇이며 누구의 어떤 문제를 푸는가

`libcamera`는 `Linux`, `Android`, `ChromeOS`를 위한 오픈 소스 복잡한 카메라 지원 라이브러리입니다. 이 라이브러리는 `Linux` 커널 장치 드라이버와 연동하고, 개발자에게 직관적인 API를 제공하여 `Linux` 시스템에서 복잡한 카메라로 이미지를 캡처하는 과정의 복잡성을 단순화합니다. 커널 드라이버를 활용해 동작하는 카메라 스택을 구성하는 책임은 사용자 공간에 있으며, 이는 공통 아키텍처나 애플리케이션 개발자용 API 없이 벤더마다 따로 구현되는 경우가 일반적입니다. 특히 하드웨어 파이프라인의 차이와 커널 API에서 그 차이가 표현되는 방식을 고려하면, 맞춤형 처리가 자주 필요해져 작업의 복잡성이 크게 늘어납니다. `Documentation/introduction.rst:10`, `Documentation/introduction.rst:35`

<!-- sdd:visual:camera-stack -->
### 카메라 스택의 네 계층

애플리케이션에서 카메라 하드웨어까지 어떤 계층을 지납니까? 지원 기종이나 성능을 보장하는 그림은 아닙니다.

```mermaid
flowchart TB
%% sdd:translations {"C++ API로 직접 사용": "Use the C++ API directly", "V4L2 계열 API로 제어": "Control through the V4L2 <br/>family of APIs", "libcamera 프레임워크": "libcamera framework", "libcamera에 연결": "Connect to libcamera", "다른 프레임워크를 거쳐 사용": "Use through another <br/>framework", "애플리케이션·상위 프레임워크": "Applications and <br/>upper-level frameworks", "어댑테이션 (V4L2 <br/>호환·GStreamer·Android HAL)": "Adaptation (V4L2 <br/>compatibility, GStreamer, <br/>Android HAL)", "커널 드라이버 (V4L2 계열 <br/>API)": "Kernel drivers (V4L2 family <br/>of APIs)"}
  v_apps["애플리케이션·상위 프레임워크"]
  v_adaptation["어댑테이션 (V4L2 <br/>호환·GStreamer·Android HAL)"]
  v_framework["libcamera 프레임워크"]
  v_kernel["커널 드라이버 (V4L2 계열 <br/>API)"]
  v_apps -->|"C++ API로 직접 사용"| v_framework
  v_apps -->|"다른 프레임워크를 거쳐 사용"| v_adaptation
  v_adaptation -->|"libcamera에 연결"| v_framework
  v_framework -->|"V4L2 계열 API로 제어"| v_kernel
```

[Mermaid 원문](vendor-overview.camera-stack.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | 애플리케이션·상위 프레임워크 | [Documentation/introduction.rst:137](#source-e3b563f549a8c46d) |
    | 어댑테이션 (V4L2 호환·GStreamer·Android HAL) | [Documentation/introduction.rst:137](#source-e3b563f549a8c46d) |
    | libcamera 프레임워크 | [Documentation/introduction.rst:137](#source-e3b563f549a8c46d) |
    | 커널 드라이버 (V4L2 계열 API) | [Documentation/introduction.rst:137](#source-e3b563f549a8c46d) |
    | C++ API로 직접 사용 | [Documentation/introduction.rst:137](#source-e3b563f549a8c46d) |
    | 다른 프레임워크를 거쳐 사용 | [Documentation/introduction.rst:137](#source-e3b563f549a8c46d) |
    | libcamera에 연결 | [Documentation/introduction.rst:137](#source-e3b563f549a8c46d) |
    | V4L2 계열 API로 제어 | [Documentation/introduction.rst:137](#source-e3b563f549a8c46d) |
<!-- /sdd:visual:camera-stack -->

`libcamera`는 `Linux` 기반 시스템에 완전한 카메라 스택을 제공하며, 커널 API를 통해 카메라에서 원하는 결과를 얻는 데 필요한 하드웨어 구성과 이미지 제어 알고리즘의 설정을 추상화합니다. 이 작업들을 개발자에게 단순하고 일관된 방법으로 줄입니다. 카메라 스택의 가장 아래 계층에서 커널 드라이버는 카메라 하드웨어를 제어하며, `Linux` 커널의 `V4L2` 계열 API인 `Media Controller API`, `V4L2 Video Device API`, `V4L2 Subdev API`를 통해 낮은 수준의 인터페이스를 사용자 공간에 노출합니다. `Documentation/introduction.rst:45`, `Documentation/introduction.rst:137`

그 위의 `libcamera` 프레임워크는 스택의 핵심 부분입니다. 핵심 구성요소인 `libcamera`에서 카메라 장치의 모든 제어를 처리하고, 상위 계층에 네이티브 `C++` API를 제공합니다. 선택적 언어 바인딩을 사용하면 다른 프로그래밍 언어에서도 `libcamera`와 연동할 수 있습니다. `Documentation/introduction.rst:137`

`libcamera` 어댑테이션은 다른 프레임워크에서 `libcamera`와 연결되는 구성요소를 가리키는 포괄 용어입니다. 대표 예로 `V4L2` 호환성 계층, `gstreamer libcamera` 요소, `libcamera` 기반 `Android` 카메라 HAL 구현이 있습니다. 애플리케이션과 상위 프레임워크는 `libcamera` 프레임워크 또는 `libcamera` 어댑테이션을 기반으로 하며, `libcamera` 프로젝트의 범위 밖에 있습니다. `Documentation/introduction.rst:137`

근거 원문: [Documentation/introduction.rst:10](#source-34fda84500757231) · [Documentation/introduction.rst:35](#source-de476c940b030e4a) · [Documentation/introduction.rst:45](#source-f350cabac0db8343) · [Documentation/introduction.rst:137](#source-e3b563f549a8c46d)

## 지원하는 하드웨어와 빌드 선택

`libcamera`는 전용 파이프라인 핸들러를 갖춘 하드웨어 플랫폼으로 Arm `Mali-C55`, Intel `IPU3`(`ipu3`), NXP `i.MX8MP`(`imx8-isi`와 `rkisp1`), `RaspberryPi` 3, 4, zero(`rpi/vc4`), Rockchip `RK3399`(`rkisp1`)를 지원합니다. `libcamera`는 이와 별도로 일반 플랫폼 지원 대상으로 USB 비디오 장치 클래스 카메라(`uvcvideo`), `iMX7`, `IPU6`, Allwinner `Sun6i`(`simple`), 테스트 사용 사례를 위한 가상 미디어 컨트롤러 드라이버(`vimc`)를 제공합니다. `Documentation/platform_support.rst:6`

`meson_options.txt`의 `pipelines` 옵션은 빌드할 파이프라인 핸들러를 선택합니다. 값이 `auto`이면 대상 아키텍처에 적용 가능한 모든 파이프라인이 빌드되고, 값이 `all`이면 모든 파이프라인이 빌드됩니다. 두 값을 함께 선택하면 `all`이 우선합니다. `meson_options.txt:75`

근거 원문: [Documentation/platform_support.rst:6](#source-9d6502e234c4647d) · [meson_options.txt:75](#source-691389506fe87b32)

## 제공 기능과 지원 범위

`Camera` 클래스는 단일 이미지 소스에서 하나 이상의 이미지 스트림을 생성할 수 있는 카메라를 모델링합니다. 이 클래스는 장치를 구성하고 제어하며 이미지 스트림을 캡처하는 주요 인터페이스를 제공하고, `libcamera`가 노출하는 중심 객체입니다. 파이프라인 핸들러는 필요한 미디어 장치를 시스템에 존재하는 장치와 맞추는 책임을 지며, 필요한 장치를 모두 획득할 수 있게 되면 대응하는 `Camera` 인스턴스를 생성해야 합니다. `libcamera`가 지원하는 각 파이프라인은 파이프라인 핸들러 구현으로 뒷받침되어야 하고, `PipelineHandler`의 모든 하위 클래스는 `REGISTER_PIPELINE_HANDLER()` 매크로를 사용해 `libcamera`에 등록해야 합니다. `src/libcamera/camera.cpp:752`, `src/libcamera/pipeline_handler.cpp:30`

<!-- sdd:visual:hardware-boundary -->
### 공통 Camera와 장치별 구현의 경계

장치 지원은 해당 PipelineHandler 구현과 필요한 미디어 장치 확보에 달려 있습니다. 지원 기종이나 성능을 보장하는 그림은 아닙니다.

```mermaid
flowchart TB
%% sdd:translations {"공통 Camera 인터페이스": "Common Camera interface", "장치별 PipelineHandler 구현": "Device-specific <br/>PipelineHandler", "필요 장치와 시스템 장치 매칭": "Match required devices to <br/>the system", "필요한 미디어 장치 확보": "Acquire required media <br/>devices", "확보 성공 시 Camera 생성": "Create Camera after <br/>acquisition"}
  v_handler["장치별 PipelineHandler 구현"]
  v_media["필요한 미디어 장치 확보"]
  v_camera["공통 Camera 인터페이스"]
  v_handler -->|"필요 장치와 시스템 장치 매칭"| v_media
  v_media -->|"확보 성공 시 Camera 생성"| v_camera
```

[Mermaid 원문](vendor-overview.hardware-boundary.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | 장치별 PipelineHandler 구현 | [src/libcamera/pipeline_handler.cpp:30](#source-05721740b01bcd0e) |
    | 필요한 미디어 장치 확보 | [src/libcamera/pipeline_handler.cpp:30](#source-05721740b01bcd0e) |
    | 공통 Camera 인터페이스 | [src/libcamera/camera.cpp:752](#source-8264067114dccdee) |
    | 필요 장치와 시스템 장치 매칭 | [src/libcamera/pipeline_handler.cpp:30](#source-05721740b01bcd0e) |
    | 확보 성공 시 Camera 생성 | [src/libcamera/pipeline_handler.cpp:30](#source-05721740b01bcd0e) |
<!-- /sdd:visual:hardware-boundary -->

근거 원문: [src/libcamera/camera.cpp:752](#source-8264067114dccdee) · [src/libcamera/pipeline_handler.cpp:30](#source-05721740b01bcd0e)

## 장치 구현자가 공통 계층에서 얻는 것

`PipelineHandler::queueRequest()`는 전달받은 요청을 내부 대기 목록에 추가합니다. 이 목록은 순회되며, 파이프라인 핸들러로 넘길 수 있게 준비된 요청이 최대 `maxQueuedRequestsDevice_`개까지 이 함수를 호출한 순서대로 전달됩니다. 요청이 준비 단계에서 실패하거나, 파이프라인 핸들러가 요청을 하드웨어 큐에 등록하는 데 실패하면 그 `Request`는 취소됩니다. `src/libcamera/pipeline_handler.cpp:447`, `src/libcamera/pipeline_handler.cpp:460`

큐에 넣은 요청을 추적하면, 파이프라인 핸들러가 `stop()`으로 정지될 때 모든 요청의 자동 완료가 보장됩니다. 요청 완료는 파이프라인 핸들러가 `completeRequest()` 함수로 통지해야 합니다. `src/libcamera/pipeline_handler.cpp:463`

근거 원문: [src/libcamera/pipeline_handler.cpp:447](#source-106682bf83e3416a) · [src/libcamera/pipeline_handler.cpp:460](#source-0a5bda976f5815de) · [src/libcamera/pipeline_handler.cpp:463](#source-35ab684c1adef175)

## 장치 요청 한도와 대기 큐

`PipelineHandler` 생성자 선언에서 `maxQueuedRequestsDevice`의 기본값은 `32`입니다. `maxQueuedRequestsDevice_`가 제한하는 요청 수는 파이프라인 핸들러가 기저 하드웨어에 큐잉하는 요청, 즉 장치 큐에 해당하며, 나머지 요청은 내부 대기 큐에 남아 나중 단계에서 큐잉됩니다. 애플리케이션은 원하는 만큼 요청을 큐에 넣을 수 있지만, 하드웨어에는 한 시점에 `maxQueuedRequestsDevice_`개의 요청만 큐잉되며 나머지 요청은 내부 대기 큐에서 기다렸다가 나중 단계에 큐잉됩니다. `include/libcamera/internal/pipeline_handler.h:38`, `src/libcamera/pipeline_handler.cpp:805`

근거 원문: [include/libcamera/internal/pipeline_handler.h:38](#source-0cf3f7eced88f3df) · [src/libcamera/pipeline_handler.cpp:805](#source-bf25a409490e6fa9)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 어떤 고객 문제를 해결하며 어떤 환경을 대상으로 합니까? | [무엇이며 누구의 어떤 문제를 푸는가](#무엇이며-누구의-어떤-문제를-푸는가) | 코드 근거와 설명 연결 |
    | 어디까지 지원하며 지원 대상은 어떻게 고릅니까? | [지원하는 하드웨어와 빌드 선택](#지원하는-하드웨어와-빌드-선택) | 코드 근거와 설명 연결 |
    | 어떤 기능을 제공하며 지원 범위는 어떤 구현에 달려 있습니까? | [제공 기능과 지원 범위](#제공-기능과-지원-범위) | 코드 근거와 설명 연결 |
    | 공통 구현을 활용할 수 있는 강점과 그 조건은 무엇입니까? | [장치 구현자가 공통 계층에서 얻는 것](#장치-구현자가-공통-계층에서-얻는-것) | 코드 근거와 설명 연결 |
    | 장치에 동시에 제출하는 요청 수의 기본 한도와 대기 요청의 처리는 무엇입니까? | [장치 요청 한도와 대기 큐](#장치-요청-한도와-대기-큐) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-34fda84500757231"></a>

??? note "소스 근거: Documentation/introduction.rst:10"
    `Documentation/introduction.rst:10`에서 시작하는 발췌입니다. 종료 줄은 13이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `84621541899cba7430b844bc03d13fc8e6f3f03e7c30556df0bf1cd11007494c`
    
    ```text
    libcamera is an open source complex camera support library for Linux, Android
    and ChromeOS. The library interfaces with Linux kernel device drivers and
    provides an intuitive API to developers in order to simplify the complexity
    involved in capturing images from complex cameras on Linux systems.
    ```

<a id="source-de476c940b030e4a"></a>

??? note "소스 근거: Documentation/introduction.rst:35"
    `Documentation/introduction.rst:35`에서 시작하는 발췌입니다. 종료 줄은 40이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `0c6b72f4ffe9e608101639096b5597a61f41f776e4f5ac4aaa43229c744db3f0`
    
    ```text
    The usage of these drivers to provide a functioning camera stack is a
    responsibility that lies in userspace, and is commonly implemented separately
    by vendors without a common architecture or API for application developers. This
    adds a lot of complexity to the task, particularly when considering that the
    differences in hardware pipelines and their representation in the kernel's APIs
    often necessitate bespoke handling.
    ```

<a id="source-f350cabac0db8343"></a>

??? note "소스 근거: Documentation/introduction.rst:45"
    `Documentation/introduction.rst:45`에서 시작하는 발췌입니다. 종료 줄은 49이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `56f623776b7eab9511de1f32c1f3080c4eab37239185f5134db6b2644760b1f5`
    
    ```text
    libcamera provides a complete camera stack for Linux-based systems to abstract
    the configuration of hardware and image control algorithms required to obtain
    desirable results from the camera through the kernel's APIs, reducing those
    operations to a simple and consistent method for developers. In short instead of
    having to deal with this:
    ```

<a id="source-e3b563f549a8c46d"></a>

??? note "소스 근거: Documentation/introduction.rst:137"
    `Documentation/introduction.rst:137`에서 시작하는 발췌입니다. 종료 줄은 165이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `750a623b45ad76fbd899b56427ad76ef91bdc922497972317df868fe538c3b03`
    
    ```text
    The camera stack comprises four software layers. From bottom to top:
    
    * The kernel drivers control the camera hardware and expose a
      low-level interface to userspace through the Linux kernel V4L2
      family of APIs (Media Controller API, V4L2 Video Device API and
      V4L2 Subdev API).
    
    * The libcamera framework is the core part of the stack. It
      handles all control of the camera devices in its core component,
      libcamera, and exposes a native C++ API to upper layers. Optional
      language bindings allow interfacing to libcamera from other
      programming languages.
    
      Those components live in the same source code repository and
      all together constitute the libcamera framework.
    
    * The libcamera adaptation is an umbrella term designating the
      components that interface to libcamera in other frameworks.
      Notable examples are a V4L2 compatibility layer, a gstreamer
      libcamera element, and an Android camera HAL implementation based
      on libcamera.
    
      Those components can live in the libcamera project source code
      in separate repositories, or move to their respective project's
      repository (for instance the gstreamer libcamera element).
    
    * The applications and upper level frameworks are based on the
      libcamera framework or libcamera adaptation, and are outside of
      the scope of the libcamera project.
    ```

<a id="source-9d6502e234c4647d"></a>

??? note "소스 근거: Documentation/platform_support.rst:6"
    `Documentation/platform_support.rst:6`에서 시작하는 발췌입니다. 종료 줄은 19이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `c3521ec69316b30bbb021a31f90ae53cd0d641f77c91a13ed2d6fa0f7266f2bb`
    
    ```text
    The library currently supports the following hardware platforms specifically
    with dedicated pipeline handlers:
    
       - Arm Mali-C55
       - Intel IPU3 (ipu3)
       - NXP i.MX8MP (imx8-isi and rkisp1)
       - RaspberryPi 3, 4 and zero (rpi/vc4)
       - Rockchip RK3399 (rkisp1)
    
    Furthermore, generic platform support is provided for the following:
    
       - USB video device class cameras (uvcvideo)
       - iMX7, IPU6, Allwinner Sun6i (simple)
       - Virtual media controller driver for test use cases (vimc)
    ```

<a id="source-691389506fe87b32"></a>

??? note "소스 근거: meson_options.txt:75"
    `meson_options.txt:75`에서 시작하는 발췌입니다. 종료 줄은 92이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `6884c14e5ebb9b81b76a500c4890a7c14db2e86c34395d71c496a6c86bf0b58d`
    
    ```text
    option('pipelines',
            type : 'array',
            value : ['auto'],
            choices : [
                'all',
                'auto',
                'imx8-isi',
                'ipu3',
                'mali-c55',
                'rkisp1',
                'rpi/pisp',
                'rpi/vc4',
                'simple',
                'uvcvideo',
                'vimc',
                'virtual'
            ],
            description : 'Select which pipeline handlers to build. If this is set to "auto", all the pipelines applicable to the target architecture will be built. If this is set to "all", all the pipelines will be built. If both are selected then "all" will take precedence.')
    ```

<a id="source-8264067114dccdee"></a>

??? note "소스 근거: src/libcamera/camera.cpp:752"
    `src/libcamera/camera.cpp:752`에서 시작하는 발췌입니다. 종료 줄은 784이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `325c2af6569c185be1bc686e1fb6d161782dcbc8db34a0fbb719cff005ba7625`
    
    ```text
    \class Camera
     * \brief Camera device
     *
     * \todo Add documentation for camera start timings. What exactly does the
     * camera expect the pipeline handler to do when start() is called?
     *
     * The Camera class models a camera capable of producing one or more image
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
     * \section camera_operation Operating the Camera
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
     * Functions that affect the camera state as defined below are generally not
     * synchronized with each other by the Camera class. The caller is responsible
     * for ensuring their synchronization if necessary.
     *
     * \subsection Camera States
    ```

<a id="source-05721740b01bcd0e"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:30"
    `src/libcamera/pipeline_handler.cpp:30`에서 시작하는 발췌입니다. 종료 줄은 43이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `2ba321cd394e987c2851002e9db5df0634635d71c749580c066e5556df90a715`
    
    ```text
    \file pipeline_handler.h
     * \brief Create pipelines and cameras from a set of media devices
     *
     * Each pipeline supported by libcamera needs to be backed by a pipeline
     * handler implementation that operate on a set of media devices. The pipeline
     * handler is responsible for matching the media devices it requires with the
     * devices present in the system, and once all those devices can be acquired,
     * create corresponding Camera instances.
     *
     * Every subclass of PipelineHandler shall be registered with libcamera using
     * the REGISTER_PIPELINE_HANDLER() macro.
     */
    
    using namespace std::chrono_literals;
    ```

<a id="source-106682bf83e3416a"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:447"
    `src/libcamera/pipeline_handler.cpp:447`에서 시작하는 발췌입니다. 종료 줄은 458이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `93b81531d0a6f65b242cd4cfe014e0a861502c2fc2ad1d5e1f593dda7564c17d`
    
    ```text
    \fn PipelineHandler::queueRequest()
     * \brief Queue a request
     * \param[in] request The request to queue
     *
     * This function queues a capture request to the pipeline handler for
     * processing. The request is first added to the internal list of waiting
     * requests which have to be prepared to make sure they are ready for being
     * queued to the pipeline handler.
     *
     * The queue of waiting requests is iterated and up to \a
     * maxQueuedRequestsDevice_ prepared requests are passed to the pipeline handler
     * in the same order they have been queued by calling this function.
    ```

<a id="source-0a5bda976f5815de"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:460"
    `src/libcamera/pipeline_handler.cpp:460`에서 시작하는 발췌입니다. 종료 줄은 461이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `06067fbd4ead51418e85617bc3d67c04439619836e4f024497d1583f6ac0787c`
    
    ```text
    If a Request fails during the preparation phase or if the pipeline handler
     * fails in queuing the request to the hardware the request is cancelled.
    ```

<a id="source-35ab684c1adef175"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:463"
    `src/libcamera/pipeline_handler.cpp:463`에서 시작하는 발췌입니다. 종료 줄은 465이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `c3d1253c0ef92dd7f0ef5fd41450b788e9aa00145ac2f65bf727bf6a11e08863`
    
    ```text
    Keeping track of queued requests ensures automatic completion of all requests
     * when the pipeline handler is stopped with stop(). Request completion shall be
     * signalled by the pipeline handler using the completeRequest() function.
    ```

<a id="source-0cf3f7eced88f3df"></a>

??? note "소스 근거: include/libcamera/internal/pipeline_handler.h:38"
    `include/libcamera/internal/pipeline_handler.h:38`에서 시작하는 발췌입니다. 종료 줄은 40이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `192dbd8152727ba28535110f878eaf807b85e7b9e7be25d58355dd1e0a94690a`
    
    ```text
    PipelineHandler(CameraManager *manager,
    			unsigned int maxQueuedRequestsDevice = 32);
    	virtual ~PipelineHandler();
    ```

<a id="source-bf25a409490e6fa9"></a>

??? note "소스 근거: src/libcamera/pipeline_handler.cpp:805"
    `src/libcamera/pipeline_handler.cpp:805`에서 시작하는 발췌입니다. 종료 줄은 819이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `bebb0d8c2cd1119a344011aa4263c60740456a685b32ed3f02cd6f49c1d6101e`
    
    ```text
    \var PipelineHandler::maxQueuedRequestsDevice_
     * \brief The maximum number of requests the pipeline handler shall queue to the
     * device
     *
     * maxQueuedRequestsDevice_ limits the number of request that the
     * pipeline handler shall queue to the underlying hardware, in order to
     * saturate the pipeline with requests. The application may choose to queue
     * as many requests as it desires, however only maxQueuedRequestsDevice_
     * requests will be queued to the hardware at a given point in time. The
     * remaining requests will be kept waiting in the internal waiting
     * queue, to be queued at a later stage.
     */
    
    /**
     * \fn PipelineHandler::name()
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
    - 근거 파일: `Documentation/introduction.rst`, `Documentation/platform_support.rst`, `include/libcamera/camera.h`, `include/libcamera/internal/ipa_manager.h`, `include/libcamera/internal/pipeline_handler.h`, `meson_options.txt`, `src/libcamera/camera.cpp`, `src/libcamera/ipa_manager.cpp`, `src/libcamera/pipeline/ipu3/ipu3.cpp`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp`, `src/libcamera/pipeline_handler.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `2c4b67c079`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-27 · 사람 검토 전

다음 단계: [연동 가이드](vendor-integration.md)
