from lists.dll import DLL
from hash_tables.hasher import hash_obj

# Own implementation inspired by PageKey Solutions

# TODO: refactor
# TODO: implement bst(red-black tree)-based hash table (like in Java)

class HTItem:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return 'HTItem(%s, %s)' % (self.key, self.value)

class HashTable:

    def __init__(self, tuples=None, num_buckets=5):
        self.buckets = [ DLL() for _ in range(num_buckets) ]
        self.size = 0
        if tuples:
            self.extend(tuples)
        # print(self)

    def __repr__(self):
        return 'HashTable(%s)' % list(self)
        
    def print(self):
        print('Hash Table:')
        for i, dll in enumerate(self.buckets):
            print('%s: %s' % (i, dll))
    
    def extend(self, tuples):
        for t in tuples:
            self.insert(t[0], t[1])

    def clear(self):
        self.__init__(num_buckets=len(self.buckets))

    def get_hash(self, key):
        return hash_obj(key, len(self.buckets))

    def insert(self, key, value=None):
        ind = self.get_hash(key)
        dll = self.buckets[ind]

        for item in dll:
            if item.key == key:
                print('Changed item (key = %s) value: %s -> %s' % (item.key, item.value, value))
                item.value = value
                return

        dll.push_back(HTItem(key, value))
        # print('Inserted item: %s in bucket #%s' % ((key, value), ind))
        self.size += 1

    def delete(self, key):
        ind = self.get_hash(key)
        dll = self.buckets[ind]

        for i, item in enumerate(dll):
            if item.key == key:
                dll.pop(i)
                print('Deleted item: %s' % (item))
                self.size -= 1
                print(self)
                return
        
        print('Item with key "%s" not found!' % key)

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        ind = self.get_hash(key)
        dll = self.buckets[ind]

        for item in dll:
            if item.key == key:
                return item.value

        raise Exception('No such key: "%s"' % key)
    
    # iter by tuples
    def __iter__(self):
        for dll in self.buckets:
            for item in dll:
                yield (item.key, item.value)