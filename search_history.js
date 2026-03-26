const fs = require('fs');
const path = require('path');

const historyDir = 'C:/Users/user/AppData/Roaming/Code/User/History';
if (!fs.existsSync(historyDir)) {
    console.error('History dir not found');
    process.exit(1);
}

let targetDirs = [];
const dirs = fs.readdirSync(historyDir);

for (const dir of dirs) {
    const dirPath = path.join(historyDir, dir);
    if (!fs.statSync(dirPath).isDirectory()) continue;
    const entriesPath = path.join(dirPath, 'entries.json');
    if (fs.existsSync(entriesPath)) {
        try {
            const entriesData = JSON.parse(fs.readFileSync(entriesPath, 'utf-8'));
            if (entriesData.resource && entriesData.resource.endsWith('index.html')) {
                if (entriesData.entries) {
                    for (const entry of entriesData.entries) {
                        const filePath = path.join(dirPath, entry.id);
                        if (fs.existsSync(filePath)) {
                            targetDirs.push({ filePath, timestamp: entry.timestamp });
                        }
                    }
                }
            }
        } catch (e) {
            // ignore
        }
    }
}

targetDirs.sort((a, b) => b.timestamp - a.timestamp);

let foundPath = null;
for (const entry of targetDirs) {
    const content = fs.readFileSync(entry.filePath, 'utf-8');
    if (content.includes('홍길동') || content.toLowerCase().includes('welcome')) {
        foundPath = entry.filePath;
        break;
    }
}

if (foundPath) {
    console.log('FOUND:', foundPath);
    console.log('CONTENT_START');
    console.log(fs.readFileSync(foundPath, 'utf-8'));
    console.log('CONTENT_END');
} else {
    console.log('Not found');
}
