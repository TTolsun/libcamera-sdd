{
  "statements": [
    {
      "text": "`createIPA()` 함수는 먼저 주어진 이름, 최소 버전, 최대 버전을 사용하여 `module()` 함수를 호출하여 IPA 모듈을 검색합니다.",
      "quote_id": "selection:0",
      "covers": ["algorithm"],
      "kind": "behavior"
    },
    {
      "text": "모듈 검색이 실패하면 즉각적으로 `nullptr`를 반환하며, 이 경우 이후의 모듈 로딩이나 프록시 생성 단계는 수행되지 않습니다.",
      "quote_id": "selection:0",
      "covers": ["algorithm"],
      "kind": "behavior"
    },
    {
      "text": "검색된 모듈이 유효한지 확인하기 위해 `isSignatureValid(m)` 함수를 호출하여 서명을 판정합니다.",
      "quote_id": "selection:1",
      "covers": ["algorithm"],
      "kind": "behavior"
    },
    {
      "text": "서명이 유효하면 `Threaded` 실행 방식으로, 그렇지 않으면 `Isolated` 실행 방식으로 모듈을 기반으로 프록시를 생성합니다.",
      "quote_id": "selection:1",
      "covers": ["algorithm"],
      "kind": "behavior"
    },
    {
      "text": "생성된 프록시가 유효하지 않은 경우 `LOG`를 통해 에러 로그를 출력하고 다시 `nullptr`를 반환하여 생성 실패를 알립니다.",
      "quote_id": "selection:2",
      "covers": ["algorithm"],
      "kind": "behavior"
    },
    {
      "text": "모든 검증과 생성 단계가 성공적으로 완료되면 최종적으로 생성된 프록시 객체를 반환합니다.",
      "quote_id": "selection:3",
      "covers": ["algorithm"],
      "kind": "behavior"
    }
  ]
}
