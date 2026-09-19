import re

with open('career.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Swiper CSS in <head>
swiper_css = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css"/>'
html = html.replace('<link rel="stylesheet" href="styles.css?v=2.0">', '<link rel="stylesheet" href="styles.css?v=2.0">\n  ' + swiper_css)

# 2. Add Swiper JS and initialization before </body>
swiper_js = """
<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    new Swiper('.coverflow-swiper', {
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
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      keyboard: {
        enabled: true,
      }
    });
  });
</script>
"""
html = html.replace('</body>', swiper_js + '\n</body>')

# 3. Inject the Coverflow HTML
coverflow_html = """
    <!-- Coverflow Testimonials -->
    <section class="coverflow-section" aria-label="Customer testimonials">
      <div class="eyebrow" style="justify-content: center; width: 100%; margin-bottom: 40px; color: #B39DDB;"><span></span> Employee Stories</div>
      <div class="swiper coverflow-swiper">
        <div class="swiper-wrapper">
          <!-- Slide 1 -->
          <div class="swiper-slide">
            <figure class="coverflow-item">
              <blockquote>"Working at SAPXG has been a transformative experience. The opportunities for growth are unmatched."</blockquote>
              <figcaption>Sarah Jenkins - Lead Analyst</figcaption>
            </figure>
          </div>
          <!-- Slide 2 -->
          <div class="swiper-slide">
            <figure class="coverflow-item">
              <blockquote>"The collaborative culture and focus on cutting-edge solutions makes every day exciting."</blockquote>
              <figcaption>David Chen - Senior Consultant</figcaption>
            </figure>
          </div>
          <!-- Slide 3 -->
          <div class="swiper-slide">
            <figure class="coverflow-item">
              <blockquote>"I love the royal treatment we give to our customers. It reflects in the quality of our work."</blockquote>
              <figcaption>Elena Rodriguez - Project Manager</figcaption>
            </figure>
          </div>
          <!-- Slide 4 -->
          <div class="swiper-slide">
            <figure class="coverflow-item">
              <blockquote>"SAPXG truly values its people and invests heavily in our professional development."</blockquote>
              <figcaption>Michael Chang - Data Engineer</figcaption>
            </figure>
          </div>
        </div>
        <!-- Add Pagination -->
        <div class="swiper-pagination"></div>
        <!-- Add Navigation -->
        <div class="swiper-button-prev" style="color: var(--accent);"></div>
        <div class="swiper-button-next" style="color: var(--accent);"></div>
      </div>
    </section>
"""
# Insert after the journey section
html = html.replace('</section>\n    \n    <section class="content-section"', '</section>\n' + coverflow_html + '    \n    <section class="content-section"')


# 4. Add CSS for Coverflow to the existing <style> block
custom_styles = """
    .coverflow-section {
      padding: clamp(60px, 8vw, 100px) 0;
      background: transparent;
      overflow: hidden;
    }
    .coverflow-swiper {
      width: 100%;
      padding-top: 50px;
      padding-bottom: 50px;
    }
    .swiper-slide {
      background-position: center;
      background-size: cover;
      width: min(80vw, 400px);
    }
    .coverflow-item {
      display: flex;
      flex-direction: column;
      gap: 16px;
      border-radius: 12px;
      border: 1px solid rgba(245, 158, 11, 0.2);
      background: rgba(26, 26, 36, 0.6);
      backdrop-filter: blur(8px);
      padding: 32px;
      text-align: left;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
      margin: 0;
      height: 100%;
    }
    .coverflow-item blockquote {
      font-size: 18px;
      color: #FAFAFA;
      margin: 0;
      line-height: 1.6;
    }
    .coverflow-item figcaption {
      font-size: 14px;
      color: #F59E0B;
      margin-top: auto;
      font-weight: 600;
    }
    .swiper-pagination-bullet {
      background: #F59E0B !important;
    }
"""
html = html.replace('</style>', custom_styles + '\n  </style>')

# 5. Fix the dark theme inline styles in career.html which were inverted
html = html.replace('background: var(--ink);', 'background: transparent;')
html = html.replace('color: var(--white);', 'color: #FAFAFA;')
html = html.replace('background: var(--white);', 'background: var(--card); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px;')
html = html.replace('color: var(--ink);', 'color: #FAFAFA;')

with open('career.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Coverflow added successfully to career.html!")
