"""
GNE'S APEX 2026 — Replace Local Asset Paths with GitHub / CDN URLs
===================================================================
Replaces relative `assets/...` paths in index.html with public GitHub raw/cdn URLs.

Usage Example:
  python scripts/update_image_urls.py --repo "username/apex-mailing" --branch "main"
"""

import os
import re
import argparse

def update_asset_urls(input_html, output_html, base_url):
    with open(input_html, 'r', encoding='utf-8') as f:
        content = f.read()

    # Normalize trailing slash
    if not base_url.endswith('/'):
        base_url += '/'

    # Replace src="assets/..." or src='assets/...'
    pattern = r'src=["\']assets/([^"\']+)["\']'
    
    def replacer(match):
        rel_path = match.group(1)
        new_url = f'{base_url}assets/{rel_path}'
        print(f"Replaced: assets/{rel_path} -> {new_url}")
        return f'src="{new_url}"'

    new_content = re.sub(pattern, replacer, content)

    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"\nGenerated updated HTML with hosted URLs at: {output_html}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Update asset URLs to GitHub/CDN")
    parser.add_argument('--repo', help="GitHub repository in 'username/repo' format", default="")
    parser.add_argument('--branch', help="Branch name (default: main)", default="main")
    parser.add_argument('--base-url', help="Custom base URL (e.g., https://raw.githubusercontent.com/user/repo/main/)", default="")
    parser.add_argument('--cdn', action='store_true', help="Use jsDelivr CDN for faster global caching")

    args = parser.parse_args()

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    input_file = os.path.join(base_dir, 'index.html')
    output_file = os.path.join(base_dir, 'index-hosted.html')

    if args.base_url:
        target_base_url = args.base_url
    elif args.repo:
        if args.cdn:
            target_base_url = f"https://cdn.jsdelivr.net/gh/{args.repo}@{args.branch}/"
        else:
            target_base_url = f"https://raw.githubusercontent.com/{args.repo}/{args.branch}/"
    else:
        # Default placeholder demo
        target_base_url = "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/apex-mailing/main/"

    update_asset_urls(input_file, output_file, target_base_url)
