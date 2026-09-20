import re
import os

# 1. Fix styles.css
with open('styles.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# Replace the entire :root block
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
}"""

css = re.sub(r':root\s*\{[^}]+\}', original_root, css, count=1)

# Ensure body is clean light theme
body_pattern = r'body\s*\{[^}]+\}'
light_body = """body {
    margin: 0;
    color: var(--ink);
    font: 16px/1.55 'Inter', system-ui, sans-serif;
    background: var(--white);
}"""
css = re.sub(body_pattern, light_body, css, count=1)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Force Cache Busting on HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
        
        # bump styles.css?v=2.0 or anything similar to v=3.0
        html = re.sub(r'styles\.css\?v=[0-9.]+', 'styles.css?v=4.0', html)
        html = html.replace('styles.css"', 'styles.css?v=4.0"')
        
        # Also revert any inline background styles we forced (like in career.html)
        html = html.replace('background: transparent;', 'background: var(--white);')
        html = html.replace('background: transparent', 'background: var(--white)')
        html = html.replace('color: #FAFAFA;', 'color: var(--ink);')
        html = html.replace('color: #cbd5e1;', 'color: var(--muted);')
        
        with open(html_file, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(html)
    except Exception as e:
        print(f"Skipping {html_file}: {e}")

print("Light Theme completely restored and cache busters updated!")
