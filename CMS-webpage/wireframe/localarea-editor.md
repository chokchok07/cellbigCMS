# LocalArea Editor UI 와이어프레임

## 개요
- 목적: 신규 지역(LocalArea)을 등록하거나 기존 지역 정보를 편집합니다.
- 접근 경로: 
  - 신규: LocalArea List에서 [+ Register LocalArea] 버튼 클릭
  - 편집: LocalArea List 또는 LocalArea Detail에서 [Edit] 버튼 클릭

## 레이아웃
```
┌───────────────────────────────────────────────────────────────────────────┐
│ [Product ▼]  🔍 Search...          🔔 (3)  👤 Admin                      │
├─────────────┬─────────────────────────────────────────────────────────────┤
│             │                                                             │
│ 📊 Dashboard│  🌏 LocalArea Editor                  [Cancel] [Save]      │
│ 🏢 Product  │  Create New LocalArea / Edit: Seoul                        │
│ 📦 Package  │                                                             │
│ 📄 Content  │  ┌──────────────────────────────────────────────────────┐  │
│ 💻 Devices  │  │ 📋 기본 정보 *필수                                   │  │
│ 🏪 Stores   │  │                                                      │  │
│ 🌏 LocalAreas  │ LocalArea ID: [___________________] [Generate ID]    │  │
│ 📈 Reports  │  │ (편집 시 읽기전용)                                   │  │
│ ⚙️  Settings│  │                                                      │  │
│             │  │ Area Name *: [___________________________]           │  │
│             │  │                                                      │  │
│             │  │ Description:                                         │  │
│             │  │ ┌─────────────────────────────────────────────────┐│  │
│             │  │ │                                                 ││  │
│             │  │ │  지역에 대한 상세 설명을 입력하세요...          ││  │
│             │  │ │                                                 ││  │
│             │  │ └─────────────────────────────────────────────────┘│  │
│             │  └──────────────────────────────────────────────────────┘  │
│             │                                                             │
│             │  ┌──────────────────────────────────────────────────────┐  │
│             │  │ 🌳 계층 구조                                         │  │
│             │  │                                                      │  │
│             │  │ Parent Area: [Select Parent Area... ▼]              │  │
│             │  │ (선택하지 않으면 최상위 지역)                        │  │
│             │  │                                                      │  │
│             │  │ ⚠️  순환 참조 방지: 현재 지역과 하위 지역은 선택 불가│  │
│             │  └──────────────────────────────────────────────────────┘  │
│             │                                                             │
│             │  ┌──────────────────────────────────────────────────────┐  │
│             │  │ 🌍 위치 정보                                         │  │
│             │  │                                                      │  │
│             │  │ Country Code *: [Select Country... ▼]               │  │
│             │  │ (ISO 3166-1 alpha-2: KR / US / JP ...)              │  │
│             │  │                                                      │  │
│             │  │ Representative Address (선택):                       │  │
│             │  │ Street: [___________________________]                │  │
│             │  │ City: [___________________________]                  │  │
│             │  │ Postal Code: [___________]                           │  │
│             │  └──────────────────────────────────────────────────────┘  │
│             │                                                             │
│             │  ┌──────────────────────────────────────────────────────┐  │
│             │  │ 📝 추가 메타데이터 (선택)                           │  │
│             │  │                                                      │  │
│             │  │ Sales Region: [___________________________]          │  │
│             │  │                                                      │  │
│             │  │ Priority Rollout: [☐] Enable                         │  │
│             │  │                                                      │  │
│             │  │ Custom Fields (JSON):                                │  │
│             │  │ ┌─────────────────────────────────────────────────┐│  │
│             │  │ │ {                                               ││  │
│             │  │ │   "customKey": "customValue"                    ││  │
│             │  │ │ }                                               ││  │
│             │  │ └─────────────────────────────────────────────────┘│  │
│             │  └──────────────────────────────────────────────────────┘  │
│             │                                                             │
│             │  ┌──────────────────────────────────────────────────────┐  │
│             │  │ 🏢 소속 스토어 (편집 시에만 표시)                   │  │
│             │  │                                                      │  │
│             │  │ Current Stores (8):                                  │  │
│             │  │ • store-1001 | 강남 쇼룸 | 3 devices  [View]        │  │
│             │  │ • store-1002 | 홍대 매장 | 5 devices  [View]        │  │
│             │  │ • store-1003 | 잠실 롯데점 | 4 devices  [View]      │  │
│             │  │                                                      │  │
│             │  │ [Show All Stores]                                    │  │
│             │  └──────────────────────────────────────────────────────┘  │
│             │                                                             │
│             │  ┌──────────────────────────────────────────────────────┐  │
│             │  │ 🌳 하위 지역 (편집 시에만 표시)                     │  │
│             │  │                                                      │  │
│             │  │ Child Areas (0):                                     │  │
│             │  │ 📭 No child areas                                    │  │
│             │  └──────────────────────────────────────────────────────┘  │
│             │                                                             │
│             │  ┌──────────────────────────────────────────────────────┐  │
│             │  │ ℹ️  메타데이터 (편집 시에만 표시)                    │  │
│             │  │                                                      │  │
│             │  │ Created: 2025-10-01 09:00 by admin                   │  │
│             │  │ Updated: 2026-01-15 15:30 by admin                   │  │
│             │  └──────────────────────────────────────────────────────┘  │
│             │                                                             │
│             │  [Cancel]  [Save LocalArea]                                │
└─────────────┴─────────────────────────────────────────────────────────────┘
```

