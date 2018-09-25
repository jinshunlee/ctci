class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
        self.length += 1

    def print_list(self):
        lst = []
        cur = self.head
        while cur is not None:
            lst.append(cur.data)
            cur = cur.next
        print(lst)
