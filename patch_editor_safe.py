import re

with open('CMS-webpage/wireframe_site/content-editor.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make titles dynamic
text = text.replace('<h1 class="page-title">🎬 Content Editor</h1>', '<h1 class="page-title" id="pageMainTitle">🎬 Content Editor</h1>')

js_old = "document.getElementById('pageMode').textContent = 'Edit: Content ' + urlParams.get('id');"
js_new = """const pgTitle = document.getElementById('pageMainTitle');
      if(pgTitle) pgTitle.textContent = '🎬 콘텐츠 상세정보';
      document.getElementById('pageMode').textContent = '콘텐츠의 상세 정보를 확인하고 수정합니다';
      // keep the original textContent logic commented out just in case
      // document.getElementById('pageMode').textContent = 'Edit: Content ' + urlParams.get('id');
"""
text = text.replace(js_old, js_new)

# Move versionsSection
m = re.search(r'<div class="card" id="versionsSection"[\s\S]*?<!-- Right Column -->', text)
if m:
    # We matched all the way from versionsSection to Right Column
    # The actual versions section ends right before it. Let's do it precisely string-based:
    pass

start_idx = text.find('<div class="card" id="versionsSection" style="display:none;">')
if start_idx != -1:
    end_idx = text.find('<!-- Right Column -->')
    if end_idx != -1:
        # Extract versions section
        versionsSection = text[start_idx:end_idx]
        
        # Remove it from its current position
        text = text[:start_idx] + text[end_idx:]
        
        # Insert after <div style="display: flex; flex-direction: column; gap: 24px;"> under Right Column
        target_str = '<!-- Right Column -->\n          <div style="display: flex; flex-direction: column; gap: 24px;">\n'
        insertion_point = text.find(target_str)
        if insertion_point != -1:
            insertion_point += len(target_str)
            text = text[:insertion_point] + versionsSection + text[insertion_point:]

with open('CMS-webpage/wireframe_site/content-editor.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('content-editor.html patched safely')
