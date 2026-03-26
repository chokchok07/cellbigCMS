# 권장 DB 스키마 (PostgreSQL 기준)

이 문서는 `Content`, `Package`, `Product`, `Device`, `Store`, `LocalArea` 등의 엔티티에 대한 권장 테이블 구조와 제약을 정리합니다. 실제 도입 시에는 사용 DB, 성능 요구, 마이그레이션 정책에 맞춰 조정하세요.

-- 설계 원칙
- 모든 엔터티의 식별자(id)는 가능한 유연하게 `VARCHAR`(또는 `UUID`) 사용을 권장합니다.
- 반복/다대다 관계는 조인 테이블로 분리합니다(예: `package_contents`).
- 자유형 메타는 `jsonb`로 저장(스키마 진화 유리).
- MAC 주소는 최대 2개로 제한: `mac_addresses varchar[]` + CHECK로 제한.

## 테이블 정의 예시
다음 SQL 예시는 이해를 돕기 위한 권장 형태입니다.

-- 1) products
```sql
CREATE TABLE products (
  product_id VARCHAR PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT,
  default_package_id VARCHAR,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);
ALTER TABLE products
  ADD CONSTRAINT fk_products_default_package
  FOREIGN KEY (default_package_id) REFERENCES packages(package_id);
```

-- 2) contents
```sql
CREATE TABLE contents (
  content_id BIGSERIAL PRIMARY KEY,
  title JSONB NOT NULL, -- 권장: {"ko":"...","en":"..."} 형태
  description TEXT,
  thumbnail TEXT,
  category TEXT,
  type VARCHAR(32), -- single|container|child|mixed
  product_id VARCHAR,
  meta JSONB,
  entry_point TEXT,
  assets JSONB, -- 배열 또는 객체 형태 권장
  checksum TEXT,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now(),
  CONSTRAINT fk_contents_product FOREIGN KEY(product_id) REFERENCES products(product_id)
);
CREATE INDEX idx_contents_product_id ON contents(product_id);

-- content_versions (Content versioning with ZIP artifacts)
```sql
CREATE TABLE content_versions (
  content_version_id BIGSERIAL PRIMARY KEY,
  content_id BIGINT NOT NULL REFERENCES contents(content_id),
  version_tag VARCHAR NOT NULL,
  checksum VARCHAR NOT NULL, -- SHA-256 of the ZIP artifact
  artifact_url TEXT,
  artifact_filename TEXT,
  artifact_size_bytes BIGINT,
  artifact_content_type VARCHAR,
  storage_provider VARCHAR,
  state VARCHAR(32) NOT NULL DEFAULT 'draft',
  meta JSONB,
  created_by VARCHAR,
  created_at TIMESTAMPTZ DEFAULT now(),
  UNIQUE (content_id, version_tag)
);
CREATE INDEX idx_content_versions_content ON content_versions(content_id);
```

-- note: package_contents should reference content_version_id to pin a package to specific content versions
```

-- 3) packages
```sql
CREATE TABLE packages (
  package_id VARCHAR PRIMARY KEY,
  product_id VARCHAR NOT NULL,
  name TEXT NOT NULL,
  description TEXT,
  published BOOLEAN DEFAULT false,
  meta JSONB,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now(),
  CONSTRAINT fk_packages_product FOREIGN KEY(product_id) REFERENCES products(product_id)
);
CREATE INDEX idx_packages_product_id ON packages(product_id);
```

-- 3a) package_contents (Package N:M Content)
```sql
CREATE TABLE package_contents (
  package_id VARCHAR NOT NULL,
  content_id BIGINT NOT NULL,
  content_version_id BIGINT, -- NULL이면 항상 최신 버전, 값이 있으면 해당 버전 고정(Pinned)
  position INT DEFAULT 0,
  PRIMARY KEY (package_id, content_id),
  CONSTRAINT fk_pc_package FOREIGN KEY(package_id) REFERENCES packages(package_id) ON DELETE CASCADE,
  CONSTRAINT fk_pc_content FOREIGN KEY(content_id) REFERENCES contents(content_id) ON DELETE RESTRICT,
  CONSTRAINT fk_pc_version FOREIGN KEY(content_version_id) REFERENCES content_versions(content_version_id) ON DELETE SET NULL
);
CREATE INDEX idx_pc_package ON package_contents(package_id);
```

