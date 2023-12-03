"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Tag: 88/150
Tag: 98/2927, R393/2936 (overall frequency ranking)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    prev = float('-inf')

    def inorder(node):
        nonlocal prev
        if not node:
            return True
        if not (inorder(node.left) and prev < node.val):
            return False
        prev = node.val
        return inorder(node.right)
    return inorder(root)


def main():
    root = TreeNode(5, TreeNode(1), TreeNode(4))
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print(is_valid_bst(root))


if __name__ == "__main__":
    main()
