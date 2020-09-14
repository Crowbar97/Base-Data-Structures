from stack import ArrayStack

s = ArrayStack(3)

# [ None, None, None ]
s.print_array()

s.push(5)
s.push(6)
# 6 5
s.print()
# [ 5, 6, None ]
s.print_array()

# 6
print("Received:", s.pop())
# 5
print("Received:", s.pop())
# error, None
print("Received:", s.pop())
# Nothing
s.print()
# [ 5, 6, None ]
s.print_array()

s.push(7)
# 7
s.print()
# [ 7, 6, None ]
s.print_array()

s.push(8)
s.push(9)
# 9 8 7
s.print()
# [ 7, 8, 9 ]
s.print_array()

# error
s.push(10)
# 9, 8, 7
s.print()
# [ 7, 8, 9 ]
s.print_array()
