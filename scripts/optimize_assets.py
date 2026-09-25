import os
from PIL import Image

def optimize_images(assets_dir):
    # Optimize logos (displayed at 38x38, max 100x100 is plenty for retina)
    logos = ['assets/logos/causmic-club-logo.png', 'assets/logos/gndec-logo.png']
    for rel_path in logos:
        full_path = os.path.join(assets_dir, '..', rel_path.replace('/', os.sep))
        if os.path.exists(full_path):
            with Image.open(full_path) as img:
                img.thumbnail((120, 120), Image.Resampling.LANCZOS)
                img.save(full_path, 'PNG', optimize=True)
                print(f"Optimized logo {rel_path} -> size: {os.path.getsize(full_path)} bytes")

    # Optimize photography (displayed at ~280px width, max 600px width for 2x retina)
    photos = [
        'assets/photography/tech-robotics.jpg',
        'assets/photography/creative-art.jpg',
        'assets/photography/performance-stage.jpg',
        'assets/photography/campus-gndec.jpg'
    ]
    for rel_path in photos:
        full_path = os.path.join(assets_dir, '..', rel_path.replace('/', os.sep))
        if os.path.exists(full_path):
            with Image.open(full_path) as img:
                img.thumbnail((600, 400), Image.Resampling.LANCZOS)
                img.save(full_path, 'JPEG', quality=82, optimize=True)
                print(f"Optimized photo {rel_path} -> size: {os.path.getsize(full_path)} bytes")

    # Optimize icons (displayed at 18x18 - 34x34)
    icons_dir = os.path.join(assets_dir, 'icons')
    if os.path.exists(icons_dir):
        for icon_name in os.listdir(icons_dir):
            if icon_name.endswith('.png'):
                icon_path = os.path.join(icons_dir, icon_name)
                with Image.open(icon_path) as img:
                    img.thumbnail((80, 80), Image.Resampling.LANCZOS)
                    img.save(icon_path, 'PNG', optimize=True)
                    print(f"Optimized icon {icon_name} -> size: {os.path.getsize(icon_path)} bytes")

if __name__ == '__main__':
    base_dir = os.path.abspath(os.path.dirname(__file__) + '/..')
    assets_dir = os.path.join(base_dir, 'assets')
    optimize_images(assets_dir)
