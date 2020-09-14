from queue import ArrayQueue

# queue of size 4
s = ArrayQueue(4)
# Nothing
s.print()
# [ None, None, None, None, None ]
s.print_cont()

s.enqueue(5)
s.enqueue(6)
# 5, 6
s.print()
# [ 5, 6, None, None, None ]
s.print_cont()

# 5
print("Received:", s.dequeue())
# 6
print("Received:", s.dequeue())
# error: empty, None
print("Received:", s.dequeue())
# Nothing
s.print()
# [ 5, 6, None, None, None ]
s.print_cont()

s.enqueue(7)
# 7
s.print()
# [ 5, 6, 7, None, None ]
s.print_cont()

s.enqueue(8)
# 7, 8
s.print()
# [ 5, 6, 7, 8, None ]
s.print_cont()

s.enqueue(9)
# 7, 8, 9
s.print()
# [ 5, 6, 7, 8, 9 ]
s.print_cont()

s.enqueue(10)
# 7, 8, 9, 10
s.print()
# [ 10, 6, 7, 8, 9 ]
s.print_cont()

# error: full
s.enqueue(11)
# 7, 8, 9, 10
s.print()
# [ 10, 6, 7, 8, 9 ]
s.print_cont()

# 7
print("Received:", s.dequeue())
# 8, 9, 10
s.print()
# [ 10, 6, 7, 8, 9 ]
s.print_cont()

# 8
print("Received:", s.dequeue())
# 9, 10
s.print()
# [ 10, 6, 7, 8, 9 ]
s.print_cont()

# 9
print("Received:", s.dequeue())
# 10
s.print()
# [ 10, 6, 7, 8, 9 ]
s.print_cont()

# 10
print("Received:", s.dequeue())
# Nothing
s.print()
# [ 10, 6, 7, 8, 9 ]
s.print_cont()

# error: empty, None
print("Received:", s.dequeue())
# Nothing
s.print()
# [ 10, 6, 7, 8, 9 ]
s.print_cont()
