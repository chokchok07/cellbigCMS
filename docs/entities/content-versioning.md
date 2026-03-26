# Content 버전 관리 요구사항

## 개요
CMS에서 `Content`는 버전 단위로 관리해야 하며, 클라이언트(Device)는 CMS의 최신 배포 버전과 로컬에 설치된 버전을 비교하여 업데이트를 수행합니다. 이 문서는 필요 요소(데이터 모델, API, 클라이언트 흐름, 보안·운영 요구사항)를 정리합니다.

## 핵심 요구사항 요약
- 버전은 불변(immutable)으로 관리: 기존 버전 변경 대신 새 버전 생성
- 게시 상태(`draft`, `staged`, `published`)를 통해 배포 가시성 제어
- 아티팩트(패키지) 무결성 확인을 위한 `checksum`(SHA-256) 필수
- 디바이스는 빠른 비교를 위해 `version_tag` 또는 `checksum`을 보고
- 롤아웃(캔버리·페이즈드)과 롤백 지원

## 데이터 모델(권장)
- `contents` 테이블: 기본 메타(식별자·타이틀 등)
- `content_versions` 테이땠(새로 추가)
  - `content_version_id` (PK)
  - `content_id` (FK -> contents.content_id)
  - `version_major` (INT): 메이저 버전 (0-999)
  - `version_minor` (INT): 마이너 버전 (0-999)
  - `version_patch` (INT): 패치 버전 (0-999)
  - `version_tag` (VARCHAR, computed): SemVer 포맷 "major.minor.patch" (예: "2.1.0")
  - `update_type` (VARCHAR): `forced` | `optional` (강제 업데이트 여부)
  - `deployment_target` (VARCHAR): `production` | `test` (배포 대상 환경)
  - `checksum` (VARCHAR): SHA-256 (ZIP 파일 전체 해시)
  - `artifact_url` (TEXT): 아티팩트 접근 URL (서명된 URL 포함)
  - `artifact_filename` (TEXT, optional): 저장소에 업로드된 zip 파일명(예: `content-101-v2.1.0.zip`).
  - `artifact_size_bytes` (BIGINT, optional): zip 파일 크기(바이트).
  - `artifact_content_type` (TEXT, optional): 아티팩트 MIME 타입(예: `application/zip`).
  - `storage_provider` (TEXT, optional): 아티팩트 저장소 식별자(S3, GCS, internal).
  - `signed_url_ttl` (INT, optional): 서명된 URL의 권한 유효 기간(초).
  - `state` (VARCHAR): `draft`|`staged`|`published`|`deprecated`
  - `release_notes` (TEXT, optional): 버전 설명 및 변경 사항
  - `created_by`, `created_at`, `meta`(jsonb)
  - UNIQUE(content_id, version_major, version_minor, version_patch)

참고: `entryPoint`는 버전과 무관하게 일정하므로 `contents` 테이블에 저장됩니다. ZIP 파일에 모든 파일이 포함되므로 별도의 assets 목록은 불필요합니다.

- `package_contents` 변경 권장
  - 기존 `content_id` 대신 `content_version_id`를 참조하여 패키지가 특정 버전의 콘텐츠를 포함함을 명시

- `device_installed_contents` (클라이언트 설치 기록, 선택)
  - `device_id`, `content_id`, `content_version_id`, `installed_at`, `status`

