import io

with open('CMS-webpage/wireframe_site/styles.css', 'r', encoding='utf-8') as f:
    text = f.read()

with open('dump_styles_css.txt', 'w', encoding='utf-8') as out:
    out.write(text)
