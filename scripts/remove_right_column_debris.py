import codecs
import re

file_path = 'CMS-webpage/wireframe_site/store-editor.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    html = f.read()

# Remove anything from "<!-- Right Column -->" up to right before "</main>"
# and replace it with closing divs for Content Grid and container.
html = re.sub(
    r'<!-- Right Column -->.*?</main>',
    '        </div>\n      </div>\n    </main>',
    html,
    flags=re.DOTALL
)

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(html)
print("Fixed Right Column debris!")
