import re
html = open('CMS-webpage/wireframe_site/package-detail.html', 'r', encoding='utf-8').read()

out = []
# Find all modal-overlay divs
modals = re.findall(r'<div[^>]*class="modal-overlay"[^>]*>', html)
out.append("MODALS:")
out.extend(modals)

# Find button that opens the modal (e.g. Manage)
manages = re.findall(r'<button[^>]*>Manage<\/button>', html, re.IGNORECASE)
out.append("\nMANAGE BUTTONS:")
out.extend(manages)

# Find the Done button
dones = re.findall(r'<button[^>]*>Done<\/button>', html, re.IGNORECASE)
out.append("\nDONE BUTTONS:")
out.extend(dones)

# Output all functions that might be related
funcs = re.findall(r'function \w+\([^\)]*\)\s*\{[^\}]+\}', html)
out.append("\nFUNCTIONS (partial):")
for f in funcs:
    if 'manage' in f.lower() or 'modal' in f.lower():
        out.append(f.split('\n')[0])

with open('debug_ultimate.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
