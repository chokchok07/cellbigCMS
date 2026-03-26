import os, re

file_path = 'CMS-webpage/wireframe_site/content-versions.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Add explicit guarantees to inner modal
text = text.replace(
    'class="v-modal" style="background:#fff; border-radius:8px; width:600px; max-width:90vw; box-shadow:0 4px 20px rgba(0,0,0,0.2);"',
    'class="v-modal" style="display:block !important; background:#fff !important; border-radius:8px; width:600px; max-width:90vw; box-shadow:0 4px 20px rgba(0,0,0,0.2); z-index:10005; opacity:1 !important; visibility:visible !important;"'
)

# And to make double sure about overlay
text = text.replace(
    'class="v-modal-overlay" id="versionModal" style="display: none; align-items:center; justify-content:center; z-index:9999;"',
    'class="v-modal-overlay" id="versionModal" style="display: none; position:fixed; top:0; left:0; width:100%; height:100%; align-items:center; justify-content:center; z-index:9999; background:rgba(0,0,0,0.5);"'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Forced display styles applied.")
