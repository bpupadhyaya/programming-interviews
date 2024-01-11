"""
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were
swapped by mistake. Recover the tree without changing its structure.

Example:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Constraints:
The number of nodes in the tree is in the range [2, 1000].
-2^{31} <= Node.val <= 2^{31} - 1
Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?

Tag: M31/50
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recover_tree(root: TreeNode) -> None:
    res = []
    start_node = None
    prev = None
    last_node = None

    def dfs(root):
        nonlocal res, start_node, prev, last_node
        if not root:
            return
            # go to left  (inorder step 1)
        dfs(root.left)

        # do processing....(inorder step 2)
        # get the first node where the sorted order is broken the first time and the last time
        if prev and prev.val > root.val:
            if not start_node:
                start_node = prev
            last_node = root

        prev = root

        # go to right (inorder step 3)
        dfs(root.right)

    dfs(root)
    # swap the nodes that are not in place
    if start_node and last_node:
        start_node.val, last_node.val = last_node.val, start_node.val


def main():
    root = TreeNode(1, TreeNode(3), None)
    root.left.right = TreeNode(2)
    recover_tree(root)
    print(root.val, root.left.val, root.left.right.val)


if __name__ == "__main__":
    main()

