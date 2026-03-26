import io

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    target = f.read()

import re
m = re.search(r'<div class="v-modal-overlay".*?</script>', target, flags=re.DOTALL)
if m:
    with open('output_modal.txt', 'w', encoding='utf-8') as out:
        out.write(m.group(0))
