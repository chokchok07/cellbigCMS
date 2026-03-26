# Store Editor UI 와이어프레임

## 개요
- 목적: 신규 스토어를 등록하거나 기존 스토어 정보를 편집합니다.
- 접근 경로: 
  - 신규: Store List에서 [+ Register Store] 버튼 클릭
  - 편집: Store List 또는 Store Detail에서 [Edit] 버튼 클릭

## 레이아웃
```
┌───────────────────────────────────────────────────────────────────────────┐
│ [Product ▼]  🔍 Search...          🔔 (3)  👤 Admin                      │
├─────────────┬─────────────────────────────────────────────────────────────┤
│             │                                                             │
│ 📊 Dashboard│  🏪 Store Editor                      [Cancel] [Save]      │
│ 🏢 Product  │  Create New Store / Edit: 강남 쇼룸                        │
│ 📦 Package  │                                                             │
│ 📄 Content  │  ┌──────────────────────────────────────────────────────┐  │
│ 💻 Devices  │  │ 📋 기본 정보 *필수                                   │  │
│ 🏪 Stores   │  │                                                      │  │
│ 🌏 LocalAreas  │ Store ID: [___________________] [Generate ID]        │  │
│ 📈 Reports  │  │ (편집 시 읽기전용)                                   │  │
│ ⚙️  Settings│  │                                                      │  │
│             │  │ Store Name *: [___________________________]          │  │
│             │  │                                                      │  │
│             │  │ LocalArea *: [Select LocalArea... ▼]                │  │
│             │  │ (Seoul / Busan / Incheon ...)                        │  │
│             │  └──────────────────────────────────────────────────────┘  │
│             │                                                             │
│             │  ┌──────────────────────────────────────────────────────┐  │
│             │  │ 📍 주소 정보 *필수                                   │  │
│             │  │                                                      │  │
│             │  │ Street Address *: [___________________________]      │  │
│             │  │                                                      │  │
│             │  │ City *: [___________________________]                │  │
│             │  │                                                      │  │
│             │  │ Postal Code: [___________]                           │  │
│             │  │                                                      │  │
│             │  │ Country *: [Select Country... ▼]                     │  │
│             │  │ (KR / US / JP ...)                                   │  │
│             │  └──────────────────────────────────────────────────────┘  │
│             │                                                             │
│             │  ┌──────────────────────────────────────────────────────┐  │
│             │  │ 👤 담당자 정보 (선택)                                │  │
│             │  │                                                      │  │
│             │  │ Manager Name: [___________________________]          │  │
│             │  │                                                      │  │
│             │  │ Phone: [___________________________]                 │  │
│             │  │ Format: 010-1234-5678                                │  │
│             │  │                                                      │  │
│             │  │ Email: [___________________________]                 │  │
│             │  │                                                      │  │
│             │  │ SLA Level: [___________________________]             │  │
│             │  │ (예: 24h support, Business hours only)               │  │
│             │  └──────────────────────────────────────────────────────┘  │
│             │                                                             │
│             │  ┌──────────────────────────────────────────────────────┐  │
│             │  │ 💻 디바이스 할당 (편집 시에만 표시)                 │  │
│             │  │                                                      │  │
│             │  │ Assigned Devices:                                    │  │
│             │  │ • dev-001 | sand-pc-01 | 🟢 Online    [Remove]      │  │
│             │  │ • dev-002 | sand-pc-02 | 🟢 Online    [Remove]      │  │
│             │  │ • dev-010 | sand-pc-03 | 🔴 Offline   [Remove]      │  │
│             │  │                                                      │  │
│             │  │ [+ Assign Device]                                    │  │
│             │  └──────────────────────────────────────────────────────┘  │
│             │                                                             │
│             │  ┌──────────────────────────────────────────────────────┐  │
│             │  │ ℹ️  메타데이터 (편집 시에만 표시)                    │  │
│             │  │                                                      │  │
│             │  │ Created: 2024-01-15 10:30 by admin                   │  │
│             │  │ Updated: 2026-01-15 10:30 by admin                   │  │
│             │  └──────────────────────────────────────────────────────┘  │
│             │                                                             │
│             │  [Cancel]  [Save Store]                                    │
└─────────────┴─────────────────────────────────────────────────────────────┘
```

