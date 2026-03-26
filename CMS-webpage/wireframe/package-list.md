# Package List UI 와이어프레임

## 개요
- 목적: 등록된 모든 패키지를 목록으로 보여주고, 필터링·검색·대량 작업·상세 조회·생성을 수행합니다.
- 접근 경로: 좌측 사이드바 "Package" 클릭

## 레이아웃
```
+------------------+--------------------------------------------------+
| Sidebar          | Header: Package Management                       |
| - Dashboard      +--------------------------------------------------+
| - Content        | Search/Filter Panel:                              |
| - Package        | [Search: _______________] [Product: All ▼]        |
| - Product        | [Published: All ▼]                                |
| - Devices        +--------------------------------------------------+
|                  | Actions: [+ New Package]                          |
|                  | Bulk Actions: [☐ Select All] [Delete] [Publish]  |
|                  +--------------------------------------------------+
|                  | Package List Table:                               |
|                  | ☐ | Package ID | Name | Product | Contents | Status | Actions |
|                  | ☐ | pkg-sand-11 | SandCraft - 11 Items | SandCraft | 11 | Published | [View][Edit][Delete] |
|                  | ☐ | pkg-sand-full | SandCraft - Full | SandCraft | 45 | Published | [View][Edit][Delete] |
|                  | ☐ | pkg-fish-basic | FishWorld - Basic | FishWorld | 5 | Draft | [View][Edit][Delete] |
|                  +--------------------------------------------------+
|                  | Pagination: [< Prev] Page 1 of 3 [Next >]        |
+------------------+--------------------------------------------------+
```

## 주요 구성 요소

### 1. 공통 사이드바
- Dashboard, Content, Package, Product, Devices 메뉴 항목
- 현재 페이지(Package) 강조 표시

### 2. 헤더
- 페이지 제목: "Package Management"
- 부제: "Manage content packages for products"

### 3. 검색/필터 패널
- **검색창**: 패키지 이름 또는 ID로 검색
- **Product 필터**: 특정 제품의 패키지만 필터링 (All/SandCraft/FishWorld 등)
- **Published 필터**: Published/Draft/All 상태로 필터링

### 4. 액션 바
- **[+ New Package]**: 새 패키지 생성 페이지로 이동
- **Bulk Actions**: 
  - [☐ Select All]: 모든 패키지 선택
  - [Delete]: 선택된 패키지들 삭제
  - [Publish]: 선택된 Draft 패키지들을 Published로 변경
  - [Unpublish]: 선택된 Published 패키지들을 Draft로 변경

### 5. 패키지 목록 테이블
각 행은 다음 컬럼으로 구성:
- **체크박스**: 대량 작업 선택용
- **Package ID**: 고유 식별자 (예: pkg-sand-11)
- **Name**: 패키지 이름 (예: SandCraft - 11 Items)
- **Product**: 소속 제품명 (productId 참조)
- **Contents**: 포함된 콘텐츠 수 (contents 배열 길이)
- **Status**: 
  - 🟢 Published: 게시된 패키지
  - 🟡 Draft: 작업 중인 패키지
- **Actions**: 
  - [View]: 패키지 상세 페이지로 이동 (package-detail)
  - [Edit]: 패키지 편집 페이지로 이동
  - [Delete]: 패키지 삭제 확인 후 삭제

### 6. 페이지네이션
- 이전/다음 버튼
- 현재 페이지 번호 표시
- 페이지당 20개 항목 표시

## 상태 표시 규칙
- **Published (🟢)**: 게시 완료된 패키지, 클라이언트에서 조회하여 사용 가능
- **Draft (🟡)**: 작업 중인 패키지, 게시 전 상태

## 비즈니스 로직
1. **검색**: 패키지 이름 또는 ID를 포함하는 항목 필터링
2. **Product 필터**: 특정 제품의 패키지만 표시
3. **Status 필터**: Published/Draft 상태로 필터링
4. **대량 작업**: 
   - 삭제는 확인 다이얼로그 표시 후 실행
   - Publish/Unpublish는 상태 변경 후 목록 갱신
5. **View**: package-detail 페이지로 이동하여 패키지 상세 정보 표시
6. **Edit**: 패키지 편집 폼으로 이동
7. **Delete**: 확인 후 패키지 삭제

## 데이터 소스
- Package 엔티티: packageId, productId, name, description, contents, published
- Product 엔티티 참조: 제품명 표시를 위해 productId로 조회

## 추가 고려사항
- 패키지 내 콘텐츠 수는 실시간 계산 또는 캐시
- Published 패키지는 클라이언트가 조회 가능한 콘텐츠 묶음으로 사용됨
