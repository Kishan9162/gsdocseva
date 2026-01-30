Generate favicons from `images/gs-logo.png`

Requirements
- Python 3.8+
- Pillow: `pip install Pillow`

Run
```
python scripts/generate_favicons.py
```

Outputs (saved to project root):
- `favicon-16.png`
- `favicon-32.png`
- `apple-touch-icon.png` (180x180)
- `favicon.ico`

After running, upload these files to your site root (same folder as `index.html`) so browsers can fetch them at `https://your-site.com/favicon.ico` etc.