import os

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add explicit rules to make the back links black
fix = """
.detail-back, .blog-back {
    color: var(--ink) !important;
}
.detail-back:hover, .blog-back:hover {
    color: var(--accent) !important;
}
"""

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css + '\n' + fix)

print("Back links fixed!")
