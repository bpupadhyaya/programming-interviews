"""
Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the
last level h.
Design an algorithm that runs in less than O(n) time complexity.

Example:
Input: root = [1,2,3,4,5,6]
Output: 6

Tag: 80/150
Tag: 222/2927, R1538/2936 (overall frequency ranking)
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_nodes(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    def depth_left(node):
        d = 0
        while node:
            d += 1
            node = node.left
        return d

    def depth_right(node):
        d = 0
        while node:
            d += 1
            node = node.right
        return d
    ld = depth_left(root.left)
    rd = depth_right(root.right)
    if ld == rd:
        return 2 ** (ld + 1) - 1
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)


def count_nodes_using_walrus_operator(root: Optional[TreeNode]) -> int:
    # Note: see how concise the solution is
    q, cnt = deque([root]), 0
    while node := q.popleft():
        cnt += 1
        q.extend([node.left, node.right])
    return cnt


def main():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    print(count_nodes_using_walrus_operator(root))


if __name__ == "__main__":
    main()

