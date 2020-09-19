from math import inf
from copy import deepcopy

from sets.hash_set import HashSet

# TODO:
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

    GREATER = 1
    LESS = -1
    EQUAL = 0

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
            # for debug
            print('%s%s' % (' ' * 8 * h, '%s | %s' % (node.axis, node.keys)))
            # print('%s%s' % (' ' * 8 * h, '%s <- %s' % (node.parent and list(node.parent.keys), node.keys)))
            # print('%s%s' % (' ' * 8 * h, node.keys))
            self.rkl(node.left, h + 1)

    # TODO: draw links
    # TODO: print division axes above tree
    def print(self):
        print('KDTree[s = %s]:' % self.size)
        if self.size == 0:
            print('Tree is empty!')
        self.rkl(self.root, 0)

    def __concat_keys(self, keys, main_ind):
        return keys[main_ind:] + keys[:main_ind]

    # defines which son of base_node we should visit next
    # while searching target_node
    def get_order(self, base_node, target_node, axis=None):
        # explicit checking is needed because axis can be 0,
        # so 'not 0' == 'not None' == True
        if axis is None:
            axis = base_node.axis
        bn_superkey = self.__concat_keys(base_node.keys, axis)
        tn_superkey = self.__concat_keys(target_node.keys, axis)
        if tn_superkey > bn_superkey:
            return self.GREATER
        elif tn_superkey < bn_superkey:
            return self.LESS
        # all keys are equal
        return self.EQUAL

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
            order = self.get_order(node, new_node)
            # print('%s, %s: %s' % (node, new_node, order))
            if order is self.GREATER:
                if not node.right:
                    new_node.axis = self.next_axis(node)
                    node.right = new_node
                    new_node.parent = node
                    print('Inserted right!')
                    return True
                node = node.right
            elif order is self.LESS:
                if not node.left:
                    new_node.axis = self.next_axis(node)
                    node.left = new_node
                    new_node.parent = node
                    print('Inserted left!')
                    return True
                node = node.left
            # order is EQUAL
            else:
                print('Error: node with such keys exists!')
                return False

    # supports exact / partial query
    # need to specify key value for each axis
    # ('None' if any key value is correct)
    def find(self, keys):
        rect_bounds = [ (key, key) if key is not None else (-inf, inf) for key in keys ]
        return self.find_rect(rect_bounds)

    # rect query
    # need to specify bounds for each axis
    def find_rect(self, rect_bounds):
        if not self.dim_is_correct(rect_bounds):
            print('Rect\'s dim is not correct!')
        # print('Points inside %s:' % rect_bounds)
        res = []
        rect_bounds = [ Bounds(key[0], key[1]) for key in rect_bounds ]
        search_bounds = [ Bounds(-inf, inf) for _ in range(self.dim) ]
        self.__find_rect(rect_bounds, self.root, search_bounds, res)
        return res

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
    def __find_rect(self, rect_bounds, node, search_bounds, res):
        if self.in_region(rect_bounds, node):
            # print(node)
            res.append(node)
        
        sb_left = deepcopy(search_bounds)
        # left subtree values is bounded by max
        sb_left[node.axis].max = node.keys[node.axis]

        if node.left and self.intersect(rect_bounds, sb_left):
            self.__find_rect(rect_bounds, node.left, sb_left, res)

        sb_right = deepcopy(search_bounds)
        # right subtree values is bounded by min
        sb_left[node.axis].min = node.keys[node.axis]

        if node.right and self.intersect(rect_bounds, sb_right):
            self.__find_rect(rect_bounds, node.right, sb_right, res)

    # find axis-based min
    def find_min(self, node, axis):
        min_node = [ node ]
        self.__find_min(node, min_node, axis)
        return min_node[0]

    # traversal-based method
    def __find_min(self, node, min_node, axis):
        if self.get_order(min_node[0], node, axis) is self.LESS:
            min_node[0] = node
            print('New min: %s' % min_node[0])

        if node.left:
            self.__find_min(node.left, min_node, axis)
        if node.axis != axis and node.right:
            self.__find_min(node.right, min_node, axis)

    # find axis-based max
    def find_max(self, node, axis):
        max_node = [ node ]
        self.__find_max(node, max_node, axis)
        return max_node[0]

    # traversal-based method
    def __find_max(self, node, max_node, axis):
        if self.get_order(max_node[0], node, axis) is self.GREATER:
            max_node[0] = node
            print('New max: %s' % max_node[0])

        if node.right:
            self.__find_max(node.right, max_node, axis)
        if node.axis != axis and node.left:
            self.__find_max(node.left, max_node, axis)

    def delete(self, keys):
        print('Keys to delete: %s' % str(keys))
        res = self.find(keys)
        if not res:
            print('No node with such keys!')
            return False
        node = res[0]
        
        subtree_root = self.__delete(node)
        # if root
        if not node.parent:
            self.root = subtree_root
        else:
            if node.parent.left is node:
                node.parent.left = subtree_root
            else:
                print(node, node.parent)
                node.parent.right = subtree_root
        self.size -= 1
        self.print()
        return True

    # returns new subtree root
    def __delete(self, node):
        if not (node.left or node.right):
            return None
        
        # find node to replace
        if node.right:
            rep_node = self.find_min(node.right, node.axis)
        else:
            rep_node = self.find_max(node.left, node.axis)

        subtree_root = self.__delete(rep_node)

        if rep_node.parent.left is rep_node:
            rep_node.parent.left = subtree_root
        else:
            rep_node.parent.right = subtree_root
        
        print(rep_node)
        # make rep node new subtree root
        rep_node.axis = node.axis
        rep_node.left = node.left
        node.left.parent = rep_node
        rep_node.right = node.right
        node.right.parent = rep_node
        rep_node.parent = node.parent
        return rep_node

    # for numerical key values only
    def is_valid(self):
        bounds = [ Bounds(-inf, inf) for _ in range(self.dim) ]
        keys = HashSet()
        valid = self.__is_valid(self.root, bounds, keys)
        if valid:
            print('KDT is valid!')
        else:
            print('KDT is NOT valid!')
        return valid

    # traversal-based method
    # doesn't take into account 'get_order'
    # function rules, only value bounds and links
    def __is_valid(self, node, bounds, keys):
        if not node:
            return True

        if node.left:
            if node.left.parent is not node:
                print('Error (broken parent link): %s <- %s' % (node.left.parent, node.left))
                return False
        
        if node.right:
            if node.right.parent is not node:
                print('Error (broken parent link): %s <- %s' % (node.right.parent, node.right))
                return False

        for axis in range(self.dim):
            if not (bounds[axis].min <= node.keys[axis] <= bounds[axis].max):
                print('Error: #%s component of %s must be in [%s, %s]'
                      % (axis, node, bounds[axis].min, bounds[axis].max))
                return False

        if node.keys in keys:
            print('Error: keys of node %s already exists!' % node)
            return False
        keys.add(node.keys)

        bounds_left = deepcopy(bounds)
        bounds_left[node.axis].max = node.keys[node.axis]
        left_res = self.__is_valid(node.left, bounds_left, keys)

        bounds_right = deepcopy(bounds)
        bounds_right[node.axis].min = node.keys[node.axis]
        right_res = self.__is_valid(node.right, bounds_right, keys)

        return left_res and right_res