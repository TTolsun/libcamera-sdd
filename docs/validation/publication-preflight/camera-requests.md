---
generated_at: 2026-11-05T00:17:37+00:00
source_commit: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61
status: ok
section: camera-requests
generation_method: facts-and-llm
evidence_fingerprint: 6c202a69485d7ae8f1f6b8d2561bbe0b7a24e8535118de63b9161a23bfb6ac25
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "6c202a69485d7ae8f1f6b8d2561bbe0b7a24e8535118de63b9161a23bfb6ac25", "answers": {"request": [{"text": "`Request::addBuffer()`는 세 거절 검사를 통과한 뒤 `fence && fence->isValid()`가 참이면 `setFence(std::move(fence))`를 호출해 전달받은 `fence`를 버퍼로 이동합니다. 전달받은 `fence`가 null이거나 유효하지 않으면 이 분기를 실행하지 않습니다.", "evidence": ["buffer-code"], "covers": ["request"], "kind": "behavior", "quote": "if (fence && fence->isValid())\n\t\tbuffer->_d()->setFence(std::move(fence));"}]}, "topic_inputs": {"request": "7949b72b58087eb6930d8987b1a50bc2bc277d262095a96925db3f3e27fd3b3e"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["request"], "topic_agents": {"request": "cli/codex/gpt-6.1-terra"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "367d18b95f8f0d01a15ae0f4d1b70f7e13e4d0298df4215e2c449ac4905db6f9", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "93f0e8b5bdc1b40bf4ab38168e92c2772aa36747bec6add25921fbb90b909e38", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "d0f7ab4c48fcf52409935931eb9b93aacd48af4b19e9bb816fa496f1214fdb2f", "answer_contracts": "a39c9a8818afc47e059141d486337c0f12a7fd34319e2b6f7674fc428bc83e2b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "050c20aa2fdcceae10c6275fbb5f850f616ab5051bb67ccbcb4a204877a238d9", "explanation": "69bcaa207ef39d20f6a47ac201c3edf119f59b333e85131dea1bce85eef4006b", "design_response": "a7c199bc52bcc0e749ef01186e50bca98107473d5c82e2248712f465d02e1e69", "design_validation": "a4edf8364d73d169c3f10ecbadf487a8a4dc10328622d07578b281eae810c3aa"}, "validation_model": "fa46211a17e40c777f219a3bb3ef96bd8717bc81ca878dc4ca6886d133ad0b8b", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "b87a84b1bc31079837dc4dc4527ce02c9dc2cbc3a26ff7e99e0872941d213995"}, "body_sha256": "d05bc0b9fb4939505097a06637b59bf442c5889dda6d4d5641628dda824be143"}
---

# addBuffer의 전달 fence 조건

**전달 fence가 버퍼로 이동하는 조건을 확인합니다.**



## 전달 fence의 이동 조건

`Request::addBuffer()`는 세 거절 검사를 통과한 뒤 `fence && fence->isValid()`가 참이면 `setFence(std::move(fence))`를 호출해 전달받은 `fence`를 버퍼로 이동합니다. 전달받은 `fence`가 null이거나 유효하지 않으면 이 분기를 실행하지 않습니다. `src/libcamera/request.cpp:475`

<!-- sdd:visual:fence-transfer -->
### 전달 fence의 조건부 이동

```mermaid
flowchart TB
%% sdd:translations {"0 반환": "Return 0", "setFence#40;std::move#40;fence#41;#41; <br/>호출": "Call <br/>setFence#40;std::move#40;fence#41;#41;", "반환": "Return", "아니요": "No", "앞선 검사와 버퍼 연결 통과": "Earlier checks and buffer <br/>linking passed", "예": "Yes", "전달 fence가 있고 <br/>isValid#40;#41;인가?": "Is a supplied fence present <br/>and valid?", "조건 검사": "Check condition"}
  v_linked["앞선 검사와 버퍼 연결 통과"]
  v_valid{"전달 fence가 있고 <br/>isValid#40;#41;인가?"}
  v_move["setFence#40;std::move#40;fence#41;#41; <br/>호출"]
  v_done["0 반환"]
  v_linked -->|"조건 검사"| v_valid
  v_valid -->|"예"| v_move
  v_valid -->|"아니요"| v_done
  v_move -->|"반환"| v_done
```

[Mermaid 원문](camera-requests.fence-transfer.mmd)

??? note "그림 근거와 확인 범위"
    Request::addBuffer()에서 세 거절 검사를 통과한 뒤 전달받은 fence를 어떤 조건에서 버퍼로 이동합니까? fence && fence->isValid()와 setFence(std::move(fence))를 연결하고 null 또는 유효하지 않은 전달 fence에서는 이 분기를 실행하지 않는다는 점을 설명하세요. 앞선 거절 조건의 전체 설명과 실패 시 소유권·기기 동작은 제외하세요.
    
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | <span data-sdd-label-en="Earlier checks and buffer linking passed">앞선 검사와 버퍼 연결 통과</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Is a supplied fence present and valid?">전달 fence가 있고 isValid&#40;&#41;인가?</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Call setFence(std::move(fence))">setFence&#40;std::move&#40;fence&#41;&#41; 호출</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Return 0">0 반환</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Check condition">조건 검사</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Yes">예</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="No">아니요</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
    | <span data-sdd-label-en="Return">반환</span> | [src/libcamera/request.cpp:475](#source-605100b059a6864d) |
<!-- /sdd:visual:fence-transfer -->

근거 원문: [src/libcamera/request.cpp:475](#source-605100b059a6864d)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | Request::addBuffer()에서 세 거절 검사를 통과한 뒤 전달받은 fence를 어떤 조건에서 버퍼로 이동합니까? fence && fence->isValid()와 setFence(std::move(fence))를 연결하고 null 또는 유효하지 않은 전달 fence에서는 이 분기를 실행하지 않는다는 점을 설명하세요. 앞선 거절 조건의 전체 설명과 실패 시 소유권·기기 동작은 제외하세요. | [전달 fence의 이동 조건](#전달-fence의-이동-조건) | 코드 근거와 설명 연결 |

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
