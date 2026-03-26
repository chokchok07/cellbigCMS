import codecs
import re

with codecs.open('CMS-webpage/wireframe_site/localarea-detail.html', 'r', 'utf-8') as f:
    html = f.read()

# ---------------------------------------------------------
# 1. Create localarea-editor.html based on detail
# ---------------------------------------------------------
editor_html = html

# Update titles and breadcrumbs
editor_html = re.sub(r'📍 LocalArea Detail: Seoul', r'✨ Create New Local Area', editor_html)
editor_html = re.sub(r'<span style="color: #374151; font-weight: 600; padding: 4px 8px;">.*?</span', r'<span style="color: #374151; font-weight: 600; padding: 4px 8px;">✨ Create New Local Area</span>', editor_html)
editor_html = re.sub(r'<div>\s*<h1 class="page-title".*?</h1>\s*<div.*?</div>\s*</div>', r'<div>\n            <h1 class="page-title" style="margin-bottom: 8px;">✨ Create New Local Area</h1>\n          </div>', editor_html, flags=re.DOTALL)

# Adjust buttons in header
editor_html = re.sub(r'<div class="header-actions".*?</div>', r'''<div class="header-actions" style="display:flex; gap:8px;">
            <button class="btn btn-secondary" onclick="history.back()" style="color:#4b5563; border-color:#d1d5db;">✕ Cancel</button>
            <button class="btn btn-primary" onclick="alert('Local Area created successfully!'); location.href='localarea-list.html'">💾 Save Local Area</button>
          </div>''', editor_html, flags=re.DOTALL)

# Adjust layout to 1 column and remove Right Column (Stores)
editor_html = re.sub(r'<div style="display: grid; grid-template-columns: 2fr 1fr; gap: 24px;">', r'<div style="display: grid; grid-template-columns: 1fr; gap: 24px;">', editor_html)
editor_html = re.sub(r'<!-- Right Column: Stores -->.*?<!-- Metadata Section -->', r'<!-- Metadata Section -->', editor_html, flags=re.DOTALL)

# Change LocalArea ID to readonly placeholder
editor_html = re.sub(r'<input type="text" class="input" style="width:100%; background:#f3f4f6; color:#6b7280;" value="localarea-seoul" disabled>', r'<input type="text" class="input" style="width:100%; background:#f3f4f6; color:#9ca3af;" value="" placeholder="서버에서 자동 생성됩니다" disabled>', editor_html)

# Clear other inputs
editor_html = re.sub(r'value="Seoul"', r'value=""', editor_html)
editor_html = re.sub(r'value="서울특별시.*?"', r'value=""', editor_html)
editor_html = re.sub(r'>서울 권역 \(본사 관할\).*?</textarea>', r'></textarea>', editor_html)

# Remove Metadata section entirely
editor_html = re.sub(r'<!-- Metadata Section -->.*?</div>', r'', editor_html, count=1, flags=re.DOTALL)
editor_html = re.sub(r'<div class="card" id="metadataSection">.*?</div>\s*</div>', r'', editor_html, flags=re.DOTALL)

# Remove JS
editor_html = re.sub(r'// Auto-generate ID placeholder.*?</script>', r'</script>', editor_html, flags=re.DOTALL)

with codecs.open('CMS-webpage/wireframe_site/localarea-editor.html', 'w', 'utf-8') as f:
    f.write(editor_html)

# ---------------------------------------------------------
# 2. Clean up localarea-detail.html (Remove dynamic new mode JS)
# ---------------------------------------------------------
detail_html = html
detail_html = re.sub(r'// Auto-generate ID placeholder.*?\}\n\s*\}\n', r'', detail_html, flags=re.DOTALL)
detail_html = re.sub(r'// Re-purpose Delete and Save buttons.*?</script>', r'</script>', detail_html, flags=re.DOTALL)

with codecs.open('CMS-webpage/wireframe_site/localarea-detail.html', 'w', 'utf-8') as f:
    f.write(detail_html)

print("Split complete!")
