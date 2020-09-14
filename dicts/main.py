from dicts.tree_dict import TreeDict
from dicts.hash_dict import HashDict

# TODO: more tests

def test_td():
    td = TreeDict([
        ('bob', 4),
        ('max', 5),
        ('clara', 5)
    ])

    td.add('alice', 6)
    td.add('tim', 6)

    print(td.get('max'))

    print(td)

    td.pop('max')

def test_hd():
    hd = HashDict([
        ('bob', 4),
        ('max', 5),
        ('clara', 5)
    ])

    hd.add('alice', 6)
    hd.add('tim', 6)

    print(hd['max'])

    print(hd)

    print('Hash dict iteration by keys:')
    print('First:')
    for item in hd:
        print(item)
    print('Second:')
    for item in hd:
        print(item)

    hd.pop('max')


# test_td()
test_hd()