# 후보 회귀: 신입 관점 자동 독자 관측

동일 에이전트의 두 번째 노출이다. 이전 시험의 학습 효과가 있으며 독립 cold-reader 평가도 사람 평가도 아니다. 문맥이 유지되므로 '보지 않고 설명'과 탐색 재개를 사람의 기억·망각 실험으로 취급하지 않는다. 사람 부담·흥미·자연스러움·망각 점수는 측정하거나 만들지 않았다. 기본 과업 성공 점수나 합산 점수도 없다.

- 문서 조회 전 시각: 2026-11-04 20:11:11 UTC.
- 첫 도구 호출에서 candidate/site-manifest.json만 읽어 요청 build_id `f6b6072fea0fb8c8e05b82801afb1ffad29d00b1042534b37d15bee0dadd67c8`와 일치함을 확인한 뒤 HTML 조회를 시작했다.
- 사전 manifest SHA-256: `457889301da28033392cce7c44c97886b5bc150b661064bd2e7f9caeeb69a97b`.
- 내용 입력은 `build/issue248/candidate/`의 HTML과 그 안의 발췌뿐이다. 작성 이력·프로젝트 코드·정답표는 읽지 않았다. 아래 URL은 후보 HTML의 대응 공개 경로를 식별하는 참조이며 현재 공개 배포본이 후보와 같다는 뜻이 아니다. 실제 방문은 로컬 HTML 내용 조회다. 브라우저·화면·링크 클릭 성공은 평가하지 않았다.

## N1 — 시작과 다음 문서

