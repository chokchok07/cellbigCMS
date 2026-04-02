import sys
html = open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8').read()
js = '''<script>
function openNewVersionModal() {
    document.getElementById('newVersionModal').style.display = 'flex';
}
function closeNewVersionModal() {
    document.getElementById('newVersionModal').style.display = 'none';
}
function handleNewVersionFileSelect(e) {
    if (e.target.files && e.target.files.length > 0) {
        var file = e.target.files[0];
        document.getElementById('newVersionFileName').textContent = file.name;
        document.getElementById('newVersionFileSize').textContent = (file.size / (1024*1024)).toFixed(2) + ' MB';
        document.getElementById('verifyFileBtn').disabled = false;
        document.getElementById('verifyFileBtn').style.opacity = '1';
        document.getElementById('verifyFileBtn').style.cursor = 'pointer';
    }
}
function submitNewVersion() {
    alert('버전이 등록되었습니다.');
    closeNewVersionModal();
}
</script>'''

if 'function openNewVersionModal(' not in html:
    html = html.replace('</body>', js + '\n</body>')
    with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('js added')
