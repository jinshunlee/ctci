# Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
# binary search tree. You may assume that each node has a link to its parent.

from TreeNode import TreeNode

# Time O(lg N)
# Space O(lg N)


def successor(root, node):
    # Find left most node of node's right subtree
    if node.right:
        temp = node.right
        while temp.left:
            temp = temp.left
        return temp
    # Go to 1st parent that is greater than node
    else:
        cur = root
        firstLargerParent = None
        while cur and cur.data != node.data:
            if node.data < cur.data:
                firstLargerParent = cur
                cur = cur.left
            else:
                cur = cur.right
        return firstLargerParent


if __name__ == "__main__":
    two = TreeNode(2)
    six = TreeNode(6)
    eight = TreeNode(8)
    seven = TreeNode(7, six, eight)
    fifteen = TreeNode(15)
    tree = TreeNode(10, TreeNode(5, TreeNode(3, two), seven), fifteen)
    print(successor(tree, two).data)
    print(successor(tree, six).data)
    print(successor(tree, seven).data)
    print(successor(tree, eight).data)
    print(successor(tree, fifteen))