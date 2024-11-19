class Node:
    '''Node for use with doubly-linked list'''

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class OrderedList:
    """A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of
    list)"""

    def __init__(self):
        self.head: Node = Node(None)
        self.head.next = self.head  # dummy node next
        self.head.prev = self.head  # dummy node prev
    """Use ONE dummy node as described in class  
               ***No other attributes***  
               DO NOT have an attribute to keep track of size"""

    def is_empty(self):
        """Returns True if OrderedList is empty
        MUST have O(1) performance"""
        return self.head.next == self.head

    def add(self, item):
        """Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False."""
        if self.search(item):
            return False

        new = Node(item)
        if self.is_empty():
            new.next = self.head
            new.prev = self.head
            self.head.next = new
            self.head.prev = new
        else:
            curr = self.head.next
            while curr is not self.head:
                if curr.item > item:
                    new.next = curr
                    new.prev = curr.prev
                    curr.prev.next = new
                    curr.prev = new
                    return True
                else:
                    curr = curr.next

            # If the item is greater than all values in the list
            if curr == self.head:
                curr = curr.prev
                new.prev = curr
                new.next = self.head
                curr.next = new
                self.head.prev = new

            return True

        '''Adds an item to OrderedList, in the proper location based on ordering of items
               from lowest (at head of list) to highest (at tail of list) and returns True.
               If the item is already in the list, do not add it again and return False.
               MUST have O(n) average-case performance'''

    def remove(self, item):
        node = self.search_help(self.head.next, item)  # current node
        if node is None:
            return False
        node.next.prev = node.prev
        node.prev.next = node.next
        return True

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of
        list is index 0).
        If item is not in list, return None
        MUST have O(n) average-case performance'''
        return self.index_help(item, self.head.next, 0)

    def index_help(self, item, node, index):
        if node != self.head:
            if node.item == item:
                return index
            else:
                return self.index_help(item, node.next, index + 1)
        return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
               If index is negative or >= size of list, raises IndexError
               MUST have O(n) average-case performance'''
        if index < 0 or index > self.size():
            raise IndexError
        node = self.head.next
        for n in range(index):
            node = node.next
        item = node
        self.remove(node.item)
        return item.item

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
               To practice recursion, this method must call a RECURSIVE method that
               will search the list
               MUST have O(n) average-case performance'''
        if self.search_help(self.head.next, item) is not None:
            return True

    def search_help(self, node, item):
        """Search helper, recursively searches down Node linked list until either sentinel is reached,
        or item is found. Returns the Node if found or False if not"""

        if node != self.head:
            if node.item == item:
                return node

            return self.search_help(node.next, item)

        return None

    def python_list(self):
        """Return a Python list representation of OrderedList, from head to tail
               For example, list with integers 1, 2, and 3 would return [1, 2, 3]
               MUST have O(n) performance"""
        list1 = []
        node = self.head.next
        while node != self.head:
            list1.append(node.item)
            node = node.next
        return list1

    def python_list_reversed(self):
        """Return a Python list representation of OrderedList, from tail to head, using
    recursion

        For example, list with integers 1, 2, and 3 would return [3, 2, 1]
               To practice recursion, this method must call a RECURSIVE method that
               will return a reversed list
               MUST have O(n) performance"""
        return self.list_help(self.head.prev, [])

    def list_help(self, node: Node, list1):
        if node != self.head:
            list1.append(node.item)
            return self.list_help(node.prev, list1)
        return list1

    def size(self):
        """Returns number of items in the OrderedList
               To practice recursion, this method must call a RECURSIVE method that
               will count and return the number of items in the list
               MUST have O(n) performance"""
        return self.size_help(self.head.next)

    def size_help(self, node: Node) -> int:
        if node != self.head:
            size1 = 1 + self.size_help(node.next)
            return size1
        return 0