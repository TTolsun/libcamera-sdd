## require_guard_branches

**결론:** LLM 시각 계획의 선택적 boolean 플래그입니다. 켜면 조건(guard) 간선이 결정 노드에서 나오는지, 그 노드가 쓰는 원본 조건마다 `true`와 `false` 결과가 모두 있는지 로컬에서 검사합니다.

### 1. 설정 위치와 기본값
- `generation: llm`인 시각 계획 항목에 둡니다.
- 생략하면 `false`로 동작합니다.
- boolean이 아닌 값은 설정 검증에서 거부합니다.

```yaml
- id: capture-guards
  topic: capture
  kind: decision
  title: 캡처 분기
  question: 캡처 요청은 어떤 조건에서 처리되는가?
  generation: llm
  require_guard_branches: true
```

### 2. 검사 규칙
1. `always`가 아닌 `condition_ref` 간선은 `decision` 모양 노드에서 출발해야 합니다.
2. 그 노드가 사용하는 원본 조건마다 `true`와 `false` 결과가 모두 있어야 합니다.
3. 기존 원본 바인딩 검사(끝점 심볼과 조건 ID의 인용 근거 포함 여부)는 그대로 적용됩니다.
4. 프롬프트의 추가 지시는 모델에게 주는 안내일 뿐이며, 실제 강제는 생성 후 로컬 검사가 맡습니다.

### 3. 한계
- 구조 검사는 원본의 모든 분기를 그리도록 요구하지 않습니다.
- 의미상 완전성을 증명하지 않으며, 사람 승인을 뜻하지 않습니다.