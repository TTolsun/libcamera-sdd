# #242 후속: 이전 미판정의 근거와 표본 약어를 확인하세요

최신 공개 본문을 조사한 결과 영어 의미 오류는 #248의 실제 재번역에서 이미 수정됐습니다. 해당 영어 값은 그대로 유지합니다. 큐의 오류 우선순위도 올바른 주장입니다. 전체 자동 대조 보고서에는 빠졌던 `include/libcamera/internal/camera.h:59–60`의 `allowDisconnected = false` 선언을 정확한 Git 원문으로 제공해 새 독립 CLI 검토에서 확인했습니다. 이전 `insufficient-evidence` 응답과 최신 전체 보고서를 수정하지 않았습니다.

[새 공개 표본](https://ttolsun.github.io/libcamera-sdd/validation/issue242-followup/probe.html)에는 API와 LLM의 뜻을 추가했습니다. [용어집](https://ttolsun.github.io/libcamera-sdd/validation/issue242-followup/glossary.html)은 두 용어의 확장과 설명을 실제로 표시합니다. 생성기 실행 정책·의미 검토·본문은 바꾸지 않았고 `common: []`, `site.undefined_terms: fail`을 유지했습니다. 사람 검토는 계속 pending이며 표본의 semantic_review는 human-review-required입니다.

| 항목 | 조사·처리 |
|---|---|
| 스트림과 매개변수를 잘못 연결한 영어 | 이미 수정된 현재 번역을 유지하고 실제 CLI로 대조했습니다. |
| 큐 오류 우선순위의 선언 근거 누락 | 헤더의 기본 인자와 구현·호출부를 함께 제공해 본문을 유지할 근거를 확인했습니다. |
| API 경고 | Application Programming Interface의 뜻을 제공했습니다. |
| LLM 경고 | Large Language Model의 뜻과 자동 판정의 한계를 제공했습니다. |

## 실제 실행과 보존

별도 Codex CLI / gpt-6.1-terra / high를 두 번 실행했습니다. 첫 검토 16.3291초는 LLM 정의의 표본 사용 설명을 좁히라는 지적을 남겼습니다. 이 설명만 일반적인 정의로 바꾸고 최종 검토 14.0641초에서 두 주장·두 API 답변·두 용어 모두 지지를 확인했습니다. 별도 실제 CLI diff 검토 1회·6.5322초도 추가 결함이 없었습니다. 세 새 영수증의 CLI 무결성을 검증했습니다. 직접 API·다른 CLI·저장 응답을 새 성공으로 대체하지 않았습니다.

생성 경로 재개는 0.9370초·새 모델 호출 0회이며 기존 답변을 현재 검사로 재검증했습니다. 원래 본문·답변·사람 검토 상태는 같습니다. 시각·체크포인트 메타데이터 차이와 이전 원고 바이트는 따로 보존했습니다. 최종 정상 export 두 번은 합계 0.4878초, 같은 manifest·3페이지·끊어진 링크 0개·미정의 약어 0개·stderr 경고 0개입니다. 원본 네이티브 38개 파일의 바이트도 그대로입니다. 원래 전체 사이트의 344개 소유 산출물과 manifest는 수정하지 않고 별도 validation 경로를 추가합니다.

관련 기존 회귀 63개 통과·1개 생략은 용어집 동작과 CLI 프로토콜 대역·손상 거부 검사입니다. 위 실제 CLI 세 호출과 구분합니다. 전체 CI·생성기 PR #270 병합은 generator-merge.json에, 공개 병합·Pages·실제 URL 해시는 공개 PR과 원래 이슈의 배포 후 댓글에 연결합니다. 로컬 검사만으로 배포 완료를 주장하지 않습니다.

## 증거와 재현

- `original-evidence.zip`, `archive-index.json`, `package.json`: 이전 원고·정상 사이트·네이티브 원본, 실패·수정 지적·새 검토·실행 스크립트·표본 설정을 보존합니다. 원본 archive 180개 항목과 zip 자체의 해시를 기록했습니다.
- `plan-02.json`: 분석 소스 293, 현재 주장과 문자 그대로의 소스 창·해시·줄 및 검토 범위입니다. 최초 계획과 제품 소스가 아닌 분석 표현을 Git 파일로 읽으려다 중단한 준비 실패도 zip에 남아 있습니다. 준비 실패는 모델 호출 전이며 새 성공 호출로 세지 않습니다.
- `native-verification-final.json`, `independent-review-01.json`, `independent-review.json`, `diff-review.json`: 실제 세 CLI 호출과 첫 지적·최종 판정입니다.
- `probe-result-01.json`, `export-final.json`, `manuscript-preservation.json`: API/LLM 2→0, 현재 검사 재개·반복 빌드·본문/답변/검토 상태와 원본 영수증 보존입니다.
- `upstream.json`: 공식 upstream와 공개 mirror는 be7e83e로 일치합니다. 분석293 이후 바뀐 세 파일과 이번 세 API 소스 파일은 겹치지 않습니다. 최신 전체 추출·실기기·사내 HAL 검증이 아닙니다.

재현 시 zip의 probe/sdd.yaml과 independent-review.yaml을 복사하고 경로를 현재 환경에 맞게 연결합니다. 보관 facts·소스·원고·스타일·명령/모델/인자와 원본 영수증을 유지합니다. `paths.glossary_file`은 이 디렉터리의 glossary.yaml을 가리키고 `site.undefined_terms: fail`이어야 합니다. 새 CLI 검토에는 plan-02.json의 선언·구현·호출부와 현재 주장을 함께 전달하며 원본 결과를 고치지 않습니다. 생성기에서 표준 generate/export-site/verify-site 경로를 사용합니다. 표본의 원본 API 답변을 수동으로 쓰거나 최신 소스 전체 검증으로 승격하지 않습니다.

짧은 두 API 질문과 용어는 상태·반환 목록으로 충분하다는 독립 검토의 그림 생략 사유를 보존했습니다. 전체 문서의 그림·가독성·사람 평가 완료로 확대하지 않습니다. 다음으로 [기존 #242 증거](../issue242/README.md)에서 원래 변경 행렬과 배포 이력을 확인하세요.
