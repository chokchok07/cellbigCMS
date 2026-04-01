from bs4 import BeautifulSoup
import re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    text = f.read()

with open('extracted_versions.html', 'r', encoding='utf-8') as f:
    ext_vers = f.read()

with open('extracted_modal.html', 'r', encoding='utf-8') as f:
    ext_modal = f.read()

with open('extracted_modal.js', 'r', encoding='utf-8') as f:
    ext_js = f.read()

# Replace the inner version list
# In content-versions.html, there is:
# <!-- Versions List Area -->
# <div style="display: flex; flex-direction: column; gap: 16px;"> ... </div> (all the cards)
# Let's replace the button logic first
text = text.replace('onclick="openModal()"', 'onclick="openNewVersionModal()"')

# Now replace the versions list area.
# Find <!-- Versions List Area -->
list_area_start = text.find('<!-- Versions List Area -->')
if list_area_start != -1:
    # Find the next </div> for the container wrapping the cards... wait, it's a bit hard with string manipulation.
    # Let's use BeautifulSoup on text
    soup = BeautifulSoup(text, 'html.parser')
    
    # Wait, using bs4 directly might lose formatting heavily, but it's safe.
    # Let's just do a regex replace from <!-- Versions List Area --> up to the end of that main container.
    m = re.search(r'<!-- Versions List Area -->.*?<div style="display: flex; flex-direction: column; gap: 16px;">.*?<!-- Version Item : v2\.0\.0 -->.*?(</div>\s*</div>)', text, re.DOTALL)
    if m:
        # Actually it's easier to find the parent container.
        pass
    
    # Or just replace the hardcoded cards between <!-- Versions List Area --> and the end of </main>
    container = soup.find('main', class_='main-content').find('.container')
    
# Let's do it simply by injecting ext_vers, ext_modal, ext_js into a cleanly built content-versions.html body.
# Wait, content-versions.html doesn't have much else, it's just the versions page.
# I'll just rewrite the <main class="main-content"> completely.

new_main = f"""
    <main class="main-content">
      <div class="container">
        <!-- Breadcrumb / Header -->
        <div class="page-header" style="flex-direction: column; align-items: flex-start;">
          <div style="color:#6b7280; font-size:14px; margin-bottom:8px; cursor:pointer;" onclick="history.back()">
            ← Back to Content
          </div>
          <div style="display:flex; justify-content:space-between; width:100%; align-items:center;">
            <div>
              <h1 class="page-title">📂 Version History</h1>
              <p class="page-desc">ID: 101 | 샌드크래프트 - 해변 (SandCraft - Beach)</p>
            </div>
            <div class="header-actions">
            </div>
          </div>
        </div>

        {ext_vers.replace('style="display:none;"', 'style="display:block;"')}
      </div>
    </main>
"""

# Let's replace the whole main tag
m_main = re.search(r'<main class="main-content">.*?</main>', text, re.DOTALL)
if m_main:
    text = text.replace(m_main.group(0), new_main)

# Also we need to replace the old modals and JS
m_modal = re.search(r'<div id="versionModal".*?</form>\s*</div>\s*</div>', text, re.DOTALL)
if m_modal:
    text = text.replace(m_modal.group(0), '')

m_modal2 = re.search(r'<div id="statusConfirmModal".*?</form>\s*</div>\s*</div>', text, re.DOTALL)
if m_modal2:
    text = text.replace(m_modal2.group(0), '')

m_js2 = re.search(r'function openModal\(\).*?\}\s*\}', text, re.DOTALL)
if m_js2:
    text = text.replace(m_js2.group(0), '')

# Remove extra modal bits if they exist. Wait, let's just append our modal before </body>
body_end = text.rfind('</body>')
text = text[:body_end] + ext_modal + "\n</body>\n"

# Append JS before </script> or at body_end
script_end = text.rfind('</script>')
if script_end != -1:
    text = text[:script_end] + ext_js + "\n</script>\n"
else:
    text = text.replace('</body>', f'<script>\n{ext_js}\n</script>\n</body>')

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated content-versions.html successfully!")