## 주요 구성 요소

### 1. 공통 사이드바
- Dashboard, Product, Package, Content, Devices, Stores(활성화), LocalAreas, Reports, Settings 메뉴
- 현재 페이지(Stores) 강조 표시

### 2. 헤더
- 페이지 제목: "🏪 Store Editor"
- 부제: 
  - 신규: "Create New Store"
  - 편집: "Edit: {스토어명}"
- 액션 버튼:
  - [Cancel]: 변경사항 취소하고 이전 페이지로 복귀 (확인 모달)
  - [Save]: 스토어 저장

### 3. 기본 정보 섹션 (*필수 항목 표시)

#### Store ID
- **신규 등록**: 
  - [Generate ID] 버튼: "store-{랜덤숫자}" 자동 생성
  - 수동 입력 옵션: 사용자가 직접 입력 (중복 검사)
  - 형식: 영문 소문자, 숫자, 하이픈만 허용
- **편집 모드**: 읽기 전용 (회색 배경, 수정 불가)

#### Store Name *필수
- 입력 필드: 텍스트 (최대 100자)
- 검증: 빈 값 불가
- 예시: "강남 쇼룸", "홍대 매장", "부산 본점"

#### LocalArea *필수
- 드롭다운: 등록된 지역 목록에서 선택
- 계층 구조 표시 (예: "Korea > Seoul")
- 검증: 반드시 선택해야 함

### 4. 주소 정보 섹션 (*필수 항목 표시)

#### Street Address *필수
- 입력 필드: 텍스트 (최대 200자)
- 검증: 빈 값 불가
- 예시: "서울시 강남구 테헤란로 1"

#### City *필수
- 입력 필드: 텍스트 (최대 100자)
- 검증: 빈 값 불가
- 예시: "Seoul", "Busan"

#### Postal Code (선택)
- 입력 필드: 텍스트 (최대 20자)
- 형식: 숫자 및 하이픈 (국가별 형식 다름)
- 예시: "06236", "12345-6789"

#### Country *필수
- 드롭다운: ISO 3166-1 alpha-2 국가 코드 목록
- 검증: 반드시 선택해야 함
- 예시: KR (South Korea), US (United States), JP (Japan)

### 5. 담당자 정보 섹션 (선택 사항)

#### Manager Name
- 입력 필드: 텍스트 (최대 100자)
- 선택 사항
- 예시: "홍길동", "김철수"

#### Phone
- 입력 필드: 텍스트 (최대 20자)
- 형식 안내: "010-1234-5678"
- 검증: 전화번호 형식 (국가별 다름)

#### Email
- 입력 필드: 이메일 (최대 100자)
- 검증: 이메일 형식
- 예시: "hong@example.com"

#### SLA Level
- 입력 필드: 텍스트 (최대 100자)
- 선택 사항
- 예시: "24h support", "Business hours only"

### 6. 디바이스 할당 섹션 (편집 시에만 표시)
- 현재 스토어에 할당된 디바이스 목록
- 각 디바이스 정보:
  - Device ID | Device Name
  - 상태: 🟢 Online / 🔴 Offline
  - [Remove] 버튼: 디바이스 할당 해제
- [+ Assign Device] 버튼: 새 디바이스 할당 (모달)

### 7. 메타데이터 섹션 (편집 시에만 표시)
- Created: 생성일시 및 생성자
- Updated: 최종 수정일시 및 수정자
- 읽기 전용 정보

### 8. 하단 액션 버튼
- **[Cancel]**: 
  - 변경사항이 있으면 확인 모달 표시
  - "변경사항을 저장하지 않고 나가시겠습니까?"
  - 확인 → 이전 페이지로 복귀
- **[Save Store]**:
  - 필수 항목 검증
  - 저장 성공 → Store Detail 페이지로 이동
  - 저장 실패 → 에러 메시지 표시

