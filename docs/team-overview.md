---
generated_at: 2026-11-11 20:35:47+00:00
source_commit: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
status: ok
section: team-overview
generation_method: facts-and-llm
evidence_fingerprint: 7810357af92fe198def6a3c92e05c9264cd371403de5a33c806c0115178519bd
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design:
  schema: 1
  input_fingerprint: 7810357af92fe198def6a3c92e05c9264cd371403de5a33c806c0115178519bd
  answers:
    role:
    - text: libcamera는 Linux, Android, ChromeOS를 위한 오픈 소스 복합 카메라 지원 라이브러리입니다. Linux
        커널 장치 드라이버와 연결하고 개발자에게 직관적인 API를 제공하여 Linux 시스템에서 복합 카메라로 이미지를 캡처하는 과정의 복잡성을
        줄입니다.
      evidence:
      - what
      covers:
      - role
      kind: behavior
      quote: 'libcamera is an open source complex camera support library for Linux,
        Android

        and ChromeOS. The library interfaces with Linux kernel device drivers and

        provides an intuitive API to developers in order to simplify the complexity

        involved in capturing images from complex cameras on Linux systems.'
      part_id: what
    - text: 드라이버를 사용하여 동작하는 카메라 스택을 제공할 책임은 사용자 공간에 있으며, 벤더가 보통 이를 각각 구현합니다. 이러한 구현에는
        응용 프로그램 개발자를 위한 공통 아키텍처나 API가 없으며, 하드웨어 파이프라인과 커널 API에서의 표현 방식이 서로 다르기 때문에
        맞춤 처리가 필요한 경우가 많습니다.
      evidence:
      - problem
      covers:
      - role
      kind: behavior
      quote: 'The usage of these drivers to provide a functioning camera stack is
        a

        responsibility that lies in userspace, and is commonly implemented separately

        by vendors without a common architecture or API for application developers.
        This

        adds a lot of complexity to the task, particularly when considering that the

        differences in hardware pipelines and their representation in the kernel''s
        APIs

        often necessitate bespoke handling.'
      part_id: problem
    - text: libcamera는 Linux 기반 시스템에 카메라 스택을 제공하여, 카메라에서 원하는 결과를 얻는 데 필요한 하드웨어 설정과
        이미지 제어 알고리즘을 커널 API를 통해 처리하는 작업을 추상화합니다. 이를 통해 개발자는 해당 작업을 간단하고 일관된 방식으로 수행할
        수 있습니다.
      evidence:
      - for
      covers:
      - role
      kind: behavior
      quote: 'libcamera provides a complete camera stack for Linux-based systems to
        abstract

        the configuration of hardware and image control algorithms required to obtain

        desirable results from the camera through the kernel''s APIs, reducing those

        operations to a simple and consistent method for developers. In short instead
        of

        having to deal with this:'
      part_id: easier
    - text: 카메라 스택은 아래에서 위로 커널 드라이버, libcamera 프레임워크, libcamera 적응 계층, 애플리케이션·상위 프레임워크의
        네 계층으로 구성됩니다.
      evidence:
      - stack
      covers:
      - role
      kind: behavior
      quote: "The camera stack comprises four software layers. From bottom to top:\n\
        \n* The kernel drivers control the camera hardware and expose a\n  low-level\
        \ interface to userspace through the Linux kernel V4L2\n  family of APIs (Media\
        \ Controller API, V4L2 Video Device API and\n  V4L2 Subdev API).\n\n* The\
        \ libcamera framework is the core part of the stack. It\n  handles all control\
        \ of the camera devices in its core component,\n  libcamera, and exposes a\
        \ native C++ API to upper layers. Optional\n  language bindings allow interfacing\
        \ to libcamera from other\n  programming languages.\n\n  Those components\
        \ live in the same source code repository and\n  all together constitute the\
        \ libcamera framework.\n\n* The libcamera adaptation is an umbrella term designating\
        \ the\n  components that interface to libcamera in other frameworks.\n  Notable\
        \ examples are a V4L2 compatibility layer, a gstreamer\n  libcamera element,\
        \ and an Android camera HAL implementation based\n  on libcamera.\n\n  Those\
        \ components can live in the libcamera project source code\n  in separate\
        \ repositories, or move to their respective project's\n  repository (for instance\
        \ the gstreamer libcamera element).\n\n* The applications and upper level\
        \ frameworks are based on the\n  libcamera framework or libcamera adaptation,\
        \ and are outside of\n  the scope of the libcamera project."
      part_id: layers
    outputs:
    - text: libcamera는 애플리케이션 등 상위 계층이 카메라 장치를 제어할 수 있도록 네이티브 C++ API를 제공합니다. 선택적인
        언어 바인딩을 사용하면 다른 프로그래밍 언어에서도 libcamera와 연결할 수 있습니다.
      evidence:
      - framework
      - camera
      covers:
      - outputs
      kind: behavior
      quote: "* The libcamera framework is the core part of the stack. It\n  handles\
        \ all control of the camera devices in its core component,\n  libcamera, and\
        \ exposes a native C++ API to upper layers. Optional\n  language bindings\
        \ allow interfacing to libcamera from other\n  programming languages.\n\n\
        \  Those components live in the same source code repository and\n  all together\
        \ constitute the libcamera framework."
      part_id: api
    - text: libcamera adaptation은 다른 프레임워크의 구성 요소 중 libcamera와 연결되는 구성 요소를 통칭합니다.
        예로는 V4L2 호환 계층, gstreamer의 libcamera 요소, libcamera를 기반으로 구현한 Android 카메라 HAL(하드웨어와
        소프트웨어를 연결하는 계층)이 있습니다. 이러한 구성 요소는 libcamera 프로젝트 소스 코드의 별도 저장소에 있거나 각 프로젝트의
        저장소로 옮겨질 수 있습니다. 구체적인 입출력과 협업 책임은 확인되지 않습니다.
      evidence:
      - adaptation
      covers:
      - outputs
      kind: behavior
      quote: "* The libcamera adaptation is an umbrella term designating the\n  components\
        \ that interface to libcamera in other frameworks.\n  Notable examples are\
        \ a V4L2 compatibility layer, a gstreamer\n  libcamera element, and an Android\
        \ camera HAL implementation based\n  on libcamera.\n\n  Those components can\
        \ live in the libcamera project source code\n  in separate repositories, or\
        \ move to their respective project's\n  repository (for instance the gstreamer\
        \ libcamera element)."
      part_id: adapters
    boundaries:
    - text: libcamera 프레임워크(소프트웨어 개발의 기반 구조) 또는 libcamera를 맞춰 적용한 것을 기반으로 하는 애플리케이션(응용
        프로그램)과 상위 수준 프레임워크는 libcamera 프로젝트의 범위 밖에 있습니다.
      evidence:
      - apps
      covers:
      - boundaries
      kind: behavior
      quote: "* The applications and upper level frameworks are based on the\n  libcamera\
        \ framework or libcamera adaptation, and are outside of\n  the scope of the\
        \ libcamera project."
      part_id: outside
    - text: Pipeline Handler(파이프라인 처리기)는 장치별 파이프라인을 관리하며, 장치 제조사는 이를 libcamera에 기여해야
        합니다. 이미지 처리 알고리즘(`Image` Processing Algorithms, IPA)은 상위 계층의 매개변수를 바탕으로 하드웨어
        이미지 처리를 제어하며, IPA `Module`(IPA 모듈)은 외부에서 별도로 제공할 수 있습니다. libcamera에 포함된 IPA
        `Module`에는 자유 소프트웨어 라이선스가 적용되며, 외부 모듈은 libcamera 프로젝트의 소스 코드를 포함하지 않는 조건으로
        비공개 소스 라이선스로 배포할 수 있습니다. IPA `Module`은 libcamera와 Pipeline Handler가 제공하는 API(응용
        프로그램 인터페이스)로만 상호작용하며 kernel camera devices(커널 카메라 장치)에 직접 접근할 수 없습니다.
      evidence:
      - handler
      - ipa
      - licensing
      - ipa-access
      covers:
      - boundaries
      kind: behavior
      quote: 'Handlers are a part of the libcamera code base and need to be contributed

        upstream by device vendors. IPA modules included in libcamera are covered
        by a

        free software license, however third-parties may develop IPA modules outside
        of

        libcamera and distribute them under a closed-source license, provided they
        do

        not include source code from the libcamera project.'
      part_id: vendors-module-access
    inputs:
    - text: 커널 드라이버는 카메라 하드웨어를 제어하는 구성 요소로, Linux 영상 장치용 API인 V4L2를 비롯한 API를 통해 사용자
        공간에 하위 수준의 접점을 제공합니다. API는 프로그램이 장치 기능을 요청하는 접점입니다. libcamera의 Pipeline Handler는
        이 접점으로 노출된 파이프라인을 관리하고, 스트림 설정을 바탕으로 파이프라인을 구성하며 장치에 필요한 경우 실행과 일정을 관리합니다.
        장치별 Pipeline Handler는 감지하고 지원하는 장치를 바탕으로 `Camera` 인스턴스를 만들고 카메라 장치와의 상호작용을
        관리합니다.
      evidence:
      - kernel
      - kernel-handler
      covers:
      - inputs
      kind: behavior
      quote: "The Pipeline Handler manages the complex pipelines exposed by the kernel\n\
        \  drivers through the Media Controller and V4L2 APIs. It abstracts pipeline\n\
        \  handling to hide device-specific details from the rest of the library,\
        \ and\n  implements both pipeline configuration based on stream configuration,\
        \ and\n  pipeline runtime execution and scheduling when needed by the device.\n\
        \n  The Pipeline Handler lives in the same process as the rest of the library,\
        \ and\n  has access to all helpers and kernel camera-related devices.\n\n\
        \  Hardware abstraction is handled by device specific Pipeline Handlers which\
        \ are\n  derived from the Pipeline Handler base class allowing commonality\
        \ to be shared\n  among the implementations.\n\n  Derived pipeline handlers\
        \ create Camera device instances based on the devices\n  they detect and support\
        \ on the running system, and are responsible for\n  managing the interactions\
        \ with a camera device."
      part_id: below
    - text: '`Camera` Manager(카메라 관리자)는 카메라를 찾아 목록화하고, libcamera가 지원하는 각 카메라를 관리할
        Pipeline Handler(카메라 처리 관리자)를 생성합니다. 각 애플리케이션에는 `Camera` Manager가 하나만 실행되며,
        한 번에 하나의 애플리케이션만 카메라 장치의 제어권을 가질 수 있도록 합니다.'
      evidence:
      - manager
      covers:
      - inputs
      kind: behavior
      quote: "The Camera Manager enumerates cameras and instantiates Pipeline Handlers\
        \ to\n  manage each Camera that libcamera supports. The Camera Manager supports\n\
        \  hotplug detection and notification events when supported by the underlying\n\
        \  kernel devices.\n\n  There is only ever one instance of the Camera Manager\
        \ running per application.\n  Each application's instance of the Camera Manager\
        \ ensures that only a single\n  application can take control of a camera device\
        \ at once."
      part_id: discover
  topic_inputs:
    role: 639c2df3bdf51187da58ba647737087c9571936f6a9f3c145c0dd1a4ebbcb4c9
    inputs: 9a36db16ee222bc38e4e80240959bbb7bdd88ad04f2eaf8622f9f168b73ef8f7
    outputs: 4be21aaaac0ce21dbdec835b6e31e0c3d38449f2ac4183a4a92508aeb00ccc2f
    boundaries: a63ba455136377c609c365c0ddb8312bb9d854d498ed7bb3ef364d6c5a907bcb
  reused_topics:
  - role
  - outputs
  - boundaries
  replayed_units: []
  generated_topics:
  - inputs
  topic_agents:
    role: cli/codex/gpt-6.1-terra
    outputs: cli/codex/gpt-6.1-terra
    boundaries: cli/codex/gpt-6.1-terra
    inputs: cli/codex/gpt-6.1-terra
  grounding_review: passed
  grounding_policy: 3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2
  reader_scope:
    revision: 2
    change_reason: 공개 예제의 대상을 libcamera로 명시하여 사내 HAL의 미확인 사항을 본문에 덧붙이지 않게 합니다.
    tasks:
    - id: collaboration
      goal: 타팀이 libcamera의 역할·입출력·인터페이스와 협업 책임을 구분합니다.
      completion: 역할·입출력·책임 경계에 답하는 절과 근거에 도달합니다.
      requirements:
      - role
      - inputs
      - outputs
      - boundaries
    optional:
    - id: implementation-detail
      location: scenarios/index.md
      reason: 내부 상세는 과업에 필요한 조건과 예외를 유지한 채 연결해서 읽습니다.
    excluded:
    - id: all-features
      reason: 전체 기능·모든 하드웨어 조합의 참조서는 이 개요의 목적이 아닙니다.
    removed_requirements: []
  validation_policy:
    manuscript: 367d18b95f8f0d01a15ae0f4d1b70f7e13e4d0298df4215e2c449ac4905db6f9
    semantic: 571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968
    duplicates: 93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38
    design_contracts: 9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0
    validate: 78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372
    reader_profiles: ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797
    contract_schema: d0f7ab4c48fcf52409935931eb9b93aacd48af4b19e9bb816fa496f1214fdb2f
    answer_contracts: a39c9a8818afc47e059141d486337c0f12a7fd34319e2b6f7674fc428bc83e2b
    reader_scope: 1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782
    product_context: 050c20aa2fdcceae10c6275fbb5f850f616ab5051bb67ccbcb4a204877a238d9
    explanation: 69bcaa207ef39d20f6a47ac201c3edf119f59b333e85131dea1bce85eef4006b
    design_response: a7c199bc52bcc0e749ef01186e50bca98107473d5c82e2248712f465d02e1e69
    design_validation: 92ddb9a65c909173ff4c7cb627dff83e71c10c8258c51344ef0eb1a7a023937f
  validation_model: d06f781e3773ea582e2dd019cbb6ae2e683edc981a216ae871b595905ff3332b
  style_policy:
    fluent-korean.md: ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975
    i-have-adhd.md: 3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9
    README.md: b87a84b1bc31079837dc4dc4527ce02c9dc2cbc3a26ff7e99e0872941d213995
  reuse_lineage:
    source_commit: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
    body_sha256: e7c6552bb295b99f968f09557f53be1e21270f8e2b42c8d4e30d892352e09f82
    topics:
    - role
    - outputs
    - boundaries
    validation: current source, contract and editorial checks; human review pending
  checkpoint_units:
  - checkpoint: 6621f88cbc6185115f16da4eef0978b4a24d144487224c5c4d4bee914bc8d348.json
    topic: inputs
    part: discover
    subpart: null
    revalidated: true
    new_grounding_review: false
    receipts:
    - 061a614cf8034169814f8db6d9cf0bdc/011.receipt.json
    - 061a614cf8034169814f8db6d9cf0bdc/012.receipt.json
  body_sha256: f0ecd9691a7f02f2aa6a5dc1b028388b391b284e6f0901c19e7d8b226467a978
