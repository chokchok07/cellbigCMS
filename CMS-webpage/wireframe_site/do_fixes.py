import codecs

def fix_file(filename):
    with codecs.open(filename, 'r', 'utf-8') as f:
        text = f.read()

    text = text.replace(r"href=\'content-detail", "href='content-detail")
    text = text.replace(r"101\'", "101'")
    text = text.replace(r"href=\'content-versions", "href='content-versions")

    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(text)

fix_file('content-list.html')
print("Fixed slashes")
