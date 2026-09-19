import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Replace the root variables
css = re.sub(
    r':root\{[^\}]+\}', 
    ':root{--yellow:#F59E0B;--yellow-soft:rgba(245, 158, 11, 0.15);--ink:#FAFAFA;--ink-2:#FAFAFA;--white:#0A0A0F;--grey:#12121A;--muted:#71717A;--line:rgba(255, 255, 255, 0.08);--blue:#FAFAFA;--accent:#F59E0B;--accent-fg:#0A0A0F;--card:rgba(26, 26, 36, 0.6);}', 
    css
)

# 2. Update Font Stack in body
css = css.replace("font:16px/1.55 'DM Sans',sans-serif", "font:16px/1.55 'Inter', system-ui, sans-serif; background-image: radial-gradient(ellipse at top, rgba(245, 158, 11, 0.03) 0%, transparent 50%), linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px); background-size: 100% 100%, 40px 40px, 40px 40px; min-height: 100vh;")

# 3. Header background
css = css.replace("background:rgba(255,255,255,.95)", "background:rgba(10, 10, 15, .8); backdrop-filter: blur(12px); border-bottom: 1px solid var(--line);")

# 4. Update Button Styles
css = css.replace("background:var(--yellow);color:var(--ink)", "background:var(--accent);color:var(--accent-fg);box-shadow: 0 0 20px rgba(245,158,11,0.15);border-radius:12px;")
css = css.replace("box-shadow:4px 4px 0 var(--ink)", "box-shadow:0 0 40px rgba(245, 158, 11, 0.4); filter:brightness(1.1); transform:scale(1.02);")

# 5. Service Cards & Why Cards
css = css.replace("background:var(--white);padding:27px 27px 31px", "background:var(--card);backdrop-filter:blur(8px);border-radius:12px;padding:27px 27px 31px;border:1px solid var(--line);")
css = css.replace("background:var(--white);padding:30px;min-height:260px", "background:var(--card);backdrop-filter:blur(8px);border-radius:12px;padding:30px;min-height:260px;border:1px solid var(--line);")

# Card Hover
css = css.replace("box-shadow:8px 8px 0 var(--yellow);border-color:var(--ink)", "box-shadow:0 10px 15px rgba(0,0,0,0.3);border-color:rgba(255,255,255,0.15);transform:scale(1.02);")
css = css.replace("box-shadow:7px 7px 0 var(--yellow)", "box-shadow:0 10px 15px rgba(0,0,0,0.3);border-color:rgba(255,255,255,0.15);transform:scale(1.02);")

# 6. Hero and Sections Backgrounds
css = css.replace("background:linear-gradient(110deg,#fff 58%,#fffdf0 58%)", "background:transparent;")
css = css.replace("background:var(--ink)", "background:transparent;")
css = css.replace("background:var(--grey)", "background:transparent;")

# 7. Hero Visual Glow
css = css.replace("background:var(--yellow);width:330px;height:330px;border-radius:50%;left:50%;top:75px;transform:translateX(-50%);box-shadow:0 0 80px rgba(250,204,21,.3)", "background:rgba(245, 158, 11, 0.15);width:600px;height:600px;border-radius:50%;left:50%;top:0px;transform:translateX(-50%);box-shadow:0 0 150px rgba(245,158,11,0.2); filter:blur(100px);")
css = css.replace("background:var(--white);width:min(280px,calc(100% - 45px));padding:17px;box-shadow:8px 8px 0 var(--yellow)", "background:var(--card);backdrop-filter:blur(8px);border-radius:12px;width:min(280px,calc(100% - 45px));padding:17px;border:1px solid var(--line);box-shadow:0 10px 25px rgba(0,0,0,0.5);")

# 8. Typography and headings 
css = css.replace("'DM Sans',sans-serif", "'Inter', system-ui, sans-serif")

# 9. Spacing
css = css.replace("padding-top:70px;padding-bottom:70px", "padding-top:140px;padding-bottom:140px")
css = css.replace("padding-top:105px;padding-bottom:120px", "padding-top:140px;padding-bottom:140px")
css = css.replace("padding-top:115px;padding-bottom:135px", "padding-top:160px;padding-bottom:160px")
css = css.replace("padding-top:125px;padding-bottom:130px", "padding-top:160px;padding-bottom:160px")

# Fix floating whatsapp button
css = css.replace("background-color: #25D366;", "background-color: var(--card); backdrop-filter: blur(8px); border: 1px solid var(--line); color: var(--accent);")
css = css.replace("border: 2px solid #20B358;", "")

# Fix input fields and contact form
css = css.replace("background:var(--white);padding:39px", "background:var(--card);backdrop-filter:blur(8px);padding:39px;border-radius:12px;border:1px solid var(--line);")

# Write out the modified CSS
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS transformed!")
