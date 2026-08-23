
class Stack:
    def __init__(self):
        self.count = 0
        self.stack = []

    def add(self, val):
        self.stack.append(val)

    def is_empty(self):
        if self.stack:
            return False
        else:
            return True

    def peek(self):
        print(self.stack[-1])

    def pop(self):
        self.stack.pop()

    def display(self):
        print(self.stack)


stack = Stack()
stack.display()

stack.add(1)
stack.add(2)
stack.add(3)
stack.display()

stack.peek()
print(stack.is_empty())

stack.pop()
stack.display()