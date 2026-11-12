---
generated_at: 2026-11-04 07:00:44+00:00
source_commit: da6a6ed33ed0ab305f10b6f8b44736150d39cef4
status: ok
section: scenario-manager_start
generation_method: facts-and-llm
scenario_id: manager_start
entry: CameraManager::start()
scenario_fingerprint: cd1259592467fd5fcd35810d789ea55d2db35418700286e14384affaabeacf99
evidence_fingerprint: 1fefde07c0253f8851e4ddf5e61fcf8442f556340361f7e220f93106c84cb8bf
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design:
  schema: 1
  input_fingerprint: 1fefde07c0253f8851e4ddf5e61fcf8442f556340361f7e220f93106c84cb8bf
  answers:
    discovery:
    - text: '`CameraManager::start()`는 카메라 관리자를 시작하고 시스템의 모든 장치를 열거합니다.'
      evidence:
      - api
      covers:
      - discovery
      kind: behavior
      quote: "\\brief Start the camera manager\n *\n * Start the camera manager and\
        \ enumerate all devices in the system. Once\n * the start has been confirmed\
        \ the user is free to list and otherwise\n * interact with cameras in the\
        \ system until either the camera manager\n * is stopped or the camera is unplugged\
        \ from the system.\n *\n * \\return 0 on success or a negative error code\
        \ otherwise\n */"
      part_id: answer
    - text: 시작이 확인되면 사용자는 관리자가 중지되거나 카메라가 시스템에서 분리될 때까지 시스템의 카메라 목록을 확인하고 카메라와 상호작용할
        수 있습니다.
      evidence:
      - api
      covers:
      - discovery
      kind: behavior
      quote: "\\brief Start the camera manager\n *\n * Start the camera manager and\
        \ enumerate all devices in the system. Once\n * the start has been confirmed\
        \ the user is free to list and otherwise\n * interact with cameras in the\
        \ system until either the camera manager\n * is stopped or the camera is unplugged\
        \ from the system.\n *\n * \\return 0 on success or a negative error code\
        \ otherwise\n */"
      part_id: answer
    initialization:
    - text: '`CameraManager::Private::start()`는 `Thread::start()`로 스레드를 시작하고 `initialized_`가
        참이 될 때까지 기다린 뒤 `status_`를 복사합니다. 복사한 상태가 음수이면 `exit()`와 `wait()`를 차례로 호출하고
        그 상태를 반환하며, 그렇지 않으면 0을 반환합니다.'
      evidence:
      - start
      covers:
      - initialization
      kind: behavior
      quote: "{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
        \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t}"
      part_id: answer
    - text: '`CameraManager::Private::run()`은 `init()`의 반환값을 `ret`에 저장하고 `mutex_`를
        잠근 상태에서 `status_`에 복사한 뒤 `initialized_`를 참으로 설정합니다. `mutex_.unlock()`이 끝난
        뒤 `cv_.notify_one()`을 호출합니다. `ret`이 음수이면 `cleanup()`을 호출하고 반환하며, 그렇지 않으면 `exec()`를
        호출한 뒤 `cleanup()`을 호출합니다.'
      evidence:
      - run
      covers:
      - initialization
      kind: behavior
      quote: "mutex_.lock();\n\tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\
        \tcv_.notify_one();"
      part_id: answer
    - text: '`CameraManager::Private::init()`은 `IPAManager`를 만든 뒤 `DeviceEnumerator::create()`로
        `enumerator_`를 생성합니다. 생성에 실패하거나 `enumerate()`가 실패하면 `-ENODEV`를 반환합니다. 그렇지
        않으면 `createPipelineHandlers()`를 호출하고 `devicesAdded`를 `Private::createPipelineHandlers`에
        연결한 뒤 0을 반환합니다.'
      evidence:
      - init
      covers:
      - initialization
      kind: behavior
      quote: "enumerator_ = DeviceEnumerator::create();\n\tif (!enumerator_ || enumerator_->enumerate())\n\
        \t\treturn -ENODEV;"
      part_id: answer
  topic_inputs:
    discovery: 7ee6b373f4fb6b5e7ff2a096a50399157eccfb38ee5eb59e2b405efb1dd12c74
    initialization: 83dfc5adf11378e7426a78af0376103a8e7aa5948f5e5abdfbf21f4549aae081
  reused_topics:
  - discovery
  - initialization
  replayed_units: []
  generated_topics: []
  topic_agents:
    discovery: cli/codex/gpt-6.1-terra
    initialization: cli/codex/gpt-6.1-terra
  grounding_review: passed
  grounding_policy: 3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2
  validation_policy:
    manuscript: 367d18b95f8f0d01a15ae0f4d1b70f7e13e4d0298df4215e2c449ac4905db6f9
    semantic: 571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968
    duplicates: 93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38
    design_contracts: 9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0
    validate: 78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372
    reader_profiles: ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797
    contract_schema: 2f593eec0430a4e6b5822e642c0a7a1227fc150a0b27d8a71f521acf93b6439e
    answer_contracts: 1e0d24e0cf26ded53ecec2e5a6fbc51836bac6e17530318a9fa7cffaa936c00b
    reader_scope: 1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782
    product_context: 050c20aa2fdcceae10c6275fbb5f850f616ab5051bb67ccbcb4a204877a238d9
    design_response: deb70dda7ad27f001267e4a9712c5b0dc1fe9fa67acd13bedbfefaaad0ad83c8
    design_validation: 0613b830b96fd2828171dea499807c3366edd72208ed814a95e5228dd106dd73
  validation_model: 75b09aab91bfc2ad01f4821a947e107eb89f20ad987768c44ec40e9d0a83349d
  style_policy:
    fluent-korean.md: ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975
    i-have-adhd.md: 3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9
    README.md: b87a84b1bc31079837dc4dc4527ce02c9dc2cbc3a26ff7e99e0872941d213995
  reuse_lineage:
    source_commit: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61
    body_sha256: e47405ac416483923891feb0a8217bced2f13e4719333e20c28fa2eff7f0d86e
    topics:
    - discovery
    - initialization
    validation: current source, contract and editorial checks; human review pending
  body_sha256: 93b00b14dcd75a3aa5b336a9850d1710df98b41238d30b632e552baaee0857ed
