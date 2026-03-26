import io
import re

# Fix LocalArea Description
fp_la = 'CMS-webpage/wireframe_site/localarea-editor.html'
html_la = io.open(fp_la, 'r', encoding='utf-8').read()
html_la = re.sub(
    r'<h3[^>]*>.*?Description</h3>\s*<textarea([^>]*)>.*?</textarea>',
    r'''<div class="form-group">
              <label class="form-label">Description</label>
              <textarea\1 placeholder="내용을 입력하세요"></textarea>
            </div>''',
    html_la, flags=re.DOTALL
)
io.open(fp_la, 'w', encoding='utf-8').write(html_la)
print('Fixed LA Description')

# Fix Product and Package editors properly
# They are currently exactly the same as Detail pages but with title changed.
def clean_editor(fp, target_titles):
    html = io.open(fp, 'r', encoding='utf-8').read()
    
    # Let's cleanly remove ANY <div class="card">...</div> that contains the target titles in an h2.
    for title in target_titles:
        # Find all cards
        # Wait, an easier way is to just find the marker for the h2 and remove its parent card.
        while True:
            m = re.search(r'<div[^>]*class="card"[^>]*>.*?<h2[^>]*>.*?'+title+r'.*?</h2>.*?</div>\s*(?=</div>|<!--|<div)', html, flags=re.DOTALL)
            if m:
                # But regex matching `</div>` properly for nested divs is impossible.
                break
            else:
                break

    # Alternative: A manual parser.
    # Actually, we can just replace the left/right columns layout completely, 
    # since editors shouldn't have columns!
    
    # In both product and package, there's `<!-- Content Grid -->` followed by `<div style="display: grid; grid-template-columns: 1fr 380px; ...`
    # Let's just remove the 380px grid template!
    html = html.replace('grid-template-columns: 1fr 380px;', 'grid-template-columns: 1fr;')
    
    # Now, let's just physically slice out the things we don't want using exact string or simple tag parsing
    io.open(fp, 'w', encoding='utf-8').write(html)

