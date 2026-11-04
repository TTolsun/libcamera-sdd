---
generated_at: 2026-11-04T21:50:17+00:00
source_commit: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61
status: ok
section: camera-requests
generation_method: facts-and-llm
evidence_fingerprint: 40f0361e2ea945a46e337e3649f515bb564b62e6a076848d50a0df506fc32f62
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "40f0361e2ea945a46e337e3649f515bb564b62e6a076848d50a0df506fc32f62", "answers": {"request": [{"text": "`Request::addBuffer()`는 먼저 `stream`이 비어 있으면 `-EINVAL`을 반환합니다. 다음으로 버퍼에 `fence`가 남아 있으면 `-EEXIST`를 반환하고, 이어서 `stream`이 이미 등록되어 있으면 `-EEXIST`를 반환합니다. 세 검사를 통과하면 `buffer->_d()->setRequest(this)`를 호출한 뒤 `pending_.insert(buffer)`를 실행합니다.", "evidence": ["buffer-code"], "covers": ["request"], "kind": "behavior", "quote": "int Request::addBuffer(const Stream *stream, FrameBuffer *buffer,\n\t\t       std::unique_ptr<Fence> &&fence)\n{\n\tif (!stream) {\n\t\tLOG(Request, Error) << \"Invalid stream reference\";\n\t\treturn -EINVAL;\n\t}"}]}, "topic_inputs": {"request": "f2627407ca705440c94e62c4373ca832b45854ae76fde9294caad4579d30b3c2"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["request"], "topic_agents": {"request": "cli/codex/gpt-6.1-terra"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "367d18b95f8f0d01a15ae0f4d1b70f7e13e4d0298df4215e2c449ac4905db6f9", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "2f593eec0430a4e6b5822e642c0a7a1227fc150a0b27d8a71f521acf93b6439e", "answer_contracts": "1e0d24e0cf26ded53ecec2e5a6fbc51836bac6e17530318a9fa7cffaa936c00b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "050c20aa2fdcceae10c6275fbb5f850f616ab5051bb67ccbcb4a204877a238d9", "design_response": "deb70dda7ad27f001267e4a9712c5b0dc1fe9fa67acd13bedbfefaaad0ad83c8", "design_validation": "946deebb694018f6361ee86669e1a7a26cd61dfffef11bb3a7de0a193639fabe"}, "validation_model": "fa46211a17e40c777f219a3bb3ef96bd8717bc81ca878dc4ca6886d133ad0b8b", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "b87a84b1bc31079837dc4dc4527ce02c9dc2cbc3a26ff7e99e0872941d213995"}, "checkpoint_units": [{"checkpoint": "06804ec739aa04d98fa9f9de58d7ecceb97585267f3a0bfa23e8fb55b1906a1c.json", "topic": "request", "part": null, "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["3521ff61a16f44fda3614c04a11140b6/001.receipt.json", "3521ff61a16f44fda3614c04a11140b6/002.receipt.json"]}], "body_sha256": "1bd5951c56ac9318a9bae615b30a611c890587f4fb46b8c9e89a59fc92f7a0ae"}
---

# addBuffer 발행 계약 검증 표본

**addBuffer의 거절 조건과 요청·버퍼 연결 경계를 확인합니다.**



## addBuffer의 검사 순서와 연결 경계

`Request::addBuffer()`는 먼저 `stream`이 비어 있으면 `-EINVAL`을 반환합니다. 다음으로 버퍼에 `fence`가 남아 있으면 `-EEXIST`를 반환하고, 이어서 `stream`이 이미 등록되어 있으면 `-EEXIST`를 반환합니다. 세 검사를 통과하면 `buffer->_d()->setRequest(this)`를 호출한 뒤 `pending_.insert(buffer)`를 실행합니다. `src/libcamera/request.cpp:475`

<!-- sdd:visual:buffer-rejection -->
### 세 거절 검사와 요청 연결

