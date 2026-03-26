import glob, re

files = glob.glob('CMS-webpage/wireframe_site/*-detail.html')

script_template = '''
    <script>
      // Navigation handling
      document.querySelectorAll('.sidebar-item').forEach(item => {
        item.addEventListener('click', function() {
          const page = this.getAttribute('data-page');
          if (page) {
            window.location.href = page;
          }
        });
      });

      // New vs Edit Mode Detection
      document.addEventListener('DOMContentLoaded', () => {
        const urlParams = new URLSearchParams(window.location.search);
        const isNew = !urlParams.has('id');
        
        // Base Name Mapping
        const entityNames = {
          'localarea': 'LocalArea',
          'store': 'Store',
          'device': 'Device',
          'package': 'Package',
          'product': 'Product',
          'content': 'Content'
        };
        
        const path = window.location.pathname;
        let entityKey = 'Item';
        for(let key in entityNames) {
            if(path.includes(key + '-detail')) {
                entityKey = entityNames[key];
                break;
            }
        }

        const pageTitle = document.querySelector('.page-title');
        const breadcrumbLast = document.querySelector('.breadcrumb span:last-child');
        const statusSpan = document.querySelector('.status-badge') || document.querySelector('.page-title span');
        const metaSection = document.getElementById('metadataSection');
        
        if (isNew) {
          if (pageTitle) {
            // Strip out inner HTML like badges when replacing text
            const badgeHTML = statusSpan ? statusSpan.outerHTML : '';
            pageTitle.innerHTML = `✨ Create New ${entityKey} ${badgeHTML}`;
          }
          if (breadcrumbLast) breadcrumbLast.innerHTML = `✨ New ${entityKey}`;
          if (statusSpan) statusSpan.style.display = 'none'; // Hide status in new mode
          
          if (metaSection) metaSection.style.display = 'none'; // Hide metadata section
          
          // Hide Delete Button
          const deleteBtn = document.querySelector('.btn-secondary[onclick*="elete"]');
          if (deleteBtn) deleteBtn.style.display = 'none';
          
          // Clear inputs
          document.querySelectorAll('input[type="text"], textarea').forEach(el => {
              if (el.id !== 'searchInput') el.value = '';
          });
          document.querySelectorAll('.info-value').forEach(el => {
              if (el.tagName !== 'SPAN') el.innerHTML = '-';
          });
        }
      });
    </script>
'''

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        t = file.read()
    
    # Identify meta section
    t = re.sub(r'(<div class="card"[^>]*>)(\s*<h2[^>]*>(?:🕒|🏢|📦|🎒|🖥️|🎬)?\s*(?:Metadata|메타데이터|기본 정보))', r'<div class="card" id="metadataSection">\2', t, flags=re.IGNORECASE)
    
    # Replace existing script blocks that handle sidebar with our unified one
    t = re.sub(r'<script>\s*// Sidebar navigation.*?</script>', script_template, t, flags=re.DOTALL)
    
    # Just in case there are other generic scripts at the bottom that wasn't matched
    if '// New vs Edit Mode Detection' not in t:
        if '</body>' in t:
            t = t.replace('</body>', script_template + '\n</body>')
            
    with open(f, 'w', encoding='utf-8') as file:
        file.write(t)
    print(f'Updated {f}')

