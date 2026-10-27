---
generated_at: 2026-10-27T00:53:12+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: team-overview
generation_method: facts-and-llm
evidence_fingerprint: 591da4e17d16add42fbe67cf79417ecb3d0838749a258b54acd788e3d47dcb4a
semantic_review: human-review-required
agent: response-bundle/claude-haiku-5-5-subagent-high
generated_design: {"schema": 1, "input_fingerprint": "591da4e17d16add42fbe67cf79417ecb3d0838749a258b54acd788e3d47dcb4a", "answers": {"role": [{"text": "libcamera는 Linux, Android, ChromeOS를 대상으로 하는 오픈소스 복잡한 카메라 지원 라이브러리입니다. 이 라이브러리는 Linux kernel device driver와 연동하고, 개발자에게 직관적인 API를 제공합니다. 이를 통해 Linux 시스템에서 복잡한 카메라로 이미지를 캡처하는 과정의 복잡성을 줄입니다.", "evidence": ["what"], "covers": ["role"], "kind": "behavior", "quote": "libcamera is an open source complex camera support library for Linux, Android\nand ChromeOS. The library interfaces with Linux kernel device drivers and\nprovides an intuitive API to developers in order to simplify the complexity\ninvolved in capturing images from complex cameras on Linux systems.", "part_id": "what"}, {"text": "이러한 드라이버를 이용해 제대로 동작하는 카메라 스택(camera stack)을 구현하는 책임은 userspace에 있습니다. 이 작업은 흔히 vendor마다 따로 구현되며, 응용 프로그램 개발자를 위한 공통 아키텍처나 API가 없습니다. 하드웨어 파이프라인의 차이와 커널 API에서 그 차이가 표현되는 방식 때문에 맞춤형 처리가 자주 필요해지며, 이는 작업에 많은 복잡성을 더합니다.", "evidence": ["problem"], "covers": ["role"], "kind": "behavior", "quote": "The usage of these drivers to provide a functioning camera stack is a\nresponsibility that lies in userspace, and is commonly implemented separately\nby vendors without a common architecture or API for application developers. This\nadds a lot of complexity to the task, particularly when considering that the\ndifferences in hardware pipelines and their representation in the kernel's APIs\noften necessitate bespoke handling.", "part_id": "problem"}, {"text": "libcamera는 Linux 기반 시스템을 위한 완전한 카메라 스택(camera stack)을 제공합니다. 이 스택은 카메라에서 원하는 결과를 얻는 데 필요한 하드웨어 설정과 이미지 제어 알고리즘을 추상화(abstract)하고, 커널 API를 통해 이루어지는 이 작업들을 개발자가 쓸 수 있는 단순하고 일관된 방법 하나로 줄여 줍니다.", "evidence": ["for"], "covers": ["role"], "kind": "behavior", "quote": "libcamera provides a complete camera stack for Linux-based systems to abstract\nthe configuration of hardware and image control algorithms required to obtain\ndesirable results from the camera through the kernel's APIs, reducing those\noperations to a simple and consistent method for developers. In short instead of\nhaving to deal with this:", "part_id": "easier"}, {"text": "카메라 스택은 아래에서 위 순서로 네 개의 소프트웨어 계층으로 나뉘며, 가장 아래 계층인 kernel drivers는 카메라 하드웨어를 제어하고 V4L2 계열 API(Media `Controller` API, V4L2 Video `Device` API, V4L2 Subdev API)를 통해 낮은 수준의 인터페이스를 userspace에 노출합니다. 그 위의 libcamera framework는 스택의 핵심 부분으로, 카메라 장치의 모든 제어를 담당하고 상위 계층에 네이티브 C++ API를 제공합니다. 세 번째 계층인 libcamera adaptation은 다른 프레임워크와 연결되는 구성 요소를 가리키는 포괄적인 용어이며, 대표 예로 V4L2 호환성 계층, gstreamer libcamera 요소, libcamera 기반 Android 카메라 HAL 구현이 있습니다. 가장 위 계층인 애플리케이션과 상위 수준 프레임워크는 libcamera framework 또는 libcamera adaptation을 기반으로 하며, libcamera 프로젝트의 범위 밖에 있습니다.", "evidence": ["stack"], "covers": ["role"], "kind": "behavior", "quote": "The camera stack comprises four software layers. From bottom to top:\n\n* The kernel drivers control the camera hardware and expose a\n  low-level interface to userspace through the Linux kernel V4L2\n  family of APIs (Media Controller API, V4L2 Video Device API and\n  V4L2 Subdev API).\n\n* The libcamera framework is the core part of the stack. It\n  handles all control of the camera devices in its core component,\n  libcamera, and exposes a native C++ API to upper layers. Optional\n  language bindings allow interfacing to libcamera from other\n  programming languages.\n\n  Those components live in the same source code repository and\n  all together constitute the libcamera framework.\n\n* The libcamera adaptation is an umbrella term designating the\n  components that interface to libcamera in other frameworks.\n  Notable examples are a V4L2 compatibility layer, a gstreamer\n  libcamera element, and an Android camera HAL implementation based\n  on libcamera.\n\n  Those components can live in the libcamera project source code\n  in separate repositories, or move to their respective project's\n  repository (for instance the gstreamer libcamera element).\n\n* The applications and upper level frameworks are based on the\n  libcamera framework or libcamera adaptation, and are outside of\n  the scope of the libcamera project.", "part_id": "layers"}], "inputs": [{"text": "아래 계층인 kernel drivers는 카메라 하드웨어를 제어하고, Linux 커널의 V4L2 계열 API(Media `Controller` API, V4L2 Video `Device` API, V4L2 Subdev API)를 통해 낮은 수준의 인터페이스를 userspace에 노출합니다. 이 구절에는 libcamera가 이 인터페이스를 어떻게 받아 쓰는지가 나와 있지 않으므로, 이 구절만으로는 그 내용을 확정할 수 없습니다.", "evidence": ["kernel"], "covers": ["inputs"], "kind": "behavior", "quote": "* The kernel drivers control the camera hardware and expose a\n  low-level interface to userspace through the Linux kernel V4L2\n  family of APIs (Media Controller API, V4L2 Video Device API and\n  V4L2 Subdev API).", "part_id": "below"}, {"text": "카메라는 `Camera` Manager가 열거(enumerate)합니다. `Camera` Manager는 libcamera가 지원하는 각 카메라를 관리하기 위해 Pipeline Handler를 인스턴스화(instantiate)합니다. `Camera` Manager 인스턴스는 애플리케이션마다 하나만 실행되며, 한 번에 단일 애플리케이션만 카메라 장치의 제어권을 가질 수 있도록 보장합니다.", "evidence": ["manager"], "covers": ["inputs"], "kind": "behavior", "quote": "The Camera Manager enumerates cameras and instantiates Pipeline Handlers to\n  manage each Camera that libcamera supports. The Camera Manager supports\n  hotplug detection and notification events when supported by the underlying\n  kernel devices.\n\n  There is only ever one instance of the Camera Manager running per application.\n  Each application's instance of the Camera Manager ensures that only a single\n  application can take control of a camera device at once.", "part_id": "discover"}], "outputs": [{"text": "libcamera framework는 스택의 핵심 부분으로, 핵심 구성 요소인 libcamera가 카메라 장치의 모든 제어를 처리하고 상위 계층(upper layers)에 네이티브 C++ API를 제공합니다. libcamera가 노출하는 객체 중 가장 상위 수준의 객체는 `Camera` 클래스이며, 하나의 카메라 하드웨어 항목을 나타내고 이미지 스트림을 만들 수 있는 기반 장치와 상호작용하는 API를 제공합니다. 같은 하드웨어가 여러 개 연결된 시스템에서는 각 하드웨어가 자신의 `Camera` 클래스 인스턴스를 가지며, 설정부터 캡처까지 다른 API 작업들이 이 객체와 상호작용합니다.", "evidence": ["framework", "camera"], "covers": ["outputs"], "kind": "behavior", "quote": "The Camera class represents a single item of camera hardware that is capable\n  of producing one or more image streams, and provides the API to interact with\n  the underlying device.\n\n  If a system has multiple instances of the same hardware attached, each has its\n  own instance of the camera class.\n\n  The API exposes full control of the device to upper layers of libcamera through\n  the public API, making it the highest level object libcamera exposes, and the\n  object that all other API operations interact with from configuration to\n  capture.", "part_id": "api"}, {"text": "libcamera adaptation은 다른 프레임워크에서 libcamera에 연결되는 구성 요소들을 가리키는 포괄적인 용어입니다. 대표 예로 V4L2 호환성 계층(V4L2 compatibility layer), gstreamer libcamera 요소, libcamera 기반의 Android 카메라 HAL 구현이 있습니다. 이 구성 요소들은 libcamera 프로젝트의 소스 코드 저장소 안의 별도 저장소에 있을 수 있으며, 예를 들어 gstreamer libcamera 요소처럼 각 프로젝트의 저장소로 옮겨질 수도 있습니다.", "evidence": ["adaptation"], "covers": ["outputs"], "kind": "behavior", "quote": "* The libcamera adaptation is an umbrella term designating the\n  components that interface to libcamera in other frameworks.\n  Notable examples are a V4L2 compatibility layer, a gstreamer\n  libcamera element, and an Android camera HAL implementation based\n  on libcamera.\n\n  Those components can live in the libcamera project source code\n  in separate repositories, or move to their respective project's\n  repository (for instance the gstreamer libcamera element).", "part_id": "adapters"}], "boundaries": [{"text": "이 프로젝트의 범위 밖에 있는 것은 애플리케이션과 상위 수준 프레임워크입니다. 이들은 libcamera framework 또는 libcamera adaptation을 기반으로 하지만, libcamera 프로젝트의 범위에는 포함되지 않습니다.", "evidence": ["apps"], "covers": ["boundaries"], "kind": "behavior", "quote": "* The applications and upper level frameworks are based on the\n  libcamera framework or libcamera adaptation, and are outside of\n  the scope of the libcamera project.", "part_id": "outside"}, {"text": "장치 제조사(vendor)가 기여하는 부분 중 하나는 장치별 Pipeline Handler이며, 이 핸들러는 libcamera 코드 베이스의 일부로서 장치 제조사가 upstream에 기여해야 합니다. IPA 모듈은 3A(Auto-Exposure, Auto-White Balance, Auto-Focus) 등을 구현하는 `Image` Processing Algorithms(IPA)이며, libcamera 코드 베이스에 포함될 수 있고 카메라 vendor가 외부에서 따로 제공할 수도 있습니다. libcamera에 포함된 IPA 모듈은 자유 소프트웨어 라이선스를 따르며, 외부 IPA 모듈은 오픈소스 또는 비공개 소스가 될 수 있습니다. 제3자는 libcamera 프로젝트의 소스 코드를 포함하지 않는다는 조건에서 비공개 소스 라이선스로 IPA 모듈을 개발하고 배포할 수 있습니다.", "evidence": ["handler", "ipa", "licensing"], "covers": ["boundaries"], "kind": "behavior", "quote": "Handlers are a part of the libcamera code base and need to be contributed\nupstream by device vendors. IPA modules included in libcamera are covered by a\nfree software license, however third-parties may develop IPA modules outside of\nlibcamera and distribute them under a closed-source license, provided they do\nnot include source code from the libcamera project.", "part_id": "vendors"}]}, "topic_inputs": {"role": "6a4feef953246976fff8fb1898306cd296a156305fcd84d6e42848f965ae9cfc", "inputs": "5d6978210abf92beb7d0c408059e52263c5a126239303d0e20ce519551888930", "outputs": "efd9721b430390171a9872143be2f536d8a4ff18f845cbafaf3e668ae52733d6", "boundaries": "b5d27085c8f9e8c620df12ca7c2603f87294243925e3181af214b10a18062620"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["role", "inputs", "outputs", "boundaries"], "topic_agents": {"role": "response-bundle/claude-haiku-5-5-subagent-high", "inputs": "response-bundle/claude-haiku-5-5-subagent-high", "outputs": "response-bundle/claude-haiku-5-5-subagent-high", "boundaries": "response-bundle/claude-haiku-5-5-subagent-high"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "body_sha256": "007be9b0b0956d284f4ba57da4f930bda394187c02b222530aa988ae00a21ebd"}
---

# 이 프로젝트가 하는 일

**이 프로젝트가 무엇을 받아 무엇을 내놓는지, 어느 계층·팀과 맞닿아 있는지 짧게 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 하는 일 절을 확인합니다. | [하는 일](#하는-일) |
| 받는 것 절을 확인합니다. | [받는 것](#받는-것) |
| 내놓는 것 절을 확인합니다. | [내놓는 것](#내놓는-것) |
| 다른 팀·계층과의 경계 절을 확인합니다. | [다른 팀·계층과의 경계](#다른-팀계층과의-경계) |

## 하는 일

libcamera는 Linux, Android, ChromeOS를 대상으로 하는 오픈소스 복잡한 카메라 지원 라이브러리입니다. 이 라이브러리는 Linux kernel device driver와 연동하고, 개발자에게 직관적인 API를 제공합니다. 이를 통해 Linux 시스템에서 복잡한 카메라로 이미지를 캡처하는 과정의 복잡성을 줄입니다. `Documentation/introduction.rst:10`

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

[Mermaid 원문](team-overview.camera-stack.mmd)

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

이러한 드라이버를 이용해 제대로 동작하는 카메라 스택(camera stack)을 구현하는 책임은 userspace에 있습니다. 이 작업은 흔히 vendor마다 따로 구현되며, 응용 프로그램 개발자를 위한 공통 아키텍처나 API가 없습니다. 하드웨어 파이프라인의 차이와 커널 API에서 그 차이가 표현되는 방식 때문에 맞춤형 처리가 자주 필요해지며, 이는 작업에 많은 복잡성을 더합니다. `Documentation/introduction.rst:35`

libcamera는 Linux 기반 시스템을 위한 완전한 카메라 스택(camera stack)을 제공합니다. 이 스택은 카메라에서 원하는 결과를 얻는 데 필요한 하드웨어 설정과 이미지 제어 알고리즘을 추상화(abstract)하고, 커널 API를 통해 이루어지는 이 작업들을 개발자가 쓸 수 있는 단순하고 일관된 방법 하나로 줄여 줍니다. `Documentation/introduction.rst:45`

카메라 스택은 아래에서 위 순서로 네 개의 소프트웨어 계층으로 나뉘며, 가장 아래 계층인 kernel drivers는 카메라 하드웨어를 제어하고 V4L2 계열 API(Media `Controller` API, V4L2 Video `Device` API, V4L2 Subdev API)를 통해 낮은 수준의 인터페이스를 userspace에 노출합니다. 그 위의 libcamera framework는 스택의 핵심 부분으로, 카메라 장치의 모든 제어를 담당하고 상위 계층에 네이티브 C++ API를 제공합니다. 세 번째 계층인 libcamera adaptation은 다른 프레임워크와 연결되는 구성 요소를 가리키는 포괄적인 용어이며, 대표 예로 V4L2 호환성 계층, gstreamer libcamera 요소, libcamera 기반 Android 카메라 HAL 구현이 있습니다. 가장 위 계층인 애플리케이션과 상위 수준 프레임워크는 libcamera framework 또는 libcamera adaptation을 기반으로 하며, libcamera 프로젝트의 범위 밖에 있습니다. `Documentation/introduction.rst:137`

근거 원문: [Documentation/introduction.rst:10](#source-34fda84500757231) · [Documentation/introduction.rst:35](#source-de476c940b030e4a) · [Documentation/introduction.rst:45](#source-f350cabac0db8343) · [Documentation/introduction.rst:137](#source-e3b563f549a8c46d)

## 받는 것

아래 계층인 kernel drivers는 카메라 하드웨어를 제어하고, Linux 커널의 V4L2 계열 API(Media `Controller` API, V4L2 Video `Device` API, V4L2 Subdev API)를 통해 낮은 수준의 인터페이스를 userspace에 노출합니다. 이 구절에는 libcamera가 이 인터페이스를 어떻게 받아 쓰는지가 나와 있지 않으므로, 이 구절만으로는 그 내용을 확정할 수 없습니다. `Documentation/introduction.rst:139`

카메라는 `Camera` Manager가 열거(enumerate)합니다. `Camera` Manager는 libcamera가 지원하는 각 카메라를 관리하기 위해 Pipeline Handler를 인스턴스화(instantiate)합니다. `Camera` Manager 인스턴스는 애플리케이션마다 하나만 실행되며, 한 번에 단일 애플리케이션만 카메라 장치의 제어권을 가질 수 있도록 보장합니다. `Documentation/libcamera_architecture.rst:60`

근거 원문: [Documentation/introduction.rst:139](#source-e93209ecbe248c51) · [Documentation/libcamera_architecture.rst:60](#source-64bdc114ca74bd2c)

## 내놓는 것

libcamera framework는 스택의 핵심 부분으로, 핵심 구성 요소인 libcamera가 카메라 장치의 모든 제어를 처리하고 상위 계층(upper layers)에 네이티브 C++ API를 제공합니다. libcamera가 노출하는 객체 중 가장 상위 수준의 객체는 `Camera` 클래스이며, 하나의 카메라 하드웨어 항목을 나타내고 이미지 스트림을 만들 수 있는 기반 장치와 상호작용하는 API를 제공합니다. 같은 하드웨어가 여러 개 연결된 시스템에서는 각 하드웨어가 자신의 `Camera` 클래스 인스턴스를 가지며, 설정부터 캡처까지 다른 API 작업들이 이 객체와 상호작용합니다. `Documentation/introduction.rst:144`, `Documentation/libcamera_architecture.rst:72`

libcamera adaptation은 다른 프레임워크에서 libcamera에 연결되는 구성 요소들을 가리키는 포괄적인 용어입니다. 대표 예로 V4L2 호환성 계층(V4L2 compatibility layer), gstreamer libcamera 요소, libcamera 기반의 Android 카메라 HAL 구현이 있습니다. 이 구성 요소들은 libcamera 프로젝트의 소스 코드 저장소 안의 별도 저장소에 있을 수 있으며, 예를 들어 gstreamer libcamera 요소처럼 각 프로젝트의 저장소로 옮겨질 수도 있습니다. `Documentation/introduction.rst:153`

근거 원문: [Documentation/introduction.rst:144](#source-d47b8630f593cf3c) · [Documentation/libcamera_architecture.rst:72](#source-611760d3be65ec8c) · [Documentation/introduction.rst:153](#source-72dfdf22c79d4609)

## 다른 팀·계층과의 경계

이 프로젝트의 범위 밖에 있는 것은 애플리케이션과 상위 수준 프레임워크입니다. 이들은 libcamera framework 또는 libcamera adaptation을 기반으로 하지만, libcamera 프로젝트의 범위에는 포함되지 않습니다. `Documentation/introduction.rst:163`

장치 제조사(vendor)가 기여하는 부분 중 하나는 장치별 Pipeline Handler이며, 이 핸들러는 libcamera 코드 베이스의 일부로서 장치 제조사가 upstream에 기여해야 합니다. IPA 모듈은 3A(Auto-Exposure, Auto-White Balance, Auto-Focus) 등을 구현하는 `Image` Processing Algorithms(IPA)이며, libcamera 코드 베이스에 포함될 수 있고 카메라 vendor가 외부에서 따로 제공할 수도 있습니다. libcamera에 포함된 IPA 모듈은 자유 소프트웨어 라이선스를 따르며, 외부 IPA 모듈은 오픈소스 또는 비공개 소스가 될 수 있습니다. 제3자는 libcamera 프로젝트의 소스 코드를 포함하지 않는다는 조건에서 비공개 소스 라이선스로 IPA 모듈을 개발하고 배포할 수 있습니다. `Documentation/libcamera_architecture.rst:87`, `Documentation/libcamera_architecture.rst:109`, `Documentation/introduction.rst:200`

근거 원문: [Documentation/introduction.rst:163](#source-9e653b8ff755db78) · [Documentation/libcamera_architecture.rst:87](#source-8bd888bd0473995e) · [Documentation/libcamera_architecture.rst:109](#source-1f130cc8640ef810) · [Documentation/introduction.rst:200](#source-341442e08591ef50)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 이 프로젝트는 무엇을 하며 누구의 어떤 문제를 풉니까? | [하는 일](#하는-일) | 코드 근거와 설명 연결 |
    | 이 프로젝트는 무엇을 입력으로 받습니까? | [받는 것](#받는-것) | 코드 근거와 설명 연결 |
    | 이 프로젝트는 무엇을 결과로 내놓습니까? | [내놓는 것](#내놓는-것) | 코드 근거와 설명 연결 |
    | 어느 계층·팀과 책임이 나뉩니까? | [다른 팀·계층과의 경계](#다른-팀계층과의-경계) | 코드 근거와 설명 연결 |

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

<a id="source-e93209ecbe248c51"></a>

??? note "소스 근거: Documentation/introduction.rst:139"
    `Documentation/introduction.rst:139`에서 시작하는 발췌입니다. 종료 줄은 142이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `33d991f6b824d355da564d0c328fb633374964b7dfee2b8e68b450cb29a80efa`
    
    ```text
    * The kernel drivers control the camera hardware and expose a
      low-level interface to userspace through the Linux kernel V4L2
      family of APIs (Media Controller API, V4L2 Video Device API and
      V4L2 Subdev API).
    ```

<a id="source-64bdc114ca74bd2c"></a>

??? note "소스 근거: Documentation/libcamera_architecture.rst:60"
    `Documentation/libcamera_architecture.rst:60`에서 시작하는 발췌입니다. 종료 줄은 67이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `bd036b31d192ef7504f07202ebcbc475e23b8b4387bf322ddf529accbbb786a7`
    
    ```text
    The Camera Manager enumerates cameras and instantiates Pipeline Handlers to
      manage each Camera that libcamera supports. The Camera Manager supports
      hotplug detection and notification events when supported by the underlying
      kernel devices.
    
      There is only ever one instance of the Camera Manager running per application.
      Each application's instance of the Camera Manager ensures that only a single
      application can take control of a camera device at once.
    ```

<a id="source-d47b8630f593cf3c"></a>

??? note "소스 근거: Documentation/introduction.rst:144"
    `Documentation/introduction.rst:144`에서 시작하는 발췌입니다. 종료 줄은 151이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `69bc145221729420c980f5fe5887a43497e96b41eb16fa12ed7fdef01ccfdb97`
    
    ```text
    * The libcamera framework is the core part of the stack. It
      handles all control of the camera devices in its core component,
      libcamera, and exposes a native C++ API to upper layers. Optional
      language bindings allow interfacing to libcamera from other
      programming languages.
    
      Those components live in the same source code repository and
      all together constitute the libcamera framework.
    ```

<a id="source-611760d3be65ec8c"></a>

??? note "소스 근거: Documentation/libcamera_architecture.rst:72"
    `Documentation/libcamera_architecture.rst:72`에서 시작하는 발췌입니다. 종료 줄은 82이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `d64fa7a71ca69a53433d250a2fd8f59a0beed2578980eee658d8dfb44a7513ee`
    
    ```text
    The Camera class represents a single item of camera hardware that is capable
      of producing one or more image streams, and provides the API to interact with
      the underlying device.
    
      If a system has multiple instances of the same hardware attached, each has its
      own instance of the camera class.
    
      The API exposes full control of the device to upper layers of libcamera through
      the public API, making it the highest level object libcamera exposes, and the
      object that all other API operations interact with from configuration to
      capture.
    ```

<a id="source-72dfdf22c79d4609"></a>

??? note "소스 근거: Documentation/introduction.rst:153"
    `Documentation/introduction.rst:153`에서 시작하는 발췌입니다. 종료 줄은 161이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `684ccb39cfc9bebf3125bd79b4b2f847de806a34261a9bcac9216bda52f1f99d`
    
    ```text
    * The libcamera adaptation is an umbrella term designating the
      components that interface to libcamera in other frameworks.
      Notable examples are a V4L2 compatibility layer, a gstreamer
      libcamera element, and an Android camera HAL implementation based
      on libcamera.
    
      Those components can live in the libcamera project source code
      in separate repositories, or move to their respective project's
      repository (for instance the gstreamer libcamera element).
    ```

<a id="source-9e653b8ff755db78"></a>

??? note "소스 근거: Documentation/introduction.rst:163"
    `Documentation/introduction.rst:163`에서 시작하는 발췌입니다. 종료 줄은 165이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `e8a1fc73a04b4feadbf1c6ca5d820f482b4eaaebfafec27a74612e2189b01c7c`
    
    ```text
    * The applications and upper level frameworks are based on the
      libcamera framework or libcamera adaptation, and are outside of
      the scope of the libcamera project.
    ```

<a id="source-8bd888bd0473995e"></a>

??? note "소스 근거: Documentation/libcamera_architecture.rst:87"
    `Documentation/libcamera_architecture.rst:87`에서 시작하는 발췌입니다. 종료 줄은 102이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `868d392c7f94391d196168c05db330a1f07da72687d94f7b5a6ffaf1d6dee988`
    
    ```text
    The Pipeline Handler manages the complex pipelines exposed by the kernel
      drivers through the Media Controller and V4L2 APIs. It abstracts pipeline
      handling to hide device-specific details from the rest of the library, and
      implements both pipeline configuration based on stream configuration, and
      pipeline runtime execution and scheduling when needed by the device.
    
      The Pipeline Handler lives in the same process as the rest of the library, and
      has access to all helpers and kernel camera-related devices.
    
      Hardware abstraction is handled by device specific Pipeline Handlers which are
      derived from the Pipeline Handler base class allowing commonality to be shared
      among the implementations.
    
      Derived pipeline handlers create Camera device instances based on the devices
      they detect and support on the running system, and are responsible for
      managing the interactions with a camera device.
    ```

<a id="source-1f130cc8640ef810"></a>

??? note "소스 근거: Documentation/libcamera_architecture.rst:109"
    `Documentation/libcamera_architecture.rst:109`에서 시작하는 발췌입니다. 종료 줄은 118이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `f0858f8576140aaf8b57ac5d757e8be0910218fb68d85b4704fe9275e2683a28`
    
    ```text
    Together with the hardware image processing and hardware statistics
      collection, the Image Processing Algorithms (IPA) implement 3A (Auto-Exposure,
      Auto-White Balance and Auto-Focus) and other algorithms. They run on the CPU
      and control hardware image processing based on the parameters supplied by
      upper layers, closing the control loop of the ISP.
    
      IPAs are loaded as external plugins named IPA Modules. IPA Modules can be
      part of the libcamera code base or provided externally by camera vendors.
      In-tree IPA modules are covered by the same license as the rest of libcamera,
      external IPA modules can be open-source or closed-source.
    ```

<a id="source-341442e08591ef50"></a>

??? note "소스 근거: Documentation/introduction.rst:200"
    `Documentation/introduction.rst:200`에서 시작하는 발췌입니다. 종료 줄은 204이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `ef0482e955d8c625e622517f8a1bd58e9fcc321770a02c19aa241cdc485bb623`
    
    ```text
    Handlers are a part of the libcamera code base and need to be contributed
    upstream by device vendors. IPA modules included in libcamera are covered by a
    free software license, however third-parties may develop IPA modules outside of
    libcamera and distribute them under a closed-source license, provided they do
    not include source code from the libcamera project.
    ```

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `Documentation/introduction.rst`, `Documentation/libcamera_architecture.rst`, `include/libcamera/camera.h`, `include/libcamera/camera_manager.h`, `include/libcamera/internal/pipeline_handler.h`, `src/libcamera/camera.cpp`, `src/libcamera/camera_manager.cpp`, `src/libcamera/pipeline_handler.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `2c4b67c079`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-27 · 사람 검토 전

다음 단계: [시스템 개요](overview.md)
