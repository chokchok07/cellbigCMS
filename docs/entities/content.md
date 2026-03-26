# `Content` 엔티티 정의

## 개요
`Content`는 CMS가 관리하는 개별 콘텐츠 어플리케이션 단위입니다. 콘텐츠는 단독으로 동작하거나, 다른 콘텐츠를 포함하는 컨테이너 형태일 수 있습니다.
 
참고: 콘텐츠 버전/아티팩트 관리는 [docs/entities/content-versioning.md](docs/entities/content-versioning.md) 를 따릅니다.

## 주요 속성

### contents 테이블 (콘텐츠 메타데이터)
- `contentId` (int, PK): 콘텐츠 고유 ID
- `title` (string | object): 콘텐츠 제목(단일 문자열 또는 BCP-47 키를 사용하는 다국어 객체)
- `description` (string | object, optional): 콘텐츠 설명(최대 255자 권장). 다국어 표현은 `title`과 동일한 규칙을 따릅니다
- `thumbnail` (string, optional): 콘텐츠 썸네일 이미지 URL
- `category` (string, optional): 콘텐츠 카테고리
- `type` (enum): `single` | `container` | `child` | `mixed`
- `productId` (int, FK, optional): 소속 제품
- `entryPoint` (string, optional): ZIP 내부의 실행 시작점 경로 (예: `/app/sand/beach.exe`). `container` 타입은 생략 가능
- `createdAt` / `updatedAt`

### content_versions 테이블 (버전별 아티팩트 - docs/entities/content-versioning.md 참고)
- `version_major`, `version_minor`, `version_patch` (int): 시맨틱 버저닝
- `version_tag` (string, computed): "major.minor.patch" 형식
- `artifact_url` (string): 아티팩트 다운로드 URL
- `artifact_filename` (string): ZIP 파일명
- `artifact_size_bytes` (bigint): 파일 크기
- `artifact_content_type` (string): MIME 타입 (예: `application/zip`)
- `checksum` (string): SHA-256 해시 (ZIP 파일 전체)
- `update_type` (enum): `forced` | `optional`
- `deployment_target` (enum): `production` | `test`
- `state` (enum): `draft` | `staged` | `published` | `deprecated`
- `release_notes` (text): 버전 설명

### 레거시 필드 (하위 호환성)
- `version` (string, optional, legacy): 기존 호환성용 버전 필드. → `content_versions` 테이블 사용 권장
- `packageFormat` (string, optional, legacy): → `content_versions.artifact_content_type` 사용 권장
- `checksum` (string, optional, legacy): → `content_versions.checksum` 사용 권장

## 속성 상세 설명

### contents 테이블 속성

**title (string | object)**
콘텐츠 제목. 단일 문자열 또는 BCP-47 언어 코드를 키로 하는 다국어 객체. 예: `{"ko":"제목","en":"Title"}`

**type (enum)**
- `single`: 단독 실행 가능 콘텐츠
- `container`: 하위 콘텐츠를 관리하는 상위 콘텐츠
- `child`: 컨테이너에 의해 관리되는 단일 콘텐츠
- `mixed`: 컨테이너 역할과 하위를 함께 포함하는 배포형

**entryPoint (string, optional)**
콘텐츠 시작점(실행 파일 경로, 런처 식별자). ZIP 패키지 내부의 상대 경로(예: `/app/sand/beach.exe`)를 권장합니다. 모든 버전에서 동일한 경로를 사용하므로 `contents` 테이블에 저장됩니다. `container` 타입 콘텐츠는 생략 가능합니다.

### content_versions 테이블 속성 (버전별 아티팩트)

**checksum (string)**
패키지(ZIP) 단위 전체 무결성 해시(SHA-256, 헥스 문자열). `content_versions` 테이블에 저장되며 버전별로 유일합니다. 클라이언트는 다운로드 후 이 값을 검증해야 합니다.

**artifact_content_type (string)**
아티팩트 MIME 타입. 기본값: `application/zip`. 레거시 `packageFormat` 필드를 대체합니다.

## 데이터 모델 구조

```
contents (콘텐츠 메타데이터)
  ├─ contentId (PK)
  ├─ title, description, thumbnail
  ├─ category, type, productId
  ├─ entryPoint (실행 시작점)
  └─ 1:N → content_versions (버전별 아티팩트 ZIP)
        ├─ content_version_id (PK)
        ├─ version_major, version_minor, version_patch
        ├─ artifact_url, artifact_filename, artifact_size_bytes
        ├─ checksum (SHA-256)
        └─ state, update_type, deployment_target
```


## DB Schema

`sql
CREATE TABLE contents (
  content_id VARCHAR PRIMARY KEY,
  title TEXT NOT NULL,
  description TEXT,
  content_type VARCHAR(50),
  status VARCHAR(20) DEFAULT 'draft',
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);
`

## 관계
- **Content 1:N ContentVersions** — 하나의 콘텐츠는 여러 버전을 가질 수 있음. 각 버전은 고유한 artifact(ZIP)와 checksum을 가지며, entryPoint는 contents 테이블에서 공통으로 관리
- **Content N:M Package** — 콘텐츠는 여러 패키지에서 재사용 가능 (정확히는 `content_version_id`를 통해 특정 버전이 패키지에 포함됨)
- **Content N:1 Product** — 콘텐츠는 특정 제품에 속함 (선택적)

