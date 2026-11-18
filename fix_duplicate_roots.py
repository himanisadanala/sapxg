import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Remove ALL :root blocks
css = re.sub(r':root\s*\{[^}]+\}', '', css)

# 2. Add one clean, definitive Light Theme :root block at the very top
original_root = """:root {
  --yellow: #F59E0B;
  --yellow-soft: #FEF3C7;
  --ink: #0A0A0F;
  --ink-2: #333333;
  --white: #FFFFFF;
  --grey: #F5F5F5;
  --muted: #52525B;
  --line: #E5E7EB;
  --blue: #2563EB;
  --accent: #2563EB;
  --accent-fg: #FFFFFF;
  --card: #FFFFFF;
}
"""

css = original_root + css.lstrip()

# Also ensure body doesn't have multiple rules
css = re.sub(r'body\s*\{[^}]+\}', '', css)
light_body = """body {
    margin: 0;
    color: var(--ink);
    font: 16px/1.55 'Inter', system-ui, sans-serif;
    background: var(--white);
}
"""
css = original_root + light_body + css[len(original_root):].lstrip()

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

import os
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
        
        html = re.sub(r'styles\.css\?v=[0-9.]+', 'styles.css?v=6.0', html)
        
        with open(html_file, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(html)
    except Exception as e:
        pass

print("Root blocks consolidated and cleaned!")
