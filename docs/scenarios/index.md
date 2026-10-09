---
generated_at: 2026-10-09T16:52:35+00:00
source_commit: 06c3e2d719490aad8ce789fb5d2ad4dfa1459bfb
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
| 캡처 종료 요청 (Camera::stop) 흐름을 추적합니다. | [캡처 종료 요청 (Camera::stop)](camera_stop.md) |

## 시나리오 목록

| 시나리오 | 진입점 | 요약 대상 호출 | 요약에서 뺀 호출 | 예약된 호출 | 미해결 호출 |
|---|---|---|---|---|---|
| [카메라 탐색 (CameraManager::start)](manager_start.md) | `CameraManager::start()` | 16 | 17 | 1 | 0 |
| [스트림 구성 (Camera::configure)](configure.md) | `Camera::configure(CameraConfiguration *)` | 121 | 87 | 1 | 0 |
| [캡처 시작 (Camera::start)](camera_start.md) | `Camera::start(const ControlList *)` | 21 | 27 | 2 | 0 |
| [요청 제출 (Camera::queueRequest)](queue_request.md) | `Camera::queueRequest(Request *)` | 29 | 51 | 1 | 0 |
| [요청 완료 통지 (PipelineHandler::completeRequest)](complete_request.md) | `PipelineHandler::completeRequest(Request *)` | 43 | 62 | 0 | 0 |
| [캡처 종료 요청 (Camera::stop)](camera_stop.md) | `Camera::stop()` | 7 | 26 | 1 | 0 |

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 설정으로 생성
    - 검증 범위: 표와 목록을 facts 또는 문서 설정에서 구성합니다. LLM을 호출하지 않습니다.
    - 근거 파일: (없음)
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `06c3e2d719`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-10 · 사람 검토 전

다음 단계: [요청 처리와 문제 진단](../request-lifecycle.md)