## 주요 구성 요소

### 1. 공통 사이드바
- Dashboard, Product, Package, Content, Devices, Stores, LocalAreas(활성화), Reports, Settings 메뉴
- 현재 페이지(LocalAreas) 강조 표시

### 2. 헤더
- 페이지 제목: "🌏 LocalArea Editor"
- 부제: 
  - 신규: "Create New LocalArea"
  - 편집: "Edit: {지역명}"
- 액션 버튼:
  - [Cancel]: 변경사항 취소하고 이전 페이지로 복귀 (확인 모달)
  - [Save]: 지역 저장

### 3. 기본 정보 섹션 (*필수 항목 표시)

#### LocalArea ID
- **신규 등록**: 
  - [Generate ID] 버튼: "localarea-{랜덤문자열}" 자동 생성
  - 수동 입력 옵션: 사용자가 직접 입력 (중복 검사)
  - 형식: 영문 소문자, 숫자, 하이픈만 허용
- **편집 모드**: 읽기 전용 (회색 배경, 수정 불가)

#### Area Name *필수
- 입력 필드: 텍스트 (최대 100자)
- 검증: 빈 값 불가
- 예시: "Seoul", "Korea", "APAC"

#### Description
- 텍스트 영역: 여러 줄 입력 가능 (최대 500자)
- 선택 사항
- 플레이스홀더: "지역에 대한 상세 설명을 입력하세요..."

### 4. 위치 정보 섹션

#### Country Code *필수
- 드롭다운: ISO 3166-1 alpha-2 국가 코드 목록
- 검증: 반드시 선택해야 함
- 예시: KR (South Korea), US (United States), JP (Japan)

#### Representative Address (선택)
- **Street**: 도로명 주소 (최대 200자)
- **City**: 도시명 (최대 100자)
- **Postal Code**: 우편번호 (최대 20자)
- 모두 선택 사항

### 5. 소속 스토어 섹션 (편집 시에만 표시)
- 현재 지역에 속한 스토어 목록 (최대 3개만 표시)
- 각 스토어 정보:
  - Store ID | Store Name
  - 디바이스 개수
  - [View]: Store Detail로 이동
- [Show All Stores] 버튼:
  - Store List로 이동 (해당 지역 필터링)

### 6. 하위 지역 섹션 (편집 시에만 표시)
- 현재 지역의 하위 지역 목록
- 각 하위 지역 정보:
  - LocalArea ID | Name
  - 스토어 개수
  - [View]: LocalArea Detail로 이동

### 7. 메타데이터 섹션 (편집 시에만 표시)
- Created: 생성일시 및 생성자
- Updated: 최종 수정일시 및 수정자
- 읽기 전용 정보