generated_visuals:
  schema: 1
  records:
    manager-start-wait-result:
      input_fingerprint: 0322dd343cd68d35306dc9744118c0c9d6c4981694cf9773040adf7711d24a15
      draft:
        nodes:
        - id: entry
          symbol: CameraManager::Private::start
          label: CameraManager::Private::start는 스레드 초기화를 기다린 뒤 결과를 반환합니다.
          label_en: CameraManager::Private::start waits for thread initialization
            and returns a result.
          shape: box
          quote_ids:
          - start:0
        - id: thread_start
          symbol: Thread::start
          label: Thread::start를 호출해 스레드를 시작합니다.
          label_en: It calls Thread::start to start the thread.
          shape: process
          quote_ids:
          - start:0
        - id: wait_init
          symbol: cv_
          label: MutexLocker로 mutex_를 잠그고 initialized_가 참이 될 때까지 cv_에서 기다립니다.
          label_en: It locks mutex_ with MutexLocker and waits on cv_ until initialized_
            is true.
          shape: process
          quote_ids:
          - start:0
        - id: copy_status
          symbol: status_
          label: status_를 지역 변수 status에 복사한 뒤 잠금 범위를 끝냅니다.
          label_en: It copies status_ to local status and leaves the lock scope.
          shape: process
          quote_ids:
          - start:0
        - id: check_status
          symbol: status
          label: status가 0보다 작습니까?
          label_en: Is status less than 0?
          shape: decision
          quote_ids:
          - start:0
        - id: stop
          symbol: exit
          label: exit()를 호출해 스레드 종료를 요청합니다.
          label_en: It calls exit() to request thread termination.
          shape: process
          quote_ids:
          - start:0
        - id: join
          symbol: wait
          label: wait()를 호출해 스레드가 끝나기를 기다립니다.
          label_en: It calls wait() to wait for the thread to finish.
          shape: process
          quote_ids:
          - start:0
        - id: return_failure
          symbol: return
          label: 복사한 실패 상태 status를 반환합니다.
          label_en: It returns the copied failure status.
          shape: box
          quote_ids:
          - start:0
        - id: return_success
          symbol: return
          label: 성공을 뜻하는 0을 반환합니다.
          label_en: It returns 0 for success.
          shape: box
          quote_ids:
          - start:0
        edges:
        - from: entry
          to: thread_start
          label: start가 Thread::start를 호출합니다.
          label_en: start calls Thread::start.
          condition_ref: always
          quote_ids:
          - start:0
        - from: thread_start
          to: wait_init
          label: Thread::start가 정상 복귀하면 초기화를 기다립니다.
          label_en: After Thread::start returns normally, it waits for initialization.
          condition_ref: always
          quote_ids:
          - start:0
        - from: wait_init
          to: copy_status
          label: 대기가 끝나면 status_를 복사합니다.
          label_en: After the wait, it copies status_.
          condition_ref: always
          quote_ids:
          - start:0
        - from: copy_status
          to: check_status
          label: 잠금 범위를 끝낸 뒤 status를 확인합니다.
          label_en: After leaving the lock scope, it checks status.
          condition_ref: always
          quote_ids:
          - start:0
        - from: check_status
          to: stop
          label: 조건이 참이면 exit()를 호출합니다.
          label_en: If the condition is true, it calls exit().
          condition_ref: c1:true
          quote_ids:
          - start:0
        - from: stop
          to: join
          label: exit()가 정상 복귀하면 wait()를 호출합니다.
          label_en: After exit() returns normally, it calls wait().
          condition_ref: always
          quote_ids:
          - start:0
        - from: join
          to: return_failure
          label: wait()가 정상 복귀하면 status를 반환합니다.
          label_en: After wait() returns normally, it returns status.
          condition_ref: always
          quote_ids:
          - start:0
        - from: check_status
          to: return_success
          label: 조건이 거짓이면 0을 반환합니다.
          label_en: If the condition is false, it returns 0.
          condition_ref: c1:false
          quote_ids:
          - start:0
      graph:
        id: manager-start-wait-result
        topic: initialization
        kind: flow
        title: 시작 호출자의 초기화 대기와 반환
        question: Private::start는 스레드 초기화 결과를 어떻게 기다리고 실패 또는 성공을 반환합니까?
        condition_display: inline
        nodes:
        - id: entry
          label: CameraManager::Private::start는 스레드 초기화를 기다린 뒤 결과를 반환합니다.
          label_en: CameraManager::Private::start waits for thread initialization
            and returns a result.
          shape: box
          evidence:
          - source: initialization/start
            sha256: 89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7
            quote: "int CameraManager::Private::start()\n{\n\tint status;\n\n\t/*\
              \ Start the thread and wait for initialization to complete. */\n\tThread::start();\n\
              \n\t{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
              \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t\
              }\n\n\t/* If a failure happened during initialization, stop the thread.\
              \ */\n\tif (status < 0) {\n\t\texit();\n\t\twait();\n\t\treturn status;\n\
              \t}\n\n\treturn 0;\n}"
        - id: thread_start
          label: Thread::start를 호출해 스레드를 시작합니다.
          label_en: It calls Thread::start to start the thread.
          shape: box
          evidence:
          - source: initialization/start
            sha256: 89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7
            quote: "int CameraManager::Private::start()\n{\n\tint status;\n\n\t/*\
              \ Start the thread and wait for initialization to complete. */\n\tThread::start();\n\
              \n\t{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
              \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t\
              }\n\n\t/* If a failure happened during initialization, stop the thread.\
              \ */\n\tif (status < 0) {\n\t\texit();\n\t\twait();\n\t\treturn status;\n\
              \t}\n\n\treturn 0;\n}"
        - id: wait_init
          label: MutexLocker로 mutex_를 잠그고 initialized_가 참이 될 때까지 cv_에서 기다립니다.
          label_en: It locks mutex_ with MutexLocker and waits on cv_ until initialized_
            is true.
          shape: box
          evidence:
          - source: initialization/start
            sha256: 89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7
            quote: "int CameraManager::Private::start()\n{\n\tint status;\n\n\t/*\
              \ Start the thread and wait for initialization to complete. */\n\tThread::start();\n\
              \n\t{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
              \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t\
              }\n\n\t/* If a failure happened during initialization, stop the thread.\
              \ */\n\tif (status < 0) {\n\t\texit();\n\t\twait();\n\t\treturn status;\n\
              \t}\n\n\treturn 0;\n}"
        - id: copy_status
          label: status_를 지역 변수 status에 복사한 뒤 잠금 범위를 끝냅니다.
          label_en: It copies status_ to local status and leaves the lock scope.
          shape: box
          evidence:
          - source: initialization/start
            sha256: 89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7
            quote: "int CameraManager::Private::start()\n{\n\tint status;\n\n\t/*\
              \ Start the thread and wait for initialization to complete. */\n\tThread::start();\n\
              \n\t{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
              \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t\
              }\n\n\t/* If a failure happened during initialization, stop the thread.\
              \ */\n\tif (status < 0) {\n\t\texit();\n\t\twait();\n\t\treturn status;\n\
              \t}\n\n\treturn 0;\n}"
        - id: check_status
          label: status가 0보다 작습니까?
          label_en: Is status less than 0?
          shape: decision
          evidence:
          - source: initialization/start
            sha256: 89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7
            quote: "int CameraManager::Private::start()\n{\n\tint status;\n\n\t/*\
              \ Start the thread and wait for initialization to complete. */\n\tThread::start();\n\
              \n\t{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
              \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t\
              }\n\n\t/* If a failure happened during initialization, stop the thread.\
              \ */\n\tif (status < 0) {\n\t\texit();\n\t\twait();\n\t\treturn status;\n\
              \t}\n\n\treturn 0;\n}"
        - id: stop
          label: exit()를 호출해 스레드 종료를 요청합니다.
          label_en: It calls exit() to request thread termination.
          shape: box
          evidence:
          - source: initialization/start
            sha256: 89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7
            quote: "int CameraManager::Private::start()\n{\n\tint status;\n\n\t/*\
              \ Start the thread and wait for initialization to complete. */\n\tThread::start();\n\
              \n\t{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
              \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t\
              }\n\n\t/* If a failure happened during initialization, stop the thread.\
              \ */\n\tif (status < 0) {\n\t\texit();\n\t\twait();\n\t\treturn status;\n\
              \t}\n\n\treturn 0;\n}"
        - id: join
          label: wait()를 호출해 스레드가 끝나기를 기다립니다.
          label_en: It calls wait() to wait for the thread to finish.
          shape: box
          evidence:
          - source: initialization/start
            sha256: 89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7
            quote: "int CameraManager::Private::start()\n{\n\tint status;\n\n\t/*\
              \ Start the thread and wait for initialization to complete. */\n\tThread::start();\n\
              \n\t{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
              \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t\
              }\n\n\t/* If a failure happened during initialization, stop the thread.\
              \ */\n\tif (status < 0) {\n\t\texit();\n\t\twait();\n\t\treturn status;\n\
              \t}\n\n\treturn 0;\n}"
        - id: return_failure
          label: 복사한 실패 상태 status를 반환합니다.
          label_en: It returns the copied failure status.
          shape: box
          evidence:
          - source: initialization/start
            sha256: 89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7
            quote: "int CameraManager::Private::start()\n{\n\tint status;\n\n\t/*\
              \ Start the thread and wait for initialization to complete. */\n\tThread::start();\n\
              \n\t{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
              \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t\
              }\n\n\t/* If a failure happened during initialization, stop the thread.\
              \ */\n\tif (status < 0) {\n\t\texit();\n\t\twait();\n\t\treturn status;\n\
              \t}\n\n\treturn 0;\n}"
        - id: return_success
          label: 성공을 뜻하는 0을 반환합니다.
          label_en: It returns 0 for success.
          shape: box
          evidence:
          - source: initialization/start
            sha256: 89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7
            quote: "int CameraManager::Private::start()\n{\n\tint status;\n\n\t/*\
              \ Start the thread and wait for initialization to complete. */\n\tThread::start();\n\
              \n\t{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
              \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t\
              }\n\n\t/* If a failure happened during initialization, stop the thread.\
              \ */\n\tif (status < 0) {\n\t\texit();\n\t\twait();\n\t\treturn status;\n\
              \t}\n\n\treturn 0;\n}"
        edges:
        - from: entry
          to: thread_start
          label: start가 Thread::start를 호출합니다.
          label_en: start calls Thread::start.
          evidence:
          - source: initialization/start
            sha256: 89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7
            quote: "int CameraManager::Private::start()\n{\n\tint status;\n\n\t/*\
              \ Start the thread and wait for initialization to complete. */\n\tThread::start();\n\
              \n\t{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
              \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t\
              }\n\n\t/* If a failure happened during initialization, stop the thread.\
              \ */\n\tif (status < 0) {\n\t\texit();\n\t\twait();\n\t\treturn status;\n\
              \t}\n\n\treturn 0;\n}"
        - from: thread_start
          to: wait_init
          label: Thread::start가 정상 복귀하면 초기화를 기다립니다.
          label_en: After Thread::start returns normally, it waits for initialization.
          evidence:
          - source: initialization/start
            sha256: 89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7
            quote: "int CameraManager::Private::start()\n{\n\tint status;\n\n\t/*\
              \ Start the thread and wait for initialization to complete. */\n\tThread::start();\n\
              \n\t{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
              \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t\
              }\n\n\t/* If a failure happened during initialization, stop the thread.\
              \ */\n\tif (status < 0) {\n\t\texit();\n\t\twait();\n\t\treturn status;\n\
              \t}\n\n\treturn 0;\n}"
        - from: wait_init
          to: copy_status
          label: 대기가 끝나면 status_를 복사합니다.
          label_en: After the wait, it copies status_.
          evidence:
          - source: initialization/start
            sha256: 89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7
            quote: "int CameraManager::Private::start()\n{\n\tint status;\n\n\t/*\
              \ Start the thread and wait for initialization to complete. */\n\tThread::start();\n\
              \n\t{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
              \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t\
              }\n\n\t/* If a failure happened during initialization, stop the thread.\
              \ */\n\tif (status < 0) {\n\t\texit();\n\t\twait();\n\t\treturn status;\n\
              \t}\n\n\treturn 0;\n}"
        - from: copy_status
          to: check_status
          label: 잠금 범위를 끝낸 뒤 status를 확인합니다.
          label_en: After leaving the lock scope, it checks status.
          evidence:
          - source: initialization/start
            sha256: 89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7
            quote: "int CameraManager::Private::start()\n{\n\tint status;\n\n\t/*\
              \ Start the thread and wait for initialization to complete. */\n\tThread::start();\n\
              \n\t{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
              \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t\
              }\n\n\t/* If a failure happened during initialization, stop the thread.\
              \ */\n\tif (status < 0) {\n\t\texit();\n\t\twait();\n\t\treturn status;\n\
              \t}\n\n\treturn 0;\n}"
        - from: check_status
          to: stop
          label: 조건이 참이면 exit()를 호출합니다. · status < 0 [true]
          label_en: If the condition is true, it calls exit(). · status < 0 [true]
          evidence:
          - source: initialization/start
            sha256: 89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7
            quote: "int CameraManager::Private::start()\n{\n\tint status;\n\n\t/*\
              \ Start the thread and wait for initialization to complete. */\n\tThread::start();\n\
              \n\t{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
              \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t\
              }\n\n\t/* If a failure happened during initialization, stop the thread.\
              \ */\n\tif (status < 0) {\n\t\texit();\n\t\twait();\n\t\treturn status;\n\
              \t}\n\n\treturn 0;\n}"
        - from: stop
          to: join
          label: exit()가 정상 복귀하면 wait()를 호출합니다.
          label_en: After exit() returns normally, it calls wait().
          evidence:
          - source: initialization/start
            sha256: 89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7
            quote: "int CameraManager::Private::start()\n{\n\tint status;\n\n\t/*\
              \ Start the thread and wait for initialization to complete. */\n\tThread::start();\n\
              \n\t{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
              \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t\
              }\n\n\t/* If a failure happened during initialization, stop the thread.\
              \ */\n\tif (status < 0) {\n\t\texit();\n\t\twait();\n\t\treturn status;\n\
              \t}\n\n\treturn 0;\n}"
        - from: join
          to: return_failure
          label: wait()가 정상 복귀하면 status를 반환합니다.
          label_en: After wait() returns normally, it returns status.
          evidence:
          - source: initialization/start
            sha256: 89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7
            quote: "int CameraManager::Private::start()\n{\n\tint status;\n\n\t/*\
              \ Start the thread and wait for initialization to complete. */\n\tThread::start();\n\
              \n\t{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
              \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t\
              }\n\n\t/* If a failure happened during initialization, stop the thread.\
              \ */\n\tif (status < 0) {\n\t\texit();\n\t\twait();\n\t\treturn status;\n\
              \t}\n\n\treturn 0;\n}"
        - from: check_status
          to: return_success
          label: 조건이 거짓이면 0을 반환합니다. · status < 0 [false]
          label_en: If the condition is false, it returns 0. · status < 0 [false]
          evidence:
          - source: initialization/start
            sha256: 89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7
            quote: "int CameraManager::Private::start()\n{\n\tint status;\n\n\t/*\
              \ Start the thread and wait for initialization to complete. */\n\tThread::start();\n\
              \n\t{\n\t\tMutexLocker locker(mutex_);\n\t\tcv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_)\
              \ {\n\t\t\treturn initialized_;\n\t\t});\n\t\tstatus = status_;\n\t\
              }\n\n\t/* If a failure happened during initialization, stop the thread.\
              \ */\n\tif (status < 0) {\n\t\texit();\n\t\twait();\n\t\treturn status;\n\
              \t}\n\n\treturn 0;\n}"
        producer: cli/codex/gpt-6.1-terra
      producer: cli/codex/gpt-6.1-terra
      generation_commit: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61
      citation_binding_policy: identifier-boundaries-v1
      reused: true
      citation_binding_revalidation:
        policy: identifier-and-guard-boundaries-v2
        original_input_fingerprint: 0322dd343cd68d35306dc9744118c0c9d6c4981694cf9773040adf7711d24a15
        new_inference: false
    manager-run-notify-before-branch:
      input_fingerprint: 18062c7353d76b4a4be24605b12763c79995a1e680f2310811a1faa164a37075
      draft:
        nodes:
        - id: init
          symbol: init
          label: run은 init()의 반환값을 ret에 저장합니다.
          label_en: run stores the return value of init() in ret.
          shape: process
          quote_ids:
          - run:0
        - id: lock
          symbol: lock
          label: run은 mutex_를 잠급니다.
          label_en: run locks mutex_.
          shape: process
          quote_ids:
          - run:0
        - id: status
          symbol: status_
          label: run은 status_에 ret을 저장하고 initialized_를 true로 설정합니다.
          label_en: run stores ret in status_ and sets initialized_ to true.
          shape: process
          quote_ids:
          - run:0
        - id: unlock
          symbol: unlock
          label: run은 mutex_의 잠금을 풉니다.
          label_en: run unlocks mutex_.
          shape: process
          quote_ids:
          - run:0
        - id: notify
          symbol: notify_one
          label: run은 cv_.notify_one()을 호출해 알립니다.
          label_en: run signals by calling cv_.notify_one().
          shape: process
          quote_ids:
          - run:0
        - id: branch
          symbol: if
          label: ret이 0보다 작습니까?
          label_en: Is ret less than 0?
          shape: decision
          quote_ids:
          - run:0
        - id: failure_cleanup
          symbol: cleanup
          label: run은 cleanup()을 호출합니다. init()이 enumerator_를 null로 남길 수 있지만 cleanup()은
            이를 역참조합니다.
          label_en: run calls cleanup(); init() can leave enumerator_ null, which
            cleanup() dereferences.
          shape: process
          quote_ids:
          - run:0
          - init:0
          - cleanup:0
        - id: failure_return
          symbol: return
          label: cleanup()이 정상 복귀하면 run은 반환합니다.
          label_en: If cleanup() returns normally, run returns.
          shape: box
          quote_ids:
          - run:0
        - id: exec
          symbol: exec
          label: run은 exec()를 호출해 이벤트와 메시지 처리를 시작합니다.
          label_en: run calls exec() to start processing events and messages.
          shape: process
          quote_ids:
          - run:0
        - id: success_cleanup
          symbol: cleanup
          label: run은 cleanup()을 호출합니다. cleanup()이 정상 복귀하면 run이 끝납니다.
          label_en: run calls cleanup(). If cleanup() returns normally, run ends.
          shape: process
          quote_ids:
          - run:0
        edges:
        - from: init
          to: lock
          label: init()이 반환한 뒤 잠급니다.
          label_en: run locks after init() returns.
          condition_ref: always
          quote_ids:
          - run:0
        - from: lock
          to: status
          label: 잠근 뒤 값을 설정합니다.
          label_en: run sets the values after locking.
          condition_ref: always
          quote_ids:
          - run:0
        - from: status
          to: unlock
          label: 값을 설정한 뒤 잠금을 풉니다.
          label_en: run unlocks after setting the values.
          condition_ref: always
          quote_ids:
          - run:0
        - from: unlock
          to: notify
          label: 잠금을 푼 뒤 알립니다.
          label_en: run signals after unlocking.
          condition_ref: always
          quote_ids:
          - run:0
        - from: notify
          to: branch
          label: 알린 뒤 조건을 검사합니다.
          label_en: run checks the condition after signaling.
          condition_ref: always
          quote_ids:
          - run:0
        - from: branch
          to: failure_cleanup
          label: 조건이 참이면 cleanup()을 호출합니다.
          label_en: If the condition is true, run calls cleanup().
          condition_ref: c1:true
          quote_ids:
          - run:0
        - from: failure_cleanup
          to: failure_return
          label: cleanup()이 정상 복귀하면 반환합니다.
          label_en: If cleanup() returns normally, run returns.
          condition_ref: always
          quote_ids:
          - run:0
        - from: branch
          to: exec
          label: 조건이 거짓이면 exec()를 호출합니다.
          label_en: If the condition is false, run calls exec().
          condition_ref: c1:false
          quote_ids:
          - run:0
        - from: exec
          to: success_cleanup
          label: exec()가 정상 복귀하면 cleanup()을 호출합니다.
          label_en: If exec() returns normally, run calls cleanup().
          condition_ref: always
          quote_ids:
          - run:0
      graph:
        id: manager-run-notify-before-branch
        topic: initialization
        kind: flow
        title: 관리자 스레드의 알림과 정리
        question: run은 초기화 결과를 저장하고 알린 뒤 언제 정리하고 언제 이벤트 처리를 시작합니까?
        condition_display: inline
        nodes:
        - id: init
          label: run은 init()의 반환값을 ret에 저장합니다.
          label_en: run stores the return value of init() in ret.
          shape: box
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        - id: lock
          label: run은 mutex_를 잠급니다.
          label_en: run locks mutex_.
          shape: box
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        - id: status
          label: run은 status_에 ret을 저장하고 initialized_를 true로 설정합니다.
          label_en: run stores ret in status_ and sets initialized_ to true.
          shape: box
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        - id: unlock
          label: run은 mutex_의 잠금을 풉니다.
          label_en: run unlocks mutex_.
          shape: box
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        - id: notify
          label: run은 cv_.notify_one()을 호출해 알립니다.
          label_en: run signals by calling cv_.notify_one().
          shape: box
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        - id: branch
          label: ret이 0보다 작습니까?
          label_en: Is ret less than 0?
          shape: decision
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        - id: failure_cleanup
          label: run은 cleanup()을 호출합니다. init()이 enumerator_를 null로 남길 수 있지만 cleanup()은
            이를 역참조합니다.
          label_en: run calls cleanup(); init() can leave enumerator_ null, which
            cleanup() dereferences.
          shape: box
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
          - source: initialization/init
            sha256: 8e85184e2eacbf523477a4c87d878c17069fa18f3358f39501fcaaca8e3dbffe
            quote: "int CameraManager::Private::init()\n{\n\tCameraManager *const\
              \ o = LIBCAMERA_O_PTR();\n\tipaManager_ = std::make_unique<IPAManager>(*o);\n\
              \n\tenumerator_ = DeviceEnumerator::create();\n\tif (!enumerator_ ||\
              \ enumerator_->enumerate())\n\t\treturn -ENODEV;\n\n\tcreatePipelineHandlers();\n\
              \tenumerator_->devicesAdded.connect(this, &Private::createPipelineHandlers);\n\
              \n\treturn 0;\n}"
          - source: initialization/cleanup
            sha256: 013ef95052c9ca394b4c18cb59a7c9c53873cfb4efe8d23138bd1f2ae1007bfa
            quote: "void CameraManager::Private::cleanup()\n{\n\tenumerator_->devicesAdded.disconnect(this);\n\
              \n\t/*\n\t * Release all references to cameras to ensure they all get\
              \ destroyed\n\t * before the device enumerator deletes the media devices.\
              \ Cameras are\n\t * destroyed via Object::deleteLater() API, hence we\
              \ need to explicitly\n\t * process deletion requests from the thread's\
              \ message queue as the event\n\t * loop is not in action here.\n\t */\n\
              \t{\n\t\tMutexLocker locker(mutex_);\n\t\tcameras_.clear();\n\t}\n\n\
              \tdispatchMessages(Message::Type::DeferredDelete);\n\n\tenumerator_.reset(nullptr);\n\
              }"
        - id: failure_return
          label: cleanup()이 정상 복귀하면 run은 반환합니다.
          label_en: If cleanup() returns normally, run returns.
          shape: box
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        - id: exec
          label: run은 exec()를 호출해 이벤트와 메시지 처리를 시작합니다.
          label_en: run calls exec() to start processing events and messages.
          shape: box
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        - id: success_cleanup
          label: run은 cleanup()을 호출합니다. cleanup()이 정상 복귀하면 run이 끝납니다.
          label_en: run calls cleanup(). If cleanup() returns normally, run ends.
          shape: box
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        edges:
        - from: init
          to: lock
          label: init()이 반환한 뒤 잠급니다.
          label_en: run locks after init() returns.
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        - from: lock
          to: status
          label: 잠근 뒤 값을 설정합니다.
          label_en: run sets the values after locking.
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        - from: status
          to: unlock
          label: 값을 설정한 뒤 잠금을 풉니다.
          label_en: run unlocks after setting the values.
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        - from: unlock
          to: notify
          label: 잠금을 푼 뒤 알립니다.
          label_en: run signals after unlocking.
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        - from: notify
          to: branch
          label: 알린 뒤 조건을 검사합니다.
          label_en: run checks the condition after signaling.
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        - from: branch
          to: failure_cleanup
          label: 조건이 참이면 cleanup()을 호출합니다. · ret < 0 [true]
          label_en: If the condition is true, run calls cleanup(). · ret < 0 [true]
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        - from: failure_cleanup
          to: failure_return
          label: cleanup()이 정상 복귀하면 반환합니다.
          label_en: If cleanup() returns normally, run returns.
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        - from: branch
          to: exec
          label: 조건이 거짓이면 exec()를 호출합니다. · ret < 0 [false]
          label_en: If the condition is false, run calls exec(). · ret < 0 [false]
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        - from: exec
          to: success_cleanup
          label: exec()가 정상 복귀하면 cleanup()을 호출합니다.
          label_en: If exec() returns normally, run calls cleanup().
          evidence:
          - source: initialization/run
            sha256: 99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa
            quote: "void CameraManager::Private::run()\n{\n\tLOG(Camera, Debug) <<\
              \ \"Starting camera manager\";\n\n\tint ret = init();\n\n\tmutex_.lock();\n\
              \tstatus_ = ret;\n\tinitialized_ = true;\n\tmutex_.unlock();\n\tcv_.notify_one();\n\
              \n\tif (ret < 0) {\n\t\tcleanup();\n\t\treturn;\n\t}\n\n\t/* Now start\
              \ processing events and messages. */\n\texec();\n\n\tcleanup();\n}"
        producer: cli/codex/gpt-6.1-terra
      producer: cli/codex/gpt-6.1-terra
      generation_commit: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61
      citation_binding_policy: identifier-boundaries-v1
      reused: true
      citation_binding_revalidation:
        policy: identifier-and-guard-boundaries-v2
        original_input_fingerprint: 18062c7353d76b4a4be24605b12763c79995a1e680f2310811a1faa164a37075
        new_inference: false
  body_sha256: 93b00b14dcd75a3aa5b336a9850d1710df98b41238d30b632e552baaee0857ed
