"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any
two different nodes in the tree.

Sample 1:
Input: root = [4,2,6,1,3]
Output: 1

Tag: 86/150
Tag: 530/2927, R1302/2936 (overall frequency ranking)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_minimum_difference(root: Optional[TreeNode]) -> int:
    cur, stack, min_diff, prev = root, [], 10**5, -10**5

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        node = stack.pop()
        min_diff = min(min_diff, node.val - prev)
        prev = node.val
        cur = node.right

    return min_diff


def main():
    root = TreeNode(4, TreeNode(2), TreeNode(6))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print(get_minimum_difference(root))


if __name__ == "__main__":
    main()
