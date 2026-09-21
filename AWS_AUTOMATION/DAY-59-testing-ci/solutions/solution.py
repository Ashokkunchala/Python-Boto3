# Reference design — implement and test your own version first.
def normalize(item):
    return {'id':item['id'],'state':item['state']}

def test_normalize():
    assert normalize({'id':'1','state':'running'}) == {'id':'1','state':'running'}
