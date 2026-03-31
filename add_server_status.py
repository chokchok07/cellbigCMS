import os
import glob

# 사이드바가 포함된 모든 html 파일을 찾습니다
html_files = glob.glob('CMS-webpage/wireframe_site/*.html')

css_update = """
.sidebar {
  display: flex;
  flex-direction: column;
}
"""

status_html = """
        <div style="margin-top: auto; padding-top: 24px; margin-bottom: 8px;">
          <div style="padding: 12px 16px; border-radius: 8px; background: #f8fafc; border: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: space-between; cursor: default;" title="Last checked: Just now">
            <div style="display: flex; align-items: center; gap: 8px;">
              <div style="width: 8px; height: 8px; border-radius: 50%; background-color: #10b981; box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.2); animation: pulse 2s infinite;"></div>
              <div style="display: flex; flex-direction: column;">
                <span style="font-size: 12px; font-weight: 600; color: #374151;">API Server</span>
                <span style="font-size: 11px; color: #10b981; font-weight: 500;">Online (42ms)</span>
              </div>
            </div>
            <span style="font-size: 12px; color: #64748b;">v1.2</span>
          </div>
        </div>
"""

# styles.css 업데이트 (사이드바 flex 속성 추가)
with open('CMS-webpage/wireframe_site/styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if 'flex-direction:column;' not in css_content.replace(' ', ''):
    css_content = css_content.replace('.sidebar{', '.sidebar{display:flex;flex-direction:column;', 1)
    
    # Add pulse animation for the live dot
    pulse_anim = """
@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.4); }
  70% { box-shadow: 0 0 0 4px rgba(16, 185, 129, 0); }
  100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}
"""
    if 'keyframes pulse' not in css_content:
        css_content += pulse_anim

    with open('CMS-webpage/wireframe_site/styles.css', 'w', encoding='utf-8') as f:
        f.write(css_content)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<aside class="sidebar">' not in content:
        continue

    # 중복 추가 방지
    if 'API Server' in content and 'Online' in content:
        continue
        
    content = content.replace("</aside>", status_html + "      </aside>")
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Server status widget added to all sidebars.")
