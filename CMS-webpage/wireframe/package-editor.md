# Package Editor UI 와이어프레임

## 개요
- 목적: 새 패키지를 등록하거나 기존 패키지 정보를 편집합니다.
- 접근 경로: 
  - Package List에서 [+ New Package] 버튼 → 신규 등록 모드
  - Package List 또는 상세 페이지에서 [Edit] 버튼 → 편집 모드

## 레이아웃

```
+------------------+--------------------------------------------------+
| Sidebar          | Header: [Create/Edit] Package                    |
| - Dashboard      +--------------------------------------------------+
| - Content        | [← Back to List]                                  |
| - Package ●      |                                                   |
| - Product        | Basic Information                                 |
| - Devices        | ┌────────────────────────────────────────────┐  |
|                  | │ Package ID: [pkg-sand-11___] [Auto Generate]│  |
|                  | │ Product: [SandCraft ▼] *Required              │  |
|                  | │ Name: [SandCraft - 11 Items___] *Required     │  |
|                  | │ Description: [________________________]       │  |
|                  | │              [________________________]       │  |
|                  | │ Status: ( ) Draft  (●) Published              │  |
|                  | └────────────────────────────────────────────┘  |
|                  |                                                   |
|                  | Connected Contents (Edit mode only)               |
|                  | ┌────────────────────────────────────────────┐  |
|                  | │ [+ Add Content]                              │  |
|                  | │                                               │  |
|                  | │ [Content List Table]                          │  |
|                  | │ ☐ c-sand-01 | Sand Animation 01 | [Remove]   │  |
|                  | │ ☐ c-sand-02 | Sand Animation 02 | [Remove]   │  |
|                  | │ ... (11 contents)                             │  |
|                  | └────────────────────────────────────────────┘  |
|                  |                                                   |
|                  | Metadata (Edit mode only)                         |
|                  | ┌────────────────────────────────────────────┐  |
|                  | │ Created: 2024-01-15 14:30:00                  │  |
|                  | │ Updated: 2024-01-20 10:15:00                  │  |
|                  | └────────────────────────────────────────────┘  |
|                  |                                                   |
|                  | [Cancel]                            [Save]        |
+------------------+--------------------------------------------------+
```

## 주요 구성 요소

### 1. 헤더
- **Create Package**: 신규 등록 모드
- **Edit Package**: 편집 모드
- **[← Back to List]**: Package List로 돌아가기

### 2. Basic Information 섹션
모든 모드에서 표시되는 기본 정보 입력 폼

#### Package ID
- **신규 등록**: 자동 생성 또는 수동 입력
  - [Auto Generate] 버튼: "pkg-{랜덤문자열}" 형식으로 자동 생성
  - 수동 입력 시 형식 검증 (소문자, 숫자, 하이픈만 허용)
- **편집 모드**: 읽기 전용 (변경 불가)
- **검증**: 
  - 필수 항목
  - 소문자, 숫자, 하이픈(-)만 허용
  - 중복 확인 (패키지 ID는 고유해야 함)

#### Product (Required)
- **드롭다운 선택**: 등록된 Product 목록에서 선택
- **필수 항목**: 패키지는 반드시 하나의 제품에 속해야 함
- **표시**: Product Name (Product ID)
- **검증**: 선택 필수

#### Name (Required)
- **텍스트 입력**: 패키지 이름 (예: "SandCraft - 11 Items")
- **필수 항목**: 사람이 읽을 수 있는 이름
- **검증**: 
  - 필수 항목
  - 최소 2자 이상
  - 최대 100자

#### Description
- **텍스트 영역**: 패키지에 대한 설명 (선택 사항)
- **용도**: 포함 콘텐츠 요약, 대상 고객, 배포 조건 등
- **검증**: 최대 500자

#### Status
- **라디오 버튼**:
  - ( ) Draft: 작업 중인 상태
  - ( ) Published: 게시 완료 상태 (클라이언트에서 조회 가능)
