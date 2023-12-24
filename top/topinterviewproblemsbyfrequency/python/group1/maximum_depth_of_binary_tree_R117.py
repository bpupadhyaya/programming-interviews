"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the
farthest leaf node.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: 3
Note: Visualize to understand

Tag: R117/145
Tag: 68/150
Tag: 104/2927, R670/2936 (overall frequency ranking)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    def dfs(root, depth):
        if not root:
            return depth
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
    return dfs(root, 0)


def main():
    # root = [3,9,20,null,null,15,7]
    root = TreeNode(3, TreeNode(9), TreeNode(20))
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(max_depth(root))


if __name__ == "__main__":
    main()
