import re

with open('CMS-webpage/wireframe_site/content-list.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make sure basic emojis are OK, though the previous runSubagent or my command might have fixed it.
# Check what matches '?'
lines_with_q = [line for line in text.split('\n') if '?' in line]

if lines_with_q:
    print(f"Found {len(lines_with_q)} lines with '?'.")
    for l in lines_with_q:
        print(l.strip())
else:
    print("No '?' found! File is clean.")
    
