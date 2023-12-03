"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge
connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass
through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
Note: Visualize to understand

Tag: 78/150
Tag: 124/2927, R96/2936 (overall frequency ranking)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_numbers(root: Optional[TreeNode]) -> int:
    ans = [root.val]

    def dfs(root):
        if root is None:
            return 0
        lmax = dfs(root.left)
        rmax = dfs(root.right)
        lmax = 0 if lmax <0 else lmax
        rmax = 0 if rmax < 0 else rmax

        ans[0] = max(ans[0], root.val + lmax + rmax)

        return root.val + max(lmax, rmax)
    dfs(root)
    return ans[0]


def main():
    root = TreeNode(-10, TreeNode(9), TreeNode(20))
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(sum_numbers(root))


if __name__ == "__main__":
    main()
