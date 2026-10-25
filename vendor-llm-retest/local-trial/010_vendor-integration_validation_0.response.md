{
  "statements": [
    {
      "text": "`PipelineHandler::completeRequest` 함수가 반환되면 해당 요청은 더 이상 파이프라인 핸들러에 의해 관리되지 않습니다.",
      "quote_id": "completion:0",
      "covers": ["validation"],
      "kind": "behavior"
    },
    {
      "text": "이 함수가 반환된 이후에는 해당 요청을 접근하거나 사용하지 않아야 합니다.",
      "quote_id": "completion:0",
      "covers": ["validation"],
      "kind": "behavior"
    },
    {
      "text": "`PipelineHandler::completeRequest` 는 애플리케이션이 제출한 요청의 원래 순서대로 반환되도록 보장합니다.",
      "quote_id": "completion:0",
      "covers": ["validation"],
      "kind": "behavior"
    },
    {
      "text": "파이프라인 핸들러는 완료된 요청에 대해 이 함수를 호출할 때 어떤 순서 제약도 따르지 않아도 됩니다.",
      "quote_id": "completion:0",
      "covers": ["validation"],
      "kind": "behavior"
    },
    {
      "text": "`PipelineHandler::completeRequest` 는 반드시 카메라 매니저 스레드에서 호출되어야 합니다.",
      "quote_id": "completion:0",
      "covers": ["validation"],
      "kind": "behavior"
    }
  ]
}
