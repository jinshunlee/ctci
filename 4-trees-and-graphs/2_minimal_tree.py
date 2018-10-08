# Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an
# algorithm to create a binary search tree with minimal height.

from TreeNode import TreeNode


def minimalTree(arr):
    return helper(arr, 0, len(arr) - 1)


def helper(arr, start, end):
    if end < start:
        return None
    mid = (end + start) // 2
    node = TreeNode(arr[mid])
    node.left = helper(arr, start, mid - 1)
    node.right = helper(arr, mid + 1, end)
    return node


if __name__ == "__main__":
    tree = minimalTree([1, 2, 3, 4, 5])
    print(tree)
    tree2 = minimalTree([1, 2, 3, 4, 5, 6])
    print(tree2)
    emptyTree = minimalTree([])
    print(emptyTree)
