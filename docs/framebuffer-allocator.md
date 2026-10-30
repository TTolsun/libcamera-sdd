---
generated_at: 2026-10-30T15:19:58+00:00
source_commit: 293d751a814e0d4c34e85ad457ccd9d5eefd1a61
status: ok
section: framebuffer-allocator-boundary
generation_method: facts-and-llm
evidence_fingerprint: 74b130a1fd4056efc0d8e01b5f68bb145d8f2bd2018eb8e99792840359a81940
semantic_review: human-review-required
agent: cli/claude/claude-haiku-5-5
generated_design: {"schema": 1, "input_fingerprint": "74b130a1fd4056efc0d8e01b5f68bb145d8f2bd2018eb8e99792840359a81940", "answers": {"allocation-preconditions": [{"text": "`allocate()`를 호출하기 전에 카메라는 `Camera::configure()`로 미리 구성되어 있고 정지해야 하며, 스트림은 활성 카메라 구성에 속해야 합니다.", "evidence": ["allocate-preconditions"], "covers": ["allocation-preconditions"], "kind": "behavior", "quote": "Allocate buffers suitable for capturing frames from the \\a stream. The Camera\n * shall have been previously configured with Camera::configure() and shall be\n * stopped, and the stream shall be part of the active camera configuration.", "part_id": "configured-stopped-stream"}, {"text": "카메라 상태가 버퍼를 할당할 수 없는 경우에는 `-EACCES`가 반환되고, `stream`이 카메라에 속하지 않거나 활성 카메라 구성의 일부가 아닌 경우에는 `-EINVAL`이 반환됩니다.", "evidence": ["allocate-state-stream-errors"], "covers": ["allocation-preconditions"], "kind": "behavior", "quote": "\\retval -EACCES The camera is not in a state where buffers can be allocated\n * \\retval -EINVAL The \\a stream does not belong to the camera or the stream is\n * not part of the active camera configuration", "part_id": "access-stream-errors"}], "reference-lifetime": [{"text": "`buffers()`는 해당 스트림에 대해 `allocate()`로 버퍼 할당이 성공한 뒤에만 호출해야 합니다.", "evidence": ["buffers-precondition"], "covers": ["reference-lifetime"], "kind": "behavior", "quote": "This function shall only be called after successfully allocating buffers for\n * \\a stream with allocate().", "part_id": "successful-allocation"}, {"text": "`buffers()`가 반환하는 버퍼는 같은 스트림에 대해 `free()`가 호출되거나 `FrameBufferAllocator` 인스턴스가 파괴될 때까지 유효합니다.", "evidence": ["buffers-validity"], "covers": ["reference-lifetime"], "kind": "behavior", "quote": "The returned buffers are valid until free() is\n * called for the same stream or the FrameBufferAllocator instance is destroyed.", "part_id": "valid-until"}], "allocation-failure": [{"text": "`try_emplace`의 `inserted`가 `false`이면 `FrameBufferAllocator::allocate()`는 \"Buffers already allocated for stream\" 오류 로그를 남기고 `-EBUSY`를 반환합니다.", "evidence": ["allocation-body"], "covers": ["allocation-failure"], "kind": "behavior", "quote": "if (!inserted) {\n\t\tLOG(Allocator, Error) << \"Buffers already allocated for stream\";\n\t\treturn -EBUSY;\n\t}", "part_id": "duplicate-allocation"}, {"text": "`camera_->exportFrameBuffers(stream, &it->second)`가 반환한 값은 변수 `ret`에 저장됩니다. 따라서 `exportFrameBuffers()`는 함수이고 `ret`는 그 반환값을 담는 변수입니다. `ret`가 음수, 즉 `ret < 0`이면 `allocate()`는 `buffers_.erase(it)`를 실행해 `it`가 가리키는 `buffers_` 항목을 제거합니다.", "evidence": ["allocation-body"], "covers": ["allocation-failure"], "kind": "behavior", "quote": "if (ret < 0)\n\t\tbuffers_.erase(it);", "part_id": "export-failure"}, {"text": "`FrameBufferAllocator::allocate`는 `exportFrameBuffers` 호출 결과인 `ret`를 음수 여부와 관계없이 그대로 반환합니다.", "evidence": ["export-return-code"], "covers": ["allocation-failure"], "kind": "behavior", "quote": "int ret = camera_->exportFrameBuffers(stream, &it->second);\n\tif (ret == -EINVAL)\n\t\tLOG(Allocator, Error)\n\t\t\t<< \"Stream is not part of \" << camera_->id()\n\t\t\t<< \" active configuration\";\n\n\tif (ret < 0)\n\t\tbuffers_.erase(it);\n\n\treturn ret;", "part_id": "export-return"}], "free-result": [{"text": "`stream`을 찾지 못하면, 즉 `iter`가 `buffers_.end()`와 같으면 `-EINVAL`을 반환하고 `buffers_`의 항목을 제거하지 않습니다. 스트림을 찾은 경우에는 해당 항목을 `buffers_.erase(iter)`로 삭제한 뒤 `0`을 반환합니다.", "evidence": ["free-body"], "covers": ["free-result"], "kind": "behavior", "quote": "int FrameBufferAllocator::free(Stream *stream)\n{\n\tauto iter = buffers_.find(stream);\n\tif (iter == buffers_.end())\n\t\treturn -EINVAL;\n\n\tbuffers_.erase(iter);\n\n\treturn 0;\n}", "part_id": "stream-result"}]}, "topic_inputs": {"allocation-preconditions": "2138789efeb5033a0c2637a8eac70574f8b0da08e1b935984202c6e0e7b3df2c", "reference-lifetime": "5765bec2e7b60101b21e3096287a37e5b743ad4c911ae92980d136ea6550b75e", "allocation-failure": "ee20435bff38889422cbf42df9ac898a036549770d87bab4d39e180c82999620", "free-result": "437c508e4a6aa9863fc93a37244afb62f8b6f34e69e4379bbb389cf1d4a0060b"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["allocation-preconditions", "reference-lifetime", "allocation-failure", "free-result"], "topic_agents": {"allocation-preconditions": "cli/claude/claude-haiku-5-5", "reference-lifetime": "cli/claude/claude-haiku-5-5", "allocation-failure": "cli/claude/claude-haiku-5-5", "free-result": "cli/claude/claude-haiku-5-5"}, "grounding_review": "not-run", "grounding_policy": null, "validation_policy": {"manuscript": "e0c429a5c80a01c34563ce00a616df89d8f75c735f8669bcbd1f75d84cce82a6", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "281d217a1d4a212dd56cdb3ce61e9fae7a4622099962c1beee847a57866e83e0", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "fecc4ee78a481139776e562c164c0da9a3e5edf0a64a72be1d1c8feddee3cd08", "answer_contracts": "1e0d24e0cf26ded53ecec2e5a6fbc51836bac6e17530318a9fa7cffaa936c00b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "9db4d42a710b4a71a7d2bb16f69db06926409281dc1a200c796e77d5deaa25a0", "design_response": "74ebb2d21768d6bdd4ef7611c1c539526a7e72e6a58604c82e8305003d24f8b7", "design_validation": "b8133c78a8eb42fd5194c2756bb649b396ec54b40c49b72544bdbbcaf3366c57"}, "validation_model": "6d7b40d6cf6b277e785cb3b10128faa4707edc543d8ca670138f358e37cf5bd9", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "f8fd5a3d8041c23fc68b93ff32b8727e98393383b5099032eb00ad0013e7611c"}, "checkpoint_units": [{"checkpoint": "8994ab2929f1e579fb20e3eeae2b55e1e1028fc25616afc8e589ffe847613edf.json", "topic": "allocation-preconditions", "part": "configured-stopped-stream", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["3e26e44c94c6440da01911b135421971/001.receipt.json", "3e26e44c94c6440da01911b135421971/002.receipt.json"]}], "body_sha256": "d42900c9596f896045eb95ad285229756594b6537f77db4af57364318c36071e"}
revalidated_from: 212c689fcf2450bbfbaab25c7472895ac277b5d6
---

# FrameBufferAllocator의 실패와 참조 수명

**중복 할당·버퍼 내보내기 실패와 반환 버퍼의 유효기간을 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| `allocate()`를 호출하기 전에 카메라는 `Camera::configure()`로 미리 구성되어 있고 정지해야 하며, 스트림은 활성 카메라 구성에 속해야 합니다. | [할당 전에 확인할 카메라 상태와 스트림](#할당-전에-확인할-카메라-상태와-스트림) |
| `buffers()`는 해당 스트림에 대해 `allocate()`로 버퍼 할당이 성공한 뒤에만 호출해야 합니다. | [buffers 반환 참조의 유효기간](#buffers-반환-참조의-유효기간) |
| `try_emplace`의 `inserted`가 `false`이면 `FrameBufferAllocator::allocate()`는 "Buffers already allocated for stream" 오류 로그를 남기고 `-EBUSY`를 반환합니다. | [중복 할당과 내보내기 실패를 구분하기](#중복-할당과-내보내기-실패를-구분하기) |
| `stream`을 찾지 못하면, 즉 `iter`가 `buffers_.end()`와 같으면 `-EINVAL`을 반환하고 `buffers_`의 항목을 제거하지 않습니다. | [free의 스트림 조회와 반환값](#free의-스트림-조회와-반환값) |

## 할당 전에 확인할 카메라 상태와 스트림

`allocate()`를 호출하기 전에 카메라는 `Camera::configure()`로 미리 구성되어 있고 정지해야 하며, 스트림은 활성 카메라 구성에 속해야 합니다. 카메라 상태가 버퍼를 할당할 수 없는 경우에는 `-EACCES`가 반환되고, `stream`이 카메라에 속하지 않거나 활성 카메라 구성의 일부가 아닌 경우에는 `-EINVAL`이 반환됩니다. `src/libcamera/framebuffer_allocator.cpp:72`, `src/libcamera/framebuffer_allocator.cpp:81`

근거 원문: [src/libcamera/framebuffer_allocator.cpp:72](#source-4f32d036f2dee319) · [src/libcamera/framebuffer_allocator.cpp:81](#source-224d9d0ce4f1ad7f)

## buffers 반환 참조의 유효기간

`buffers()`는 해당 스트림에 대해 `allocate()`로 버퍼 할당이 성공한 뒤에만 호출해야 합니다. `buffers()`가 반환하는 버퍼는 같은 스트림에 대해 `free()`가 호출되거나 `FrameBufferAllocator` 인스턴스가 파괴될 때까지 유효합니다. `src/libcamera/framebuffer_allocator.cpp:141`, `src/libcamera/framebuffer_allocator.cpp:142`

근거 원문: [src/libcamera/framebuffer_allocator.cpp:141](#source-68023250094ce1a8) · [src/libcamera/framebuffer_allocator.cpp:142](#source-d60c5ad57e6699de)

## 중복 할당과 내보내기 실패를 구분하기

`try_emplace`의 `inserted`가 `false`이면 `FrameBufferAllocator::allocate()`는 "Buffers already allocated for stream" 오류 로그를 남기고 `-EBUSY`를 반환합니다. `camera_->exportFrameBuffers(stream, &it->second)`가 반환한 값은 변수 `ret`에 저장됩니다. 따라서 `exportFrameBuffers()`는 함수이고 `ret`는 그 반환값을 담는 변수입니다. `ret`가 음수, 즉 `ret < 0`이면 `allocate()`는 `buffers_.erase(it)`를 실행해 `it`가 가리키는 `buffers_` 항목을 제거합니다. `src/libcamera/framebuffer_allocator.cpp:86`

`FrameBufferAllocator::allocate`는 `exportFrameBuffers` 호출 결과인 `ret`를 음수 여부와 관계없이 그대로 반환합니다. `src/libcamera/framebuffer_allocator.cpp:95`

근거 원문: [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) · [src/libcamera/framebuffer_allocator.cpp:95](#source-c091763d679ea029)

## free의 스트림 조회와 반환값

`stream`을 찾지 못하면, 즉 `iter`가 `buffers_.end()`와 같으면 `-EINVAL`을 반환하고 `buffers_`의 항목을 제거하지 않습니다. 스트림을 찾은 경우에는 해당 항목을 `buffers_.erase(iter)`로 삭제한 뒤 `0`을 반환합니다. `src/libcamera/framebuffer_allocator.cpp:119`

근거 원문: [src/libcamera/framebuffer_allocator.cpp:119](#source-fe0210ae47a5ebe2)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | allocate를 호출하기 위한 카메라·스트림 조건과 상태·스트림 오류의 원인은 무엇입니까? | [할당 전에 확인할 카메라 상태와 스트림](#할당-전에-확인할-카메라-상태와-스트림) | 코드 근거와 설명 연결 |
    | 중복 할당과 버퍼 내보내기 실패는 반환값과 할당 항목 처리에서 어떻게 다릅니까? | [중복 할당과 내보내기 실패를 구분하기](#중복-할당과-내보내기-실패를-구분하기) | 코드 근거와 설명 연결 |
    | free는 모르는 스트림과 등록된 스트림에 각각 무엇을 반환합니까? | [free의 스트림 조회와 반환값](#free의-스트림-조회와-반환값) | 코드 근거와 설명 연결 |
    | buffers를 호출할 수 있는 시점과 반환 참조의 유효기간은 무엇입니까? | [buffers 반환 참조의 유효기간](#buffers-반환-참조의-유효기간) | 코드 근거와 설명 연결 |

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-4f32d036f2dee319"></a>

??? note "소스 근거: src/libcamera/framebuffer_allocator.cpp:72"
    `src/libcamera/framebuffer_allocator.cpp:72`에서 시작하는 발췌입니다. 종료 줄은 74이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `87ee819fc59da5231c8e99985771ae1821150196f2ed452822578208da94972f`
    
    ```text
    Allocate buffers suitable for capturing frames from the \a stream. The Camera
     * shall have been previously configured with Camera::configure() and shall be
     * stopped, and the stream shall be part of the active camera configuration.
    ```

<a id="source-224d9d0ce4f1ad7f"></a>

??? note "소스 근거: src/libcamera/framebuffer_allocator.cpp:81"
    `src/libcamera/framebuffer_allocator.cpp:81`에서 시작하는 발췌입니다. 종료 줄은 83이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `46d80bb2f91831ad0dda0a83fea0d3139ce6c0f156cf75033d97a9947cafde1e`
    
    ```text
    \retval -EACCES The camera is not in a state where buffers can be allocated
     * \retval -EINVAL The \a stream does not belong to the camera or the stream is
     * not part of the active camera configuration
    ```

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
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `212c689fcf`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-31 · 사람 검토 전

다음 단계: [Camera·Request와 버퍼 참조의 책임](camera-model.md)
