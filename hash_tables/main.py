from hash_tables.hash_table import HashTable

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Dog(%s, %s)' % (self.name, self.age)

ht = HashTable(num_buckets=5)

ht.insert('mary', 528)
ht.insert('marty', 38)
ht.insert('max', 92)
ht.insert('john', 34)
ht.insert('abba', 28)
ht.insert('super', 55)
ht.insert('fernando', 35)
ht.insert('drums', 11)
ht.insert('pink floyd', 99)
ht.insert('bruce', 42)
ht.insert('im on fire', 28)

ht.insert('mary', 672)

ht.insert('dog', Dog('Jack', 8))

print(ht)
ht.print()

ht.delete('drums')
ht.delete('max')
ht.delete('fernando')
ht.delete('john')
ht.delete('super')

ht.insert('super', 55)
ht.print()

ht.delete('mex')

x = 'pink floyd'
print('%s: %s' % (x, ht[x]))

ht.clear()
ht.print()