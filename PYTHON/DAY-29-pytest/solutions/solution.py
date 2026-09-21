# Reference solution — attempt first.
def resource_names(items):
    return [x['name'] for x in items]

def test_resource_names():
    assert resource_names([{'name':'web-01'}]) == ['web-01']

