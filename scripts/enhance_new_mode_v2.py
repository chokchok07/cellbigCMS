import os, glob

for file in glob.glob('CMS-webpage/wireframe_site/*-detail.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to fix the JS injection
    # Replace the old bad injection first
    import re
    content = re.sub(r'// Auto-generate ID placeholder.*?window\.location\.href = location\.pathname\.replace\(\'-detail\', \'-list\'\); \};\n\s*\}', '', content, flags=re.DOTALL)
    
    # And then insert the right one inside `if (!urlParams.has('id')) {`
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

            // Re-purpose Delete and Save buttons for New Mode
            const btnPrimary = document.querySelector('.btn-primary');
            if (btnPrimary && titleEl) {
                const objName = titleEl.textContent.replace('✨ Create New ', '').trim();
                btnPrimary.innerHTML = '✨ Save ' + objName;
                btnPrimary.onclick = function() { 
                    alert(objName + ' created successfully!'); 
                    window.location.href = location.pathname.replace('-detail', '-list'); 
                };
            }
            
            // Delete button was hidden by previous scripts. Un-hide it and turn into Cancel.
            const deleteBtn = document.querySelector('.btn-secondary');
            if (deleteBtn) {
                deleteBtn.style.display = 'inline-block';
                deleteBtn.innerHTML = '✕ Cancel';
                deleteBtn.style.color = '#4b5563';
                deleteBtn.style.borderColor = '#d1d5db';
                deleteBtn.onclick = function() { history.back(); };
            }
"""
    # Wait, the previous code also had this line:
    # "if (deleteBtn) deleteBtn.style.display = 'none';"
    # I should remove or overwrite that.
    
    content = content.replace("if (deleteBtn) deleteBtn.style.display = 'none';", "")

    target = "if (metaSection) metaSection.style.display = 'none';"
    if target in content and "Auto-generate ID" not in content:
        content = content.replace(target, target + "\n" + injection)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {file}")
