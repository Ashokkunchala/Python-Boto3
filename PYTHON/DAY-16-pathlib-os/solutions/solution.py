# Reference solution — attempt the exercise first.
import os
from pathlib import Path
print([p.name for p in Path('.').glob('*.py')])
print(os.getenv('ENVIRONMENT','not-set'))

