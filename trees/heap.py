from math import log2

# TODO:
# delete
# use decrease and increase for insertion, deletion and extraction
# use heap item

# implemented by wiki materials

class Heap:

    def __init__(self, values=None):
        self.array = []
        self.extend(values)

    def __repr__(self):
        return 'Heap(%s)' % self.array

    def print(self):
        print('Heap[s = %s]:' % len(self.array))
        if not self.array:
            print('Heap is empty!')
        self.rkl(0)

    # right-key-left traversal
    def rkl(self, ind):
        right_ind = 2 * ind + 2
        if right_ind < len(self.array):
            self.rkl(right_ind)

        print('%s%s' % (' ' * 4 * int(log2(ind + 1)), self.array[ind]))

        left_ind = 2 * ind + 1
        if left_ind < len(self.array):
            self.rkl(left_ind)

    def extend(self, values):
        if values:
            for value in values:
                self.insert(value)

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

    def insert(self, value):
        self.array.append(value)
        self.sift_up(len(self.array) - 1)

    # iterative version
    def sift_down(self, par_ind):
        # while left son exist
        while 2 * par_ind + 1 < len(self.array):
            # pick left son
            max_son_ind = 2 * par_ind + 1

            # if right son exist and greater than left son
            # => pick him
            if ( max_son_ind + 1 < len(self.array)
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
        self.array[0] = self.array.pop()
        self.sift_down(0)
        return max

    def build(self, values):
        self.array = list(values)
        for k in range(len(self.array) // 2 - 1, -1, -1):
            self.sift_down(k)

    def is_valid(self):
        for par_ind in range(len(self.array)):
            left_ind = 2 * par_ind + 1
            if left_ind < len(self.array):
                if self.array[par_ind] < self.array[left_ind]:
                    print('Error: parent "%s" (ind=%s) < left "%s" (ind=%s)'
                          % (self.array[par_ind], par_ind, self.array[left_ind], left_ind))
                    return False
                right_ind = left_ind + 1
                if right_ind < len(self.array):
                    if self.array[par_ind] < self.array[right_ind]:
                        print('Error: parent "%s" (ind=%s) < right "%s" (ind=%s)'
                              % (self.array[par_ind], par_ind, self.array[right_ind], right_ind))
                        return False
        print('Heap is valid!')
        return True

    # finds all occurrences
    def find(self, value):
        res = []
        self.__find(0, value, res)
        return res

    # traversal search
    # with extra branch excluding
    def __find(self, ind, value, res):
        if ind >= len(self.array):
            return

        if self.array[ind] == value:
            res.append(ind)
        
        # find only if value can be found
        # in the child subtrees
        if value <= self.array[ind]:
            self.__find(2 * ind + 1, value, res)
            self.__find(2 * ind + 2, value, res)

    def delete(self, value):
        pass

# a = [5, 9, 2, 1, 0 ,5 ,7 ,2]
# heap_sort(a)
# print(a)