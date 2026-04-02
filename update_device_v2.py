import re

with open('CMS-webpage/wireframe_site/device-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix routing in device-list.html
with open('CMS-webpage/wireframe_site/device-list.html', 'r', encoding='utf-8') as f:
    dl_text = f.read()
dl_text = dl_text.replace("window.location.href = 'device-detail.html?deviceId=' + deviceId;",
                          "window.location.href = 'device-detail.html?id=' + deviceId;")
with open('CMS-webpage/wireframe_site/device-list.html', 'w', encoding='utf-8') as f:
    f.write(dl_text)

new_basic_info = '''
                <div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">Name:</div>
                <input type="text" class="input" style="width:100%" value="Device-A">

                <div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">MAC Address:</div>
                <input type="text" class="input" style="width:100%; font-family:monospace" value="00:1A:2B:3C:4D:5E">

                <div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">Product:</div>
                <div style="position:relative;">
                  <input type="text" list="productList" class="input" style="width:100%" value="Product A" placeholder="Search Product...">
                  <datalist id="productList">
                      <option value="Product A">Product A</option>
                      <option value="Product B">Product B</option>
                  </datalist>
                </div>

                <div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">Package:</div>
                <div style="position:relative;">
                  <input type="text" list="packageList" class="input" style="width:100%" value="Package v1.0" placeholder="Search Package...">
                  <datalist id="packageList">
                      <option value="Package v1.0">Package v1.0</option>
                      <option value="Package v2.0">Package v2.0</option>
                  </datalist>
                </div>

                <div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">Location:</div>
                <div style="display:flex; gap:8px;">
                  <select class="input" style="flex:1;">
                    <option value="" disabled>-- Local Area 검색 / 선택 --</option>
                    <option value="seoul-01" selected>SEOUL-01</option>
                    <option value="busan-01">BUSAN-01</option>
                  </select>

                  <select class="input" style="flex:1;">
                    <option value="" disabled>-- Store 검색 / 선택 --</option>
                    <option value="store-01" selected>Store-01 (Main)</option>
                    <option value="store-02">Store-02</option>
                  </select>
                </div>

                <div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">인증 모드:</div>
                <select class="input" style="width:100%;" onchange="const isOffline = this.value === 'offline'; document.getElementById('licenseSection').style.display = isOffline ? 'flex' : 'none'; document.getElementById('licenseLabel').style.display = isOffline ? 'block' : 'none';">
                  <option value="online">온라인 인증</option>
                  <option value="offline" selected>오프라인 인증</option>
                </select>

                <div class="info-label" id="licenseLabel" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">라이선스 키:</div>
                <div id="licenseSection" style="display:flex; gap:8px;">
                  <input type="text" list="licenseList" class="input" style="flex:1; font-family:monospace;" value="LIC-OFF-X8B9Q2MA" placeholder="Search License Key...">
                  <datalist id="licenseList">
                    <option value="LIC-OFF-X8B9Q2MA">LIC-OFF-X8B9Q2MA (Current)</option>
                    <option value="LIC-OFF-NEW123">LIC-OFF-NEW123 (Unused)</option>
                  </datalist>
                  <button type="button" class="btn btn-outline" style="padding:4px 12px; font-size:13px;" onclick="alert('클립보드에 복사되었습니다.')">복사</button>
                </div>
'''

new_text = re.sub(
    r'(<h2[^>]*>.*?기본 정보</h2>\s*<div[^>]*>)(.*?)(</div>\s*</div>\s*<div class=\"card\">\s*<h2[^>]*>.*?Hardware Specs)',
    rf'\g<1>{new_basic_info}\g<3>',
    text,
    flags=re.DOTALL
)

with open('CMS-webpage/wireframe_site/device-detail.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updates applied successfully.")
