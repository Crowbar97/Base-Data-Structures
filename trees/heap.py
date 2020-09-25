from math import log2

# implemented by wiki materials

# insert / delete operations can be speed up
# if we will keep track of last element index
# instead of reallocating array each time

class HeapItem:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return '%s(%s, %s)' % (self.__class__.__name__, self.key, self.value)

    def __lt__(self, other):
        # print('LT: %s and %s' % (self, other))
        return self.key < other.key

    def __ge__(self, other):
        # print('GE: %s and %s' % (self, other))
        return self.key >= other.key

class Heap:

    def __init__(self, tuples=None):
        '''
        :param tuples: iterable collection of (key, value) tuples
        '''
        self.array = []
        self.extend(tuples)

    def __repr__(self):
        return 'Heap(%s)' % list(map(lambda item: (item.key, item.value), self.array))

    def __len__(self):
        return len(self.array)

    def print(self):
        print('Heap[s = %s]:' % len(self))
        if not self.array:
            print('Heap is empty!')
        self.rkl(0)

    # right-key-left traversal
    def rkl(self, ind):
        right_ind = 2 * ind + 2
        if right_ind < len(self):
            self.rkl(right_ind)

        print('%s%s' % (' ' * 4 * int(log2(ind + 1)), self.array[ind].key))

        left_ind = 2 * ind + 1
        if left_ind < len(self):
            self.rkl(left_ind)

    def extend(self, tuples):
        if tuples:
            for t in tuples:
                self.insert(t[0], t[1])

    # iterative version
    def sift_up(self, son_ind):
        # while not root
        while son_ind != 0:
            par_ind = (son_ind - 1) // 2
            if self.array[par_ind] < self.array[son_ind]:
                self.array[par_ind], self.array[son_ind] = self.array[son_ind], self.array[par_ind]
                son_ind = par_ind
            else:
                break

    def insert(self, key, value):
        item = HeapItem(key, value)
        self.array.append(item)
        self.sift_up(len(self) - 1)

    # iterative version
    def sift_down(self, par_ind):
        # while left son exist
        while 2 * par_ind + 1 < len(self):
            # pick left son
            max_son_ind = 2 * par_ind + 1

            # if right son exist and greater than left son
            # => pick him
            if ( max_son_ind + 1 < len(self)
                 and self.array[max_son_ind + 1] > self.array[max_son_ind] ):
                max_son_ind += 1

            # if heap property satisfied
            if self.array[par_ind] >= self.array[max_son_ind]:
                break

            # swap parent with max son
            self.array[par_ind], self.array[max_son_ind] = self.array[max_son_ind], self.array[par_ind]
            # go next
            par_ind = max_son_ind

    def extract_max(self):
        if not self.array:
            print('Error: heap is empty!')
            return None
        max = self.array[0]
        self.__delete(0)
        return (max.key, max.value)

    def build(self, tuples):
        self.array = [ HeapItem(key, value) for key, value in tuples ]
        for k in range(len(self) // 2 - 1, -1, -1):
            self.sift_down(k)

    def is_valid(self):
        for par_ind in range(len(self)):
            left_ind = 2 * par_ind + 1
            if left_ind < len(self):
                if self.array[par_ind] < self.array[left_ind]:
                    print('Error: parent "%s" (ind=%s) < left "%s" (ind=%s)'
                          % (self.array[par_ind], par_ind, self.array[left_ind], left_ind))
                    return False
                right_ind = left_ind + 1
                if right_ind < len(self):
                    if self.array[par_ind] < self.array[right_ind]:
                        print('Error: parent "%s" (ind=%s) < right "%s" (ind=%s)'
                              % (self.array[par_ind], par_ind, self.array[right_ind], right_ind))
                        return False
        print('Heap is valid!')
        return True

    def find(self, key):
        '''
        Finds all occurrences
        :param key: key to find
        :return: array of indices
        '''
        res = []
        self.__find(0, key, res)
        return res

    # traversal search
    # with extra branch excluding
    def __find(self, ind, key, res):
        if ind >= len(self):
            return

        if self.array[ind].key == key:
            res.append(ind)
        
        # search only if key can be found
        # in the child subtrees
        if key <= self.array[ind].key:
            self.__find(2 * ind + 1, key, res)
            self.__find(2 * ind + 2, key, res)

    def delete(self, key):
        inds = self.find(key)

        print('Key to delete: "%s"' % key)

        if not inds:
            print('No such key!')
            return False

        self.__delete(inds[0])
        return True

    def __delete(self, ind):
        '''
        Correct index expected
        '''
        if len(self) == 1:
            self.array.pop()
        else:
            old_key, new_key = self.array[ind], self.array[-1]
            self.array[ind] = self.array.pop()
            if new_key < old_key:
                self.sift_down(ind)
            else:
                self.sift_up(ind)
