# Reference solution — attempt first.
class Resource:
    def __init__(self,name): self.name=name
class EC2Server(Resource):
    service='ec2'
print(EC2Server('web-01').service)
