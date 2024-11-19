class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:
    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.front = None
        self.back = None
        self.num_items = 0

    pass

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise
        MUST have O(1) performance'''
        return self.num_items == 0

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise
         MUST have O(1) performance'''
        return self.num_items == self.capacity

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue
        If Queue is full when enqueue is attempted, raises IndexError
        MUST have O(1) performance'''
        if not self.is_full():
            node = Node(item)
            if self.front is None:
                self.front = node
            self.back = node
            self.num_items += 1
        else:
            raise IndexError

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
        If Queue is empty when dequeue is attempted, raises IndexError
        MUST have O(1) performance'''
        if not self.is_empty():
            item = self.front.item
            self.front = self.front.next
            self.num_items -= 1
            return item

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity
        MUST have O(1) performance'''
        return self.num_items