- **기본값**: Draft (신규 등록 시)
- **주의**: Published로 변경 시 경고 메시지 표시
  - "게시하시겠습니까? 클라이언트에서 이 패키지를 다운로드할 수 있습니다."

### 3. Connected Contents 섹션 (편집 모드만 표시)
패키지에 포함된 콘텐츠 관리

#### [+ Add Content] 버튼
- 클릭 시 콘텐츠 선택 모달 표시
- 등록된 Content 목록에서 선택하여 추가
- 이미 추가된 콘텐츠는 비활성화 표시

#### Content List Table
- **컬럼**:
  - 체크박스: 다중 선택용
  - Content ID: 콘텐츠 고유 ID
  - Name: 콘텐츠 이름
  - [Remove]: 개별 제거 버튼
- **기능**:
  - 드래그 앤 드롭으로 순서 변경 가능
  - [Remove] 버튼: 패키지에서 콘텐츠 제거 (확인 없음)
  - 체크박스로 다중 선택 후 일괄 제거 가능

### 4. Metadata 섹션 (편집 모드만 표시)
- Created: 패키지 생성 일시
- Updated: 마지막 수정 일시
- 읽기 전용 정보

### 5. 액션 버튼
- **[Cancel]**: 변경사항 취소
  - 변경사항이 있으면 확인 다이얼로그 표시
  - "저장하지 않은 변경사항이 있습니다. 정말 취소하시겠습니까?"
- **[Save]**: 패키지 저장
  - 검증 실패 시 에러 메시지 표시
  - 성공 시 Package Detail 페이지로 이동

## 상태별 화면 구성

### 신규 등록 모드 (Create)
- URL: `/package-editor.html` (id 파라미터 없음)
- 표시되는 섹션:
  - ✓ Basic Information (모든 필드 입력 가능)
  - ✗ Connected Contents (신규 등록 후 추가 가능)
  - ✗ Metadata (신규 등록 시 자동 생성)
- Package ID: 자동 생성 또는 수동 입력
- Status: Draft가 기본값

### 편집 모드 (Edit)
- URL: `/package-editor.html?id=pkg-sand-11`
- 표시되는 섹션:
  - ✓ Basic Information (Package ID는 읽기 전용)
  - ✓ Connected Contents (콘텐츠 추가/제거/순서 변경)
  - ✓ Metadata (읽기 전용)
- 기존 데이터를 폼에 채워서 표시

## 인터랙션 플로우

### 신규 패키지 등록
1. Package List에서 [+ New Package] 클릭
2. Package Editor 페이지 로드 (신규 모드)
3. Package ID 자동 생성 또는 수동 입력
4. Product 선택 (필수)
5. Name 입력 (필수)
6. Description 입력 (선택)
7. Status 선택 (Draft/Published)
8. [Save] 클릭
9. 검증 통과 → Package 생성 → Package Detail 페이지로 이동
10. Package Detail에서 [Edit]로 콘텐츠 추가

### 기존 패키지 편집
1. Package List 또는 Detail에서 [Edit] 클릭
2. Package Editor 페이지 로드 (편집 모드, id 파라미터 포함)
3. 기존 데이터를 폼에 채워서 표시
4. 정보 수정:
   - Product 변경 가능 (드롭다운)
   - Name, Description 수정 가능
   - Status 변경 가능 (Draft ↔ Published)
5. 콘텐츠 관리:
   - [+ Add Content]: 콘텐츠 추가
   - [Remove]: 콘텐츠 제거
   - 드래그로 순서 변경
6. [Save] 클릭
7. 검증 통과 → Package 업데이트 → Package Detail 페이지로 복귀

### 콘텐츠 추가
1. [+ Add Content] 클릭
2. 콘텐츠 선택 모달 표시
   - 등록된 모든 Content 목록
   - 이미 추가된 콘텐츠는 비활성화
   - 검색/필터 기능
3. 콘텐츠 선택 (다중 선택 가능)
4. [Add] 클릭
5. 선택된 콘텐츠가 Connected Contents 테이블에 추가

