import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update the background pattern to yellowish-black
old_bg = "background-color: var(--white); background-image: radial-gradient(circle at 15% 30%, rgba(245, 158, 11, 0.08), transparent 35%), radial-gradient(circle at 85% 70%, rgba(50, 25, 80, 0.3), transparent 40%), radial-gradient(ellipse at top, rgba(245, 158, 11, 0.05) 0%, transparent 60%), linear-gradient(rgba(255,255,255,0.015) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.015) 1px, transparent 1px); background-size: 100% 100%, 100% 100%, 100% 100%, 40px 40px, 40px 40px; background-attachment: fixed; min-height: 100vh;"

new_bg = "background-color: #0A0905; background-image: radial-gradient(circle at 15% 30%, rgba(245, 158, 11, 0.12), transparent 45%), radial-gradient(circle at 85% 70%, rgba(200, 150, 20, 0.08), transparent 50%), radial-gradient(ellipse at top, rgba(255, 215, 0, 0.05) 0%, transparent 60%), linear-gradient(rgba(245, 158, 11, 0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(245, 158, 11, 0.03) 1px, transparent 1px); background-size: 100% 100%, 100% 100%, 100% 100%, 40px 40px, 40px 40px; background-attachment: fixed; min-height: 100vh;"

if old_bg in css:
    css = css.replace(old_bg, new_bg)
else:
    print("Could not find the old background string.")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Yellowish-black background applied!")
