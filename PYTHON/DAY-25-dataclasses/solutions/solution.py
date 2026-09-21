# Reference solution — attempt first.
from dataclasses import dataclass
@dataclass
class Instance:
    id: str
    state: str
print(Instance('i-001','running'))
