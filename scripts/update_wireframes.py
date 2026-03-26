import re
import os

def update_wireframes():
    base_dir = r"CMS-webpage\wireframe_site"

    # 1. Update log-content-access.html
    log_path = os.path.join(base_dir, 'log-content-access.html')
    with open(log_path, 'r', encoding='utf-8') as f:
        log_html = f.read()
    
    # Change Table Headers
    log_headers_old = """<tr>
                        <th width="160">Timestamp</th>
                        <th>Device</th>
                        <th>Content / Action</th>
                        <th>Duration</th>
                        <th>Metadata</th>
                        <th>IP Address</th>
                    </tr>"""
    log_headers_new = """<tr>
                        <th width="160">Created At</th>
                        <th>Action Type</th>
                        <th>Target Entity</th>
                        <th>Target ID</th>
                        <th>Before Value</th>
                        <th>After Value</th>
                    </tr>"""
    # Replace dummy data rows (Just a broad stroke to replace the first row layout format)
    log_html = log_html.replace(log_headers_old, log_headers_new)
    log_html = log_html.replace('<td>dev-001 (Main Kiosk)</td>', '<td>Login / Start</td>')
    log_html = log_html.replace('<td><span class="badge" style="background:#dbeafe;color:#1e40af">START</span> Aqua Park (ver 1.2)</td>', '<td>Contents</td>\n                        <td>content_001</td>')
    log_html = log_html.replace('<td style="color:#6b7280">-</td>', '<td>null</td>\n                        <td>null</td>')
    log_html = log_html.replace('<td>{ "user": "guest" }</td>', '')
    log_html = log_html.replace('<td>192.168.1.50</td>', '')
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(log_html)

    # 2. Update notice-editor.html
    notice_path = os.path.join(base_dir, 'notice-editor.html')
    with open(notice_path, 'r', encoding='utf-8') as f:
        notice_html = f.read()

    notice_html = notice_html.replace('<label class="form-label">Type</label>', '<label class="form-label">Importance</label>')
    notice_html = notice_html.replace('<option>Info</option>', '<option>NORMAL</option>')
    notice_html = notice_html.replace('<option>Warning</option>', '<option>URGENT</option>')
    notice_html = notice_html.replace('<option>Update</option>', '')
    
    notice_html = notice_html.replace('<label class="form-label">Target Audience</label>', '<label class="form-label">Target Audience (Target Type & Display)</label>')
    notice_html = notice_html.replace('<option>All Devices</option>', '<option>ALL (All Types)</option>')
    notice_html = notice_html.replace('<option>Specific Stores</option>', '<option>AREA (Specific Area)</option>\n                        <option>STORE (Specific Store)</option>')
    notice_html = notice_html.replace('<option>Specific Groups</option>', '<option>DASHBOARD (Dashboard Only)</option>\n                        <option>POPUP (Popup Only)</option>\n                        <option>BOTH (Dashboard & Popup)</option>')

    with open(notice_path, 'w', encoding='utf-8') as f:
        f.write(notice_html)

    # 3. Update device-detail.html
    device_path = os.path.join(base_dir, 'device-detail.html')
    with open(device_path, 'r', encoding='utf-8') as f:
        device_html = f.read()
    
    device_html = device_html.replace('<p><strong>Product:</strong> CMS Player</p>', '<p><strong>Products (Array):</strong> CMS Player, Content Viewer</p>')
    device_html = device_html.replace('<p><strong>LocalArea:</strong> Store-01</p>', '<p><strong>Stores (Array):</strong> Store-01 (Main), Store-02</p>')

    hardware_panel = """
      </section>

      <section class="panel">
        <div style="display:flex;justify-content:space-between;align-items:center;">
            <h3>💻 Hardware Specifications (Meta Data)</h3>
        </div>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px; margin-top:10px;">
            <p><strong>CPU:</strong> Intel Core i7-12700</p>
            <p><strong>GPU:</strong> NVIDIA RTX 3060</p>
            <p><strong>RAM:</strong> 16GB</p>
            <p><strong>Disk Free:</strong> 450 GB</p>
            <p><strong>OS Version:</strong> Windows 10 Pro IoT</p>
            <p><strong>Resolution:</strong> 1920x1080</p>
        </div>
      </section>

      <section class="panel">"""
    
    device_html = device_html.replace('</section>\n\n      <section class="panel">', hardware_panel, 1)

    with open(device_path, 'w', encoding='utf-8') as f:
        f.write(device_html)

    # 4. Update device-editor.html
    device_ed_path = os.path.join(base_dir, 'device-editor.html')
    with open(device_ed_path, 'r', encoding='utf-8') as f:
        device_ed_html = f.read()

    device_ed_html = device_ed_html.replace('<select class="form-input">', '<select class="form-input" multiple>')
    
    with open(device_ed_path, 'w', encoding='utf-8') as f:
        f.write(device_ed_html)

    print("Updated wireframes!")

update_wireframes()
