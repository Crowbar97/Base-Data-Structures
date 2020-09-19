from hash_tables.hash_table import HashTable

# TODO: implement in single dict with base (Tree / Hash) switcher

# TODO: does this wrapper make sense?
# it only calls methods from hash table
class HashDict:
    
    def __init__(self, tuples=None):
        self.ht = HashTable(tuples)
        print(self)

    def __repr__(self):
        return 'HashDict(%s)' % list(self.ht)

    def extend(self, tuples):
        for (key, value) in tuples:
            self.add(key, value)
    
    def add(self, key, value):
        self.ht.insert(key, value)
        print(self)

    def __getitem__(self, key):
        return self.ht[key]

    def __setitem__(self, key, value):
        self.ht.insert(key, value)

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

    