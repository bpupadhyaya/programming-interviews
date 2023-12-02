"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
Note: Visualize to understand

Tag: 71/150
Tag: 101/2927, R485/2936 (overall frequency ranking)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Check if the left subtree is the mirror image or the right subtree
def is_same(left_root, right_root):
    if left_root is None and right_root is None:
        return True
    if left_root is None or right_root is None:
        return False
    if left_root.val != right_root.val:
        return False
    return is_same(left_root.left, right_root.right) and is_same(left_root.right, right_root.left)


def is_symmetric(root: Optional[TreeNode]) -> bool:
    # Base case
    if not root:
        return True
    # Return the function recursively
    return is_same(root.left, root.right)


def main():
    root = TreeNode(1, TreeNode(2), TreeNode(2))
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(is_symmetric(root))


if __name__ == "__main__":
    main()