### 콘텐츠 제거
1. 개별 제거: 행의 [Remove] 버튼 클릭 → 즉시 제거
2. 다중 제거: 체크박스로 선택 → [Remove Selected] 클릭 → 확인 후 제거

### 취소 처리
1. [Cancel] 버튼 클릭
2. 변경사항이 있으면 확인 다이얼로그 표시
3. 확인 시 Package List로 이동

## 검증 규칙

### 필수 항목
- Package ID (신규 등록 시)
- Product (신규/편집 모두)
- Name (신규/편집 모두)

### Package ID 검증
- 형식: 소문자, 숫자, 하이픈(-)만 허용
- 패턴: `^[a-z0-9-]+$`
- 중복: 기존 패키지 ID와 중복 불가
- 예시: `pkg-sand-11`, `pkg-fish-basic`

### Name 검증
- 최소 2자 이상
- 최대 100자

### Description 검증
- 최대 500자

### Product 검증
- 유효한 Product ID 선택 필수
- 존재하지 않는 제품은 선택 불가

### Status 변경 검증
- Draft → Published: 경고 메시지 표시
  - "게시하시겠습니까? 클라이언트에서 이 패키지를 다운로드할 수 있게 됩니다."
- Published → Draft: 경고 메시지 표시
  - "게시를 취소하시겠습니까? 이미 배포된 디바이스에 영향을 줄 수 있습니다."

## 에러 처리

### 검증 실패
- 필수 항목 누락: "필수 항목을 입력해주세요."
- Package ID 형식 오류: "Package ID는 소문자, 숫자, 하이픈(-)만 사용할 수 있습니다."
- Package ID 중복: "이미 존재하는 Package ID입니다."
- Name 길이 오류: "Name은 2자 이상 100자 이하로 입력해주세요."
- Description 길이 오류: "Description은 500자 이하로 입력해주세요."

### 서버 에러
- 네트워크 오류: "서버와 통신할 수 없습니다. 잠시 후 다시 시도해주세요."
- 저장 실패: "패키지 저장에 실패했습니다. 다시 시도해주세요."

### 권한 오류
- 편집 권한 없음: "이 패키지를 편집할 권한이 없습니다."

## 변경 추적
- 폼 데이터가 변경되면 `hasChanges` 플래그 설정
- 페이지 이탈 시 (beforeunload 이벤트) 경고 표시
  - "저장하지 않은 변경사항이 있습니다. 정말 떠나시겠습니까?"
- [Cancel] 버튼 클릭 시 변경사항 확인 후 이동

## 비즈니스 로직
1. **신규 등록**: POST /api/packages
   - Package ID, Product ID, Name, Description, Status 전송
   - 성공 시 생성된 Package ID로 Detail 페이지 이동
2. **편집**: PUT /api/packages/{packageId}
   - 수정된 필드만 전송
   - 성공 시 Package Detail 페이지로 복귀
3. **콘텐츠 추가**: 편집 모드에서만 가능
   - Connected Contents 섹션에서 관리
   - 저장 시 contents 배열 전송
4. **Status 변경**: Published로 변경 시 무결성 검증 필요
   - 서버에서 콘텐츠 유효성 확인
   - 해시/서명 검증 후 게시

## 데이터 소스
- Package 엔티티: packageId, productId, name, description, contents, published
- Product 엔티티: Product 드롭다운 목록 생성용
- Content 엔티티: 콘텐츠 추가 모달용

## 추가 고려사항
- Package ID 자동 생성: "pkg-" + 랜덤문자열 (8자)
- Product 드롭다운: Product List API 호출하여 동적 생성
- 콘텐츠 순서: 드래그 앤 드롭 라이브러리 사용 (Sortable.js 등)
- Published 패키지 편집 시 버전 관리 고려 (향후)
- 대용량 콘텐츠 목록: 페이지네이션 또는 가상 스크롤 적용

## 관련 페이지
- [Package List](./package-list.md) - 패키지 목록 페이지
- [Package Detail](./package-detail.md) - 패키지 상세 페이지
