# Cover for the icon render: the emblem only, drawn large so it reads when small.
# Run tex.py first (it makes cover_base.png and page.png), then this.
from PIL import Image, ImageDraw, ImageFilter
import math, os
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'icon'); os.makedirs(OUT, exist_ok=True)
W, H = 1024, 1536
gold = Image.new('L', (W, H), 0); glow = Image.new('L', (W, H), 0); g = ImageDraw.Draw(gold)
g.rectangle([56, 56, W - 56, H - 56], outline=255, width=8); g.rectangle([84, 84, W - 84, H - 84], outline=255, width=3)
cx, cy = W / 2, H / 2
c = ImageDraw.Draw(glow); c.ellipse([cx - 330, cy - 330, cx + 330, cy + 330], outline=255, width=12)
for rot in (-28, 28):
    lay = Image.new('L', (W, H), 0); ImageDraw.Draw(lay).ellipse([cx - 330, cy - 116, cx + 330, cy + 116], outline=255, width=12)
    glow.paste(255, mask=lay.rotate(rot, center=(cx, cy), resample=Image.BICUBIC))
c = ImageDraw.Draw(glow)
for i in range(18):
    a = i / 18 * 2 * math.pi - math.pi / 2; x = cx + 410 * math.cos(a); y = cy + 410 * math.sin(a); c.ellipse([x - 14, y - 14, x + 14, y + 14], fill=255)
s = 6.6; ox, oy = cx - 32 * s, cy - 33 * s
P = lambda x, y: (ox + x * s, oy + y * s)
pts = [P(8, 18), P(16, 14.5), P(24, 15), P(32, 20), P(40, 15), P(48, 14.5), P(56, 18), P(56, 48), P(48, 44.5), P(40, 45), P(32, 50), P(24, 45), P(16, 44.5), P(8, 48)]
ko = Image.new('L', (W, H), 0); ImageDraw.Draw(ko).polygon(pts, fill=255); ko = ko.filter(ImageFilter.MaxFilter(31))
glow = Image.composite(Image.new('L', (W, H), 0), glow, ko)
g.polygon(pts, fill=255); g.line([P(32, 20), P(32, 50)], fill=0, width=16)
gold.save(os.path.join(OUT, 'cover_gold.png')); glow.save(os.path.join(OUT, 'cover_glow.png'))
for n in ('cover_base.png', 'page.png'): Image.open(os.path.join(HERE, n)).save(os.path.join(OUT, n))
print('ok')
