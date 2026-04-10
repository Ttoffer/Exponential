"""Build a dramatic apple-touch-icon.png (180x180): jewel-like tile + glowing e + glints."""
from __future__ import annotations

import math
import random
from PIL import Image, ImageDraw, ImageFont

SIZE = 180
R = int(SIZE * 0.224)
CX, CY = SIZE * 0.5, SIZE * 0.48


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def clamp01(t: float) -> float:
    return max(0.0, min(1.0, t))


def bg_rgb(nx: float, ny: float) -> tuple[int, int, int]:
    """Radial jewel: hot centre → violet → deep edge."""
    dx, dy = nx - 0.5, ny - 0.48
    r = math.sqrt(dx * dx + dy * dy) * 1.35
    t = clamp01(r)
    # inner: gold-teal sparkle
    ir, ig, ib = 255, 220, 120
    mr, mg, mb = 56, 189, 248
    pr, pg, pb = 76, 29, 149
    er, eg, eb = 8, 6, 22
    if t < 0.35:
        u = t / 0.35
        r_, g_, b_ = lerp(ir, mr, u), lerp(ig, mg, u), lerp(ib, mb, u)
    elif t < 0.72:
        u = (t - 0.35) / 0.37
        r_, g_, b_ = lerp(mr, pr, u), lerp(mg, pg, u), lerp(mb, pb, u)
    else:
        u = (t - 0.72) / 0.28
        r_, g_, b_ = lerp(pr, er, u), lerp(pg, eg, u), lerp(pb, eb, u)
    # subtle angle tint
    ang = math.atan2(dy, dx)
    tw = 0.5 + 0.5 * math.sin(ang * 3)
    r_ += 18 * tw * (1 - t)
    g_ += 12 * tw * (1 - t)
    b_ += 28 * tw * (1 - t)
    return int(clamp01(r_ / 255) * 255), int(clamp01(g_ / 255) * 255), int(clamp01(b_ / 255) * 255)


def main() -> None:
    rng = random.Random(42)
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    px = img.load()
    for y in range(SIZE):
        for x in range(SIZE):
            r, g, b = bg_rgb(x / SIZE, y / SIZE)
            px[x, y] = (r, g, b, 255)

    mask = Image.new("L", (SIZE, SIZE), 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.rounded_rectangle((0, 0, SIZE - 1, SIZE - 1), radius=R, fill=255)
    img.putalpha(mask)

    # Specular sweep + inner rim light
    gloss = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    gd = ImageDraw.Draw(gloss)
    gd.ellipse((SIZE * 0.08, SIZE * 0.04, SIZE * 0.92, SIZE * 0.48), fill=(255, 255, 255, 55))
    gd.ellipse((SIZE * 0.22, SIZE * 0.62, SIZE * 0.78, SIZE * 0.94), fill=(168, 85, 247, 35))
    img = Image.alpha_composite(img, gloss)

    draw = ImageDraw.Draw(img)

    # Deterministic star glints
    for k in range(14):
        ang = k * 1.7 + 0.3
        rr = SIZE * (0.38 + 0.06 * math.sin(k * 1.1))
        sx = CX + rr * math.cos(ang)
        sy = CY + rr * math.sin(ang)
        br = 2 + (k % 3)
        a = 90 + rng.randint(0, 50)
        draw.ellipse((sx - br, sy - br, sx + br, sy + br), fill=(255, 250, 220, a))

    # Chromatic rim stroke (fake)
    rim = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    rd = ImageDraw.Draw(rim)
    for i, col in enumerate([(255, 100, 200, 90), (56, 220, 255, 110), (250, 230, 140, 70)]):
        o = 2 + i
        rd.rounded_rectangle((o, o, SIZE - 1 - o, SIZE - 1 - o), radius=max(2, R - o), outline=col, width=1)
    img = Image.alpha_composite(img, rim)
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 102)
    except OSError:
        font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 102)

    ch = "e"
    bbox = draw.textbbox((0, 0), ch, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (SIZE - tw) / 2 - bbox[0]
    ty = (SIZE - th) / 2 - bbox[1] - 6

    # Glitzy multi-layer glow
    layers = [
        (6, 6, (236, 72, 153, 55)),
        (-5, -4, (56, 189, 248, 70)),
        (4, -3, (167, 139, 250, 60)),
        (0, 0, (52, 211, 153, 120)),
        (0, 0, (255, 255, 255, 200)),
    ]
    for ox, oy, rgba in layers:
        draw.text((tx + ox, ty + oy), ch, font=font, fill=rgba)

    out = "apple-touch-icon.png"
    img.save(out, "PNG", optimize=True)
    print("Wrote", out)


if __name__ == "__main__":
    main()
