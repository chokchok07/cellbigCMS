# 콘텐츠 에디터 와이어프레임

## ASCII Layout

```
┌───────────────────────────────────────────────────────────────────────────┐
│  Content Editor                          [Draft ▼] [Save] [Publish]          │
├───────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  📝 기본 정보                                                           │
│                                                                           │
│  Content ID: [101]  (자동생성, 읽기전용)                              │
│                                                                           │
│  제목 (JSON):                                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ {"ko":"샌드크래프트 - 해변", "en":"SandCraft - Beach"}         │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                           │
│  설명 (JSON, optional):                                                    │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ {"ko":"해변에서 즐기는 샌드 게임", "en":"Sand game on beach"} │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                           │
│  Type: [single ▼]                                                          │
│  Category: [___________________]                                           │
│  Product ID: [201 ▼]                                                      │
│                                                                           │
│  Thumbnail (이미지 파일 업로드):                                          │
│  [파일 선택...] [미리보기 이미지]                                      │
│                                                                           │
│  Entry Point (ZIP 내 실행 경로):                                          │
│  [/app/sand/beach.exe]                                                      │
│                                                                           │
├───────────────────────────────────────────────────────────────────────────┤
│  📊 버전 히스토리 (content_versions 테이블)                                    │
│  ┌─────┬──────────┬────────────────────┬────────┬──────────┬──────┬────────┐  │
│  │ Ver │ Date     │ Artifact File      │ Size   │ Checksum │Latest│ Action │  │
│  ├─────┼──────────┼────────────────────┼────────┼──────────┼──────┼────────┤  │
│  │v2.1 │2026-02-10│content-101-v2.1.zip│45.2 MB │abcd12... │  ✓   │ [View] │  │
│  │v2.0 │2026-01-15│content-101-v2.0.zip│43.8 MB │def456... │      │ [View] │  │
│  └─────┴──────────┴────────────────────┴────────┴──────────┴──────┴────────┘  │
│                                                                                 │
│  Release Notes: [_____________________________________________________]        │
└─────────────────────────────────────────────────────────────────────────────────┘
```

목적: 콘텐츠 메타데이터를 관리하고 버전 히스토리를 확인하는 화면. 아티팩트(ZIP) 업로드는 버전 등록 화면에서 수행합니다.

레이아웃:
- 상단 바: [제품 선택] [전역 검색] [알림 아이콘] [사용자 메뉴]
- 좌측 사이드바: Dashboard / Content(활성화) / Package / Product / Devices / Reports / Settings
- 메인 영역 헤더: Content Editor 제목, 상태(Draft/Staged/Published) 토글, 저장 및 Publish 버튼
- 메인 영역: 기본 정보 폼
  - contentId (자동 생성, 읽기 전용)
  - title (JSON 형식 다국어 지원: `{"ko":"한글","en":"English"}`)
  - description (JSON 형식 다국어 지원, optional)
  - type (single/container/child/mixed)
  - category (optional)
  - productId 선택 (optional)
  - thumbnail (이미지 파일 업로드, optional, 미리보기 표시)
  - entryPoint (ZIP 내 실행 파일 경로, optional - container는 생략 가능)
- 하단: 버전 히스토리(최근 N개, content_versions 테이블 참조), 신규 버전 등록 버튼

주요 플로우:
1. 기본 정보 입력 → contentId는 자동 생성 (읽기 전용)
2. 다국어 제목/설명을 JSON 형식으로 입력 (BCP-47 표준, 예: `{"ko":"한글","en":"English"}`)
3. Type(single/container/child/mixed), Category, Product ID 선택
4. Thumbnail 이미지 업로드 (미리보기 제공)
5. Entry Point (ZIP 내 상대 경로) 입력 - container 타입은 생략 가능
6. 저장(Save) → contents 테이블에 메타데이터 저장
7. 신규 버전 등록 버튼 클릭 → 버전 등록 화면으로 이동 (여기서 ZIP 업로드)
8. Publish 버튼 → 현재 상태를 published로 변경

컴포넌트/검증:
- Title은 필수이며 JSON 형식의 다국어 객체 또는 단일 문자열 지원 (BCP-47 키)
  - 예시: `{"ko":"한글 제목","en":"English Title"}`
  - 유효한 JSON 형식인지 검증 필요
- Description은 최대 255자 권장 (JSON 형식 또는 단일 문자열)
- Thumbnail은 이미지 파일(jpg, png, gif) 업로드 및 미리보기, 최대 2MB 권장
- Entry Point는 ZIP 내 상대 경로 (container 타입은 선택적)
- Type=container인 경우 하위 콘텐츠 의존성 검증 필요
- 민감한 변경(Publish/삭제)는 확인 모달

버전 관리:
- 버전 히스토리는 content_versions 테이블에서 관리
- 각 버전은 artifact_url, artifact_filename, artifact_size_bytes, checksum 포함
- 신규 버전 등록은 별도 화면에서 ZIP 파일과 함께 업로드
- 버전 히스토리 테이블에서 각 버전의 상태, 배포 대상, 업데이트 타입 확인 가능

UX 노트:
- 자동 저장(임시) 기능과 명시적 Publish 분리
- 다국어 필드는 JSON 형식으로 입력 (BCP-47 표준 언어 코드 사용)
  - UI에서 JSON 유효성 검사 및 피드백 제공
  - 예시: `{"ko":"한글 제목","en":"English Title"}`
- Entry Point는 ZIP 내부의 상대 경로로 입력
- Thumbnail은 파일 업로드 후 미리보기 제공
- 아티팩트 업로드는 버전 등록 화면에서 수행 (분리된 워크플로우)
- Type=container 선택 시 하위 콘텐츠 목록 추가 UI 표시
- content_versions 테이블 기반 버전 관리로 롤백 및 버전 비교 지원