import glob, re

for f in glob.glob('CMS-webpage/wireframe_site/*list.html'):
    text = open(f, 'r', encoding='utf-8').read()
    
    text = text.replace(r"location.href=\'", "location.href='")
    text = text.replace(r"\'\"", "'\"")
    text = text.replace(r"\'\"\"", "'\"")
    text = text.replace(r"\'\">", "'>")
    text = text.replace(r"'\"\">", "'\">")
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(text)
print('Fixed quotes!')
