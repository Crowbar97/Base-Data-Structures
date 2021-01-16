from math import log, e
from random import randint

from hash_tables.hasher import hash_obj as hash_fun

class BloomFilter:

    def __init__(self, num_elems=10, fp_prob=0.01):
        '''
            num_elems -- approximate num of elements to be stored
            fp_prob -- false positive probability
        '''

        print('Bloom filter input params:')
        print('\tnum_elems: %s' % num_elems)
        print('\tfp_prob: %s' % fp_prob)

        print('Calculated optimal params:')
        # calculating optimal array length
        length = -log(fp_prob, 2) / log(2, e) * num_elems
        length = int(length + 0.5)
        self.array = [ False ] * length
        print('\tlength: %s' % len(self.array))

        # calculating optimal num of hash functions
        num_hash_funs = -log(fp_prob, 2)
        num_hash_funs = int(num_hash_funs + 0.5)
        # TODO: set seed for randint?
        seeds = [ randint(1, 100) for _ in range(num_hash_funs) ]
        print('seeds: %s' % seeds)
        self.hash_funs = [ lambda obj, s=seed: hash_fun(obj, bound=len(self.array), seed=s)
                           for seed in seeds ]
        print('\tnum_hash_funs: %s' % len(self.hash_funs))

    def extend(self, values):
        for value in values:
            self.insert(value)

    def insert(self, value):
        for hash_fun in self.hash_funs:
            ind = hash_fun(value)
            # print(ind)
            self.array[ind] = True

    def contains(self, value):
        for hash_fun in self.hash_funs:
            ind = hash_fun(value)
            # print(ind)
            if not self.array[ind]:
                return False
        return True