# own implementation by CLRS book
class ArrayQueue:
    def __init__(self, size):
        self.array = [ None ] * (size + 1)
        self.head = 0
        self.tail = 0

    def is_full(self):
        return (self.tail + 1) % len(self.array) == self.head

    def enqueue(self, x):
        if self.is_full():
            print('Can\'t enq: queue is full!')
        else:
            self.array[self.tail] = x
            print('Enqueued: %s' % self.array[self.tail])
            self.tail = (self.tail + 1) % len(self.array)

    def is_empty(self):
        return self.tail == self.head

    def dequeue(self):
        if self.is_empty():
            print('Can\'t deq: queue is empty!')
            return None
        x = self.array[self.head]
        print('Dequeued: %s' % x)
        self.head = (self.head + 1) % len(self.array)
        return x

    def print(self):
        print('Queue elements:')
        if self.is_empty():
            print('Nothing to print: queue is empty!')
        else:
            abs_tail = self.tail
            if self.head > self.tail:
                abs_tail += len(self.array)

            for i in range(self.head, abs_tail):
                print('\tqueue[%s]: %s' % (i - self.head, self.array[i % len(self.array)]))

    def print_cont(self):
        print('Array:')
        for i in range(len(self.array)):
            print('\tarray[%s]: %s' % (i, self.array[i]), end='')
            if i == self.head:
                print(' <- h', end='')
            if i == self.tail:
                print(' <- t', end='')
            print()


