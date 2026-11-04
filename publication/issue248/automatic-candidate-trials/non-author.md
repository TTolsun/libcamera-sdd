# 최종 후보 비작성자 자동 독자 재시험

## 조건과 식별

- 이 시험자는 자동 에이전트이며 사람이 아닙니다. 같은 에이전트가 앞선 배포본으로 B1·B2·S·R·X를 수행했습니다. 용어·과업·탐색 경로의 반복 노출과 학습 효과가 있으며, 독립 cold-reader 또는 실제 사람 평가로 세지 않습니다. 사람의 부담·흥미·자연스러움·망각에 관한 점수는 만들지 않습니다.
- 2026-11-04 20:11:31 UTC에 내용 조회 전 `build/issue248/candidate/site-manifest.json`을 읽어 build_id `f6b6072fea0fb8c8e05b82801afb1ffad29d00b1042534b37d15bee0dadd67c8`의 일치를 확인했습니다.
- 내용 근거는 `build/issue248/candidate/`의 HTML과 그 안의 발췌뿐입니다. 프로젝트 코드·정답표·작성 이력·이전 결과 파일은 읽지 않았습니다. 이 대화 문맥의 이전 시험 내용은 남아 있습니다. 외부 전체 소스 링크를 열지 않았습니다.
- 시작 주소에 대응하는 후보 index.html에서 시작해 파일을 파싱했습니다. 브라우저 방문·뒤로 가기·화면·확대·검색 동작을 시험하지 않았습니다. 아래 공개 URL은 후보 HTML의 대응 주소이며, 해당 후보가 그 URL에 이미 배포됐음을 뜻하지 않습니다. 실제 방문 경로는 후보 안의 파일과 앵커로 적습니다.
- 기본 과업별 순수 소요 시간은 미측정입니다. 시각은 도구 호출 전후의 관측값이며 사람의 과업 시간으로 해석할 수 없습니다. 각 기본 과업 10분 상한 안에서 진행합니다. 추가 영어 기술 대조는 기본 과업 평가에 합산하지 않습니다.

## B1

실제 답: `completeBuffer()`는 개별 버퍼 완료를 앱에 알리고 요청 내부의 버퍼 추적 정보를 갱신합니다. 마지막 버퍼가 완료돼도 요청 완료는 자동으로 이뤄지지 않습니다. 파이프라인 핸들러가 `completeRequest()`를 명시적으로 호출해야 합니다. 파이프라인 핸들러는 두 함수를 CameraManager 스레드에서 호출해야 합니다. `completeRequest()` 뒤에는 해당 요청을 더 이상 접근해서는 안 되며, 완료된 요청은 제출 순서로 앱에 반환됩니다.

