import io

fp = "CMS-webpage/wireframe_site/device-editor.html"
with io.open(fp, 'r', encoding='utf-8') as f:
    orig = f.read()

res = orig.replace(
    '<div style="display: grid; grid-template-columns: 140px 1fr; gap: 16px 24px; align-items: start;">',
    '<div style="display: flex; flex-direction: column; gap: 16px;">'
).replace(
    '<div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">MAC Address:</div>\n                <input type="text" class="input" style="width:100%; font-family:monospace" value="">',
    '<div class="form-group">\n                <label class="form-label required">MAC Address</label>\n                <input type="text" class="input" style="width:100%; font-family:monospace" value="">\n              </div>'
).replace(
    '<div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">Product:</div>\n                  <select class="input" style="width:100%">',
    '<div class="form-group">\n                <label class="form-label required">Product</label>\n                <select class="input" style="width:100%">'
).replace(
    '<option value="prod-02">Product B</option>\n                  </select>',
    '<option value="prod-02">Product B</option>\n                </select>\n              </div>'
).replace(
    '<div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">Package:</div>\n                  <select class="input" style="width:100%">',
    '<div class="form-group">\n                <label class="form-label required">Package</label>\n                <select class="input" style="width:100%">'
).replace(
    '<option value="pkg-02">Package v2.0</option>\n                  </select>',
    '<option value="pkg-02">Package v2.0</option>\n                </select>\n              </div>'
).replace(
    '<div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">Stores:</div>\n                <select class="input" style="width:100%;">',
    '<div class="form-group">\n                <label class="form-label required">Stores</label>\n                <select class="input" style="width:100%;">'
).replace(
    '<option value="store-02">Store-02</option>\n                </select>',
    '<option value="store-02">Store-02</option>\n                </select>\n              </div>'
).replace(
    '<div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">인증 모드 / 라이선스:</div>\n                <div>',
    '<div class="form-group">\n                <label class="form-label required">인증 모드 / 라이선스</label>\n                <div>'
)

# wait, adding ending div for the auth block logic
# we also need the last one for "Name:"
res = res.replace(
    '<div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">Name:</div>\n                  <input type="text" class="input" style="width:100%" value="Device-A">\n                </div>',
    '<div class="form-group">\n                  <label class="form-label required">Name</label>\n                  <input type="text" class="input" style="width:100%" value="Device-A">\n                </div>'
)

# also need to close the div for "인증 모드 / 라이선스:" properly inside the block
# The original block has:
#                 </div>   <-- this closes the inner div of auth mode? Actually Let's verify original HTML for Name and auth mode.
with io.open(fp, 'w', encoding='utf-8') as f:
    f.write(res)
print("done")
