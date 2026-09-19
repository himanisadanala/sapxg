import os

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the previous green training background with the dark blue one and text colors
import re
css = re.sub(r'\.training\s*\{[^}]+\}', '', css)

dark_training_css = """
.training {
    background-color: #1b2438 !important; /* Dark navy blue from screenshot */
    padding: 80px 0;
    color: #F8FAFC;
}
.training .training-heading h2 {
    color: #FFFFFF;
}
.training .training-heading p {
    color: #94A3B8;
}
.training .table-head {
    color: #94A3B8;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}
.training .training-row {
    border-bottom: 1px solid rgba(255,255,255,0.1);
}
.training .training-row b {
    color: #F8FAFC;
}
.training .training-row small {
    color: #64748B;
}
.training .training-row span {
    color: #E2E8F0;
}
"""

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css + '\n' + dark_training_css)

# Bump HTML cache
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
        html = re.sub(r'styles\.css\?v=[0-9.]+', 'styles.css?v=9.0', html)
        with open(html_file, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(html)
    except Exception as e:
        pass

print("Training section made dark blue with white text!")
