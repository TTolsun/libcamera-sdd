# 요청·버퍼 경로의 진단·변경 근거를 확인하세요

이 기록은 [생성기 이슈 #252](https://github.com/TTolsun/camera-hal-sdd-generator/issues/252)의 **선택된 공통/UVC 경로**를 다룹니다. 요청 제출부터 준비·장치 제출·버퍼와 요청 완료·취소·정지까지 조건, 관찰값, 다음 분기와 변경 후 검증 조건을 연결했습니다. 기존 자원 소유권·FIFO 설명과 최신 #253의 관찰 계획·다른 원고·독자 경로를 보존했습니다. 분량·그림 수·호출 수를 개선 점수로 사용하지 않습니다.

## 기준과 한계를 확인하세요

생성 전에 고정한 Q1–Q7과 [범위](scope.json), [전체 소스 창 색인](source-window-index.json)을 확인할 수 있습니다. 최종 소스는 `be7e83e91348250c015aad6d6f59f1468555bae8`이며 선택한 전체 파일은 27개입니다. 293 기준의 초기 시도와 be7로 기준을 바꾼 시점·이유·실패 기록을 보존합니다. 과거 실행을 새 커밋의 실행으로 바꾸지 않았습니다.

[새 be7 UVC 빌드](build-provenance-current.json)와 [실제 libclang 추출](current-uvc-extraction.json)은 135 TU·파싱 오류 0개입니다. 전체 사이트는 기존 공개 facts를 사용합니다. `controls.cpp`에는 분석용 `-Wno-error=c99-designator`를 적용했습니다. 공식 upstream과 미러는 이후 `c19d05128`에 도달했습니다. 그 사이 선택한 27개 파일은 바이트가 동일하며, 사이트의 소스 링크와 facts는 실제 빌드한 be7에 고정했습니다. [upstream 비교](upstream-2026-11-12.json)

[별도 신호 프로브](signal-probe.json)는 **293의 별도 새 빌드**에서 얻은 제한된 관찰입니다. Auto/Queued 수신 본문 표식이 두 번째 동기 슬롯에 의해 아직 emit이 진행 중인 동안 관측될 수 있음을 확인했습니다. 정확한 C++ 반환 명령·실제 카메라/DMA·포인터 오류·사내 HAL을 검증한 결과가 아닙니다.

## 같은 질문의 조건 누락을 비교하세요

비교 전 원고는 공개 #253 반영본입니다. 이후 공개 PR #98이 인접 세 페이지를 갱신했으며, 선택 원고는 같은 바이트를 유지했습니다. 표의 미충족은 질문에 필요한 조건이 빠졌다는 판정입니다. 기존의 충분한 소유권·FIFO 설명을 보존했습니다. [공개 기준 근거](current-public-baseline-proof.json)

| 질문 | 판단 범위 | 보완 전 공개 기준 원고 | 보완 원고 |
| --- | --- | --- | --- |
| Q1 | 제출·준비·대기와 재진입 | 필수 조건 누락 | 충족 |
| Q2 | 제어 처리·QBUF 전후 실패와 정리 | 필수 조건 누락 | 충족 |
| Q3 | 요청 완료와 프레임·metadata 유효성 | 필수 조건 누락 | 충족 |
| Q4 | 소유권·재사용과 지연 수신자 수명 | 필수 조건 누락 | 충족 |
| Q5 | 정지·잔존 알림·오류와 연결 해제 | 필수 조건 누락 | 충족 |
| Q6 | 전달 스레드·직접/지연 호출·재귀 dispatch | 필수 조건 누락 | 충족 |
| Q7 | 관찰 위치·논리적 제출 회차·변경 검증 | 필수 조건 누락 | 충족 |

[질문별 원래 답변·근거·진단값·다음 분기·변경 검증 조건](answerability-comparison.json)을 그대로 공개합니다. 실제 사람 참가자는 0명이며 #163·#253의 사람 평가, #215 전체 시각화, 사내 HAL 검증은 완료하지 않았습니다.

## 독립 검토의 원본을 구분하세요

생성·번역과 독립 검토는 실제 Codex CLI / `gpt-6.1-terra` / `-c model_reasoning_effort="high"`로 실행했습니다. [정확성](independent-accuracy.json), [근거 충분성](independent-sufficiency.json), [한영 의미 대조](independent-bilingual.json)는 별도 호출입니다. 인용 발췌만이 아니라 고정된 전체 소스 창을 제공했고 Q1–Q7의 필수 필드와 모든 H2/H3의 질문별 그림 또는 생략 사유를 확인했습니다. 자동 판정은 사람 승인이 아니며 기존 사람 상태를 바꾸지 않습니다.

통과 전의 반례·부족한 발췌·중복·잘못된 그림·번역·파일 접근·검증 도구 실패와 수정 이유도 archive에 남깁니다. [실제 CLI 원본 검증](native-call-verification.json)은 거절된 답변과 재시도를 포함한 완료 호출을 집계하며, 이를 성공 문서 수로 표시하지 않습니다. 과거 영수증은 공개 원본의 고정 해시와 별도 목록으로 결합해 새 호출에서 제외했습니다. 체크포인트 재사용은 새 추론이 아닙니다.

표준 계약 감사에서 준비 완료 호출 주체, 늦게 도착한 완료의 상태 검사, 캡처 플레인 검사, 정지 중 캐시 검사 전에 반환하는 경계를 보완했습니다. QBUF 전에 플레인이 모자란 경우와 초과한 경우도 구분했습니다. 지정 CLI로 답변 단위 다섯 개를 갱신했고, 그 밖의 답변과 생성 그림을 보존했습니다. [초기 네 답변의 근거](standard-contract-repair-final.json) · [QBUF 플레인 수 경계](final-planes-unit-repair.json)

## 화면과 발행 입력을 확인하세요

[브라우저 기록](browser-verification.json)은 한영·desktop 1440px/mobile 390px의 네 독립 Chrome 컨텍스트에서 선택 그림의 렌더링·원본 MMD·확대·노드 검색·Escape·포커스 복귀·근거 앵커·문서 검색을 확인했습니다. 실제 휴대전화·사람 읽기 부담 측정은 아닙니다. [실제 한영 HTML 결합](bilingual-peer.json)은 C++ 발췌의 동일성과 검토된 HTML 해시를 보존합니다.

한영 대조 입력에서는 양쪽 발췌의 동일성을 확인한 뒤 영문 발췌 본문의 중복을 줄였습니다. 실제 Chrome에서는 두 언어의 소스 발췌와 앵커가 모두 있었으며, 네 이전 주소 안내는 기본 화면에서 숨겨져 있었습니다. 독립 CLI가 실제 서두와 브라우저 결과를 대조해 원래 지적 두 건을 확인했습니다. [브라우저 원본 대조](bilingual-projection-browser-proof.json)

최초 로컬 export/verify와 반복 빌드는 같은 manifest를 생성했습니다. 공개 main이 새 upstream을 반영하고 역할별 시작 페이지를 제거한 뒤에는 기존 사이트를 보존하도록 `/issue252/`에서 별도 export/verify를 수행했습니다. 검토한 한영 원고를 유지했고 역할별 시작 페이지를 생성하지 않았습니다. [공개 한국어 문서](https://ttolsun.github.io/libcamera-sdd/issue252/request-lifecycle.html) · [공개 영어 문서](https://ttolsun.github.io/libcamera-sdd/issue252/en/request-lifecycle.html) · [공개 범위](scoped-pages-release-plan.json) · [발행 manifest](site-manifest.json)

표준 계약 감사에서 확정 모순은 없었습니다. 자동 미판정 두 건은 실행 전 시험의 계측과 경로 확인 한계로 남겨 두었습니다. 선택한 필수 질문 일곱 개의 정적 근거 검토와 시험의 실제 수행 상태는 별도로 기록합니다. [자동 미판정 원본과 실행 한계](standard-unresolved-disposition.json)

생성기 [PR #266](https://github.com/TTolsun/camera-hal-sdd-generator/pull/266)의 병합 기준은 `ae49f537fa271ebec718d8b03b7faaa26045b70c`입니다. 공개 빌드 ID는 `513092ba14c8fa698ec65188376caf9f72d74d757e1506db7f545d495f643970`입니다. [공개 manifest](https://ttolsun.github.io/libcamera-sdd/issue252/site-manifest.json) · [Pages 실행](https://github.com/TTolsun/libcamera-sdd/actions?query=workflow%3Apages-build-deployment)

## 실제 입력과 재현 경계를 확인하세요

[패키지 범위](package.json), [파일별 SHA-256](native-index.json), [원본 아카이브](native-evidence.tar.xz)는 실행한 설정·원고·facts·전체 소스 창·원래 요청과 응답·CLI 표준 출력과 영수증·실패·빌드·추출·브라우저·검증 로그를 보존합니다. 최종 경로의 설정과 실행 로그는 [별도 아카이브](scoped-release-evidence.tar.xz)와 [파일별 해시](scoped-release-index.json)에 있습니다. 소스는 고정된 공개 libcamera Git에서 확보합니다. 아카이브의 절대 경로는 실행 당시 값이며, 다른 환경으로 옮길 때는 프로필과 원본 자원의 연결을 조정해야 합니다. 고정된 과거 영수증 목록은 원래 바이트 그대로 복원합니다.

저장된 응답·직접 모델 API·다른 CLI·수동 원고를 새 CLI 생성이나 재현 성공으로 대체하지 않습니다. 실제 실행 모델·인자는 profiles와 원래 영수증에 남아 있으며 앱/CLI 전역 기본값은 바꾸지 않았습니다. 기존 다른 모델 기록은 당시 설정 그대로 보존했습니다. 공개 정기 예약과 사내 데이터 배포는 없습니다.
