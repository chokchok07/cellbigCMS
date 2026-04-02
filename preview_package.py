import re

def preview_modal():
    with open('CMS-webpage/wireframe_site/package-detail.html', 'r', encoding='utf-8') as f:
        data = f.read()

    m = re.search(r'<div[^>]*id="manageModal"[\s\S]*?(?:</script>|</body>)', data)
    if m:
        print(m.group(0)[:1000]) # First 1000 chars

def preview_version():
    with open('CMS-webpage/wireframe_site/package-editor.html', 'r', encoding='utf-8') as f:
        data = f.read()

    m = re.search(r'<div class="form-group">\s*<label[^>]*>Version</label>.*?</div>', data, re.DOTALL)
    if m:
        print(m.group(0))

preview_modal()
print("-----")
preview_version()
