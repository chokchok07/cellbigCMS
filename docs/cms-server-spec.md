# CMS 서버 개발자 기획서

## 목적
CMS 서버는 콘텐츠 메타데이터·패키지·디바이스 정보를 중앙에서 관리하고, 디바이스(콘텐츠 클라이언트)에 콘텐츠 인증·다운로드 정보·버전 관리를 제공합니다.

## 핵심 책임
- 콘텐츠·패키지 CRUD 및 버전관리
- 디바이스 등록·인증·자격 관리
- 콘텐츠 다운로드 정보 제공(다운로드 URL, 서명/해시 제공)
- 실행·인증 로그 수집(사용 통계, 실행 횟수)
- 관리 UI(운영자용)와 REST/HTTPS API 제공

## 주요 도메인 모델 (Overview.md 기반)
- Product: 제품 단위(여러 어플리케이션 포함)
- Package: Product 내 콘텐츠 그룹, `packageId`
- Content: 개별 콘텐츠, `contentId`, 타입(단독/컨테이너/하위/혼합)
- Device: 설치된 물리 장치, `deviceId`, MAC 등 식별자

## 인증 방식
- 상시 인증: 클라이언트가 콘텐츠 실행 시마다 `contentId` + PC MAC으로 서버에 인증 요청.
- One-time 인증: 최초 실행 시 1회 인증(오프라인/제한적 네트워크 환경 대응).
- 권장: JWT 기반 액세스 토큰(만료 포함) + 서버 측 실행 로그 기록.

## 주요 API (권장 엔드포인트 예시)
- POST /api/devices/register — 디바이스 등록 (payload: deviceId, mac, productId)
- POST /api/auth/verify — 인증(상시/one-time) (payload: contentId, deviceId, mac)
- GET /api/packages/{packageId} — 패키지 메타데이터(버전, 포함된 contentId 목록)
- GET /api/content/{contentId}/download — 콘텐츠 다운로드 메타(서명, 해시, CDN URL)
- GET /api/products — 제품 목록 및 메타
- GET /api/telemetry/config — 클라이언트 전송 설정

## 데이터 모델 예시 (요약)
```json
{
  "device": {"deviceId":"...","mac":"...","productId":"..."},
  "package": {"packageId":"...","version":"1.2.0","contents":["c1","c2"]},
  "content": {"contentId":"...","type":"container|single","hash":"..."}
}
```

## 보안·무결성
- 파일 다운로드 전 서버가 제공하는 해시/서명으로 무결성 검사 수행.
- 전송은 HTTPS 필수, 서명에선 권장 대칭/비대칭 결합 사용.
- 권한: 운영자 UI는 RBAC 적용(콘텐츠 생성/삭제 등 권한 구분).

## 운영·배포
- CDN 사용 권장: 대용량 콘텐츠를 위해 S3/Blob + 서명된 URL 제공.
- 롤링·버전 전략: 패키지에 버전 필드 포함, 클라이언트는 버전 비교 후 업데이트.
- 로그·모니터링: 인증/다운로드/에러 이벤트는 중앙 로깅(예: ELK, Prometheus)으로 전송.

## 테스트·검증
- 유닛: 메타데이터 변환, 권한 검사, 인증 로직
- 통합: 기기 등록 → 인증 → 다운로드 흐름 시뮬레이션
- 부하: 동시 디바이스 인증/다운로드 시나리오(다운로드는 CDN 분리)

## 운영자 가이드(간단)
- 콘텐츠 업로드 → 패키지 생성/버전 지정 → 게시(게시 후 클라이언트가 새 버전 감지)
- 긴급 롤백: 이전 패키지 버전으로 마킹 후 클라이언트는 버전 확인 시 롤백 적용

## 추가 고려사항
- 오프라인 환경 지원: One-time 인증 토큰 발급·갱신 정책
- 멀티-디바이스 제품: 하나의 Product가 여러 Device로 구성되는 경우 동기화 고려
- 메타데이터 마이그레이션/백업 절차 문서화

---

참고: 핵심 도메인과 인증 방식은 [Overview.md](../Overview.md#L1)와 일치해야 합니다.
