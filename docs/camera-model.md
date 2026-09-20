---
generated_at: 2026-09-20T14:09:01+00:00
source_commit: 279d355ef8f7a4f98bb0a3004c0f788387814506
agent: ollama/qwen3.5:4b
status: needs-review
section: camera-model
---

# 카메라와 요청 모델

**CameraManager, Camera, Request의 선언과 메서드 위치부터 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 관련 클래스 절을 확인합니다. | [관련 클래스](#관련-클래스) |
| 구조 설명 절을 확인합니다. | [구조 설명](#구조-설명) |

## 관련 클래스

| 클래스 | 선언 위치 | 상속 | 책임 (주석) |
|---|---|---|---|
| `libcamera::Camera` | `include/libcamera/camera.h:114` | `libcamera::Object`, `libcamera::Extensible` | 확인 필요 |
| `libcamera::CameraManager` | `include/libcamera/camera_manager.h:24` | `libcamera::Object`, `libcamera::Extensible` | 확인 필요 |
| `libcamera::Request` | `include/libcamera/request.h:29` | `libcamera::Extensible` | 확인 필요 |

## 구조 설명

카메라 탐색과 요청 처리는 `libcamera::CameraManager` [include/libcamera/camera_manager.h:24] 와 `libcamera::Camera` [include/libcamera/camera.h:114] 클래스로 나뉘며, 카메라 생성은 `create()` [src/libcamera/camera.cpp:860] 메서드를 통해 수행됩니다. `libcamera::Camera` 의 ID 를 확인하거나 `acquire()` [src/libcamera/camera.cpp:1007] 와 같은 접근 권한을 관리하는 메서드들은 해당 클래스의 내부 구현에 의존합니다.

??? note "근거와 검토 정보"
    - 근거 파일: `include/libcamera/camera.h`, `include/libcamera/camera_manager.h`, `include/libcamera/request.h`, `src/libcamera/camera.cpp`, `src/libcamera/camera_manager.cpp`, `src/libcamera/request.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `279d355ef8`)
    - 인용 검증: 실패 (인용이 하나도 없습니다.; 클래스나 함수를 언급하면서 인용이 없는 문단 1 개)
    - 검토: 2026-09-20 · ollama/qwen3.5:4b · 사람 검토 전

다음 단계: [Pipeline Handler](pipeline-handler.md)
