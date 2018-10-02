# Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
# node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.


from LinkedList import LinkedList

# Time O(n)
# Space O(1)


def intersection(xs, ys):

    longer = xs.head if xs.length >= ys.length else ys.head
    shorter = ys.head if xs.length >= ys.length else xs.head

    # shift longer list to same length as shorter list
    for _ in range(0, abs(xs.length - ys.length)):
        longer = longer.next

    while shorter:
        if longer == shorter:
            return longer
        longer = longer.next
        shorter = shorter.next
    return None


if __name__ == "__main__":
    xs = LinkedList()
    xs.add(1)
    xs.add(2)
    xs.add(3)
    xs.add(4)
    xs.add(5)
    ys = LinkedList()
    ys.head = xs.head.next.next
    ys.length = 3
    print(intersection(xs, ys).data)
    lst = LinkedList()
    lst.add(1)
    lst.add(2)
    lst.add(3)
    lst2 = LinkedList()
    lst2.head = lst.head.next
    lst2.length = 2
    print(intersection(lst, lst2).data)
    lst3 = LinkedList()
    lst3.add(9)
    lst3.add(4)
    print(intersection(lst, lst3))