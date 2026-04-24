"""Génère les PNG de favicon (16, 32, 180, 512) à partir du design SVG.
À lancer ponctuellement depuis la racine du projet."""
from PIL import Image, ImageDraw, ImageFont
import os

PURPLE = (110, 76, 146, 255)   # #6E4C92
CREAM  = (251, 246, 233, 255)  # #FBF6E9
RED    = (200, 16, 46, 255)    # #C8102E

# Polices candidates (ordre de priorité) — Windows + common
FONT_CANDIDATES = [
    r"C:\Windows\Fonts\georgiab.ttf",   # Georgia Bold
    r"C:\Windows\Fonts\timesbd.ttf",    # Times New Roman Bold
    r"C:\Windows\Fonts\arialbd.ttf",    # Arial Bold (fallback)
]

def get_font(size):
    for p in FONT_CANDIDATES:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def draw_favicon(size, out_path):
    # Travaille en 4× pour un antialiasing propre, puis resize
    scale = 4
    s = size * scale
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # Cercle violet (fond)
    d.ellipse((0, 0, s, s), fill=PURPLE)

    # "J" blanc cream centré
    font_size = int(s * 0.75)
    font = get_font(font_size)
    # Positionnement du J via bbox
    bbox = d.textbbox((0, 0), "J", font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (s - tw) // 2 - bbox[0]
    ty = (s - th) // 2 - bbox[1]
    d.text((tx, ty), "J", font=font, fill=CREAM)

    # Point hinomaru rouge en haut-droite
    hr = int(s * 0.125)
    hx = int(s * 0.78)
    hy = int(s * 0.22)
    d.ellipse((hx - hr, hy - hr, hx + hr, hy + hr), fill=RED)

    # Downscale avec Lanczos
    img = img.resize((size, size), Image.LANCZOS)
    img.save(out_path, "PNG", optimize=True)
    print(f"OK {out_path} ({size}x{size})")

for size, name in [
    (16,  "favicon-16.png"),
    (32,  "favicon-32.png"),
    (180, "apple-touch-icon.png"),
    (192, "icon-192.png"),
    (512, "icon-512.png"),
]:
    draw_favicon(size, name)
