# Reference solution — attempt first.
from contextlib import contextmanager
@contextmanager
def managed():
    print('start')
    try: yield
    finally: print('cleanup')
with managed(): print('work')
