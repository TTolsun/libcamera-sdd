---
generated_at: 2026-11-04T22:34:01+00:00
source_commit: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61
status: ok
section: probe
generation_method: facts-and-llm
evidence_fingerprint: cc827695de1d0c11e86493e2b1a33962f82ceaf0153b1d52ca04d43dd7fd8f82
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "cc827695de1d0c11e86493e2b1a33962f82ceaf0153b1d52ca04d43dd7fd8f82", "answers": {"create": [{"text": "호출자는 카메라가 `Configured` 또는 `Running` 상태일 때만 `Camera::createRequest()`를 호출해야 합니다. 이 함수는 스레드 안전하며, 새로 만든 요청의 포인터를 반환하고 오류가 발생하면 `nullptr`을 반환합니다.", "evidence": ["create-state"], "covers": ["create"], "kind": "behavior", "quote": "\\context This function is \\threadsafe. It may only be called when the camera\n * is in the Configured or Running state as defined in \\ref camera_operation.\n *\n * \\return A pointer to the newly created request, or nullptr on error\n */\nstd::unique_ptr<Request> Camera::createRequest(uint64_t cookie)"}], "queue": [{"text": "호출자는 카메라가 `Running` 상태일 때만 `Camera::queueRequest()`를 호출해야 합니다. 이 함수는 스레드 안전하며, 성공하면 0을 반환하고 그렇지 않으면 음수 오류 코드를 반환합니다. 카메라가 시스템에서 연결 해제된 경우 `-ENODEV`, 카메라가 실행 중이 아니어서 요청을 큐에 넣을 수 없는 경우 `-EACCES`, 요청이 해당 카메라에 속하지 않는 경우 `-EXDEV`를 반환합니다. 요청이 유효하지 않으면 `-EINVAL`, 요청을 처리할 버퍼 메모리가 없으면 `-ENOMEM`을 반환합니다.", "evidence": ["queue-state"], "covers": ["queue"], "kind": "behavior", "quote": "\\context This function is \\threadsafe. It may only be called when the camera\n * is in the Running state as defined in \\ref camera_operation.\n *\n * \\return 0 on success or a negative error code otherwise\n * \\retval -ENODEV The camera has been disconnected from the system\n * \\retval -EACCES The camera is not running so requests can't be queued\n * \\retval -EXDEV The request does not belong to this camera\n * \\retval -EINVAL The request is invalid\n * \\retval -ENOMEM No buffer memory was available to handle the request\n */\nint Camera::queueRequest(Request *request)"}]}, "topic_inputs": {"create": "9b78f702ecc0b8dd34df2f2052888f8229bfcb251e5148c7a05c0c565bb69e79", "queue": "4c84cbb4fd06f20e5c237387d25b8639f4abc389a9467069c35c1a56b9ef1a7e"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["create", "queue"], "topic_agents": {"create": "cli/codex/gpt-6.1-terra", "queue": "cli/codex/gpt-6.1-terra"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "367d18b95f8f0d01a15ae0f4d1b70f7e13e4d0298df4215e2c449ac4905db6f9", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "d0f7ab4c48fcf52409935931eb9b93aacd48af4b19e9bb816fa496f1214fdb2f", "answer_contracts": "a39c9a8818afc47e059141d486337c0f12a7fd34319e2b6f7674fc428bc83e2b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "050c20aa2fdcceae10c6275fbb5f850f616ab5051bb67ccbcb4a204877a238d9", "explanation": "69bcaa207ef39d20f6a47ac201c3edf119f59b333e85131dea1bce85eef4006b", "design_response": "a7c199bc52bcc0e749ef01186e50bca98107473d5c82e2248712f465d02e1e69", "design_validation": "a4edf8364d73d169c3f10ecbadf487a8a4dc10328622d07578b281eae810c3aa"}, "validation_model": "a83f97866e9854354d0734a30ec1aee606af34e23c65bbddc27c454aa925a7cc", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "b87a84b1bc31079837dc4dc4527ce02c9dc2cbc3a26ff7e99e0872941d213995"}, "checkpoint_units": [{"checkpoint": "9b80992bc637b9078680e42e837cd214578644ac3830ee4eb53fc0997c86a226.json", "topic": "create", "part": null, "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["6dc6f3ba1a234c95b84d6996f6397e1e/001.receipt.json", "6dc6f3ba1a234c95b84d6996f6397e1e/002.receipt.json"]}, {"checkpoint": "6dbe182f3cd0b377c3f81b4c32bb222173123d4c1b150ce565a4885027d495ce.json", "topic": "queue", "part": null, "subpart": null, "revalidated": true, "new_grounding_review": false, "receipts": ["e321e9897bb34feeaf07c871a8d2ebcd/003.receipt.json", "e321e9897bb34feeaf07c871a8d2ebcd/004.receipt.json"]}], "body_sha256": "a5d3b39dc4504d695e5504808eac231b899ca7ca4f0ea0487bd7deb44a7a9524"}
---

