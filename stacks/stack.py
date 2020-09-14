# own implementation by CLRS book
class ArrayStack:
    def __init__(self, size):
        self.array = [ None ] * size
        self.top = -1

    def is_full(self):
        return self.top == len(self.array) - 1

    def push(self, x):
        if self.is_full():
            print('Can\'t push: stack is full!')
        else:
            self.top += 1
            self.array[self.top] = x
            print('Pushed: %s' % self.array[self.top])

    def is_empty(self):
        return self.top == -1

    def pop(self):
        if self.is_empty():
            print('Can\'t pop: stack is empty!')
            return None

        x = self.array[self.top]
        self.top -= 1
        print('Popped: %s' % x)
        return x

    def print(self):
        print('Stack elements:')
        if self.is_empty():
            print('Nothing to print: stack is empty!')
        else:
            for i in range(self.top, -1, -1):
                print('\tstack[%s]: %s' % (i, self.array[i]))

    def print_array(self):
        print('Array:')
        for i in range(len(self.array)):
            print('\tarray[%s]: %s' % (i, self.array[i]), end='')
            if i == self.top:
                print(' <- top', end='')
            print()
