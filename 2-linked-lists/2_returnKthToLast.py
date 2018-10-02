# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

from LinkedList import LinkedList

# Assumption k = 0 will return the last element

# Time O(n)
# Space O(1)


def returnKthToLast(xs, k):
    cur = xs.head
    if k >= xs.length or k < 0:
        return None
    for _ in range(0, xs.length - k - 1):
        cur = cur.next
    return cur.data

# Time O(n)
# Space O(1)
# without knowing what is the length of the list


def returnKthToLast2(xs, k):
    pt1 = xs.head
    pt2 = xs.head
    if k < 0:
        return None
    for _ in range(0, k + 1):
        if pt1 is None:
            return None
        pt1 = pt1.next
    while pt1 is not None:
        pt1 = pt1.next
        pt2 = pt2.next
    return pt2.data


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
    empty = LinkedList()
    print(returnKthToLast(ys, -1))
    print(returnKthToLast(ys, 0))
    print(returnKthToLast(ys, 1))
    print(returnKthToLast(ys, 4))
    print(returnKthToLast(ys, 5))
    print(returnKthToLast(empty, 0))
    print(returnKthToLast2(ys, -1))
    print(returnKthToLast2(ys, 0))
    print(returnKthToLast2(ys, 1))
    print(returnKthToLast2(ys, 4))
    print(returnKthToLast2(ys, 5))
    print(returnKthToLast2(empty, 0))
