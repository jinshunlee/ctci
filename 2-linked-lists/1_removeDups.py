# Remove Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

from LinkedList import LinkedList

# Time O(n)
# Space O(n)


def removeDuplicates(xs):
    seen = set()
    cur = xs.head
    prev = None
    while cur is not None:
        if cur.data in seen:
            prev.next = cur.next
        else:
            seen.add(cur.data)
            prev = cur
        cur = cur.next
    return xs

# Time O(n^2)
# Space O(1)


def removeDuplicatesFollowUp(xs):
    pt1 = xs.head
    while (pt1.next is not None):
        cur_value = pt1.data
        pt2 = pt1.next
        while(pt2.next is not None):
            if cur_value == pt2.data:
                pt1.next1 = pt1.next.next
            else:
                pt2 = pt2.next
            pt1 = pt1.next
        return xs


if __name__ == "__main__":
    xs = LinkedList()
    xs.add(1)
    xs.add(3)
    xs.add(3)
    xs.add(1)
    xs.add(5)
    ys = LinkedList()
    ys.add(1)
    ys.add(2)
    ys.add(3)
    ys.add(4)
    ys.add(5)
    removeDuplicates(xs).print_list()
    removeDuplicates(ys).print_list()
    removeDuplicatesFollowUp(xs).print_list()
    removeDuplicatesFollowUp(ys).print_list()
