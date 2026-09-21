# Read-only reference solution.
import boto3
client=boto3.client('lambda', region_name='ap-south-1')
for fn in client.list_functions().get('Functions',[]): print(fn['FunctionName'],fn.get('Runtime'))
