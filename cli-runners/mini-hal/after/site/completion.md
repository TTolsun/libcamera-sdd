---
generated_at: 2026-10-26T13:25:31+00:00
source_commit: 83cca0fa441c40002f06087725ecbefb8580428c
status: ok
section: completion-demo
generation_method: facts-and-llm
evidence_fingerprint: 5ff0c6340bb5542a432a441a35a663253434f54bd0f60d7f4db160c1d7cf8385
semantic_review: human-review-required
agent: cli/hermes/qwen3.5:9b
generated_design: {"schema": 1, "input_fingerprint": "5ff0c6340bb5542a432a441a35a663253434f54bd0f60d7f4db160c1d7cf8385", "answers": {"completion": [{"text": "RequestManager::onFrame에서 factory.runPipes(frame)가 0 이상을 반환하면 sendResult(frame)를 호출하고, onFrameDone(frame)는 if 블록 밖에서 무조건 호출됩니다.", "covers": ["completion-rule"], "kind": "behavior", "quote": "void RequestManager::onFrame(Frame &frame) {\n    FrameFactory &factory = frame.isPreview ? static_cast<FrameFactory &>(previewFactory_)\n                                            : static_cast<FrameFactory &>(captureFactory_);\n    int ret = factory.runPipes(frame);\n    if (ret >= 0) {\n        sendResult(frame);\n    }\n    onFrameDone(frame);\n}\n\nvoid RequestManager::sendResult", "evidence": ["on-frame"], "part_id": "completion-rule"}]}, "topic_inputs": {"completion": "e925aaeca29596f9bb574bf8839d49b7ab41b673c5e1dc55d904ebed0ff5e7d7"}, "reused_topics": [], "generated_topics": ["completion"], "topic_agents": {"completion": "cli/hermes/qwen3.5:9b"}, "body_sha256": "b8cfbc1c3a9e6723667743141291e6f3c3e4fa55dcde04c384208f53edbca1c3"}
generated_visuals: {"schema": 1, "records": {"completion-branches": {"input_fingerprint": "8bd1a8547df1e686aabda9e30f2571022e466844c01b861ddd191bf36ed72a42", "draft": {"nodes": {"n0": {"label": "runPipes 실행", "label_en": "execute runPipes", "shape": "process", "quote_ids": ["on-frame:0"]}, "n1": {"label": "sendResult 호출", "label_en": "call sendResult", "shape": "process", "quote_ids": ["on-frame:0", "on-frame:1"]}, "n2": {"label": "onFrameDone 호출", "label_en": "call onFrameDone", "shape": "process", "quote_ids": ["on-frame:0"]}}, "edges": [{"from": "n0", "to": "n1", "label": "성공 시 결과 전송", "label_en": "send result on success", "condition_ref": "c0:true", "quote_ids": ["on-frame:0"]}, {"from": "n0", "to": "n2", "label": "반드시 최종 완료 호출", "label_en": "always call done", "condition_ref": "always", "quote_ids": ["on-frame:0"]}]}, "graph": {"id": "completion-branches", "topic": "completion", "kind": "decision", "title": "파이프 결과와 완료 처리의 분기", "question": "RequestManager::onFrame에서 runPipes, sendResult, onFrameDone의 연결을 그리세요. 결과 전송 조건의 condition_ref를 원문 조건 ID의 참·거짓으로 선택하고 성공·실패 경로를 구분하세요. onFrameDone이 성공·실패 양쪽에서 호출되는 것을 보존하세요. 기기 동작이나 스레드 보장은 추정하지 마세요. 세 호출을 각각 한 노드로 표현하며 진입점·변수·성공실패별 가상 상태 노드는 추가하지 마세요. label과 label_en에는 함수의 역할만 적으세요. 비교식·숫자·성공실패 판정은 레이블에 쓰지 말고 분기는 현재 원문 조건의 condition_ref로만 지정하세요.", "nodes": [{"id": "n0", "label": "runPipes 실행", "label_en": "execute runPipes", "shape": "box", "evidence": [{"source": "completion/on-frame", "sha256": "64ce50dbc9085701f44bbba8bc5573bc9ed24bb9eedbc15e7676446eb4f629fe", "quote": "void RequestManager::onFrame(Frame &frame) {\n    FrameFactory &factory = frame.isPreview ? static_cast<FrameFactory &>(previewFactory_)\n                                            : static_cast<FrameFactory &>(captureFactory_);\n    int ret = factory.runPipes(frame);\n    if (ret >= 0) {\n        sendResult(frame);\n    }\n    onFrameDone(frame);\n}"}]}, {"id": "n1", "label": "sendResult 호출", "label_en": "call sendResult", "shape": "box", "evidence": [{"source": "completion/on-frame", "sha256": "64ce50dbc9085701f44bbba8bc5573bc9ed24bb9eedbc15e7676446eb4f629fe", "quote": "void RequestManager::onFrame(Frame &frame) {\n    FrameFactory &factory = frame.isPreview ? static_cast<FrameFactory &>(previewFactory_)\n                                            : static_cast<FrameFactory &>(captureFactory_);\n    int ret = factory.runPipes(frame);\n    if (ret >= 0) {\n        sendResult(frame);\n    }\n    onFrameDone(frame);\n}"}, {"source": "completion/on-frame", "sha256": "64ce50dbc9085701f44bbba8bc5573bc9ed24bb9eedbc15e7676446eb4f629fe", "quote": "void RequestManager::sendResult"}]}, {"id": "n2", "label": "onFrameDone 호출", "label_en": "call onFrameDone", "shape": "box", "evidence": [{"source": "completion/on-frame", "sha256": "64ce50dbc9085701f44bbba8bc5573bc9ed24bb9eedbc15e7676446eb4f629fe", "quote": "void RequestManager::onFrame(Frame &frame) {\n    FrameFactory &factory = frame.isPreview ? static_cast<FrameFactory &>(previewFactory_)\n                                            : static_cast<FrameFactory &>(captureFactory_);\n    int ret = factory.runPipes(frame);\n    if (ret >= 0) {\n        sendResult(frame);\n    }\n    onFrameDone(frame);\n}"}]}], "edges": [{"from": "n0", "to": "n1", "label": "성공 시 결과 전송 · ret >= 0 [true]", "label_en": "send result on success · ret >= 0 [true]", "evidence": [{"source": "completion/on-frame", "sha256": "64ce50dbc9085701f44bbba8bc5573bc9ed24bb9eedbc15e7676446eb4f629fe", "quote": "void RequestManager::onFrame(Frame &frame) {\n    FrameFactory &factory = frame.isPreview ? static_cast<FrameFactory &>(previewFactory_)\n                                            : static_cast<FrameFactory &>(captureFactory_);\n    int ret = factory.runPipes(frame);\n    if (ret >= 0) {\n        sendResult(frame);\n    }\n    onFrameDone(frame);\n}"}]}, {"from": "n0", "to": "n2", "label": "반드시 최종 완료 호출", "label_en": "always call done", "evidence": [{"source": "completion/on-frame", "sha256": "64ce50dbc9085701f44bbba8bc5573bc9ed24bb9eedbc15e7676446eb4f629fe", "quote": "void RequestManager::onFrame(Frame &frame) {\n    FrameFactory &factory = frame.isPreview ? static_cast<FrameFactory &>(previewFactory_)\n                                            : static_cast<FrameFactory &>(captureFactory_);\n    int ret = factory.runPipes(frame);\n    if (ret >= 0) {\n        sendResult(frame);\n    }\n    onFrameDone(frame);\n}"}]}], "producer": "cli/hermes/qwen3.5:9b"}, "producer": "cli/hermes/qwen3.5:9b", "generation_commit": "83cca0fa441c40002f06087725ecbefb8580428c", "reused": false}}, "body_sha256": "b8cfbc1c3a9e6723667743141291e6f3c3e4fa55dcde04c384208f53edbca1c3"}
---

