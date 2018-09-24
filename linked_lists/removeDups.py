# Remove Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

class Node:
  def __init__(self, value, next):
    self.value = value
    self.next = next

  def toString(self):
    while self:
      print(self.value)
      self = self.next

# Time O(n)
# Space O(n)
def removeDuplicates(xs):
  seen = set()
  cur = xs
  prev = None
  while cur is not None:
    if cur.value in seen:
      prev.next = cur.next
    else:
      seen.add(cur.value)
      prev = cur
    cur = cur.next
  return xs

# Time O(n^2)
# Space O(1)
def removeDuplicatesFollowUp(xs):
  pt1 = xs
  while (pt1.next is not None):
    cur_value = pt1.value
    pt2 = pt1.next
    while(pt2.next is not None):
      if cur_value == pt2.value:
        pt1.next1 = pt1.next.next
      else:
        pt2 = pt2.next
      pt1 = pt1.next
    return xs
      

if __name__ == "__main__":
  xs = Node(1, Node(3, Node(3, Node(1, Node(5, None)))))
  ys = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
  removeDuplicates(xs).toString()
  removeDuplicatesFollowUp(xs).toString()
  removeDuplicates(ys).toString()
  removeDuplicatesFollowUp(ys).toString()