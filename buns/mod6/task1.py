class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def get(self, index):
        if index < 0:
            return None
        current = self.head
        for i in range(index):
            if not current:
                return None
            current = current.next
        return current.data

    def remove(self, index):
        if index < 0:
            return
        if index == 0:
            if self.head:
                self.head = self.head.next
            return
        current = self.head
        for i in range(index - 1):
            if not current:
                return
            current = current.next
        if current and current.next:
            current.next = current.next.next

    def insert(self, n, val):
        if n < 0:
            return
        if n == 0:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(n - 1):
            if not current:
                return
            current = current.next
        if current:
            new_node = Node(val)
            new_node.next = current.next
            current.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
