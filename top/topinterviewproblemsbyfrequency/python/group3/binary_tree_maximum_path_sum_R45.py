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

Constraints:
The number of nodes in the tree is in the range [1, 3 * 10^4].
-1000 <= Node.val <= 1000

Tag: R45/145
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: TreeNode) -> int:
    max_sum = float('-inf')

    def traverse(root_):
        nonlocal max_sum
        if root_:
            left = traverse(root_.left)
            right = traverse(root_.right)
            max_sum = max(max_sum, root_.val, root_.val + left, root_.val + right, root_.val + left + right)
            return max(root_.val, root_.val + left, root_.val + right)
        else:
            return 0
    traverse(root)
    return max_sum


def main():
    root = TreeNode(-10, TreeNode(9), TreeNode(20))
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(max_path_sum(root))


if __name__ == "__main__":
    main()
