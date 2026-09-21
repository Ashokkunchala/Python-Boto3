# Reference solution — attempt first.
from pathlib import Path
import json

def build_report():
    return {'files':[p.name for p in Path('.').glob('*.py')]}

Path('inventory.json').write_text(json.dumps(build_report(), indent=2))

