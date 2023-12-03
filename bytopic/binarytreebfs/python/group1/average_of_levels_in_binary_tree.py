"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
Answers within 10^{-5} of the actual answer will be accepted.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Note: Visualize the binary tree to understand

Tag: 82/150
Tag: 199/2927, R549/2936 (overall frequency ranking)
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_of_levels(root: Optional[TreeNode]) -> list[float]:
    q = deque([root])
    ans = []
    while q:
        qlen = len(q)
        row = 0
        for i in range(qlen):
            node = q.popleft()
            row += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(row / qlen)
    return ans


def main():
    root = TreeNode(3, TreeNode(9), TreeNode(20))
    root.left.left = TreeNode(15)
    root.left.right = TreeNode(7)
    print(average_of_levels(root))


if __name__ == "__main__":
    main()
