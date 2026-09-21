# Reference design — implement and test your own version first.
def bucket_record(bucket):
    return {'name':bucket['Name'],'created':bucket.get('CreationDate')}
print(bucket_record({'Name':'example'}))
