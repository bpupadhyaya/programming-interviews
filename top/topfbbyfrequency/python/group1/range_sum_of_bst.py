"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes
with a value in the inclusive range [low, high].

Example:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Note: Visualize to understand.

Tag: fb R33/50, 938/2927, R665/2936
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def range_sum_bst(root: Optional[TreeNode], low: int, high: int) -> int:
    if not root:
        return 0
    return range_sum_bst(root.left, low, high) + \
        range_sum_bst(root.right, low, high) + \
        (root.val if low <= root.val <= high else 0)


def main():
    root = TreeNode(10, TreeNode(5), TreeNode(15))
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    low = 7
    high = 15
    print('Range sum from BST: ', range_sum_bst(root, low, high))


if __name__ == "__main__":
    main()


"""
Analysis:
The method (DFS) traverses all nodes in worst case, and if we count in the recursion trace space cost,
the complexities are as follows:
Time: O(n), space: O(h), where n is the number of total nodes, h is the height of the tree.
"""