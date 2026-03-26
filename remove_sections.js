const fs = require('fs');
let content = fs.readFileSync('api.html', 'utf8');

// 1. Remove "공지사항 관리 (Notices)" section
const noticeStart = content.indexOf('<h3>공지사항 관리 (Notices)</h3>');
const telemetryStart = content.indexOf('<h2>4. Logging & Telemetry API</h2>');

if (noticeStart !== -1 && telemetryStart !== -1) {
    content = content.slice(0, noticeStart) + content.slice(telemetryStart);
}

// 2. Remove "Logging & Telemetry API" section
const telemetryStartUpdated = content.indexOf('<h2>4. Logging & Telemetry API</h2>');
if (telemetryStartUpdated !== -1) {
    // The section goes until the closing </div> of container or </body>
    const bodyClose = content.indexOf('</body>');
    const lastDiv = content.lastIndexOf('</div>', bodyClose);
    
    // We basically want to remove everything from telemetryStartUpdated until the closing tags
    // Let's just slice until the end of the container div
    content = content.slice(0, telemetryStartUpdated) + '\n    </div>\n</body>\n</html>';
}

// 3. Remove them from the Table of Contents (TOC)
content = content.replace(/<li[^>]*>.*?공지사항 관리 \(Notices\).*?<\/li>/gs, '');
content = content.replace(/<li[^>]*>.*?4\. Logging &amp; Telemetry API.*?<\/li>/gs, '');

fs.writeFileSync('api.html', content);
console.log('Removed Notices and Telemetry/Logs sections from api.html');
