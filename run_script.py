import subprocess

result = subprocess.run(['python', 'fix_emojis_content.py'], capture_output=True, text=True, encoding='utf-8')
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(result.stdout)
