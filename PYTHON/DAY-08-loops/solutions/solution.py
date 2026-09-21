# Attempt the exercise first.
items=[{'state':'running'},{'state':'stopped'}]
print(sum(x['state']=='running' for x in items))
