a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for v in list(a):
    print(v)
    a.pop(v)

print(a)