# Reference solution — attempt the exercise first.
from pathlib import Path
p=Path('servers.txt')
if p.exists():
    lines=p.read_text().splitlines()
    Path('summary.txt').write_text(f'lines={len(lines)}\n')

