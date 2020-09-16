from trees.bst import BST
from trees.trie import Trie

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


# test_bst()
test_trie()
