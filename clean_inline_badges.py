import re
import glob

for filepath in glob.glob('CMS-webpage/wireframe_site/*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    original = text
    # Clean up hardcoded inline spans for Published, Test, Unpublished statuses in any table cell or general context
    text = re.sub(r'<span[^>]*style="[^"]*?(?:#dcfce7|#10b981|#1d4ed8)[^"]*"[^>]*>Published(?: \(?[^)]*\))?</span>', '<span class=\"badge badge-published\">Published</span>', text)
    text = re.sub(r'<span[^>]*style="[^"]*?(?:#fef3c7|#f59e0b|#047857)[^"]*"[^>]*>Test(?: \(?[^)]*\))?</span>', '<span class=\"badge badge-test\">Test</span>', text)
    text = re.sub(r'<span[^>]*style="[^"]*?(?:#f3f4f6|#6b7280)[^"]*"[^>]*>Unpublished(?: \(?[^)]*\))?</span>', '<span class=\"badge badge-unpublished\">Unpublished</span>', text)
    
    # Also catch some basic ones without regex capturing too broadly
    text = re.sub(r'<span style="color:#10b981">🟢 Published</span>', '<span class=\"badge badge-published\">Published</span>', text)
    text = re.sub(r'<span style="color:#f59e0b">🟡 Test</span>', '<span class=\"badge badge-test\">Test</span>', text)
    text = re.sub(r'<span style="color:#6b7280">⚪ Unpublished</span>', '<span class=\"badge badge-unpublished\">Unpublished</span>', text)
    
    if text != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Cleaned inline styles in {filepath}")
