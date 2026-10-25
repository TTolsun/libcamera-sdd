---
generated_at: 2026-10-25T10:25:04+00:00
source_commit: f058f7908e135eb6c518168dae297b81d5527b3e
status: ok
section: completion-demo
generation_method: source-question
evidence_fingerprint: 1915a734b8d0dd3179df065697afc4e5d67dd6becd912309519afae968c45970
semantic_review: human-review-required
generated_visuals: {"schema": 1, "records": {"completion-branches": {"input_fingerprint": "60e051e0b5a85ff92ddc2f34cc604ed3a7bd6284c35afef799c104f80adea4f0", "draft": {"nodes": {"n0": {"label": "runPipes 실행 후 결과 반환값 확인", "label_en": "Check return value after runPipes execution", "shape": "process", "quote_ids": ["on-frame:0"]}, "n1": {"label": "성공 시 결과 전송 (ret >= 0)", "label_en": "Send result on success (ret >= 0)", "shape": "process", "quote_ids": ["on-frame:0"]}, "n2": {"label": "성공 또는 실패 후 완료 호출", "label_en": "Call done callback on success or failure", "shape": "process", "quote_ids": ["on-frame:0"]}}, "edges": [{"from": "n0", "to": "n1", "label": "ret >= 0", "label_en": "ret >= 0", "condition_ref": "c0:true", "quote_ids": ["on-frame:0"]}, {"from": "n0", "to": "n2", "label": "항상 호출됨 (성공/실패 모두)", "label_en": "Always called (success/failure both)", "condition_ref": "always", "quote_ids": ["on-frame:0"]}]}, "graph": {"id": "completion-branches", "topic": "completion", "kind": "decision", "title": "파이프 결과와 완료 처리의 분기", "question": "RequestManager::onFrame에서 runPipes, sendResult, onFrameDone의 연결을 그리세요. 결과 전송 조건의 condition_ref를 원문 조건 ID의 참·거짓으로 선택하고 성공·실패 경로를 구분하세요. onFrameDone이 성공·실패 양쪽에서 호출되는 것을 보존하세요. 기기 동작이나 스레드 보장은 추정하지 마세요. 세 호출을 각각 한 노드로 표현하며 진입점·변수·성공실패별 가상 상태 노드는 추가하지 마세요.", "nodes": [{"id": "n0", "label": "runPipes 실행 후 결과 반환값 확인", "label_en": "Check return value after runPipes execution", "shape": "box", "evidence": [{"source": "completion/on-frame", "sha256": "64ce50dbc9085701f44bbba8bc5573bc9ed24bb9eedbc15e7676446eb4f629fe", "quote": "void RequestManager::onFrame(Frame &frame) {\n    FrameFactory &factory = frame.isPreview ? static_cast<FrameFactory &>(previewFactory_)\n                                            : static_cast<FrameFactory &>(captureFactory_);\n    int ret = factory.runPipes(frame);\n    if (ret >= 0) {\n        sendResult(frame);\n    }\n    onFrameDone(frame);\n}"}]}, {"id": "n1", "label": "성공 시 결과 전송 (ret >= 0)", "label_en": "Send result on success (ret >= 0)", "shape": "box", "evidence": [{"source": "completion/on-frame", "sha256": "64ce50dbc9085701f44bbba8bc5573bc9ed24bb9eedbc15e7676446eb4f629fe", "quote": "void RequestManager::onFrame(Frame &frame) {\n    FrameFactory &factory = frame.isPreview ? static_cast<FrameFactory &>(previewFactory_)\n                                            : static_cast<FrameFactory &>(captureFactory_);\n    int ret = factory.runPipes(frame);\n    if (ret >= 0) {\n        sendResult(frame);\n    }\n    onFrameDone(frame);\n}"}]}, {"id": "n2", "label": "성공 또는 실패 후 완료 호출", "label_en": "Call done callback on success or failure", "shape": "box", "evidence": [{"source": "completion/on-frame", "sha256": "64ce50dbc9085701f44bbba8bc5573bc9ed24bb9eedbc15e7676446eb4f629fe", "quote": "void RequestManager::onFrame(Frame &frame) {\n    FrameFactory &factory = frame.isPreview ? static_cast<FrameFactory &>(previewFactory_)\n                                            : static_cast<FrameFactory &>(captureFactory_);\n    int ret = factory.runPipes(frame);\n    if (ret >= 0) {\n        sendResult(frame);\n    }\n    onFrameDone(frame);\n}"}]}], "edges": [{"from": "n0", "to": "n1", "label": "ret >= 0 · ret >= 0 [true]", "label_en": "ret >= 0 · ret >= 0 [true]", "evidence": [{"source": "completion/on-frame", "sha256": "64ce50dbc9085701f44bbba8bc5573bc9ed24bb9eedbc15e7676446eb4f629fe", "quote": "void RequestManager::onFrame(Frame &frame) {\n    FrameFactory &factory = frame.isPreview ? static_cast<FrameFactory &>(previewFactory_)\n                                            : static_cast<FrameFactory &>(captureFactory_);\n    int ret = factory.runPipes(frame);\n    if (ret >= 0) {\n        sendResult(frame);\n    }\n    onFrameDone(frame);\n}"}]}, {"from": "n0", "to": "n2", "label": "항상 호출됨 (성공/실패 모두)", "label_en": "Always called (success/failure both)", "evidence": [{"source": "completion/on-frame", "sha256": "64ce50dbc9085701f44bbba8bc5573bc9ed24bb9eedbc15e7676446eb4f629fe", "quote": "void RequestManager::onFrame(Frame &frame) {\n    FrameFactory &factory = frame.isPreview ? static_cast<FrameFactory &>(previewFactory_)\n                                            : static_cast<FrameFactory &>(captureFactory_);\n    int ret = factory.runPipes(frame);\n    if (ret >= 0) {\n        sendResult(frame);\n    }\n    onFrameDone(frame);\n}"}]}], "producer": "ollama/qwen3.5:9b"}, "producer": "ollama/qwen3.5:9b", "generation_commit": "f058f7908e135eb6c518168dae297b81d5527b3e", "reused": false}}, "body_sha256": "0e318e11870633d14d2d20781a2e43f0598442ea57412323e20c031af98fb1f5"}
---

