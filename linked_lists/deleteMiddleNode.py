# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# lnput:the node c from the linked lista->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e- >f

from LinkedList import LinkedList

# Time O(n)
# Space O(n)


def deleteMiddleNode(node):
    node.data = node.next.data
    node.next = node.next.next


if __name__ == "__main__":
    xs = LinkedList()
    xs.add(1)
    xs.add(2)
    xs.add(3)
    xs.add(4)
    xs.add(5)
    x = xs.head.next.next
    deleteMiddleNode(x)
    xs.print_list()
    ys = LinkedList()
    ys.add(1)
    ys.add(2)
    ys.add(3)
    y = ys.head.next
    deleteMiddleNode(y)
    ys.print_list()
