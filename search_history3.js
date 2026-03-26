const fs = require('fs');
const path = require('path');

const historyDir = 'C:/Users/user/AppData/Roaming/Code/User/History';
if (!fs.existsSync(historyDir)) {
    console.error('History dir not found');
    process.exit(1);
}

const targetDirs = [];
const dirs = fs.readdirSync(historyDir);

for (const dir of dirs) {
    const dirPath = path.join(historyDir, dir);
    if (!fs.statSync(dirPath).isDirectory()) continue;
    const entriesPath = path.join(dirPath, 'entries.json');
    if (fs.existsSync(entriesPath)) {
        try {
            const entriesData = JSON.parse(fs.readFileSync(entriesPath, 'utf-8'));
            if (entriesData.entries) {
                for (const entry of entriesData.entries) {
                    const filePath = path.join(dirPath, entry.id);
                    if (fs.existsSync(filePath)) {
                        const content = fs.readFileSync(filePath, 'utf-8');
                        if (content.includes('홍길동') || content.toLowerCase().includes('welcome')) {
                            targetDirs.push({ filePath, timestamp: entry.timestamp, content, resource: entriesData.resource });
                        }
                    }
                }
            }
        } catch (e) {}
    }
}

targetDirs.sort((a, b) => b.timestamp - a.timestamp);

if (targetDirs.length > 0) {
    console.log('FOUND RESOURCE:', targetDirs[0].resource);
    console.log('FOUND PATH:', targetDirs[0].filePath);
    console.log('CONTENT_START');
    console.log(targetDirs[0].content);
    console.log('CONTENT_END');
} else {
    console.log('Not found at all globally');
}
