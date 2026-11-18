import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace fixed width with 100% so it fits in the grid track
css = css.replace(".why-card{width:360px}", ".why-card{width:100%}")

# Fix any double closing braces that might break media queries
css = css.replace("!important;gap:24px!important;}}", "!important;gap:24px!important;}")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Overlap fixed!")
