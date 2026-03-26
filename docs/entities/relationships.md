# 엔티티 관계(Overview)

이 문서는 CMS 내 주요 엔티티들 간의 상관관계와 기본 흐름을 정리합니다. 관련 엔티티 정의는 다음 파일을 참고하세요:
- [Content 엔티티](docs/entities/content.md)
- [Package 엔티티](docs/entities/package.md)
- [Product 엔티티](docs/entities/product.md)
- [Device 엔티티](docs/entities/device.md)
- [Store 엔티티](docs/entities/store.md)
- [LocalArea 엔티티](docs/entities/localarea.md)

## 핵심 관계 요약
- User vs Resources (관리 주체와 대상)
  - `User`는 시스템의 운영자/관리자이며, `User`와 나머지 엔티티(`Product`, `Store`, `Device` 등)는 **직접적인 소유 관계가 아닌 관리/피관리 관계**입니다.
  - 사용자는 권한에 따라 리소스를 생성/수정하며, 이 행위는 `UserActivityLogs`에 기록됩니다.
- Product 1:N Package
  - 한 `Product`는 여러 `Package`를 가질 수 있습니다. 패키지는 해당 제품의 콘텐츠 묶음 단위입니다.
- Package N:M Content
  - `Package`는 여러 `Content`를 포함하고, 하나의 `Content`는 여러 `Package`에서 재사용될 수 있습니다.
- Device N:M Product
  - 하나의 물리적 `Device`는 여러 `Product`(소프트웨어)를 실행할 수 있습니다. `device_products` 테이블에서 디바이스별로 설치된 제품 목록과 활성 패키지를 관리합니다.
  - 예: 한 대의 키오스크가 `SandCraft`와 `FishWorld`를 모두 지원.
- Store 1:N Device
  - 하나의 `Store`(지점)는 여러 `Device`를 가질 수 있으며, `Device`는 소속 `storeId`를 가집니다.
- LocalArea 1:N Store
  - 지역(`LocalArea`)은 여러 `Store`를 포함하며 계층 구조(`parentLocalAreaId`)를 통해 범위를 정의합니다.

## 관계 다이어그램(텍스트)
Product
  ├─ Package (1:N)
  │    └─ Content (N:M)
  └─ Device (N:M, via device_products)

Store
  └─ Device (1:N)
LocalArea
  └─ Store (1:N)

(실제 배포/조회 시에는 위 관계들이 조합되어 동작합니다 — 예: 특정 LocalArea 내 Store들의 Device에 Product의 특정 Package를 게시)

## 대표 운영 흐름 예시
1. 운영자가 `Content`를 등록하고 메타·무결성(`checksum`)을 설정합니다. ([docs/entities/content.md](docs/entities/content.md))
2. 콘텐츠를 묶어 `Package`를 생성합니다. 패키지는 여러 `contentId`를 포함합니다. (`contents` 필드) ([docs/entities/package.md](docs/entities/package.md))
3. `Package`를 `Product`에 연결하거나 `Product`의 기본 패키지로 설정합니다. ([docs/entities/product.md](docs/entities/product.md))
4. 패키지를 게시(`published=true`)하면 클라이언트가 해당 패키지의 콘텐츠 목록을 조회할 수 있습니다. ([docs/entities/package.md](docs/entities/package.md))
5. `Device`는 서버에서 패키지 정보를 조회하고, 필요한 개별 콘텐츠를 다운로드하여 실행합니다. (`Device`는 `storeId`·`mac` 등으로 인증/식별) ([docs/entities/device.md](docs/entities/device.md), [docs/entities/store.md](docs/entities/store.md))

## 제약·유효성 포인트
- Referential integrity: `productId`, `contentId`, `packageId`, `localAreaId`, `storeId`, `deviceId`는 참조 무결성이 보장되어야 합니다.
- 순환 금지: `LocalArea.parentLocalAreaId`는 순환 참조를 허용하지 않아야 합니다.
- 게시 정책: `Package.published` 상태 전환 시 무결성 검사(체크섬/서명)와 검토 절차 필요.
- 다중 매핑: 콘텐츠 재사용으로 인해 패키지 간 의존성·호환성(예: `Content` 타입, entryPoint 호환성)을 관리해야 합니다.

## 구현/운영 팁
- 쿼리 효율: 특정 `LocalArea`의 모든 `Device`를 찾으려면 `LocalArea -> Store -> Device` 경로를 따라 집계 쿼리를 구성하세요.
- 콘텐츠 관리: 패키지는 메타데이터이며 실제 배포는 개별 콘텐츠 단위로 이루어집니다. 디바이스는 패키지 정보를 참조하여 다운로드할 콘텐츠를 결정합니다.
- 인증 흐름: `Device.mac`(최대 2개) 또는 `deviceId` 기반 인증을 적용하고, 패키지 다운로드 권한은 게시 상태와 스토어/제품 매핑으로 제어하세요.

---
문서를 더 기술적으로 확장(ERD, SQL 예시, API 엔드포인트 매핑)하길 원하시면 말씀해 주세요. 