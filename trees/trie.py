from dicts.hash_dict import HashDict

# implemented by Tushar Roy lesson

class TrieNode:

    def __init__(self):
        self.children = HashDict()
        self.is_word = False

    # not conventional
    def __repr__(self):
        return 'TrieNode<%s, %s>' % (repr(self.children), self.is_word)

class Trie:

    def __init__(self, words=None):
        self.root = TrieNode()
        self.size = 0
        if words:
            extend(words)
        self.print()

    def clear(self):
        print('Clearing...')
        self.__init__()
    
    def extend(self, words):
        for word in words:
            self.insert(word)

    def __repr__(self):
        return 'Trie(%s)' % list(self)

    def __yield_words(self, node, prefix):
        if node.is_word:
            yield prefix
        for char in node.children:
            for word in self.__yield_words(node.children[char], prefix + char):
                yield word
                
    def __iter__(self):
        return self.__yield_words(self.root, '')

    def preorder(self):
        print('Preorder:')
        self.__preorder(self.root)
        print()

    def __preorder(self, node):
        for char in node.children:
            print(char, end=' ')
            self.__preorder(node.children[char])

    # right-key-left traversal
    def __rkl(self, node, link_label, h):
        num_ch = len(node.children)

        for char in list(node.children)[:num_ch // 2]:
            self.__rkl(node.children[char], char, h + 1)
        
        print('%s%s' % (' ' * 4 * h, link_label))

        for char in list(node.children)[num_ch // 2:]:
            self.__rkl(node.children[char], char, h + 1)

    def print(self):
        print('Trie:')
        print(self.root)
        self.__rkl(self.root, '@', 0)

    # iterative version
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    # iterative version
    def __get_node(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

    def __contains__(self, word):
        return self.__get_node(word).is_word

    def has_prefix(self, prefix):
        return bool(self.__get_node(prefix))

    # recursive version
    def delete(self, seq):
        print('Deleting: "%s"' % seq)
        deleted = self.__delete(self.root, seq, 0)
        self.print()
        return deleted

    def __delete(self, node, seq, ind):
        if not node:
            print('Error: no such seq!')
            return False

        if ind == len(seq):
            if node.is_word:
                node.is_word = False
                print('Flag removed!')
                return not node.children
            print('Error: this is prefix!')
            return False
        
        char = seq[ind]
        no_children = self.__delete(node.children[char], seq, ind + 1)

        if no_children:
            node.children.pop(char)
            print('Removed: %s' % char)
            return not node.children

        return False
            