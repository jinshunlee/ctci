# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.

from LinkedList import LinkedList

# Time O(n)
# Space O(n)

def sumLists(xs, ys):
    pt_x = xs.head
    pt_y = ys.head
    zs = LinkedList()
    additional = 0

    while pt_x or pt_y :
        x = pt_x.data if pt_x else 0
        y = pt_y.data if pt_y else 0 
        zs.add((x + y + additional) % 10)
        additional = (x + y + additional) / 10
        if pt_x:
            pt_x = pt_x.next
        if pt_y:
            pt_y = pt_y.next
    if additional == 1:
        zs.add(1)
    return zs

if __name__ == "__main__":
    xs = LinkedList()
    xs.add(9)
    xs.add(9)
    xs.add(9)
    ys = LinkedList()
    ys.add(5)
    ls = LinkedList()
    ls.add(7)
    ls.add(1)
    ls.add(6)
    ks = LinkedList()
    ks.add(5)
    ks.add(9)
    ks.add(2)
    empty = LinkedList()
    sumLists(xs, ys).print_list()
    sumLists(empty, ys).print_list()
    sumLists(ls, ks).print_list()