# Own implementation (by SSU course) 

# TODO: encapsulate all neccessary behaviour

# DLL Node
class DLLNode:

        def __init__(self, value):
            # can be object of any class
            self.value = value
            self.next = None
            self.prev = None

        def __repr__(self):
            return 'DLLNode(%s)' % self.value

# Doubly Linked List
class DLL:

    def __init__(self, init_values=None): 
        self.head = None
        self.tail = None
        self.size = 0
        if init_values:
            self.extend(init_values)

    def clear(self):
        self.__init__()

    def __repr__(self):
        nodes = []
        this_node = self.head
        while this_node:
            nodes.append(this_node.value)
            this_node = this_node.next
        return 'DLL(%s)' % nodes

    def __len__(self):
        return self.size

    def get_node(self, ind):
        if ind < 0 or ind >= self.size:
            # print('List of size %s has no node at index %s' % (ind, self.size))
            raise IndexError('Error: out of range!')
        this_node = self.head
        for _ in range(ind):
            this_node = this_node.next
        return this_node

    def __getitem__(self, ind):
        return self.get_node(ind).value

    def __iter__(self):
        # print('iter!')
        node = self.head
        while node:
            yield node.value
            node = node.next

    # method should satisfy two cases:
    # no one node in the list and otherwise
    def push_front(self, value):
        # creating new node
        new_node = DLLNode(value)       
  
        # if list not empty
        if self.head:
            # setting new node as prev
            self.head.prev = new_node
            # setting first node as next
            new_node.next = self.head
        else:
            # initializing tail
            self.tail = new_node
  
        # setting new head
        self.head = new_node

        self.size += 1

        print(self, self.size)
  
    # method should satisfy two cases:
    # no one node in the list and otherwise
    def push_back(self, value):
        # creating new node
        new_node = DLLNode(value)

        if self.head:
            self.tail.next = new_node
            new_node.prev = self.tail
        else:
            self.head = new_node
  
        self.tail = new_node

        self.size += 1

        # print(self, self.size)
        
    def insert(self, ind, value):
        # if first position or incorrect negative
        if ind <= 0:
            self.push_front(value)
        # if incorrect large
        elif ind >= self.size:
            self.push_back(value)
        # in the middle
        else:
            this_node = self.get_node(ind)
            new_node = DLLNode(value)
            new_node.next = this_node
            new_node.prev = this_node.prev
            this_node.prev.next = new_node
            this_node.prev = new_node
            self.size += 1
            print(self, self.size)

    def extend(self, values):
        for value in values:
            self.push_back(value)
        print(self, self.size)

    def __setitem__(self, ind, value):
        if ind < 0 or ind >= self.size:
            print('Index out of range!')
        else:
            self.get_node(ind).value = value
        print(self)

    def pop_front(self):
        # if list is empty
        if not self.head:
            print('Pop front error: list is empty!')
            return None
        
        # save value
        value = self.head.value

        # if next element exist
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        # => list consists of single element
        else:
            self.head = self.tail = None

        self.size -= 1
        return value

    def pop_back(self):
        # if list is empty
        if not self.tail:
            print('Pop back error: list is empty!')
            return None
        
        # save value
        value = self.tail.value

        # if prev element exist
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        # => list consists of single element
        else:
            self.tail = self.head = None

        self.size -= 1
        return value

    def pop(self, ind):
        # if first position or incorrect negative
        if ind <= 0:
            self.pop_front()
        # if incorrect large
        elif ind >= self.size - 1:
            self.pop_back()
        # from the middle
        else:
            this_node = self.get_node(ind)
            this_node.next.prev = this_node.prev
            this_node.prev.next = this_node.next
            self.size -= 1
            return this_node.value

    def find(self, selector):
        node = self.head
        while node and not selector(node.value):
            node = node.next
        return node

    def __contains__(self, value):
        return bool(self.find(lambda node_value: node_value == value))

    # !correct list node expected
    def delete(self, node):
        print('Deleting node: %s' % node)
        
        # if this node is last
        if self.head == self.tail:
            self.head = self.tail = None
        # front node
        elif node == self.head:
            node.next.prev = None
            self.head = node.next
        # last node
        elif node == self.tail:
            node.prev.next = None
            self.tail = node.prev
        # middle node
        else:
            node.next.prev = node.prev
            node.prev.next = node.next

        self.size -= 1

        return node.value

    def reverse(self):
        this_node = self.head
        while this_node:
            this_node.next, this_node.prev = this_node.prev, this_node.next
            this_node = this_node.prev
        self.head, self.tail = self.tail, self.head
    
    def is_empty(self):
        return self.size == 0

    def print(self):
        print('List (size = %s):' % self.size)
        if self.is_empty():
            print('List is empty!')
        else:
            this_node = self.head
            ind = 0
            while this_node:
                print('\tlist[%s]: %s' % (ind, this_node.value))
                this_node = this_node.next
                ind += 1
  