- 실제 읽기 경로: candidate/index.html → `#어디서-시작할까요` → `#처음-읽는-개발자의-순서` → `#기준-설명-찾기` → candidate/overview.html.
- 실제 답: 신입이 먼저 열 문서는 For Developer 카드의 **시스템 개요**다. 구조를 익힌 뒤 요청을 따라가는 목적과 맞는다. 먼저 `#탐색과-파이프라인-선택`의 CameraManager 진입점을 보고, `#요청-제출과-완료`로 가서 요청 이동과 신호를 읽는다. 완료 지연 조사에는 **요청 처리와 문제 진단**으로 이어진다.
- 근거: [시작 카드](https://ttolsun.github.io/libcamera-sdd/index.html#어디서-시작할까요), [신입 읽기 순서](https://ttolsun.github.io/libcamera-sdd/index.html#처음-읽는-개발자의-순서).
- 시간: 문서 첫 조회 호출은 사전 식별 다음에 시작했고 20:11:33 UTC에 반환되었다. N1과 N2 본문을 한 호출에서 순서대로 읽었으므로 개별 N1 시간을 분리 측정하지 않았다. 식별 시작부터 이 반환까지 22초이며 10분 상한 이내다.
- 막힌 점: 내용상 시작 선택의 장애는 없었다. `기준 설명 찾기`의 '카메라와 요청 모델', 'Pipeline Handler'는 후보 HTML에서도 링크가 아닌 텍스트로 추출된다.
- 자동 편집 의견: 시작 카드와 신입 순서가 답의 이유를 제공한다. 기준 설명의 소유권·큐 계약 이름에 직접 상세 링크가 있으면 되돌아가 찾는 수고를 줄일 수 있다. 렌더링된 화면이나 첫 그림 가독성은 미평가다.

## N2 — 소유권과 재사용

- 실제 경로: candidate/overview.html의 `#요청-생성과-소유권` → 같은 페이지 `#source-d61960ed2545ba78` → `#source-0556d5e91908d040`.
- 실제 답: `Camera::createRequest()`의 반환 요청은 호출자가 소유하고 삭제할 책임도 진다. 완료 핸들러에서 삭제할 수 있다. 기존 요청을 다시 제출하기 전에는 `Request::reuse()`로 상태와 controls를 초기화한다. 발췌는 metadata 초기화와 RequestPending 복귀도 보여준다. 기존 버퍼를 그대로 쓰려면 `ReuseBuffers`를 지정한다. 지정하지 않으면 버퍼 맵이 비워지므로 재제출할 버퍼를 다시 연결해야 한다.
- 근거: [요청 생성과 소유권](https://ttolsun.github.io/libcamera-sdd/overview.html#요청-생성과-소유권), [생성 계약 발췌](https://ttolsun.github.io/libcamera-sdd/overview.html#source-d61960ed2545ba78), [reuse 발췌](https://ttolsun.github.io/libcamera-sdd/overview.html#source-0556d5e91908d040).
- 시간: N1과 공유한 본문 조회 후 두 발췌를 20:11:41 UTC까지 확인했다. 첫 사전 식별부터 최대 30초이며 개별 독해 시간은 분리 미측정이다. 10분 상한 이내다.
- 막힌 점: 계약 답은 찾았다. '요청 완료 전 어느 때라도 재사용 가능' 같은 확장 주장은 하지 않았다.
- 자동 편집 의견: 소유권·삭제 책임은 직접 적혀 있다. 반면 ReuseFlag, bufferMap_, pending_ 등의 구현 이름 앞에 '유지/다시 연결' 행동 요약을 두면 신입에게 더 명확하겠다. 이 절에 재사용 순서 그림 또는 상세의 직접 절 링크는 없다.

## S — 재조회 없이 쓴 설명

20:11:41 UTC 이후 문서를 새로 조회하지 않고 쓴다. 성공 반환은 제출이 받아들여졌다는 결과이며, 그 요청의 촬영 처리와 애플리케이션 반환이 끝났다는 뜻이 아니다. 종료는 별도의 requestCompleted 알림으로 확인해야 한다. 성공 반환만으로 장치의 후속 처리 성공도 확정할 수 없다. 버퍼 전체 완료와 요청 완료 사이에도 명시적인 요청 완료 호출이 필요하다. 그러므로 알림이 없다는 사례는 어느 후속 단계에서 멈췄는지 조사해야 하며 원인을 바로 단정할 수 없다.

이 설명은 두 번째 노출이며 과거 문맥의 도움을 받는다. 사람의 독립 회상 성공으로 세지 않는다. 다음에는 후보 상세 문서의 발췌로 근거를 다시 찾는다.

### S — 후보 근거를 다시 찾은 결과

- 실제 재조회 경로: candidate/request-lifecycle.html → `#제출에서-완료까지` → `#접수-반환과-완료-알림` → `#source-28d007de6ad1a8a5`.
- 실제 답 확인: API의 0 반환은 유효성 검사 뒤 `ConnectionTypeQueued`로 PipelineHandler 호출을 예약했다는 뜻이다. 요청 완료는 별도 `requestCompleted` 통지다. 재조회 전 설명의 '받아들여졌다'는 장치가 처리했다는 뜻으로 확대하지 않는다.
- 근거: [제출에서 완료까지](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#제출에서-완료까지), [접수와 알림 그림](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#접수-반환과-완료-알림), [예약과 반환 발췌](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#source-28d007de6ad1a8a5).
- 시간: 20:11:41–20:12:32 UTC, 51초(설명 저장·재조회 포함). 10분 상한 이내다.
- 막힌 점: 사례의 실제 원인은 이 구분만으로 알 수 없다.
- 자동 편집 의견: 접수 결과와 완료를 나눈 그림의 의미는 질문에 맞는다. overview의 '촬영 완료'라는 제목은 요청 취소 완료까지 포함하는 상태와 구분하는 링크가 있으면 좋겠다. 실제 그림 렌더링은 평가하지 않았다.

## R — 조회 중단 전 자유 메모

메모 기준 20:12:50 UTC. 사례가 제공한 관측은 '제출 성공, 완료 알림 없음'뿐이다. 실제 로그·fence·장치 상태·버퍼 상태는 미제공이다. 확인한 문서 단계는 입력 검사 → 비동기 핸들러 예약 → waitingRequests_ 등록과 prepare → 큐 한도/선두 prepared_ 검사 → doQueueRequest의 취소 또는 장치 제출 → 버퍼 완료 → 명시 completeRequest → 선두 Pending 검사와 제출 순서 반환이다.

원시 반환값과 요청 식별자/순번부터 보존하겠다. 아직 모르는 값은 prepared_, queuedRequests_ 크기와 한도, 각 fence의 신호, cancelled_, queueRequestDevice ret, 버퍼별 완료, completeRequest 진입, 선두 status()이다. 이 메모는 실행 관측 기록이 아니라 문서로 정한 조사 계획이다.

다음 분기는 선두가 미준비면 준비/fence를 조사하고, 소프트웨어 큐 크기가 한도와 같으면 앞 요청의 진행을 조사하는 것이다. 전달됐다면 취소 여부와 장치 ret을 기록한다. 장치 제출 뒤에는 버퍼별 완료를 기록하고, 모두 완료 뒤 명시 completeRequest 호출을 확인한다. 호출 뒤에도 알림이 없으면 제출 큐 선두 RequestPending이 뒤 요청 반환을 막는지 확인한다. 소프트웨어 큐 크기를 장치 처리 요청 수로 단정하지 않는다.

메모에 남긴 복귀 주소:

- [준비·전달 조건](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#선두-요청을-전달하거나-반복을-멈추는-조건), [전달 발췌](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#source-789eafedfaa7f3c5).
- [fence와 버퍼 유효 기간 발췌](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#source-95ae69eeb085e3b1).
- [제출 큐 선두와 반환 순서](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#제출-큐의-선두-상태와-반환-순서), [반환 발췌](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#source-236c920e906cb6fd).

이제 문서 조회를 중단하고 시계만 조회한 뒤 시작 index로 돌아간다. 자동 탐색 재개만 시험하며 실제 5분 망각을 재현하지 않는다. 대화 문맥과 두 번째 노출의 학습 효과가 유지된다.

### R — 시작점 복귀와 자기 메모로 재개

- 실제 경로: 메모 저장 → 20:13:23 UTC 시계만 조회 → candidate/index.html의 신입 순서 → 내 R 메모만 재독.
- 문서를 더 조회하기 전에 메모에서 복원한 답: 사례는 여전히 제출 성공/완료 미통지이고 원인은 미확정이다. 원시 ret과 요청 ID를 보존하고 선두 prepared_·큐 크기/한도를 먼저 확인한다. 이후 취소/장치 ret → 버퍼별 완료 → 명시 completeRequest → 앞 요청 Pending 순으로 진행한다.
- 메모에서 복원한 근거 주소: `request-lifecycle.html#source-789eafedfaa7f3c5`와 `#source-236c920e906cb6fd`다. 다음 도구 호출에서 이 주소로 돌아간다. 버퍼 유효 기간은 메모의 `#source-95ae69eeb085e3b1`에 남아 있다.
- 자동 재개 관측: 상태·미확인 값·다음 행동·주소가 자기 메모에 남아 있어 다시 찾을 수 있었다. 사람이 기억에서 복원했거나 5분 후 덜 잊었다는 관측은 아니다.

- 실제 재조회: 메모에서 복원한 두 앵커를 후보 HTML에서 다시 열어 준비·전달 검사와 선두 Pending의 break를 찾았다. R 확인 뒤 버퍼 완료 발췌와 해당 Mermaid 정의도 읽었다.
- 시간: 20:12:32–20:13:51 UTC, 79초(발췌 확인·메모·조회 중단·index 복귀·메모 재독·근거 재조회 포함). 10분 상한 이내다. 중단은 짧은 도구 호출 간 간격이며 5분 중단이 아니다.
- 막힌 점: 실제 로그가 없어 원인은 미확정이다. '확인한 문서 조건'과 '관측하지 않은 실행 값'을 분리해 남겼다.
- 자동 편집 의견: 선두 준비·큐 한도·순서 반환의 각 그림에는 직접 근거 앵커가 있어 메모로 복귀할 수 있다. waitingRequests_와 queuedRequests_의 차이를 한 표로 모으거나 각각의 관측 필드 이름을 제시하면 조사 계획을 더 빨리 적을 수 있겠다. 이는 편집 의견이며 사람의 부담 개선 실측이 아니다.

## X — 두 버퍼 중 한 버퍼만 완료

- 실제 경로: R 근거 재조회 → candidate/request-lifecycle.html `#버퍼-완료와-명시적-요청-완료의-경계` → `#source-ab8710f8a8a7905d` → `#source-5b0ae08604dff588` → 같은 절의 Mermaid 정의. R/X가 마지막 조회 호출을 공유하므로 전용 독해 시간을 분리하지 않았다.
- 실제 답: 같은 요청의 두 버퍼 중 실제로 하나만 완료됐다면 버퍼 하나의 완료와 추적 갱신만 확정할 수 있다. 아직 하나가 남으므로 모든 버퍼 완료 조건은 거짓이며 completeBuffer 계약상 false다. 요청 전체 완료나 안전한 요청 재사용을 단정할 수 없다. 단지 완료 알림 하나만 관측했다는 뜻이라면 둘째 버퍼 실제 미완료와 관측 누락을 먼저 구분해야 한다.
- 추가 조사: 두 버퍼가 같은 요청의 서로 다른 스트림에 속하는지와 둘째 버퍼의 상태·완료 통지를 추적한다. 버퍼를 요청 완료 콜백까지 유효하게 유지해야 한다. 두 버퍼가 모두 완료돼도 명시 completeRequest가 호출됐는지 확인하고, 그 뒤 알림이 없다면 선두 요청 Pending/제출 순서 반환을 조사한다. 한 버퍼 완료로 둘째 지연 원인이나 영상 성공을 추정하지 않는다.
- 근거: [버퍼/요청 완료 경계](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#버퍼-완료와-명시적-요청-완료의-경계), [completeBuffer 계약](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#source-ab8710f8a8a7905d), [명시 완료 의무](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#source-5b0ae08604dff588), [버퍼 유효 기간/스트림 계약](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#source-95ae69eeb085e3b1), [선두 Pending](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#source-236c920e906cb6fd).
- 시간: R 말미의 자료 조회를 재사용해 20:13:51–20:14:24 UTC에 답 작성·종료 식별을 수행했다(33초). 개별 독해 시간은 미측정이다. 기본 10분 상한 이내다.
- 막힌 점: 실제 버퍼 상태·콜백·장치 로그가 없어 사례 원인은 정할 수 없다.
- 자동 편집 의견: Mermaid 정의가 '아니요→false/남은 버퍼', '예→true/자동 요청 완료 아님→명시 호출'을 나누므로 질문에 맞는다. 실제 도형 배치·읽기 크기·확대·검색은 평가하지 않았다. 완료와 영상 성공을 구분하는 상태 상세 연결은 계속 유용하겠다.

## 원문 관측의 범위

후보에서 위 답과 앵커를 실제로 다시 찾았다. 이를 기본 과업 합산 점수나 독립 신입 성능으로 바꾸지 않는다. 두 번째 노출의 학습 효과와 유지된 대화 문맥 때문에 전후 속도 차이를 문서 개선 효과로 해석할 수 없다. 화면이나 브라우저를 시험하지 않았고, 한정된 질문에 필요한 HTML 절·발췌만 읽었으므로 사이트 전체에 회귀가 없다고 보증하지 않는다. 코드·작성 이력·정답표·이전 결과 파일을 추가로 읽지 않았다. 결과 파일은 이 파일만 썼다.

## 종료 식별

- 종료 build_id: `f6b6072fea0fb8c8e05b82801afb1ffad29d00b1042534b37d15bee0dadd67c8`.
- 종료 manifest SHA-256: `457889301da28033392cce7c44c97886b5bc150b661064bd2e7f9caeeb69a97b`.
- 조회 전후 build_id와 manifest SHA-256은 동일하다. 요청한 후보 식별과 일치하며 평가 중 식별 불일치는 관측하지 않았다.

종료 식별 확인 시각: 2026-11-04 20:14:24 UTC. 첫 식별 시작부터 3분 13초이며 도구·기록 시간을 포함한다. 사람의 독서·회복 시간으로 사용할 수 없다.
