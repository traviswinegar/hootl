"""Generate hootl.org's og-image.png — 1200x630 social card preview.

Matches the site palette: deep teal background, amber accent, cream
text. Run from the site directory:

    python scripts/og-image-gen.py

Writes the PNG to public/og-image.png.
"""

from PIL import Image, ImageDraw, ImageFont
import os
import sys

# Output lives in public/ so it ships with the site.
OUT = os.path.join(
    os.path.dirname(__file__), "..", "public", "og-image.png"
)

W, H = 1200, 630

# Palette (from src/styles/global.css)
DEEP_TEAL = (15, 61, 74)      # #0f3d4a
TEAL = (2, 128, 144)          # #028090
MID_TEAL = (77, 165, 158)     # #4da59e
CREAM = (245, 241, 232)       # #f5f1e8
AMBER = (212, 160, 74)        # #d4a04a


def find_font(candidates, size):
    """Try candidates; fall back to the default."""
    for name in candidates:
        try:
            return ImageFont.truetype(name, size)
        except (OSError, IOError):
            continue
    print(f"  ! falling back to default for size {size}", file=sys.stderr)
    return ImageFont.load_default()


def main() -> None:
    img = Image.new("RGB", (W, H), DEEP_TEAL)
    draw = ImageDraw.Draw(img)

    # Brand dot (amber circle) + wordmark
    dot_x, dot_y, dot_r = 80, 80, 18
    draw.ellipse(
        (dot_x - dot_r, dot_y - dot_r, dot_x + dot_r, dot_y + dot_r),
        fill=AMBER,
    )

    brand_font = find_font(
        ["georgia.ttf", "Georgia.ttf", "DejaVuSerif-Bold.ttf"], 36
    )
    draw.text(
        (dot_x + dot_r + 18, dot_y - 24),
        "HOOTL",
        font=brand_font,
        fill=CREAM,
    )

    # Big title — wrap to two lines
    title_font = find_font(
        ["georgia.ttf", "Georgia.ttf", "DejaVuSerif-Bold.ttf"], 66
    )
    line1 = "Eight principles for safe"
    line2 = "autonomous-agent operation."
    draw.text((80, 200), line1, font=title_font, fill=CREAM)
    draw.text((80, 290), line2, font=title_font, fill=MID_TEAL)

    # Subtitle
    sub_font = find_font(
        ["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 28
    )
    draw.text(
        (80, 432),
        "Humans Out Of The Loop · operator-side substrate properties",
        font=sub_font,
        fill=CREAM,
    )

    # URL bottom right
    url_font = find_font(
        ["arial.ttf", "Arial.ttf", "DejaVuSans-Bold.ttf"], 32
    )
    url_text = "hootl.org"
    bbox = draw.textbbox((0, 0), url_text, font=url_font)
    url_w = bbox[2] - bbox[0]
    draw.text(
        (W - 80 - url_w, H - 80 - 32),
        url_text,
        font=url_font,
        fill=AMBER,
    )

    # Amber accent bar at the bottom
    draw.rectangle((0, H - 12, W, H), fill=AMBER)

    img.save(OUT, "PNG", optimize=True)
    print(f"Wrote {OUT} ({os.path.getsize(OUT)} bytes)")


if __name__ == "__main__":
    main()
