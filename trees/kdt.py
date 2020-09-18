from math import inf
from copy import deepcopy

# TODO:

# delete
# build optimal tree
# KNN

# TODO: replace error prints with exceptions?

# TODO: plot 2D space division by tree

# implemented by original paper and own BST implementation
# with help of stefankoegl implementation

class Bounds:

    def __init__(self, min, max):
        self.min = min
        self.max = max

    # not conventional
    def __repr__(self):
        return '(%s, %s)' % (self.min, self.max)

class KDTNode:

    def __init__(self, keys=None, value=None):
        self.keys = keys
        self.value = value
        self.axis = None
        self.left = None
        self.right = None
        self.parent = None

    # not conventional
    def __repr__(self):
        return 'Node<%s, %s, %s>' % (self.keys, self.value, self.axis)

class KDT:

    RIGHT_SIDE = True
    LEFT_SIDE = False
    CURRENT_NODE = None

    def __init__(self, dim):
        self.root = None
        self.size = 0
        # tree dimensionality (of each compound key)
        self.dim = dim
        # self.print()

    def clear(self):
        print('Clearing...')
        self.__init__(self.dim)
    
    # right-key-left traversal
    def rkl(self, node, h):
        if node:
            self.rkl(node.right, h + 1)
            print('%s%s' % (' ' * 4 * h, '%s | %s' % (node.axis, node.keys)))
            self.rkl(node.left, h + 1)

    # TODO: draw links
    def print(self):
        print('KDTree[s = %s]:' % self.size)
        if self.size == 0:
            print('Tree is empty!')
        self.rkl(self.root, 0)

    def __concat_keys(self, keys, main_ind):
        keys = list(map(str, keys))
        first_part = ''.join(keys[main_ind:])
        second_part = ''.join(keys[:main_ind])
        return first_part + second_part

    # defines which son of base_node we should visit next
    # while searching target_node
    def get_side(self, base_node, target_node):
        bn_superkey = self.__concat_keys(base_node.keys, base_node.axis)
        tn_superkey = self.__concat_keys(target_node.keys, base_node.axis)
        if tn_superkey > bn_superkey:
            return self.RIGHT_SIDE
        elif tn_superkey < bn_superkey:
            return self.LEFT_SIDE
        # all keys are equal
        return self.CURRENT_NODE

    def next_axis(self, node):
        return (node.axis + 1) % self.dim

    def dim_is_correct(self, keys):
        return self.dim == len(keys)

    def insert(self, keys, value=None):
        inserted = self.__insert(keys, value)
        if inserted:
            self.size += 1
        return inserted

    # iterative version
    def __insert(self, keys, value=None):
        if not self.dim_is_correct(keys):
            print('Error: dim is not correct!')
            return False

        new_node = KDTNode(keys, value)

        if not self.root:
            new_node.axis = 0
            self.root = new_node
            print('Inserted root!')
            return True

        node = self.root
        while True:
            side = self.get_side(node, new_node)
            # here explicit check is necessary
            # because 'not False' == 'not None'
            if side is self.RIGHT_SIDE:
                if not node.right:
                    new_node.axis = self.next_axis(node)
                    node.right = new_node
                    print('Inserted right!')
                    return True
                node = node.right
            elif side is self.LEFT_SIDE:
                if not node.left:
                    new_node.axis = self.next_axis(node)
                    node.left = new_node
                    print('Inserted left!')
                    return True
                node = node.left
            # side is CURRENT_NODE
            else:
                print('Error: node with such keys exists!')
                return False

    # common case for exact and partial queries
    def rect_search(self, rect_bounds):
        if not self.dim_is_correct(rect_bounds):
            print('Rect\'s dim is not correct!')
        print('Points inside %s:' % rect_bounds)
        search_bounds = [ Bounds(-inf, inf) for _ in range(self.dim) ]
        self.__rect_search(rect_bounds, self.root, search_bounds)

    def in_region(self, rect_bounds, node):
        for axis in range(len(node.keys)):
            if not (rect_bounds[axis].min <= node.keys[axis] <= rect_bounds[axis].max):
                return False
        return True

    def intersect(self, rect_bounds, search_bounds):
        for axis in range(len(rect_bounds)):
            if ( search_bounds[axis].min > rect_bounds[axis].max
                 or search_bounds[axis].max < rect_bounds[axis].min ):
                return False
        return True

    # tree traversal search with excluding extra branches
    def __rect_search(self, rect_bounds, node, search_bounds):
        if self.in_region(rect_bounds, node):
            print(node)
        
        sb_left = deepcopy(search_bounds)
        # left subtree values is bounded by max
        sb_left[node.axis].max = node.keys[node.axis]

        if node.left and self.intersect(rect_bounds, sb_left):
            self.__rect_search(rect_bounds, node.left, sb_left)

        sb_right = deepcopy(search_bounds)
        # right subtree values is bounded by min
        sb_left[node.axis].min = node.keys[node.axis]

        if node.right and self.intersect(rect_bounds, sb_right):
            self.__rect_search(rect_bounds, node.right, sb_right)

    def find_min(node):
        pass

    def __find_min(node, min):
        pass

    def delete(self, keys):
        pass