### 8. 하단 액션 버튼
- **[Cancel]**: 
  - 변경사항이 있으면 확인 모달 표시
  - "변경사항을 저장하지 않고 나가시겠습니까?"
  - 확인 → 이전 페이지로 복귀
- **[Save LocalArea]**:
  - 필수 항목 검증
  - 순환 참조 검증
  - 저장 성공 → LocalArea Detail 페이지로 이동
  - 저장 실패 → 에러 메시지 표시

## 주요 상호작용 플로우

### 1. 신규 지역 등록
1. LocalArea List에서 [+ Register LocalArea] 클릭
2. LocalArea Editor 오픈 (빈 폼)
3. [Generate ID] 클릭하여 LocalArea ID 자동 생성
4. Area Name 입력 (필수)
5. Country Code 선택 (필수)
6. 주소 정보 입력 (선택)
7. [Save LocalArea] 클릭
8. 검증 통과 → 저장 → LocalArea Detail 페이지로 이동

### 2. 기존 지역 편집
1. LocalArea List 또는 LocalArea Detail에서 [Edit] 클릭
2. LocalArea Editor 오픈 (기존 정보 로드)
3. LocalArea ID는 읽기 전용 상태
4. Name, Description, Country 수정 가능
5. [Save LocalArea] 클릭
6. 검증 통과 → 저장 → LocalArea Detail 페이지로 이동

### 5. 취소 및 복귀
1. [Cancel] 버튼 클릭
2. 변경사항이 있으면 확인 모달
3. 확인 → 이전 페이지로 복귀

## 데이터 소스
- LocalArea 엔티티: localAreaId, name, countryCode, address, description
- LocalArea 엔티티 (재귀): 하위 지역 목록
- Store 엔티티: 소속 스토어 목록

## 컴포넌트 및 검증

### 필수 항목 검증
- LocalArea ID: 중복 검사, 형식 검증
- Area Name: 빈 값 불가
- Country Code: 반드시 선택

### 실시간 검증
- LocalArea ID 중복 검사: 입력 후 즉시 확인
- JSON 형식 검증: 입력 중 구문 하이라이팅

### 에러 메시지
- 필수 항목 누락: "This field is required"
- 중복 ID: "LocalArea ID already exists"
- 순환 참조: "Cannot select current area or child areas as parent"
- JSON 형식 오류: "Invalid JSON format"

## 에러 및 엣지 케이스 처리

### 저장 실패
- 네트워크 오류:
  ```
  ⚠️ Failed to save local area
  Network error occurred. Please try again.
  [Retry]
  ```

### 중복 ID
- LocalArea ID가 이미 존재:
  ```
  ⚠️ LocalArea ID already exists
  Please choose a different ID or use [Generate ID].
  ```

### 순환 참조
- Parent Area에 자기 자신 또는 하위 지역 선택:
  ```
  ⚠️ Circular reference detected
  Cannot select current area or child areas as parent.
  ```

### 필수 항목 누락
- 필수 항목이 비어있음:
  ```
  ⚠️ Required fields missing
  Please fill in all required fields (marked with *).
  ```

## UX 노트
- LocalArea ID는 자동 생성 옵션을 제공하여 편의성 향상
- 계층 구조를 명확히 표시하고 순환 참조를 방지
- Timezone은 Country 선택 시 해당 국가의 시간대만 표시
- 메타데이터는 JSON 에디터로 유연하게 추가 가능
- 실시간 검증으로 에러를 조기에 발견

## 접근성
- 키보드 내비게이션 지원: Tab, Enter로 모든 필드 접근 가능
- 필수 항목에 * 표시 및 aria-required 속성
- 에러 메시지는 명확하고 구체적으로 표시
- JSON 에디터는 접근성 지원 (스크린리더 호환)

## 다음 단계
- 계층 구조 시각화 (트리 뷰)
- 지역 템플릿 기능 (기존 지역 구조 복제)
- 지역별 배포 정책 설정

---

문서 작성자: CMS 팀  
작성일: 2026-02-14
