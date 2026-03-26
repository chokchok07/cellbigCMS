import os
import re

def wrap_with_container(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    if '<main class="main-content">' in html and '<div class="container">' not in html:
        # Wrap everything between <main class="main-content"> and </main> in <div class="container">
        # Or easier: just replace <main class="main-content"> with <main class="main-content">\n      <div class="container">
        # And replace </main> with </div>\n    </main>
        
        html = html.replace('<main class="main-content">', '<main class="main-content">\n      <div class="container">')
        html = html.replace('</main>', '</div>\n    </main>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Wrapped {filepath} in .container")

wrap_with_container('CMS-webpage/wireframe_site/localarea-list.html')
wrap_with_container('CMS-webpage/wireframe_site/store-list.html')
wrap_with_container('CMS-webpage/wireframe_site/device-list.html')  # Just to be safe
wrap_with_container('CMS-webpage/wireframe_site/log-content-access.html')
wrap_with_container('CMS-webpage/wireframe_site/serial-list.html')
wrap_with_container('CMS-webpage/wireframe_site/package-list.html')
wrap_with_container('CMS-webpage/wireframe_site/notice-list.html')

print("Done wrapping missing containers.")
