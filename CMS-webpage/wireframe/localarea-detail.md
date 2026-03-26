# LocalArea Detail UI 와이어프레임

## 개요
- 목적: 개별 지역(LocalArea)의 상세 정보, 하위 지역, 스토어 목록을 확인하고 관리합니다.
- 접근 경로: LocalArea List에서 [View] 버튼 클릭

## ASCII Layout

```
┌─────────────────────────────────────────────────────────────────────────┐
│  LocalArea Detail: Seoul (ID: localarea-seoul)                          │
│  🌏 Active  •  8 Stores                                                │
├────────────────────────────┬────────────────────────────────────────────┤
│                            │                                            │
│  📋 기본 정보              │  🏢 스토어 목록 (8)                       │
│                            │                                            │
│  LocalArea ID:             │  ┌──────────────────────────────────────┐ │
│  localarea-seoul           │  │ store-1001 | 강남 쇼룸               │ │
│                            │  │ Address: 서울시 강남구 테헤란로 1    │ │
│  Name: Seoul               │  │ Devices: 3                           │ │
│  Code: KR-SEL              │  │ [View Store]                         │ │
│                            │  └──────────────────────────────────────┘ │
│  Parent Area: Korea        │                                            │
│  (Click to view)           │  ┌──────────────────────────────────────┐ │
│                            │  │ store-1002 | 홍대 매장               │ │
│  Country: KR               │  │ Address: 서울시 마포구 홍익로 1      │ │
│  Timezone: Asia/Seoul      │  │ Devices: 5                           │ │
│                            │  │ [View Store]                         │ │
│  Description:              │  └──────────────────────────────────────┘ │
│  서울 권역 (본사 관할)     │                                            │
│                            │  ┌──────────────────────────────────────┐ │
│  [Edit LocalArea]          │  │ store-1003 | 잠실 롯데점             │ │
│  [Delete LocalArea]        │  │ Address: 서울시 송파구 올림픽로 1    │ │
│                            │  │ Devices: 4                           │ │
│                            │  │ [View Store]                         │ │
│                            │  └──────────────────────────────────────┘ │
│                            │                                            │
│                            │  [Show All Stores]                         │
├────────────────────────────┼────────────────────────────────────────────┤
│  🌳 하위 지역 (0)          │                                            │
│                            │                                            │
│  📭 No child areas         │                                            │
│                            │                                            │
├────────────────────────────┴──────────────────────────────────────────────┤
│  📍 위치 정보                                                           │
│  Address: 1 Jongno, Seoul, 03000, Korea                                │
│  [Show on Map] - 지도에 지역 표시                                      │
├─────────────────────────────────────────────────────────────────────────┤
│  ℹ️  메타데이터                                                         │
│  Created: 2025-10-01 09:00 by admin                                    │
│  Updated: 2026-01-15 15:30 by admin                                    │
└─────────────────────────────────────────────────────────────────────────┘
```

## 주요 구성 요소

### 1. 공통 사이드바
- Dashboard, Product, Package, Content, Devices, Stores, LocalAreas(활성화), Reports, Settings 메뉴
- 현재 페이지(LocalAreas) 강조 표시

### 2. 헤더
- 페이지 제목: "LocalArea Detail: {지역명} (ID: {localAreaId})"
- 서브 정보:
  - 상태: 🌏 Active
  - 스토어 개수: N Stores

### 3. 기본 정보 섹션 (좌측 상단)

#### 지역 식별 정보
- **LocalArea ID**: 고유 식별자 (읽기 전용)
- **Name**: 지역 이름
- **Country**: 국가 코드 (countryCode)

#### 설명
- **Description**: 지역에 대한 상세 설명

#### 액션 버튼
- **[Edit LocalArea]**: 지역 편집 페이지로 이동
- **[Delete LocalArea]**: 지역 삭제 (확인 모달)
  - 스토어가 있으면 경고

### 4. 스토어 목록 섹션 (우측 상단)
- 제목: "🏢 스토어 목록 (N)"
- 각 스토어 카드 표시:
  - Store ID | Store Name
  - Address: 주소 요약
  - Devices: 디바이스 개수
  - [View Store]: 스토어 상세 페이지로 이동
- 최대 5개까지만 표시
- **[Show All Stores]** 버튼:
  - Store List로 이동 (해당 지역으로 필터링)

