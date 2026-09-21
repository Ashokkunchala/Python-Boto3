# Attempt the exercise first.
def valid_region(region, allowed=None):
    allowed=allowed or {'ap-south-1','us-east-1'}
    return region in allowed

print(valid_region('ap-south-1'))