managed_visual_refresh:
- schema: 1
  source_commit: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
  original_manuscript_sha256: 2c845ca920262743a504d13f588fb01165d16ace5622624450acaddcffecac73
  previous_body_sha256: d63e37265098edf2a1088252dca5b2514aa91fa2bbd628691e783870107c2ed3
  body_sha256: f0ecd9691a7f02f2aa6a5dc1b028388b391b284e6f0901c19e7d8b226467a978
  visual_definitions_sha256: 8a41a2f9830606d4f58b0b38a373e8c758c9b8766794a5e7d650b14ee41e26fc
  unchanged_native_records_sha256: 44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a
  preserved_outside_body_sha256: b976e0b0b5007d2369d8cfceb78156060a10d7e63816e86118b5c5b80193612d
  owned_edit_regions:
  - original_start_byte: 1929
    original_end_byte: 5056
    original_sha256: 3199a3985cfae7b7fbdc3e0bd87c92020e477090f8628a1dd9734ec17e5de8d8
    replacement_sha256: 3199a3985cfae7b7fbdc3e0bd87c92020e477090f8628a1dd9734ec17e5de8d8
    visual_ids:
    - camera-stack
  - original_start_byte: 6726
    original_end_byte: 14702
    original_sha256: 14d417dd3362ae921114b9e956b990b042a65bfe5f174c067f285658d96b49ca
    replacement_sha256: 14d417dd3362ae921114b9e956b990b042a65bfe5f174c067f285658d96b49ca
    visual_ids:
    - item-inputs
  - original_start_byte: 15722
    original_end_byte: 15722
    original_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    replacement_sha256: 47b7583e4513dc28778106f55ad98c0885fed54efd97637856dbd898027eb7dc
    visual_ids:
    - interfaces-to-upper-layers
  - original_start_byte: 16865
    original_end_byte: 28691
    original_sha256: beb7f0dde624c10f1b5275da4f6d6be0c7b628a6cc89fadc9dc0ea20e129d00c
    replacement_sha256: beb7f0dde624c10f1b5275da4f6d6be0c7b628a6cc89fadc9dc0ea20e129d00c
    visual_ids:
    - item-boundaries
  added_visuals:
  - interfaces-to-upper-layers
  scope: Configured figure reassembly only; figure authorship remains per visual
  new_inference: false
  semantic_approval: false
  human_review: unchanged
