# Read-only reference solution.
import boto3
session=boto3.Session()
sts=session.client('sts')
identity=sts.get_caller_identity()
print({'account':identity['Account'],'arn':identity['Arn']})
