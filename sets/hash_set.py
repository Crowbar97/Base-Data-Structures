from hash_tables.hash_table import HashTable

class HashSet:

    def __init__(self, keys=None):
        self.ht = HashTable()
        if keys:
            self.extend(keys)
        # print(self)

    def __repr__(self):
        return 'HashSet(%s)' % list(self)

    def extend(self, keys):
        for key in keys:
            self.add(key)

    def add(self, key):
        self.ht.insert(key)
        # print(self)

    def __contains__(self, key):
        try:
            self.ht[key]
            return True
        except:
            return False

    def __len__(self):
        return len(self.ht)

    # iter by keys
    def __iter__(self):
        for t in self.ht:
            yield t[0]

    def pop(self, key):
        self.ht.delete(key)
        print(self)