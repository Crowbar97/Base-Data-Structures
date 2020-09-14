from trees.bst import BST

# TODO: more functionality

class TreeDict:
    def __init__(self, items=None):
        self.bst = BST()
        if items:
            self.extend(items)
        print(self)

    def __repr__(self):
        return 'TreeDict(%s)' % self.bst.get_items()

    def extend(self, items):
        for (key, value) in items:
            self.add(key, value)

    def add(self, key, value):
        self.bst.insert(key, value)
        print(self)

    def get(self, key):
        node = self.bst.find(key)
        if node:
            return node.value
        return None

    def pop(self, key):
        self.bst.delete(key)
        print(self)
