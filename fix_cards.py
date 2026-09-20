import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fix the double border issue in .why-card
# Old: border:1px solid rgba(245, 158, 11, 0.15);;border:1px solid transparent;
css = css.replace("border:1px solid rgba(245, 158, 11, 0.15);;border:1px solid transparent;", "border:1px solid rgba(245, 158, 11, 0.15);")
css = css.replace("border:1px solid rgba(245, 158, 11, 0.15);border:1px solid transparent;", "border:1px solid rgba(245, 158, 11, 0.15);")

# 2. Add styles for .why-card-link to make it work well in grid
if ".why-card-link" not in css:
    css += "\n.why-card-link { display: block; height: 100%; text-decoration: none; outline: none; border-radius: 12px; }"

# 3. Ensure gap is definitely applied and cards expand properly
# We might need to ensure the grid gap is enough and box-sizing applies to all
css = css.replace(".why-grid{display:grid;grid-template-columns:repeat(2,minmax(0,360px));gap:18px}", ".why-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}")

# The media query has this:
css = css.replace("@media(min-width:761px){.why-layout .why-grid{grid-template-columns:repeat(2,minmax(0,360px))!important}", "@media(min-width:761px){.why-layout .why-grid{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:24px!important;}}")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Card layout fixed!")
