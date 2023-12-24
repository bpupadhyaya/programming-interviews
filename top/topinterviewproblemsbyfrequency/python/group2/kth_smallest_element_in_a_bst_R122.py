"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the
values of the nodes in the tree.

Example:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Tag: R122/145
Tag: 87/150
Tag: 230/2927, R731/2936 (overall frequency ranking)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    stack = []
    current = root
    while True:
        while current is not None:
            stack.append(current)
            current = current.left
        if not stack:
            break
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        current = node.right


def main():
    root = TreeNode(3, TreeNode(1), TreeNode(4))
    root.left.right = TreeNode(2)
    k = 1
    print(kth_smallest(root, k))


if __name__ == "__main__":
    main()