## 예시 JSON

### contents 테이블 레코드
```json
{
  "contentId": 101,
  "title": {"ko":"샌드크래프트 - 해변","en":"SandCraft - Beach"},
  "description": {"ko":"해변에서 즐기는 샌드 게임","en":"Sand game on the beach"},
  "thumbnail": "https://cdn.example.com/thumbnails/sandcraft-beach.jpg",
  "category": "게임",
  "type": "single",
  "productId": 201,
  "entryPoint": "/app/sand/beach.exe",
  "createdAt": "2026-01-15T10:00:00Z",
  "updatedAt": "2026-02-12T10:00:00Z"
}
```

### content_versions 테이블 레코드 (버전 2.1.0)
```json
{
  "content_version_id": 501,
  "content_id": 101,
  "version_major": 2,
  "version_minor": 1,
  "version_patch": 0,
  "version_tag": "2.1.0",
  "artifact_url": "https://storage.example.com/content-101-v2.1.0.zip",
  "artifact_filename": "content-101-v2.1.0.zip",
  "artifact_size_bytes": 47448064,
  "artifact_content_type": "application/zip",
  "checksum": "abcd1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
  "update_type": "optional",
  "deployment_target": "test",
  "state": "published",
  "release_notes": "버그 수정: 로그인 오류 해결, 새 기능: 다크 모드 지원",
  "created_at": "2026-02-12T10:00:00Z",
  "created_by": "admin@example.com"
}
```

### API 응답 예시 (클라이언트용 - contents + latest version)
```json
{
  "contentId": 101,
  "title": {"ko":"샌드크래프트 - 해변","en":"SandCraft - Beach"},
  "type": "single",
  "productId": 201,
  "entryPoint": "/app/sand/beach.exe",
  "latestVersion": {
    "version_tag": "2.1.0",
    "artifact_url": "https://storage.example.com/content-101-v2.1.0.zip",
    "artifact_size_bytes": 47448064,
    "checksum": "abcd1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
    "update_type": "optional"
  }
}
```

## 유효성 규칙

### contents 테이블
- `contentId`: 유일해야 함 (PK)
- `title`: 문자열 또는 언어 맵(BCP-47 키)이어야 하며 최소 하나의 값 필요. 클라이언트는 언어 우선순위로 선택, 없으면 `default` 또는 지정 기본 언어 폴백 권장
- `type`: `single`, `container`, `child`, `mixed` 중 하나
- `entryPoint`: ZIP 내부 경로, 실행 가능한 파일 경로여야 함 (예: `/app/sand/beach.exe`). `container` 타입은 선택적

### content_versions 테이블
- `version_major`, `version_minor`, `version_patch`: 0-999 범위의 정수
- `checksum`: 필수, SHA-256 해시 (64자 헥스 문자열)
- `artifact_url`: 접근 가능한 URL (서명된 URL 권장)
- `artifact_content_type`: `application/zip` 고정
- `state`: `draft`, `staged`, `published`, `deprecated` 중 하나
  - `draft`: 작성 중인 버전. 관리자만 확인 가능하며 클라이언트에 배포되지 않음
  - `staged`: 테스트 준비 완료된 버전. 내부 테스트 환경에서만 사용 가능
  - `published`: 배포 완료된 버전. 클라이언트에서 다운로드 및 실행 가능
  - `deprecated`: 더 이상 사용하지 않는 버전. 클라이언트에 노출되지 않으며 기록 보관용
- `update_type`: `forced`, `optional` 중 하나
  - `forced`: 강제 업데이트. 클라이언트는 반드시 이 버전으로 업데이트해야 하며, 업데이트 전까지 콘텐츠 실행이 차단됨
  - `optional`: 선택적 업데이트. 클라이언트가 업데이트 여부를 선택할 수 있으며, 이전 버전으로도 계속 사용 가능
- `deployment_target`: `production`, `test` 중 하나

## 배포·업데이트
- 콘텐츠는 ZIP 아카이브(artifact)로 CMS에 업로드되며, `content_versions`에 아티팩트 메타(artifact_url, artifact_filename, artifact_size_bytes, checksum 등)를 저장합니다.
- 클라이언트는 `contents` 테이블에서 `entryPoint`를 조회하고, `content_versions.latest`의 `artifact_url`을 통해 ZIP을 다운로드하여 checksum을 검증한 뒤 압축을 풀어 실행합니다.
- 동일한 `checksum`이면 재다운로드를 생략하도록 클라이언트에서 캐시/체크를 구현하세요.
- ZIP 파일에는 모든 실행 파일과 리소스가 포함되므로 별도의 assets 목록 관리는 불필요합니다.
- `container` 타입은 하위 리스트 변경 시 의존성 및 호환성 검사(버전 호환성)를 수행하세요.

## 주의사항
- ZIP 파일에는 모든 실행 파일과 리소스가 포함되어야 하며, `entryPoint`는 ZIP 내부의 상대 경로로 지정합니다.
- 외부 라이브러리/플러그인 의존성이 있다면 ZIP에 포함하거나 배포 문서에 명시하세요.
- 민감 권한이 필요한 경우 문서화하고 사용자 동의 흐름을 고려할 것.
- `entryPoint` 경로 변경 시 `contents` 테이블 업데이트가 필요하며, 모든 버전에 영향을 미칩니다.
