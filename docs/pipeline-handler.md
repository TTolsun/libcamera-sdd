---
generated_at: 2026-09-23T16:34:40+00:00
source_commit: 279d355ef8f7a4f98bb0a3004c0f788387814506
agent: ollama/qwen3.5:4b
status: ok
section: pipeline-handler
evidence_fingerprint: 7abb77d540bf0fcb9063101cf9e9645dfc63f0f60945a3d140ff036a7bcda00e
semantic_review: human-review-required
---

# Pipeline Handler

**공통 PipelineHandler와 빌드에 포함된 구현의 관계를 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 구조 설명 절을 확인합니다. | [구조 설명](#구조-설명) |
| 클래스 관계 절을 확인합니다. | [클래스 관계](#클래스-관계) |
| 관련 클래스 절을 확인합니다. | [관련 클래스](#관련-클래스) |

## 구조 설명

`libcamera::PipelineHandler`는 `libcamera::Object`를 직접 기반으로 하며, 하드웨어별 구현은 이를 상속받아 `PipelineHandlerIPU3`, `PipelineHandlerRkISP1`, `PipelineHandlerUVC`가 생성됩니다. `PipelineHandlerIPU3`와 `PipelineHandlerRkISP1`의 상속 관계는 각각 해당 클래스 정의 위치에서 확인 가능합니다 `src/libcamera/pipeline/ipu3/ipu3.cpp:124`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp:184`.

설정과 요청 전달을 위한 메서드는 `PipelineHandler`와 하위 클래스에 공통적으로 존재하며, 구체적인 구현 위치는 각 파일의 해당 라인에서 확인합니다. `PipelineHandlerIPU3`의 `generateConfiguration()` 및 `configure()`는 `src/libcamera/pipeline/ipu3/ipu3.cpp:393`, `src/libcamera/pipeline/ipu3/ipu3.cpp:480`에 정의되고, `PipelineHandlerRkISP1`의 대응 메서드는 `src/libcamera/pipeline/rkisp1/rkisp1.cpp:790`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp:913`에서 찾을 수 있습니다.


<!-- sdd:class-diagram -->
## 클래스 관계

화살표의 글자는 추출한 관계를 나타내며, 점선은 상속입니다. 화살표는 참조 대상 또는 기반 클래스를 향합니다. 호출 순서를 뜻하지 않습니다.

```mermaid
flowchart LR
  c0["Object"]:::context
  c1["PipelineHandler"]
  c2["PipelineHandlerFactory"]
  c3["PipelineHandlerFactoryBase"]
  c4["PipelineHandlerIPU3"]
  c5["PipelineHandlerIPU3::IPU3PipeModes"]
  c6["PipelineHandlerRkISP1"]
  c7["PipelineHandlerUVC"]
  c1 -.->|상속| c0
  c2 -.->|상속| c3
  c4 -.->|상속| c1
  c6 -.->|상속| c1
  c7 -.->|상속| c1
  classDef context fill:#fafafa,stroke:#aaa,stroke-dasharray:4 3,color:#555
```
<!-- /sdd:class-diagram -->



## 관련 클래스

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::PipelineHandler` | `include/libcamera/internal/pipeline_handler.h:34` | `libcamera::Object` | 확인 필요 |
| `libcamera::PipelineHandlerFactory` | `include/libcamera/internal/pipeline_handler.h:144` | `libcamera::PipelineHandlerFactoryBase` | 확인 필요 |
| `libcamera::PipelineHandlerFactoryBase` | `include/libcamera/internal/pipeline_handler.h:121` | – | 확인 필요 |
| `libcamera::PipelineHandlerIPU3` | `src/libcamera/pipeline/ipu3/ipu3.cpp:124` | `libcamera::PipelineHandler` | 확인 필요 |
| `libcamera::PipelineHandlerIPU3::IPU3PipeModes` | `src/libcamera/pipeline/ipu3/ipu3.cpp:130` | – | 확인 필요 |
| `libcamera::PipelineHandlerRkISP1` | `src/libcamera/pipeline/rkisp1/rkisp1.cpp:184` | `libcamera::PipelineHandler` | 확인 필요 |
| `libcamera::PipelineHandlerUVC` | `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp:81` | `libcamera::PipelineHandler` | 확인 필요 |

??? note "근거와 검토 정보"
    - 근거 파일: `include/libcamera/internal/pipeline_handler.h`, `src/libcamera/pipeline/ipu3/ipu3.cpp`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp`, `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp`, `src/libcamera/pipeline_handler.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `279d355ef8`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토: 2026-09-24 · ollama/qwen3.5:4b · 사람 검토 전

다음 단계: [IPA 관련 클래스](ipa.md)
