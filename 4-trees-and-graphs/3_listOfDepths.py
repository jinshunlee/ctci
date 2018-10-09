# List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

from TreeNode import TreeNode
from LinkedList import LinkedList

# Time O(n)
# Space O(n)

def listOfDepths(tree):
    return helper(tree, [], 0)


def helper(root, lists, level):
    if not root:
        return

    if level == len(lists):
        ll = LinkedList()
        ll.add(root.data)
        lists.append(ll)
    else:
        lists[level].add(root.data)

    helper(root.left, lists, level + 1)
    helper(root.right, lists, level + 1)

    return lists


if __name__ == "__main__":
    lists = listOfDepths(TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(2)))
    for ll in lists:
        ll.print_list()