# 공개 mini HAL의 완료 분기

**파이프 반환 조건과 완료 정리를 소스와 함께 확인하세요.**



## 결과 전송과 프레임 정리

RequestManager::onFrame에서 factory.runPipes(frame)가 0 이상을 반환하면 sendResult(frame)를 호출하고, onFrameDone(frame)는 if 블록 밖에서 무조건 호출됩니다. `src/device/RequestManager.cpp:37`

<!-- sdd:visual:completion-branches -->
### 파이프 결과와 완료 처리의 분기

RequestManager::onFrame에서 runPipes, sendResult, onFrameDone의 연결을 그리세요. 결과 전송 조건의 condition_ref를 원문 조건 ID의 참·거짓으로 선택하고 성공·실패 경로를 구분하세요. onFrameDone이 성공·실패 양쪽에서 호출되는 것을 보존하세요. 기기 동작이나 스레드 보장은 추정하지 마세요. 세 호출을 각각 한 노드로 표현하며 진입점·변수·성공실패별 가상 상태 노드는 추가하지 마세요. label과 label_en에는 함수의 역할만 적으세요. 비교식·숫자·성공실패 판정은 레이블에 쓰지 말고 분기는 현재 원문 조건의 condition_ref로만 지정하세요.

LLM 그림 초안 · 사람 검토 전