# 공개 mini HAL의 완료 분기

**파이프 반환 조건과 완료 정리를 소스와 함께 확인하세요.**



## 결과 전송과 프레임 정리

RequestManager::onFrame에서 runPipes 반환값에 따른 sendResult 조건과 onFrameDone 호출을 설명하세요. if 블록 안팎을 구분하고 실패 시 정리도 설명하세요. 실행 스레드나 성공 보장을 추정하지 마세요.

<!-- sdd:visual:completion-branches -->
### 파이프 결과와 완료 처리의 분기

RequestManager::onFrame에서 runPipes, sendResult, onFrameDone의 연결을 그리세요. 결과 전송 조건의 condition_ref를 원문 조건 ID의 참·거짓으로 선택하고 성공·실패 경로를 구분하세요. onFrameDone이 성공·실패 양쪽에서 호출되는 것을 보존하세요. 기기 동작이나 스레드 보장은 추정하지 마세요. 세 호출을 각각 한 노드로 표현하며 진입점·변수·성공실패별 가상 상태 노드는 추가하지 마세요.

LLM 그림 초안 · 사람 검토 전

작성 모델: `ollama/qwen3.5:9b`

```mermaid
flowchart TB
%% sdd:translations {"ret &gt;= 0 · ret &gt;= 0 [true]": "ret &gt;= 0 · ret &gt;= 0 [true]", "runPipes 실행 후 결과 <br/>반환값 확인": "Check return value after <br/>runPipes execution", "성공 또는 실패 후 완료 호출": "Call done callback on <br/>success or failure", "성공 시 결과 전송 (ret &gt;= 0)": "Send result on success (ret <br/>&gt;= 0)", "항상 호출됨 (성공/실패 모두)": "Always called <br/>(success/failure both)"}
  v_n0["runPipes 실행 후 결과 <br/>반환값 확인"]
  v_n1["성공 시 결과 전송 (ret &gt;= 0)"]
  v_n2["성공 또는 실패 후 완료 호출"]
  v_n0 -->|"ret &gt;= 0 · ret &gt;= 0 [true]"| v_n1
  v_n0 -->|"항상 호출됨 (성공/실패 모두)"| v_n2
```

[Mermaid 원문](completion.completion-branches.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | runPipes 실행 후 결과 반환값 확인 | [src/device/RequestManager.cpp:37](#source-da034a9a1147d012) |
    | 성공 시 결과 전송 (ret &gt;= 0) | [src/device/RequestManager.cpp:37](#source-da034a9a1147d012) |
    | 성공 또는 실패 후 완료 호출 | [src/device/RequestManager.cpp:37](#source-da034a9a1147d012) |
    | ret &gt;= 0 · ret &gt;= 0 [true] | [src/device/RequestManager.cpp:37](#source-da034a9a1147d012) |
    | 항상 호출됨 (성공/실패 모두) | [src/device/RequestManager.cpp:37](#source-da034a9a1147d012) |
<!-- /sdd:visual:completion-branches -->

`src/device/RequestManager.cpp:37`

근거 원문: [src/device/RequestManager.cpp:37](#source-da034a9a1147d012)

## 소스 근거

같은 발췌는 한 번만 싣습니다. 필요한 원문을 펼쳐 설명과 대조하세요.

<a id="source-da034a9a1147d012"></a>

??? note "소스 근거: src/device/RequestManager.cpp:37"
    `src/device/RequestManager.cpp:37`에서 시작하는 발췌입니다. 종료 줄은 47이며, 아래 원문을 설명과 대조할 수 있습니다.
    
    SHA-256: `64ce50dbc9085701f44bbba8bc5573bc9ed24bb9eedbc15e7676446eb4f629fe`
    
    ```text
    void RequestManager::onFrame(Frame &frame) {
        FrameFactory &factory = frame.isPreview ? static_cast<FrameFactory &>(previewFactory_)
                                                : static_cast<FrameFactory &>(captureFactory_);
        int ret = factory.runPipes(frame);
        if (ret >= 0) {
            sendResult(frame);
        }
        onFrameDone(frame);
    }
    
    void RequestManager::sendResult
    ```

??? note "근거와 검토 정보"
    - 생성 방식: 질문과 소스 원문 보기
    - 검증 범위: 동작 설명을 생성하지 않습니다. 질문과 소스 위치를 표시하며 그림 초안의 작성자와 검사 범위는 그림 아래에 따로 기록합니다.
    - 근거 파일: `src/device/RequestManager.cpp`
    - 근거 수준: 코드 확인 (정적 분석, public-excerpt-fixture 구성, commit `f058f7908e`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-25 · 사람 검토 전

다음 단계: [완료 분기](completion.md)
