# Reference solution — attempt the exercise first.
from pathlib import Path
import json
report={'hostname':'local','files':[p.name for p in Path('.').glob('*.py')]}
Path('report.json').write_text(json.dumps(report, indent=2))
print('report.json created')