-- 4) local_areas
```sql
CREATE TABLE local_areas (
  local_area_id VARCHAR PRIMARY KEY,
  name TEXT NOT NULL,
  code VARCHAR,
  description TEXT,
  parent_local_area_id VARCHAR,
  country_code VARCHAR(2),
  timezone VARCHAR,
  address JSONB,
  meta JSONB,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now(),
  CONSTRAINT fk_localarea_parent FOREIGN KEY(parent_local_area_id) REFERENCES local_areas(local_area_id)
);
CREATE INDEX idx_localareas_parent ON local_areas(parent_local_area_id);
```

-- 5) stores
```sql
CREATE TABLE stores (
  store_id VARCHAR PRIMARY KEY,
  name TEXT NOT NULL,
  address JSONB,
  address2 JSONB,
  local_area_id VARCHAR,
  zip VARCHAR,
  contacts JSONB, -- [{name,role,phone,email},...]
  status VARCHAR(32),
  timezone VARCHAR,
  meta JSONB,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now(),
  CONSTRAINT fk_stores_localarea FOREIGN KEY(local_area_id) REFERENCES local_areas(local_area_id)
);
CREATE INDEX idx_stores_localarea ON stores(local_area_id);
```

-- 6) devices
```sql
CREATE TABLE devices (
  device_id VARCHAR PRIMARY KEY,
  name TEXT,
  description TEXT,
  -- product_id 제거 (N:M 관계로 변경)
  store_id VARCHAR,
  mac_addresses VARCHAR[] DEFAULT ARRAY[]::VARCHAR[], -- 최대 2개
  -- installed_package_id 제거 (N:M 관계로 변경)
  last_seen TIMESTAMPTZ,
  meta JSONB,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now(),
  CONSTRAINT fk_devices_store FOREIGN KEY(store_id) REFERENCES stores(store_id),
  CONSTRAINT chk_mac_count CHECK (COALESCE(array_length(mac_addresses,1),0) <= 2)
);
CREATE INDEX idx_devices_store ON devices(store_id);

-- 7) device_products (N:M Mapping)
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

-- 8) users
```sql
CREATE TABLE users (
  user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  username VARCHAR(50) NOT NULL UNIQUE,
  email VARCHAR(255) UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  full_name VARCHAR(100),
  role VARCHAR(32), -- 'local_manager', 'store_manager', 'technician', 'super_admin'
  scope_id VARCHAR, -- 관리 대상 ID (LocalAreaID or StoreID or DeviceID)
  status VARCHAR(32) DEFAULT 'active', -- active, suspended
  last_login_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
  -- CONSTRAINT: scope_id는 role에 따라 동적으로 참조되므로 DB 레벨 FK는 생략하거나 다중 컬럼 사용 고려
);
```

-- 8) user_activity_logs (Audit)
```sql
CREATE TABLE user_activity_logs (
  log_id BIGSERIAL PRIMARY KEY,
  user_id UUID NOT NULL,
  action_type VARCHAR(64) NOT NULL, -- CREATE_CONTENT, LOGIN ...
  target_entity VARCHAR(64), -- content, device
  target_id VARCHAR,
  details JSONB,
  created_at TIMESTAMPTZ DEFAULT now(),
  CONSTRAINT fk_logs_user FOREIGN KEY(user_id) REFERENCES users(user_id)
);
CREATE INDEX idx_logs_user_created ON user_activity_logs(user_id, created_at DESC);
```

## 추가 권장 사항
- package_contents.position을 이용해 패키지 내 콘텐츠 순서 보장.
- 대량 조회 성능 향상을 위해 아래 인덱스 고려:
  - `packages(product_id, published)`
  - `devices(store_id, product_id)`
- `contents.title`는 JSONB이므로 언어별 검색을 위해 GIN 인덱스 및 expression index 사용 가능.

## 무결성·운영 고려사항
- 외래키 제약은 개발 단계에서 유효하지만, 대규모 마이그레이션/성능 티어에서는 어플리케이션 레벨 검증과 병행할 수 있음.
- `package.published` 전환 시 무결성(체크섬·서명) 검사 프로세스를 강제하세요.
- `LocalArea.parent_local_area_id` 순환 방지를 위해 트리 검증 로직 필요.

---
원하시면 ERD(mermaid) 다이어그램, MySQL 또는 다른 DB 타깃용 변환(SQL) 또는 마이그레이션 예시(DDL 스크립트 + 간단한 트랜잭션 흐름)를 추가로 생성해 드리겠습니다.