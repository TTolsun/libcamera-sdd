---
generated_at: 2026-10-30T17:20:44+00:00
source_commit: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61
status: ok
section: scenarios
generation_method: deterministic
scenario_index_fingerprint: 911dedbcdc3ecbb5a97dbb746a1cda781743a19d9b1587295b92fbe8bff9d29f
scenario_index_body_sha256: 5f5a05fccd457f0094c17b57e4d73a5afc1ee0c714d0d87c37c0d43ef52d551e
revalidated_from: 212c689fcf2450bbfbaab25c7472895ac277b5d6
---

# 핵심 시나리오

**확인할 동작을 고른 뒤 호출 전제와 완료·실패 설명을 읽으세요. 주요 호출과 전체 추적 기록은 각 문서의 상세 자료로 이어집니다.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 카메라 탐색 (CameraManager::start) 흐름을 추적합니다. | [카메라 탐색](manager_start.md) |
| 스트림 구성 (Camera::configure) 흐름을 추적합니다. | [스트림 구성](configure.md) |
| 캡처 시작 (Camera::start) 흐름을 추적합니다. | [캡처 시작](camera_start.md) |
| 요청 제출 (Camera::queueRequest) 흐름을 추적합니다. | [요청 제출](queue_request.md) |
| 요청 완료 통지 (PipelineHandler::completeRequest) 흐름을 추적합니다. | [요청 완료 통지](complete_request.md) |
| 캡처 종료 요청 (Camera::stop) 흐름을 추적합니다. | [캡처 종료 요청](camera_stop.md) |

## 시나리오 목록

| 시나리오 | 확인할 동작과 조건 | 진입점 |
|---|---|---|
| [카메라 탐색 (CameraManager::start)](manager_start.md) | 관리자 시작의 성공·실패를 확인한 뒤 탐색된 카메라를 사용하세요. | `CameraManager::start()` |
| [스트림 구성 (Camera::configure)](configure.md) | 캡처 전에 유효한 스트림 구성을 적용하고 실패 조건과 연결된 Stream을 확인하세요. | `Camera::configure(CameraConfiguration *)` |
| [캡처 시작 (Camera::start)](camera_start.md) | 구성이 끝난 카메라를 시작하고 성공 뒤 요청을 제출할 수 있는 상태인지 확인하세요. | `Camera::start(const ControlList *)` |
| [요청 제출 (Camera::queueRequest)](queue_request.md) | 시작된 카메라에 유효한 요청을 제출하고 완료 알림은 별도로 확인하세요. | `Camera::queueRequest(Request *)` |
| [요청 완료 통지 (PipelineHandler::completeRequest)](complete_request.md) | 버퍼 완료와 요청 완료를 구분하고 제출 순서대로 돌아오는 알림과 접근 종료 책임을 확인하세요. | `PipelineHandler::completeRequest(Request *)` |
| [캡처 종료 요청 (Camera::stop)](camera_stop.md) | 캡처를 멈추고 대기 요청의 취소 완료와 구성 상태 복귀 조건을 확인하세요. | `Camera::stop()` |

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 설정으로 생성
    - 검증 범위: 표와 목록을 facts 또는 문서 설정에서 구성합니다. LLM을 호출하지 않습니다.
    - 근거 파일: (없음)
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `212c689fcf`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-31 · 사람 검토 전

다음 단계: [요청 처리와 문제 진단](../request-lifecycle.md)
