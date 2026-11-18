import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Enhance the <em> tags in headings to have a beautiful gold gradient
old_em = ".hero h1 em,.section-intro h2 em,.section-heading h2 em,.training h2 em,.career-panel h2 em,.blog-panel h2 em,.contact h2 em{font-style:normal;color:var(--blue)}"
new_em = ".hero h1 em,.section-intro h2 em,.section-heading h2 em,.training h2 em,.career-panel h2 em,.blog-panel h2 em,.contact h2 em{font-style:normal;background:linear-gradient(to right, #F59E0B, #FFD700);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-shadow:0 0 20px rgba(245,158,11,0.3);}"
css = css.replace(old_em, new_em)

# 2. Add a subtle gold tint to card borders for a royal feel
css = css.replace("border:1px solid var(--line);", "border:1px solid rgba(245, 158, 11, 0.15);")
# For the hover states, make the border brighter gold
css = css.replace("border-color:rgba(255,255,255,0.15);", "border-color:rgba(255, 215, 0, 0.4);")

# 3. Enhance the buttons to be more vibrant
# Replace outline button styling
old_btn_outline = ".button-outline{border:1px solid var(--ink);background:transparent;color:var(--ink)}"
new_btn_outline = ".button-outline{border:1px solid rgba(245,158,11,0.5);background:transparent;color:#F59E0B;box-shadow:0 0 15px rgba(245,158,11,0.1);}"
css = css.replace(old_btn_outline, new_btn_outline)

# 4. Enhance the .dash-number and metrics to use gold instead of --blue
css = css.replace("color:var(--blue)", "color:var(--accent)")
# This changes .dash-number small, .hero-proof strong, .about-metrics strong, .card-top

# 5. Make the hover states of links more vibrant
css = css.replace(".main-nav a:hover, .main-nav a.active{border-color:var(--yellow)}", ".main-nav a:hover, .main-nav a.active{border-color:var(--accent);color:#F59E0B;text-shadow:0 0 10px rgba(245,158,11,0.4);}")

# 6. Make eyebrows (the little tags above headings) purple/gold
old_eyebrow = ".eyebrow{display:flex;align-items:center;gap:12px;text-transform:uppercase;letter-spacing:1.8px;font-size:24px;font-weight:700;color:var(--muted);margin-bottom:22px}"
new_eyebrow = ".eyebrow{display:flex;align-items:center;gap:12px;text-transform:uppercase;letter-spacing:1.8px;font-size:24px;font-weight:700;color:#B39DDB;margin-bottom:22px}"
css = css.replace(old_eyebrow, new_eyebrow)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Royal colors applied!")
