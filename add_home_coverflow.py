import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Swiper CSS if not present
swiper_css = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css"/>'
if swiper_css not in html:
    html = html.replace('<link rel="stylesheet" href="styles.css?v=2.0">', '<link rel="stylesheet" href="styles.css?v=2.0">\n  ' + swiper_css)

# 2. Add Swiper JS and init if not present
swiper_js = """
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    new Swiper('.why-coverflow-swiper', {
      effect: 'coverflow',
      grabCursor: true,
      centeredSlides: true,
      slidesPerView: 'auto',
      coverflowEffect: {
        rotate: 22,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: true,
      },
      loop: true,
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      keyboard: {
        enabled: true,
      }
    });
  });
</script>
"""
if "swiper-bundle.min.js" not in html:
    html = html.replace('</body>', swiper_js + '\n</body>')

# 3. Replace the why-grid with the Swiper structure
# Find the why-grid
grid_start = html.find('<div class="why-grid">')
if grid_start != -1:
    grid_end = html.find('</div></section>', grid_start)
    if grid_end != -1:
        grid_content = html[grid_start:grid_end]
        
        # Replace `<div class="why-grid">`
        new_content = grid_content.replace('<div class="why-grid">', '<div class="swiper why-coverflow-swiper" style="width: 100%; padding: 50px 0; overflow: hidden;"><div class="swiper-wrapper">')
        
        # Wrap every <a href="..." class="why-card-link"> in a swiper-slide
        # We can use regex to wrap them
        new_content = re.sub(r'(<a href="[^"]+" class="why-card-link">.*?</a>)', r'<div class="swiper-slide" style="width: min(80vw, 360px);"><div style="height: 100%;">\1</div></div>', new_content)
        
        # Add the closing tags for wrapper and swiper
        new_content += '</div><div class="swiper-button-prev" style="color: var(--accent);"></div><div class="swiper-button-next" style="color: var(--accent);"></div></div>'
        
        # Replace in html
        html = html[:grid_start] + new_content + html[grid_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Coverflow applied to home page!")
