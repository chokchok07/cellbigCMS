# Package Detail UI 와이어프레임

## 개요
- 목적: 패키지의 상세 정보를 조회하고 관리합니다.
- 접근 경로: Package List에서 [View] 버튼 클릭

## 레이아웃

```
+------------------+--------------------------------------------------+
| Sidebar          | Header: Package Detail                          |
| - Dashboard      +--------------------------------------------------+
| - Product        | [← Back to List]                    [Edit] [Delete]
| - Package ●      |                                                   |
| - Content        | Package: SandCraft - 11 Items                     |
| - Devices        | Status: 🟢 Published                             |
|                  | ID: pkg-sand-11                                   |
|                  +--------------------------------------------------+
|                  | Basic Information                                 |
|                  | ┌────────────────────────────────────────────┐  |
|                  | │ Product: SandCraft (product-sandcraft)      │  |
|                  | │ Package ID: pkg-sand-11                      │  |
|                  | │ Package Name: SandCraft - 11 Items           │  |
|                  | │ Description: 샌드크래프트 기본 11종 콘텐츠   │  |
|                  | │              패키지                          │  |
|                  | │ Status: Published                            │  |
|                  | └────────────────────────────────────────────┘  |
|                  |                                                   |
|                  | Connected Contents (11)            [Manage]       |
|                  | ┌────────────────────────────────────────────┐  |
|                  | │ Content ID          | Name                  │  |
|                  | │ c-sand-01          | Sand Animation 01      │  |
|                  | │ c-sand-02          | Sand Animation 02      │  |
|                  | │ c-sand-03          | Sand Animation 03      │  |
|                  | │ ...                 | ...                   │  |
|                  | │ c-sand-11          | Sand Animation 11      │  |
|                  | └────────────────────────────────────────────┘  |
|                  |                                                   |
|                  | Metadata                                          |
|                  | ┌────────────────────────────────────────────┐  |
|                  | │ Created: 2024-01-15 14:30:00 by admin        │  |
|                  | │ Updated: 2024-01-20 10:15:00 by admin        │  |
|                  | └────────────────────────────────────────────┘  |
+------------------+--------------------------------------------------+
```

## 주요 구성 요소

### 1. 헤더
- **[← Back to List]**: Package List로 돌아가기
- **[Edit]**: 패키지 편집 화면(package-editor)으로 이동
- **[Delete]**: 패키지 삭제 (확인 모달)
- **패키지 이름**: 현재 조회 중인 패키지 이름
- **상태 배지**: Published 🟢 / Draft 🟡

### 2. Basic Information 섹션
패키지의 기본 정보 표시 (읽기 전용)

- **Product**: 소속 제품 이름 (Product ID)
- **Package ID**: 패키지 고유 ID
- **Package Name**: 패키지 이름
- **Description**: 패키지 설명
- **Status**: Published / Draft

### 3. Connected Contents 섹션
패키지에 포함된 콘텐츠 목록 표시

- **[Manage] 버튼**: 패키지 편집 화면으로 이동하여 콘텐츠 관리
- **콘텐츠 목록 테이블**:
  - Content ID: 콘텐츠 고유 ID
  - Name: 콘텐츠 이름
- **클릭 동작**: 콘텐츠 행 클릭 시 해당 콘텐츠 상세 페이지로 이동

### 4. Metadata 섹션
패키지 메타데이터 (읽기 전용)

- **Created**: 생성 일시 및 생성자
- **Updated**: 최종 수정 일시 및 수정자

## 인터랙션 플로우

### 상세 조회
1. Package List에서 [View] 클릭
2. Package Detail 페이지 로드
3. 패키지 기본 정보, 연결된 콘텐츠, 메타데이터 표시

### 편집으로 이동
1. [Edit] 버튼 클릭
2. package-editor.html?id={packageId}로 이동

### 콘텐츠 관리
1. [Manage] 버튼 클릭
2. package-editor.html?id={packageId}로 이동하여 콘텐츠 추가/제거

### 삭제
1. [Delete] 버튼 클릭
2. 확인 모달 표시: "정말 이 패키지를 삭제하시겠습니까?"
3. 확인 시 패키지 삭제 → Package List로 복귀

### 목록으로 복귀
1. [← Back to List] 클릭
2. Package List 페이지로 이동

## 비즈니스 로직

1. **패키지 조회**: GET /api/packages/{packageId}
   - 패키지 기본 정보, 연결된 콘텐츠 목록, 메타데이터 조회
2. **콘텐츠 목록 표시**: contents 배열을 테이블로 렌더링
3. **상태 표시**: published 값에 따라 배지 색상 변경
4. **권한 확인**: 편집/삭제 권한이 없으면 버튼 비활성화

## 데이터 소스
- Package 엔티티: packageId, productId, name, description, contents, published
- Product 엔티티: 제품명 표시를 위해 productId로 조회
- Content 엔티티: 콘텐츠 이름 표시를 위해 contentId로 조회

## 추가 고려사항
- 콘텐츠 목록이 많을 경우 페이지네이션 또는 가상 스크롤 적용
- Published 패키지는 클라이언트가 조회 가능한 상태임을 명시
- 콘텐츠 클릭 시 해당 콘텐츠 상세 페이지로 이동 (선택 사항)

## 관련 페이지
- [Package List](./package-list.md) - 패키지 목록 페이지
- [Package Editor](./package-editor.md) - 패키지 편집 페이지
