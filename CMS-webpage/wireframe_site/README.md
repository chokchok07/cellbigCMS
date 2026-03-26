# Wireframe Static Site

간단한 정적 사이트로 `CMS-webpage/wireframe` 폴더의 각 화면을 HTML/CSS로 구현한 예시입니다.

## 실행 방법

Python 3가 설치되어 있다면:

```powershell
# 프로젝트 루트에서
cd CMS-webpage/wireframe_site
python -m http.server 8000
```

브라우저에서 http://localhost:8000 로 접속하세요.

## 생성된 파일

- `index.html` - 메인 페이지
- `dashboard.html` - 대시보드
- `content-list.html` - 콘텐츠 리스트
- `content-editor.html` - 콘텐츠 에디터
- `version-register.html` - 버전 등록
- `product-list.html` - 제품 리스트
- `product-detail.html` - 제품 상세
- `product-editor.html` - 제품 등록/편집
- `package-list.html` - 패키지 리스트
- `package-editor.html` - 패키지 등록/편집
- `package-detail.html` - 패키지 상세
- `device-list.html` - 디바이스 리스트
- `device-detail.html` - 디바이스 상세
- `styles.css` - 공통 스타일

## 추가 개선 가능 사항

- 실제 에디터(예: TinyMCE, Quill) 통합
- React/Vue 같은 SPA로 변환
- API 연동
- 상태 관리 추가
