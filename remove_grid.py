import os

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

grid_html = """
    <section class="reorder-stage section-shell">
        <div class="eyebrow" style="margin-bottom: 30px; justify-content: center; width: 100%;"><span></span> Interactive Grid</div>
        <div class="reorder-grid" id="reorder-grid" aria-label="Reorderable grid">
        </div>
    </section>
"""

script_html = """<script src="https://cdn.jsdelivr.net/npm/sortablejs@latest/Sortable.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    const grid = document.getElementById("reorder-grid");
    if(grid) {
      for(let i = 1; i <= 16; i++) {
        const item = document.createElement("div");
        item.className = "reorder-item";
        item.style.backgroundColor = `var(--hue-${(i % 6) + 1})`;
        item.innerText = String(i).padStart(2, "0");
        grid.appendChild(item);
      }
      new Sortable(grid, {
        animation: 350,
        easing: "cubic-bezier(0.175, 0.885, 0.32, 1.275)",
        ghostClass: "sortable-ghost",
        chosenClass: "sortable-chosen",
        dragClass: "sortable-drag"
      });
    }
  });
</script>"""

# We'll just replace them with empty strings
if grid_html in html:
    html = html.replace(grid_html, "")
else:
    # try a more flexible removal for grid html
    import re
    html = re.sub(r'<section class="reorder-stage section-shell">.*?</section>', '', html, flags=re.DOTALL)

if script_html in html:
    html = html.replace(script_html, "")
else:
    html = html.replace(script_html + '\n', "")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Remove from styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_append = """/* Reorder Grid Component */
.reorder-stage {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    touch-action: none;
    padding-top: 100px;
    padding-bottom: 100px;
}

.reorder-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 8px;
    width: min(76vw, 420px);
}

.reorder-item {
    display: grid;
    place-items: center;
    aspect-ratio: 1;
    color: #FAFAFA;
    cursor: grab;
    font-family: 'Space Grotesk', monospace;
    font-size: clamp(11px, 2.2vw, 15px);
    font-weight: 600;
    user-select: none;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    transition: transform 0.2s, box-shadow 0.2s;
    border: 1px solid rgba(255,255,255,0.1);
}

.reorder-item:active {
    cursor: grabbing;
}

.sortable-ghost {
    opacity: 0.2;
}

.sortable-chosen {
    transform: scale(1.08);
    box-shadow: 0 15px 25px rgba(245, 158, 11, 0.3);
    z-index: 10;
}

:root {
    --hue-1: #311B92; /* Royal Purple Deep */
    --hue-2: #B45309; /* Deep Amber */
    --hue-3: #1A237E; /* Deep Royal Blue */
    --hue-4: #880E4F; /* Royal Burgundy */
    --hue-5: #004D40; /* Royal Emerald */
    --hue-6: #F59E0B; /* Bright Gold Accent */
}"""

if css_append in css:
    css = css.replace(css_append, "")
else:
    # Find the start of the block and truncate
    idx = css.find("/* Reorder Grid Component */")
    if idx != -1:
        css = css[:idx]

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Grid removed successfully!")
