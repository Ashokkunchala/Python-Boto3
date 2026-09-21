# Reference solution — attempt first.
class Server:
    def __init__(self,name,state): self.name,self.state=name,state
    def healthy(self): return self.state=='running'
print(Server('web-01','running').healthy())
