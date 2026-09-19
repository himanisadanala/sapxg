import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_bg = "background-color: #0A0905; background-image: radial-gradient(circle at 15% 30%, rgba(245, 158, 11, 0.12), transparent 45%), radial-gradient(circle at 85% 70%, rgba(200, 150, 20, 0.08), transparent 50%), radial-gradient(ellipse at top, rgba(255, 215, 0, 0.05) 0%, transparent 60%), linear-gradient(rgba(245, 158, 11, 0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(245, 158, 11, 0.03) 1px, transparent 1px); background-size: 100% 100%, 100% 100%, 100% 100%, 40px 40px, 40px 40px; background-attachment: fixed; min-height: 100vh;"

new_bg = "background-color: #0A0A0A; background-image: repeating-linear-gradient(45deg, rgba(212, 175, 55, 0.04) 0px, rgba(212, 175, 55, 0.04) 1px, transparent 1px, transparent 40px), repeating-linear-gradient(-45deg, rgba(212, 175, 55, 0.04) 0px, rgba(212, 175, 55, 0.04) 1px, transparent 1px, transparent 40px), radial-gradient(ellipse at top, rgba(212, 175, 55, 0.1) 0%, transparent 60%); background-attachment: fixed; min-height: 100vh;"

if old_bg in css:
    css = css.replace(old_bg, new_bg)
else:
    # try regex for body
    css = re.sub(r'body\{.*?\}', "body{margin:0;color:var(--ink);" + new_bg + "font:16px/1.55 'Inter', system-ui, sans-serif;}", css, count=1)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Art Deco background applied!")
