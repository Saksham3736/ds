import os
import re
import base64
import mimetypes

def inline_images_to_base64(input_html_path, output_html_path):
    with open(input_html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Find all src="assets/..." or src="https://cdn.jsdelivr.net/.../assets/..." matches
    pattern = r'src=["\'](?:https://cdn\.jsdelivr\.net/gh/[^/]+/[^/]+/)?(assets/[^"\']+)["\']'
    
    def replacer(match):
        relative_path = match.group(1)
        full_path = os.path.join(os.path.dirname(input_html_path), relative_path.replace('/', os.sep))
        
        if os.path.exists(full_path):
            mime_type, _ = mimetypes.guess_type(full_path)
            if not mime_type:
                mime_type = 'image/png' if full_path.endswith('.png') else 'image/jpeg'
            
            with open(full_path, 'rb') as img_file:
                encoded = base64.b64encode(img_file.read()).decode('utf-8')
                data_uri = f'data:{mime_type};base64,{encoded}'
                print(f"Inlined: {relative_path} ({len(encoded)} chars)")
                return f'src="{data_uri}"'
        else:
            print(f"Warning: File not found: {full_path}")
            return match.group(0)

    new_html = re.sub(pattern, replacer, html_content)

    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print(f"\nSuccessfully generated standalone self-contained file: {output_html_path}")

if __name__ == '__main__':
    base_dir = os.path.abspath(os.path.dirname(__file__) + '/..')
    input_file = os.path.join(base_dir, 'index.html')
    output_file = os.path.join(base_dir, 'index-embedded.html')
    inline_images_to_base64(input_file, output_file)

