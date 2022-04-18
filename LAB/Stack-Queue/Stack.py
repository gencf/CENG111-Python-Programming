class Stack:
    def __init__(self):
        self.Stack = []

    def push(self, item):
        self.Stack.append(item)

    def pop(self):
        return self.Stack.pop()

    def top(self):
        return self.Stack[-1]

    def is_empty(self):
        return self.Stack == []

    def length(self):
        return len(self.Stack)