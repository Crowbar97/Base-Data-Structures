from trees.bst import BST
from trees.trie import Trie
from trees.kdt import KDT, KDTNode

def test_bst():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(7)
    bst.insert(6)
    bst.insert(8)
    bst.insert(7)
    bst.insert(9)

    bst.preorder()
    bst.inorder()
    bst.postorder()

    print('Next:')
    x = 2
    while x:
        print(x, end=' ')
        x = bst.next(x)

    print('Prev:')
    x = 9
    while x:
        print(x, end=' ')
        x = bst.prev(x)

    x = 4
    print('Find %s: %s' % (x, bst.find(x)))
    x = 7
    print('Find %s: %s' % (x, bst.find(x)))
    x = 2
    print('Find %s: %s' % (x, bst.find(x)))
    x = 5
    print('Find %s: %s' % (x, bst.find(x)))
    x = 12
    print('Find %s: %s' % (x, bst.find(x)))

    print('Min: %s' % bst.min(bst.find(5)))
    print('Max: %s' % bst.max(bst.find(5)))

    bst.is_valid()
    bst.insert(6.5)
    target = bst.find(6.5)
    target.key = 10
    bst.print()
    bst.is_valid()
    target.key = 6.5
    bst.print()
    bst.is_valid()

    bst.delete(4)
    bst.delete(8)
    bst.delete(7)
    bst.delete(5)

    bst.clear()
    bst.insert(8)
    bst.insert(3)
    bst.insert(9)

def test_trie():
    t = Trie()
    t.insert('hello')
    t.insert('hellb')
    t.insert('hellc')
    t.insert('world')
    t.insert('how')
    t.insert('wow')
    t.insert('where')

    t.preorder()
    t.print()

    x = 'hello'
    print('Contains "%s": %s' % (x, x in t))
    x = 'how'
    print('Contains "%s": %s' % (x, x in t))
    x = 'hell'
    print('Contains "%s": %s' % (x, x in t))
    x = 'hell'
    print('Prefix "%s": %s' % (x, t.has_prefix(x)))
    x = 'wow'
    print('Prefix "%s": %s' % (x, t.has_prefix(x)))
    x = 'ho'
    print('Prefix "%s": %s' % (x, t.has_prefix(x)))
    x = 'hot'
    print('Prefix "%s": %s' % (x, t.has_prefix(x)))

    t.delete('world')
    t.delete('world')
    t.delete('hellb')

    print(t)

def test_kdt():
    kdt = KDT(dim=2)

    kdt.insert((2, 3))
    kdt.insert((3, 2))
    kdt.insert((1, 1))
    kdt.insert((0, 8))
    kdt.insert((1, 5))
    kdt.insert((3, 1))
    kdt.insert((4, 5))
    kdt.insert((2, 0))
    kdt.insert((5, 1))

    kdt.print()

    print('Rect: %s' % kdt.find_rect([ (2, 4), (2, 3) ]))
    print('Rect: %s' % kdt.find_rect([ (4, 8), (0, 2) ]))
    print('Exact: %s' % kdt.find((3, 2)))
    print('Exact: %s' % kdt.find((3, 4)))
    print('Partial: %s' % kdt.find((3, None)))
    print('Partial: %s' % kdt.find((None, 1)))

    kdt = KDT(dim=3)
    kdt.insert((1, 1, 1))
    kdt.insert((0, 1, 1))
    kdt.insert((5, 5, 5))
    kdt.insert((5, 2, 5))
    kdt.insert((5, 8, 5))
    kdt.insert((4, 8, 4))
    kdt.insert((8, 8, 6))
    kdt.insert((3, 8, 4))
    kdt.insert((5, 8, 4))
    kdt.insert((7, 8, 6))
    kdt.insert((9, 8, 6))
    kdt.insert((7, 9, 7))
    kdt.insert((9, 9, 6))

    kdt.print()
    node = kdt.root.right.right
    print('Min: %s' % kdt.find_min(node, node.axis))
    print('Max: %s' % kdt.find_max(node, node.axis))

    kdt.delete((5, 5, 5))

    kdt = KDT(dim=3)
    kdt.insert((10, 10, 10))
    kdt.insert((0, 1, 1))
    kdt.insert((15, 8, 12))
    kdt.insert((17, 5, 4))
    kdt.insert((11, 15, 5))
    kdt.insert((16, 10, 3))
    kdt.insert((14, 10, 14))
    kdt.insert((14, 12, 4))
    kdt.insert((20, 19, 2))
    kdt.insert((12, 15, 18))
    kdt.insert((15, 9, 8))
    kdt.insert((15, 10, 4))
    kdt.insert((12, 15, 1))
    kdt.insert((13, 12, 6))
    kdt.insert((12, 18, 6))

    kdt.print()

    kdt.delete((10, 10, 10))
    kdt.is_valid()
    kdt.delete((15, 8, 12))
    kdt.is_valid()

    print('Out of range value test:')
    node = kdt.find((12, 15, 18))[0]
    node_keys = node.keys
    node.keys = (8, 15, 18)
    kdt.print()
    kdt.is_valid()
    node.keys = node_keys

    print('Duplicate key value test:')
    node = kdt.find((14, 10, 14))[0]
    new_node = KDTNode((15, 9, 8))
    node.right = new_node
    new_node.parent = node
    new_node.axis = kdt.next_axis(node)
    kdt.print()
    kdt.is_valid()
    node.right = None

    print('Broken parent link test:')
    node = kdt.find((12, 15, 18))[0]
    node_parent = node.parent
    node.parent = 'Fake'
    kdt.print()
    kdt.is_valid()
    node.parent = node_parent

    kdt = KDT(dim=3)
    kdt.build_optimal([
        (10, 10, 10),
        (0, 1, 1),
        (15, 8, 12),
        (17, 5, 4),
        (11, 15, 5),
        (16, 10, 3),
        (14, 10, 14),
        (14, 12, 4),
        (20, 19, 2),
        (12, 15, 18),
        (15, 9, 8),
        (15, 10, 4),
        (12, 15, 1),
        (13, 12, 6),
        (12, 18, 6),
    ])
    kdt.print()
    kdt.is_valid()

# test_bst()
# test_trie()
test_kdt()
