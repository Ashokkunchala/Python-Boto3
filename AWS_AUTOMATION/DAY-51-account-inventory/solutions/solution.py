# Reference design — implement and test your own version first.
import boto3
session=boto3.Session(region_name='ap-south-1')
identity=session.client('sts').get_caller_identity()
print(identity['Account'])
