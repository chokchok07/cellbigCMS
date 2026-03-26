const fs = require('fs');

let f1 = 'CMS-webpage/wireframe_site/store-list.html';
if(fs.existsSync(f1)) {
    let h1 = fs.readFileSync(f1, 'utf8');
    h1 = h1.replace(/<option value="Open">.*?<\/option>/g, '<option value="Active">Active</option>');
    h1 = h1.replace(/<option value="Closed">.*?<\/option>/g, '<option value="Inactive">Inactive</option>');
    h1 = h1.replace(/<span class="badge badge-online">Open<\/span>/g, '<span class="badge active">Active</span>');
    h1 = h1.replace(/<span class="badge badge-offline">Closed<\/span>/g, '<span class="badge inactive">Inactive</span>');
    fs.writeFileSync(f1, h1);
    console.log('store-list updated');
}

let f2 = 'CMS-webpage/wireframe_site/store-detail.html';
if(fs.existsSync(f2)) {
    let h2 = fs.readFileSync(f2, 'utf8');
    h2 = h2.replace(/>Open</g, '>Active<');
    h2 = h2.replace(/>Closed</g, '>Inactive<');
    h2 = h2.replace(/class="badge badge-online"/g, 'class="badge active"');
    h2 = h2.replace(/class="badge badge-offline"/g, 'class="badge inactive"');
    fs.writeFileSync(f2, h2);
    console.log('store-detail updated');
}

let f3 = 'CMS-webpage/wireframe_site/store-editor.html';
if(fs.existsSync(f3)) {
    let h3 = fs.readFileSync(f3, 'utf8');
    h3 = h3.replace(/>Open</g, '>Active<');
    h3 = h3.replace(/>Closed</g, '>Inactive<');
    h3 = h3.replace(/class="badge badge-online"/g, 'class="badge active"');
    h3 = h3.replace(/class="badge badge-offline"/g, 'class="badge inactive"');
    fs.writeFileSync(f3, h3);
    console.log('store-editor updated');
}