## 주요 상호작용 플로우

### 1. 신규 스토어 등록
1. Store List에서 [+ Register Store] 클릭
2. Store Editor 오픈 (빈 폼)
3. [Generate ID] 클릭하여 Store ID 자동 생성
4. Store Name 입력 (필수)
5. LocalArea 선택 (필수)
6. 주소 정보 입력 (Street, City, Country 필수)
7. 담당자 정보 입력 (선택)
8. [Save Store] 클릭
9. 검증 통과 → 저장 → Store Detail 페이지로 이동

### 2. 기존 스토어 편집
1. Store List 또는 Store Detail에서 [Edit] 클릭
2. Store Editor 오픈 (기존 정보 로드)
3. Store ID는 읽기 전용 상태
4. Name, LocalArea, Address, Manager 정보 수정 가능
5. 디바이스 할당 섹션에서 디바이스 추가/제거
6. [Save Store] 클릭
7. 검증 통과 → 저장 → Store Detail 페이지로 이동

### 3. 디바이스 할당 (편집 시)
1. [+ Assign Device] 버튼 클릭
2. 디바이스 선택 모달 표시
3. 스토어에 할당되지 않은 디바이스 목록
4. 디바이스 선택 후 [Assign] 클릭
5. 할당된 디바이스 목록에 추가

### 4. 디바이스 제거 (편집 시)
1. 특정 디바이스의 [Remove] 클릭
2. 확인 모달: "이 디바이스를 스토어에서 제거하시겠습니까?"
3. 확인 → 할당 해제

### 5. 취소 및 복귀
1. [Cancel] 버튼 클릭
2. 변경사항이 있으면 확인 모달
3. 확인 → 이전 페이지로 복귀

## 데이터 소스
- Store 엔티티: storeId, name, address, localAreaId, meta
- LocalArea 엔티티: 드롭다운 목록 제공
- Device 엔티티: 디바이스 할당/제거

## 컴포넌트 및 검증

### 필수 항목 검증
- Store ID: 중복 검사, 형식 검증
- Store Name: 빈 값 불가
- LocalArea: 반드시 선택
- Address (Street, City, Country): 빈 값 불가

### 선택 항목
- Postal Code: 형식 검증 (선택)
- Manager 정보: 모두 선택 사항

### 실시간 검증
- Store ID 중복 검사: 입력 후 즉시 확인
- Email 형식 검증: 이메일 형식 확인
- Phone 형식 검증: 전화번호 형식 확인

### 에러 메시지
- 필수 항목 누락: "This field is required"
- 중복 ID: "Store ID already exists"
- 이메일 형식 오류: "Please enter a valid email address"

## 에러 및 엣지 케이스 처리

### 저장 실패
- 네트워크 오류:
  ```
  ⚠️ Failed to save store
  Network error occurred. Please try again.
  [Retry]
  ```

### 중복 ID
- Store ID가 이미 존재:
  ```
  ⚠️ Store ID already exists
  Please choose a different ID or use [Generate ID].
  ```

### 필수 항목 누락
- 필수 항목이 비어있음:
  ```
  ⚠️ Required fields missing
  Please fill in all required fields (marked with *).
  ```

## UX 노트
- Store ID는 자동 생성 옵션을 제공하여 사용자 편의성 향상
- LocalArea는 계층 구조로 표시하여 관계를 명확히 이해
- 주소 정보는 구조화하여 입력받아 데이터 일관성 유지
- 담당자 정보는 선택 사항으로 하여 유연성 제공
- 실시간 검증으로 에러를 조기에 발견

## 접근성
- 키보드 내비게이션 지원: Tab, Enter로 모든 필드 접근 가능
- 필수 항목에 * 표시 및 aria-required 속성
- 에러 메시지는 명확하고 구체적으로 표시
- 폼 레이블과 입력 필드 명확히 연결

## 다음 단계
- 주소 자동 완성 API 연동
- 지도에서 위치 선택 기능
- 스토어 템플릿 기능 (기존 스토어 복제)

---

문서 작성자: CMS 팀  
작성일: 2026-02-14
