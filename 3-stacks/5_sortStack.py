# Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.

from Stack import Stack

# Time O(n^2)
# Space O(n)


def sortStack(stack):
    temp = Stack()
    while not stack.isEmpty():
        cur = stack.pop()
        if temp.isEmpty() or cur < temp.peek():
            temp.push(cur)
        else:
            while not temp.isEmpty() and cur >= temp.peek():
                stack.push(temp.pop())
            temp.push(cur)
    return temp


if __name__ == "__main__":
    stack = Stack()
    stack.push(7)
    stack.push(6)
    stack.push(2)
    stack.push(1)
    stack.push(5)
    stack.push(4)
    stack.print_stack()
    sortStack(stack).print_stack()
