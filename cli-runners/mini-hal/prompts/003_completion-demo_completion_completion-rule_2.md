<!-- system -->
제공된 소스만 사용하여 한국어 기술 문서를 작성합니다. 질문의 각 조건에 답하세요. 원문에 없는 보장이나 이유를 추가하지 마세요. 의무(must/shall), 가능성(may), 부정을 그대로 유지하세요.

<!-- user -->
근거:
{"on-frame": [{"text": "void RequestManager::onFrame(Frame &frame) {\n    FrameFactory &factory = frame.isPreview ? static_cast<FrameFactory &>(previewFactory_)\n                                            : static_cast<FrameFactory &>(captureFactory_);\n    int ret = factory.runPipes(frame);\n    if (ret >= 0) {\n        sendResult(frame);\n    }\n    onFrameDone(frame);\n}\n\nvoid RequestManager::sendResult", "quote_id": "on-frame:0"}]}
질문: RequestManager::onFrame에서 runPipes 반환값에 따른 sendResult 조건과 onFrameDone 호출을 설명하세요. if 블록 안팎을 구분하고 실패 시 정리도 설명하세요. 실행 스레드나 성공 보장을 추정하지 마세요. 답변은 세 문장 이내로 작성하세요. runPipes와 sendResult의 현재 조건, 음수 반환 때의 호출 여부, if 블록 밖 onFrameDone의 무조건 호출을 각각 명시하세요. 전체 오류 처리가 미정이라고 추정하지 마세요.
작성 조건: completion: 답변 계약 검사: 필수 용어 누락: onFrameDone
질문의 모든 조건을 근거에서 다시 확인하세요.
출력: {"statements": [{"text": "질문의 모든 조건에 답하는 한 문단. 여러 문장을 써도 됩니다.", "quote_id": "직접 근거의 구절 ID", "covers": ["completion-rule"], "kind": "behavior"}]} 형식의 JSON만 반환하세요.
