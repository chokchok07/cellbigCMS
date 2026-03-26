import os
import textwrap
from PIL import Image, ImageDraw, ImageFont


def strip_md(md: str) -> str:
    lines = []
    in_code = False
    for l in md.splitlines():
        if l.strip().startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        s = l.lstrip('#').strip()
        if s.startswith('- '):
            s = s[2:]
        lines.append(s)
    return '\n'.join(lines).strip()


def render_text_to_image(text: str, title: str, outpath: str, width: int = 1200, padding: int = 40, font_path: str | None = None):
    title_size = 28
    font_size = 20
    try:
        if font_path and os.path.exists(font_path):
            title_font = ImageFont.truetype(font_path, title_size)
            font = ImageFont.truetype(font_path, font_size)
        else:
            title_font = ImageFont.load_default()
            font = ImageFont.load_default()
    except Exception:
        title_font = ImageFont.load_default()
        font = ImageFont.load_default()

    # Prepare wrapped lines
    wrapper = textwrap.TextWrapper(width=80)
    paragraphs = [p for p in text.split('\n\n') if p.strip()]
    lines = []
    for p in paragraphs:
        lines.extend(wrapper.wrap(p))
        lines.append('')

    # Estimate heights (use a temporary draw to support Pillow versions)
    tmp_img = Image.new('RGB', (10, 10), 'white')
    tmp_draw = ImageDraw.Draw(tmp_img)
    sample_bbox = tmp_draw.textbbox((0, 0), 'Ay', font=font)
    line_height = (sample_bbox[3] - sample_bbox[1]) + 6
    title_bbox = tmp_draw.textbbox((0, 0), 'Ay', font=title_font)
    title_height = (title_bbox[3] - title_bbox[1]) + 10
    total_height = padding + title_height + max(200, len(lines) * line_height) + padding

    img = Image.new('RGB', (width, total_height), 'white')
    draw = ImageDraw.Draw(img)

    x = padding
    y = padding
    draw.text((x, y), title, font=title_font, fill='black')
    y += title_height + 10

    for ln in lines:
        draw.text((x, y), ln, font=font, fill='black')
        y += line_height

    img.save(outpath)


def main():
    base = os.path.join('CMS-webpage', 'wireframe')
    outdir = os.path.join(base, 'images')
    os.makedirs(outdir, exist_ok=True)
    font_path = 'C:\\Windows\\Fonts\\arial.ttf'

    md_files = [f for f in os.listdir(base) if f.endswith('.md')]
    for fname in md_files:
        path = os.path.join(base, fname)
        with open(path, 'r', encoding='utf-8') as fh:
            md = fh.read()
        txt = strip_md(md)
        title = os.path.splitext(fname)[0]
        outpath = os.path.join(outdir, f'{title}.png')
        render_text_to_image(txt or title, title, outpath, width=1200, font_path=font_path)
        print('WROTE', outpath)


if __name__ == '__main__':
    main()
