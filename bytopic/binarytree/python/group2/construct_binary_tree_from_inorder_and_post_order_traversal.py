"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder
is the postorder traversal of the same tree, construct and return the binary tree.

Example:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Tag: 73/150
Tag: 106/2927, R1542/2936 (overall frequency ranking)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
    if not inorder or not postorder:
        return None
    root = TreeNode(postorder[-1])
    index = inorder.index(postorder[-1])
    root.left = build_tree(inorder[:index], postorder[:index])
    root.right = build_tree(inorder[index+1:], postorder[index:-1])
    return root


def main():
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    root = build_tree(inorder, postorder)
    print(root.val, root.left.val, root.right.val, root.right.left.val, root.right.right.val)


if __name__ == "__main__":
    main()
