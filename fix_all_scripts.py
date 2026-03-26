import os
import glob

for f_path in glob.glob('CMS-webpage/wireframe_site/*-editor.html'):
    with open(f_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if '<script>' not in content:
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
        content = content.replace('</body>', script_block)
        with open(f_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed missing script in {f_path}')
    else:
        print(f'{f_path} already has script')
