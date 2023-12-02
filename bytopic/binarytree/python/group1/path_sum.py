"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path
such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Sample 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum has leaf node 2.
Note: visualize to understand

Tag: 76/150
Tag: 112/2927, R966/2936 (overall frequency ranking)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return target_sum == root.val
    left_sum = has_path_sum(root.left, target_sum - root.val)
    right_sum = has_path_sum(root.right, target_sum - root.val)
    return left_sum or right_sum


def main():
    root = TreeNode(5, TreeNode(4), TreeNode(8))
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    target_sum = 22
    print(has_path_sum(root, target_sum))


if __name__ == "__main__":
    main()
