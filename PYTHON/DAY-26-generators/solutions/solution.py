# Reference solution — attempt first.
def names(items):
    for item in items:
        yield item['name']
print(list(names([{'name':'a'},{'name':'b'}])))
