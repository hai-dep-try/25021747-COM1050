import json
import sys

# Fix encoding for Windows console
sys.stdout.reconfigure(encoding='utf-8')

with open('TH6_CS2.ipynb', encoding='utf-8') as f:
    nb = json.load(f)
    
cells = nb.get('cells', [])
for i, cell in enumerate(cells):
    source = cell.get('source', [])
    if isinstance(source, list):
        source = ''.join(source)
    if 'W6A9' in source.upper() or 'dict' in source.lower():
        print(f"=== Cell {i} ===")
        print(source)
        print()
