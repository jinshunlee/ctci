# Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

from Stack import Stack


class MyQueue:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    # O(1) time to push   
    def add(self, item):
        self.inStack.push(item)
        
    # O(n) time to remove
    def remove(self):
        if not self.inStack.isEmpty() and self.outStack.isEmpty():
            while not self.inStack.isEmpty():
                self.outStack.push(self.inStack.pop())
        return self.outStack.pop()

    # O(n) time to peek
    def peek(self):
        if not self.inStack.isEmpty() and self.outStack.isEmpty():
            while not self.inStack.isEmpty():
                self.outStack.push(self.inStack.pop())
        return self.outStack.peek()

    def print_myQueue(self):
        self.inStack.print_stack()
        self.outStack.print_stack()


if __name__ == "__main__":
    queue = MyQueue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    queue.add(4)
    queue.add(5)
    queue.add(6)
    print(queue.remove())
    queue.print_myQueue()
    print(queue.remove())
    queue.print_myQueue()