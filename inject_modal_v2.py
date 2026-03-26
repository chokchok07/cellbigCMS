import re

target_file = 'CMS-webpage/wireframe_site/content-versions.html'
with open(target_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

with open('modal_css.html', 'r', encoding='utf-8') as f:
    modal_css = f.read()
with open('modal_html.html', 'r', encoding='utf-8') as f:
    modal_html = f.read()
with open('modal_js.html', 'r', encoding='utf-8') as f:
    modal_js = f.read()

# Make sure the modal overlay uses the ID and is hidden
modal_html = modal_html.replace('class="modal-overlay"', 'class="modal-overlay" id="versionModal" style="display: none;"')

# Also, update modal_html to fulfill specific user requests for the New Version popup
# 1. 버전 번호
# 2. 업데이트 유형 (강제/선택)
# 3. 배포 방식 (상용/테스트)
# 4. 버전 파일 로컬 불러오기 or 취소 (이미 구현됨)
# 5. 파일 크기 및 다시 다운로드 버튼
# 6. 버전 설명 (이미 구현됨)
# 7. 취소 / 등록(수정) 버튼

# Add a download button to the file display area
# Existing file html has: <div class="file-display" id="fileDisplay">파일을 선택해 주세요.</div>
download_btn_html = '''<div class="file-display" id="fileDisplay">파일을 선택해 주세요.</div>
                <button type="button" class="file-button" id="fileDownload" style="display:none; background:#10b981;">다운로드</button>'''
modal_html = modal_html.replace('<div class="file-display" id="fileDisplay">파일을 선택해 주세요.</div>', download_btn_html)

# Let's cleanly inject
if '<style>' in html_content:
    html_content = html_content.replace('</head>', f'{modal_css}\n</head>')
else:
    html_content = html_content.replace('</head>', f'{modal_css}\n</head>')

injection = f'''
  <!-- Version Registration Modal -->
  {modal_html}

  {modal_js}
  <script>
    function openModal() {{
       document.getElementById('versionModal').style.display = 'flex';
    }}
    function closeModal() {{
       document.getElementById('versionModal').style.display = 'none';
    }}
  </script>
'''

html_content = html_content.replace('</body>', f'{injection}\n</body>')
html_content = html_content.replace('''onclick="location.href='version-register.html?contentId=101'"''', 'onclick="openModal()"')

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Modal injection successful.")
