import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add safe padding to the why-card so arrows don't overlap text
css = css.replace("padding:20px 18px", "padding:40px 70px")
css = css.replace("padding:30px;", "padding:40px 70px;")

# Ensure the grid layout accommodates the new padding nicely and centers vertically
css = css.replace("align-items:start", "align-items:center")

# Let's also style the arrows specifically for the why-coverflow to push them further to the edges
arrow_styles = """
.why-coverflow-swiper .swiper-button-prev { left: 10px; top: 50%; }
.why-coverflow-swiper .swiper-button-next { right: 10px; top: 50%; }
.why-coverflow-swiper .swiper-button-prev::after, .why-coverflow-swiper .swiper-button-next::after { font-size: 32px; font-weight: bold; text-shadow: 0 4px 10px rgba(0,0,0,0.5); }
"""

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css + '\n' + arrow_styles)

print("Card layout fixed for arrows!")
