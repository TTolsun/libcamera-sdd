# 이슈 #242 착수 조사

사용자가 구현 방향을 선택하기 전의 독립 조사 기록입니다. 새 공유 발행 계약과 무효화 정책은 구현하지 않았습니다.

- 원격 main과 작업 HEAD: `83c83158dfd1ff876a4c52ae3db8e56fdc1aaae5`. GitHub 연결 도구로 확인했습니다. 셸의 원격 조회는 DNS 실패였으며 동기화 성공으로 표시하지 않습니다. 추적 파일 변경은 없습니다.
- #241·#242는 열려 있고 댓글은 없으며, 조회 당시 열린 생성기 PR도 없습니다. #241의 새 기준·변경 이력 계약은 아직 확정으로 간주하지 않습니다. 원본 조회 결과는 이 디렉터리의 JSON으로 보존합니다.
- AGENTS.md, DESIGN.md, docs/concepts/site.md, style/README.md와 두 집필 원문, reader-quality.md, reuse-boundaries.md, contract-consistency.md, #214 기록과 현행 구현을 확인했습니다.
- CPython 3.14.7 / pytest 9.1.1에서 `test_issue214_matrix.py`와 `test_publication_plan.py`: **11 passed in 7.74s**. 7.74초는 pytest 실행 시간이며 환경 구성·조사 시간이나 실제 CLI 시간은 아닙니다. `baseline-ready.xml`과 `observed-matrix.json`에 결과를 보존합니다.
- 앞선 실행은 테스트 환경 준비에 실패했습니다. 기본 Python에는 pytest가 없었고, 기존 기본 체크아웃 venv에는 jsonschema가 없었습니다. 실패 JUnit `baseline.xml`도 보존합니다. uv로 이 작업 트리 전용 .venv를 구성한 뒤 정상 시험을 실행했습니다.
- 모든 행렬 호출은 통제된 CLI 대역입니다. 실제 Codex CLI 생성·번역·독립 검토는 아직 실행하지 않았습니다. 공개 기본 프로필은 Codex / gpt-6.1-terra / high이며 기존 한도·전역 설정은 바꾸지 않았습니다.

| 변경 | 신규 생성 | 신규 근거 검토 | 두 번째 생성 실행의 초 |
|---|---:|---:|---:|
| 동일 | 0 | 0 | 0.2353 |
| 질문 하나 | 1 | 1 | 0.2769 |
| 근거 하나 | 1 | 1 | 0.2925 |
| summary 추가 | 1 | 1 | 0.4560 |
| 화면 설정 | 0 | 0 | 0.2465 |
| 결정적 검증 정책 | 0 | 0 | 0.3225 |
| 근거 대조 정책 | 0 | 2 | 0.4127 |
| 전역 집필 규칙 | 2 | 2 | 0.3316 |

수치는 기존 두 질문 fixture의 실행 결과입니다. 공개 libcamera 전체 발행 성능·품질이나 실제 CLI 호출 시간을 뜻하지 않습니다. 현재 확인 범위에서 과잉 신규 호출은 입증되지 않았습니다.

## 재현한 설명 공백

1. 질문·근거·집필 규칙 변경 모두 `no exact completed checkpoint or reusable manuscript`라는 같은 사유를 출력합니다. 변경된 입력과 의존성을 구분해 설명하지 않습니다.
2. 질문·근거 행에서 사전 계획은 prepare 단위를 `revalidate-checkpoint`로 표시하지만 실행 집계는 reused=1, revalidated=0입니다. summary 추가 행에서는 계획이 두 기존 단위를 `reuse-checkpoint`로 표시하지만 실행은 revalidated=2입니다. 이 차이를 신규 호출 수 오류와 혼동하지 않습니다. 신규 답변에 의존하는 후속 검사는 사전 확정 여부와 실제 실행 판정을 구분해야 합니다.
3. 번역·consistency의 묶음 정책 해시는 조사 후보입니다. 파일 이름이 화면 관련이라는 이유나 해시 범위가 넓다는 사실만으로 과잉 무효화라고 확정하지 않습니다.

기존 공개 원고·출력·실제 CLI 영수증과 사람 검토 상태는 변경하지 않았습니다. 테스트 fixture가 만든 원본 request/response/receipt·실행 기록·계획은 `baseline-20261105-03` 아래에 유지합니다. 번역·그림·CLI 프로필·미등록 의존성·손상 영수증·혼합 소스 등 #242 전체 비교와 실제 CLI 시험은 남아 있습니다.

이 착수 기록은 표로 비교할 수 있는 계측·판정 증거이므로 별도 그림을 생략합니다. 전체 완료·병합·배포를 주장하지 않습니다.
