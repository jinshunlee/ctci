# Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
# this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one.

from TreeNode import TreeNode


def height(tree):
    if not tree:
        return 0
    tree.height = 1 + max((height(tree.left), height(tree.right)))
    return tree.height

# Time O(N)
# Space O(N)


def checkBalanced(tree):
    height(tree)
    return helper(tree)


def helper(tree):
    if not tree:
        return True
    leftHeight = tree.left.height if tree.left else 0
    rightHeight = tree.right.height if tree.right else 0
    return abs(leftHeight - rightHeight) <= 1 and checkBalanced(tree.left) and checkBalanced(tree.right)


if __name__ == "__main__":
    tree = TreeNode(1, TreeNode(2, TreeNode(3)))
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(checkBalanced(tree))
    print(checkBalanced(tree2))
 
