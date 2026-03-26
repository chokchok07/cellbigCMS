const fs = require('fs');
const path = require('path');
const dir = 'CMS-webpage/wireframe_site';

const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

for (const file of files) {
  const fp = path.join(dir, file);
  let content = fs.readFileSync(fp, 'utf8');
  let changed = false;

  // 1. Revert editors: remove Active/Inactive buttons from header-actions
  if (file.includes('-editor.html') || file.includes('edit')) {
    // Remove the dynamically added buttons
    const activeInactiveRx = /<button[^>]*>Active<\/button>\s*<button[^>]*>Inactive<\/button>/gi;
    if (activeInactiveRx.test(content)) {
      content = content.replace(activeInactiveRx, '');
      changed = true;
    }
    
    // In case there is an old Inactive button left over next to cancel
    const singleInactiveRx = /<button[^>]*>Inactive<\/button>\s*(?=<button[^>]*>Cancel<\/button>)/gi;
    if (singleInactiveRx.test(content)) {
      content = content.replace(singleInactiveRx, '');
      changed = true;
    }
  }

  // 2. In list pages, update the action buttons to use openStatusModal
  if (file.includes('-list.html')) {
    // Usually lists have buttons like <button class="..." onclick="...">Active</button>
    // We want to replace whatever onclick they have with onclick="openStatusModal('inactive')"
    
    content = content.replace(/<button([^>]*)>Inactive<\/button>/gi, (match, p1) => {
        // Strip existing onclick
        let attrs = p1.replace(/onclick="[^"]*"/g, '').replace(/onclick='[^']*'/g, '');
        return `<button ${attrs} onclick="openStatusModal('inactive')">Inactive</button>`;
    });
    
    content = content.replace(/<button([^>]*)>Active<\/button>/gi, (match, p1) => {
        let attrs = p1.replace(/onclick="[^"]*"/g, '').replace(/onclick='[^']*'/g, '');
        return `<button ${attrs} onclick="openStatusModal('active')">Active</button>`;
    });
    
    changed = true;
  }
  
  if (changed) {
    fs.writeFileSync(fp, content, 'utf8');
  }
}
console.log('Fixed editors and lists!');