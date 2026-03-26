const fs = require('fs');
const path = require('path');

const dir = 'CMS-webpage/wireframe_site';

// Use content-editor.html as the source of truth for header and aside shapes
const sourceTruth = fs.readFileSync(path.join(dir, 'content-editor.html'), 'utf8');

const headerMatch = sourceTruth.match(/<header.*?<\/header>/is);
if (!headerMatch) throw new Error("Header not found in source");
const headerHTML = headerMatch[0];

// The layout the user wants for sidebar: NO dashboard, NO reports.
const sidebarTemplate = `    <aside class="sidebar">
      <div class="sidebar-category">Infrastructure (Location)</div>
      <div class="sidebar-item {localarea_active}" data-page="localarea-list.html">🏢 LocalAreas</div>
      <div class="sidebar-item {store_active}" data-page="store-list.html">🏪 Stores</div>
      
      <div class="sidebar-category">Device & Monitoring</div>
      <div class="sidebar-item {device_active}" data-page="device-list.html">🖥️ Devices</div>
      <div class="sidebar-item {access_log_active}" data-page="log-content-access.html">📊 Access Logs</div>

      <div class="sidebar-category">Contents & Product</div>
      <div class="sidebar-item {product_active}" data-page="product-list.html">📦 Product</div>
      <div class="sidebar-item {serial_active}" data-page="serial-list.html">🔑 Licenses (Serial)</div>
      <div class="sidebar-item {package_active}" data-page="package-list.html">🎒 Package</div>
      <div class="sidebar-item {content_active}" data-page="content-list.html">🎬 Content</div>
      
      <div class="sidebar-category">System</div>
      <div class="sidebar-item {settings_active}" data-page="settings.html">⚙️ Settings</div>

      <div class="sidebar-category">Help</div>
      <div class="sidebar-item {overview_active}" data-page="overview.html">📘 Overview</div>
    </aside>`;

const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

let updated = 0;
for (const file of files) {
    const fPath = path.join(dir, file);
    let content = fs.readFileSync(fPath, 'utf8');
    
    // 1. Determine active menu item
    let mapping = {
        localarea_active: '', store_active: '', device_active: '',
        access_log_active: '', product_active: '', serial_active: '',
        package_active: '', content_active: '', settings_active: '', overview_active: ''
    };
    
    if (file.includes('localarea')) mapping.localarea_active = 'active';
    else if (file.includes('store')) mapping.store_active = 'active';
    else if (file.includes('device')) mapping.device_active = 'active';
    else if (file.includes('log-content-access')) mapping.access_log_active = 'active';
    else if (file.includes('product')) mapping.product_active = 'active';
    else if (file.includes('serial')) mapping.serial_active = 'active';
    else if (file.includes('package')) mapping.package_active = 'active';
    else if (file.includes('content') && !file.includes('log-')) mapping.content_active = 'active';
    else if (file.includes('settings')) mapping.settings_active = 'active';
    else if (file.includes('overview') || file.includes('index') || file.includes('dashboard')) mapping.overview_active = 'active'; // Default highlight for index? No dashboard page left.

    let newSidebar = sidebarTemplate;
    for (const [k, v] of Object.entries(mapping)) {
        newSidebar = newSidebar.replace(`{${k}}`, v ? 'active' : '');
    }
    // Clean up empty braces in sidebar-item class lists
    newSidebar = newSidebar.replace(/class="sidebar-item "/g, 'class="sidebar-item"');

    // 2. Replace Header
    let newContent = content.replace(/<header.*?<\/header>/is, headerHTML);
    
    // 3. Replace Sidebar
    newContent = newContent.replace(/<aside class="sidebar">.*?<\/aside>/is, newSidebar);

    if (content !== newContent) {
        fs.writeFileSync(fPath, newContent, 'utf8');
        updated++;
    }
}

console.log("Files updated:", updated);