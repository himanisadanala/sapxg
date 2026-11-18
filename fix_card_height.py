import os

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make sure why-card and why-card-link take up the full height of the grid cell
height_fix = """
.why-card-link {
    display: block;
    height: 100%;
}
.why-card {
    height: 100%;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}
/* Revert the padding we added for arrows since it's a grid again */
.why-card {
    padding: 30px !important;
}
"""

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css + '\n' + height_fix)

print("Card heights normalized!")
