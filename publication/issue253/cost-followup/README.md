# #253 추가 비용과 검증 결함 수정

[생성기 PR #264](https://github.com/TTolsun/camera-hal-sdd-generator/pull/264)를 병합했습니다. 소스 커밋 이월과 사이트 출력이 같은 명시 검토 프로필을 사용하며, 개요 그림의 대상은 대상 자신의 프로필 또는 발행 기본값으로 검증합니다. 역사 CLI는 실행하지 않습니다. 소스·질문·근거·본문 검사는 유지합니다.

qcam을 포함한 실제 부모·머리 빌드·추출과 영향 분석을 별도로 측정했습니다. 증분 빌드 4.435초, 변경 뒤 재추출 622.896초, 영향 분석 1.075초입니다. 최초 구축·환경 설치·실패는 [원본 장부](linux-run-02/execution.json)와 [전체 증거](https://github.com/TTolsun/camera-hal-sdd-generator/tree/cdfbd0f3e35c80cb94dd95891577583b2962761f/examples/libcamera/validation/issue253/runs/cost-followup)에 별도로 남았습니다. 전체 갱신 비용·사람 검토 시간은 미완료이며 절감률을 만들지 않습니다.

실제 공개 원고의 추가 이월 대조에서는 수정 전 4개와 수정 후 28개를 이월했고, 새 qcam facts와 달라진 구성요소 색인 1개는 계속 차단했습니다. 이 결과는 프로필 처리 결함의 수정 증거이며 독자 업무 효과가 아닙니다. [상세 결과](https://github.com/TTolsun/camera-hal-sdd-generator/blob/cdfbd0f3e35c80cb94dd95891577583b2962761f/docs/libcamera/records/issue253/cost-qt-result.md)를 확인하세요.

원래 24개 자동 독자 시행과 고정 비교 버전은 보존합니다. 사람 참가자는 0명이고 사람 평가는 미완료입니다. T2·D2 설명 보완, D1 연결 개선과 같은 기준의 별도 재평가가 남습니다. 자동 검토·배포를 사람 승인이나 사내 HAL·실기기 검증으로 바꾸지 않습니다.

이 공개 반영은 추가 증거와 그 연결입니다. 현재 제품 문서 build `9d1838449623639b698d377feea05bc79198c1a0a1b586e9c28584450cb6dbf7`의 330개 파일을 manifest와 대조했고 문서 파일은 변경하지 않았습니다. 새 제품 생성·번역·최신 upstream 전체 반영을 완료했다고 주장하지 않습니다. Pages와 공개 URL은 병합 뒤 별도 확인합니다.
