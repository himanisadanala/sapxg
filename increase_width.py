import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the cards much wider so they fill up the space
if "width: min(80vw, 360px);" in html:
    html = html.replace("width: min(80vw, 360px);", "width: min(90vw, 700px);")

# Also, the previous script might have left multiple width declarations if I ran it multiple times? 
# I only ran it once.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Coverflow width increased!")
