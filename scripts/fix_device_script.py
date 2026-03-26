import codecs
import re

def fix_script(filepath):
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    script_pattern = re.compile(r'<script>\s*// Navigation handling.*?</script>', re.DOTALL)
    
    new_script = '''<script>
      // Navigation handling
      document.querySelectorAll('.sidebar-item').forEach(item => {
        item.addEventListener('click', function() {
          const page = this.getAttribute('data-page');
          if (page) {
            window.location.href = page;
          }
        });
      });

      function showDeleteModal() {
        document.getElementById('deleteModal').style.display = 'flex';
      }
      function closeDeleteModal() {
        document.getElementById('deleteModal').style.display = 'none';
      }
      function deleteDevice() {
        alert('Deleted successfully!');
        window.location.href = 'device-list.html';
      }
    </script>'''
    
    html = script_pattern.sub(new_script, html)
    
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(html)

fix_script('CMS-webpage/wireframe_site/device-editor.html')
print('Fixed!')
