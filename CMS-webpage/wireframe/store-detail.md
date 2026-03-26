# Store Detail UI 와이어프레임

## 개요
- 목적: 개별 스토어의 상세 정보, 디바이스 목록, 위치 정보를 확인하고 관리합니다.
- 접근 경로: Store List에서 [View] 버튼 클릭

## ASCII Layout

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Store Detail: 강남 쇼룸 (ID: store-1001)                               │
│  🏢 Active  •  LocalArea: Seoul  •  3 Devices                          │
├────────────────────────────┬────────────────────────────────────────────┤
│                            │                                            │
│  📋 기본 정보              │  💻 연결된 디바이스 (3)                   │
│                            │                                            │
│  Store ID: store-1001      │  ┌──────────────────────────────────────┐ │
│  Name: 강남 쇼룸           │  │ dev-001 | sand-pc-01                 │ │
│  LocalArea: Seoul          │  │ 🟢 Online | Last seen: 2 mins ago   │ │
│                            │  │ Package: pkg-sand-11                 │ │
│  Address:                  │  │ [View Device]                        │ │
│  서울시 강남구 테헤란로 1  │  └──────────────────────────────────────┘ │
│  Postal Code: 06236        │                                            │
│  Country: KR               │  ┌──────────────────────────────────────┐ │
│                            │  │ dev-002 | sand-pc-02                 │ │
│  Manager: 홍길동           │  │ 🟢 Online | Last seen: 5 mins ago   │ │
│  Phone: 010-1234-5678      │  │ Package: pkg-sand-11                 │ │
│  Email: hong@example.com   │  │ [View Device]                        │ │
│                            │  └──────────────────────────────────────┘ │
│  SLA: 24h support          │                                            │
│                            │  ┌──────────────────────────────────────┐ │
│                            │  │ dev-010 | sand-pc-03                 │ │
│  [Edit Store]              │  │ 🔴 Offline | Last seen: 2 hours ago │ │
│  [Delete Store]            │  │ Package: pkg-sand-11                 │ │
│                            │  │ [View Device]                        │ │
│                            │  └──────────────────────────────────────┘ │
│                            │                                            │
│                            │  [+ Assign Device]                         │
├────────────────────────────┴────────────────────────────────────────────┤
│  📍 위치 정보                                                           │
│  [Show on Map] - 지도에 스토어 위치 표시                               │
├─────────────────────────────────────────────────────────────────────────┤
│  ℹ️  메타데이터                                                         │
│  Created: 2024-01-15 10:30 by admin                                    │
│  Updated: 2026-01-15 10:30 by admin                                    │
└─────────────────────────────────────────────────────────────────────────┘
```

## 주요 구성 요소

### 1. 공통 사이드바
- Dashboard, Product, Package, Content, Devices, Stores(활성화), LocalAreas, Reports, Settings 메뉴
- 현재 페이지(Stores) 강조 표시

### 2. 헤더
- 페이지 제목: "Store Detail: {스토어명} (ID: {storeId})"
- 서브 정보:
  - 상태: 🏢 Active
  - 소속 지역: LocalArea 이름 (클릭 시 LocalArea Detail로 이동)
  - 디바이스 개수: N Devices

### 3. 기본 정보 섹션 (좌측)

#### 스토어 식별 정보
- **Store ID**: 고유 식별자 (읽기 전용)
- **Name**: 스토어 이름
- **LocalArea**: 소속 지역 (링크 - LocalArea Detail로 이동)

#### 주소 정보
- **Address**: 전체 주소 (address.street, city)
- **Postal Code**: 우편번호 (address.postalCode)
- **Country**: 국가 코드 (address.country)

#### 담당자 정보
- **Manager**: 담당자 이름 (meta.manager)
- **Phone**: 연락처 (meta.phone)
- **Email**: 이메일 (meta.email)
- **SLA**: 지원 수준 (meta.sla)

#### 액션 버튼
- **[Edit Store]**: 스토어 편집 페이지로 이동
- **[Delete Store]**: 스토어 삭제 (확인 모달)
  - 디바이스가 연결되어 있으면 경고

### 4. 연결된 디바이스 섹션 (우측)
- 제목: "💻 연결된 디바이스 (N)"
- 각 디바이스 카드 표시:
  - Device ID | Device Name
  - 상태: 🟢 Online / 🟡 Idle / 🔴 Offline
  - Last seen: 상대 시간 표시
  - Package: 설치된 패키지명
  - [View Device]: 디바이스 상세 페이지로 이동
- **[+ Assign Device]** 버튼:
  - 디바이스 할당 모달 표시
  - 스토어에 할당되지 않은 디바이스 목록
  - 선택 후 할당

### 5. 위치 정보 섹션
- **[Show on Map]** 버튼: 지도에 스토어 위치 표시
- 지도 API 연동 (Google Maps, Naver Maps, etc.)

### 6. 메타데이터 섹션 (하단)
- **Created**: 생성일시 및 생성자
- **Updated**: 최종 수정일시 및 수정자
- 읽기 전용 정보

## 주요 상호작용 플로우

### 1. 스토어 정보 확인
1. Store List에서 특정 스토어의 [View] 클릭
2. Store Detail 페이지 오픈
3. 스토어 기본 정보, 주소, 담당자 정보 확인
4. 연결된 디바이스 목록 확인

### 2. 스토어 편집
1. [Edit Store] 버튼 클릭
2. Store Editor 페이지로 이동
3. 정보 수정 후 저장
4. Store Detail 페이지로 복귀 (변경사항 반영)

### 3. 스토어 삭제
1. [Delete Store] 버튼 클릭
2. 확인 모달 표시:
   - "정말 삭제하시겠습니까?"
   - 연결된 디바이스가 있으면: "이 스토어에 {N}개의 디바이스가 연결되어 있습니다. 삭제하면 디바이스의 스토어 할당이 해제됩니다."
3. 확인 → 삭제 수행
4. Store List로 복귀

### 4. 디바이스 확인
1. 디바이스 카드의 [View Device] 클릭
2. Device Detail 페이지로 이동
3. 디바이스 상세 정보 확인

### 5. 디바이스 할당
1. [+ Assign Device] 버튼 클릭
2. 디바이스 할당 모달 표시
   - 현재 스토어에 할당되지 않은 디바이스 목록
   - 검색 및 필터링 기능
3. 디바이스 선택 후 [Assign] 클릭
4. 연결된 디바이스 목록에 추가
5. 성공 토스트 메시지 표시

### 6. LocalArea 확인
1. LocalArea 이름 클릭
2. LocalArea Detail 페이지로 이동
3. 상위 지역 정보 및 다른 스토어 목록 확인

### 7. 지도 보기
1. [Show on Map] 버튼 클릭
2. 지도 모달 또는 새 탭에서 지도 표시
3. 스토어 위치 마커 표시

## 데이터 소스
- Store 엔티티: storeId, name, address, localAreaId, meta
- LocalArea 엔티티: 지역명 표시를 위해 참조
- Device 엔티티: 스토어에 할당된 디바이스 목록

## 컴포넌트 및 검증

### 주소 표시
- 전체 주소를 구조화하여 표시
- 국가 코드는 ISO 3166-1 alpha-2 형식

### 디바이스 상태 표시
- Online 🟢: 5분 이내 통신
- Idle 🟡: 5분~1시간 이내 통신
- Offline 🔴: 1시간 이상 통신 없음

### 연락처 정보
- Phone: 클릭 시 전화 걸기 (tel: 링크)
- Email: 클릭 시 메일 작성 (mailto: 링크)

## 에러 및 엣지 케이스 처리

### 스토어 없음
- 잘못된 storeId로 접근 시:
  ```
  ⚠️ Store not found
  The store you are looking for does not exist.
  [Back to Store List]
  ```

### 디바이스 없음
- 연결된 디바이스가 없는 경우:
  ```
  💻 연결된 디바이스 (0)
  
  📭 No devices assigned to this store
  [+ Assign Device]
  ```

### 삭제 시 의존성 경고
- 디바이스가 연결되어 있을 경우:
  ```
  ⚠️ Warning: This store has 3 connected devices.
  Deleting will unassign these devices from the store.
  
  Do you want to continue?
  [Cancel] [Delete Anyway]
  ```

## UX 노트
- 스토어의 위치 정보를 시각적으로 확인할 수 있도록 지도 연동 제공
- 디바이스 목록은 상태별로 정렬하여 Offline 디바이스를 쉽게 파악
- LocalArea와의 관계를 명확히 표시하여 계층 구조 이해 지원
- 담당자 연락처는 즉시 통신 가능하도록 링크 제공

## 접근성
- 키보드 내비게이션 지원: Tab, Enter로 모든 기능 접근 가능
- 스크린리더 지원: 각 섹션에 적절한 헤딩과 레이블 제공
- 디바이스 상태는 색상과 아이콘, 텍스트 모두 제공

## 다음 단계
- 지도 뷰 통합 (Google Maps, OpenStreetMap)
- 스토어별 통계 대시보드 (디바이스 상태, 패키지 배포 현황)
- 스토어 이력 관리 (변경 이력 추적)

---

문서 작성자: CMS 팀  
작성일: 2026-02-14
