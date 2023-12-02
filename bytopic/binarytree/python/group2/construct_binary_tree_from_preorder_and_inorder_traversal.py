"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and
inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Tag: 72/150
Tag: 101/2927, R485/2936 (overall frequency ranking)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    index = inorder.index(preorder[0])
    root.left = build_tree(preorder[1:index+1], inorder[:index])
    root.right = build_tree(preorder[index+1:], inorder[index+1:])
    return root


def main():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = build_tree(preorder, inorder)
    print(root.val, root.left.val, root.right.val, root.right.left.val, root.right.right.val)


if __name__ == "__main__":
    main()
