import json
import xml.etree.ElementTree as ET
import html
import re

def parse_drawio_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'data-mxgraph="([^"]+)"', content)
    if not match:
        print("No drawio data found.")
        return

    json_str = html.unescape(match.group(1))
    try:
        data = json.loads(json_str)
        xml_str = data['xml']
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return

    try:
        root = ET.fromstring(xml_str)
    except Exception as e:
        print(f"Error parsing XML: {e}")
        return

    entities = []
    
    for cell in root.iter('mxCell'):
        val = cell.get('value')
        if val:
            # simple html tag cleaner
            text = re.sub(r'<[^>]+>', '\n', val)
            text = text.replace('&nbsp;', ' ').replace('&#39;', "'")
            lines = [line.strip() for line in text.split('\n') if line.strip()]
            if lines:
                entities.append(lines)
                
    for i, entity in enumerate(entities):
        print(f"--- ENTITY {i} ---")
        for line in entity:
            print(line)

if __name__ == "__main__":
    parse_drawio_html('cellbigCMS.drawio.html')