```mermaid
flowchart TB
%% sdd:translations {"-EINVAL로 거절": "Reject with -EINVAL", "buffer에 fence가 남았는가?": "Does buffer retain a fence?", "setRequest와 pending#95;에 연결": "Bind with setRequest and <br/>pending#95;", "stream 등록이 중복됐는가?": "Is the stream already <br/>registered?", "stream이 null인가?": "Is stream null?", "아니요": "No", "예": "Yes", "잔존 fence: -EEXIST": "Retained fence: -EEXIST", "중복 stream: -EEXIST": "Duplicate stream: -EEXIST"}
  v_stream{"stream이 null인가?"}
  v_invalid["-EINVAL로 거절"]
  v_fence{"buffer에 fence가 남았는가?"}
  v_stale["잔존 fence: -EEXIST"]
  v_duplicate{"stream 등록이 중복됐는가?"}
  v_exists["중복 stream: -EEXIST"]
  v_linked["setRequest와 pending#95;에 연결"]
  v_stream -->|"예"| v_invalid
  v_stream -->|"아니요"| v_fence
  v_fence -->|"예"| v_stale
  v_fence -->|"아니요"| v_duplicate
  v_duplicate -->|"예"| v_exists
  v_duplicate -->|"아니요"| v_linked
```

[Mermaid 원문](camera-requests.buffer-rejection.mmd)

??? note "그림 근거와 확인 범위"
    stream·잔존 fence·중복 stream 검사와 요청 연결까지만 다루며, 이후 전달받은 fence의 이동은 제외합니다.
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Is stream null?">stream이 null인가?</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Reject with -EINVAL">-EINVAL로 거절</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Does buffer retain a fence?">buffer에 fence가 남았는가?</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Retained fence: -EEXIST">잔존 fence: -EEXIST</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Is the stream already registered?">stream 등록이 중복됐는가?</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Duplicate stream: -EEXIST">중복 stream: -EEXIST</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Bind with setRequest and pending_">setRequest와 pending&#95;에 연결</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Yes">예</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="No">아니요</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Yes">예</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="No">아니요</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Yes">예</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="No">아니요</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
<!-- /sdd:visual:buffer-rejection -->

근거 원문: [src/libcamera/request.cpp:475](#source-605100b059a6864d)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | Request::addBuffer() 구현에서 빈 stream, 버퍼에 남은 fence, 이미 등록한 stream을 검사하는 순서와 각 반환값을 설명하세요. -EINVAL과 두 -EEXIST 조건을 각각 연결하고, 세 검사를 통과한 뒤의 setRequest(this)와 pending_.insert(buffer) 경계를 설명하세요. 전달받은 fence의 이동과 실패 시 소유권은 이 표본 범위에서 제외하세요. | [addBuffer의 검사 순서와 연결 경계](#addbuffer의-검사-순서와-연결-경계) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-605100b059a6864d"></a>

??? note "소스 근거: src/libcamera/request.cpp:475"
    `src/libcamera/request.cpp:475`에서 시작하는 발췌입니다. 종료 줄은 505이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `c1c0b55f2925856df843fa155a14bb07eb616f52b6bde75cd3b0b5a4ab03b64a`
    
    ```text
    int Request::addBuffer(const Stream *stream, FrameBuffer *buffer,
    		       std::unique_ptr<Fence> &&fence)
    {
    	if (!stream) {
    		LOG(Request, Error) << "Invalid stream reference";
    		return -EINVAL;
    	}
    
    	/*
    	 * Make sure the fence has been extracted from the buffer
    	 * to avoid waiting on a stale fence.
    	 */
    	if (buffer->_d()->fence()) {
    		LOG(Request, Error) << "Can't add buffer that still references a fence";
    		return -EEXIST;
    	}
    
    	auto [it, inserted] = bufferMap_.try_emplace(stream, buffer);
    	if (!inserted) {
    		LOG(Request, Error) << "FrameBuffer already set for stream";
    		return -EEXIST;
    	}
    
    	buffer->_d()->setRequest(this);
    	_d()->pending_.insert(buffer);
    
    	if (fence && fence->isValid())
    		buffer->_d()->setFence(std::move(fence));
    
    	return 0;
    }
    ```

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `src/libcamera/request.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `293d751a81`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-11-05 · 사람 검토 전
