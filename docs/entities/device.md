# `Device` 엔티티 정의

## 개요
`Device`는 CMS가 관리하는 실제 설치 장치 단위입니다. 디바이스는 PC(호스트)와 연결된 주변 장치들(터치모니터, 센서, 프로젝터 등)로 구성되며, CMS와 통신하여 인증·다운로드·상태 보고를 수행합니다.

## 주요 속성
 - `deviceId` (string, PK): 디바이스 고유 식별자. CMS 내에서 장치를 유일하게 식별하는 값으로 등록·조회·권한 부여에 사용됩니다.
 - `name` (string): 사용자에게 표시되는 장치명(예: 호스트명). 관리 UI와 로그에서 식별 용도로 사용합니다.
 - `description` (string, optional): 장치에 대한 추가 설명(설치 위치, 비고 등).
 - `storeId` (string, FK, optional): 디바이스가 소속된 물리적 매장 또는 지점 ID. 매장 단위 집계·권한 관리를 위해 사용합니다.
 - `mac` (string[], max 2): MAC 주소 목록. 최대 2개까지 등록 가능하며, 첫번째 항목이 우선 식별자로 사용됩니다. 인증·디바이스 식별에 사용됩니다.
 - `lastSeen` (datetime, ISO8601, optional): CMS가 마지막으로 장치와 통신한 시각. 상태 모니터링 및 오프라인 판단에 사용됩니다.
 - `meta` (object, optional): 하드웨어 및 주변장치 정보(예: CPU, RAM, connectedDevices 등). 디바이스 특성에 따른 콘텐츠 제공·지원용입니다.

### DB Schema (devices)

| 필드명 | 타입 | 설명 | 비고 |
|---|---|---|---|
| `device_id` | VARCHAR | 디바이스 고유 ID | **PK** |
| `name` | TEXT | 디바이스명 (Host Name 등) | |
| `store_id` | VARCHAR | 소속된 매장 ID (옵션) | FK (`stores`) |
| `mac_addresses` | VARCHAR[] | 유니크 맥 주소 목록 (Max 2) | |
| `status` | VARCHAR(20) | 현재 상태 (`online`, `offline`) | Default: `offline` |
| `last_seen` | TIMESTAMPTZ | 마지막 접속 일시 | |
| `ip_address` | VARCHAR(45) | 마지막 접속 IP | |
| `meta` | JSONB | 디바이스 사양 (`{cpu, ram}`) | |
| `created_at` | TIMESTAMPTZ | 생성 일시 | Default: `now()` |
| `updated_at` | TIMESTAMPTZ | 수정 일시 | Default: `now()` |

```sql
CREATE TABLE devices (
  device_id VARCHAR PRIMARY KEY,
  name TEXT,
  description TEXT,
  store_id VARCHAR, -- FK (stores)
  mac_addresses VARCHAR[] DEFAULT ARRAY[]::VARCHAR[],
  last_seen TIMESTAMPTZ,
  ip_address VARCHAR(45),
  status VARCHAR(20) DEFAULT 'offline',
  meta JSONB,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now(),
  CONSTRAINT fk_devices_store FOREIGN KEY(store_id) REFERENCES stores(store_id),
  CONSTRAINT chk_mac_count CHECK (COALESCE(array_length(mac_addresses,1),0) <= 2)
);
```

### DB Schema (device_products) — N:M Mapping

한 디바이스에 여러 제품이 설치될 수 있으므로 별도 테이블로 분리합니다.

| 필드명 | 타입 | 설명 | 비고 |
|---|---|---|---|
| `device_id` | VARCHAR | 디바이스 ID | **PK, FK** |
| `product_id` | VARCHAR | 제품 ID | **PK, FK** |
| `installed_package_id` | VARCHAR | 해당 제품의 설치된 패키지 | FK (`packages`) |
| `is_active` | BOOLEAN | 제품 활성화 여부 | Default: `true` |
| `updated_at` | TIMESTAMPTZ | 마지막 상태 변경일 | |

```sql
CREATE TABLE device_products (
  device_id VARCHAR,
  product_id VARCHAR,
  installed_package_id VARCHAR,
  is_active BOOLEAN DEFAULT true,
  updated_at TIMESTAMPTZ DEFAULT now(),
  PRIMARY KEY (device_id, product_id),
  CONSTRAINT fk_dp_device FOREIGN KEY(device_id) REFERENCES devices(device_id) ON DELETE CASCADE,
  CONSTRAINT fk_dp_product FOREIGN KEY(product_id) REFERENCES products(product_id),
  CONSTRAINT fk_dp_package FOREIGN KEY(installed_package_id) REFERENCES packages(package_id)
);
```

## 관계
- Device N:M Product — 디바이스는 여러 제품을 설치할 수 있으며, `device_products` 테이블을 통해 관리됩니다.

## 인증 관련
- 인증은 `contentId` + `mac`(목록 중 하나) 방식 또는 One-time 인증으로 수행.
- 디바이스 등록 시 `deviceId`와 `mac` 목록(최대 2개)을 서버에 제출하고, 서버는 등록 정보를 저장.

## 예시 JSON
```json
{
  "deviceId": "dev-001",
  "name": "sand-pc-01",
  "description": "샌드크래프트 전시장 호스트",
  "productId": "product-sandcraft",
  "storeId": "store-010",
  "mac": ["AA:BB:CC:DD:EE:FF", "11:22:33:44:55:66"],
  "installedPackageId": "pkg-sand-11",
  "lastSeen": "2026-02-05T12:00:00Z",
  "meta": {
    "cpu": "Intel i5",
    "ram": "8GB",
    "connectedDevices": ["touch-monitor-01"]
  }
}
```

## 운영·유지보수
- 하드웨어 변경(예: MAC 변경) 시 재등록 정책을 정의.

## 보안·프라이버시
- MAC 주소 등 식별 정보는 필요한 경우에만 전송 및 저장하고, 접근 제어를 적용.

## 주의사항
- 하나의 제품이 다수의 디바이스로 구성되는 경우(멀티-디바이스 제품) 동기화 정책 및 역할 분담(예: 마스터/슬레이브)을 문서화하세요.
