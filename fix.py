import os, glob
replacements = {
    'â†—': '↗',
    'â€”': '—',
    'âœ…': '✅',
    'â Œ': '❌',
    'âŒ›': '⏳',
    'â† ': '←',
    'â†’': '→',
    'ï¿½': '©'
}
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    orig = content
    for k, v in replacements.items():
        content = content.replace(k, v)
    if content != orig:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
