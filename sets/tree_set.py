from trees.bst import BST

# TODO: more functionality

class TreeSet:
    def __init__(self, keys=None):
        self.bst = BST()
        if keys:
            self.extend(keys)

    def __repr__(self):
        return 'TreeSet(%s)' % list(map(lambda item: item[0], self.bst.get_items()))

    def extend(self, keys):
        for key in keys:
            self.add(key)

    def add(self, key):
        self.bst.insert(key)
        print(self)

    def is_in(self, key):
        return bool(self.bst.find(key))

    def pop(self, key):
        self.bst.delete(key)
        print(self)
