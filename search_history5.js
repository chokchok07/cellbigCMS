const fs = require('fs');
const path = require('path');

const historyDir = 'C:/Users/user/AppData/Roaming/Code/User/History';

const targetDirs = [];
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
                            const content = fs.readFileSync(filePath, 'utf-8');
                            // Even if it's garbled, just store the most recent one.
                            targetDirs.push({ filePath, timestamp: entry.timestamp, content });
                        }
                    }
                }
            }
        } catch (e) {}
    }
}

targetDirs.sort((a, b) => b.timestamp - a.timestamp);

let bestMatch = null;
for (const cand of targetDirs) {
    if (cand.content.includes('홍길동') || cand.content.toLowerCase().includes('welcome')) {
        bestMatch = cand;
        break;
    }
}

if (!bestMatch && targetDirs.length > 0) {
    bestMatch = targetDirs[0];
}

if (bestMatch) {
    fs.writeFileSync('js_result_5.txt', bestMatch.content, 'utf-8');
} else {
    fs.writeFileSync('js_result_5.txt', 'NO INDEX.HTML FOUND', 'utf-8');
}
