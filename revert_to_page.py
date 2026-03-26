import re

# 1. Clean up content-versions.html and route button
with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    cv = f.read()

# Replace button click with navigation
cv = re.sub(r'onclick="[^"]*openModal\(\)[^"]*"', 'onclick="location.href=\'version-register.html\'"', cv)
cv = cv.replace('onclick="openModal()"', 'onclick="location.href=\'version-register.html\'"')

# Cut off any injected modal garbage at the bottom
script_start = cv.find("<script>\n    document.querySelectorAll('.sidebar-item[data-page]'")
if script_start != -1:
    clean_end = """<script>
    document.querySelectorAll('.sidebar-item[data-page]').forEach(item => {
      item.addEventListener('click', function() {
        const page = this.getAttribute('data-page');
        if (page) window.location.href = page;
      });
    });
  </script>
</body>
</html>"""
    cv = cv[:script_start] + clean_end

# Attempt to remove injected <style> block from head
cv = re.sub(r'<style>\s*\.v-modal-overlay.*?</style>\s*', '', cv, flags=re.DOTALL)

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(cv)


# 2. Rebuild version-register.html as a standard clean page (removing modal background)
with open('CMS-webpage/wireframe_site/version-register.html', 'r', encoding='utf-8') as f:
    vr = f.read()

# Extract old JS
js_match = re.search(r'<script>(.*?)</script>\s*</body>', vr, flags=re.DOTALL)
js_code = js_match.group(1) if js_match else ""
js_code = js_code.replace("closeModal()", "history.back()")

# Extract old Form
form_match = re.search(r'<form id="versionForm">.*?</form>', vr, flags=re.DOTALL)
form_code = form_match.group(0) if form_match else ""

new_vr = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>새 버전 등록 - CellbigCMS</title>
  <link rel="stylesheet" href="styles.css">
  <style>
    .form-group {{ margin-bottom: 24px; }}
    .form-group label {{ display: block; margin-bottom: 8px; font-weight: 600; color: #374151; }}
    .version-inputs {{ display: flex; align-items: center; gap: 8px; }}
    .version-inputs input {{ width: 80px; padding: 8px 12px; border: 1px solid #d1d5db; border-radius: 4px; font-size: 16px; text-align: center; }}
    .radio-group {{ display: flex; gap: 24px; }}
    .radio-option {{ display: flex; align-items: center; gap: 8px; cursor: pointer; }}
    .radio-option input {{ width: 18px; height: 18px; }}
    .file-input-group {{ display: flex; gap: 8px; align-items: center; }}
    .file-display {{ flex: 1; padding: 10px 12px; border: 1px solid #d1d5db; border-radius: 4px; background: #f9fafb; color: #6b7280; font-size:14px; display: flex; align-items: center; }}
    .file-display.has-file {{ color: #111827; font-weight:500; background:#fff; }}
    textarea {{ width: 100%; min-height: 120px; padding: 12px; border: 1px solid #d1d5db; border-radius: 4px; font-family: inherit; font-size: 14px; }}
    .file-button {{ padding: 8px 16px; border: 1px solid #d1d5db; background: white; border-radius: 4px; cursor: pointer; white-space: nowrap; }}
    .file-clear {{ padding: 8px 16px; border: 1px solid #d1d5db; background: white; border-radius: 4px; cursor: pointer; color: #666; }}
    .verify-button {{ padding: 8px 16px; border: none; background: #28a745; color: white; border-radius: 4px; cursor: pointer; font-weight: 500; }}
    .verify-button:disabled {{ background: #ccc; cursor: not-allowed; }}
    .btn-secondary {{ padding: 10px 24px; border: none; background: #6c757d; color: white; border-radius: 4px; cursor: pointer; font-weight: 500; }}
    .btn-primary {{ padding: 10px 24px; border: none; background: #007bff; color: white; border-radius: 4px; cursor: pointer; font-weight: 500; }}
    .btn-primary:disabled {{ background: #ccc; cursor: not-allowed; }}
    .checksum-info {{ margin-top: 8px; font-size: 13px; color: #6b7280; }}
  </style>
</head>
<body>
  <header class="site-header">
    <div style="display:flex;align-items:center;gap:16px">
      <span style="font-weight:700;font-size:20px;color:#1f2937;cursor:pointer" onclick="location.href='index.html'">CellbigCMS</span>
    </div>
    <div style="display:flex;gap:16px;align-items:center">
      <span style="cursor:pointer">🔔 (3)</span>
      <span style="cursor:pointer">👤 Admin(SP)</span>
    </div>
  </header>

  <div class="dashboard-layout">
    <aside class="sidebar">
      <div class="sidebar-category">Contents & Product</div>
      <div class="sidebar-item" onclick="location.href='content-list.html'">🎬 Content</div>
      <div class="sidebar-item" onclick="location.href='content-versions.html'">↳ 📂 Version History</div>
      <div class="sidebar-item active" style="font-weight:bold;">↳ ✨ New Version</div>
    </aside>
    <main class="main-content">
      <div class="container" style="max-width:800px;">
        <div style="color:#6b7280; font-size:14px; margin-bottom:12px; cursor:pointer;" onclick="history.back()">← 버전 히스토리로 돌아가기</div>
        <h1 style="margin-bottom:24px; font-size:24px; color:#111827;">새 버전 등록</h1>
        
        <div class="card" style="padding: 32px;">
          {form_code}
          
          <div style="margin-top:32px; padding-top:24px; border-top:1px solid #e5e7eb; display:flex; justify-content:flex-end; gap:12px;">
            <button class="btn-secondary" onclick="history.back()">취소</button>
            <button class="btn-primary" id="registerButton" onclick="registerVersion()" disabled>버전 등록 완료</button>
          </div>
        </div>
      </div>
    </main>
  </div>
  
  <script>
    {js_code}
  </script>
</body>
</html>
"""

with open('CMS-webpage/wireframe_site/version-register.html', 'w', encoding='utf-8') as f:
    f.write(new_vr)

print("Modal completely removed, standalone page perfectly integrated.")
