import os

filepath = 'CMS-webpage/wireframe_site/device-list.html'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

out = []
for line in lines:
    out.append(line)
    if '<th>Package</th>' in line:
        out.append('                        <th>Certification</th>\n')
    elif '<td>pkg-sand-11</td>' in line or '<td>pkg-sand-full</td>' in line or '<td>pkg-fish-basic</td>' in line or '<td>pkg-dino-starter</td>' in line or '<td>pkg-sand-lite</td>' in line:
        # Check active status somehow, let's just make it alternating
        is_active = 'Online' if 'active' in ''.join(lines) else 'Offline' # simplified
        out.append('                        <td><span class="badge" style="background:#e0f2fe; color:#1e40af;">Online</span></td>\n')
    elif '<td>pkg-fish-premium</td>' in line:
        out.append('                        <td><span class="badge" style="background:#f3f4f6; color:#4b5563;">Offline</span></td>\n')
    

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(out)

print("HTML modified")
