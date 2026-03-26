# Device List UI 와이어프레임

## 개요
- 목적: 등록된 모든 디바이스를 목록으로 보여주고, 필터링·검색·대량 작업·상세 조회·등록을 수행합니다.
- 접근 경로: 좌측 사이드바 "Devices" 클릭

## 레이아웃
```
+------------------+--------------------------------------------------+
| Sidebar          | Header: Device Management                        |
| - Dashboard      +--------------------------------------------------+
| - Content        | Search/Filter Panel:                              |
| - Package        | [Search: _______________] [Product: All ▼]        |
| - Product        | [Store: All ▼] [Status: All ▼]                    |
| - Devices        +--------------------------------------------------+
|                  | Actions: [+ Register Device]                      |
|                  | Bulk Actions: [☐ Select All] [Delete] [Update]   |
|                  +--------------------------------------------------+
|                  | Device List Table:                                |
|                  | ☐ | Device ID | Name | Product | Store | Package | Last Seen | Actions |
|                  | ☐ | dev-001 | sand-pc-01 | SandCraft | Store A | pkg-sand-11 | 2 mins ago | [View][Edit][Delete] |
|                  | ☐ | dev-002 | sand-pc-02 | SandCraft | Store A | pkg-sand-11 | 1 hour ago | [View][Edit][Delete] |
|                  | ☐ | dev-010 | fish-pc-01 | FishWorld | Store B | pkg-fish-basic | 3 days ago | [View][Edit][Delete] |
|                  +--------------------------------------------------+
|                  | Pagination: [< Prev] Page 1 of 5 [Next >]        |
+------------------+--------------------------------------------------+
```

## 주요 구성 요소

### 1. 공통 사이드바
- Dashboard, Content, Package, Product, Devices 메뉴 항목
- 현재 페이지(Devices) 강조 표시

### 2. 헤더
- 페이지 제목: "Device Management"
- 부제: "Monitor and manage installed devices"

### 3. 검색/필터 패널
- **검색창**: 디바이스 이름, ID, MAC 주소로 검색
- **Product 필터**: 특정 제품의 디바이스만 필터링 (All/SandCraft/FishWorld 등)
- **Store 필터**: 특정 매장의 디바이스만 필터링 (All/Store A/Store B 등)

### 4. 액션 바
- **[+ Register Device]**: 새 디바이스 등록 페이지로 이동
- **Bulk Actions**: 
  - [☐ Select All]: 모든 디바이스 선택
  - [Delete]: 선택된 디바이스들 삭제
  - [Update Package]: 선택된 디바이스들의 패키지 업데이트

### 5. 디바이스 목록 테이블
각 행은 다음 컬럼으로 구성:
- **체크박스**: 대량 작업 선택용
- **Device ID**: 고유 식별자 (예: dev-001)
- **Name**: 디바이스 이름 (예: sand-pc-01)
- **Product**: 설치된 제품명 (productId 참조)
- **Store**: 소속 매장명 (storeId 참조, 없으면 "-")
- **Package**: 설치된 패키지 이름 (installedPackageId 참조, 없으면 "None")
- **Last Seen**: 마지막 통신 시각 (상대 시간 표시: "2 mins ago", "3 days ago")
- **Actions**: 
  - [View]: 디바이스 상세 페이지로 이동 (device-detail)
  - [Edit]: 디바이스 정보 편집 페이지로 이동
  - [Delete]: 디바이스 등록 해제 확인 후 삭제

### 6. 페이지네이션
- 이전/다음 버튼
- 현재 페이지 번호 표시
- 페이지당 20개 항목 표시

## 비즈니스 로직
1. **검색**: 디바이스 이름, ID, MAC 주소를 포함하는 항목 필터링
2. **Product 필터**: 특정 제품의 디바이스만 표시
3. **Store 필터**: 특정 매장의 디바이스만 표시
4. **대량 작업**: 
   - 삭제는 확인 다이얼로그 표시 후 실행
   - Update Package는 패키지 선택 모달 표시 후 업데이트
5. **View**: device-detail 페이지로 이동하여 디바이스 상세 정보 표시
6. **Edit**: 디바이스 정보 편집 폼으로 이동 (이름, 설명, 매장 등)
7. **Delete**: 확인 후 디바이스 등록 해제

## 데이터 소스
- Device 엔티티: deviceId, name, description, productId, storeId, mac, installedPackageId, lastSeen, meta
- Product 엔티티 참조: 제품명 표시를 위해 productId로 조회
- Store 엔티티 참조: 매장명 표시를 위해 storeId로 조회
- Package 엔티티 참조: 패키지명 표시를 위해 installedPackageId로 조회

## 추가 고려사항
- lastSeen 타임스탬프는 상대 시간으로 표시 ("2 mins ago", "1 hour ago", "3 days ago")
- MAC 주소는 검색 가능하되 목록에는 표시하지 않음 (보안 고려)
- 디바이스 정보는 주기적으로 갱신 (auto-refresh 옵션 제공)
