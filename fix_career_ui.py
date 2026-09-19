import re

with open('career.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Enhance the Journey section to look royal and fix any remaining color issues
old_journey = """<section class="journey-section" style="padding: clamp(60px, 8vw, 100px) clamp(22px, 8vw, 128px); background: transparent;">
      <div style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; align-items: center;">
        <div>
          <h2 style="font: 700 clamp(36px, 6vw, 52px)/1.1 'Space Grotesk', sans-serif; margin-bottom: 24px; color: #FAFAFA; letter-spacing: -1px;">Begin The Journey With / <br>Through Us</h2>
          <p style="font-size: 18px; line-height: 1.6; color: #cbd5e1; margin-bottom: 24px;">Our group of seasoned experts, having sound experience in respective domains, ensure a long-lasting relationship with Global Customers fulfilling Customer's Business needs.</p>
          <p style="font-size: 18px; line-height: 1.6; color: #cbd5e1; margin-bottom: 32px;">These experts bring to our notice both the domain skills required and job positions available in Customer projects and that makes us bridge your career journey.</p>
        </div>
        <div>
          <img src="career_support.jpg" alt="Career support professional" style="width: 100%; height: auto; border-radius: 12px; object-fit: cover;">
        </div>
      </div>
    </section>"""

new_journey = """<section class="journey-section" style="padding: clamp(60px, 8vw, 100px) clamp(22px, 8vw, 128px); background: transparent; position: relative;">
      <div style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 60px; align-items: center; position: relative; z-index: 2;">
        <div style="background: rgba(10, 10, 15, 0.4); padding: 40px; border-radius: 16px; border: 1px solid rgba(245, 158, 11, 0.15); backdrop-filter: blur(10px); box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);">
          <div class="eyebrow" style="margin-bottom: 16px; color: #B39DDB; font-size: 16px;"><span></span> Build Your Future</div>
          <h2 style="font: 700 clamp(36px, 6vw, 52px)/1.1 'Space Grotesk', sans-serif; margin-bottom: 24px; color: #FAFAFA; letter-spacing: -1px;">
            Begin The Journey <br><em style="background: linear-gradient(to right, #F59E0B, #FFD700); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 0 0 20px rgba(245,158,11,0.3); font-style: normal;">With Us</em>
          </h2>
          <p style="font-size: 18px; line-height: 1.6; color: #A1A1AA; margin-bottom: 24px;">Our seasoned experts leverage deep domain experience to ensure long-lasting relationships and fulfill the most complex business needs globally.</p>
          <p style="font-size: 18px; line-height: 1.6; color: #A1A1AA; margin-bottom: 0;">We constantly bridge the gap between domain skills and elite job positions in enterprise projects, actively guiding your career trajectory.</p>
        </div>
        <div style="position: relative;">
          <div style="position: absolute; inset: 0; background: linear-gradient(135deg, rgba(245, 158, 11, 0.4) 0%, rgba(30, 20, 60, 0.6) 100%); mix-blend-mode: overlay; border-radius: 16px; z-index: 1;"></div>
          <img src="career_support.jpg" alt="Career support professional" style="width: 100%; height: auto; border-radius: 16px; object-fit: cover; box-shadow: 0 0 30px rgba(245,158,11,0.15); filter: contrast(1.1) saturate(0.9);">
        </div>
      </div>
    </section>"""

if old_journey in html:
    html = html.replace(old_journey, new_journey)
else:
    print("Could not find old journey section.")

with open('career.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Career page polished!")
