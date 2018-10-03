# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.

from Stack import Stack

# Multi Stack takes 0(1) time for pop, push
# for popAt(), it can take up to 0(n) time due to "rolling over" of stack


class StackOfPlates:
    def __init__(self, stackSize=5):
        self.list = []
        self.list.append(Stack())
        self.stackSize = stackSize

    def pop(self):
        self.list[-1].pop()
        if self.list[-1].isEmpty():
            self.list.pop()

    def push(self, item):
        if self.list[-1].size() == self.stackSize:
            self.list.append(Stack())
        self.list[-1].push(item)

    def print_stackOfPlates(self):
        for stack in self.list:
            stack.print_stack()

    def popAt(self, index):
        if index < len(self.list):
            self.list[index].pop()
            for i in range(index + 1, len(self.list)):
                if not self.list[i].isEmpty():
                    elem = self.list[i].stack.pop(0)
                    self.list[i - 1].push(elem)


if __name__ == "__main__":
    stack = StackOfPlates()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.pop()
    stack.pop()
    stack.push(8)
    stack.push(9)
    stack.push(10)
    stack.push(11)
    stack.push(12)
    stack.push(13)
    stack.push(14)
    stack.push(15)
    stack.push(16)
    stack.push(17)
    stack.push(18)
    stack.push(19)
    stack.popAt(0)
    stack.print_stackOfPlates()
