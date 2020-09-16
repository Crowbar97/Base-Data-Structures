# TODO:
# plain insert
# find partial / exact match
# rect-query search
# delete
# build optimal tree
# KNN

# implemented by original paper and own BST implementation

class KDTNode:

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return 'Node(%s, %s)' % (self.key, self.value)

class KDT:

    def __init__(self):
        self.root = None
        self.size = 0
        # self.print()

    def clear(self):
        print('Clearing...')
        self.__init__()
    
    def insert(self, key, value=None):
        print('Inserting key: %s' % key)

        inserted = True
        # if root exist => run iterations from root
        if self.root:
            inserted = self.__insert(self.root, key, value)
        # else make root
        else:
            self.root = Node(key, value)

        if inserted:
            self.size += 1
            print('Inserted: %s' % key)
        else:
            print('Error: key already exist: %s' % key)
        self.print()

    def __insert(self, node, key, value):
        if key < node.key:
            # beforehand checking
            if node.left:
                return self.__insert(node.left, key, value)
            node.left = Node(key, value)
            node.left.parent = node
            return True

        if key > node.key:
            # beforehand checking
            if node.right:
                return self.__insert(node.right, key, value)
            node.right = Node(key, value)
            node.right.parent = node
            return True

        # key exist
        return False