# `Store` 엔티티 정의

## 개요
`Store`는 실제 콘텐츠가 운영되는 점포(지점) 단위를 나타냅니다. 각 스토어는 하나의 `LocalArea`에 속하며, 1개 이상의 `Device`와 연관됩니다.

## 주요 속성
- `storeId` (string, PK): 스토어 고유 ID
- `name` (string): 스토어 명
- `address` (object): { `street`, `city`, `postalCode`, `country` }
- `localAreaId` (string, FK): 소속 지역(LocalArea) ID
- `zip` (string, optional): 해당 지역의 대표 우편번호. 주소 객체의 `postalCode`와 중복될 수 있습니다.
- `address` (object, optional): 주소 정보(선택). 예시 구조: `{ "street", "city", "postalCode", "country" }`. 물리적 위치·지원·배송 관련으로 사용됩니다.
- `address2` (object, optional): 보조 주소 정보(예: 지급청구지, 상세 위치). `address`와 동일한 구조를 가집니다.
- `meta` (object): 추가 메타데이터(예: 고객 계약 정보, SLA, 현장 특이사항)
- `createdAt` / `updatedAt`

### DB Schema (stores)

| 필드명 | 타입 | 설명 | 비고 |
|---|---|---|---|
| `store_id` | VARCHAR | 매장 고유 식별자 | **PK** |
| `name` | TEXT | 매장 이름 | NOT NULL |
| `local_area_id` | VARCHAR | 소속 지역 ID | FK (`local_areas`) |
| `address` / `address2` | JSONB | 주소 및 상세 주소 | |
| `status` | VARCHAR(32) | 운영 상태 (active, closed 등) | |
| `contacts` | JSONB | 연락처 목록 (`[{name,phone},...]`) | |
| `timezone` | VARCHAR | 타임존 (예: Asia/Seoul) | |
| `meta` | JSONB | 확장 메타데이터 (SLA 등) | |
| `meta` | JSONB | 확장 메타데이터 (SLA 등) | |
| `created_at` | TIMESTAMPTZ | 생성 일시 | Default: `now()` |
| `updated_at` | TIMESTAMPTZ | 수정 일시 | Default: `now()` |

```sql
CREATE TABLE stores (
  store_id VARCHAR PRIMARY KEY,
  name TEXT NOT NULL,
  address JSONB, -- {street, city, state, country, zipcode}
  address2 JSONB,
  local_area_id VARCHAR, -- FK (local_areas)
  zip VARCHAR,
  contacts JSONB, -- [{name,role,phone,email},...]
  status VARCHAR(32), -- active, closed, renovation
  timezone VARCHAR,
  meta JSONB,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now(),
  CONSTRAINT fk_stores_localarea FOREIGN KEY(local_area_id) REFERENCES local_areas(local_area_id)
);
-- Index: local_area_id
```

## 관계
- Store N:1 LocalArea — 스토어는 특정 지역에 속합니다.
- Store 1:N Device — 스토어는 여러 디바이스를 가집니다.

## 예시 JSON
```json
{
  "storeId": "store-1001",
  "name": "강남 쇼룸",
  "address": {
    "street": "서울시 강남구 테헤란로 1",
    "city": "Seoul",
    "postalCode": "06236",
    "country": "KR"
  },
  "address2": null,
  "localAreaId": "localarea-seoul",
  "zip": "06236",
  "meta": {
    "manager": "홍길동",
    "phone": "010-1234-5678",
    "email": "hong@example.com",
    "sla": "24h support"
  },
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-15T10:30:00Z"
}
```

## 유효성 규칙
- `storeId`는 유일해야 함.
- `localAreaId`는 존재하는 `LocalArea`를 참조해야 함.
- 연락처 항목은 최소 하나 이상 권장.
- 주소의 `country`는 ISO 3166-1 alpha-2 코드 권장.

## 운영·관리 노트
- 배포 정책(예: 점진적 롤아웃)과 스토어 단위 필터를 지원하면 현장 운영에 유용합니다.
- 오프라인 스토어의 경우 디바이스 상태 동기화·대역폭 정책을 명확히 하세요.
- 개인정보(담당자 연락처)는 접근 제어 및 로그 감사 대상으로 관리해야 함.


