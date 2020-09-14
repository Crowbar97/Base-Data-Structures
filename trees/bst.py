from math import inf

# Classic implementation with parent pointer
# from Brian Faure and SSU course

class Node:

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return 'Node(%s, %s)' % (self.key, self.value)

class BST:

    # TODO: levelorder (bfs)
    # TODO: visually divide methods in groups by '###'

    def __init__(self):
        self.root = None
        self.size = 0
        self.print()

    def clear(self):
        print('Clearing...')
        self.__init__()

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

    def height(self):
        return self.__height(self.root, -1)

    def __height(self, node, h):
        if not node:
            return h
        left_h = self.__height(node.left, h + 1)
        right_h = self.__height(node.right, h + 1)
        return max(left_h, right_h)

    # TODO: draw links
    def print(self):
        print('Tree[s = %s, h = %s]:' % (self.size, self.height()))
        if self.height() == -1:
            print('Tree is empty!')
        self.rkl(self.root, 0)
        # self.krl(self.root, 0)

    def preorder(self):
        print('Preorder:')
        self.__preorder(self.root)
        print()

    def __preorder(self, node):
        if node:
            print(node.key, end=' ')
            self.__preorder(node.left)
            self.__preorder(node.right)

    def inorder(self):
        print('Inorder:')
        self.__inorder(self.root)
        print()

    def __inorder(self, node):
        if node:
            self.__inorder(node.left)
            print(node.key, end=' ')
            self.__inorder(node.right)

    # get list of (key, value) items
    def get_items(self):
        tuples = []
        self.__get_items(self.root, tuples)
        return tuples

    def __get_items(self, node, tuples):
        if node:
            self.__get_items(node.left, tuples)
            tuples.append((node.key, node.value))
            self.__get_items(node.right, tuples)

    def postorder(self):
        print('Postorder:')
        self.__postorder(self.root)
        print()

    def __postorder(self, node):
        if node:
            self.__postorder(node.left)
            self.__postorder(node.right)
            print(node.key, end=' ')

    # for numerical keys only
    def is_valid(self):
        valid = self.__is_valid(self.root, -inf, inf)
        if valid:
            print('BST is valid!')
        else:
            print('BST is NOT valid!')
        return valid

    def __is_valid(self, node, min, max):
        if not node:
            return True

        if not (min < node.key < max):
            return False

        # can be speed up by using in single expression
        # with 'and' operator (will not perform extra calculations
        # if one of the branches already gave False)
        left_res = self.__is_valid(node.left, min, node.key)
        right_res = self.__is_valid(node.right, node.key, max)

        return left_res and right_res

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

    def find(self, key):
        return self.__find(self.root, key)

    def __find(self, node, key):
        # return found node or None
        if not node or key == node.key:
            return node
        if key < node.key:
            return self.__find(node.left, key)
        return self.__find(node.right, key)

    def degree(self, node):
        return bool(node.left) + bool(node.right)

    def min(self, node):
        if not node.left:
            return node
        return self.min(node.left)

    def max(self, node):
        if not node.right:
            return node
        return self.max(node.right)

    def delete(self, key):
        print('Deleting key: %s' % key)

        node = self.find(key)
        if node:
            self.__delete(node)
            self.size -= 1
            print('Deleted key: %s' % key)
        else:
            print('Error: no such key: %s' % key)

        self.print()

    def __delete(self, node):
        # cases 1 and 2: node has no one or single child
        if self.degree(node) < 2:
            print('Case 1-2!')

            # in case of single child -- we get him
            # in case of no child -- we get None
            if node.left:
                child = node.left
            else:
                child = node.right

            # if the node we delete is not root
            if node.parent:
                # replace the node to be deleted with its child or None
                if node.parent.left == node:
                    node.parent.left = child
                else:
                    node.parent.right = child
            else:
                self.root = child

            # if deleted node has child
            if self.degree(node) == 1:
                # bind him to the parent
                child.parent = node.parent
        # case 3: node has two children
        else:
            print('Case 3!')

            # get the inorder successor of the deleted node
            succ_node = self.min(node.right)

            # copy the inorder successor's key to the node
            node.key = succ_node.key
            node.value = succ_node.value

            # delete the inorder successor (that is extra for now)
            self.__delete(succ_node)

    def next(self, key):
        node = self.find(key)

        if not node:
            print('Error: no such key: %s' % key)
            return None

        if node.right:
            return self.min(node.right).key

        parent = node.parent
        while parent and parent.right == node:
            node = parent
            parent = parent.parent
        if parent:
            return parent.key
        
        print('Error: key %s is max, so it\'s no next key for it!' % key)
        return None

    def prev(self, key):
        node = self.find(key)

        if not node:
            print('Error: no such key: %s' % key)
            return None

        if node.left:
            return self.max(node.left).key
        
        parent = node.parent
        while parent and parent.left == node:
            node = parent
            parent = parent.parent
        if parent:
            return parent.key
        
        print('Error: key %s is min, so it\'s no prev key for it!' % key)
        return None