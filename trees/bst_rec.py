# laconic implementation without parent pointer (linking via recursion)
# from GeeksForGeeks (modified)

# BST node
class Node:

    def __init__(self, key):
        self.key = key
        # TODO: add field for data
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node(%s)' % self.key

# Binary Search Tree
class BST:

    def __init__(self):
        self.root = None

    # TODO: draw links
    def print(self):
        self.rkl(self.root, 0)
        # self.krl(self.root, 0)

    # right-key-left traversal
    def rkl(self, node, h):
        if node:
            self.rkl(node.right, h + 1)
            print('%s%s' % ('   ' * h, node.key))
            self.rkl(node.left, h + 1)

    # key-right-left traversal
    def krl(self, node, h):
        if node:
            print('%s%s' % ('   ' * h, node.key))
            self.krl(node.right, h + 1)
            self.krl(node.left, h + 1)

    def preorder(self):
        print('Preorder:')
        self.__preorder(self.root)

    def __preorder(self, node):
        if node:
            print(self.key)
            self.__preorder(node.right)
            self.__preorder(node.left)

    def inorder(self):
        print('Inorder:')
        self.__inorder(self.root)

    def __inorder(self, node):
        if node:
            self.__inorder(node.left)
            print(node.key)
            self.__inorder(node.right)

    def postorder(self):
        print('Postorder:')
        self.__postorder(self.root)

    def __postorder(self, node):
        if node:
            self.__postorder(node.left)
            self.__postorder(node.right)
            print(node.key)

    # insert wrapper
    def insert(self, key):
        print('Inserting: %s' % key)
        root = self.__insert(self.root, key)
        if not self.root:
            self.root = root
        self.print()
        return root

    # node -- current node to check
    # key -- key of the inserting node
    # returns root
    def __insert(self, node, key):
        # if the node not exist, return a new node
        if not node:
            return Node(key)

        # otherwise recur down the tree
        if key < node.key:
            node.left = self.__insert(node.left, key)
        else:
            node.right = self.__insert(node.right, key)

        # back from recursion
        return node

    # FIXME: it's not next, it's min in the right subtree
    def get_next(node):
        current = node

        # loop down to find the leftmost leaf
        while current.left:
            current = current.left

        return current

    # remove wrapper
    def remove(self, key):
        # TODO: remove root if empty
        self.__remove(self.root, key)

    # node -- current node to check
    # key -- key of the removal node
    def __remove(self, node, key):
        # if node not exist
        if not node:
            return node

        # if smaller
        if key < node.key:
            node.left = self.__remove(node.left, key)
        # if greater
        elif key > node.key:
            node.right = self.__remove(node.right, key)
        # if we found target node
        else:
            # if this node has only one or no child (cases 1 and 2)
            if not node.left:
                right_node = node.right
                node = None
                return right_node
            elif not node.right:
                left_node = node.left
                node = None
                return left_node

            # => this node has two children
            # getting next node
            next_node = get_next(node.right)
            # copying the key
            node.key = next_node.key
            # removing extra node: 1st or 2nd case
            node.right = self.__remove(node.right, next_node.key)

        # back from recursion
        return node
