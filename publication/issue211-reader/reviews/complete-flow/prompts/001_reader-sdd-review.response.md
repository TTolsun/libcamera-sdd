{
  "verdict": "needs-revision",
  "findings": [
    "완료 흐름 그림의 증가 후 분기 «미도달: 재큐 확인 [false]»와 영어 «Not reached: check requeue [false]»는 captureLimit_이 설정되지 않은 경우도 포함하도록 수정하세요. 소스의 조건은 한도가 설정되고 카운트가 한도 이상일 때만 참입니다.",
    "재현 흐름 그림의 «커널·udmabuf·Virtual2 400x300 NV12 모두 일치 결정»과 영어 «All match: kernel, udmabuf, Virtual2 400x300 NV12»에서 udmabuf가 무엇을 통과해야 하는지 불명확합니다. root의 /dev/udmabuf 접근 확인을 조건으로 명시하세요."
  ],
  "reader_tasks": [],
  "reviewed_scope": "제공된 한국어 본문과 연결된 재현 절차를 함께 검토하고, 고정 소스와 측정 기록에 대한 사실 부합성 및 두 Mermaid 원문과 영어 번역 라벨을 검토했습니다. 할당기 결론의 그림 생략 사유도 검토했습니다.",
  "unreviewed": [
    "영어 본문은 제공되지 않아 한국어 본문과 비교하지 못했습니다.",
    "실제 렌더링된 그림의 시각적 가독성과 외부 링크의 현재 내용은 확인하지 못했습니다."
  ]
}
