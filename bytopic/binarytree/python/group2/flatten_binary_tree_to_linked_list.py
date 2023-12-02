"""
Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class where the right child pointer points to the next
node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Sample 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Note: Visualize to understand, note that the binary tree is sorted by nature.

Tag: 75/150
Tag: 114/2927, R646/2936 (overall frequency ranking)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.cur = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node):
            if not node:
                return
            left, right = node.left, node.right
            node.left = None
            if self.cur:
                self.cur.right = node
                self.cur = self.cur.right
            else:
                self.cur = node
            dfs(left)
            dfs(right)

        dfs(root)


def main():
    root = TreeNode(1, TreeNode(2), TreeNode(5))
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)

    sol = Solution()
    sol.flatten(root)
    while root is not None:
        print(root.val, end=", ")
        root = root.right


if __name__ == "__main__":
    main()

