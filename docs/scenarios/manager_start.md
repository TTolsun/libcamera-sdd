---
generated_at: 2026-09-24T14:04:54+00:00
source_commit: 279d355ef8f7a4f98bb0a3004c0f788387814506
agent: ollama/qwen3.5:4b
status: ok
section: scenarios
entry: CameraManager::start()
---

# 카메라 탐색 (CameraManager::start)

**`CameraManager::start()` 에서 시작하는 호출 순서를 아래 번호대로 따라가세요.**



```mermaid
sequenceDiagram
    participant CameraManager
    participant Private
    participant Thread
    participant MutexLocker
    participant ConditionVariable
    participant EventDispatcherPoll
    participant UniqueFD
    participant lambda_at__home_baboess_work_libcamera_ab_validation_20260921_b_source_src_libcamera_base_thread_cpp_409_21 as (lambda at /home/baboess/work/libcamera-ab-validation-20260921/b/source/src/libcamera/base/thread.cpp:409:21)
    CameraManager->>Private: start()
    Private->>Thread: start()
    Thread->>MutexLocker: MutexLocker()
    Thread-->>Thread: startThread() [예약된 호출, 실행 순서는 정적으로 확인 불가]
    Thread->>Thread: setThreadAffinityInternal()
    Private->>MutexLocker: MutexLocker()
    Private->>ConditionVariable: wait()
    Private->>Thread: exit()
    Thread-->>EventDispatcherPoll: interrupt() [virtual, 현재 구현 하나]
    EventDispatcherPoll->>UniqueFD: get()
    Private->>Thread: wait()
    Thread->>MutexLocker: MutexLocker()
    Thread->>ConditionVariable: wait()
    Thread->>lambda_at__home_baboess_work_libcamera_ab_validation_20260921_b_source_src_libcamera_base_thread_cpp_409_21: (lambda at /home/baboess/work/libcamera-ab-validation-20260921/b/source/src/libcamera/base/thread.cpp:409:21)()
    Thread->>ConditionVariable: wait_for()
    Thread->>lambda_at__home_baboess_work_libcamera_ab_validation_20260921_b_source_src_libcamera_base_thread_cpp_409_21: (lambda at /home/baboess/work/libcamera-ab-validation-20260921/b/source/src/libcamera/base/thread.cpp:409:21)()
```

## 호출 순서

1. `CameraManager` 가 `Private::start()` 를 호출합니다. `src/libcamera/camera_manager.cpp:342`
2. `Private` 가 `Thread::start()` 를 호출합니다. `src/libcamera/camera_manager.cpp:51`
3. `Thread` 가 `MutexLocker::MutexLocker()` 를 호출합니다. `src/libcamera/base/thread.cpp:255`
4. `Thread` 가 `Thread::startThread()` 를 호출합니다. (예약된 호출, 실행 순서는 정적으로 확인 불가) `src/libcamera/base/thread.cpp:264`
5. `Thread` 가 `Thread::setThreadAffinityInternal()` 를 호출합니다. `src/libcamera/base/thread.cpp:266`
6. `Private` 가 `MutexLocker::MutexLocker()` 를 호출합니다. `src/libcamera/camera_manager.cpp:54`
7. `Private` 가 `ConditionVariable::wait()` 를 호출합니다. `src/libcamera/camera_manager.cpp:55`
8. `Private` 가 `Thread::exit()` 를 호출합니다. `src/libcamera/camera_manager.cpp:63`
9. `Thread` 가 `EventDispatcherPoll::interrupt()` 를 호출합니다. (virtual, 현재 구현 하나) `src/libcamera/base/thread.cpp:386`
10. `EventDispatcherPoll` 가 `UniqueFD::get()` 를 호출합니다. `src/libcamera/base/event_dispatcher_poll.cpp:177`
11. `Private` 가 `Thread::wait()` 를 호출합니다. `src/libcamera/camera_manager.cpp:64`
12. `Thread` 가 `MutexLocker::MutexLocker()` 를 호출합니다. `src/libcamera/base/thread.cpp:407`
13. `Thread` 가 `ConditionVariable::wait()` 를 호출합니다. `src/libcamera/base/thread.cpp:414`
14. `Thread` 가 `(lambda at /home/baboess/work/libcamera-ab-validation-20260921/b/source/src/libcamera/base/thread.cpp:409:21)::(lambda at /home/baboess/work/libcamera-ab-validation-20260921/b/source/src/libcamera/base/thread.cpp:409:21)()` 를 호출합니다. `src/libcamera/base/thread.cpp:414`
15. `Thread` 가 `ConditionVariable::wait_for()` 를 호출합니다. `src/libcamera/base/thread.cpp:416`
16. `Thread` 가 `(lambda at /home/baboess/work/libcamera-ab-validation-20260921/b/source/src/libcamera/base/thread.cpp:409:21)::(lambda at /home/baboess/work/libcamera-ab-validation-20260921/b/source/src/libcamera/base/thread.cpp:409:21)()` 를 호출합니다. `src/libcamera/base/thread.cpp:417`

표시에서 뺀 호출이 17 개 있습니다. `config/scenarios.yaml` 의 `hide` 규칙에 걸린 로깅과 접근자 호출이며, `facts.json` 에는 그대로 남아 있습니다.

## 이 흐름에서 확인할 것

`CameraManager::start()` 진입점에서 스레드 생성과 동기화 로직이 어떻게 분기하는지 확인하려면 먼저 `src/libcamera/camera_manager.cpp:342` 의 호출 경로를 추적해야 합니다. `Private::start()` 가 `Thread::start()` 를 통해 스레드를 시작하지만, `Thread::setThreadAffinityInternal()` 와 같은 초기화 작업은 정적 분석으로 실행 순서를 확정하기 어렵습니다.

스레드 내부의 대기 및 인터럽트 처리 흐름을 파악하려면 `src/libcamera/base/thread.cpp:264` 의 `startThread()` 호출과 `src/libcamera/camera_manager.cpp:55` 의 `ConditionVariable::wait()` 를 확인해야 합니다. `EventDispatcherPoll::interrupt()` 가 가상 함수이므로 현재 구현 하나만 존재하며, `src/libcamera/base/event_dispatcher_poll.cpp:177` 의 `UniqueFD::get()` 호출은 파일 디스크립터 관리와 직접적인 관련이 없습니다.

`Thread::wait()` 와 `ConditionVariable::wait_for()` 사이의 콜백 전달과 스레드 종료 시점의 정확한 순서는 현재 사실 목록에 근거가 부족합니다. `src/libcamera/base/thread.cpp:414` 의 람다 호출과 `src/libcamera/camera_manager.cpp:63` 의 `Thread::exit()` 호출이 어떻게 상호작용하는지 확인해야 합니다.

확인 필요: 메서드를 인자로 넘겨 예약한 호출이 1 개 있습니다. 위에서 `예약된 호출, 실행 순서는 정적으로 확인 불가` 로 표시한 단계가 그 자리입니다. 대상 메서드는 확인했지만, 실제 실행 시점과 스레드는 큐나 신호 구현이 정하므로 이 번호 목록은 그 지점 이후의 순서를 보장하지 않습니다. 이후 흐름은 예약을 받는 쪽의 구현에서 직접 확인해야 합니다.

??? note "근거와 검토 정보"
    - 근거 파일: `src/libcamera/base/event_dispatcher_poll.cpp`, `src/libcamera/base/thread.cpp`, `src/libcamera/camera_manager.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `279d355ef8`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토: 2026-09-24 · ollama/qwen3.5:4b · 사람 검토 전

다음 단계: [스트림 구성 (Camera::configure)](configure.md)
