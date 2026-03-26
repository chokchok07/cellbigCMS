const fs = require('fs');
let html = fs.readFileSync('schema.html', 'utf8');

// 1. Mermaid module fix
html = html.replace(/<script type="module">[\s\S]*?<\/script>/, `<script src="https://cdn.jsdelivr.net/npm/mermaid@10.6.1/dist/mermaid.min.js"></script>
    <script>
        document.addEventListener("DOMContentLoaded", () => {
            mermaid.initialize({ startOnLoad: true, theme: 'default' });
        });
    </script>`);

// 2. Add Links to FKs
html = html.replace(/<span class="fk">area_id<\/span>/g, '<a href="#tb-local-area" class="fk-link">🔗 area_id</a>');
html = html.replace(/<span class="fk">store_id<\/span>/g, '<a href="#tb-store" class="fk-link">🔗 store_id</a>');
html = html.replace(/<span class="fk">product_id<\/span>/g, '<a href="#tb-product" class="fk-link">🔗 product_id</a>');
html = html.replace(/<span class="fk">device_id<\/span>/g, '<a href="#tb-device" class="fk-link">🔗 device_id</a>');
html = html.replace(/<span class="fk">package_id<\/span>/g, '<a href="#tb-package" class="fk-link">🔗 package_id</a>');

// For multi-keys
html = html.replace(/<span class="pk">package_id<\/span><\/td><td><span class="type-badge">VARCHAR\(50\)<\/span><\/td><td>PK, FK<\/td>/g, 
  '<a href="#tb-package" class="fk-link" style="color:var(--pk-color);">🔗 package_id</a></td><td><span class="type-badge">VARCHAR(50)</span></td><td>PK, FK</td>');
html = html.replace(/<span class="pk">content_id<\/span><\/td><td><span class="type-badge">VARCHAR\(50\)<\/span><\/td><td>PK, FK<\/td>/g, 
  '<a href="#tb-content" class="fk-link" style="color:var(--pk-color);">🔗 content_id</a></td><td><span class="type-badge">VARCHAR(50)</span></td><td>PK, FK</td>');

// 3. Add CSS
if(!html.includes('.fk-link')) {
    html = html.replace('</style>', `
        .fk-link { color: #047857; font-weight: bold; text-decoration: none; border-bottom: 1px dashed #047857; }
        .fk-link:hover { background-color: #d1fae5; color: #065f46; }
    </style>`);
}

fs.writeFileSync('schema.html', html);
console.log('Successfully updated schema!');
