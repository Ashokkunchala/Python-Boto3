# Reference solution — attempt first.
from typing import Iterable

def names(items: Iterable[dict[str,str]]) -> list[str]:
    return [x['name'] for x in items]
print(names([{'name':'web-01'}]))
