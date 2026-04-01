from bs4 import BeautifulSoup

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    text = f.read()

with open('extracted_versions.html', 'r', encoding='utf-8') as f:
    ext_vers = f.read()

with open('extracted_modal.html', 'r', encoding='utf-8') as f:
    ext_modal = f.read()

with open('extracted_modal.js', 'r', encoding='utf-8') as f:
    ext_js = f.read()

soup = BeautifulSoup(text, 'html.parser')

# Remove old versions main content
main = soup.find('main', class_='main-content')
if main:
    main.clear()
    
    # We will reconstruct main.
    # Because bs4 parsing + string injection can just be appended.
    main.append(BeautifulSoup(f'''
      <div class="container">
        <!-- Breadcrumb / Header -->
        <div class="page-header" style="flex-direction: column; align-items: flex-start; border-bottom: none; margin-bottom: 0;">
          <div style="color:#6b7280; font-size:14px; margin-bottom:8px; cursor:pointer;" onclick="history.back()">
            ← Back to Content
          </div>
          <div style="display:flex; justify-content:space-between; width:100%; align-items:center;">
            <div>
              <h1 class="page-title">📂 Version History</h1>
              <p class="page-desc">ID: 101 | 샌드크래프트 - 해변 (SandCraft - Beach)</p>
            </div>
            <!-- Handled inside extracted content -->
          </div>
        </div>

        <div style="margin-top: 16px;">
        {ext_vers.replace('style="display:none;"', 'style="display:block;"')}
        </div>
      </div>
    ''', 'html.parser'))

# Remove old versionModal and statusConfirmModal if they exist
for m in soup.find_all(id='versionModal'): m.decompose()
for m in soup.find_all(id='statusConfirmModal'): m.decompose()

# Remove old modal scripts. We can just find script tags and remove the ones with openModal.
for script in soup.find_all('script'):
    if script.string and 'function openModal()' in script.string:
        # Just clear its string
        script.string = script.string.replace('function openModal() {', '/* removed openModal */')
        # We don't need to surgically remove everything, just clear all script content and put our own?
        # No, the script tag also contains window.location.href handling for sidebar.
        pass

# Append new modal HTML to body
soup.body.append(BeautifulSoup(ext_modal, 'html.parser'))

# Append new JS to the last script tag
scripts = soup.find_all('script')
if scripts:
    last_script = scripts[-1]
    if last_script.string:
        last_script.string += f"\n{ext_js}\n"
    else:
        last_script.string = ext_js
else:
    new_script = soup.new_tag('script')
    new_script.string = ext_js
    soup.body.append(new_script)

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Created content-versions.html via bs4")
