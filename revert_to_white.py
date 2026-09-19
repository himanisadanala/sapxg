import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Restore CSS Variables to light theme
css = re.sub(r'--white:\s*#[0-9A-Fa-f]+;', '--white: #FAFAFA;', css)
css = re.sub(r'--card:\s*#[0-9A-Fa-f]+;', '--card: #FFFFFF;', css)

# Restore the body tag to just use var(--white)
body_pattern = r'body\s*\{[^}]+\}'
light_body = """body {
    margin: 0;
    color: var(--ink);
    font: 16px/1.55 'Inter', system-ui, sans-serif;
    background: var(--white);
}"""
css = re.sub(body_pattern, light_body, css, count=1)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Restored Light Theme background!")
