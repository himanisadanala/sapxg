import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Completely clean the body tag
body_pattern = r'body\s*\{[^}]+\}'
new_body = """body {
    margin: 0;
    color: var(--ink);
    font: 16px/1.55 'Inter', system-ui, sans-serif;
    background-color: #0A0A0A;
    background-image: 
        repeating-linear-gradient(45deg, rgba(212, 175, 55, 0.04) 0px, rgba(212, 175, 55, 0.04) 1px, transparent 1px, transparent 40px), 
        repeating-linear-gradient(-45deg, rgba(212, 175, 55, 0.04) 0px, rgba(212, 175, 55, 0.04) 1px, transparent 1px, transparent 40px), 
        radial-gradient(ellipse at top, rgba(212, 175, 55, 0.1) 0%, transparent 60%);
    background-attachment: fixed;
    min-height: 100vh;
}"""

css = re.sub(body_pattern, new_body, css, count=1)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Body tag thoroughly cleaned and Art Deco background applied!")
