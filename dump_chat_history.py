import sqlite3
import json
import datetime
import re

db_path = r"C:\Users\user\AppData\Roaming\Code\User\globalStorage\state.vscdb"
try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT value FROM ItemTable WHERE key LIKE 'github.copilot.chat.%'")
    rows = c.fetchall()
    prompts = []
    
    for row in rows:
        val = row[0]
        # Just use regex to find all "prompt": "..." or "value": "..." where user types
        # Often it is stored under nested JSON
        matches = re.findall(r'"message"\s*:\s*"(.*?)"', val)
        if matches:
            for m in matches:
                prompts.append(m)
        matches2 = re.findall(r'"value"\s*:\s*"(.*?)"', val)
        if matches2:
            for m in matches2:
                prompts.append(m)
                
    with open('chat_prompts_dump.txt', 'w', encoding='utf-8') as f:
        for p in prompts:
            # unescape JSON strings
            p_unescaped = p.replace('\\"', '"').replace('\\n', '\n')
            f.write(p_unescaped + "\n------------------------\n")
            
    print("Dumped", len(prompts), "prompts.")
except Exception as e:
    print("Error:", e)
