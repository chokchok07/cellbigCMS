# `User` 엔티티 정의

## 개요
`User` 엔티티는 CMS 관리자 페이지에 접근하는 운영자 및 관리자 계정을 정의합니다. 역할(Role) 기반의 권한 관리와 접근 제어(RBAC)를 위한 기본 단위입니다.

관련 기능: [cms-admin-features.md](../cms-admin-features.md) (사용자 계정 관리)

## 데이터 구조

### Users 테이블 (사용자 정보)

| 필드명 | 타입 | 설명 | 제약조건 |
|---|---|---|---|
| `user_id` | UUID | 사용자 고유 식별자 | PK, Default: `gen_random_uuid()` |
| `username` | VARCHAR(50) | 로그인 아이디 | UNIQUE, NOT NULL |
| `email` | VARCHAR(255) | 연락처 이메일 | UNIQUE, NOT NULL |
| `password_hash` | VARCHAR(255) | bcrypt 등으로 암호화된 비밀번호 | NOT NULL |
| `full_name` | VARCHAR(100) | 사용자 실명 또는 표시 이름 | |
| `role` | VARCHAR(20) | 권한 레벨 (`super_admin`, `local_manager`, `store_manager`) | NOT NULL |
| `scope_ids` | VARCHAR[] | 관리 권한 접근 ID 목록 (LocalArea ID들 또는 Store ID들) | Default: `[]` |
| `status` | VARCHAR(20) | 계정 상태 (`active`, `suspended`, `pending`) | NOT NULL, Default: 'active' |
| `last_login_at` | TIMESTAMPTZ | 마지막 로그인 일시 | |
| `created_at` | TIMESTAMPTZ | 생성 일시 | Default: `now()` |
| `updated_at` | TIMESTAMPTZ | 수정 일시 | Default: `now()` |

### UserActivityLogs 테이블 (감사 로그 - 권장)

시스템 보안 및 운영 투명성을 위해 사용자의 주요 활동을 기록합니다.

| 필드명 | 타입 | 설명 | 제약조건 |
|---|---|---|---|
| `log_id` | BIGSERIAL | 로그 고유 식별자 | PK |
| `user_id` | UUID | 활동 수행자 ID | FK (`users.user_id`) |
| `action_type` | VARCHAR(50) | 활동 유형 (예: `LOGIN`, `CREATE_CONTENT`, `DELETE_DEVICE`) | NOT NULL |
| `target_entity` | VARCHAR(50) | 대상 엔티티 (예: `content`, `device`) | |
| `target_id` | VARCHAR | 대상 엔티티의 ID | |
| `details` | JSONB | 변경 내용 또는 추가 정보 (IP 주소, 변경 전/후 값 등) | |
| `created_at` | TIMESTAMPTZ | 활동 일시 | Default: `now()` |

## 역할(Role) 정의 예시

### 권한 모델 (Role & Scope)

사용자의 권한은 **Role(할 수 있는 일)**과 **Target(적용 대상)**의 조합으로 구성됩니다.
하나의 컬럼 `scope_id`를 사용하여 다양한 대상을 유연하게 가리킬 수 있습니다.

| Role | Scope ID (Target ID) | 설명 및 접근 범위 |
|---|---|---|
| `super_admin` | `NULL` | 전체 시스템 관리자 (모든 데이터 접근) |
| `local_manager` | `'localarea-seoul'` | **지역 관리자**: 해당 지역(`LocalArea`) 및 하위 모든 매장/디바이스 관리 |
| `store_manager` | `'store-gangnam'` | **매장 관리자**: 특정 매장(`Store`) 및 소속 디바이스 관리 |
| `technician` | `'device-001'` (선택) | **기술자**: 특정 디바이스(`Device`) 유지보수 및 로그 확인 |

### Users 테이블 구조 (수정 제안)

`managed_local_area_id` 등 개별 컬럼 대신, `scope_id` 하나로 통합하여 유연성을 확보합니다.

| 필드명 | 타입 | 설명 |
|---|---|---|
| `user_id` | UUID | PK |
| `role` | VARCHAR(20) | `super_admin`, `local_manager`, `store_manager`, `technician` |
| `scope_id` | VARCHAR | **권한 범위 대상 ID** (Role에 따라 LocalAreaID, StoreID, DeviceID 중 하나가 들어감) |
| `...` | ... | 나머지 정보 |

> **Tip**: `scope_id`가 어떤 테이블의 ID인지(참조 대상)는 `role` 값에 의해 결정됩니다. 애플리케이션 레벨에서 이를 해석하여 적절한 조회 쿼리를 생성해야 합니다.


- **Admin (관리자)**:
  - 모든 메뉴 접근 가능.
  - 사용자 생성/삭제 및 시스템 설정 변경 가능.
- **Operator (운영자)**:
  - 콘텐츠 업로드, 패키지 구성, 디바이스 관리 등 일상적인 운영 업무 수행.
  - 시스템 설정 및 사용자 관리 메뉴 접근 제한.
- **Viewer (읽기 전용)**:
  - 대시보드 및 각종 리스트 조회만 가능.
  - 데이터 변경(생성/수정/삭제) 불가.
