import codecs

filepath = 'CMS-webpage/wireframe_site/localarea-list.html'
with codecs.open(filepath, 'r', 'utf-8') as f:
    html = f.read()

bad_str = "    // Register LocalArea button\r\n    document.querySelector('.btn-primary').addEventListener('click', function() \n{\n        window.location.href = 'localarea-editor.html';\n    // Apply Filters button"

html = html.replace("window.location.href = 'localarea-editor.html';\r\n    // Apply Filters button", "window.location.href = 'localarea-editor.html';\n      });\n\n      // Apply Filters button")
html = html.replace("window.location.href = 'localarea-editor.html';\n    // Apply Filters button", "window.location.href = 'localarea-editor.html';\n      });\n\n      // Apply Filters button")

html = html.replace("window.location.href = 'localarea-editor.html';\r\n      // Apply Filters button", "window.location.href = 'localarea-editor.html';\n      });\n\n      // Apply Filters button")


with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(html)
