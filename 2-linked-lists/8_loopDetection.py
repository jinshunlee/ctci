# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.

from LinkedList import LinkedList

# Time O(n)
# Space O(1)


def loopDetection(xs):  # returns the node where the slow and fast pointer meets
    slow = xs.head
    fast = xs.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return fast
    return None


# Time O(n)
# Space O(1)

def getStartOfLoop(xs):  # returns the node at the begining of the loop
    node = loopDetection(xs)
    cur = xs.head
    while cur != node:
        cur = cur.next
        node = node.next
    return node


if __name__ == "__main__":
    xs = LinkedList()
    xs.add(1)
    xs.add(2)
    xs.add(3)
    xs.add(4)
    xs.add(5)
    last_node = xs.head.next.next.next.next
    third_node = xs.head.next.next
    last_node.next = third_node
    print(getStartOfLoop(xs).data)
