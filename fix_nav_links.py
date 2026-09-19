import os

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add explicit rules to make the nav links black
fix = """
.site-nav a, .nav-link, .nav-links a {
    color: var(--ink) !important;
}
.site-nav a:hover, .nav-link:hover, .nav-links a:hover {
    color: var(--accent) !important;
}
"""

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css + '\n' + fix)

print("Nav links fixed!")
