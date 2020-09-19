import random

# implemented by Russell Cohen post

def get_middle(l):
    return l[len(l) // 2]

def quickselect_median(l, less_fn, pivot_fn=get_middle):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) // 2, less_fn, pivot_fn)
    return (quickselect(l, len(l) // 2 - 1, less_fn, pivot_fn) +
            quickselect(l, len(l) // 2, less_fn, pivot_fn)) / 2


# TODO: implement classic version
# (with at least no extra space consumption)
def quickselect(l, k, less_fn, pivot_fn):
    """
        Selects the kth minimum in list (0-based)
        :param l: List of numerics
        :param k: Index of minimum
        :param less_fn: Function of x1 and x2 that returns True if x1 < x2
        :param pivot_fn: Function to choose a pivot
        :return: The kth minimum of l
    """
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [ el for el in l if less_fn(el, pivot) ]
    highs = [ el for el in l if less_fn(pivot, el) ]
    pivots = [ el for el in l if (not less_fn(el, pivot)) and (not less_fn(pivot, el)) ]

    if k < len(lows):
        return quickselect(lows, k, less_fn, pivot_fn)
    elif k < len(lows) + len(pivots):
        # We got lucky and guessed the median
        return pivots[0]
    else:
        return quickselect(highs, k - (len(lows) + len(pivots)), less_fn, pivot_fn)


if __name__ == '__main__':
    less_fn = lambda x, y: x < y
    print(quickselect_median([5, 2, 4, 3, 1], less_fn=less_fn))
    print(quickselect_median([5, 2, 4, 3, 1, 6], less_fn=less_fn))