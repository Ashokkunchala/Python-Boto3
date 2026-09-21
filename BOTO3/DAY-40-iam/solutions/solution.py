# Read-only reference solution.
import boto3
iam=boto3.client('iam')
print([r['RoleName'] for r in iam.list_roles(MaxItems=10).get('Roles',[])])
