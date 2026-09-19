import glob
import re

site_header_template = '''  <header class="site-header">
    <a class="brand" href="index.html#home" aria-label="SAPXG home">
      <img class="full-logo" src="sapxg logo.png" alt="SAPXG - A Smart Analytics &amp; Planning Experts Group">
    </a>
    <button class="menu-toggle" type="button" aria-label="Toggle navigation" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="main-nav" aria-label="Primary navigation">
      <a href="index.html#home"{home_act}>Home</a><a href="index.html#why-us"{about_act}>About Us</a><a href="index.html#services"{serv_act}>Domain &amp; Services</a><a href="career.html"{car_act}>Careers</a><a href="index.html#training"{train_act}>Training Schedule</a><a href="index.html#contact"{contact_act}>Contact Us</a><a href="blogs.html"{blog_act}>Blogs</a><a href="credits.html"{cred_act}>Credits</a>
    </nav>
  </header>'''

index_header_template = '''  <header class="site-header">
    <a class="brand" href="#home" aria-label="SAPXG home">
      <img class="full-logo" src="sapxg logo.png" alt="SAPXG - A Smart Analytics &amp; Planning Experts Group">
    </a>
    <button class="menu-toggle" type="button" aria-label="Toggle navigation" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="main-nav" aria-label="Primary navigation">
      <a href="#home">Home</a><a href="#why-us">About Us</a><a href="#services">Domain &amp; Services</a><a href="career.html">Careers</a><a href="#training">Training Schedule</a><a href="#contact">Contact Us</a><a href="blogs.html">Blogs</a><a href="credits.html">Credits</a>
    </nav>
  </header>'''

for fn in glob.glob('*.html'):
    if fn.startswith('temp_'):
        continue
    with open(fn, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if fn == 'index.html':
        header_html = index_header_template
    else:
        car_act = ' class="active"' if fn == 'career.html' else ''
        blog_act = ' class="active"' if fn == 'blogs.html' or fn.startswith('post-') else ''
        cred_act = ' class="active"' if fn == 'credits.html' else ''
        train_act = ' class="active"' if fn == 'training.html' or fn == 'register.html' else ''
        serv_act = ' class="active"' if fn in ['analytics.html', 'planning.html', 'consulting.html', 'offshore.html', 'augmentation.html'] else ''

        header_html = site_header_template.format(
            home_act='',
            about_act='',
            serv_act=serv_act,
            car_act=car_act,
            train_act=train_act,
            contact_act='',
            blog_act=blog_act,
            cred_act=cred_act
        )

    new_content = re.sub(r'<header[^>]*>.*?</header>', header_html, content, flags=re.DOTALL)

    if new_content != content:
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated header in {fn}')
