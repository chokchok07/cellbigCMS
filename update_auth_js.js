const fs = require('fs');

const editorFile = 'CMS-webpage/wireframe_site/device-editor.html';
let html = fs.readFileSync(editorFile, 'utf8');

const jsInjection = `
      function toggleAuthMode() {
        const mode = document.getElementById('authMode')?.value;
        const offlineSec = document.getElementById('offline-keygen-section');
        if(!offlineSec) return;
        
        if (mode === 'OFFLINE') {
          offlineSec.style.display = 'block';
        } else {
          offlineSec.style.display = 'none';
        }
      }
      
      function generateLicenseKey() {
        alert('시리얼 키를 생성했습니다.');
        const el = document.getElementById('generatedLicense');
        if(el) el.value = 'CBIG-A1B2-C3D4-E5F6'; // MOCK
      }
`;

if(!html.includes('toggleAuthMode')) {
    html = html.replace('</script>\n</body>', jsInjection + '\n</script>\n</body>');
    fs.writeFileSync(editorFile, html);
    console.log('Injected js');
}
