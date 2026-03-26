import codecs

filepath = 'CMS-webpage/wireframe_site/device-list.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    html = f.read()

html = html.replace("onclick=\"window.location.href='device-detail.html'\">+ Register Device</button>", "onclick=\"window.location.href='device-editor.html'\">+ Register Device</button>")

with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(html)
