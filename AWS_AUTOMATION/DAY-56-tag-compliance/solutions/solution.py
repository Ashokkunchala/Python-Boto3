# Reference design — implement and test your own version first.
def missing_tags(tags, required):
    return sorted(set(required)-set(tags))
print(missing_tags({'Environment':'prod'},{'Environment','Owner'}))
