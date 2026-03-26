import os
import re

ws = r'c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site'
idx_path = os.path.join(ws, 'index.html')
ver_path = os.path.join(ws, 'version-register.html')

with open(idx_path, 'r', encoding='utf-8') as f:
    idx_content = f.read()

prod_path = os.path.join(ws, 'product-list.html')
with open(prod_path, 'r', encoding='utf-8') as f:
    prod_content = f.read()
    
sidebar_match = re.search(r'<div class="dashboard-layout">\s*<aside class="sidebar">.*?</aside>', prod_content, re.DOTALL)
sidebar_html = sidebar_match.group(0) if sidebar_match else ''

start_idx = idx_content.find('<!-- Release Notes / Patch Logs Section -->')
end_idx = idx_content.find('</main>', start_idx)
rel_notes_html = idx_content[start_idx:end_idx]

# Remove the 'onclick="alert..."' from the "+ 신규 등록" to now trigger the modal!
rel_notes_html = rel_notes_html.replace(
    '''onclick=\"alert('패치노트 등록 양식 모달/페이지가 열립니다. (Super Admin 전용)')\"''',
    '''onclick=\"openModal()\"'''
)
rel_notes_html = rel_notes_html.replace(
    '''+ 신규 패치노트 등록''',
    '''+ 신규 버전/패치 등록'''
)

new_main = '''    <main class="main-content" style="display:flex; justify-content:center; align-items:center; height:calc(100vh - 60px);">
      <div style="text-align:center;">
        <h1 style="font-size:32px; color:#1f2937; margin-bottom:10px;">👋 Welcome, 홍길동</h1>
        <p style="color:#6b7280; font-size:16px;">셀빅 CMS 어드민 사이트에 오신 것을 환영합니다.</p>
      </div>'''

clean_idx = idx_content[:idx_content.find('<main class="main-content">')] + new_main + idx_content[end_idx:]

with open(idx_path, 'w', encoding='utf-8') as f:
    f.write(clean_idx)

# Now, we need to inject the release notes into version-register.html
with open(ver_path, 'r', encoding='utf-8') as f:
    ver_content = f.read()

head_match = re.search(r'<head>.*?</head>', ver_content, re.DOTALL)
head = head_match.group(0) if head_match else '<head></head>'

modal_idx = ver_content.find('<div class="modal-overlay"')
modal_html = ver_content[modal_idx:]

new_ver_html = f'''<!DOCTYPE html>
<html lang="ko">
{head}
<body>
    <header class="site-header">
      <div style="display:flex;align-items:center;gap:16px">
        <span style="font-weight:700;font-size:20px;color:#1f2937;cursor:pointer" onclick="location.href='index.html'">CellbigCMS</span>
      </div>
      <div style="display:flex;gap:16px;align-items:center">
        <span style="cursor:pointer">🔔 (3)</span>
        <div style="display:flex; align-items:center; gap:12px;">
          <span style="cursor:pointer">👤 Admin(SP)</span>
          <button type="button" style="padding:4px 12px; font-size:12px; font-weight:500; color:#4b5563; background:#f3f4f6; border:1px solid #d1d5db; border-radius:4px; cursor:pointer;" onclick="location.href='index.html';">로그아웃</button>
        </div>
      </div>
    </header>
    {sidebar_html}
    <main class="main-content">
      <div class="container" style="max-width: 1000px; margin: 0 auto; padding-top: 20px;">
{rel_notes_html}
      </div>
    </main>
  </div>
{modal_html}
'''

with open(ver_path, 'w', encoding='utf-8') as f:
    f.write(new_ver_html)