# 요청 API의 상태와 반환값 검증 표본

**두 요청 API의 공개 소스 계약을 대조합니다.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| 호출자는 카메라가 `Configured` 또는 `Running` 상태일 때만 `Camera::createRequest()`를 호출해야 합니다. | [요청 생성](#요청-생성) |
| 호출자는 카메라가 `Running` 상태일 때만 `Camera::queueRequest()`를 호출해야 합니다. | [요청 큐잉](#요청-큐잉) |

## 요청 생성

호출자는 카메라가 `Configured` 또는 `Running` 상태일 때만 `Camera::createRequest()`를 호출해야 합니다. 이 함수는 스레드 안전하며, 새로 만든 요청의 포인터를 반환하고 오류가 발생하면 `nullptr`을 반환합니다. `src/libcamera/camera.cpp:1258`

근거 원문: [src/libcamera/camera.cpp:1258](#source-8f791427a31c3313)

## 요청 큐잉

호출자는 카메라가 `Running` 상태일 때만 `Camera::queueRequest()`를 호출해야 합니다. 이 함수는 스레드 안전하며, 성공하면 0을 반환하고 그렇지 않으면 음수 오류 코드를 반환합니다. 카메라가 시스템에서 연결 해제된 경우 `-ENODEV`, 카메라가 실행 중이 아니어서 요청을 큐에 넣을 수 없는 경우 `-EACCES`, 요청이 해당 카메라에 속하지 않는 경우 `-EXDEV`를 반환합니다. 요청이 유효하지 않으면 `-EINVAL`, 요청을 처리할 버퍼 메모리가 없으면 `-ENOMEM`을 반환합니다. `src/libcamera/camera.cpp:1320`

근거 원문: [src/libcamera/camera.cpp:1320](#source-e0caa8c16f728202)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | createRequest()를 호출할 수 있는 상태와 실패 반환값은 무엇입니까? | [요청 생성](#요청-생성) | 코드 근거와 설명 연결 |
    | queueRequest()에 허용되는 상태와 오류 반환값은 무엇입니까? | [요청 큐잉](#요청-큐잉) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-8f791427a31c3313"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1258"
    `src/libcamera/camera.cpp:1258`에서 시작하는 발췌입니다. 종료 줄은 1263이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `fd7dc6ea02f64424f17322fff027c34131ac5a3fb64d69d83aa6fa55ca9f826a`
    
    ```text
    \context This function is \threadsafe. It may only be called when the camera
     * is in the Configured or Running state as defined in \ref camera_operation.
     *
     * \return A pointer to the newly created request, or nullptr on error
     */
    std::unique_ptr<Request> Camera::createRequest(uint64_t cookie)
    ```

<a id="source-e0caa8c16f728202"></a>

??? note "소스 근거: src/libcamera/camera.cpp:1320"
    `src/libcamera/camera.cpp:1320`에서 시작하는 발췌입니다. 종료 줄은 1330이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `b9de90acc07617b489b367e116e41ecc8bc712180c6f445763b58658ff1bc649`
    
    ```text
    \context This function is \threadsafe. It may only be called when the camera
     * is in the Running state as defined in \ref camera_operation.
     *
     * \return 0 on success or a negative error code otherwise
     * \retval -ENODEV The camera has been disconnected from the system
     * \retval -EACCES The camera is not running so requests can't be queued
     * \retval -EXDEV The request does not belong to this camera
     * \retval -EINVAL The request is invalid
     * \retval -ENOMEM No buffer memory was available to handle the request
     */
    int Camera::queueRequest(Request *request)
    ```

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `src/libcamera/camera.cpp`
    - 근거 수준: 코드 확인 (정적 분석, ndk-build 구성, commit `293d751a81`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-05 · 사람 검토 전

다음 단계: [검증 표본](probe.md)
