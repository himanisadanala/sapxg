import re

with open('career.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# 1. Update Swiper JS configuration to include loopedSlides and center_insufficient
swiper_config_old = """    new Swiper('.coverflow-swiper', {
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
      loop: true,"""

swiper_config_new = """    new Swiper('.coverflow-swiper', {
      effect: 'coverflow',
      grabCursor: true,
      centeredSlides: true,
      slidesPerView: 'auto',
      loopedSlides: 8,
      coverflowEffect: {
        rotate: 22,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: true,
      },
      loop: true,"""

if swiper_config_old in html:
    html = html.replace(swiper_config_old, swiper_config_new)
else:
    # If not found precisely, try regex
    html = re.sub(r"slidesPerView:\s*'auto',", "slidesPerView: 'auto',\n      loopedSlides: 8,", html)

# 2. Duplicate the slides in the HTML to ensure there's enough DOM nodes for Swiper to clone
# We will find the slides block and duplicate the inner content
start = html.find('<div class="swiper-wrapper">')
if start != -1:
    end = html.find('</div>\n        <!-- Add Navigation -->', start)
    if end == -1: # wait, pagination was removed
        end = html.find('</div>\n        <div class="swiper-button-prev"', start)
    if end != -1:
        wrapper_content = html[start + len('<div class="swiper-wrapper">'):end]
        
        # double it
        new_wrapper_content = wrapper_content + wrapper_content
        
        html = html[:start + len('<div class="swiper-wrapper">')] + new_wrapper_content + html[end:]

with open('career.html', 'w', encoding='utf-8', errors='ignore') as f:
    f.write(html)

print("Swiper looping fixed!")
