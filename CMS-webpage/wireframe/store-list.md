# Store List UI 와이어프레임

## 개요
- 목적: 등록된 모든 스토어(지점)를 목록으로 보여주고, 필터링·검색·대량 작업·상세 조회·등록을 수행합니다.
- 접근 경로: 좌측 사이드바 "Stores" 클릭

## 레이아웃
```
+------------------+--------------------------------------------------+
| Sidebar          | Header: Store Management                         |
| - Dashboard      +--------------------------------------------------+
| - Product        | Search/Filter Panel:                              |
| - Package        | [Search: _______________] [LocalArea: All ▼]      |
| - Content        | [Country: All ▼] [Status: All ▼]                  |
| - Devices        +--------------------------------------------------+
| - Stores         | Actions: [+ Register Store]                       |
| - LocalAreas     | Bulk Actions: [☐ Select All] [Delete] [Export]   |
| - Reports        +--------------------------------------------------+
| - Settings       | Store List Table:                                 |
|                  | ☐ | Store ID | Name | LocalArea | Address | Devices | Manager | Actions |
|                  | ☐ | store-1001 | 강남 쇼룸 | Seoul | 서울시 강남구... | 3 | 홍길동 | [View][Edit][Delete] |
|                  | ☐ | store-1002 | 홍대 매장 | Seoul | 서울시 마포구... | 5 | 김철수 | [View][Edit][Delete] |
|                  | ☐ | store-2001 | 부산 본점 | Busan | 부산시 해운대구... | 2 | 이영희 | [View][Edit][Delete] |
|                  +--------------------------------------------------+
|                  | Pagination: [< Prev] Page 1 of 3 [Next >]        |
+------------------+--------------------------------------------------+
```

## 주요 구성 요소

### 1. 공통 사이드바
- Dashboard, Product, Package, Content, Devices, Stores, LocalAreas, Reports, Settings 메뉴 항목
- 현재 페이지(Stores) 강조 표시

### 2. 헤더
- 페이지 제목: "Store Management"
- 부제: "Manage store locations and assignments"

### 3. 검색/필터 패널
- **검색창**: 스토어 이름, ID, 주소, 담당자로 검색
- **LocalArea 필터**: 특정 지역의 스토어만 필터링 (All/Seoul/Busan 등)
- **Country 필터**: 국가별 필터링 (All/KR/US/JP 등)
- **Status 필터**: Active/Inactive 상태로 필터링

### 4. 액션 바
- **[+ Register Store]**: 새 스토어 등록 페이지로 이동
- **Bulk Actions**: 
  - [☐ Select All]: 모든 스토어 선택
  - [Delete]: 선택된 스토어들 삭제 (확인 필요)
  - [Export]: 선택된 스토어 정보 CSV/Excel 내보내기

### 5. 스토어 목록 테이블
각 행은 다음 컬럼으로 구성:
- **체크박스**: 대량 작업 선택용
- **Store ID**: 고유 식별자 (예: store-1001)
- **Name**: 스토어 이름 (예: 강남 쇼룸)
- **LocalArea**: 소속 지역명 (localAreaId 참조)
- **Address**: 주소 요약 (예: 서울시 강남구 테헤란로 1)
- **Devices**: 해당 스토어의 디바이스 개수 (클릭 시 디바이스 리스트 필터링)
- **Manager**: 담당자 이름 (meta.manager)
- **Actions**: 
  - [View]: 스토어 상세 페이지로 이동
  - [Edit]: 스토어 정보 편집 페이지로 이동
  - [Delete]: 스토어 삭제 확인 후 삭제

### 6. 페이지네이션
- 이전/다음 버튼
- 현재 페이지 번호 표시
- 페이지당 20개 항목 표시

## 비즈니스 로직
1. **검색**: 스토어 이름, ID, 주소, 담당자를 포함하는 항목 필터링
2. **LocalArea 필터**: 특정 지역의 스토어만 표시
3. **Country 필터**: 특정 국가의 스토어만 표시
4. **대량 작업**: 
   - 삭제는 확인 다이얼로그 표시 후 실행 (디바이스 연결 확인 필요)
   - Export는 CSV/Excel 형식으로 다운로드