### 5. 하위 지역 섹션 (좌측 하단)
- 제목: "🌳 하위 지역 (N)"
- 하위 지역이 있는 경우:
  - 각 하위 지역 카드 표시
  - LocalArea ID | Name
  - Stores 수
  - [View Area]: 하위 LocalArea Detail로 이동
- 하위 지역이 없는 경우:
  ```
  📭 No child areas
  This is a leaf-level area.
  ```

### 6. 위치 정보 섹션
- **Address**: 지역 대표 주소 (address 객체)
- **[Show on Map]** 버튼: 지도에 지역 범위 표시

### 7. 메타데이터 섹션 (하단)
- **Created**: 생성일시 및 생성자
- **Updated**: 최종 수정일시 및 수정자
- 읽기 전용 정보

## 주요 상호작용 플로우

### 1. 지역 정보 확인
1. LocalArea List에서 특정 지역의 [View] 클릭
2. LocalArea Detail 페이지 오픈
3. 지역 기본 정보, 국가 확인
4. 소속 스토어 목록 확인
5. 하위 지역 목록 확인

### 2. 지역 편집
1. [Edit LocalArea] 버튼 클릭
2. LocalArea Editor 페이지로 이동
3. 정보 수정 후 저장
4. LocalArea Detail 페이지로 복귀 (변경사항 반영)

### 3. 지역 삭제
1. [Delete LocalArea] 버튼 클릭
2. 확인 모달 표시:
   - "정말 삭제하시겠습니까?"
   - 스토어가 있으면: "이 지역에 {M}개의 스토어가 있습니다."
   - "삭제하면 모든 하위 항목에 영향을 미칩니다."
3. 확인 → 삭제 수행
4. LocalArea List로 복귀

### 4. 스토어 확인
1. 스토어 카드의 [View Store] 클릭
2. Store Detail 페이지로 이동
3. 스토어 상세 정보 확인

### 5. 전체 스토어 목록 보기
1. [Show All Stores] 버튼 클릭
2. Store List 페이지로 이동
3. 해당 지역으로 필터링된 상태

### 6. 상위 지역 확인
1. 지역 보기를 통해 상위 지역 정보 확인

### 7. 하위 지역 확인
1. 하위 지역 카드의 [View Area] 클릭
2. 하위 LocalArea Detail 페이지로 이동
3. 하위 지역 정보 확인

### 8. 지도 보기
1. [Show on Map] 버튼 클릭
2. 지도 모달 또는 새 탭에서 지도 표시
3. 지역 범위 및 스토어 위치 마커 표시

## 데이터 소스
- LocalArea 엔티티: localAreaId, name, countryCode, address, description
- Store 엔티티: 지역에 속한 스토어 목록
- LocalArea 엔티티 (재귀): 하위 지역 목록

## 컴포넌트 및 검증

### 계층 구조 표시
- 하위 지역: 트리 구조로 표시

### 시간대 표시
- 삭제됨

## 에러 및 엣지 케이스 처리

### 지역 없음
- 잘못된 localAreaId로 접근 시:
  ```
  ⚠️ LocalArea not found
  The area you are looking for does not exist.
  [Back to LocalArea List]
  ```

### 스토어 없음
- 소속 스토어가 없는 경우:
  ```
  🏢 스토어 목록 (0)
  
  📭 No stores in this area
  ```

### 하위 지역 없음
- 하위 지역이 없는 경우:
  ```
  🌳 하위 지역 (0)
  
  📭 No child areas
  This is a leaf-level area.
  ```

### 삭제 시 의존성 경고
- 스토어가 있을 경우:
  ```
  ⚠️ Warning: This local area has:
  - 8 stores
  
  Deleting will affect all child items.
  How do you want to proceed?
  
  [Cancel] [Delete All] [Reassign Items]
  ```

## UX 노트
- 하위 지역을 명확히 표시하여 관계 이해 지원
- 스토어 목록은 요약만 표시하고 전체 보기는 별도 버튼 제공
- 하위 지역 간 네비게이션을 원활하게 지원

## 접근성
- 키보드 내비게이션 지원: Tab, Enter로 모든 기능 접근 가능
- 스크린리더 지원: 각 섹션에 적절한 헤딩과 레이블 제공
- 계층 구조는 들여쓰기와 함께 aria-level 속성 제공

## 다음 단계
- 지도 뷰 통합 (지역 범위 표시)
- 지역별 통계 대시보드 (스토어, 디바이스 현황)
- 지역별 배포 정책 관리

---

문서 작성자: CMS 팀  
작성일: 2026-02-14
