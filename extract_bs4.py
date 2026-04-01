from bs4 import BeautifulSoup
with open('CMS-webpage/wireframe_site/content-editor.bak.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

modal = soup.find(id='newVersionModal')
if modal:
    # also add the comment manually
    with open('extracted_modal.html', 'w', encoding='utf-8') as mf:
        mf.write('<!-- New Version Modal -->\n' + str(modal))
    print(len(str(modal)))
else:
    print('Modal not found via bs4')
