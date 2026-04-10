"""Build apple-touch-icon.png (180x180) for home-screen: stylised e on a deep gradient tile."""
from __future__ import annotations

import math
from PIL import Image, ImageDraw, ImageFont

SIZE = 180
R = int(SIZE * 0.22)


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def pixel(x: int, y: int) -> tuple[int, int, int]:
    t = (x + y) / (2 * SIZE)
    r = int(lerp(30, 14, t))
    g = int(lerp(24, 80, t))
    b = int(lerp(56, 120, t))
    return r, g, b


def main() -> None:
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    px = img.load()
    for y in range(SIZE):
        for x in range(SIZE):
            r, g, b = pixel(x, y)
            px[x, y] = (r, g, b, 255)

    mask = Image.new("L", (SIZE, SIZE), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, SIZE - 1, SIZE - 1), radius=R, fill=255)
    img.putalpha(mask)

    draw = ImageDraw.Draw(img)
    # subtle inner highlight (Apple-style gloss hint)
    hl = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    hld = ImageDraw.Draw(hl)
    hld.ellipse((SIZE * 0.12, SIZE * 0.06, SIZE * 0.88, SIZE * 0.42), fill=(255, 255, 255, 38))
    img = Image.alpha_composite(img, hl)

    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 96)
    except OSError:
        font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 96)

    ch = "e"
    bbox = draw.textbbox((0, 0), ch, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (SIZE - tw) / 2 - bbox[0]
    ty = (SIZE - th) / 2 - bbox[1] - 4
    # soft glow
    for ox, oy, alpha in [(0, 0, 50), (1, 0, 40), (-1, 0, 40), (0, 1, 35), (0, -1, 35)]:
        draw.text((tx + ox, ty + oy), ch, font=font, fill=(52, 211, 153, alpha))
    draw.text((tx, ty), ch, font=font, fill=(236, 253, 245, 255))

    out = "apple-touch-icon.png"
    img.save(out, "PNG", optimize=True)
    print("Wrote", out)


if __name__ == "__main__":
    main()
