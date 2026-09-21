# Read-only reference solution.
import boto3
client=boto3.client('dynamodb', region_name='ap-south-1')
print(client.list_tables().get('TableNames',[]))
