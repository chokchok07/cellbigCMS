# `Package` 엔티티 정의

## 개요
`Package`는 하나의 `Product` 내부에서 콘텐츠를 묶는 단위입니다. 패키지는 특정 디바이스에서 작동 가능한 콘텐츠의 리스트를 정의하며, 제품의 구성 요소를 그룹화하는 역할을 합니다.

## 주요 속성
- `packageId` (string, PK): 패키지의 고유 식별자. 시스템에서 패키지를 유일하게 식별하며 조회·권한 부여에 사용됩니다.
- `productId` (string, FK): 이 패키지가 속한 제품의 ID. 해당 `productId`가 존재하는 Product를 참조해야 하며 제품 단위로 패키지를 그룹화합니다.
- `name` (string): 사람이 읽을 수 있는 패키지명(예: "11종", "Full Edition"). UI와 로그에 표시되며 운영자가 패키지를 식별하는 데 사용됩니다.
- `description` (string, optional): 패키지에 대한 추가 설명(포함 콘텐츠 요약, 대상 장치 등).
- `contents` (array of string `contentId`): 패키지에 포함된 콘텐츠 ID 목록. 각 `contentId`는 등록된 `Content` 엔티티를 참조하며, 이 순서 또는 구성에 따라 디바이스에서 사용 가능한 콘텐츠를 정의합니다.
- `published` (boolean, optional): 패키지 게시 여부. `true`이면 클라이언트가 조회 가능한 게시 상태입니다.



## DB Schema

`sql
CREATE TABLE packages (
  package_id VARCHAR PRIMARY KEY,
  product_id VARCHAR REFERENCES products(product_id),
  name TEXT NOT NULL,
  description TEXT,
  status VARCHAR(20) DEFAULT 'draft',
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);
`

## 관계
- Package N:1 Product — 패키지는 하나의 제품에 속함.
- Package N:M Content — 패키지는 여러 콘텐츠를 포함하며, 콘텐츠는 다수의 패키지에 재사용될 수 있음.

## 용도 및 사용 사례
- 운영자는 특정 디바이스 요구에 맞춰 패키지를 구성(예: 기능 제한판, 전체판)하고, `published` 상태로 가용성을 관리합니다.
- 클라이언트는 패키지의 `published` 여부를 기반으로 사용 가능한 콘텐츠 목록을 확인합니다.
- 패키지는 배포 단위가 아니며, 디바이스에서 실행 가능한 콘텐츠의 묶음을 표현합니다.

## 예시 JSON
```json
{
  "packageId":"pkg-sand-11",
  "productId":"product-sandcraft",
  "name":"SandCraft - 11 Items",
  "contents":["c-sand-01","c-sand-02"],
  "published":true
}
```
  "contents":["c-sand-01","c-sand-02"],
  "published":true
}
```

## 유효성 규칙
- `packageId`는 유일해야 하며, `productId`가 존재하는 Product를 참조해야 합니다.
- `contents` 배열의 각 `contentId`는 등록된 `Content` 엔티티를 참조해야 하며, 유효성 검사가 필요합니다.
- `published`는 boolean이며, `true`로 설정하기 전에 콘텐츠 구성의 무결성과 적절한 검토 프로세스를 통과해야 합니다.

## 패키지 관리 전략
- 패키지는 게시 단위로 관리하며, 클라이언트는 `published`가 `true`인 패키지를 조회하여 사용 가능한 콘텐츠 목록을 확인합니다.
- 콘텐츠 무결성(해시/디지털 서명) 검증은 개별 콘텐츠 단위로 수행됩니다.
- 패키지 변경 시 새로운 패키지로 관리하거나 기존 패키지의 contents 배열을 수정할 수 있습니다.

## 주의사항
- 패키지는 배포 단위가 아니며, 콘텐츠의 논리적 그룹화를 위한 메타데이터입니다.
- `published` 상태는 보안 검토(권한·라이선스 점검) 후에만 변경하세요.
- 패키지의 `contents`가 외부 리소스를 참조하는 경우, 해당 리소스의 가용성을 고려하여 패키지 구성의 유효성을 확보하세요.
- 디바이스는 패키지가 아닌 개별 콘텐츠를 다운로드하고 실행합니다. 패키지는 어떤 콘텐츠들이 함께 제공되는지를 나타내는 메타데이터입니다.
