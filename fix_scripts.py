import sys

def add_script(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

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
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed {filename}')
    else:
        print(f'{filename} already has script')

add_script('CMS-webpage/wireframe_site/product-editor.html')
add_script('CMS-webpage/wireframe_site/package-editor.html')
