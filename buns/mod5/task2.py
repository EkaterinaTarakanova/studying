class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def pop(self):
        if self.start is None:
            raise Exception("Queue is empty")
        val = self.start.data
        if self.start is self.end:
            self.start = self.end = None
        else:
            self.start = self.start.nref
        return val

    def push(self, val):
        new_node = Node(val)
        if self.start is None:
            self.start = self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        new_node = Node(val)
        if self.start is None:
            self.start = self.end = new_node
            return
        current = self.start
        while current is not None and n > 0:
            current = current.nref
            n -= 1

        if current is None:
            self.end.nref = new_node
            new_node.pref = self.end
            self.end = new_node
        else:
            prev_node = current.pref
            new_node.nref = current
            new_node.pref = prev_node
            current.pref = new_node
            prev_node.nref = new_node

    def print(self):
        current = self.start
        while current is not None:
            print(current.data)
            current = current.nref
