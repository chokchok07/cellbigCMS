import re

def remove_category_from_list():
    with open('CMS-webpage/wireframe_site/content-list.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Remove Filter Group for Category
    filter_pattern = re.compile(
        r'<div class="filter-group">\s*<label>Category</label>\s*<select class="input".*?>.*?</select>\s*</div>',
        re.DOTALL
    )
    text = filter_pattern.sub('', text)

    # 2. Remove Category input from New Content Modal
    modal_pattern = re.compile(
        r'<div class="form-group" style="flex:1;">\s*<label class="form-label required"[^>]*>Category \(카테고리\)</label>\s*<select class="input".*?>.*?</select>\s*</div>',
        re.DOTALL
    )
    text = modal_pattern.sub('', text)

    with open('CMS-webpage/wireframe_site/content-list.html', 'w', encoding='utf-8') as f:
        f.write(text)

def remove_category_from_editor():
    with open('CMS-webpage/wireframe_site/content-editor.html', 'r', encoding='utf-8') as f:
        text = f.read()

    # The editor has:
    # <div>
    # <label class="form-label required">Category</label>
    # <select class="input" id="category" style="width:100%">
    #   ...
    # </select>
    # </div>
    
    editor_pattern = re.compile(
        r'<div>\s*<label class="form-label required">Category</label>\s*<select class="input" id="category".*?>.*?</select>\s*</div>',
        re.DOTALL
    )
    text = editor_pattern.sub('', text)

    with open('CMS-webpage/wireframe_site/content-editor.html', 'w', encoding='utf-8') as f:
        f.write(text)

remove_category_from_list()
remove_category_from_editor()

print("Category fields removed successfully.")
