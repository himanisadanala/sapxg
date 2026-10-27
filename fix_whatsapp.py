import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix floating-whatsapp background and text color
css = re.sub(
    r'background-color:\s*var\(--card\);[^;]*;[^;]*;[^;]*;',
    'background-color: #25D366; border: none; color: white;',
    css
)

# If the regex missed, try a more robust replacement
if '#25D366' not in css:
    css = re.sub(
        r'\.floating-whatsapp\s*\{[^}]+\}',
        lambda m: m.group(0).replace('var(--card)', '#25D366').replace('var(--accent)', 'white').replace('border: 1px solid var(--line);', 'border: none;'),
        css
    )
    
# Ensure SVG inside it is white
svg_rule = """
.floating-whatsapp svg {
    fill: white;
}
"""
css += svg_rule

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

import os
# Force Cache Busting on HTML files to v=7.0
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
        
        html = re.sub(r'styles\.css\?v=[0-9.]+', 'styles.css?v=7.0', html)
        
        with open(html_file, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(html)
    except Exception as e:
        print(f"Skipping {html_file}: {e}")

print("WhatsApp button fixed!")
