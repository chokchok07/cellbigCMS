from bs4 import BeautifulSoup
import re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

cards = soup.find_all('div', class_='card')

for card in cards:
    # Check if this card looks like a version card (has grid-template-columns: 2fr 1fr 1fr 1fr)
    grid_div = card.find('div', style=lambda s: s and 'grid-template-columns' in s)
    if not grid_div:
        continue
    
    # Check the 3rd column (index 2 as it's 2fr 1fr 1fr 1fr => total 4 items?? No wait, let's just find the buttons div)
    # Usually it's the last direct child div of grid_div
    cols = grid_div.find_all('div', recursive=False)
    if len(cols) >= 3:
        col3 = cols[-1] # The actions column
        
        # Look for the div containing the buttons
        # Sometimes there's no div for buttons if it's deprecated, let's ensure one exists
        action_div = col3.find('div', style=lambda s: s and 'gap:8px' in s)
        if action_div:
            # Overwrite its contents
            action_div.clear()
            download_btn = soup.new_tag('button', **{'class': 'btn btn-outline', 'style': 'padding:4px 8px; font-size:12px;'})
            download_btn.string = '⬇️ Download'
            
            change_status_btn = soup.new_tag('button', **{'class': 'btn btn-secondary', 'style': 'padding:4px 8px; font-size:12px;'})
            change_status_btn.string = 'Change Status'
            
            action_div.append(download_btn)
            action_div.append(change_status_btn)
        else:
            # If no action_div, create one
            new_action_div = soup.new_tag('div', style='display:flex; gap:8px; align-items:center;')
            download_btn = soup.new_tag('button', **{'class': 'btn btn-outline', 'style': 'padding:4px 8px; font-size:12px;'})
            download_btn.string = '⬇️ Download'
            
            change_status_btn = soup.new_tag('button', **{'class': 'btn btn-secondary', 'style': 'padding:4px 8px; font-size:12px;'})
            change_status_btn.string = 'Change Status'
            
            new_action_div.append(download_btn)
            new_action_div.append(change_status_btn)
            col3.append(new_action_div)
            
        # Re-apply the onclick handler
        # Find version_span
        version_span = card.find('span', style=lambda s: s and 'font-size:20px' in s)
        if not version_span:
            version_span = card.find('span', string=re.compile(r'v\d+\.\d+'))
            
        version_txt = version_span.get_text(strip=True) if version_span else 'Unknown'
        
        badge = card.find('span', class_=re.compile(r'badge'))
        current_status = badge.get_text(strip=True).lower() if badge else 'test'
        
        change_status_btn['onclick'] = f"openVersionStatusModal(this, '{version_txt}', '{current_status}')"

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    # bs4 prettify might break some things, I will just str()
    f.write(str(soup).replace('&times;', '×'))

print("Unified buttons across all version cards!")
