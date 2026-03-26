import codecs
import re

with codecs.open('CMS-webpage/wireframe_site/localarea-editor.html', 'r', 'utf-8') as f:
    html = f.read()

# Regular expression to catch the lingering updated dates and wrapper elements
html = re.sub(r'<div class="info-value">2025-10-01 09:00 by admin</div>.*?</main>', r'</div>\n      </main>', html, flags=re.DOTALL)

with codecs.open('CMS-webpage/wireframe_site/localarea-editor.html', 'w', 'utf-8') as f:
    f.write(html)
print('Removed stray texts')
