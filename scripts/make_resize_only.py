from pathlib import Path
import shutil
import sys

base = Path(__file__).resolve().parent.parent
target = base / 'resize-only'

if target.exists():
    shutil.rmtree(target)

target.mkdir(parents=True, exist_ok=True)

# copy main HTML as index.html
src_html = base / 'resize.html'
if not src_html.exists():
    print('ERROR: resize.html not found', file=sys.stderr)
    sys.exit(1)
shutil.copy2(src_html, target / 'index.html')

# optional css
css = base / 'style.min.css'
if css.exists():
    shutil.copy2(css, target / 'style.min.css')

# images
images_src = base / 'images'
images_target = target / 'images'
images_target.mkdir(exist_ok=True)
for name in ('gs-logo-horizontal.png','gs-logo.png','resize-banner.png'):
    p = images_src / name
    if p.exists():
        shutil.copy2(p, images_target / name)

# favicons
for name in ('favicon.ico','favicon-32.png','favicon-16.png','apple-touch-icon.png'):
    p = base / name
    if p.exists():
        shutil.copy2(p, target / name)

# create zip
zip_path = base / 'resize-only.zip'
if zip_path.exists():
    zip_path.unlink()
shutil.make_archive(str(base / 'resize-only'), 'zip', root_dir=str(target))
print('DONE: resize-only.zip created at', zip_path)
