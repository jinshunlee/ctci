class Stack:
    def __init__(self):
        self.stack = []

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        item = self.stack[-1]
        self.stack = self.stack[:-1]
        return item

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return self.stack.size() == 0

    def print_stack(self):
        print(self.stack)
