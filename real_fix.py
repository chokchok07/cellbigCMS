import os

def check_and_fix(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    changed = False

    # Check if we need to add container
    if '<main class="main-content">' in html and '<div class="container">' not in html:
        print(f"Fixing container in {filepath}")
        html = html.replace('<main class="main-content">', '<main class="main-content">\n      <div class="container">')
        
        # Now find the last </main> or </body> to inject </div>
        if '</main>' in html:
            # use rpartition or rfind to only replace the LAST </main> just in case
            idx = html.rfind('</main>')
            if idx != -1:
                html = html[:idx] + '</div>\n    ' + html[idx:]
        else:
            # fallback: before </body>
            idx = html.rfind('</body>')
            if idx != -1:
                html = html[:idx] + '</div>\n    </main>\n' + html[idx:]

        changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Successfully wrote {filepath}")

for f in os.listdir('CMS-webpage/wireframe_site'):
    if f.endswith('.html'):
        check_and_fix('CMS-webpage/wireframe_site/' + f)

