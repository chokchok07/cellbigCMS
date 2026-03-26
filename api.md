# CMS API Specifications (UI-DB Sync)

본 문서는 UI/UX의 변경사항이 즉각적으로 반영되는 통합 API 명세서입니다. 변경사항(Zipcode, Timezone 제거 등)이 모두 적용되었습니다.

## 1. LocalArea API
`POST/PUT /api/localareas`
```json
{
  "name": "Seoul",
  "description": "서울 권역",
  "country_code": "KR"
}
```

## 2. Store API
`POST/PUT /api/stores`
```json
{
  "name": "Gangnam Store",
  "local_area_id": "area-seoul-01",
  "address": {"street": "강남대로 123"},
  "status": "active"
}
```

## 3. Device API
`POST/PUT /api/devices`
```json
{
  "name": "Device-A",
  "description": "강남 1호점 메인 디스플레이",
  "store_id": "store-gangnam-01",
  "mac_addresses": ["00:1A:2B:3C:4D:5E", ""],
  "status": "online",
  "meta": {
    "cpu": "Intel Core i7-12700",
    "gpu": "NVIDIA RTX 3060",
    "ram": "16GB",
    "disk_free": "450 GB",
    "os_version": "Windows 10 Pro IoT",
    "resolution": "1920x1080"
  }
}
```

## 4. Product API
`POST/PUT /api/products`
```json
{
  "name": "SandCraft",
  "description": "샌드크래프트 제품군",
  "default_package_id": "pkg-sand-11",
  "status": "published"
}
```

## 5. Package API
`POST/PUT /api/packages`
```json
{
  "product_id": "product-sandcraft",
  "name": "SandCraft - 11 Items",
  "description": "샌드크래프트 기본 11종 콘텐츠 패키지",
  "status": "published"
}
```

## 6. Content API
`POST/PUT /api/contents`
```json
{
  "title": "Sand Animation 01",
  "content_type": "video",
  "description": "모래 애니메이션 비디오",
  "status": "published"
}
```

