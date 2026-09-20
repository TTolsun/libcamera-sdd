# libcamera 설계 문서 검증

**공개 libcamera 소스에서 생성한 설계 문서의 첫 검토용 스냅샷입니다.**

| 문서 | 상태 |
|---|---|
| [카메라와 요청 모델](docs/camera-model.md) | 인용 형식 검토가 필요합니다. |
| [Pipeline Handler](docs/pipeline-handler.md) | 인용 검증을 통과했습니다. 내용은 사람 검토 전입니다. |
| [IPA 관리와 구현 진입점](docs/ipa.md) | 인용 검증을 통과했습니다. 내용은 사람 검토 전입니다. |

[웹 문서 열기](https://ttolsun.github.io/libcamera-sdd/) · [전체 HTML 내려받기](docs/index.html)

GitHub Pages는 `main` 브랜치의 `docs/`를 게시합니다. 생성 문서의 검토 상태를 확인하고 사용하세요.

## 소스와 생성기

- 원본: [libcamera upstream](https://gitlab.freedesktop.org/camera/libcamera)
- 분석 커밋: `279d355ef8f7a4f98bb0a3004c0f788387814506`
- 생성기: [camera-hal-sdd](https://github.com/TTolsun/camera-hal-sdd)
- [실행 및 검증 기록](run.json)

## 브랜치 역할

| 브랜치 | 역할 |
|---|---|
| `main` | 문서, HTML, 실행 기록을 관리합니다. |
| `upstream/master` | libcamera 원본 커밋 이력을 보존합니다. 문서를 추가하지 않습니다. |

upstream 동기화는 `upstream/master`만 갱신합니다. 문서 변경은 별도 작업 브랜치에서 검토한 뒤 `main`에 반영합니다. 원본 브랜치에는 force push와 문서 커밋을 하지 않습니다.

## 현재 검증 범위

WSL2 Ubuntu 26.04에서 IPU3·RKISP1·UVC와 GStreamer를 빌드했습니다. 171개 translation unit에서 파싱 오류는 0건이었고, 1,005개 클래스와 4,825개 인용 위치를 확보했습니다. 핵심 클래스와 파일·줄 위치 검증을 통과했습니다.

문서 서술은 Windows의 로컬 Ollama `qwen3.5:4b`가 생성했습니다. 인용 검사 통과는 문장의 의미가 맞다는 보증이 아닙니다. 문장 품질, 호출 관계와 용어를 추가 검토해야 합니다. 생성기의 `simple_compdb` 표시는 현재 메타데이터 한계이며 실제 입력은 Meson compile DB입니다.

## 다음 구현 단계

커밋 감시, 실패 재시도, 문서 변경 PR 생성, 승인 후 게시를 연결해야 합니다. 현재 자동 갱신 작업이나 예약 작업은 활성화하지 않았습니다. GitHub에서 소스를 동기화하더라도 로컬 Ollama를 사용하는 문서 생성은 집의 실행기가 담당합니다.

다음 단계: [카메라와 요청 모델](docs/camera-model.md)의 검토 상태를 확인합니다.
