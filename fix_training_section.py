import os

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add a specific green background to the .training section
fix = """
.training {
    background-color: #e8f5e9 !important; /* Soft, elegant light green */
    padding: 80px 0; /* ensure it has some padding to show the background nicely */
}
"""

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css + '\n' + fix)

# Bump HTML cache
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
        import re
        html = re.sub(r'styles\.css\?v=[0-9.]+', 'styles.css?v=8.0', html)
        with open(html_file, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(html)
    except Exception as e:
        pass

print("Training section background made green!")
