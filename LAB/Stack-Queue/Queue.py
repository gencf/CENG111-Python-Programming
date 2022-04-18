class Queue:
    def __init__(self):
        self.Queue = []

    def Enqueue(self, item):
        self.Queue.append(item)

    def Dequeue(self):
        return self.Queue.pop(0)

    def Front(self):
        return self.Queue[-1]

    def is_empty(self):
        return self.Queue == []

    def length(self):
        return len(self.Queue)