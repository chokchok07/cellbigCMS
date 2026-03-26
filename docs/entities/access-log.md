# `AccessLog` (Content Access Log) 엔티티 정의

## 개요
`AccessLog`는 디바이스에서 발생하는 콘텐츠 실행, 종료, 오류 등의 이벤트를 기록하는 로그 데이터입니다.
이 로그는 콘텐츠 사용량 집계, 과금 근거(기간제/횟수제), 기술적 문제 해결(디버깅) 등을 위해 수집됩니다.

## 주요 속성
 - `logId` (bigint, PK): 로그 고유 식별자 (Auto Increment).
 - `deviceId` (string, FK): 이벤트를 발생시킨 디바이스 ID.
 - `contentId` (string, FK): 실행된 콘텐츠 ID.
 - `packageId` (string, FK, optional): 실행된 패키지 버전 ID.
 - `action` (enum): 이벤트 유형.
    - `START`: 콘텐츠 실행 시작.
    - `STOP`: 콘텐츠 실행 종료.
    - `HEARTBEAT`: 실행 중 주기적 생존 신호 (장시간 실행 추적용).
    - `ERROR`: 실행 중 오류 발생.
 - `timestamp` (datetime): 이벤트 발생 시각 (UTC).
 - `duration` (integer, optional): `STOP` 이벤트 시, 실행 지속 시간(초).
 - `ipAddress` (string, optional): 로그 전송 당시의 디바이스 IP.
 - `meta` (jsonb, optional): 추가 정보 (에러 코드, 메모리 사용량 등).

### DB Schema (access_logs)

| 필드명 | 타입 | 설명 | 비고 |
|---|---|---|---|
| `log_id` | BIGSERIAL | 로그 ID | **PK** |
| `device_id` | VARCHAR | 디바이스 ID | FK |
| `content_id` | VARCHAR | 콘텐츠 ID | FK |
| `package_id` | VARCHAR | 패키지 ID | FK |
| `action` | VARCHAR(20) | `START`, `STOP`, `ERROR` | |
| `timestamp` | TIMESTAMPTZ | 발생 시각 | Index |
| `duration` | INTEGER | 실행 시간 (초) | STOP 로그에만 존재 |
| `ip_address` | VARCHAR(45) | IP 주소 | |
| `meta` | JSONB | 추가 메타데이터 | |
| `created_at` | TIMESTAMPTZ | 수집 서버 저장 시각 | default now() |

```sql
CREATE TABLE access_logs (
  log_id BIGSERIAL PRIMARY KEY,
  device_id VARCHAR REFERENCES devices(device_id),
  content_id VARCHAR REFERENCES contents(content_id),
  package_id VARCHAR REFERENCES packages(package_id),
  action VARCHAR(20) NOT NULL, -- 'START', 'STOP', 'HEARTBEAT', 'ERROR'
  timestamp TIMESTAMPTZ NOT NULL,
  duration INTEGER, -- Used when action='STOP'
  ip_address VARCHAR(45),
  meta JSONB,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- 인덱스: 시계열 조회 및 디바이스별/콘텐츠별 조회 최적화
CREATE INDEX idx_logs_timestamp ON access_logs(timestamp);
CREATE INDEX idx_logs_device ON access_logs(device_id, timestamp);
CREATE INDEX idx_logs_content ON access_logs(content_id, timestamp);
```

## 로그 수집 및 활용 정책
1. **수집 주기:**
   - 디바이스는 오프라인 상태일 때 로그를 로컬 DB(SQLite 등)에 적재합니다.
   - 온라인 연결 시, 또는 설정된 주기(예: 1시간)마다 서버로 일괄 전송(Batch Upload)합니다.
2. **데이터 보존:**
   - Raw Log는 3개월~1년 보관 후 Cold Storage로 이관하거나 요약 테이블(Summary)로 집계 후 삭제합니다.
3. **사용량 리포트:**
   - `START`와 `STOP` 로그를 매칭하여 정확한 가동 시간(Uptime)과 실행 횟수(Play Count)를 산출합니다.

## 데이터 접근 권한 (Role-Based Scope Policy)

`User`의 `Role`과 `Scope_IDs`에 따른 로그 조회 범위 제한 로직입니다.
다중 지역/매장 관리를 위해 `scope_ids`는 배열(Array) 형태를 가집니다.

### 1. Super Admin (전체 관리자)
- **Role:** `super_admin`
- **Scope:** `NULL` or Empty
- **Logic:** 모든 로그 조회 가능.
- **SQL:** `SELECT * FROM access_logs;`

### 2. Local Manager (지역 관리자)
- **Role:** `local_manager`
- **Scope:** `scope_ids` (예: `['SEOUL', 'BUSAN']`)
- **Logic:** 할당된 지역들(`LocalArea`)에 속한 **모든 하위 Store의 Device** 로그만 조회.
- **SQL:**
  ```sql
  SELECT al.* 
  FROM access_logs al
  JOIN devices d ON al.device_id = d.device_id
  JOIN stores s ON d.store_id = s.store_id
  WHERE s.local_area_id = ANY(:user_scope_ids); -- 예: ['SEOUL', 'BUSAN']
  ```

### 3. Store Manager (매장 관리자)
- **Role:** `store_manager`
- **Scope:** `scope_ids` (예: `['STORE_001', 'STORE_002']`)
- **Logic:** 본인 매장들(`Store`)에 소속된 **Device** 로그만 조회.
- **SQL:**
  ```sql
  SELECT al.* 
  FROM access_logs al
  JOIN devices d ON al.device_id = d.device_id
  WHERE d.store_id = ANY(:user_scope_ids); -- 예: ['STORE_001', 'STORE_002']
  ```
