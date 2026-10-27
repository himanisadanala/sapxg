import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Restore the header
css = re.sub(r'background:\s*rgba\(10,\s*10,\s*15,\s*\.8\)[^;]*;', 'background: rgba(255, 255, 255, 0.95);', css)
css = css.replace('backdrop-filter: blur(12px);', 'backdrop-filter: blur(8px);')

# 2. Fix why-card and service-card borders/glass
# We replaced borders with gold transparent earlier
css = re.sub(r'border:\s*1px solid rgba\(245,\s*158,\s*11,\s*0\.15\);', 'border: 1px solid var(--line);', css)
css = re.sub(r'border:\s*1px solid rgba\(255,\s*255,\s*255,\s*0\.08\);', 'border: 1px solid var(--line);', css)
css = re.sub(r'box-shadow:\s*0 10px 15px rgba\(0,0,0,0\.3\);', 'box-shadow: 0 4px 12px rgba(0,0,0,0.05);', css)

# 3. Text colors forced to white/FAFAFA
css = css.replace('color:var(--white)', 'color:var(--ink)')
css = css.replace('color:#FAFAFA', 'color:var(--ink)')
css = css.replace('color: #FAFAFA', 'color: var(--ink)')

# 4. Remove .glow
css = re.sub(r'\.glow\s*\{[^}]+\}', '.glow { display: none; }', css)

# 5. Fix body text colors explicitly if they are hardcoded
css = css.replace('color: var(--ink-2)', 'color: var(--muted)')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

import os
# Force Cache Busting on HTML files to v=5.0
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
        
        html = re.sub(r'styles\.css\?v=[0-9.]+', 'styles.css?v=5.0', html)
        html = html.replace('styles.css"', 'styles.css?v=5.0"')
        
        with open(html_file, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(html)
    except Exception as e:
        print(f"Skipping {html_file}: {e}")

print("Cleaned up dark theme remnants and bumped cache to v=5.0!")
