# Palindrome: Implement a function to check if a linked list is a palindrome.

from LinkedList import LinkedList

# Time O(n)
# Space O(1)


def palindrome(xs):
    slow = xs.head
    fast = xs.head

    # move slow to the second half of the list
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse second half of list
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    slow = prev
    cur = xs.head

    # compare first half to second half (reversed) of list to check if palindrome
    while slow:
        if slow.data != cur.data:
            return False
        slow = slow.next
        cur = cur.next
    return True


if __name__ == "__main__":
    xs = LinkedList()
    xs.add(1)
    xs.add(2)
    xs.add(3)
    xs.add(4)
    xs.add(5)
    ys = LinkedList()
    ys.add(1)
    ys.add(2)
    ys.add(3)
    ys.add(2)
    ys.add(1)
    zs = LinkedList()
    zs.add(1)
    zs.add(2)
    zs.add(2)
    zs.add(1)
    empty = LinkedList()
    one = LinkedList()
    one.add(1)
    print(palindrome(xs))
    print(palindrome(ys))
    print(palindrome(zs))
    print(palindrome(empty))
    print(palindrome(one))
