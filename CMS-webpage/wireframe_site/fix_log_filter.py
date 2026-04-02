import re

html_file = 'log-content-access.html'
with open(html_file, 'r', encoding='utf-8') as f:
    text = f.read()

old_block = open('extracted_panel.txt', 'r', encoding='utf-8').read().strip()

new_block = '''<!-- Search/Filter Panel -->
        <div class="filter-panel">
            <div class="filter-group">
                <label>Date</label>
                <div style="display:flex;align-items:center;gap:8px;">
                    <input type="date" class="input" style="padding:6px;width:120px;" value="2023-11-01">
                    <span>~</span>
                    <input type="date" class="input" style="padding:6px;width:120px;" value="2023-11-01">
                </div>
            </div>
            
            <div class="filter-group">
                <label>LocalArea</label>
                <select class="input" style="width:140px;">
                    <option value="">All LocalAreas</option>
                    <option value="seoul">Seoul</option>
                </select>
            </div>

            <div class="filter-group">
                <label>Store</label>
                <select class="input" style="width:140px;">
                    <option value="">All Stores</option>
                    <option value="main">Main Store</option>
                </select>
            </div>

            <div class="filter-group">
                <label>Device</label>
                <select class="input" style="width:140px;">
                    <option value="">All Devices</option>
                    <option value="dev1">dev-001</option>
                </select>
            </div>

            <div class="filter-group">
                <label>Content</label>
                <select class="input" style="width:150px;">
                    <option value="">All Contents</option>
                    <option value="sand">SandCraft</option>
                </select>
            </div>

            <div class="filter-group">
                <label>Action</label>
                <select id="actionFilter" class="input" style="width:120px;">
                    <option value="">All Actions</option>
                    <option value="START">START</option>
                    <option value="STOP">STOP</option>
                    <option value="ERROR">ERROR</option>
                    <option value="HEARTBEAT">HEARTBEAT</option>
                </select>
            </div>

            <div class="filter-group">
                <label style="opacity:0">.</label>
                <button class="btn btn-secondary">Search</button>
            </div>
        </div>'''

new_text = text.replace(old_block, new_block)
if new_text != text:
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print('Replaced successfully')
else:
    print('Block not found or identical')
