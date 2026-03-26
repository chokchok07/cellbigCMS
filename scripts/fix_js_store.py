import codecs

with codecs.open('CMS-webpage/wireframe_site/store-editor.html', 'r', 'utf-8') as f:
    html = f.read()

# removing document.getElementById('devicesSection')... line
html = html.replace("document.getElementById('devicesSection').style.display = 'block';", "")
html = html.replace("document.getElementById('systemMetadataSection').style.display = 'block';", "")

with codecs.open('CMS-webpage/wireframe_site/store-editor.html', 'w', 'utf-8') as f:
    f.write(html)
print("JS fixed.")
