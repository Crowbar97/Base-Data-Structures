from hash_tables.hash_table import HashTable

class HashSet:
    def __init__(self, keys=None):
        self.bst = HashTable()
        if keys:
            self.extend(keys)

    def __repr__(self):
        return 'HashSet(%s)' % list(map(lambda item: item[0], self.ht.get_items()))

    def extend(self, keys):
        for key in keys:
            self.add(key)

    def add(self, key):
        self.ht.insert(key)
        print(self)

    def is_in(self, key):
        return bool(self.ht.get(key))

    def pop(self, key):
        self.ht.delete(key)
        print(self)