'''Stack Class: data, push(), pop(), top(), size(), is_empty()'''


class Stack:
    def __init__(self):
        self.data = []  # initialize with an empty list

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0  # True if empty, False otherwise

    def push(self, a):
        self.data.append(a)

    def pop(self):
        if self.is_empty():
            return "error"
        return self.data.pop()

    def top(self):
        if self.is_empty():
            return "error"
        return self.data[-1]


a = Stack()
