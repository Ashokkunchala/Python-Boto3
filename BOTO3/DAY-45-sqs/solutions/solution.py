# Read-only reference solution.
import boto3
client=boto3.client('sqs', region_name='ap-south-1')
print(client.list_queues().get('QueueUrls',[]))