---

# 이 프로젝트가 하는 일

**이 프로젝트가 무엇을 받아 무엇을 내놓는지, 어느 계층·팀과 맞닿아 있는지 짧게 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| libcamera는 Linux, Android, ChromeOS를 위한 오픈 소스 복합 카메라 지원 라이브러리입니다. | [하는 일](#하는-일) |
| 커널 드라이버는 카메라 하드웨어를 제어하는 구성 요소로, Linux 영상 장치용 API인 V4L2를 비롯한 API를 통해 사용자 공간에 하위 수준의 접점을 제공합니다. | [받는 것](#받는-것) |
| libcamera는 애플리케이션 등 상위 계층이 카메라 장치를 제어할 수 있도록 네이티브 C++ API를 제공합니다. | [내놓는 것](#내놓는-것) |
| libcamera 프레임워크(소프트웨어 개발의 기반 구조) 또는 libcamera를 맞춰 적용한 것을 기반으로 하는 애플리케이션(응용 프로그램)과 상위 수준 프레임워크는 libcamera 프로젝트의 범위 밖에 있습니다. | [다른 팀·계층과의 경계](#다른-팀계층과의-경계) |

## 하는 일

libcamera는 Linux, Android, ChromeOS를 위한 오픈 소스 복합 카메라 지원 라이브러리입니다. Linux 커널 장치 드라이버와 연결하고 개발자에게 직관적인 API를 제공하여 Linux 시스템에서 복합 카메라로 이미지를 캡처하는 과정의 복잡성을 줄입니다. 드라이버를 사용하여 동작하는 카메라 스택을 제공할 책임은 사용자 공간에 있으며, 벤더가 보통 이를 각각 구현합니다. 이러한 구현에는 응용 프로그램 개발자를 위한 공통 아키텍처나 API가 없으며, 하드웨어 파이프라인과 커널 API에서의 표현 방식이 서로 다르기 때문에 맞춤 처리가 필요한 경우가 많습니다. `Documentation/introduction.rst:10`, `Documentation/introduction.rst:35`

<!-- sdd:visual:camera-stack -->
### 카메라 스택의 네 계층

```mermaid
flowchart TB
%% sdd:translations {"C++ API로 직접 사용": "Use the C++ API directly", "V4L2 계열 API로 제어": "Control through the V4L2 <br/>family of APIs", "libcamera 프레임워크": "libcamera framework", "libcamera에 연결": "Connect to libcamera", "다른 프레임워크를 거쳐 사용": "Use through another <br/>framework", "애플리케이션·상위 프레임워크": "Applications and <br/>upper-level frameworks", "어댑테이션 #40;V4L2 <br/>호환·GStreamer·Android HAL#41;": "Adaptation #40;V4L2 <br/>compatibility, GStreamer, <br/>Android HAL#41;", "커널 드라이버 #40;V4L2 계열 <br/>API#41;": "Kernel drivers #40;V4L2 family <br/>of APIs#41;"}
  v_apps["애플리케이션·상위 프레임워크"]
  v_adaptation["어댑테이션 #40;V4L2 <br/>호환·GStreamer·Android HAL#41;"]
  v_framework["libcamera 프레임워크"]
  v_kernel["커널 드라이버 #40;V4L2 계열 <br/>API#41;"]
  v_apps -->|"C++ API로 직접 사용"| v_framework
  v_apps -->|"다른 프레임워크를 거쳐 사용"| v_adaptation
  v_adaptation -->|"libcamera에 연결"| v_framework
  v_framework -->|"V4L2 계열 API로 제어"| v_kernel
```

[Mermaid 원문](team-overview.camera-stack.mmd)

??? note "그림 근거와 확인 범위"
    애플리케이션에서 카메라 하드웨어까지 어떤 계층을 지납니까? 지원 기종이나 성능을 보장하는 그림은 아닙니다.
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Applications and upper-level frameworks">애플리케이션·상위 프레임워크</span> | [Documentation/introduction.rst:137](#source-e3b563f549a8c46d) |
    | <span data-sdd-label-en="Adaptation (V4L2 compatibility, GStreamer, Android HAL)">어댑테이션 &#40;V4L2 호환·GStreamer·Android HAL&#41;</span> | [Documentation/introduction.rst:137](#source-e3b563f549a8c46d) |
    | <span data-sdd-label-en="libcamera framework">libcamera 프레임워크</span> | [Documentation/introduction.rst:137](#source-e3b563f549a8c46d) |
    | <span data-sdd-label-en="Kernel drivers (V4L2 family of APIs)">커널 드라이버 &#40;V4L2 계열 API&#41;</span> | [Documentation/introduction.rst:137](#source-e3b563f549a8c46d) |
    | <span data-sdd-label-en="Use the C++ API directly">C++ API로 직접 사용</span> | [Documentation/introduction.rst:137](#source-e3b563f549a8c46d) |
    | <span data-sdd-label-en="Use through another framework">다른 프레임워크를 거쳐 사용</span> | [Documentation/introduction.rst:137](#source-e3b563f549a8c46d) |
    | <span data-sdd-label-en="Connect to libcamera">libcamera에 연결</span> | [Documentation/introduction.rst:137](#source-e3b563f549a8c46d) |
    | <span data-sdd-label-en="Control through the V4L2 family of APIs">V4L2 계열 API로 제어</span> | [Documentation/introduction.rst:137](#source-e3b563f549a8c46d) |
<!-- /sdd:visual:camera-stack -->

libcamera는 Linux 기반 시스템에 카메라 스택을 제공하여, 카메라에서 원하는 결과를 얻는 데 필요한 하드웨어 설정과 이미지 제어 알고리즘을 커널 API를 통해 처리하는 작업을 추상화합니다. 이를 통해 개발자는 해당 작업을 간단하고 일관된 방식으로 수행할 수 있습니다. 카메라 스택은 아래에서 위로 커널 드라이버, libcamera 프레임워크, libcamera 적응 계층, 애플리케이션·상위 프레임워크의 네 계층으로 구성됩니다. `Documentation/introduction.rst:45`, `Documentation/introduction.rst:137`

근거 원문: [Documentation/introduction.rst:10](#source-34fda84500757231) · [Documentation/introduction.rst:35](#source-de476c940b030e4a) · [Documentation/introduction.rst:45](#source-f350cabac0db8343) · [Documentation/introduction.rst:137](#source-e3b563f549a8c46d)

## 받는 것

커널 드라이버는 카메라 하드웨어를 제어하는 구성 요소로, Linux 영상 장치용 API인 V4L2를 비롯한 API를 통해 사용자 공간에 하위 수준의 접점을 제공합니다. API는 프로그램이 장치 기능을 요청하는 접점입니다. libcamera의 Pipeline Handler는 이 접점으로 노출된 파이프라인을 관리하고, 스트림 설정을 바탕으로 파이프라인을 구성하며 장치에 필요한 경우 실행과 일정을 관리합니다. 장치별 Pipeline Handler는 감지하고 지원하는 장치를 바탕으로 `Camera` 인스턴스를 만들고 카메라 장치와의 상호작용을 관리합니다. `Documentation/introduction.rst:139`, `Documentation/libcamera_architecture.rst:87`

<!-- sdd:visual:item-inputs -->
### 커널 입력과 카메라 제어 책임

```mermaid
flowchart TB
%% sdd:translations {"Camera Manager가 Pipeline <br/>Handlers를 생성합니다.": "Camera Manager instantiates <br/>Pipeline Handlers.", "Camera Manager는 카메라를 <br/>열거하고 Pipeline <br/>Handlers를 생성합니다.": "Camera Manager enumerates <br/>cameras and instantiates <br/>Pipeline Handlers.", "Linux kernel의 drivers가 <br/>카메라 하드웨어를 <br/>제어합니다.": "Linux kernel drivers <br/>control the camera hardware.", "Pipeline Handlers는 <br/>libcamera가 지원하는 각 <br/>Camera를 관리합니다.": "Pipeline Handlers manage <br/>each Camera that libcamera <br/>supports.", "Pipeline Handler는 커널이 <br/>Media Controller와 V4L2로 <br/>노출한 파이프라인을 <br/>관리합니다.": "Pipeline Handler manages <br/>the pipelines exposed <br/>through Media Controller <br/>and V4L2.", "interface는 Linux 커널 V4L2 <br/>API 계열을 통해 userspace에 <br/>노출됩니다.": "The interface is exposed to <br/>userspace through Linux <br/>V4L2 APIs.", "kernel drivers가 저수준 <br/>interface를 노출합니다.": "Kernel drivers expose the <br/>low-level interface.", "userspace에는 저수준 <br/>interface가 노출됩니다.": "The low-level interface is <br/>exposed to userspace.", "각 application에서는 Camera <br/>Manager 인스턴스가 하나만 <br/>실행됩니다.": "Only one Camera Manager <br/>instance runs per <br/>application.", "각 application의 Camera <br/>Manager는 한 번에 하나의 <br/>application만 camera <br/>device를 제어할 수 있게 <br/>보장합니다.": "Camera Manager ensures only <br/>one application controls a <br/>device at once.", "기반 kernel 기기가 지원하면 <br/>Camera Manager도 핫플러그 <br/>감지와 알림 이벤트를 <br/>지원합니다.": "Camera Manager supports <br/>hotplug events when kernel <br/>devices do.", "저수준 interface는 Linux <br/>커널의 V4L2 API 계열을 <br/>사용합니다.": "The low-level interface <br/>uses the Linux kernel V4L2 <br/>family of APIs.", "한 번에 하나의 <br/>application만 camera <br/>device를 제어할 수 있습니다.": "Only one application can <br/>control a camera device at <br/>once."}
  v_kernel["Linux kernel의 drivers가 <br/>카메라 하드웨어를 <br/>제어합니다."]
  v_interface["저수준 interface는 Linux <br/>커널의 V4L2 API 계열을 <br/>사용합니다."]
  v_userspace["userspace에는 저수준 <br/>interface가 노출됩니다."]
  v_manager["Camera Manager는 카메라를 <br/>열거하고 Pipeline <br/>Handlers를 생성합니다."]
  v_handlers["Pipeline Handlers는 <br/>libcamera가 지원하는 각 <br/>Camera를 관리합니다."]
  v_application["각 application에서는 Camera <br/>Manager 인스턴스가 하나만 <br/>실행됩니다."]
  v_device["한 번에 하나의 <br/>application만 camera <br/>device를 제어할 수 있습니다."]
  v_kernel -->|"kernel drivers가 저수준 <br/>interface를 노출합니다."| v_interface
  v_interface -->|"interface는 Linux 커널 V4L2 <br/>API 계열을 통해 userspace에 <br/>노출됩니다."| v_userspace
  v_manager -->|"기반 kernel 기기가 지원하면 <br/>Camera Manager도 핫플러그 <br/>감지와 알림 이벤트를 <br/>지원합니다."| v_kernel
  v_manager -->|"Camera Manager가 Pipeline <br/>Handlers를 생성합니다."| v_handlers
  v_application -->|"각 application에서는 Camera <br/>Manager 인스턴스가 하나만 <br/>실행됩니다."| v_manager
  v_manager -->|"각 application의 Camera <br/>Manager는 한 번에 하나의 <br/>application만 camera <br/>device를 제어할 수 있게 <br/>보장합니다."| v_device
  v_userspace -->|"Pipeline Handler는 커널이 <br/>Media Controller와 V4L2로 <br/>노출한 파이프라인을 <br/>관리합니다."| v_handlers
```

[Mermaid 원문](team-overview.item-inputs.mmd)

??? note "그림 근거와 확인 범위"
    커널 인터페이스, Camera Manager, Pipeline Handler와 애플리케이션은 어떻게 관계를 맺으며 한 번에 누가 카메라를 제어할 수 있습니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Linux kernel drivers control the camera hardware.">Linux kernel의 drivers가 카메라 하드웨어를 제어합니다.</span> | [Documentation/introduction.rst:139](#source-e93209ecbe248c51) |
    | <span data-sdd-label-en="The low-level interface uses the Linux kernel V4L2 family of APIs.">저수준 interface는 Linux 커널의 V4L2 API 계열을 사용합니다.</span> | [Documentation/introduction.rst:139](#source-e93209ecbe248c51) |
    | <span data-sdd-label-en="The low-level interface is exposed to userspace.">userspace에는 저수준 interface가 노출됩니다.</span> | [Documentation/introduction.rst:139](#source-e93209ecbe248c51) |
    | <span data-sdd-label-en="Camera Manager enumerates cameras and instantiates Pipeline Handlers.">Camera Manager는 카메라를 열거하고 Pipeline Handlers를 생성합니다.</span> | [Documentation/libcamera_architecture.rst:60](#source-64bdc114ca74bd2c) |
    | <span data-sdd-label-en="Pipeline Handlers manage each Camera that libcamera supports.">Pipeline Handlers는 libcamera가 지원하는 각 Camera를 관리합니다.</span> | [Documentation/libcamera_architecture.rst:60](#source-64bdc114ca74bd2c) |
    | <span data-sdd-label-en="Only one Camera Manager instance runs per application.">각 application에서는 Camera Manager 인스턴스가 하나만 실행됩니다.</span> | [Documentation/libcamera_architecture.rst:60](#source-64bdc114ca74bd2c) |
    | <span data-sdd-label-en="Only one application can control a camera device at once.">한 번에 하나의 application만 camera device를 제어할 수 있습니다.</span> | [Documentation/libcamera_architecture.rst:60](#source-64bdc114ca74bd2c) |
    | <span data-sdd-label-en="Kernel drivers expose the low-level interface.">kernel drivers가 저수준 interface를 노출합니다.</span> | [Documentation/introduction.rst:139](#source-e93209ecbe248c51) |
    | <span data-sdd-label-en="The interface is exposed to userspace through Linux V4L2 APIs.">interface는 Linux 커널 V4L2 API 계열을 통해 userspace에 노출됩니다.</span> | [Documentation/introduction.rst:139](#source-e93209ecbe248c51) |
    | <span data-sdd-label-en="Camera Manager supports hotplug events when kernel devices do.">기반 kernel 기기가 지원하면 Camera Manager도 핫플러그 감지와 알림 이벤트를 지원합니다.</span> | [Documentation/libcamera_architecture.rst:60](#source-64bdc114ca74bd2c) |
    | <span data-sdd-label-en="Camera Manager instantiates Pipeline Handlers.">Camera Manager가 Pipeline Handlers를 생성합니다.</span> | [Documentation/libcamera_architecture.rst:60](#source-64bdc114ca74bd2c) |
    | <span data-sdd-label-en="Only one Camera Manager instance runs per application.">각 application에서는 Camera Manager 인스턴스가 하나만 실행됩니다.</span> | [Documentation/libcamera_architecture.rst:60](#source-64bdc114ca74bd2c) |
    | <span data-sdd-label-en="Camera Manager ensures only one application controls a device at once.">각 application의 Camera Manager는 한 번에 하나의 application만 camera device를 제어할 수 있게 보장합니다.</span> | [Documentation/libcamera_architecture.rst:60](#source-64bdc114ca74bd2c) |
    | <span data-sdd-label-en="Pipeline Handler manages the pipelines exposed through Media Controller and V4L2.">Pipeline Handler는 커널이 Media Controller와 V4L2로 노출한 파이프라인을 관리합니다.</span> | [Documentation/libcamera_architecture.rst:87](#source-8bd888bd0473995e) |
<!-- /sdd:visual:item-inputs -->

`Camera` Manager(카메라 관리자)는 카메라를 찾아 목록화하고, libcamera가 지원하는 각 카메라를 관리할 Pipeline Handler(카메라 처리 관리자)를 생성합니다. 각 애플리케이션에는 `Camera` Manager가 하나만 실행되며, 한 번에 하나의 애플리케이션만 카메라 장치의 제어권을 가질 수 있도록 합니다. `Documentation/libcamera_architecture.rst:60`

근거 원문: [Documentation/introduction.rst:139](#source-e93209ecbe248c51) · [Documentation/libcamera_architecture.rst:87](#source-8bd888bd0473995e) · [Documentation/libcamera_architecture.rst:60](#source-64bdc114ca74bd2c)

## 내놓는 것

libcamera는 애플리케이션 등 상위 계층이 카메라 장치를 제어할 수 있도록 네이티브 C++ API를 제공합니다. 선택적인 언어 바인딩을 사용하면 다른 프로그래밍 언어에서도 libcamera와 연결할 수 있습니다. `Documentation/introduction.rst:144`, `Documentation/libcamera_architecture.rst:72`

<!-- sdd:visual:interfaces-to-upper-layers -->
### 상위 계층이 libcamera에 연결하는 인터페이스

```mermaid
flowchart TB
%% sdd:translations {"V4L2 호환 계층, GStreamer <br/>요소, Android 카메라 HAL이 <br/>예입니다.": "Examples include a V4L2 <br/>layer, a GStreamer element, <br/>and an Android camera HAL.", "libcamera 코어가 카메라 <br/>장치를 제어합니다.": "The libcamera core controls <br/>camera devices.", "libcamera에 연결": "Connects to libcamera", "네이티브 C++ API": "Native C++ API", "다른 언어는 선택적 언어 <br/>바인딩을 사용할 수 있습니다.": "Other languages can use <br/>optional bindings.", "상위 계층은 네이티브 C++ <br/>API를 사용합니다.": "Upper layers use the native <br/>C++ API.", "선택적 바인딩": "Optional bindings", "연결 구성 요소 예": "Integration examples", "외부 프레임워크는 연결 구성 <br/>요소를 사용합니다.": "Other frameworks use <br/>integration components."}
  v_upper["상위 계층은 네이티브 C++ <br/>API를 사용합니다."]
  v_other_language["다른 언어는 선택적 언어 <br/>바인딩을 사용할 수 있습니다."]
  v_adaptation["외부 프레임워크는 연결 구성 <br/>요소를 사용합니다."]
  v_examples["V4L2 호환 계층, GStreamer <br/>요소, Android 카메라 HAL이 <br/>예입니다."]
  v_core["libcamera 코어가 카메라 <br/>장치를 제어합니다."]
  v_upper -->|"네이티브 C++ API"| v_core
  v_other_language -->|"선택적 바인딩"| v_core
  v_adaptation -->|"libcamera에 연결"| v_core
  v_adaptation -->|"연결 구성 요소 예"| v_examples
```

[Mermaid 원문](team-overview.interfaces-to-upper-layers.mmd)

??? note "그림 근거와 확인 범위"
    네이티브 API, 언어 바인딩과 외부 프레임워크의 adaptation은 어떻게 연결됩니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Upper layers use the native C++ API.">상위 계층은 네이티브 C++ API를 사용합니다.</span> | [Documentation/introduction.rst:144](#source-d47b8630f593cf3c) · [Documentation/libcamera_architecture.rst:72](#source-611760d3be65ec8c) |
    | <span data-sdd-label-en="Other languages can use optional bindings.">다른 언어는 선택적 언어 바인딩을 사용할 수 있습니다.</span> | [Documentation/introduction.rst:144](#source-d47b8630f593cf3c) |
    | <span data-sdd-label-en="Other frameworks use integration components.">외부 프레임워크는 연결 구성 요소를 사용합니다.</span> | [Documentation/introduction.rst:153](#source-72dfdf22c79d4609) |
    | <span data-sdd-label-en="Examples include a V4L2 layer, a GStreamer element, and an Android camera HAL.">V4L2 호환 계층, GStreamer 요소, Android 카메라 HAL이 예입니다.</span> | [Documentation/introduction.rst:153](#source-72dfdf22c79d4609) |
    | <span data-sdd-label-en="The libcamera core controls camera devices.">libcamera 코어가 카메라 장치를 제어합니다.</span> | [Documentation/introduction.rst:144](#source-d47b8630f593cf3c) · [Documentation/libcamera_architecture.rst:72](#source-611760d3be65ec8c) |
    | <span data-sdd-label-en="Native C++ API">네이티브 C++ API</span> | [Documentation/introduction.rst:144](#source-d47b8630f593cf3c) · [Documentation/libcamera_architecture.rst:72](#source-611760d3be65ec8c) |
    | <span data-sdd-label-en="Optional bindings">선택적 바인딩</span> | [Documentation/introduction.rst:144](#source-d47b8630f593cf3c) |
    | <span data-sdd-label-en="Connects to libcamera">libcamera에 연결</span> | [Documentation/introduction.rst:153](#source-72dfdf22c79d4609) · [Documentation/introduction.rst:144](#source-d47b8630f593cf3c) |
    | <span data-sdd-label-en="Integration examples">연결 구성 요소 예</span> | [Documentation/introduction.rst:153](#source-72dfdf22c79d4609) |
<!-- /sdd:visual:interfaces-to-upper-layers -->

libcamera adaptation은 다른 프레임워크의 구성 요소 중 libcamera와 연결되는 구성 요소를 통칭합니다. 예로는 V4L2 호환 계층, gstreamer의 libcamera 요소, libcamera를 기반으로 구현한 Android 카메라 HAL(하드웨어와 소프트웨어를 연결하는 계층)이 있습니다. 이러한 구성 요소는 libcamera 프로젝트 소스 코드의 별도 저장소에 있거나 각 프로젝트의 저장소로 옮겨질 수 있습니다. 구체적인 입출력과 협업 책임은 확인되지 않습니다. `Documentation/introduction.rst:153`

근거 원문: [Documentation/introduction.rst:144](#source-d47b8630f593cf3c) · [Documentation/libcamera_architecture.rst:72](#source-611760d3be65ec8c) · [Documentation/introduction.rst:153](#source-72dfdf22c79d4609)

## 다른 팀·계층과의 경계

libcamera 프레임워크(소프트웨어 개발의 기반 구조) 또는 libcamera를 맞춰 적용한 것을 기반으로 하는 애플리케이션(응용 프로그램)과 상위 수준 프레임워크는 libcamera 프로젝트의 범위 밖에 있습니다. `Documentation/introduction.rst:163`

<!-- sdd:visual:item-boundaries -->
### 다른 팀·계층과의 경계의 관계와 경계

```mermaid
flowchart TB
%% sdd:translations {"Handlers는 libcamera 코드 <br/>기반의 일부입니다.": "Handlers are part of the <br/>libcamera code base.", "IPA Modules는 Pipeline <br/>Handler API로만 libcamera와 <br/>상호작용하며 kernel camera <br/>devices에 직접 접근할 수 <br/>없습니다.": "IPA Modules use only the <br/>Pipeline Handler API to <br/>interact with libcamera and <br/>cannot directly access <br/>kernel camera devices.", "IPA Modules는 별도 <br/>플러그인입니다. in-tree <br/>모듈에는 free software <br/>license가 적용되며 외부 IPA <br/>Modules는 open-source 또는 <br/>closed-source일 수 있습니다.": "IPA Modules are separate <br/>plugins. In-tree modules <br/>have a free software <br/>license; external IPA <br/>Modules may be open-source <br/>or closed-source.", "IPA 알고리즘은 IPA <br/>Modules라는 외부 <br/>플러그인으로 로드됩니다.": "IPA algorithms are loaded <br/>as external plugins named <br/>IPA Modules.", "IPA 알고리즘은 하드웨어 <br/>이미지 처리 및 통계 수집과 <br/>함께 3A 등을 구현하고 <br/>하드웨어 이미지 처리를 <br/>제어합니다.": "IPA algorithms implement 3A <br/>and others with hardware <br/>image processing and <br/>statistics collection, and <br/>control hardware image <br/>processing.", "Pipeline Handler는 stream <br/>configuration을 바탕으로 <br/>pipeline을 구성하고 장치에 <br/>필요하면 runtime 실행과 <br/>scheduling을 수행합니다.": "The Pipeline Handler <br/>configures pipelines from <br/>stream configuration and <br/>handles runtime execution <br/>and scheduling when the <br/>device needs them.", "libcamera는 카메라 지원을 <br/>위한 프레임워크와 코드 <br/>기반을 제공합니다.": "libcamera provides a <br/>framework and code base for <br/>camera support.", "third parties가 배포하는 <br/>외부 closed-source IPA <br/>Modules에는 libcamera <br/>프로젝트의 소스 코드가 <br/>없어야 합니다.": "External closed-source IPA <br/>Modules distributed by <br/>third parties must not <br/>include libcamera project <br/>source code.", "third parties는 외부 IPA <br/>Modules를 개발하고 배포할 <br/>수 있습니다.": "Third parties may develop <br/>and distribute external IPA <br/>Modules.", "애플리케이션과 상위 <br/>프레임워크는 libcamera <br/>프레임워크 또는 <br/>adaptation을 기반으로 <br/>합니다.": "Applications and <br/>upper-level frameworks are <br/>based on the libcamera <br/>framework or adaptation.", "애플리케이션과 상위 <br/>프레임워크는 libcamera <br/>프로젝트 범위 밖에 있습니다.": "Applications and <br/>upper-level frameworks are <br/>outside the libcamera <br/>project scope.", "장치 제조사는 Handlers를 <br/>upstream에 기여해야 합니다.": "Device vendors must <br/>contribute Handlers <br/>upstream.", "장치 제조사는 Pipeline <br/>Handler를 upstream에 <br/>기여해야 하며 외부 IPA <br/>Modules를 제공할 수 <br/>있습니다.": "Device vendors must <br/>contribute Pipeline <br/>Handlers upstream and may <br/>provide external IPA <br/>Modules.", "장치별 Handlers는 <br/>하드웨어를 추상화하고, 실행 <br/>시스템에서 감지해 지원하는 <br/>장치의 Camera 인스턴스를 <br/>만들며 카메라 장치와의 <br/>상호작용을 관리합니다.": "Device-specific Handlers <br/>abstract hardware, create <br/>Camera instances for this <br/>system#39;s detected and <br/>supported devices, and <br/>manage camera-device <br/>interactions.", "장치별 Handlers는 Pipeline <br/>Handler 기본 클래스를 <br/>상속합니다.": "Device-specific Handlers <br/>derive from the Pipeline <br/>Handler base class."}
  v_applications["애플리케이션과 상위 <br/>프레임워크는 libcamera <br/>프로젝트 범위 밖에 있습니다."]
  v_libcamera["libcamera는 카메라 지원을 <br/>위한 프레임워크와 코드 <br/>기반을 제공합니다."]
  v_vendors["장치 제조사는 Pipeline <br/>Handler를 upstream에 <br/>기여해야 하며 외부 IPA <br/>Modules를 제공할 수 <br/>있습니다."]
  v_handlers["장치별 Handlers는 <br/>하드웨어를 추상화하고, 실행 <br/>시스템에서 감지해 지원하는 <br/>장치의 Camera 인스턴스를 <br/>만들며 카메라 장치와의 <br/>상호작용을 관리합니다."]
  v_pipeline["Pipeline Handler는 stream <br/>configuration을 바탕으로 <br/>pipeline을 구성하고 장치에 <br/>필요하면 runtime 실행과 <br/>scheduling을 수행합니다."]
  v_algorithms["IPA 알고리즘은 하드웨어 <br/>이미지 처리 및 통계 수집과 <br/>함께 3A 등을 구현하고 <br/>하드웨어 이미지 처리를 <br/>제어합니다."]
  v_modules["IPA Modules는 별도 <br/>플러그인입니다. in-tree <br/>모듈에는 free software <br/>license가 적용되며 외부 IPA <br/>Modules는 open-source 또는 <br/>closed-source일 수 있습니다."]
  v_third["third parties가 배포하는 <br/>외부 closed-source IPA <br/>Modules에는 libcamera <br/>프로젝트의 소스 코드가 <br/>없어야 합니다."]
  v_applications -->|"애플리케이션과 상위 <br/>프레임워크는 libcamera <br/>프레임워크 또는 <br/>adaptation을 기반으로 <br/>합니다."| v_libcamera
  v_handlers -->|"Handlers는 libcamera 코드 <br/>기반의 일부입니다."| v_libcamera
  v_vendors -->|"장치 제조사는 Handlers를 <br/>upstream에 기여해야 합니다."| v_handlers
  v_handlers -->|"장치별 Handlers는 Pipeline <br/>Handler 기본 클래스를 <br/>상속합니다."| v_pipeline
  v_algorithms -->|"IPA 알고리즘은 IPA <br/>Modules라는 외부 <br/>플러그인으로 로드됩니다."| v_modules
  v_third -->|"third parties는 외부 IPA <br/>Modules를 개발하고 배포할 <br/>수 있습니다."| v_modules
  v_modules -->|"IPA Modules는 Pipeline <br/>Handler API로만 libcamera와 <br/>상호작용하며 kernel camera <br/>devices에 직접 접근할 수 <br/>없습니다."| v_pipeline
```

[Mermaid 원문](team-overview.item-boundaries.mmd)

??? note "그림 근거와 확인 범위"
    애플리케이션, libcamera, 장치 제조사, Pipeline Handler와 IPA Module 사이에서 프로젝트 범위와 책임은 어떻게 나뉩니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Applications and upper-level frameworks are outside the libcamera project scope.">애플리케이션과 상위 프레임워크는 libcamera 프로젝트 범위 밖에 있습니다.</span> | [Documentation/introduction.rst:163](#source-9e653b8ff755db78) |
    | <span data-sdd-label-en="libcamera provides a framework and code base for camera support.">libcamera는 카메라 지원을 위한 프레임워크와 코드 기반을 제공합니다.</span> | [Documentation/introduction.rst:163](#source-9e653b8ff755db78) · [Documentation/introduction.rst:200](#source-341442e08591ef50) |
    | <span data-sdd-label-en="Device vendors must contribute Pipeline Handlers upstream and may provide external IPA Modules.">장치 제조사는 Pipeline Handler를 upstream에 기여해야 하며 외부 IPA Modules를 제공할 수 있습니다.</span> | [Documentation/introduction.rst:200](#source-341442e08591ef50) · [Documentation/libcamera_architecture.rst:109](#source-1f130cc8640ef810) |
    | <span data-sdd-label-en="Device-specific Handlers abstract hardware, create Camera instances for this system&#x27;s detected and supported devices, and manage camera-device interactions.">장치별 Handlers는 하드웨어를 추상화하고, 실행 시스템에서 감지해 지원하는 장치의 Camera 인스턴스를 만들며 카메라 장치와의 상호작용을 관리합니다.</span> | [Documentation/libcamera_architecture.rst:87](#source-8bd888bd0473995e) |
    | <span data-sdd-label-en="The Pipeline Handler configures pipelines from stream configuration and handles runtime execution and scheduling when the device needs them.">Pipeline Handler는 stream configuration을 바탕으로 pipeline을 구성하고 장치에 필요하면 runtime 실행과 scheduling을 수행합니다.</span> | [Documentation/libcamera_architecture.rst:87](#source-8bd888bd0473995e) |
    | <span data-sdd-label-en="IPA algorithms implement 3A and others with hardware image processing and statistics collection, and control hardware image processing.">IPA 알고리즘은 하드웨어 이미지 처리 및 통계 수집과 함께 3A 등을 구현하고 하드웨어 이미지 처리를 제어합니다.</span> | [Documentation/libcamera_architecture.rst:109](#source-1f130cc8640ef810) |
    | <span data-sdd-label-en="IPA Modules are separate plugins. In-tree modules have a free software license; external IPA Modules may be open-source or closed-source.">IPA Modules는 별도 플러그인입니다. in-tree 모듈에는 free software license가 적용되며 외부 IPA Modules는 open-source 또는 closed-source일 수 있습니다.</span> | [Documentation/libcamera_architecture.rst:109](#source-1f130cc8640ef810) · [Documentation/introduction.rst:200](#source-341442e08591ef50) |
    | <span data-sdd-label-en="External closed-source IPA Modules distributed by third parties must not include libcamera project source code.">third parties가 배포하는 외부 closed-source IPA Modules에는 libcamera 프로젝트의 소스 코드가 없어야 합니다.</span> | [Documentation/introduction.rst:200](#source-341442e08591ef50) |
    | <span data-sdd-label-en="Applications and upper-level frameworks are based on the libcamera framework or adaptation.">애플리케이션과 상위 프레임워크는 libcamera 프레임워크 또는 adaptation을 기반으로 합니다.</span> | [Documentation/introduction.rst:163](#source-9e653b8ff755db78) |
    | <span data-sdd-label-en="Handlers are part of the libcamera code base.">Handlers는 libcamera 코드 기반의 일부입니다.</span> | [Documentation/introduction.rst:200](#source-341442e08591ef50) |
    | <span data-sdd-label-en="Device vendors must contribute Handlers upstream.">장치 제조사는 Handlers를 upstream에 기여해야 합니다.</span> | [Documentation/introduction.rst:200](#source-341442e08591ef50) |
    | <span data-sdd-label-en="Device-specific Handlers derive from the Pipeline Handler base class.">장치별 Handlers는 Pipeline Handler 기본 클래스를 상속합니다.</span> | [Documentation/libcamera_architecture.rst:87](#source-8bd888bd0473995e) |
    | <span data-sdd-label-en="IPA algorithms are loaded as external plugins named IPA Modules.">IPA 알고리즘은 IPA Modules라는 외부 플러그인으로 로드됩니다.</span> | [Documentation/libcamera_architecture.rst:109](#source-1f130cc8640ef810) |
    | <span data-sdd-label-en="Third parties may develop and distribute external IPA Modules.">third parties는 외부 IPA Modules를 개발하고 배포할 수 있습니다.</span> | [Documentation/introduction.rst:200](#source-341442e08591ef50) |
    | <span data-sdd-label-en="IPA Modules use only the Pipeline Handler API to interact with libcamera and cannot directly access kernel camera devices.">IPA Modules는 Pipeline Handler API로만 libcamera와 상호작용하며 kernel camera devices에 직접 접근할 수 없습니다.</span> | [Documentation/libcamera_architecture.rst:120](#source-6c10d5aeb8fc7ca9) · [Documentation/libcamera_architecture.rst:109](#source-1f130cc8640ef810) |
<!-- /sdd:visual:item-boundaries -->

Pipeline Handler(파이프라인 처리기)는 장치별 파이프라인을 관리하며, 장치 제조사는 이를 libcamera에 기여해야 합니다. 이미지 처리 알고리즘(`Image` Processing Algorithms, IPA)은 상위 계층의 매개변수를 바탕으로 하드웨어 이미지 처리를 제어하며, IPA `Module`(IPA 모듈)은 외부에서 별도로 제공할 수 있습니다. libcamera에 포함된 IPA `Module`에는 자유 소프트웨어 라이선스가 적용되며, 외부 모듈은 libcamera 프로젝트의 소스 코드를 포함하지 않는 조건으로 비공개 소스 라이선스로 배포할 수 있습니다. IPA `Module`은 libcamera와 Pipeline Handler가 제공하는 API(응용 프로그램 인터페이스)로만 상호작용하며 kernel camera devices(커널 카메라 장치)에 직접 접근할 수 없습니다. `Documentation/libcamera_architecture.rst:87`, `Documentation/libcamera_architecture.rst:109`, `Documentation/introduction.rst:200`, `Documentation/libcamera_architecture.rst:120`

근거 원문: [Documentation/introduction.rst:163](#source-9e653b8ff755db78) · [Documentation/libcamera_architecture.rst:87](#source-8bd888bd0473995e) · [Documentation/libcamera_architecture.rst:109](#source-1f130cc8640ef810) · [Documentation/introduction.rst:200](#source-341442e08591ef50) · [Documentation/libcamera_architecture.rst:120](#source-6c10d5aeb8fc7ca9)

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

<a id="source-6c10d5aeb8fc7ca9"></a>

??? note "소스 근거: Documentation/libcamera_architecture.rst:120"
    `Documentation/libcamera_architecture.rst:120`에서 시작하는 발췌입니다. 종료 줄은 127이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `d877bb3fd4bb3023c4b18924fc81b0d964997c3ddf7263ba68b4c05d91f883c9`
    
    ```text
    IPA Modules built with libcamera are run in the same process space as the
      library. External IPA Modules are run in a separate sandboxed process. In
      either case, they can only interact with libcamera through the API provided
      by the Pipeline Handler. They have a restricted view of the system, with no
      direct access to kernel camera devices, no access to networking APIs, and
      limited access to file systems. All their accesses to image and metadata are
      mediated by dmabuf instances explicitly passed by the Pipeline Handler to the
      IPA Module.
    ```

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `Documentation/introduction.rst`, `Documentation/libcamera_architecture.rst`, `include/libcamera/camera.h`, `include/libcamera/camera_manager.h`, `include/libcamera/internal/pipeline_handler.h`, `src/libcamera/camera.cpp`, `src/libcamera/camera_manager.cpp`, `src/libcamera/pipeline_handler.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `c19d05128f`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-12 · 사람 검토 전

다음 단계: [시스템 개요](overview.md)