근거와 실제 경로: `index.html → vendor-integration.html#요청을-장치에-전달하고-반환하기 → #구현-뒤-확인할-계약과-실행-한계`. 첫 절에서 차이와 completeBuffer 호출자를, 뒤 절에서 completeRequest의 스레드를 확인했습니다. 20:11:50 UTC까지 본문 답을 찾았습니다. [요청을 장치에 전달하고 반환하기](https://ttolsun.github.io/libcamera-sdd/vendor-integration.html#요청을-장치에-전달하고-반환하기), [구현 뒤 확인할 계약과 실행 한계](https://ttolsun.github.io/libcamera-sdd/vendor-integration.html#구현-뒤-확인할-계약과-실행-한계)에 대응합니다. 발췌 연결은 같은 페이지의 `#source-2c79d29bf7fe6699`, `#source-7b871a70bfc9aa8f`, `#source-e1c3bfd748ad8a33`, `#source-699c5b0f43c595cf`, `#source-72e48606b2a92dcc`입니다. 발췌 원문 대조는 S의 재검색 단계에서 수행합니다.

막힌 점과 편집 의견: 답을 찾는 데 막히지 않았습니다. completeRequest의 호출 스레드는 다른 절에 있어 두 절을 합쳐야 합니다. 버퍼 완료와 요청 완료를 보여주는 상세 문서 또는 그림으로 직접 연결하면 이 질문에 필요한 근거를 모을 수 있습니다. 화면과 그림 렌더링 효과는 미측정입니다.

## B2

실제 답: 요청 전달 대상은 `PipelineHandler::queueRequest()`이며 `Camera::queueRequest()`가 `invokeMethod()`의 인자로 넘깁니다. 본문에 지정한 연결 방식은 `ConnectionTypeQueued`입니다. 예약 표시는 메서드가 인자로 전달됐음을 뜻하고 그 표식만으로 비동기 실행을 보장하지 않습니다. 연결 방식과 동기화 계약을 따로 확인해야 합니다. 정적 기록의 번호는 실행 순번이 아니며, 호출 화살표도 시간 순서나 모든 경로 실행을 뜻하지 않습니다. 이 목록만으로 조건 분기·반복 횟수·실행 스레드를 확정할 수 없고 가상 호출은 실제 객체에 달립니다.

근거와 실제 경로: `index.html → scenarios/queue_request.html#큐로-전달된-요청의-준비와-실패 → #주요-확인-지점 → #주요-호출-관계 → #추적-범위와-경계`. 같은 조회에서 앞 절 `#요청을-제출하기-전에-갖출-조건`도 읽었습니다. 20:11:50 UTC까지 본문 답을 찾았습니다. 대응 주소는 [큐로 전달된 요청의 준비와 실패](https://ttolsun.github.io/libcamera-sdd/scenarios/queue_request.html#큐로-전달된-요청의-준비와-실패), [주요 확인 지점](https://ttolsun.github.io/libcamera-sdd/scenarios/queue_request.html#주요-확인-지점), [추적 범위와 경계](https://ttolsun.github.io/libcamera-sdd/scenarios/queue_request.html#추적-범위와-경계)입니다. 호출부의 발췌 앵커는 `#source-997ecce495182b6b`입니다.

막힌 점과 편집 의견: 예약의 의미와 추적 한계는 직접 적혀 있어 답을 찾을 수 있었습니다. ‘설계 질문과 검증 범위’에서는 아래와 같은 원문을 실제로 다시 확인했습니다.

> Camera::queueRequest()의 캡처용 요청 접수 목적과 Running 상태·thread-safe 계약 및 연결/상태 오류 -ENODEV/-EACCES를 한 번 설명하세요. 요청을 만든 카메라 불일치 -EXDEV, RequestPending·controls infoMap·버퍼 존재·활성 스트림 검사에 따른 -EINVAL을 조건별로 설명하세요. 반환값 0과 requestCompleted 신호에 의한 요청 완료 알림을 구분하되 같은 상태나 오류 목록을 다시 요약하지 마세요.

다음 안내도 ‘Camera::queueRequest의 patchControlList 및 ConnectionTypeQueued 전달, 상태 변경을 PipelineHandler가 처리한다는 주석의 범위를 설명하세요.’로 시작하며, 마지막에는 ‘대기 큐 앞의 미준비 요청 또는 장치 한도에서 멈추고, doQueueRequest가 카메라 데이터의 queuedRequests_와 sequence_를 갱신하며 cancelled_이면 completeRequest, 장치 큐잉 오류면 cancelRequest인 분기를 구분하세요.’라고 적혀 있습니다.

이 후보 안내에는 앞선 시험에서 보았던 ‘세 문단 이내로 작성하세요’, ‘소스 한 줄마다 문단을 만들지 마세요’라는 문구는 보이지 않았습니다. 그러나 ‘한 번 설명하세요’, ‘조건별로 설명하세요’, ‘같은 상태나 오류 목록을 다시 요약하지 마세요’는 여전히 독자에게 노출됩니다. 독자의 질문을 짧은 의문문으로 제시하는 편집이 필요합니다. 무엇을 왜 수정했는지는 추측하지 않았습니다. 그림 렌더링은 평가하지 않았습니다.

## S: 추가 조회 없이 제 말로 설명

이 문단은 위 두 페이지를 읽은 뒤 다른 후보 HTML을 조회하기 전에 작성했습니다. 이전 대화 문맥이 유지되므로 사람의 무참조 회상 시험은 아닙니다.

제출이 성공했다는 것은 입력 검사를 통과한 요청을 파이프라인에서 처리하도록 넘겼다는 뜻입니다. 프레임 처리가 끝났거나 앱이 완료 신호를 받았다는 뜻은 아닙니다. 준비와 장치 전달, 각 버퍼 완료, 요청 완료와 앱 반환은 뒤에 따로 남아 있습니다. 모든 버퍼가 끝나더라도 핸들러가 요청을 명시적으로 완료해야 합니다. 그러므로 성공 반환 후 알림이 없다는 사실만으로 고장 위치를 정할 수 없으며, 같은 요청이 어느 단계까지 갔는지 관측해야 합니다.

아래에는 이 설명을 기록한 뒤 수행한 근거 재검색 결과를 추가합니다.

### S의 근거 재검색

실제 재검색 경로는 `index.html#지금-필요한-문서 → request-lifecycle.html#제출에서-완료까지 → request-diagnosis.html#실패-위치별-확인-순서 → #source-01ad7c6605c3296a`입니다. index.html의 ‘지금 필요한 문서’ 절과 요청 처리 페이지 본문, 진단 본문을 읽었으며, 앞서 본 vendor-integration과 queue_request의 발췌도 다시 열었습니다. 20:13:12 UTC에 재검색 결과를 확보했습니다. 실제 기기나 실행 로그는 읽지 않았습니다.

[제출에서 완료까지](https://ttolsun.github.io/libcamera-sdd/request-lifecycle.html#제출에서-완료까지)는 0 반환과 요청 완료를 구분하며, [실패 위치별 확인 순서](https://ttolsun.github.io/libcamera-sdd/request-diagnosis.html#실패-위치별-확인-순서)는 접수 뒤 관측할 값과 분기를 안내합니다. queue_request.html의 [L1308~1380 발췌](https://ttolsun.github.io/libcamera-sdd/scenarios/queue_request.html#source-3c1e4a3c695a8890) 및 [L1373 발췌](https://ttolsun.github.io/libcamera-sdd/scenarios/queue_request.html#source-997ecce495182b6b)에서 0 반환과 ConnectionTypeQueued, 별도 requestCompleted 계약을 확인했습니다. vendor-integration.html의 L551·553·556·558·582 발췌도 실제로 읽어 B1의 호출자와 스레드 답을 확인했습니다.

막힌 점은 없었습니다. 준비·장치 전달·버퍼 완료·요청 반환을 별도로 설명하므로 성공만으로 어느 단계의 문제인지 단정하지 않는 답을 근거와 연결할 수 있었습니다. 순수 재검색 시간은 미측정이며 이전 노출의 영향이 있습니다. 그림 제목과 검증 범위의 텍스트는 읽었지만 그림을 렌더링하지 않았으므로 시각적 효과는 미평가입니다.

## R: 중단 전 자유 메모

증상은 과업이 제시한 ‘제출 함수의 성공 반환, 완료 알림 없음’이다. 실제 요청을 실행해 얻은 관측값은 없다. 지금 확인한 것은 접수 0과 완료 알림이 별개라는 문서 계약이다. 준비·장치 전달·버퍼 상태·명시적 요청 완료·제출 순서 반환 중 어느 곳에서 멈췄는지는 미확인이다.

다음에는 원래 호출 위치와 요청 식별자, 반환값을 먼저 남기고 같은 요청을 따라간다. waitingRequests_에 항목이 있는지, queuedRequests_.size()와 maxQueuedRequestsDevice_가 같은지, 선두 prepared_가 참인지 관측한다. 큐 한도 또는 미준비라면 해당 대기 원인을 조사한다. 통과했다면 cancelled_를 확인하고, 참이면 completeRequest 경로를, 거짓이면 queueRequestDevice의 ret와 오류 때 cancelRequest 경로를 조사한다. 그다음 각 버퍼의 bufferCompleted와 completeBuffer 반환값, 마지막 버퍼 이후의 completeRequest 명시 호출을 확인한다. 완료 처리까지 확인했는데 앱 알림이 없으면 queuedRequests_ 선두의 RequestPending을 확인한다. 소프트웨어 큐 크기를 실제 장치 전달 수와 동일시하지 않는다.

근거 페이지는 `request-diagnosis.html#실패-위치별-확인-순서`이다. 선두 준비는 `#source-a637b7daf9acb7ac`, 취소 분기는 `#source-0bb6ebc961be6e80`, 장치 반환 오류는 `#source-1e06e477d10056b7`, 버퍼/요청 완료와 제출 순서는 `#source-01ad7c6605c3296a`에서 확인했다. 네 앵커와 관측할 필드를 메모에 남긴다. 후속 실행 관측은 아직 하나도 없다.

이 메모를 저장한 뒤 문서 조회를 중단한다. 자동 탐색 재개 시험이며 사람의 5분 주의 중단이나 망각을 재현하지 않는다. 대화 문맥은 유지된다.

### R: 자동 탐색 재개

20:13:48 UTC에 중단 전 메모 저장을 마쳤고 5초 자동 대기를 수행했습니다. 20:14:00 UTC의 다음 조회에서는 후보 문서 대신 방금 저장한 자기 메모만 읽었습니다. 이어 후보 시작 주소 index.html로 돌아가 메뉴의 ‘구성과 요청 오류 조사’ 연결을 다시 찾고, 메모에 남긴 페이지·절·네 발췌를 조회했습니다. 20:14:13 UTC에 재개 후 근거를 확보했습니다.

실제 경로는 `index.html → request-diagnosis.html#실패-위치별-확인-순서 → #source-a637b7daf9acb7ac → #source-0bb6ebc961be6e80 → #source-1e06e477d10056b7 → #source-01ad7c6605c3296a`입니다. [실패 위치별 확인 순서](https://ttolsun.github.io/libcamera-sdd/request-diagnosis.html#실패-위치별-확인-순서), [준비 관측 발췌](https://ttolsun.github.io/libcamera-sdd/request-diagnosis.html#source-a637b7daf9acb7ac), [완료와 반환 발췌](https://ttolsun.github.io/libcamera-sdd/request-diagnosis.html#source-01ad7c6605c3296a)에 대응합니다.

메모만 읽은 뒤 복원한 상태는 ‘접수 성공만 주어졌으며 실제 후속 값은 미확인’입니다. 다음 행동은 같은 요청의 큐 한도와 선두 준비 상태 관측입니다. 이후 분기는 메모의 cancelled_, 장치 ret, 버퍼 완료, 명시적 요청 완료, 제출 큐 선두 순서로 다시 찾을 수 있었습니다. 실제 값이 없으므로 한 원인을 선택하지 않았습니다. 후보 조회 중단 구간은 약 12초이며 그 안에 5초 자동 대기를 넣었습니다. 이것은 자동 탐색 재개만 확인한 것이며 사람의 5분 중단·망각을 재현한 시험이 아닙니다.

막힌 점은 없었습니다. 앵커와 관측할 필드 이름을 남긴 메모로 근거를 재조회할 수 있었습니다. 진단 절에 버퍼 등록 실패와 접수 성공 이후 완료 조사가 함께 있으므로 완료 누락에 맞춘 상태·관측값·미확인점·근거·다음 분기 표가 있으면 문서 항목과 메모를 대조하기 쉽겠습니다. 이 편집 의견은 사람의 부담 측정이 아닙니다. 브라우저 복귀 동작과 그림의 시각적 효과는 미평가입니다.

## X

실제 답: 같은 요청의 두 버퍼 중 하나만 내부적으로 완료됐고 다른 하나가 아직 미완료라는 조건이 확정됐다면 모든 버퍼 완료가 아닙니다. 문서 계약상 해당 completeBuffer 결과는 false입니다. 이 사실만으로 요청 완료 또는 앱의 requestCompleted를 단정할 수 없습니다. 마지막 버퍼가 완료돼도 별도 completeRequest 호출 의무가 남습니다.

반면 ‘콜백 하나만 관측했다’는 로그만 있다면 그것을 ‘다른 버퍼가 내부적으로 미완료’라고 바꿔 단정할 수 없습니다. 발췌는 `bufferCompleted.emit(request, buffer)` 뒤에 내부 completeBuffer를 호출합니다. 요청·버퍼 식별자, 콜백의 기록 위치, 각 반환값과 다른 버퍼의 완료·취소를 확인해야 합니다. 모든 버퍼 완료 후에는 CameraManager 스레드에서 completeRequest가 호출됐는지 확인하고, 요청 완료 처리까지 확인한 뒤 앱 반환이 없다면 제출 큐 선두의 RequestPending 여부를 확인합니다. 실제 미완료 원인이 장치 고장인지 완료 처리 누락인지는 이 가정만으로 알 수 없습니다.

근거는 직전에 다시 읽은 [L547~620 발췌](https://ttolsun.github.io/libcamera-sdd/request-diagnosis.html#source-01ad7c6605c3296a)와 같은 페이지 [버퍼 완료와 명시적 요청 완료의 경계](https://ttolsun.github.io/libcamera-sdd/request-diagnosis.html#버퍼-완료와-명시적-요청-완료의-경계), [제출 큐의 선두 상태와 반환 순서](https://ttolsun.github.io/libcamera-sdd/request-diagnosis.html#제출-큐의-선두-상태와-반환-순서)입니다. 실제 경로는 R에서 되돌아온 마지막 발췌에서 그대로 답을 작성했으며 추가 페이지 이동은 없었습니다. 별도 소요 시간은 미측정이고, 실행 로그나 실제 두 버퍼 동작은 확인하지 않았습니다. 막힌 점은 없었습니다. true/false 조건은 본문과 발췌에서 찾을 수 있었습니다. 그림의 시각적 효과와 이해도는 미평가입니다.

## 추가 영어 기술 대조: 기본 과업과 별도

이 대조는 B1·B2·S·R·X의 점수나 판정에 합산하지 않습니다. 사람 척도 점수는 어느 항목에도 부여하지 않았습니다. 수정 이유나 의도한 정답을 추측하지 않고 후보 문장과 연결 발췌의 관계만 비교했습니다.

실제 경로는 `en/vendor-integration.html#요청을-장치에-전달하고-반환하기 → #source-a9ed7dcbf54ccaff`이며, 20:13:12 UTC의 조회에서 확인했습니다. 대응 주소는 [영어 요청 전달 절](https://ttolsun.github.io/libcamera-sdd/en/vendor-integration.html#요청을-장치에-전달하고-반환하기)과 [L535~540 발췌](https://ttolsun.github.io/libcamera-sdd/en/vendor-integration.html#source-a9ed7dcbf54ccaff)입니다.

후보 문장 원문:

> When processing a request containing a set of buffers associated with streams and a set of parameters, the queueRequestDevice implementer must configure the device so that the parameters are applied to the frames captured in the buffers provided in the request.

연결 발췌 원문:

> The request contains a set of buffers associated with streams and a set of parameters.

후보 문장과 발췌 모두 `associated with streams`는 버퍼 집합에 연결됩니다. 요청은 그 버퍼 집합과 파라미터 집합을 포함한다고 설명합니다. 발췌의 ‘parameters will be applied to the frames captured in the buffers provided in the request’와 후보의 프레임 적용 설명도 대응합니다. 이 확인 범위에서 스트림 관계의 연결 대상이 어긋나는 문구는 찾지 못했습니다.

인접한 스트림 설정 관계도 별도로 확인했습니다. `en/vendor-integration.html#구현할-설정-인터페이스`는 ‘associate a Stream instance with each StreamConfiguration entry in CameraConfiguration by using StreamConfiguration::setStream()’이라고 적습니다. [L309~311 발췌](https://ttolsun.github.io/libcamera-sdd/en/vendor-integration.html#source-f3cf94b1dc7b9457) 역시 ‘associate a Stream instance to each StreamConfiguration entry in the CameraConfiguration using the StreamConfiguration::setStream() function’이라고 적어 Stream 인스턴스의 연결 대상은 각 StreamConfiguration 항목입니다. 이 비교에서 막힌 점은 없었습니다. 전체 영어 번역의 정확성을 판정한 것은 아닙니다.

## 종료 확인과 적용 한계

종료 시 manifest build_id를 다시 읽었으며 `f6b6072fea0fb8c8e05b82801afb1ffad29d00b1042534b37d15bee0dadd67c8`로 같았습니다. 조회 때 기록한 index.html, vendor-integration.html, scenarios/queue_request.html, request-lifecycle.html, request-diagnosis.html, en/vendor-integration.html의 SHA-256도 종료 확인에서 모두 같았습니다. 서로 다른 후보를 섞지 않았습니다.

기본 과업에서 답·근거를 찾았다는 자동 관측과, 질문 안내의 작성 지시 노출·스레드 설명 분산·조사 재개용 상태표에 대한 편집 의견을 보존했습니다. 동일 에이전트의 반복 노출 때문에 탐색 성공을 독립 첫 독자의 성공이나 이전 후보보다 개선된 사람 성능으로 해석할 수 없습니다. 화면·브라우저 조작·사람의 기억은 시험하지 않았습니다. 내용 조회는 후보 HTML과 발췌만 사용했고 결과는 이 파일에만 저장했습니다. 코드 변경은 없습니다.
