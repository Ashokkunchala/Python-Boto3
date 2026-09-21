# Read-only reference solution.
from botocore.config import Config
config=Config(retries={'mode':'adaptive','max_attempts':8}, connect_timeout=5, read_timeout=60)
print(config.retries)
