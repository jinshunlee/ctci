# Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

from Stack import Stack

# The minimum element stack is only updated when there is a new element that is smaller, worst case is O(n) space

class MinStack:
    def __init__(self):
        self.itemStack = Stack()
        self.minStack = Stack()
        self.minStack.push(10000000)

    def push(self, item):
        self.itemStack.push(item)
        if item < self.minStack.peek():
            self.minStack.push(item)

    def pop(self):
        if self.itemStack.peek() == self.minStack.peek():
            self.minStack.pop()
        self.itemStack.pop()

    def min(self):
        return self.minStack.peek()


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(5)
    minStack.push(4)
    minStack.push(8)
    minStack.push(1)
    print(minStack.min())
    minStack.pop()
    print(minStack.min())
    minStack.pop()
    print(minStack.min())
    minStack.pop()
    print(minStack.min())
    minStack.pop()
    print(minStack.min())
