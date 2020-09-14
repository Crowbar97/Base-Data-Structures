from dll import DLL

# TODO: make cover testing by test cases
# TODO: make unit tests

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Dog(%s, %s)' % (self.name, self.age)

    def __eq__(self, other):
        return ( type(other) is type(self)
                 and self.name == other.name
                 and self.age == other.age )

dll = DLL()
dll.push_back(Dog('Jack', 8))
dll.push_back(3)
dll.push_back(4)
dll.extend([5, 6, 7])
dll.push_back(8)

dll[2] = 999
dll[-1] = 5
dll[20] = 7

print('List iteration:')
print('First:')
for i, item in enumerate(dll):
    print('%s: %s' % (i, item))
print('Second:')
for i, item in enumerate(dll):
    print('%s: %s' % (i, item))

x = 3
print('Contains %s: %s' % (x, x in dll))
x = 4
print('Contains %s: %s' % (x, x in dll))
x = Dog('Jack', 8)
print('Contains %s: %s' % (x, x in dll))

dll.clear()
print(dll, dll.size)

dll.push_front(4)
print(dll, dll.size)

dll.push_front(3)
print(dll, dll.size)

dll.insert(0, 2)
print(dll, dll.size)

dll.insert(-5, 1)
print(dll, dll.size)

dll.insert(1, 2.5)
print(dll, dll.size)

dll.reverse()
print(dll, dll.size)

dll.print()

dll.pop_front()
print(dll, dll.size)

dll.pop_back()
print(dll, dll.size)

dll.pop(1)
print(dll, dll.size)

dll.clear()
print(dll, dll.size)

dll.print()

print([DLL([5, 6]), DLL([7, 8])])
