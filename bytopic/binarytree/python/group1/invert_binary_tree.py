"""
Given the root of a binary tree, invert the tree, and return its root.

Example:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Note: Visualize to understand

Tag: 70/150
Tag: 226/2927, R757/2936 (overall frequency ranking)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:  # Base case
        return root
    invert_tree(root.left)  # Call the left subtree
    invert_tree(root.right)  # Call the right subtree
    # Swap the nodes
    root.left, root.right = root.right, root.left
    return root


def main():
    root = TreeNode(4, TreeNode(2), TreeNode(7))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    res = invert_tree(root)
    print(res.val, res.left.val, res.right.val, res.left.left.val, res.left.right.val,
          res.right.left.val, res.right.right.val)


if __name__ == "__main__":
    main()
