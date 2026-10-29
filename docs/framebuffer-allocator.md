---
generated_at: 2026-10-29T20:32:20+00:00
source_commit: 212c689fcf2450bbfbaab25c7472895ac277b5d6
status: ok
section: framebuffer-allocator-boundary
generation_method: facts-and-llm
evidence_fingerprint: 57fc838cc6da7a358e10f3e84a194a32b88cd213227f3319a95cc0beb6371c81
semantic_review: human-review-required
agent: cli/codex/gpt-6.1-terra
generated_design: {"schema": 1, "input_fingerprint": "57fc838cc6da7a358e10f3e84a194a32b88cd213227f3319a95cc0beb6371c81", "answers": {"reference-lifetime": [{"text": "`buffers()`는 해당 스트림에 대해 `allocate()`로 버퍼 할당이 성공한 후에만 호출해야 합니다.", "evidence": ["buffers-precondition"], "covers": ["reference-lifetime"], "kind": "behavior", "quote": "This function shall only be called after successfully allocating buffers for\n * \\a stream with allocate().", "part_id": "successful-allocation"}, {"text": "`buffers()`가 반환하는 버퍼는 같은 스트림에 대해 `free()`가 호출되거나 `FrameBufferAllocator` 인스턴스가 파괴될 때까지 유효합니다.", "evidence": ["buffers-validity"], "covers": ["reference-lifetime"], "kind": "behavior", "quote": "The returned buffers are valid until free() is\n * called for the same stream or the FrameBufferAllocator instance is destroyed.", "part_id": "valid-until"}], "allocation-failure": [{"text": "`FrameBufferAllocator::allocate`는 `try_emplace`의 `inserted`가 false이면 오류를 기록하고 `-EBUSY`를 반환합니다.", "evidence": ["allocation-body"], "covers": ["allocation-failure"], "kind": "behavior", "quote": "if (!inserted) {\n\t\tLOG(Allocator, Error) << \"Buffers already allocated for stream\";\n\t\treturn -EBUSY;\n\t}", "part_id": "duplicate-allocation"}, {"text": "`FrameBufferAllocator::allocate()`는 `exportFrameBuffers()`가 반환한 값을 `ret`에 저장하고, `ret`가 음수이면 `buffers_.erase(it)`로 해당 `buffers_` 항목을 제거합니다.", "evidence": ["allocation-body"], "covers": ["allocation-failure"], "kind": "behavior", "quote": "if (ret < 0)\n\t\tbuffers_.erase(it);", "part_id": "export-failure"}, {"text": "`FrameBufferAllocator::allocate`는 `exportFrameBuffers`를 호출한 경우 그 결과인 `ret`를 음수 여부와 관계없이 반환합니다.", "evidence": ["export-return-code"], "covers": ["allocation-failure"], "kind": "behavior", "quote": "int ret = camera_->exportFrameBuffers(stream, &it->second);\n\tif (ret == -EINVAL)\n\t\tLOG(Allocator, Error)\n\t\t\t<< \"Stream is not part of \" << camera_->id()\n\t\t\t<< \" active configuration\";\n\n\tif (ret < 0)\n\t\tbuffers_.erase(it);\n\n\treturn ret;", "part_id": "export-return"}], "free-result": [{"text": "`FrameBufferAllocator::free`는 스트림을 찾지 못하면 `-EINVAL`을 반환하고 `buffers_` 항목을 제거하지 않습니다. 스트림을 찾으면 해당 `buffers_` 항목을 제거하고 `0`을 반환합니다.", "evidence": ["free-body"], "covers": ["free-result"], "kind": "behavior", "quote": "int FrameBufferAllocator::free(Stream *stream)\n{\n\tauto iter = buffers_.find(stream);\n\tif (iter == buffers_.end())\n\t\treturn -EINVAL;\n\n\tbuffers_.erase(iter);\n\n\treturn 0;\n}", "part_id": "stream-result"}]}, "topic_inputs": {"reference-lifetime": "bfd8f90ce8078127a72812e6be3d0e3989f28919ced42f40224197654c300192", "allocation-failure": "f711f3297de9c282dc40a72b7915d964b1a13b5ad0f1ea391f2f1d091e15f57e", "free-result": "bc1a6d637b585bc7000999f56328d022149508092487f3f0cb3072d289394858"}, "reused_topics": [], "replayed_units": [], "generated_topics": ["reference-lifetime", "allocation-failure", "free-result"], "topic_agents": {"reference-lifetime": "cli/codex/gpt-6.1-terra", "allocation-failure": "cli/codex/gpt-6.1-terra", "free-result": "cli/codex/gpt-6.1-terra"}, "grounding_review": "passed", "grounding_policy": "3c9673abb403dee9aa554ee5b3c549ebfe95bb18ec0e9cd7bf6e495e060439c2", "validation_policy": {"manuscript": "e0c429a5c80a01c34563ce00a616df89d8f75c735f8669bcbd1f75d84cce82a6", "semantic": "571896e4854c21322a1ce4580107c235cae5a9f94e71adc8c97a7e2897405968", "duplicates": "d4af3d834d8b1c99a6c9311612712a64112c30fa4621b375904d172f361285b8", "design_contracts": "9f54ecddce57c7a9caa6c02af77904b57eff2471f2a052951c1cffd18256a4f0", "validate": "78d29ffd1bf6235067edf5a0c7d9b1290f1f11e90599605a0e192e90be5f3372", "reader_profiles": "ad9005d08295212371f59e8934ace86786c0683f7a4c416301ee0e0cadc8b797", "contract_schema": "fecc4ee78a481139776e562c164c0da9a3e5edf0a64a72be1d1c8feddee3cd08", "answer_contracts": "1e0d24e0cf26ded53ecec2e5a6fbc51836bac6e17530318a9fa7cffaa936c00b", "reader_scope": "1b9c26b10b74ae8cf034f5863cbac2114e1d844e5d8332eb1f10562a18371782", "product_context": "9db4d42a710b4a71a7d2bb16f69db06926409281dc1a200c796e77d5deaa25a0", "design_response": "74ebb2d21768d6bdd4ef7611c1c539526a7e72e6a58604c82e8305003d24f8b7", "design_validation": "b8133c78a8eb42fd5194c2756bb649b396ec54b40c49b72544bdbbcaf3366c57"}, "validation_model": "44197615786b818e4d9150110e74bef6772ea4f261a58d27ac12f379abaeb439", "style_policy": {"fluent-korean.md": "ce5aa71e58371e3fc02ff8cb165e07c9234f5166f6541423a91cc4cb40878975", "i-have-adhd.md": "3170b16ace00aecb0dd7feb54c0b5aa642e7502acda06ecd24fd89a11c7127e9", "README.md": "f8fd5a3d8041c23fc68b93ff32b8727e98393383b5099032eb00ad0013e7611c"}, "checkpoint_units": [{"checkpoint": "73215689ebb04c1c1ff3e1f8c20af305de4bfa4f74eae173d68aba6be0abfdb5.json", "topic": "reference-lifetime", "part": "successful-allocation", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/587.receipt.json", "60b1bf48442840808eecd0e46851648e/588.receipt.json"]}, {"checkpoint": "4513b00d9337afc0d05c63909dd4f1b628b138f6f3926d019945e7a32fafe362.json", "topic": "reference-lifetime", "part": "valid-until", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/589.receipt.json", "60b1bf48442840808eecd0e46851648e/590.receipt.json"]}, {"checkpoint": "fc94bb6a6010a35b608ce2a32d867214ac920a90f9097ace682a32af614bd212.json", "topic": "allocation-failure", "part": "duplicate-allocation", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/591.receipt.json", "60b1bf48442840808eecd0e46851648e/592.receipt.json"]}, {"checkpoint": "eac444ea64b4f7febaf7ac0cf61e73fb4018aa81b4c3cbf6ca81969d8dbb3d44.json", "topic": "allocation-failure", "part": "export-failure", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/593.receipt.json", "60b1bf48442840808eecd0e46851648e/594.receipt.json"]}, {"checkpoint": "cc8496e0177334c1172666a971952e63f98418d5ff25495803cef192686deeff.json", "topic": "allocation-failure", "part": "export-return", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["f7b6af75301a420fbd92d0ecc1280cfc/048.receipt.json", "f7b6af75301a420fbd92d0ecc1280cfc/049.receipt.json"]}, {"checkpoint": "4168067e027380db7d7b9e6ef206521e9cda0527ea246baae29edb2ec9e03d97.json", "topic": "free-result", "part": "stream-result", "subpart": null, "revalidated": false, "new_grounding_review": false, "receipts": ["60b1bf48442840808eecd0e46851648e/597.receipt.json", "60b1bf48442840808eecd0e46851648e/598.receipt.json"]}], "body_sha256": "399e39be49d634e59f93ad7c7e613d019a03a54ab230ae243a44064537da06e8"}
---

