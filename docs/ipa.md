---
generated_at: 2026-09-24T12:17:51+00:00
source_commit: 279d355ef8f7a4f98bb0a3004c0f788387814506
agent: ollama/qwen3.5:4b
status: ok
section: ipa
evidence_fingerprint: 14c9a89e2ce5766568f800f99425cb02ee1e5ef1db1697bff4f40361d3bd8ea8
semantic_review: human-review-required
---

# IPA 관리와 구현 진입점

**IPA 관리자, 모듈, 프록시와 IPU3·RKISP1 구현의 근거 위치를 먼저 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 구조 설명 절을 확인합니다. | [구조 설명](#구조-설명) |
| 클래스 관계 절을 확인합니다. | [클래스 관계](#클래스-관계) |
| 관련 클래스 절을 확인합니다. | [관련 클래스](#관련-클래스) |

## 구조 설명

IPA 관련 클래스는 `libcamera::IPAManager`, `libcamera::IPAModule`, `libcamera::IPAProxy` 및 하드웨어 구현체인 `libcamera::ipa::ipu3::IPAIPU3`, `libcamera::ipa::rkisp1::IPARkISP1`으로 구분됩니다. `IPAManager`는 카메라 관리자와 연결되며 `createIPA()`와 `parseDir()` 메서드를 통해 모듈을 로드합니다 `include/libcamera/internal/ipa_manager.h:29` `src/libcamera/ipa_manager.cpp:175`. `IPAModule`은 `Loggable`을 상속받아 유효성 검사와 정보 조회를 수행하며 `load()`와 `createInterface()`를 통해 구현 팩토리를 인스턴타합니다 `include/libcamera/internal/ipa_module.h:21` `src/libcamera/ipa_module.cpp:406`. `IPAProxy`는 `IPAInterface`를 상속받아 프로세스 경계에서 실행되며 `resolvePath()`를 통해 유효한 경로로 해결합니다 `include/libcamera/internal/ipa_proxy.h:22` `src/libcamera/ipa_proxy.cpp:217`.

하드웨어 구현 클래스인 `IPAIPU3`와 `IPARkISP1`은 각각 해당 인터페이스와 `Module`을 상속받아 초기화부터 요청 큐잉까지의 처리 흐름을 정의합니다. `IPAIPU3`는 `init()`, `start()`, `configure()` 및 `queueRequest()`를 통해 IPU3 제어기를 설정하고 애플리케이션의 컨트롤 리스트를 처리합니다 `src/ipa/ipu3/ipu3.cpp:218` `src/ipa/ipu3/ipu3.cpp:534`. `IPARkISP1`은 유사한 순서로 `init()`, `start()` 및 `computeParams()`를 호출하여 ISP 파라미터를 계산합니다 `src/ipa/rkisp1/rkisp1.cpp:131` `src/ipa/rkisp1/rkisp1.cpp:301`. 스레드 동기화나 콜백 전달의 구체적인 순서는 메서드 목록만으로는 판단하기 어렵습니다.


<!-- sdd:class-diagram -->
## 클래스 관계

화살표의 글자는 추출한 관계를 나타내며, 점선은 상속입니다. 화살표는 참조 대상 또는 기반 클래스를 향합니다. 호출 순서를 뜻하지 않습니다.

```mermaid
flowchart LR
  c0["IPAInterface"]:::context
  c1["IPAManager"]
  c2["IPAModule"]
  c3["IPAProxy"]
  c4["Loggable"]:::context
  c5["ipa::ipu3::IPAIPU3"]
  c6["ipa::ipu3::IPAIPU3Interface"]:::context
  c7["ipa::ipu3::Module"]:::context
  c8["ipa::rkisp1::IPARkISP1"]
  c9["ipa::rkisp1::IPARkISP1Interface"]:::context
  c10["ipa::rkisp1::Module"]:::context
  c1 -->|필드 참조| c2
  c2 -.->|상속| c4
  c3 -.->|상속| c0
  c3 -->|필드 참조| c2
  c5 -.->|상속| c6
  c5 -.->|상속| c7
  c8 -.->|상속| c9
  c8 -.->|상속| c10
  classDef context fill:#fafafa,stroke:#aaa,stroke-dasharray:4 3,color:#555
```
<!-- /sdd:class-diagram -->



## 관련 클래스

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::IPAManager` | `include/libcamera/internal/ipa_manager.h:29` | – | 확인 필요 |
| `libcamera::IPAModule` | `include/libcamera/internal/ipa_module.h:21` | `libcamera::Loggable` | 확인 필요 |
| `libcamera::IPAProxy` | `include/libcamera/internal/ipa_proxy.h:22` | `libcamera::IPAInterface` | 확인 필요 |
| `libcamera::ipa::ipu3::IPAIPU3` | `src/ipa/ipu3/ipu3.cpp:139` | `libcamera::ipa::ipu3::IPAIPU3Interface`, `libcamera::ipa::ipu3::Module` | The IPU3 IPA implementation |
| `libcamera::ipa::rkisp1::IPARkISP1` | `src/ipa/rkisp1/rkisp1.cpp:46` | `libcamera::ipa::rkisp1::IPARkISP1Interface`, `libcamera::ipa::rkisp1::Module` | 확인 필요 |

??? note "근거와 검토 정보"
    - 근거 파일: `include/libcamera/internal/ipa_manager.h`, `include/libcamera/internal/ipa_module.h`, `include/libcamera/internal/ipa_proxy.h`, `src/ipa/ipu3/ipu3.cpp`, `src/ipa/rkisp1/rkisp1.cpp`, `src/libcamera/ipa_manager.cpp`, `src/libcamera/ipa_module.cpp`, `src/libcamera/ipa_proxy.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `279d355ef8`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토: 2026-09-24 · ollama/qwen3.5:4b · 사람 검토 전

다음 단계: [IPU3 LSC와 상태 연결](ipu3-lsc.md)
