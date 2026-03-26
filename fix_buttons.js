const fs = require('fs');
const path = require('path');
const dir = 'CMS-webpage/wireframe_site';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html') && f.includes('-editor.html'));

let count = 0;
for (const file of files) {
  const fp = path.join(dir, file);
  let content = fs.readFileSync(fp, 'utf8');
  
  // It seems Cancel button has class btn-secondary.
  if (!content.includes('>Inactive</button>')) {
    content = content.replace(
      /(<button[^>]*>Cancel<\/button>)/i,
      `<button type="button" class="btn btn-danger" onclick="openInactiveModal()">Inactive</button>\n            $1`
    );
    fs.writeFileSync(fp, content, 'utf8');
    count++;
  }
}
console.log('Fixed', count);
