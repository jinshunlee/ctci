# Validate BST: Implement a function to check if a binary tree is a binary search tree.

from TreeNode import TreeNode


# Time O(N)
# Space O(N)


def validateBST(tree):
    return helper(tree, -9999999, 99999999)


def helper(tree, min_value, max_value):
    if not tree:
        return True
    return min_value <= tree.data <= max_value \
    and helper(tree.left, min_value, tree.data) \
    and helper(tree.right, tree.data, max_value)


if __name__ == "__main__":
    tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(6, TreeNode(5), TreeNode(7)))
    tree2 = TreeNode(3, TreeNode(2, TreeNode(1), TreeNode(4)), TreeNode(5))
    print(tree)
    print(validateBST(tree))
    print(validateBST(tree2))
