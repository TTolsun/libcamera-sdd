---
generated_at: 2026-10-26T19:59:13+00:00
source_commit: 2c4b67c0792f88f69bcdf9cbf73e81b3d8cf4b6f
status: ok
section: framebuffer-allocator-boundary
generation_method: facts-and-llm
evidence_fingerprint: 3769312205c82e09f7823f75fa569e1849a3bc14f68d50ac1361cfbf73cc89e4
semantic_review: human-review-required
agent: cli/hermes/qwen3.5:9b-ctx64k
generated_design: {"schema": 1, "input_fingerprint": "3769312205c82e09f7823f75fa569e1849a3bc14f68d50ac1361cfbf73cc89e4", "answers": {"reference-lifetime": [{"text": "buffers() 함수는 allocate() 로 스트림에 버퍼를 성공적으로 할당한 후에만 호출해야 합니다.", "evidence": ["buffers-precondition"], "covers": ["reference-lifetime"], "kind": "behavior", "quote": "This function shall only be called after successfully allocating buffers for\n * \\a stream with allocate().", "part_id": "successful-allocation"}, {"text": "`buffers()` 가 반환하는 버퍼는 같은 스트림에 대한 `free()` 호출 또는 `FrameBufferAllocator` 인스턴스 파괴까지 유효합니다.", "evidence": ["buffers-validity"], "covers": ["reference-lifetime"], "kind": "behavior", "quote": "The returned buffers are valid until free() is\n * called for the same stream or the FrameBufferAllocator instance is destroyed.", "part_id": "valid-until"}], "allocation-failure": [{"text": "inserted 가 false 이면 -EBUSY 를 반환합니다.", "evidence": ["allocation-body"], "covers": ["allocation-failure"], "kind": "behavior", "quote": "if (!inserted) {\n\t\tLOG(Allocator, Error) << \"Buffers already allocated for stream\";\n\t\treturn -EBUSY;\n\t}", "part_id": "duplicate-allocation"}, {"text": "`exportFrameBuffers()` 함수가 반환한 값을 `ret` 변수에 저장한 후, `ret` 가 0 미만이면 `buffers_` 맵에서 해당 항목을 제거합니다.", "evidence": ["allocation-body"], "covers": ["allocation-failure"], "kind": "behavior", "quote": "if (ret < 0)\n\t\tbuffers_.erase(it);", "part_id": "export-failure"}, {"text": "`exportFrameBuffers`를 호출한 후 `return ret`는 두 개의 `if` 문 모두의 범위를 벗어나 있으며, 음수 여부와 관계없이 무조건 실행됩니다.", "evidence": ["export-return-code"], "covers": ["allocation-failure"], "kind": "behavior", "quote": "int ret = camera_->exportFrameBuffers(stream, &it->second);\n\tif (ret == -EINVAL)\n\t\tLOG(Allocator, Error)\n\t\t\t<< \"Stream is not part of \" << camera_->id()\n\t\t\t<< \" active configuration\";\n\n\tif (ret < 0)\n\t\tbuffers_.erase(it);\n\n\treturn ret;", "part_id": "export-return"}], "free-result": [{"text": "`FrameBufferAllocator::free` 함수에서 스트림을 찾지 못한 경우(iter == `buffers_`.end())는 -EINVAL를 반환하고, 스트림을 찾은 경우에는 `buffers_`에서 해당 항목을 제거한 후 0을 반환합니다.", "evidence": ["free-body"], "covers": ["free-result"], "kind": "behavior", "quote": "int FrameBufferAllocator::free(Stream *stream)\n{\n\tauto iter = buffers_.find(stream);\n\tif (iter == buffers_.end())\n\t\treturn -EINVAL;\n\n\tbuffers_.erase(iter);\n\n\treturn 0;\n}", "part_id": "stream-result"}]}, "topic_inputs": {"reference-lifetime": "c99e976b1205c8d9ddec43ed6bb3a1c53fb15e57142afa466ae106148c1dfb8a", "allocation-failure": "b34e73259606f373cdad813abb93a9408d61afac1640656dfe88efc4608a149d", "free-result": "18251fc854e2931ca6344b2467c89ffaf69d059289ff777782a9ac41dc220418"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["reference-lifetime", "allocation-failure", "free-result"], "topic_agents": {"reference-lifetime": "cli/hermes/qwen3.5:9b-ctx64k", "allocation-failure": "cli/hermes/qwen3.5:9b-ctx64k", "free-result": "cli/hermes/qwen3.5:9b-ctx64k"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "body_sha256": "2ef85c02e06c8e824c22fa9c56806c40f88424b17aa2625607b0160b034bd9e8"}
---

# FrameBufferAllocator의 실패와 참조 수명

**중복 할당·버퍼 내보내기 실패와 반환 버퍼의 유효기간을 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| buffers 반환 참조의 유효기간 절을 확인합니다. | [buffers 반환 참조의 유효기간](#buffers-반환-참조의-유효기간) |
| 중복 할당과 내보내기 실패를 구분하기 절을 확인합니다. | [중복 할당과 내보내기 실패를 구분하기](#중복-할당과-내보내기-실패를-구분하기) |
| free의 스트림 조회와 반환값 절을 확인합니다. | [free의 스트림 조회와 반환값](#free의-스트림-조회와-반환값) |

## buffers 반환 참조의 유효기간

buffers() 함수는 allocate() 로 스트림에 버퍼를 성공적으로 할당한 후에만 호출해야 합니다. `buffers()` 가 반환하는 버퍼는 같은 스트림에 대한 `free()` 호출 또는 `FrameBufferAllocator` 인스턴스 파괴까지 유효합니다. `src/libcamera/framebuffer_allocator.cpp:141`, `src/libcamera/framebuffer_allocator.cpp:142`

근거 원문: [src/libcamera/framebuffer_allocator.cpp:141](#source-68023250094ce1a8) · [src/libcamera/framebuffer_allocator.cpp:142](#source-d60c5ad57e6699de)

## 중복 할당과 내보내기 실패를 구분하기

inserted 가 false 이면 -EBUSY 를 반환합니다. `exportFrameBuffers()` 함수가 반환한 값을 `ret` 변수에 저장한 후, `ret` 가 0 미만이면 `buffers_` 맵에서 해당 항목을 제거합니다. `exportFrameBuffers`를 호출한 후 `return ret`는 두 개의 `if` 문 모두의 범위를 벗어나 있으며, 음수 여부와 관계없이 무조건 실행됩니다. `src/libcamera/framebuffer_allocator.cpp:86`, `src/libcamera/framebuffer_allocator.cpp:95`

근거 원문: [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) · [src/libcamera/framebuffer_allocator.cpp:95](#source-c091763d679ea029)

## free의 스트림 조회와 반환값

`FrameBufferAllocator::free` 함수에서 스트림을 찾지 못한 경우(iter == `buffers_`.end())는 -EINVAL를 반환하고, 스트림을 찾은 경우에는 `buffers_`에서 해당 항목을 제거한 후 0을 반환합니다. `src/libcamera/framebuffer_allocator.cpp:119`

근거 원문: [src/libcamera/framebuffer_allocator.cpp:119](#source-fe0210ae47a5ebe2)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | 중복 할당과 버퍼 내보내기 실패는 반환값과 할당 항목 처리에서 어떻게 다릅니까? | [중복 할당과 내보내기 실패를 구분하기](#중복-할당과-내보내기-실패를-구분하기) | 코드 근거와 설명 연결 |
    | free는 모르는 스트림과 등록된 스트림에 각각 무엇을 반환합니까? | [free의 스트림 조회와 반환값](#free의-스트림-조회와-반환값) | 코드 근거와 설명 연결 |
    | buffers를 호출할 수 있는 시점과 반환 참조의 유효기간은 무엇입니까? | [buffers 반환 참조의 유효기간](#buffers-반환-참조의-유효기간) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-68023250094ce1a8"></a>

??? note "소스 근거: src/libcamera/framebuffer_allocator.cpp:141"
    `src/libcamera/framebuffer_allocator.cpp:141`에서 시작하는 발췌입니다. 종료 줄은 142이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `a12056e800d2035f519dc58a4be3dc5e3c9d51920102cc9bc27c60a32790a663`
    
    ```text
    This function shall only be called after successfully allocating buffers for
     * \a stream with allocate().
    ```

<a id="source-d60c5ad57e6699de"></a>

??? note "소스 근거: src/libcamera/framebuffer_allocator.cpp:142"
    `src/libcamera/framebuffer_allocator.cpp:142`에서 시작하는 발췌입니다. 종료 줄은 143이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `7c43c6133e383a9e56e3a9163cfca05e8df576398f363e1b13bd5056664df86b`
    
    ```text
    The returned buffers are valid until free() is
     * called for the same stream or the FrameBufferAllocator instance is destroyed.
    ```

<a id="source-78a6c2f7dbdebb0f"></a>

??? note "소스 근거: src/libcamera/framebuffer_allocator.cpp:86"
    `src/libcamera/framebuffer_allocator.cpp:86`에서 시작하는 발췌입니다. 종료 줄은 105이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `0f275b59a26e4fac5b45597e08d8cf991937d31ad9e15675d574243fc7c1d63b`
    
    ```text
    int FrameBufferAllocator::allocate(Stream *stream)
    {
    	const auto &[it, inserted] = buffers_.try_emplace(stream);
    
    	if (!inserted) {
    		LOG(Allocator, Error) << "Buffers already allocated for stream";
    		return -EBUSY;
    	}
    
    	int ret = camera_->exportFrameBuffers(stream, &it->second);
    	if (ret == -EINVAL)
    		LOG(Allocator, Error)
    			<< "Stream is not part of " << camera_->id()
    			<< " active configuration";
    
    	if (ret < 0)
    		buffers_.erase(it);
    
    	return ret;
    }
    ```

<a id="source-c091763d679ea029"></a>

??? note "소스 근거: src/libcamera/framebuffer_allocator.cpp:95"
    `src/libcamera/framebuffer_allocator.cpp:95`에서 시작하는 발췌입니다. 종료 줄은 104이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `338a363feb53fd2928cc9b6d8a4d32dbfa921f4143079264e4264f9eae921b1e`
    
    ```text
    int ret = camera_->exportFrameBuffers(stream, &it->second);
    	if (ret == -EINVAL)
    		LOG(Allocator, Error)
    			<< "Stream is not part of " << camera_->id()
    			<< " active configuration";
    
    	if (ret < 0)
    		buffers_.erase(it);
    
    	return ret;
    ```

<a id="source-fe0210ae47a5ebe2"></a>

??? note "소스 근거: src/libcamera/framebuffer_allocator.cpp:119"
    `src/libcamera/framebuffer_allocator.cpp:119`에서 시작하는 발췌입니다. 종료 줄은 128이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `17715b15ff5a7663326b0ac1cd2248be6bf221eaa7551d1579901a1bb87ff6a6`
    
    ```text
    int FrameBufferAllocator::free(Stream *stream)
    {
    	auto iter = buffers_.find(stream);
    	if (iter == buffers_.end())
    		return -EINVAL;
    
    	buffers_.erase(iter);
    
    	return 0;
    }
    ```

??? note "근거와 검토 정보"
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `src/libcamera/framebuffer_allocator.cpp`
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `2c4b67c079`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-27 · 사람 검토 전

다음 단계: [Camera·Request와 버퍼 참조의 책임](camera-model.md)
