# LocalArea List UI 와이어프레임

## 개요
- 목적: 등록된 모든 지역(LocalArea)을 목록으로 보여주고, 필터링·검색·대량 작업·상세 조회·등록을 수행합니다.
- 접근 경로: 좌측 사이드바 "LocalAreas" 클릭

## 레이아웃
```
+------------------+--------------------------------------------------+
| Sidebar          | Header: LocalArea Management                     |
| - Dashboard      +--------------------------------------------------+
| - Product        | Search/Filter Panel:                              |
| - Package        | [Search: _______________] [Country: All ▼]        |
| - Content        | [Search by area name, ID...]                      |
| - Devices        +--------------------------------------------------+
| - Stores         | Actions: [+ Register LocalArea]                   |
| - LocalAreas     | Bulk Actions: [☐ Select All] [Delete] [Export]   |
| - Reports        +--------------------------------------------------+
| - Settings       | LocalArea List Table:                             |
|                  | ☐ | LocalArea ID | Name | Country | Stores | Actions |
|                  | ☐ | localarea-kr | Korea | KR | 15 | [View][Edit][Delete] |
|                  | ☐ | localarea-seoul | Seoul | KR | 8 | [View][Edit][Delete] |
|                  | ☐ | localarea-busan | Busan | KR | 5 | [View][Edit][Delete] |
|                  | ☐ | localarea-incheon | Incheon | KR | 2 | [View][Edit][Delete] |
|                  +--------------------------------------------------+
|                  | Pagination: [< Prev] Page 1 of 2 [Next >]        |
+------------------+--------------------------------------------------+
```

## 주요 구성 요소

### 1. 공통 사이드바
- Dashboard, Product, Package, Content, Devices, Stores, LocalAreas, Reports, Settings 메뉴 항목
- 현재 페이지(LocalAreas) 강조 표시

### 2. 헤더
- 페이지 제목: "LocalArea Management"
- 부제: "Manage geographical areas and hierarchies"

### 3. 검색/필터 패널
- **검색창**: 지역 이름, ID로 검색
- **Country 필터**: 국가별 필터링 (All/KR/US/JP 등)

### 4. 액션 바
- **[+ Register LocalArea]**: 새 지역 등록 페이지로 이동
- **Bulk Actions**: 
  - [☐ Select All]: 모든 지역 선택
  - [Delete]: 선택된 지역들 삭제 (확인 필요)
  - [Export]: 선택된 지역 정보 CSV/Excel 내보내기

### 5. 지역 목록 테이블
각 행은 다음 컬럼으로 구성:
- **체크박스**: 대량 작업 선택용
- **LocalArea ID**: 고유 식별자 (예: localarea-seoul)
- **Name**: 지역 이름 (예: Seoul)
- **Country**: 국가 코드 (countryCode, 예: KR)
- **Stores**: 해당 지역의 스토어 개수 (클릭 시 스토어 리스트 필터링)
- **Actions**: 
  - [View]: 지역 상세 페이지로 이동
  - [Edit]: 지역 정보 편집 페이지로 이동
  - [Delete]: 지역 삭제 확인 후 삭제

### 6. 페이지네이션
- 이전/다음 버튼
- 현재 페이지 번호 표시
- 페이지당 20개 항목 표시

## 비즈니스 로직
1. **검색**: 지역 이름, ID를 포함하는 항목 필터링
2. **Country 필터**: 특정 국가의 지역만 표시
3. **대량 작업**: 
   - 삭제는 확인 다이얼로그 표시 후 실행 (스토어 연결 확인 필요)
   - Export는 CSV/Excel 형식으로 다운로드
4. **View**: 지역 상세 페이지로 이동 (지역 정보, 스토어 목록 등)
5. **Edit**: 지역 정보 편집 폼으로 이동
6. **Delete**: 스토어가 있으면 경고 후 삭제

## 주요 상호작용 플로우

### 1. 지역 검색 및 필터링
1. 검색어 입력 또는 필터 조건 선택
2. 리스트가 조건에 맞게 갱신됨
3. URL 쿼리 파라미터 업데이트 (북마크/공유 가능)

### 1. 지역 검색 및 필터링
1. 검색어 입력 또는 필터 조건 선택
2. 리스트가 조건에 맞게 갱신됨
3. URL 쿼리 파라미터 업데이트 (북마크/공유 가능)
1. 특정 지역의 [Delete] 버튼 클릭
2. 확인 모달: "정말 삭제하시겠습니까? (하위 지역: N개, 스토어: M개)"
3. 확인 → 삭제 수행 (하위 항목 처리 전략 필요)
4. 성공 토스트 및 리스트 갱신

### 5. 일괄 작업 (Bulk Actions)
1. 여러 지역 체크박스 선택 (또는 Select All)
2. Bulk Actions 드롭다운에서 작업 선택
3. 확인 모달 표시
4. 확인 후 작업 실행
5. 성공/실패 토스트 메시지 표시
6. 리스트 자동 갱신

## 데이터 소스
- LocalArea 엔티티: localAreaId, name, description, countryCode, address
- Store 엔티티: 지역별 스토어 개수 집계

## 컴포넌트 및 검증

### 계층 구조 표시
- 지역별 들여쓰기 또는 트리 구조로 표시
- 드릴다운 기능: 특정 지역 선택 시 해당 지역으로 필터링

### 필터 패널
- 필터 조건은 URL 쿼리 파라미터로 관리 (북마크/공유 지원)
- 초기화 버튼 제공: 모든 필터를 기본값으로 리셋

### 체크박스 및 일괄 작업
- Select All 체크박스: 현재 페이지의 모든 항목 선택/해제
- 개별 체크박스: 각 항목 선택
- 선택된 항목 개수 표시 (예: "3 items selected")
- Bulk Actions는 최소 1개 이상 선택되어야 활성화

## 에러 및 엣지 케이스 처리

### 지역 없음
- 필터 조건에 맞는 지역이 없을 경우:
  ```
  📭 No local areas found
  Try adjusting your filters or [Register New LocalArea]
  ```

### 삭제 시 의존성 경고
- 지역에 스토어가 있을 경우:
  ```
  ⚠️ Warning: This local area has:
  - 8 stores
  
  Deleting it will also affect these items.
  [View Details] [Cancel] [Delete All]
  ```

### 순환 참조 방지
- 지역 등록/편집 시 유효성 검증

### 일괄 작업 실패
- 일부 항목 실패 시:
  ```
  ✓ 5 items processed successfully
  ✗ 2 items failed (child areas or stores exist)
  [View Details]
  ```

## UX 노트
- LocalArea는 Store의 상위 개념으로 지리적/조직적 계층 구조를 관리합니다
- 스토어 개수를 클릭하면 해당 지역의 스토어 리스트로 필터링된 페이지로 이동합니다
- 지역을 삭제하면 스토어에 영향을 미치므로 신중한 경고가 필요합니다

## 접근성
- 키보드 내비게이션 지원: Tab, Enter, Space로 모든 기능 접근 가능
- 스크린리더 지원: 각 컬럼, 버튼에 적절한 레이블 제공

## 다음 단계
- 지역 상세 보기 화면 (localarea-detail)
- 지역 등록/편집 화면 (localarea-editor)
- 지도 뷰: 지역을 지도에 표시

---

문서 작성자: CMS 팀  
작성일: 2026-02-13
