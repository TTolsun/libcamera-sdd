---
generated_at: 2026-09-26T13:32:24+00:00
source_commit: 279d355ef8f7a4f98bb0a3004c0f788387814506
status: ok
section: scenarios
generation_method: deterministic
---

# 핵심 시나리오

**추적하려는 동작을 표에서 고르세요. 각 시나리오에서 주요 호출, 추적 경계와 전체 기록을 확인할 수 있습니다.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 카메라 탐색 (CameraManager::start) 흐름을 추적합니다. | [카메라 탐색 (CameraManager::start)](manager_start.md) |
| 스트림 구성 (Camera::configure) 흐름을 추적합니다. | [스트림 구성 (Camera::configure)](configure.md) |
| 캡처 시작 (Camera::start) 흐름을 추적합니다. | [캡처 시작 (Camera::start)](camera_start.md) |
| 요청 제출 (Camera::queueRequest) 흐름을 추적합니다. | [요청 제출 (Camera::queueRequest)](queue_request.md) |
| 요청 완료 통지 (PipelineHandler::completeRequest) 흐름을 추적합니다. | [요청 완료 통지 (PipelineHandler::completeRequest)](complete_request.md) |

## 시나리오 목록

| 시나리오 | 진입점 | 요약 대상 호출 | 요약에서 뺀 호출 | 예약된 호출 | 미해결 호출 |
|---|---|---|---|---|---|
| [카메라 탐색 (CameraManager::start)](manager_start.md) | `CameraManager::start()` | 16 | 17 | 1 | 0 |
| [스트림 구성 (Camera::configure)](configure.md) | `Camera::configure(CameraConfiguration *)` | 121 | 87 | 1 | 0 |
| [캡처 시작 (Camera::start)](camera_start.md) | `Camera::start(const ControlList *)` | 21 | 27 | 2 | 0 |
| [요청 제출 (Camera::queueRequest)](queue_request.md) | `Camera::queueRequest(Request *)` | 29 | 51 | 1 | 0 |
| [요청 완료 통지 (PipelineHandler::completeRequest)](complete_request.md) | `PipelineHandler::completeRequest(Request *)` | 43 | 62 | 0 | 0 |

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 설정으로 생성
    - 검증 범위: 표와 목록을 facts 또는 문서 설정에서 구성합니다. LLM을 호출하지 않습니다.
    - 근거 파일: (없음)
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `279d355ef8`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-09-26 · 사람 검토 전

다음 단계: [카메라와 요청 모델](../camera-model.md)