### 예시 DDL (PostgreSQL)
```sql
CREATE TABLE content_versions (
  content_version_id BIGSERIAL PRIMARY KEY,
  content_id BIGINT NOT NULL REFERENCES contents(content_id),
  version_major INT NOT NULL DEFAULT 0,
  version_minor INT NOT NULL DEFAULT 0,
  version_patch INT NOT NULL DEFAULT 0,
  version_tag VARCHAR GENERATED ALWAYS AS (version_major || '.' || version_minor || '.' || version_patch) STORED,
  update_type VARCHAR(32) NOT NULL DEFAULT 'optional',
  deployment_target VARCHAR(32) NOT NULL DEFAULT 'test',
  checksum VARCHAR NOT NULL,
  artifact_url TEXT,
  artifact_filename TEXT,
  artifact_size_bytes BIGINT,
  artifact_content_type TEXT DEFAULT 'application/zip',
  storage_provider TEXT,
  signed_url_ttl INT,
  state VARCHAR(32) NOT NULL DEFAULT 'draft',
  release_notes TEXT,
  meta JSONB,
  created_by VARCHAR,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now(),
  UNIQUE (content_id, version_major, version_minor, version_patch),
  CHECK (version_major >= 0 AND version_major <= 999),
  CHECK (version_minor >= 0 AND version_minor <= 999),
  CHECK (version_patch >= 0 AND version_patch <= 999),
  CHECK (update_type IN ('forced', 'optional')),
  CHECK (deployment_target IN ('production', 'test'))
);

-- package_contents가 content_version_id를 참조하도록 변경(마이그레이션 필요)
CREATE TABLE package_contents (
  package_id VARCHAR NOT NULL,
  content_version_id BIGINT NOT NULL,
  position INT DEFAULT 0,
  PRIMARY KEY (package_id, content_version_id),
  FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE,
  FOREIGN KEY (content_version_id) REFERENCES content_versions(content_version_id) ON DELETE RESTRICT
);

CREATE TABLE device_installed_contents (
  device_id VARCHAR NOT NULL,
  content_id BIGINT NOT NULL,
  content_version_id BIGINT NOT NULL,
  installed_at TIMESTAMPTZ DEFAULT now(),
  status VARCHAR(32),
  PRIMARY KEY (device_id, content_id, content_version_id)
);
```

## API (권장 엔드포인트)
- `GET /contents/{contentId}/latest` : 최신 `published` 버전 메타 반환 (version_tag, checksum, artifact_url, published_at, release_notes)
- `GET /contents/{contentId}/versions` : 버전 히스토리(필터: state), release_notes 포함
- `POST /contents/{contentId}/versions` : 새 버전 생성 (version_major/minor/patch, update_type, deployment_target, artifact, release_notes 포함)
- `POST /contents/{contentId}/publish` : 특정 버전 게시 (권한 필요, 무결성 검증 트리거)
- `POST /devices/{deviceId}/check` : 디바이스가 현재 설치된 콘텐츠/버전을 전송하면, 서버가 업데이트 필요 항목 반환
- `POST /devices/{deviceId}/report` : 설치 결과/상태 보고

### API 요청/응답 예시

**새 버전 생성 요청**
```json
POST /contents/101/versions
{
  "version_major": 2,
  "version_minor": 1,
  "version_patch": 0,
  "update_type": "optional",
  "deployment_target": "test",
  "artifact_url": "https://storage.example.com/content-101-v2.1.0.zip",
  "checksum": "abcd1234...",
  "artifact_filename": "content-101-v2.1.0.zip",
  "artifact_size_bytes": 47448064,
  "release_notes": "버그 수정: 로그인 오류 해결, 새 기능: 다크 모드 지원",
  "state": "draft"
}
```

**버전 히스토리 응답**
```json
GET /contents/101/versions
{
  "versions": [
    {
      "content_version_id": 501,
      "version_tag": "2.1.0",
      "version_major": 2,
      "version_minor": 1,
      "version_patch": 0,
      "update_type": "optional",
      "deployment_target": "test",
      "state": "published",
      "release_notes": "버그 수정: 로그인 오류 해결, 새 기능: 다크 모드 지원",
      "artifact_size_bytes": 47448064,
      "created_at": "2026-02-12T10:00:00Z",
      "created_by": "admin@example.com"
    },
    {
      "content_version_id": 500,
      "version_tag": "2.0.0",
      "version_major": 2,
      "version_minor": 0,
      "version_patch": 0,
      "update_type": "forced",
      "deployment_target": "production",
      "state": "published",
      "release_notes": "초기 버전",
      "created_at": "2026-01-15T10:00:00Z",
      "created_by": "admin@example.com"
    }
  ]
}
```

