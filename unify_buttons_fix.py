from bs4 import BeautifulSoup
import re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

cards = soup.find_all('div', class_='card')

for card in cards:
    grid_div = card.find('div', style=lambda s: s and 'grid-template-columns' in s)
    if not grid_div:
        continue
    
    cols = grid_div.find_all('div', recursive=False)
    if len(cols) >= 3:
        col3 = cols[-1] 
        
        # Remove any existing action buttons div
        action_div = col3.find('div', style=lambda s: s and 'gap:8px' in s)
        if action_div:
            action_div.decompose()
            
        # Create a unified action div
        new_action_div = soup.new_tag('div', style='display:flex; gap:8px;')
        download_btn = soup.new_tag('button', **{'class': 'btn btn-outline', 'style': 'padding:4px 8px; font-size:12px;'})
        download_btn.string = '⬇️ Download'
        
        change_status_btn = soup.new_tag('button', **{'class': 'btn btn-secondary', 'style': 'padding:4px 8px; font-size:12px;'})
        change_status_btn.string = 'Change Status'
        
        new_action_div.append(download_btn)
        new_action_div.append(change_status_btn)
        
        # We also need to preserve or recreate the "Created: ..." info if it got destroyed?
        # Actually col3 usually has a div for info and a div for actions. 
        # By just removing action_div and appending new_action_div, we keep the info.
        col3.append(new_action_div)
            
        # Re-apply the onclick handler
        version_span = card.find('span', style=lambda s: s and 'font-size:20px' in s)
        if not version_span:
            version_span = card.find('span', string=re.compile(r'v\d+\.\d+'))
            
        version_txt = version_span.get_text(strip=True) if version_span else 'Unknown'
        
        badge = card.find('span', class_=re.compile(r'badge'))
        current_status = badge.get_text(strip=True).lower() if badge else 'deprecated'
        
        change_status_btn['onclick'] = f"openVersionStatusModal(this, '{version_txt}', '{current_status}')"

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(str(soup).replace('&times;', '×'))

print("All buttons unified successfully!")
