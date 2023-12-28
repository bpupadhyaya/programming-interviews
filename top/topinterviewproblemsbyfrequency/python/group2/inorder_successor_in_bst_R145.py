"""
Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST.
If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

Example:
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Note: Visualize to understand

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5
All Nodes will have unique values.

R145/145
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder_successor(root: TreeNode, p: TreeNode) -> TreeNode:
    # Approach: Recursion
    # Logic: In an iorder traversal, successor is always the very next element
    # Complexity: time: O(n), space: O(n)
    def helper(node):
        nonlocal res
        if not node or res:
            return
        helper(node.left)
        if node.val > p.val and not res:
            res = node
            return
        helper(node.right)
    res = None
    helper(root)
    return res


def inorder_successor_1(root: TreeNode, p: TreeNode) -> TreeNode:
    # Complexity: time: O(n), space: O(1)
    successor = None
    node = root
    while node:
        if node.val > p.val:
            successor = node
            node = node.left
        else:
            node = node.right
    return successor


def main():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    p = root.left
    res = inorder_successor_1(root, p)
    print(res.val)


if __name__ == "__main__":
    main()
