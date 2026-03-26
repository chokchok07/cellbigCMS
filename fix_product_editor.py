import re

with open('CMS-webpage/wireframe_site/product-editor.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'<div class=""form-group"">\s*<label class=""form-label"">\s*Default Package\s*</label>\s*<select.*?</select>\s*</div>',
    '',
    content,
    flags=re.DOTALL
)

script_block = '''
  <script>
    // Sidebar navigation
    document.querySelectorAll('.sidebar-item').forEach(item => {
      item.addEventListener('click', function() {
        const page = this.getAttribute('data-page');
        if (page) {
          window.location.href = page;
        }
      });
    });
  </script>
</body>
'''
if '<script>' not in content:
    content = content.replace('</body>', script_block)

with open('CMS-webpage/wireframe_site/product-editor.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done frontend')
