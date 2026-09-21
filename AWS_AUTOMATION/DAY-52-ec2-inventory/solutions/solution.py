# Reference design — implement and test your own version first.
def flatten(instance, region):
    return {'region':region,'id':instance['InstanceId'],'state':instance['State']['Name']}
print(flatten({'InstanceId':'i-001','State':{'Name':'running'}},'ap-south-1'))
