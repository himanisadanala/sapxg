import os

with open('career.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the HTML element for pagination
html = html.replace('<!-- Add Pagination -->\n        <div class="swiper-pagination"></div>', '')

# Remove the JS configuration for pagination
pagination_js = """      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },"""
html = html.replace(pagination_js, '')

with open('career.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Pagination dots removed!")