5. **View**: 스토어 상세 페이지로 이동 (스토어 정보, 디바이스 목록 등)
6. **Edit**: 스토어 정보 편집 폼으로 이동
7. **Delete**: 연결된 디바이스가 있으면 경고 후 삭제

## 주요 상호작용 플로우

### 1. 스토어 검색 및 필터링
1. 검색어 입력 또는 필터 조건 선택
2. 리스트가 조건에 맞게 갱신됨
3. URL 쿼리 파라미터 업데이트 (북마크/공유 가능)

### 2. 신규 스토어 등록
1. [+ Register Store] 버튼 클릭
2. 스토어 등록 폼으로 이동
3. 스토어 정보 입력 및 저장
4. 리스트로 복귀 (새 항목 추가됨)

### 3. 스토어 편집
1. 특정 스토어의 [Edit] 버튼 클릭
2. 스토어 편집 폼으로 이동
3. 수정 후 저장
4. 리스트로 복귀 (변경사항 반영)

### 4. 스토어 삭제
1. 특정 스토어의 [Delete] 버튼 클릭
2. 확인 모달: "정말 삭제하시겠습니까? (연결된 디바이스: N개)"
3. 확인 → 삭제 수행
4. 성공 토스트 및 리스트 갱신

### 5. 일괄 작업 (Bulk Actions)
1. 여러 스토어 체크박스 선택 (또는 Select All)
2. Bulk Actions 드롭다운에서 작업 선택
3. 확인 모달 표시
4. 확인 후 작업 실행
5. 성공/실패 토스트 메시지 표시
6. 리스트 자동 갱신

## 데이터 소스
- Store 엔티티: storeId, name, address, localAreaId, meta
- LocalArea 엔티티 참조: 지역명 표시를 위해 localAreaId로 조회
- Device 엔티티: 스토어별 디바이스 개수 집계

## 컴포넌트 및 검증

### 필터 패널
- 필터 조건은 URL 쿼리 파라미터로 관리 (북마크/공유 지원)
- 초기화 버튼 제공: 모든 필터를 기본값으로 리셋

### 체크박스 및 일괄 작업
- Select All 체크박스: 현재 페이지의 모든 항목 선택/해제
- 개별 체크박스: 각 항목 선택
- 선택된 항목 개수 표시 (예: "3 items selected")
- Bulk Actions는 최소 1개 이상 선택되어야 활성화

### 주소 표시
- 긴 주소는 말줄임표(...) 처리
- 마우스 오버 시 전체 주소 툴팁 표시

## 에러 및 엣지 케이스 처리

### 스토어 없음
- 필터 조건에 맞는 스토어가 없을 경우:
  ```
  📭 No stores found
  Try adjusting your filters or [Register New Store]
  ```

### 삭제 시 의존성 경고
- 스토어에 디바이스가 연결되어 있을 경우:
  ```
  ⚠️ Warning: This store has 5 connected devices.
  Deleting it will unassign these devices.
  [View Devices] [Cancel] [Delete Anyway]
  ```

### 일괄 작업 실패
- 일부 항목 실패 시:
  ```
  ✓ 8 items processed successfully
  ✗ 2 items failed (devices still connected)
  [View Details]
  ```

## UX 노트
- 스토어 리스트는 물리적 위치 관리의 중심 화면입니다
- LocalArea와의 연계를 명확히 표시하여 계층 구조를 이해할 수 있어야 합니다
- 디바이스 개수를 클릭하면 해당 스토어의 디바이스 리스트로 필터링된 페이지로 이동합니다
- 주소 정보는 간결하게 표시하고 상세는 View에서 확인할 수 있도록 합니다

## 접근성
- 키보드 내비게이션 지원: Tab, Enter, Space로 모든 기능 접근 가능
- 스크린리더 지원: 각 컬럼, 버튼에 적절한 레이블 제공

## 다음 단계
- 스토어 상세 보기 화면 (store-detail)
- 스토어 등록/편집 화면 (store-editor)
- 스토어별 디바이스 할당 관리 기능
- 지도 뷰: 스토어 위치를 지도에 표시

---

문서 작성자: CMS 팀  
작성일: 2026-02-13
