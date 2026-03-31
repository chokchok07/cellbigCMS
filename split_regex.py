import re

with open('CMS-webpage/wireframe_site/content-editor.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I want to find the section cards
# Cards are demarcated by <div class="card">
# I will find all indices of <div class="card">
card_starts = [m.start() for m in re.finditer(r'<div class="card">', html)]

# We need to find where each card ends. We can do a rudimentary div counter or just split.
# Actually, since cards are siblings, we can split by <div class="card">
parts = html.split('<div class="card">')
# parts[0] is everything before the first card.
# parts[1..] are the cards along with their trailing siblings until the next card.

# Wait, this is risky if there are nested cards. Let's assume no nested <div class="card">.
# Let's count them:
print(f"Found {len(parts)-1} cards")

if len(parts) == 7:
    # We know there are 6 cards:
    # 1: 기본 정보
    # 2: 애플리케이션
    # 3: 릴리즈 버전
    # 4: 초기 버전 파일 업로드
    # 5: 포함된 패키지
    # 6: 메타데이터

    # Let's verify:
    for i in range(1, 7):
        print(f"Card {i}: {parts[i][:50]}")

    # To rebuild:
    # Before cards: parts[0] (which contains the <div style="display: flex; flex-direction: column; gap: 24px;"> but wait, that flex is already wrapping it.
    
    # We will create our own wrapper.
    # parts[0] -> remove the display: flex if we can, or just append our grid inside it.
    
    # Let's append our grid inside parts[0]
    # But wait, parts[6] contains the close of parts[0]'s container.
    pass