# FrameBufferAllocator의 실패와 참조 수명

**중복 할당·버퍼 내보내기 실패와 반환 버퍼의 유효기간을 확인하세요.**

| 지금 확인할 내용 | 이동할 절 |
|---|---|
| `buffers()`는 해당 스트림에 대해 `allocate()`로 버퍼 할당이 성공한 후에만 호출해야 합니다. | [buffers 반환 참조의 유효기간](#buffers-반환-참조의-유효기간) |
| `FrameBufferAllocator::allocate`는 `try_emplace`의 `inserted`가 false이면 오류를 기록하고 `-EBUSY`를 반환합니다. | [중복 할당과 내보내기 실패를 구분하기](#중복-할당과-내보내기-실패를-구분하기) |
| `FrameBufferAllocator::free`는 스트림을 찾지 못하면 `-EINVAL`을 반환하고 `buffers_` 항목을 제거하지 않습니다. | [free의 스트림 조회와 반환값](#free의-스트림-조회와-반환값) |

## buffers 반환 참조의 유효기간

`buffers()`는 해당 스트림에 대해 `allocate()`로 버퍼 할당이 성공한 후에만 호출해야 합니다. `buffers()`가 반환하는 버퍼는 같은 스트림에 대해 `free()`가 호출되거나 `FrameBufferAllocator` 인스턴스가 파괴될 때까지 유효합니다. `src/libcamera/framebuffer_allocator.cpp:141`, `src/libcamera/framebuffer_allocator.cpp:142`

근거 원문: [src/libcamera/framebuffer_allocator.cpp:141](#source-68023250094ce1a8) · [src/libcamera/framebuffer_allocator.cpp:142](#source-d60c5ad57e6699de)

## 중복 할당과 내보내기 실패를 구분하기

`FrameBufferAllocator::allocate`는 `try_emplace`의 `inserted`가 false이면 오류를 기록하고 `-EBUSY`를 반환합니다. `FrameBufferAllocator::allocate()`는 `exportFrameBuffers()`가 반환한 값을 `ret`에 저장하고, `ret`가 음수이면 `buffers_.erase(it)`로 해당 `buffers_` 항목을 제거합니다. `FrameBufferAllocator::allocate`는 `exportFrameBuffers`를 호출한 경우 그 결과인 `ret`를 음수 여부와 관계없이 반환합니다. `src/libcamera/framebuffer_allocator.cpp:86`, `src/libcamera/framebuffer_allocator.cpp:95`

근거 원문: [src/libcamera/framebuffer_allocator.cpp:86](#source-78a6c2f7dbdebb0f) · [src/libcamera/framebuffer_allocator.cpp:95](#source-c091763d679ea029)

## free의 스트림 조회와 반환값

`FrameBufferAllocator::free`는 스트림을 찾지 못하면 `-EINVAL`을 반환하고 `buffers_` 항목을 제거하지 않습니다. 스트림을 찾으면 해당 `buffers_` 항목을 제거하고 `0`을 반환합니다. `src/libcamera/framebuffer_allocator.cpp:119`

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
    - 근거 수준: 코드 확인 (정적 분석, simple_compdb 구성, commit `212c689fcf`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-30 · 사람 검토 전

다음 단계: [Camera·Request와 버퍼 참조의 책임](camera-model.md)
