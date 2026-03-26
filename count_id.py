import io

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    text = f.read()

with open('count_id.txt', 'w', encoding='utf-8') as out:
    out.write(str(text.count('id="versionModal"')))
