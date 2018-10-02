# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.

from LinkedList import LinkedList

# Time O(n)
# Space O(1)

def partition(xs, x):
    smaller = None
    smallerHead = None
    prev = None
    cur = xs.head
    while cur is not None:
        if cur.data < x:
            # add cur node to smaller list
            if smaller is None:
                smaller = cur
                smallerHead = cur
            else:
                smaller.next = cur
                smaller = smaller.next

            # remove node from remainder list
            if prev is None:
                xs.head = cur.next
            else:
                prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    # add smaller list to remainder of cur
    if smaller is not None:
        smaller.next = xs.head
        xs.head = smallerHead
    return xs


if __name__ == "__main__":
    xs = LinkedList()
    xs.add(5)
    xs.add(4)
    xs.add(3)
    xs.add(2)
    xs.add(1)
    ys = LinkedList()
    ys.add(1)
    ys.add(2)
    ys.add(3)
    ys.add(4)
    ys.add(5)
    empty = LinkedList()
    partition(xs, 2).print_list()
    partition(ys, 3).print_list()
    partition(ys, 0).print_list()
    partition(empty, 4).print_list()
