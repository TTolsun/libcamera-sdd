---
generated_at: 2026-09-24T14:05:15+00:00
source_commit: 279d355ef8f7a4f98bb0a3004c0f788387814506
agent: ollama/qwen3.5:4b
status: ok
section: scenarios
---

# 핵심 시나리오 시퀀스

**추적하려는 동작을 표에서 고르세요. 각 시나리오는 진입 함수부터 호출 순서를 번호로 보여 줍니다.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 카메라 탐색 (CameraManager::start) 흐름을 추적합니다. | [카메라 탐색 (CameraManager::start)](manager_start.md) |
| 스트림 구성 (Camera::configure) 흐름을 추적합니다. | [스트림 구성 (Camera::configure)](configure.md) |
| 캡처 시작 (Camera::start) 흐름을 추적합니다. | [캡처 시작 (Camera::start)](camera_start.md) |
| 요청 제출 (Camera::queueRequest) 흐름을 추적합니다. | [요청 제출 (Camera::queueRequest)](queue_request.md) |
| 요청 완료 통지 (PipelineHandler::completeRequest) 흐름을 추적합니다. | [요청 완료 통지 (PipelineHandler::completeRequest)](complete_request.md) |

## 시나리오 목록

| 시나리오 | 진입점 | 단계 수 | 표시에서 뺀 호출 | 예약된 호출 | 미해결 호출 |
|---|---|---|---|---|---|
| [카메라 탐색 (CameraManager::start)](manager_start.md) | `CameraManager::start()` | 16 | 17 | 1 | 0 |
| [스트림 구성 (Camera::configure)](configure.md) | `Camera::configure(CameraConfiguration *)` | 129 | 79 | 1 | 0 |
| [캡처 시작 (Camera::start)](camera_start.md) | `Camera::start(const ControlList *)` | 21 | 27 | 2 | 0 |
| [요청 제출 (Camera::queueRequest)](queue_request.md) | `Camera::queueRequest(Request *)` | 31 | 49 | 1 | 0 |
| [요청 완료 통지 (PipelineHandler::completeRequest)](complete_request.md) | `PipelineHandler::completeRequest(Request *)` | 48 | 57 | 0 | 0 |

??? note "근거와 검토 정보"
    - 근거 파일: (없음)
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `279d355ef8`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토: 2026-09-24 · ollama/qwen3.5:4b · 사람 검토 전

다음 단계: [카메라와 요청 모델](../camera-model.md)
