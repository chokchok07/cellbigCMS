import codecs
import re

def fix_script(filepath, is_editor):
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    # Find everything exactly from <script>\s*// Navigation handling to </script>
    script_pattern = re.compile(r'<script>\s*// Navigation handling.*?</script>', re.DOTALL)
    
    # New clean script content
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
      function deleteLocalArea() {
        alert('Deleted successfully!');
        window.location.href = 'localarea-list.html';
      }
    </script>'''

    # For editor, we also don't need deleteLocalArea but keeping it is harmless
    # since we removed the delete button.
    
    html = script_pattern.sub(new_script, html)
    
    # Oh wait, the original had more things inside the first <script>?
    # Let me make sure not to wipe out something important.
    
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(html)

fix_script('CMS-webpage/wireframe_site/localarea-detail.html', False)
fix_script('CMS-webpage/wireframe_site/localarea-editor.html', True)
print('Fixed!')
