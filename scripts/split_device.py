import codecs
import re

with codecs.open('CMS-webpage/wireframe_site/device-detail.html', 'r', 'utf-8') as f:
    html = f.read()

# Make the Detail Page adjustments too: change Product -> Package
html = html.replace(">Products:</div>", ">Package:</div>")
html = html.replace(">Product:</div>", ">Package:</div>")

# Start building editor from the corrected html
editor_html = html

# Update titles and breadcrumbs
editor_html = re.sub(r'📱 Device Detail: Kiosk-001', r'✨ Create New Device', editor_html)
editor_html = re.sub(r'<span style="color: #374151; font-weight: 600; padding: 4px 8px;">.*?</span', r'<span style="color: #374151; font-weight: 600; padding: 4px 8px;">✨ Create New Device</span>', editor_html)
editor_html = re.sub(r'<div>\s*<h1 class="page-title".*?</h1>\s*<div.*?</div>\s*</div>', r'<div>\n            <h1 class="page-title" style="margin-bottom: 8px;">✨ Create New Device</h1>\n          </div>', editor_html, flags=re.DOTALL)

# Adjust buttons in header
editor_html = re.sub(r'<div class="header-actions".*?</div>', r'''<div class="header-actions" style="display:flex; gap:8px;">
            <button class="btn btn-secondary" onclick="history.back()" style="color:#4b5563; border-color:#d1d5db;">✕ Cancel</button>
            <button class="btn btn-primary" onclick="alert('Device created successfully!'); location.href='device-list.html'">💾 Save Device</button>
          </div>''', editor_html, flags=re.DOTALL)

# Adjust layout to 1 column and remove Right Column
editor_html = re.sub(r'<div style="display: grid; grid-template-columns: 2fr 1fr; gap: 24px;">', r'<div style="display: grid; grid-template-columns: 1fr; gap: 24px;">', editor_html)

# Remove the Right Column (Installed Contents / Event Logs) completely
# They are inside a flex-column card or multiple cards on the right.
# A simpler way is to find exactly <!-- Right Column: ... --> till the end of that grid column
editor_html = re.sub(r'<!-- Right Column: Installed Contents -->.*?(?=<!-- Metadata Section -->)', r'', editor_html, flags=re.DOTALL)

# Remove Spec info (Hardware and Software)
editor_html = re.sub(r'<div class="card" style="margin-top: 24px;">\s*<h2[^>]*>🔧 스펙 정보</h2>.*?</div>\s*</div>', r'', editor_html, flags=re.DOTALL)
# It's possible the wrapper ends differently. Let's do a more generic replace for that section block
editor_html = re.sub(r'<h2[^>]*>🔧 스펙 정보</h2>.*?<!-- Right Column:', r'<!-- Right Column:', editor_html, flags=re.DOTALL)
editor_html = re.sub(r'<div class="card" style="margin-top: 24px;">\s*<h2[^>]*>🔧 스펙 정보</h2>.*?</div>\s*</div>', r'', editor_html, flags=re.DOTALL)
editor_html = re.sub(r'<div class="card" style="margin-top: 24px;">\s*(?=<!-- Metadata Section -->)', r'', editor_html, flags=re.DOTALL)
editor_html = re.sub(r'<h2[^>]*>🔧 스펙 정보</h2>.*?(?=<!-- Metadata Section -->)', r'', editor_html, flags=re.DOTALL)

# Change Device ID to readonly placeholder
editor_html = re.sub(r'<input type="text" class="input" style="width:100%; background:#f3f4f6; color:#6b7280;" value="DEV-K-001" disabled>', r'<input type="text" class="input" style="width:100%; background:#f3f4f6; color:#9ca3af;" value="" placeholder="서버에서 자동 생성됩니다" disabled>', editor_html)

# Clear other inputs in basic info
editor_html = editor_html.replace('value="Kiosk-001"', 'value=""')
editor_html = editor_html.replace('value="00:1A:2B:3C:4D:5E"', 'value=""')
editor_html = editor_html.replace('value="CMS Player, Content Viewer"', 'value=""')
editor_html = re.sub(r'>1F 로비 입구 옆.*?</textarea>', r'></textarea>', editor_html)

# Remove Metadata section entirely
editor_html = re.sub(r'<!-- Metadata Section -->.*?</div>', r'', editor_html, count=1, flags=re.DOTALL)
editor_html = re.sub(r'<div class="card" id="metadataSection">.*?</div>\s*</div>', r'', editor_html, flags=re.DOTALL)

# Remove device-specific dynamic JS for new mode (if we injected any previously)
editor_html = re.sub(r"// Auto-generate ID placeholder.*?</script>", r"</script>", editor_html, flags=re.DOTALL)

with codecs.open('CMS-webpage/wireframe_site/device-editor.html', 'w', 'utf-8') as f:
    f.write(editor_html)

# Detail cleanup
detail_html = html
detail_html = re.sub(r"// Auto-generate ID placeholder.*?\}\n\s*\}\n", r"", detail_html, flags=re.DOTALL)
detail_html = re.sub(r"// Re-purpose Delete and Save buttons.*?\}\n", r"", detail_html, flags=re.DOTALL)
with codecs.open('CMS-webpage/wireframe_site/device-detail.html', 'w', 'utf-8') as f:
    f.write(detail_html)

print("Split Device complete!")
