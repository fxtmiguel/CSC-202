class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Linked List'''

    def __init__(self, capacity):
        '''Creates and empty stack with a capacity'''
        self.capacity = capacity
        self.head = None
        self.num_items = 0

    def is_empty(self):
        return self.num_items == 0

        '''Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance'''

    def is_full(self):
        return self.capacity == self.num_items
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''

    def push(self, item):
        if not self.is_full():
            node1 = Node(item)  # makes the node
            temp = self.head  # temp node
            self.head = node1  # make it the head
            node1.next = temp  # Put the new node on top of list
            self.num_items += 1
        else:
            return IndexError
        '''If stack is not full, pushes item on stack.
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''

    def pop(self):
        if not self.is_empty():
            pop = self.head
            self.head = pop.next
            self.num_items -= 1
            return self.head
        else:
            return IndexError

        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''

    def peek(self):
        if not self.is_empty():
            pop = self.head
            return pop
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''

    def size(self):
        return self.num_items
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''
