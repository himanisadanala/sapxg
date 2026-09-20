import re

with open('training.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Make the detail-page dark blue
html = html.replace('.detail-page{min-height:100vh;background:var(--grey)}', '.detail-page{min-height:100vh;background:#0F172A;color:#FFFFFF}')

# Make the h1 white so it's visible on dark blue
html = html.replace('.detail-page h1{font:600 clamp(46px,6vw,80px)/1 \'Space Grotesk\',sans-serif;margin:24px 0 28px}', '.detail-page h1{font:600 clamp(46px,6vw,80px)/1 \'Space Grotesk\',sans-serif;margin:24px 0 28px;color:#FFFFFF}')

# Make the intro text lighter
html = html.replace('.detail-intro{max-width:590px;color:var(--muted);font-size:20px;line-height:1.65;margin:0 0 34px}', '.detail-intro{max-width:590px;color:#CBD5E1;font-size:20px;line-height:1.65;margin:0 0 34px}')

# Ensure the cards on the page remain white with black text for contrast
html = html.replace('.detail-point{background:var(--white);padding:28px;border-top:3px solid var(--yellow)}', '.detail-point{background:var(--white);padding:28px;border-top:3px solid var(--yellow);color:var(--ink)}')

# Make the back button white so it's visible on dark blue if it's over it
# The back button is in the header, which is still white, so it's fine.

with open('training.html', 'w', encoding='utf-8', errors='ignore') as f:
    f.write(html)

print("Training page updated!")