작성 모델: `cli/hermes/qwen3.5:9b`

```mermaid
flowchart TB
%% sdd:translations {"onFrameDone 호출": "call onFrameDone", "runPipes 실행": "execute runPipes", "sendResult 호출": "call sendResult", "반드시 최종 완료 호출": "always call done", "성공 시 결과 전송 · ret &gt;= <br/>0 [true]": "send result on success · <br/>ret &gt;= 0 [true]"}
  v_n0["runPipes 실행"]
  v_n1["sendResult 호출"]
  v_n2["onFrameDone 호출"]
  v_n0 -->|"성공 시 결과 전송 · ret &gt;= <br/>0 [true]"| v_n1
  v_n0 -->|"반드시 최종 완료 호출"| v_n2
```

[Mermaid 원문](completion.completion-branches.mmd)

??? note "그림 근거와 확인 범위"
    소스에 연결한 설계 해석입니다. 자동 연결 검사는 의미 승인이나 기기 실행 검증이 아닙니다.
    
    | 요소·전이 | 소스 근거 |
    |---|---|
    | runPipes 실행 | [src/device/RequestManager.cpp:37](#source-da034a9a1147d012) |
    | sendResult 호출 | [src/device/RequestManager.cpp:37](#source-da034a9a1147d012) |
    | onFrameDone 호출 | [src/device/RequestManager.cpp:37](#source-da034a9a1147d012) |
    | 성공 시 결과 전송 · ret &gt;= 0 [true] | [src/device/RequestManager.cpp:37](#source-da034a9a1147d012) |
    | 반드시 최종 완료 호출 | [src/device/RequestManager.cpp:37](#source-da034a9a1147d012) |
<!-- /sdd:visual:completion-branches -->

근거 원문: [src/device/RequestManager.cpp:37](#source-da034a9a1147d012)

??? note "설계 질문과 검증 범위"
    질문별 답변과 근거 연결을 검사했습니다. 의미와 실행 결과는 사람 검토가 필요합니다.
    
    | 설계 질문 | 설명 위치 | 확인 범위 |
    |---|---|---|
    | RequestManager::onFrame에서 runPipes 반환값에 따른 sendResult 조건과 onFrameDone 호출을 설명하세요. if 블록 안팎을 구분하고 실패 시 정리도 설명하세요. 실행 스레드나 성공 보장을 추정하지 마세요. | [결과 전송과 프레임 정리](#결과-전송과-프레임-정리) | 코드 근거와 설명 연결 |

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
    - 생성 방식: 추출 사실과 LLM 설명
    - 검증 범위: 표·그림은 facts로 만들고 설명은 LLM이 작성합니다. 인용·문장 및 설정된 구조 검사를 적용합니다.
    - 근거 파일: `src/device/RequestManager.cpp`
    - 근거 수준: 코드 확인 (정적 분석, public-excerpt-fixture 구성, commit `83cca0fa44`)
    - 자동 검사 (인용·문장 및 설정된 구조 검사): 통과
    - 검토 상태 기록일: 2026-10-26 · 사람 검토 전

다음 단계: [완료 분기](completion.md)
