"""
Given the root of a binary tree, collect a tree's nodes as if you were doing this:
Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.

Example:
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not
matter the order on which elements are returned.

Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100

Tag: G24/50
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_leaves(root: TreeNode) -> list[list[int]]:
    res = []

    def recurse(node):
        if not node:
            return None
        if not(node.left or node.right):
            res[-1].append(node.val)
            return None
        node.left = recurse(node.left)
        node.right = recurse(node.right)
        return node
    while root:
        res.append([])
        root = recurse(root)
    return res


def main():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(find_leaves(root))


if __name__ == "__main__":
    main()
