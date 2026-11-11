# 공개 libcamera 항목별 시각화 검증

`release.json`에 분석한 libcamera 커밋, 생성기 커밋, 발행 build ID와 실효 설정 지문을 기록했습니다. `item-audit-before-after.json.gz`에는 질문별 전후 판정, 본문 분량, 그림, 근거 창과 검토 범위가 있습니다. `public103-retention-baseline-proof.json`에는 직전 공개 질문과 홈 앵커 변경의 대응 관계가 있습니다.

`release-inputs.tar.xz`는 실제 발행 입력의 원본 바이트를 보존합니다. 다른 작업 환경에서는 압축을 푼 뒤 기록된 소스 커밋과 경로를 연결하고, `strict-publication.yaml`로 사이트를 빌드합니다. 출력 파일과 지문은 사이트 manifest에서 확인할 수 있습니다.

독립 CLI 근거 검토와 자동 검증을 수행했습니다. 사람 검토는 대기 상태입니다. 가상 캡처 관측에는 기존 기록의 커밋과 실행 조건을 유지했습니다.
