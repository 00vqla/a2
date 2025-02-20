class Stack:
    def __init__(self):
        self.items = []

    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


s = Stack()
s.push(100)
s.push(50)

s.push("+")

while not s.is_empty():
    print(s.pop())