revalidated_from: c19d05128f3ae1f0ebe63acb4deaca9fbb1dde78
---

# 카메라 탐색

**관리자 시작의 성공·실패를 확인한 뒤 탐색된 카메라를 사용하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| <a id="이-흐름에서-확인할-것"></a>관리자 시작의 성공·실패를 확인한 뒤 탐색된 카메라를 사용하세요. | [탐색을 시작하고 카메라를 사용할 시점](#탐색을-시작하고-카메라를-사용할-시점) |

## 탐색을 시작하고 카메라를 사용할 시점

`CameraManager::start()`는 카메라 관리자를 시작하고 시스템의 모든 장치를 열거합니다. 시작이 확인되면 사용자는 관리자가 중지되거나 카메라가 시스템에서 분리될 때까지 시스템의 카메라 목록을 확인하고 카메라와 상호작용할 수 있습니다. `src/libcamera/camera_manager.cpp:329`

근거 원문: [src/libcamera/camera_manager.cpp:329](#source-027ec5bea3fe0dfa)

## 관리자 스레드의 초기화와 실패 처리

`CameraManager::Private::start()`는 `Thread::start()`로 스레드를 시작하고 `initialized_`가 참이 될 때까지 기다린 뒤 `status_`를 복사합니다. 복사한 상태가 음수이면 `exit()`와 `wait()`를 차례로 호출하고 그 상태를 반환하며, 그렇지 않으면 0을 반환합니다. `src/libcamera/camera_manager.cpp:46`

<!-- sdd:visual:manager-start-wait-result -->
### 시작 호출자의 초기화 대기와 반환

```mermaid
flowchart TB
%% sdd:translations {"CameraManager::Private::<br/>start는 스레드 초기화를 <br/>기다린 뒤 결과를 반환합니다.": "CameraManager::Private::<br/>start waits for thread <br/>initialization and returns <br/>a result.", "MutexLocker로 mutex#95;를 <br/>잠그고 initialized#95;가 참이 <br/>될 때까지 cv#95;에서 <br/>기다립니다.": "It locks mutex#95; with <br/>MutexLocker and waits on <br/>cv#95; until initialized#95; is <br/>true.", "Thread::start가 정상 <br/>복귀하면 초기화를 <br/>기다립니다.": "After Thread::start returns <br/>normally, it waits for <br/>initialization.", "Thread::start를 호출해 <br/>스레드를 시작합니다.": "It calls Thread::start to <br/>start the thread.", "exit#40;#41;가 정상 복귀하면 <br/>wait#40;#41;를 호출합니다.": "After exit#40;#41; returns <br/>normally, it calls wait#40;#41;.", "exit#40;#41;를 호출해 스레드 <br/>종료를 요청합니다.": "It calls exit#40;#41; to request <br/>thread termination.", "start가 Thread::start를 <br/>호출합니다.": "start calls Thread::start.", "status#95;를 지역 변수 <br/>status에 복사한 뒤 잠금 <br/>범위를 끝냅니다.": "It copies status#95; to local <br/>status and leaves the lock <br/>scope.", "status가 0보다 작습니까?": "Is status less than 0?", "wait#40;#41;가 정상 복귀하면 <br/>status를 반환합니다.": "After wait#40;#41; returns <br/>normally, it returns status.", "wait#40;#41;를 호출해 스레드가 <br/>끝나기를 기다립니다.": "It calls wait#40;#41; to wait for <br/>the thread to finish.", "대기가 끝나면 status#95;를 <br/>복사합니다.": "After the wait, it copies <br/>status#95;.", "복사한 실패 상태 status를 <br/>반환합니다.": "It returns the copied <br/>failure status.", "성공을 뜻하는 0을 <br/>반환합니다.": "It returns 0 for success.", "잠금 범위를 끝낸 뒤 <br/>status를 확인합니다.": "After leaving the lock <br/>scope, it checks status.", "조건이 거짓이면 0을 <br/>반환합니다. · status #60; 0 <br/>#91;false#93;": "If the condition is false, <br/>it returns 0. · status #60; 0 <br/>#91;false#93;", "조건이 참이면 exit#40;#41;를 <br/>호출합니다. · status #60; 0 <br/>#91;true#93;": "If the condition is true, <br/>it calls exit#40;#41;. · status #60; <br/>0 #91;true#93;"}
  v_entry["CameraManager::Private::<br/>start는 스레드 초기화를 <br/>기다린 뒤 결과를 반환합니다."]
  v_thread_start["Thread::start를 호출해 <br/>스레드를 시작합니다."]
  v_wait_init["MutexLocker로 mutex#95;를 <br/>잠그고 initialized#95;가 참이 <br/>될 때까지 cv#95;에서 <br/>기다립니다."]
  v_copy_status["status#95;를 지역 변수 <br/>status에 복사한 뒤 잠금 <br/>범위를 끝냅니다."]
  v_check_status{"status가 0보다 작습니까?"}
  v_stop["exit#40;#41;를 호출해 스레드 <br/>종료를 요청합니다."]
  v_join["wait#40;#41;를 호출해 스레드가 <br/>끝나기를 기다립니다."]
  v_return_failure["복사한 실패 상태 status를 <br/>반환합니다."]
  v_return_success["성공을 뜻하는 0을 <br/>반환합니다."]
  v_entry -->|"start가 Thread::start를 <br/>호출합니다."| v_thread_start
  v_thread_start -->|"Thread::start가 정상 <br/>복귀하면 초기화를 <br/>기다립니다."| v_wait_init
  v_wait_init -->|"대기가 끝나면 status#95;를 <br/>복사합니다."| v_copy_status
  v_copy_status -->|"잠금 범위를 끝낸 뒤 <br/>status를 확인합니다."| v_check_status
  v_check_status -->|"조건이 참이면 exit#40;#41;를 <br/>호출합니다. · status #60; 0 <br/>#91;true#93;"| v_stop
  v_stop -->|"exit#40;#41;가 정상 복귀하면 <br/>wait#40;#41;를 호출합니다."| v_join
  v_join -->|"wait#40;#41;가 정상 복귀하면 <br/>status를 반환합니다."| v_return_failure
  v_check_status -->|"조건이 거짓이면 0을 <br/>반환합니다. · status #60; 0 <br/>#91;false#93;"| v_return_success
```

[Mermaid 원문](manager_start.manager-start-wait-result.mmd)

??? note "그림 근거와 확인 범위"
    Private::start는 스레드 초기화 결과를 어떻게 기다리고 실패 또는 성공을 반환합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="CameraManager::Private::start waits for thread initialization and returns a result.">CameraManager::Private::start는 스레드 초기화를 기다린 뒤 결과를 반환합니다.</span> | [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) |
    | <span data-sdd-label-en="It calls Thread::start to start the thread.">Thread::start를 호출해 스레드를 시작합니다.</span> | [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) |
    | <span data-sdd-label-en="It locks mutex_ with MutexLocker and waits on cv_ until initialized_ is true.">MutexLocker로 mutex&#95;를 잠그고 initialized&#95;가 참이 될 때까지 cv&#95;에서 기다립니다.</span> | [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) |
    | <span data-sdd-label-en="It copies status_ to local status and leaves the lock scope.">status&#95;를 지역 변수 status에 복사한 뒤 잠금 범위를 끝냅니다.</span> | [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) |
    | <span data-sdd-label-en="Is status less than 0?">status가 0보다 작습니까?</span> | [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) |
    | <span data-sdd-label-en="It calls exit() to request thread termination.">exit&#40;&#41;를 호출해 스레드 종료를 요청합니다.</span> | [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) |
    | <span data-sdd-label-en="It calls wait() to wait for the thread to finish.">wait&#40;&#41;를 호출해 스레드가 끝나기를 기다립니다.</span> | [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) |
    | <span data-sdd-label-en="It returns the copied failure status.">복사한 실패 상태 status를 반환합니다.</span> | [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) |
    | <span data-sdd-label-en="It returns 0 for success.">성공을 뜻하는 0을 반환합니다.</span> | [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) |
    | <span data-sdd-label-en="start calls Thread::start.">start가 Thread::start를 호출합니다.</span> | [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) |
    | <span data-sdd-label-en="After Thread::start returns normally, it waits for initialization.">Thread::start가 정상 복귀하면 초기화를 기다립니다.</span> | [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) |
    | <span data-sdd-label-en="After the wait, it copies status_.">대기가 끝나면 status&#95;를 복사합니다.</span> | [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) |
    | <span data-sdd-label-en="After leaving the lock scope, it checks status.">잠금 범위를 끝낸 뒤 status를 확인합니다.</span> | [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) |
    | <span data-sdd-label-en="If the condition is true, it calls exit(). · status &lt; 0 [true]">조건이 참이면 exit&#40;&#41;를 호출합니다. · status &lt; 0 &#91;true&#93;</span> | [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) |
    | <span data-sdd-label-en="After exit() returns normally, it calls wait().">exit&#40;&#41;가 정상 복귀하면 wait&#40;&#41;를 호출합니다.</span> | [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) |
    | <span data-sdd-label-en="After wait() returns normally, it returns status.">wait&#40;&#41;가 정상 복귀하면 status를 반환합니다.</span> | [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) |
    | <span data-sdd-label-en="If the condition is false, it returns 0. · status &lt; 0 [false]">조건이 거짓이면 0을 반환합니다. · status &lt; 0 &#91;false&#93;</span> | [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) |
<!-- /sdd:visual:manager-start-wait-result -->

<!-- sdd:visual:manager-run-notify-before-branch -->
### 관리자 스레드의 알림과 정리

```mermaid
flowchart TB
%% sdd:translations {"cleanup#40;#41;이 정상 복귀하면 <br/>run은 반환합니다.": "If cleanup#40;#41; returns <br/>normally, run returns.", "cleanup#40;#41;이 정상 복귀하면 <br/>반환합니다.": "If cleanup#40;#41; returns <br/>normally, run returns.", "exec#40;#41;가 정상 복귀하면 <br/>cleanup#40;#41;을 호출합니다.": "If exec#40;#41; returns normally, <br/>run calls cleanup#40;#41;.", "init#40;#41;이 반환한 뒤 잠급니다.": "run locks after init#40;#41; <br/>returns.", "ret이 0보다 작습니까?": "Is ret less than 0?", "run은 cleanup#40;#41;을 <br/>호출합니다. cleanup#40;#41;이 <br/>정상 복귀하면 run이 <br/>끝납니다.": "run calls cleanup#40;#41;. If <br/>cleanup#40;#41; returns normally, <br/>run ends.", "run은 cleanup#40;#41;을 <br/>호출합니다. init#40;#41;이 <br/>enumerator#95;를 null로 남길 <br/>수 있지만 cleanup#40;#41;은 이를 <br/>역참조합니다.": "run calls cleanup#40;#41;; init#40;#41; <br/>can leave enumerator#95; null, <br/>which cleanup#40;#41; <br/>dereferences.", "run은 cv#95;.notify#95;one#40;#41;을 <br/>호출해 알립니다.": "run signals by calling <br/>cv#95;.notify#95;one#40;#41;.", "run은 exec#40;#41;를 호출해 <br/>이벤트와 메시지 처리를 <br/>시작합니다.": "run calls exec#40;#41; to start <br/>processing events and <br/>messages.", "run은 init#40;#41;의 반환값을 <br/>ret에 저장합니다.": "run stores the return value <br/>of init#40;#41; in ret.", "run은 mutex#95;를 잠급니다.": "run locks mutex#95;.", "run은 mutex#95;의 잠금을 <br/>풉니다.": "run unlocks mutex#95;.", "run은 status#95;에 ret을 <br/>저장하고 initialized#95;를 <br/>true로 설정합니다.": "run stores ret in status#95; <br/>and sets initialized#95; to <br/>true.", "값을 설정한 뒤 잠금을 <br/>풉니다.": "run unlocks after setting <br/>the values.", "알린 뒤 조건을 검사합니다.": "run checks the condition <br/>after signaling.", "잠근 뒤 값을 설정합니다.": "run sets the values after <br/>locking.", "잠금을 푼 뒤 알립니다.": "run signals after unlocking.", "조건이 거짓이면 exec#40;#41;를 <br/>호출합니다. · ret #60; 0 <br/>#91;false#93;": "If the condition is false, <br/>run calls exec#40;#41;. · ret #60; 0 <br/>#91;false#93;", "조건이 참이면 cleanup#40;#41;을 <br/>호출합니다. · ret #60; 0 #91;true#93;": "If the condition is true, <br/>run calls cleanup#40;#41;. · ret <br/>#60; 0 #91;true#93;"}
  v_init["run은 init#40;#41;의 반환값을 <br/>ret에 저장합니다."]
  v_lock["run은 mutex#95;를 잠급니다."]
  v_status["run은 status#95;에 ret을 <br/>저장하고 initialized#95;를 <br/>true로 설정합니다."]
  v_unlock["run은 mutex#95;의 잠금을 <br/>풉니다."]
  v_notify["run은 cv#95;.notify#95;one#40;#41;을 <br/>호출해 알립니다."]
  v_branch{"ret이 0보다 작습니까?"}
  v_failure_cleanup["run은 cleanup#40;#41;을 <br/>호출합니다. init#40;#41;이 <br/>enumerator#95;를 null로 남길 <br/>수 있지만 cleanup#40;#41;은 이를 <br/>역참조합니다."]
  v_failure_return["cleanup#40;#41;이 정상 복귀하면 <br/>run은 반환합니다."]
  v_exec["run은 exec#40;#41;를 호출해 <br/>이벤트와 메시지 처리를 <br/>시작합니다."]
  v_success_cleanup["run은 cleanup#40;#41;을 <br/>호출합니다. cleanup#40;#41;이 <br/>정상 복귀하면 run이 <br/>끝납니다."]
  v_init -->|"init#40;#41;이 반환한 뒤 잠급니다."| v_lock
  v_lock -->|"잠근 뒤 값을 설정합니다."| v_status
  v_status -->|"값을 설정한 뒤 잠금을 <br/>풉니다."| v_unlock
  v_unlock -->|"잠금을 푼 뒤 알립니다."| v_notify
  v_notify -->|"알린 뒤 조건을 검사합니다."| v_branch
  v_branch -->|"조건이 참이면 cleanup#40;#41;을 <br/>호출합니다. · ret #60; 0 #91;true#93;"| v_failure_cleanup
  v_failure_cleanup -->|"cleanup#40;#41;이 정상 복귀하면 <br/>반환합니다."| v_failure_return
  v_branch -->|"조건이 거짓이면 exec#40;#41;를 <br/>호출합니다. · ret #60; 0 <br/>#91;false#93;"| v_exec
  v_exec -->|"exec#40;#41;가 정상 복귀하면 <br/>cleanup#40;#41;을 호출합니다."| v_success_cleanup
```

[Mermaid 원문](manager_start.manager-run-notify-before-branch.mmd)

??? note "그림 근거와 확인 범위"
    run은 초기화 결과를 저장하고 알린 뒤 언제 정리하고 언제 이벤트 처리를 시작합니까?
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    LLM 그림 초안 · 사람 검토 전
    
    작성 모델: `cli/codex/gpt-6.1-terra`
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="run stores the return value of init() in ret.">run은 init&#40;&#41;의 반환값을 ret에 저장합니다.</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
    | <span data-sdd-label-en="run locks mutex_.">run은 mutex&#95;를 잠급니다.</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
    | <span data-sdd-label-en="run stores ret in status_ and sets initialized_ to true.">run은 status&#95;에 ret을 저장하고 initialized&#95;를 true로 설정합니다.</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
    | <span data-sdd-label-en="run unlocks mutex_.">run은 mutex&#95;의 잠금을 풉니다.</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
    | <span data-sdd-label-en="run signals by calling cv_.notify_one().">run은 cv&#95;.notify&#95;one&#40;&#41;을 호출해 알립니다.</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
    | <span data-sdd-label-en="Is ret less than 0?">ret이 0보다 작습니까?</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
    | <span data-sdd-label-en="run calls cleanup(); init() can leave enumerator_ null, which cleanup() dereferences.">run은 cleanup&#40;&#41;을 호출합니다. init&#40;&#41;이 enumerator&#95;를 null로 남길 수 있지만 cleanup&#40;&#41;은 이를 역참조합니다.</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) · [src/libcamera/camera_manager.cpp:94](#source-9290be142dcb4257) · [src/libcamera/camera_manager.cpp:170](#source-2130ad244cd4fcfa) |
    | <span data-sdd-label-en="If cleanup() returns normally, run returns.">cleanup&#40;&#41;이 정상 복귀하면 run은 반환합니다.</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
    | <span data-sdd-label-en="run calls exec() to start processing events and messages.">run은 exec&#40;&#41;를 호출해 이벤트와 메시지 처리를 시작합니다.</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
    | <span data-sdd-label-en="run calls cleanup(). If cleanup() returns normally, run ends.">run은 cleanup&#40;&#41;을 호출합니다. cleanup&#40;&#41;이 정상 복귀하면 run이 끝납니다.</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
    | <span data-sdd-label-en="run locks after init() returns.">init&#40;&#41;이 반환한 뒤 잠급니다.</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
    | <span data-sdd-label-en="run sets the values after locking.">잠근 뒤 값을 설정합니다.</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
    | <span data-sdd-label-en="run unlocks after setting the values.">값을 설정한 뒤 잠금을 풉니다.</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
    | <span data-sdd-label-en="run signals after unlocking.">잠금을 푼 뒤 알립니다.</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
    | <span data-sdd-label-en="run checks the condition after signaling.">알린 뒤 조건을 검사합니다.</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
    | <span data-sdd-label-en="If the condition is true, run calls cleanup(). · ret &lt; 0 [true]">조건이 참이면 cleanup&#40;&#41;을 호출합니다. · ret &lt; 0 &#91;true&#93;</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
    | <span data-sdd-label-en="If cleanup() returns normally, run returns.">cleanup&#40;&#41;이 정상 복귀하면 반환합니다.</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
    | <span data-sdd-label-en="If the condition is false, run calls exec(). · ret &lt; 0 [false]">조건이 거짓이면 exec&#40;&#41;를 호출합니다. · ret &lt; 0 &#91;false&#93;</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
    | <span data-sdd-label-en="If exec() returns normally, run calls cleanup().">exec&#40;&#41;가 정상 복귀하면 cleanup&#40;&#41;을 호출합니다.</span> | [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) |
<!-- /sdd:visual:manager-run-notify-before-branch -->

`CameraManager::Private::run()`은 `init()`의 반환값을 `ret`에 저장하고 `mutex_`를 잠근 상태에서 `status_`에 복사한 뒤 `initialized_`를 참으로 설정합니다. `mutex_.unlock()`이 끝난 뒤 `cv_.notify_one()`을 호출합니다. `ret`이 음수이면 `cleanup()`을 호출하고 반환하며, 그렇지 않으면 `exec()`를 호출한 뒤 `cleanup()`을 호출합니다. `src/libcamera/camera_manager.cpp:71`

`CameraManager::Private::init()`은 `IPAManager`를 만든 뒤 `DeviceEnumerator::create()`로 `enumerator_`를 생성합니다. 생성에 실패하거나 `enumerate()`가 실패하면 `-ENODEV`를 반환합니다. 그렇지 않으면 `createPipelineHandlers()`를 호출하고 `devicesAdded`를 `Private::createPipelineHandlers`에 연결한 뒤 0을 반환합니다. `src/libcamera/camera_manager.cpp:94`

근거 원문: [src/libcamera/camera_manager.cpp:46](#source-a4d912d45af5ed8a) · [src/libcamera/camera_manager.cpp:71](#source-5bd9506aae245794) · [src/libcamera/camera_manager.cpp:94](#source-9290be142dcb4257) · [src/libcamera/camera_manager.cpp:170](#source-2130ad244cd4fcfa)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | CameraManager::start()이 장치를 열거하는 목적과 시작이 확인된 뒤 카메라를 사용할 수 있는 범위를 두 짧은 문단으로 설명하세요. 관리자 중지 또는 카메라 분리 조건을 보존하세요. 숫자 반환값과 내부 대기·실패 처리는 다음 절에서만 설명하므로 이 절에서는 반복하지 마세요. | [탐색을 시작하고 카메라를 사용할 시점](#탐색을-시작하고-카메라를-사용할-시점) | 코드 근거와 설명 연결 |
    | Private::start()의 Thread::start·초기화 대기·status_ 복사와 음수 실패 시 exit/wait/상태 반환 및 성공 반환을 한 문단으로 설명하세요. run()의 초기화 결과 전달, 실패 cleanup과 성공 exec 뒤 cleanup을 둘째 문단에서 설명하세요. init()의 enumerator 생성·열거 실패 -ENODEV와 성공 createPipelineHandlers 및 devicesAdded 연결을 마지막 한 문단으로 묶으세요. 함수별 결과를 한 번씩만 설명하고 소스에 없는 보장이나 작업 보고를 붙이지 마세요. mutex_.unlock()이 끝난 뒤 cv_.notify_one()을 호출한다는 순서를 별도 문장으로 명시하고, 알림을 잠금 구간에 포함시키지 마세요. | [관리자 스레드의 초기화와 실패 처리](#관리자-스레드의-초기화와-실패-처리) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-027ec5bea3fe0dfa"></a>

??? note "소스 근거: src/libcamera/camera_manager.cpp:329"
    `src/libcamera/camera_manager.cpp:329`에서 시작하는 발췌입니다. 종료 줄은 337이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `2a4a445a45564c5df07c3d58252d4ee685195eb169bf1db475e00a2f81edab06`
    
    ```text
    \brief Start the camera manager
     *
     * Start the camera manager and enumerate all devices in the system. Once
     * the start has been confirmed the user is free to list and otherwise
     * interact with cameras in the system until either the camera manager
     * is stopped or the camera is unplugged from the system.
     *
     * \return 0 on success or a negative error code otherwise
     */
    ```

<a id="source-a4d912d45af5ed8a"></a>

??? note "소스 근거: src/libcamera/camera_manager.cpp:46"
    `src/libcamera/camera_manager.cpp:46`에서 시작하는 발췌입니다. 종료 줄은 69이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `89896bcb55bd900a3a96065af0cf2627c0f80233169c4c39da922bea341c06b7`
    
    ```text
    int CameraManager::Private::start()
    {
    	int status;
    
    	/* Start the thread and wait for initialization to complete. */
    	Thread::start();
    
    	{
    		MutexLocker locker(mutex_);
    		cv_.wait(locker, [&]() LIBCAMERA_TSA_REQUIRES(mutex_) {
    			return initialized_;
    		});
    		status = status_;
    	}
    
    	/* If a failure happened during initialization, stop the thread. */
    	if (status < 0) {
    		exit();
    		wait();
    		return status;
    	}
    
    	return 0;
    }
    ```

<a id="source-5bd9506aae245794"></a>

??? note "소스 근거: src/libcamera/camera_manager.cpp:71"
    `src/libcamera/camera_manager.cpp:71`에서 시작하는 발췌입니다. 종료 줄은 92이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `99f2565470c1a03de3fa75aef000454121aa8135d5ebacd6e5e9a4f8961c07aa`
    
    ```text
    void CameraManager::Private::run()
    {
    	LOG(Camera, Debug) << "Starting camera manager";
    
    	int ret = init();
    
    	mutex_.lock();
    	status_ = ret;
    	initialized_ = true;
    	mutex_.unlock();
    	cv_.notify_one();
    
    	if (ret < 0) {
    		cleanup();
    		return;
    	}
    
    	/* Now start processing events and messages. */
    	exec();
    
    	cleanup();
    }
    ```

<a id="source-9290be142dcb4257"></a>

??? note "소스 근거: src/libcamera/camera_manager.cpp:94"
    `src/libcamera/camera_manager.cpp:94`에서 시작하는 발췌입니다. 종료 줄은 107이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `8e85184e2eacbf523477a4c87d878c17069fa18f3358f39501fcaaca8e3dbffe`
    
    ```text
    int CameraManager::Private::init()
    {
    	CameraManager *const o = LIBCAMERA_O_PTR();
    	ipaManager_ = std::make_unique<IPAManager>(*o);
    
    	enumerator_ = DeviceEnumerator::create();
    	if (!enumerator_ || enumerator_->enumerate())
    		return -ENODEV;
    
    	createPipelineHandlers();
    	enumerator_->devicesAdded.connect(this, &Private::createPipelineHandlers);
    
    	return 0;
    }
    ```

<a id="source-2130ad244cd4fcfa"></a>

??? note "소스 근거: src/libcamera/camera_manager.cpp:170"
    `src/libcamera/camera_manager.cpp:170`에서 시작하는 발췌입니다. 종료 줄은 189이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `013ef95052c9ca394b4c18cb59a7c9c53873cfb4efe8d23138bd1f2ae1007bfa`
    
    ```text
    void CameraManager::Private::cleanup()
    {
    	enumerator_->devicesAdded.disconnect(this);
    
    	/*
    	 * Release all references to cameras to ensure they all get destroyed
    	 * before the device enumerator deletes the media devices. Cameras are
    	 * destroyed via Object::deleteLater() API, hence we need to explicitly
    	 * process deletion requests from the thread's message queue as the event
    	 * loop is not in action here.
    	 */
    	{
    		MutexLocker locker(mutex_);
    		cameras_.clear();
    	}
    
    	dispatchMessages(Message::Type::DeferredDelete);
    
    	enumerator_.reset(nullptr);
    }
    ```

## 주요 확인 지점

아래 항목은 추출한 호출에서 고른 코드 탐색 지점입니다. 나열 순서는 실행 순서가 아닙니다.

| 확인할 내용 | 호출 측과 대상 | 구분 | 근거 |
|---|---|---|---|
| 관리자 시작 | `CameraManager` → `Private::start()` | 정적 호출 지점입니다. | `src/libcamera/camera_manager.cpp:342` |

## 주요 호출 관계

화살표는 호출 측과 대상을 연결합니다. 시간 순서나 모든 경로의 실행을 뜻하지 않습니다. 점선에는 가상 호출 후보·예약 대상 등 확인이 필요한 관계를 표시합니다.

```mermaid
flowchart LR
  p0["CameraManager"]
  p1["Private"]
  p0 -->|"start#40;#41;"| p1
```

## 추적 범위와 경계

요약의 hide 규칙에 해당하는 호출은 17개입니다. 전체 추적 기록에는 해당 호출도 모두 보존합니다. 기록 번호는 정적 탐색의 식별자이며 실행 순번이 아닙니다.

조건 분기, 반복 횟수와 실제 실행 스레드는 이 호출 목록만으로 확정할 수 없습니다. 가상 호출 후보는 실제 객체에 따라 선택됩니다. 예약 표시는 인자로 전달한 메서드 대상을 뜻하며, 비동기 실행을 보증하지 않습니다. 호출부의 연결 방식과 동기화 계약을 확인해야 합니다.

| 호출 지점 | 후보 또는 예약 대상 | 확인할 경계 | 근거 |
|---|---|---|---|
| `Thread` | `Thread::startThread()` | 메서드 전달 대상이며 동기·비동기 여부는 호출부에서 확인해야 합니다. | `src/libcamera/base/thread.cpp:264` |
| `Thread` | `EventDispatcherPoll::interrupt()` | 동적 디스패치 후보이며 실제 대상은 확인이 필요합니다. | `src/libcamera/base/thread.cpp:386` |

추출 통계: 미해결 호출 0개, 예약된 호출 1개입니다.

## 전체 추적 기록

아래 구간을 펼치면 요약에서 제외된 호출까지 확인할 수 있습니다. 이 목록은 추출 깊이 안에서 수집한 기록이며, 소스의 모든 실행 경로를 포함한다는 뜻은 아닙니다.

??? note "추적 기록 1–25 / 33개"

    | 기록 | 호출 측 | 대상 | 구분 | 근거 |
    |---|---|---|---|---|
    | 1 | `CameraManager` | `log::isLogSeverityEnabled()` | 정적 호출 지점입니다. | `src/libcamera/camera_manager.cpp:340` |
    | 2 | `CameraManager` | `LogMessageAbortGuard::LogMessageAbortGuard()` | 정적 호출 지점입니다. | `src/libcamera/camera_manager.cpp:340` |
    | 3 | `CameraManager` | `LogMessage::stream()` | 정적 호출 지점입니다. | `src/libcamera/camera_manager.cpp:340` |
    | 4 | `CameraManager` | `log::_log()` | 정적 호출 지점입니다. | `src/libcamera/camera_manager.cpp:340` |
    | 5 | `log` | `LogMessage::LogMessage()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:990` |
    | 6 | `LogMessage` | `utils::basename()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:858` |
    | 7 | `CameraManager` | `Private::start()` | 정적 호출 지점입니다. | `src/libcamera/camera_manager.cpp:342` |
    | 8 | `Private` | `Thread::start()` | 정적 호출 지점입니다. | `src/libcamera/camera_manager.cpp:51` |
    | 9 | `Thread` | `MutexLocker::MutexLocker()` | 정적 호출 지점입니다. | `src/libcamera/base/thread.cpp:255` |
    | 10 | `Thread` | `Thread::startThread()` | 메서드 전달 대상이며 동기·비동기 여부는 호출부에서 확인해야 합니다. | `src/libcamera/base/thread.cpp:264` |
    | 11 | `Thread` | `Thread::setThreadAffinityInternal()` | 정적 호출 지점입니다. | `src/libcamera/base/thread.cpp:266` |
    | 12 | `Private` | `MutexLocker::MutexLocker()` | 정적 호출 지점입니다. | `src/libcamera/camera_manager.cpp:54` |
    | 13 | `Private` | `ConditionVariable::wait()` | 정적 호출 지점입니다. | `src/libcamera/camera_manager.cpp:55` |
    | 14 | `Private` | `Thread::exit()` | 정적 호출 지점입니다. | `src/libcamera/camera_manager.cpp:63` |
    | 15 | `Thread` | `EventDispatcherPoll::interrupt()` | 동적 디스패치 후보이며 실제 대상은 확인이 필요합니다. | `src/libcamera/base/thread.cpp:386` |
    | 16 | `EventDispatcherPoll` | `UniqueFD::get()` | 정적 호출 지점입니다. | `src/libcamera/base/event_dispatcher_poll.cpp:177` |
    | 17 | `EventDispatcherPoll` | `log::isLogSeverityEnabled()` | 정적 호출 지점입니다. | `src/libcamera/base/event_dispatcher_poll.cpp:181` |
    | 18 | `EventDispatcherPoll` | `LogMessageAbortGuard::LogMessageAbortGuard()` | 정적 호출 지점입니다. | `src/libcamera/base/event_dispatcher_poll.cpp:181` |
    | 19 | `EventDispatcherPoll` | `LogMessage::stream()` | 정적 호출 지점입니다. | `src/libcamera/base/event_dispatcher_poll.cpp:181` |
    | 20 | `EventDispatcherPoll` | `log::_log()` | 정적 호출 지점입니다. | `src/libcamera/base/event_dispatcher_poll.cpp:181` |
    | 21 | `Private` | `Thread::wait()` | 정적 호출 지점입니다. | `src/libcamera/camera_manager.cpp:64` |
    | 22 | `Thread` | `MutexLocker::MutexLocker()` | 정적 호출 지점입니다. | `src/libcamera/base/thread.cpp:407` |
    | 23 | `Thread` | `ConditionVariable::wait()` | 정적 호출 지점입니다. | `src/libcamera/base/thread.cpp:414` |
    | 24 | `Thread` | `(lambda at src/libcamera/base/thread.cpp:409:21)::(lambda at src/libcamera/base/thread.cpp:409:21)()` | 정적 호출 지점입니다. | `src/libcamera/base/thread.cpp:414` |
    | 25 | `Thread` | `ConditionVariable::wait_for()` | 정적 호출 지점입니다. | `src/libcamera/base/thread.cpp:416` |

??? note "추적 기록 26–33 / 33개"

    | 기록 | 호출 측 | 대상 | 구분 | 근거 |
    |---|---|---|---|---|
    | 26 | `Thread` | `(lambda at src/libcamera/base/thread.cpp:409:21)::(lambda at src/libcamera/base/thread.cpp:409:21)()` | 정적 호출 지점입니다. | `src/libcamera/base/thread.cpp:417` |
    | 27 | `CameraManager` | `CameraManager::_d()` | 정적 호출 지점입니다. | `src/libcamera/camera_manager.cpp:342` |
    | 28 | `CameraManager` | `log::isLogSeverityEnabled()` | 정적 호출 지점입니다. | `src/libcamera/camera_manager.cpp:344` |
    | 29 | `CameraManager` | `LogMessageAbortGuard::LogMessageAbortGuard()` | 정적 호출 지점입니다. | `src/libcamera/camera_manager.cpp:344` |
    | 30 | `CameraManager` | `LogMessage::stream()` | 정적 호출 지점입니다. | `src/libcamera/camera_manager.cpp:344` |
    | 31 | `CameraManager` | `log::_log()` | 정적 호출 지점입니다. | `src/libcamera/camera_manager.cpp:344` |
    | 32 | `log` | `LogMessage::LogMessage()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:990` |
    | 33 | `LogMessage` | `utils::basename()` | 정적 호출 지점입니다. | `src/libcamera/base/log.cpp:858` |

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `src/libcamera/base/event_dispatcher_poll.cpp`, `src/libcamera/base/log.cpp`, `src/libcamera/base/thread.cpp`, `src/libcamera/camera_manager.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `293d751a81`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-04 · 사람 검토 전

다음 단계: [스트림 구성](configure.md)
