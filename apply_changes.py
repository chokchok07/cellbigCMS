import re
import os

with open('api.md', 'r', encoding='utf-8') as f:
    text = f.read()
    
new_text = re.sub(
    r'("store_id": "store-gangnam-01",\s*"mac_addresses": \["00:1A:2B:3C:4D:5E", ""\],)',
    r'\1\n    "products": [\n      {\n        "product_id": "prod-01",\n        "installed_package_id": "pkg-sand-11"\n      }\n    ],',
    text
)

with open('api.md', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated api.md")

html_path = 'CMS-webpage/wireframe_site/device-editor.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the single card with 4 separated cards
# Target the content grid left column
start_marker = r'<!-- Left Column: Basic Info -->.*?<div class="card" style="margin-bottom: 24px;">'
end_marker = r'// Init\s*document.addEventListener\(\'DOMContentLoaded\', toggleLicenseContainer\);\s*</script>\s*</div>\s*</div>\s*</div>'

new_html_content = """<!-- Left Column -->
          <div>
            <!-- Card 1: Basic Info -->
            <div class="card" style="margin-bottom: 24px;">
              <h2 style="font-size: 18px; color: #111827; margin-top: 0; margin-bottom: 20px; border-bottom: 1px solid #e5e7eb; padding-bottom: 12px;">📋 (1/3) 기본 정보</h2>
              <div style="display: flex; flex-direction: column; gap: 16px;">
                <div class="form-group">
                  <label class="form-label required">Name (이름)</label>
                  <input type="text" class="input" style="width:100%" value="" placeholder="예: 강남 1호점 메인 디스플레이">
                </div>
                <div class="form-group">
                  <label class="form-label required">MAC Address (기기 식별자)</label>
                  <input type="text" class="input" style="width:100%; font-family:monospace" value="" placeholder="예: 00:1A:2B:3C:4D:5E">
                </div>
              </div>
            </div>

            <!-- Card 2: Location -->
            <div class="card" style="margin-bottom: 24px;">
              <h2 style="font-size: 18px; color: #111827; margin-top: 0; margin-bottom: 20px; border-bottom: 1px solid #e5e7eb; padding-bottom: 12px;">🏢 (2/3) 지점 설정 (위치)</h2>
              <div style="display: flex; flex-direction: column; gap: 16px;">
                <div class="form-group">
                  <label class="form-label required">LocalArea (권역)</label>
                  <input type="text" list="localarea-list" class="input" style="width:100%; border:1px solid #d1d5db; border-radius:6px; padding:8px 12px;" placeholder="권역명을 검색하거나 선택하세요...">
                  <datalist id="localarea-list">
                    <option value="Seoul (서울)"></option>
                    <option value="Busan (부산)"></option>
                    <option value="Jeju (제주)"></option>
                  </datalist>
                </div>
                <div class="form-group">
                  <label class="form-label required">Stores (매장)</label>
                  <input type="text" list="store-list" class="input" style="width:100%; border:1px solid #d1d5db; border-radius:6px; padding:8px 12px;" placeholder="매장명을 검색하거나 선택하세요...">
                  <datalist id="store-list">
                    <option value="store-01 (서울 강남 직영점)"></option>
                    <option value="store-02 (서울 홍대 직영점)"></option>
                    <option value="store-03 (부산 해운대점)"></option>
                  </datalist>
                  <div style="font-size:12px; color:#6b7280; margin-top:4px;">* 위에서 선택한 LocalArea에 파생되는 매장 목록만 표시됩니다.</div>
                </div>
              </div>
            </div>

            <!-- Card 3: Product -->
            <div class="card" style="margin-bottom: 24px;">
              <h2 style="font-size: 18px; color: #111827; margin-top: 0; margin-bottom: 20px; border-bottom: 1px solid #e5e7eb; padding-bottom: 12px;">📦 (3/3) 상품 설정</h2>
              <div style="display: flex; flex-direction: column; gap: 16px;">
                <div class="form-group">
                  <label class="form-label required">Product (상품)</label>
                  <input type="text" list="product-list" class="input" style="width:100%; border:1px solid #d1d5db; border-radius:6px; padding:8px 12px;" placeholder="상품 검색어 (ID 또는 이름) 입력...">
                  <datalist id="product-list">
                    <option value="prod-01 (Product A)"></option>
                    <option value="prod-02 (Product B)"></option>
                  </datalist>
                </div>
                <div class="form-group">
                  <label class="form-label required">Package (콘텐츠 패키지)</label>
                  <input type="text" list="package-list" class="input" style="width:100%; border:1px solid #d1d5db; border-radius:6px; padding:8px 12px;" placeholder="패키지 버전 검색 또는 선택...">
                  <datalist id="package-list">
                    <option value="pkg-01 (Package v1.0)"></option>
                    <option value="pkg-02 (Package v2.0)"></option>
                  </datalist>
                  <div style="font-size:12px; color:#6b7280; margin-top:4px;">* 선택한 상품의 하위 패키지가 노출됩니다.</div>
                </div>
              </div>
            </div>

            <!-- Card 4: Auth -->
            <div class="card" style="margin-bottom: 24px;">
              <h2 style="font-size: 18px; color: #111827; margin-top: 0; margin-bottom: 20px; border-bottom: 1px solid #e5e7eb; padding-bottom: 12px;">🔑 인증 모드 / 라이선스</h2>
              <div style="display: flex; flex-direction: column; gap: 16px;">
                <div class="form-group">
                  <label class="form-label required">Auth Mode</label>
                  <div>
                    <select id="authModeSelect" class="input" style="width:100%; margin-bottom: 8px;" onchange="toggleLicenseContainer()">
                      <option value="online">상시 인증 (Online)</option>
                      <option value="offline">오프라인 인증 (Offline License)</option>
                    </select>
                    <div id="licenseContainer" style="display:none; padding:16px; border:1px dashed #d1d5db; border-radius:6px; background:#f9fafb; margin-top:8px;">
                      <div style="font-size:13px; color:#4b5563; margin-bottom:8px; font-weight:600;">오프라인 라이선스 키 발급 (기간 설정)</div>
                      <div style="display:flex; gap:8px; margin-bottom:8px;">
                        <select class="input" style="flex:1;">
                          <option value="90">90일</option>
                          <option value="180">180일</option>
                          <option value="365" selected>1년 (365일)</option>
                          <option value="permanent">영구 (무제한)</option>
                        </select>
                        <button type="button" class="btn btn-primary" style="white-space:nowrap; padding:6px 16px; font-size:13px;" onclick="document.getElementById('licenseKeyInput').value='LIC-' + Math.random().toString(36).substr(2,9).toUpperCase()">키 생성</button>
                      </div>
                      <input type="text" id="licenseKeyInput" class="input" style="width:100%; font-family:monospace; background:#e5e7eb; color:#374151; font-weight:bold;" placeholder="키 생성 버튼을 눌러주세요" readonly>
                    </div>
                  </div>

                  <script>
                    function toggleLicenseContainer() {
                      const mode = document.getElementById('authModeSelect');
                      if(!mode) return;
                      const container = document.getElementById('licenseContainer');
                      if(mode.value === 'offline') {
                        container.style.display = 'block';
                      } else {
                        container.style.display = 'none';
                      }
                    }
                    document.addEventListener('DOMContentLoaded', toggleLicenseContainer);
                  </script>
                </div>
              </div>
            </div>

          </div>"""

# we replace from <!-- Left Column ... up to the end of the Left Column wrapper.
out_html = re.sub(start_marker + r'.*?' + end_marker, new_html_content, html, flags=re.DOTALL)
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(out_html)

print("Updated device-editor.html")
