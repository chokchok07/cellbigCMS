# `License` (Serial Key) 엔티티 정의

## 개요
`License`는 제품(Product) 사용 권한을 제어하는 시리얼 키 및 계약 정보를 의미합니다.
단순 영구 소장(Perpetual) 외에도 기간제(Subscription), 단기 계약 등을 지원하며 오프라인 환경을 고려한 검증 로직을 포함합니다.

## 주요 속성
 - `serialKey` (string, PK): `License-XXXX-YYYY` 형태의 고유 식별 키.
 - `productId` (string, FK): 대상 제품.
 - `type` (enum): 라이선스 유형.
    - `PERPETUAL`: 영구 라이선스 (만료 없음).
    - `SUBSCRIPTION`: 기간제 (활성화 시점부터 n일).
    - `FIXED_DATE`: 특정 날짜까지 (예: 행사 기간).
 - `duration` (integer, optional): `SUBSCRIPTION`일 경우 유효 기간(일 단위).
 - `maxDevices` (integer): 이 키 하나로 인증 가능한 최대 기기 수 (기본 1).
 - `status` (enum): `UNUSED`, `ACTIVE`, `REVOKED`, `EXPIRED`.
 - `activatedAt` (datetime): 최초 인증 일시.
 - `expiresAt` (datetime): 만료 예정 일시. (`activatedAt` + `duration` 또는 고정 날짜)

### DB Schema (licenses)

| 필드명 | 타입 | 설명 | 비고 |
|---|---|---|---|
| `serial_key` | VARCHAR | 시리얼 키 | **PK** |
| `product_id` | VARCHAR | 제품 ID | FK |
| `package_id` | VARCHAR | 고정 패키지 버전 (옵션) | FK |
| `license_type` | VARCHAR | `PERPETUAL`, `SUBSCRIPTION` | Default: `PERPETUAL` |
| `duration_days` | INTEGER | 유효 기간 (일) | `SUBSCRIPTION`용 |
| `max_devices` | INTEGER | 최대 인증 가능 수 | Default: 1 |
| `current_usage` | INTEGER | 현재 인증된 기기 수 | |
| `status` | VARCHAR | 상태 | |
| `activated_at` | TIMESTAMPTZ | 최초 활성화 일시 | |
| `expires_at` | TIMESTAMPTZ | 만료 일시 | 계산된 값 |
| `created_at` | TIMESTAMPTZ | 생성 일시 | |

```sql
CREATE TABLE licenses (
  serial_key VARCHAR PRIMARY KEY,
  product_id VARCHAR REFERENCES products(product_id),
  package_id VARCHAR REFERENCES packages(package_id), -- 특정 버전 고정 시
  license_type VARCHAR(20) DEFAULT 'PERPETUAL', -- 'PERPETUAL', 'SUBSCRIPTION', 'FIXED_DATE'
  duration_days INTEGER DEFAULT 0, -- 0이면 무제한이거나 FIXED_DATE 사용
  fixed_expire_date TIMESTAMPTZ, -- FIXED_DATE 용
  max_devices INTEGER DEFAULT 1,
  current_usage INTEGER DEFAULT 0,
  status VARCHAR(20) DEFAULT 'UNUSED', -- UNUSED, ACTIVE, REVOKED, EXPIRED
  activated_at TIMESTAMPTZ,
  expires_at TIMESTAMPTZ, -- 활성화 시점에 계산되어 저장됨
  created_at TIMESTAMPTZ DEFAULT now()
);
```

## 오프라인 인증 프로세스 (Secure Validation)

1. **발급 (Server):**
   - 클라이언트가 `serial_key` + `HW 정보` 전송.
   - 서버는 유효성 확인 후 **Signed License Token** 반환.
   - Token Payload: `{ key, expireDate: '2026-12-31', deviceId, signature }`

2. **검증 (Client):**
   - **Step 1 (서명 검증):** 로컬에 저장된 Token이 서버의 공개키로 검증되는지 확인.
   - **Step 2 (만료 검증):** `CurrentTime` timestamp가 Token의 `expireDate` 이전인지 확인.
   - **Step 3 (Anti-Rollback):** 
     - 앱 실행 시마다 암호화된 로컬 파일에 `LastRunTime` 기록.
     - `CurrentTime` < `LastRunTime` 발생 시, 시스템 시간 조작으로 간주하여 실행 차단.

3. **갱신 (Renewal):**
   - 만료가 임박하거나 계약 연장 시, 디바이스를 온라인에 연결하여 `/renew` API 호출.
   - 서버 DB의 `expires_at`이 연장되어 있다면 새로운 Token 발급.
