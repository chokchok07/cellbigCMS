````markdown
# `LocalArea` 엔티티 정의

## 개요
`LocalArea`는 스토어 및 배포 정책의 지리적/조직적 구분 단위입니다. 국가, 도시, 영업권역 등으로 사용되며 최상위 지리적 구분 단위입니다.

## 주요 속성
- `localAreaId` (string, PK): 지역 고유 식별자. 시스템에서 지역을 유일하게 식별하며 등록·조회·롤아웃 대상 지정에 사용합니다.
- `name` (string): 사람이 읽을 수 있는 지역명(예: `Seoul`, `APAC-KR`). UI 및 보고서에 표시됩니다.
- `description` (string, optional): 지역에 대한 상세 설명 또는 비고(예: 관할 범위, 특이사항).
- `address` (object, optional): 주소 정보(선택). 예시 구조: `{ "street", "city", "country" }`. 물리적 위치·지원·배송 관련으로 사용됩니다.
- `address2` (object, optional): 보조 주소 정보(예: 지급청구지, 상세 위치). `address`와 동일한 구조를 가집니다.
- `countryCode` (string, optional): 국가 코드(ISO 3166-1 alpha-2, 예: `KR`). 국가 기준 필터링 및 정책 적용에 사용됩니다.
- `createdAt` (datetime, ISO8601, optional): 레코드 생성 시각.
- `updatedAt` (datetime, ISO8601, optional): 레코드 최종 수정 시각.

### DB Schema (local_areas)

| 필드명 | 타입 | 설명 | 비고 |
|---|---|---|---|
| `local_area_id` | VARCHAR | 지역 고유 식별자 | **PK** |
| `name` | TEXT | 지역명 (사람이 읽을 수 있는 이름) | NOT NULL |
| `code` | VARCHAR | 지역 코드 (ERP/Legacy 연동용) | |
| `country_code` | VARCHAR(2) | 국가 코드 (ISO 3166-1 alpha-2) | |
| `address` | JSONB | 주소 정보 (`{street, city...}`) | |
| `meta` | JSONB | 확장 메타데이터 | |
| `created_at` | TIMESTAMPTZ | 생성 일시 | Default: `now()` |
| `updated_at` | TIMESTAMPTZ | 수정 일시 | Default: `now()` |

```sql
CREATE TABLE local_areas (
  local_area_id VARCHAR PRIMARY KEY,
  name TEXT NOT NULL,
  code VARCHAR,
  description TEXT,
  country_code VARCHAR(2),
  address JSONB, -- { street, city, country }
  meta JSONB,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now(),
);
```

## 관계
- LocalArea 1:N Store — 한 지역(로컬에어리어) 아래에 다수의 스토어가 존재.

## 예시 JSON
```json
{
  "localAreaId": "localarea-seoul",
  "name": "Seoul",
  "description": "서울 권역 (본사 관할)",
  "countryCode": "KR",
  "address": {
    "street": "1 Jongno",
    "city": "Seoul",
    "postalCode": "03000",
    "country": "Korea"
  },
  "createdAt": "2025-10-01T09:00:00Z",
  "updatedAt": "2026-01-15T15:30:00Z"
}
```

## 유효성 규칙
- `localAreaId`는 유일해야 함.
- `country` 필드는 유효한 ISO 코드여야 함.

## 운영·관리 노트
- 지역 기반 롤아웃과 보고서(지역별 배포율/오류)를 연동하면 운영 관점에서 유용.

````
