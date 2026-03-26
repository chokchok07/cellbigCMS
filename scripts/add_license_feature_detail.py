import codecs

file_path = 'CMS-webpage/wireframe_site/device-detail.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    html = f.read()

license_html = """
                <div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">인증 모드:</div>
                <div style="display:flex; align-items:center;">
                  <span class="status-badge status-active" style="background:#f0fdf4; color:#166534; padding:4px 8px; border-radius:4px; font-size:12px; font-weight:600; border:1px solid #bbf7d0;">오프라인 인증</span>
                  <span style="margin-left:8px; font-size:13px; color:#6b7280;">(유효기간: 365일)</span>
                </div>

                <div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">라이선스 키:</div>
                <div style="display:flex; gap:8px;">
                  <input type="text" class="input" style="flex:1; font-family:monospace; background:#f9fafb;" value="LIC-OFF-X8B9Q2MA" readonly>
                  <button type="button" class="btn btn-outline" style="padding:4px 12px; font-size:13px;" onclick="alert('클립보드에 복사되었습니다.')">복사</button>
                </div>
"""

# Insert before "Name:" input
html = html.replace(
    '<div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">Name:</div>',
    license_html + '\n                <div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">Name:</div>'
)

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(html)
print("Updated detail!")
