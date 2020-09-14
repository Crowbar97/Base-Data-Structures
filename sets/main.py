from sets.tree_set import TreeSet

# TODO: more tests

ts = TreeSet([
    'bob',
    'max',
    'clara',
])

ts.add('alice')
ts.add('tim')

print(ts.is_in('max'))
print(ts.is_in('jack'))

ts.pop('max')