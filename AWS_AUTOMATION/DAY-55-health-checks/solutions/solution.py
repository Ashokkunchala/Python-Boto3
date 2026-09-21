# Reference design — implement and test your own version first.
def check_state(actual, expected):
    return {'healthy':actual==expected,'actual':actual,'expected':expected}
print(check_state('running','running'))
