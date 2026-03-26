import os, glob

for file in glob.glob('CMS-webpage/wireframe_site/*-detail.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    injection = """
                // Auto-generate ID placeholder
                document.querySelectorAll('.info-label').forEach(label => {
                    if (label.textContent.includes('ID')) {
                        let nextEl = label.nextElementSibling;
                        while(nextEl && nextEl.tagName !== 'INPUT' && nextEl.tagName !== 'DIV') {
                            nextEl = nextEl.nextElementSibling;
                        }
                        if (nextEl && nextEl.tagName === 'INPUT') {
                            nextEl.value = '';
                            nextEl.placeholder = '서버에서 자동 생성됩니다';
                            nextEl.readOnly = true;
                            nextEl.style.backgroundColor = '#f3f4f6';
                            nextEl.style.color = '#9ca3af';
                        }
                    }
                });

                // Update 'Delete' and 'Save' buttons to 'Cancel' and 'Save'
                const btnDanger = document.querySelector('.action-btn-danger');
                if (btnDanger) {
                    btnDanger.innerHTML = '✕ Cancel';
                    btnDanger.onclick = function() { history.back(); };
                    btnDanger.style.backgroundColor = '#6b7280';
                    btnDanger.style.borderColor = '#6b7280';
                }
                const btnPrimary = document.querySelector('.action-btn-primary');
                if (btnPrimary && titleEl) {
                    const objName = titleEl.textContent.replace('✨ Create New ', '').trim();
                    btnPrimary.innerHTML = '💾 Save ' + objName;
                    btnPrimary.onclick = function() { alert(objName + ' created successfully!'); window.location.href = location.pathname.replace('-detail', '-list'); };
                }"""

    target = "if (metaSection) metaSection.style.display = 'none';"
    
    if target in content and "Auto-generate ID" not in content:
        content = content.replace(target, target + "\n" + injection)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Enhanced {file}")
