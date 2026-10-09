# libcamera 설계 문서 검증

**[RKISP1 카메라별 왜곡 보정](https://ttolsun.github.io/libcamera-sdd/rkisp1-dewarp.html)** 가이드를 추가했습니다. 카메라별 보정값의 소유권, 입력 오류와 스트림 적용 시점을 소스 근거와 연결합니다. [영어판](https://ttolsun.github.io/libcamera-sdd/en/rkisp1-dewarp.html)도 함께 제공합니다.

## 재현 기준과 확인 결과

- 공식 upstream의 새 커밋 3개를 동기화했습니다. 분석 기준은 `06c3e2d719490aad8ce789fb5d2ad4dfa1459bfb`이며 생성기는 `3bc2fef9782523e1f0edc80c3f110c04b9c270ff`입니다.
- WSL에서 IPU3·RKISP1·UVC와 GStreamer를 빌드하고 TU 171개를 다시 추출했습니다. 파싱 오류와 시나리오 진입점 누락은 0개입니다.
- 인용 위치 5,069개, 필수 설계 질문 35개와 소스 발췌 95개의 연결을 검사했습니다. 원고 15편에서 한국어·영어 각 16페이지를 생성했습니다.
- 문서 크기·증가율·반복 문단과 등록된 Feature의 근거 누락을 게시 전에 검사합니다. 이번 원고 15편과 Feature 3개는 검사를 통과했습니다. Feature 발견과 문서 분할·통합의 의미 판단은 자동화하지 않았습니다.
- 생성기 테스트 273개와 Windows/Linux의 Python 3.11·3.14 CI가 통과했습니다. 내부 링크 오류는 0개이며 manifest와 반복 빌드 동일성을 확인했습니다. 앱 브라우저에서 데스크톱·모바일 화면, 검색과 영어판 전환을 확인했습니다.
- 사람의 내용 승인, 여러 카메라의 동시 촬영·보정 화질과 사내 Camera HAL 검증은 수행하지 않았습니다.

[배포 기록](run.json)과 [산출물 해시](docs/site-manifest.json)를 확인할 수 있습니다. 생성기 변경은 [PR #52](https://github.com/TTolsun/camera-hal-sdd-generator/pull/52)에 있습니다.

## 동기화와 배포

`upstream/master`는 공식 소스 이력을 보관하고 `main`의 `docs/`를 GitHub Pages로 게시합니다. 공개 환경에는 정기 예약을 설치하지 않으며 생성기 작업과 함께 upstream 확인·문서 보완·검증·배포를 수행합니다.

생성 HTML을 직접 수정하지 않습니다. 원고·설정·테마는 생성기에서 관리하며 이 저장소에는 공개 libcamera 산출물만 배포합니다. 사내 Camera HAL 소스와 파생 facts·프롬프트·문서·로그는 올리지 않습니다. 영어 번역도 사람 검토 전이며 원문의 승인 상태를 상속하지 않습니다.
