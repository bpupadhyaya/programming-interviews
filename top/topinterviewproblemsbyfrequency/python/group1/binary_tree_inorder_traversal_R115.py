"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: root = [1,null,2,3]
Output: [1,3,2]
Note: Visualize to understand

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 Follow up: Recursive solution is trivial, could you do it iteratively?

R115/145
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode) -> list[int]:
    result = []

    def inorder(root):
        nonlocal result
        if not root:
            return []
        inorder(root.left)
        result.append(root.val)
        inorder(root.right)

    inorder(root)
    return result


def preorder_traversal(root):
    result = []

    def preorder(root):
        nonlocal result
        if not root:
            return []
        result.append(root.val)
        preorder(root.left)
        preorder(root.right)

    preorder(root)
    return result


def postorder_traversal(root):
    result = []

    def postorder(root):
        nonlocal result
        if not root:
            return []
        postorder(root.left)
        postorder(root.right)
        result.append(root.val)

    postorder(root)
    return result


def main():
    root = TreeNode(1, None, TreeNode(2))
    root.right.left = TreeNode(3)
    root.right.right = None

    print(inorder_traversal(root))


if __name__ == "__main__":
    main()
