"""
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the
target. If there are multiple answers, print the smallest.

Example:
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4

Note: Visualize to understand

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
0 <= Node.val <= 10^9
-10^9 <= target <= 10^9

Tag: F46/50
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def closest_value(root: TreeNode, target: float) -> int:
    nearest = float("inf")
    while root:
        if root.val == target:
            return root.val
        if abs(root.val-target) < abs(nearest - target):
            nearest = root.val
        if abs(root.val-target) == abs(nearest - target):
            nearest = min(root.val, nearest)

        if root.val > target:
            root = root.left
        else:
            root = root.right

    return nearest


def main():
    root = TreeNode(4, TreeNode(2), TreeNode(5))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    target = 3.714286
    print(closest_value(root, target))


if __name__ == "__main__":
    main()
