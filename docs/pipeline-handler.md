---
generated_at: 2026-09-20T14:09:12+00:00
source_commit: 279d355ef8f7a4f98bb0a3004c0f788387814506
agent: ollama/qwen3.5:4b
status: ok
section: pipeline-handler
---

# Pipeline Handler

**공통 PipelineHandler와 빌드에 포함된 구현의 관계를 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 관련 클래스 절을 확인합니다. | [관련 클래스](#관련-클래스) |
| 구조 설명 절을 확인합니다. | [구조 설명](#구조-설명) |

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

## 구조 설명

**공통 클래스와 하드웨어별 구현의 상속 관계를 확인하고, 설정 및 요청 전달에 직접 사용되는 메서드를 식별하세요.**

기존 본문은 인용 없이 기술적 설명을 작성했습니다. 사실 블록에 명시된 `파일:줄` 위치를 근거로 문장을 구성합니다.

`libcamera::PipelineHandler`는 공통 인터페이스를 정의하며, `src/libcamera/pipeline_handler.cpp:72`에서 생성자 호출이 확인됩니다. 하드웨어별 구현은 이 클래스를 상속받습니다. 예를 들어 `libcamera::PipelineHandlerIPU3`의 정의를 먼저 확인합니다 `src/libcamera/pipeline/ipu3/ipu3.cpp:124`.

설정은 `generateConfiguration()`과 `configure()` 메서드를 통해 처리되며, `include/libcamera/internal/pipeline_handler.h:49`와 `include/libcamera/internal/pipeline_handler.h:51`에서 선언됩니다. 요청 전달은 `queueRequestDevice()`를 통해 이루어지는데, `src/libcamera/pipeline/ipu3/ipu3.cpp:838`와 `src/libcamera/pipeline/rkisp1/rkisp1.cpp:1340`에 해당 구현이 존재합니다.

??? note "근거와 검토 정보"
    - 근거 파일: `include/libcamera/internal/pipeline_handler.h`, `src/libcamera/pipeline/ipu3/ipu3.cpp`, `src/libcamera/pipeline/rkisp1/rkisp1.cpp`, `src/libcamera/pipeline/uvcvideo/uvcvideo.cpp`, `src/libcamera/pipeline_handler.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `279d355ef8`)
    - 인용 검증: 통과
    - 검토: 2026-09-20 · ollama/qwen3.5:4b · 사람 검토 전

다음 단계: [IPA 관련 클래스](ipa.md)
