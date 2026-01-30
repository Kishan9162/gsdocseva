#!/usr/bin/env python3
"""
Generate favicon files from images/gs-logo.png
Produces: favicon-16.png, favicon-32.png, apple-touch-icon.png (180x180), favicon.ico
Requires: Pillow (pip install Pillow)
Run: python scripts/generate_favicons.py
"""
from PIL import Image
import sys
import os

ROOT = os.path.dirname(os.path.dirname(__file__))
SRC = os.path.join(ROOT, 'images', 'gs-logo.png')

OUT_FILES = [
    ('favicon-16.png', 16),
    ('favicon-32.png', 32),
    ('apple-touch-icon.png', 180),
]
ICO_SIZES = [16, 32, 48, 64, 128, 256]

def main():
    if not os.path.exists(SRC):
        print('Source image not found:', SRC)
        sys.exit(1)
    im = Image.open(SRC).convert('RGBA')

    for name, size in OUT_FILES:
        out = os.path.join(ROOT, name)
        img = im.resize((size, size), Image.LANCZOS)
        img.save(out, format='PNG')
        print('Saved', out)

    # Save ICO with multiple sizes
    ico_path = os.path.join(ROOT, 'favicon.ico')
    try:
        # Pillow lets you pass sizes to save() for ICO
        im.save(ico_path, sizes=[(s, s) for s in ICO_SIZES])
        print('Saved', ico_path)
    except Exception as e:
        # Fallback: create and save largest size as single-icon ICO
        print('ICO multi-size save failed, creating single-size ICO fallback:', str(e))
        img = im.resize((256, 256), Image.LANCZOS)
        img.save(ico_path)
        print('Saved', ico_path)

    print('\nDone. Copy the generated files to your hosting root to enable them site-wide.')

if __name__ == '__main__':
    main()
