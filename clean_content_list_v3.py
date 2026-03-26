import re

content_file = r'CMS-webpage\wireframe_site\content-list.html'

with open(content_file, 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    (r'컨테.*?너', '컨테이너'),
    (r'\?.*?Previous', '◀ Previous'),
    (r'Next \?\?/button>', 'Next ▶</button>'),
    (r'Next \?.*?</button>', 'Next ▶</button>')
]

for pat, repl in replacements:
    html = re.sub(pat, repl, html)

with open(content_file, 'w', encoding='utf-8') as f:
    f.write(html)
