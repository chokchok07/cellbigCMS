# `Product` 엔티티 정의

## 개요
`Product`는 CMS에서 관리하는 제품 단위입니다. 하나의 `Product`는 하나 이상 어플리케이션(콘텐츠)을 포함하며, 납품 단위 또는 설치 대상 제품을 나타냅니다.

## 주요 속성
- `productId` (string, PK): 제품 고유 ID
- `name` (string): 제품명
- `description` (string): 제품 설명
- `packages` (array of `packageId`): 이 제품에 적용 가능한 패키지 목록
- `defaultPackageId` (string): 기본 제공 패키지
- `createdAt` / `updatedAt` (datetime)


## DB Schema

`sql
CREATE TABLE products (
  product_id VARCHAR PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT,
  default_package_id VARCHAR,
  status VARCHAR(20) DEFAULT 'published',
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);
`

## 관계
- Product 1:N Package — 하나의 제품에 여러 패키지가 존재할 수 있음.
- Product 1:N Device — 하나의 제품이 여러 디바이스 인스턴스로 설치될 수 있음.

## 용도 및 사용 사례
- 운영자는 새로운 `Product`를 등록하고, 관련 `Package`를 생성하여 배포 단위를 관리합니다.
- 클라이언트는 `productId`를 통해 설치된 제품의 기본 패키지 또는 선택 패키지를 조회합니다.

## 예시 JSON
```json
{
  "productId":"product-sandcraft",
  "name":"SandCraft",
  "description":"샌드 크래프트 제품군",
  "packages":["pkg-sand-11","pkg-sand-24"],
  "defaultPackageId":"pkg-sand-11",
  "createdAt":"2026-02-05T10:00:00Z"
}
```

## 유효성 규칙
- `productId`는 유일해야 하며 불변(immutable)으로 관리.
- `packages`에 참조된 `packageId`는 존재해야 함.

## 라이프사이클
- 생성 → 패키지 연결 → 패키지 게시 → 필요 시 콘텐츠 업데이트 및 패키지 구성 변경

## 주의사항
- 제품의 구조(하위 콘텐츠 포함 여부)는 `Content` 타입 정의와 일치해야 합니다.