## 클라이언트(디바이스) 동작 플로우
1. 서버에 `GET /contents/{contentId}/latest` 또는 `POST /devices/{deviceId}/check` 호출
2. 서버 응답의 `version_tag` 또는 `checksum`과 로컬 설치값 비교
3. 불일치 시 `artifact_url`로 다운로드
4. 다운로드 대상은 압축된 ZIP 아티팩트(예: `application/zip`)입니다. 클라이언트는 다음을 지켜야 합니다:
  - 임시 디렉터리에 안전하게 다운로드(가능하면 Range 요청/재개 지원).
  - 다운로드 완료 후 서버가 제공한 `checksum`(SHA-256)으로 무결성 검증(필수).
  - ZIP 압축 해제는 원자적 교체(예: 임시 폴더 → 검증 → swap)로 수행.
  - `contents` 테이블의 `entryPoint`를 참조하여 실행.
5. 설치 수행 후 `POST /devices/{deviceId}/report`로 결과 전송(성공/실패/체크섬 불일치 등 상세 상태 포함)

권장: 디바이스는 다운로드 전에 충분한 디스크/권한·대역폭을 체크하고, 실패 시 지수 백오프 재시도

## 무결성·보안 요구사항
- 아티팩트는 SHA-256 등으로 무결성 체크; 가능하면 디지털 서명 적용
- 아티팩트 접근은 서명된 URL 또는 토큰 기반 인증으로 제한
- 아티팩트는 ZIP 파일 형태로 업로드되며, `checksum`은 ZIP 파일 전체에 대해 계산합니다.
- 클라이언트는 ZIP의 무결성 검증 후 압축 해제하여 `contents.entryPoint`로 실행합니다.
- `published` 전환 시 자동화된 무결성 검사(체크섬 일치, 권한 검토) 실행

## 운영·배포 정책
- 롤아웃 전략: Canary → Phased → Full
  - 타게팅: `LocalArea`, `Store`, `Product`, `Device` 태그 기반
- 롤백: 이전 `published` 상태로 즉시 복원 가능하도록 아티팩트 및 메타 보존
- 보존 정책: 오래된 버전 보존 기간·아카이브 정책 정의

## 모니터링·메트릭
- 버전별 설치율(성공/실패), 평균 배포 시간, 실패 원인(체크섬 불일치, 네트워크 등)
- 알람: 무결성 실패, 서명 실패, 높은 실패율

## CI/CD와 릴리즈 파이프라인
- 빌드 → checksum 생성 → 아티팩트 업로드 → `POST /contents/{contentId}/versions`로 버전 생성(release_notes 포함) → 자동 스테이징 → 자동/수동 테스트 → publish
- publish 단계에서 DB에 `content_versions` 레코드 추가 및 `state=published` 전환
- release_notes는 변경 내용 및 배포 이력 추적용으로 활용

## 데이터 마이그레이션 고려사항
- 기존 `contents.version` 필드를 `content_versions`로 이전하는 마이그레이션 스크립트 필요
- 기존 패키지-콘텐츠 매핑을 `package_contents`(content_version_id)로 매핑
- 마이그레이션은 트랜잭션 및 점진적 전환(핀된 트래픽에서 검증 후 전면 전환)을 권장

## 예시 운영 시나리오
- 신규 콘텐츠 빌드: CI가 `artifact` 업로드 → `content_versions` 생성(state=`draft`, release_notes 입력) → 내부 리뷰 및 승인 → state=`staged`로 변경 → QA 승인 → `publish` → 일부 디바이스(캔버리)에서 자동 업데이트 확인 → 전면 롤아웃
- 버전 히스토리 조회 시 release_notes를 통해 변경 내용 및 배포 사유 확인 가능

---
원하시면 이 문서를 `docs/entities/content.md`의 버전 관리 섹션으로 통합하거나, `docs/entities/db-schema.md`에 `content_versions` DDL을 병합해 드리겠습니다.