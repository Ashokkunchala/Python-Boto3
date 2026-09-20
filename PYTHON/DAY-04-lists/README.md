# Day 4 — Lists

## Learn
A list stores an ordered collection and can be changed.

```python
services = ["EC2", "S3", "RDS"]
services.append("Lambda")
print(services)
print(services[0])
```

Useful operations: `append()`, `remove()`, `len()`, indexing and slicing.

## Exercises
1. Create a list of five AWS services.
2. Add a service.
3. Remove a service.
4. Print the first and last item.
5. Loop over the list.

## Mini challenge
Create a list of servers and print a numbered inventory.

## DevOps connection
Boto3 frequently returns collections of resources. Lists are one of the first structures you will use to process them.

## Checklist
- [ ] I can create a list.
- [ ] I can add/remove items.
- [ ] I can access indexes.
- [ ] I can loop through a list.
