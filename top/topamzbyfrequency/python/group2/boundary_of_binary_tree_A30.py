"""
The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from
left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:
- The root node's left child is in the left boundary. If the root does not have a left child, then the left
boundary is empty.
- If a node in the left boundary and has a left child, then the left child is in the left boundary.
- If a node is in the left boundary, has no left child, but has a right child, then the right child is in the
 left boundary.
- The leftmost leaf is not in the left boundary.

The right boundary is similar to the left boundary, except it is the right side of the root's right subtree.
Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a
right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.

Example:
Input: root = [1,null,2,3,4]
Output: [1,3,4,2]
Explanation:
- The left boundary is empty because the root does not have a left child.
- The right boundary follows the path starting from the root's right child 2 -> 4.
  4 is a leaf, so the right boundary is [2].
- The leaves from left to right are [3,4].
Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].

Tag: 545/2927 , R636/2935 , R30/50 (amz)
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def boundary_of_binary_tree(root: Optional[TreeNode]) -> List[int]:
    def left_node(root_, res_):        # pre-order
        if not root_:
            return
        if root_.left:
            res_.append(root_.val)
            left_node(root_.left, res_)
        elif root_.right:
            res_.append(root_.val)
            left_node(root_.right, res_)
        return res_

    def right_node(root_, res_):
        if not root_:
            return
        if root_.right:
            right_node(root_.right, res_)
            res_.append(root_.val)
        elif root_.left:
            right_node(root_.left, res_)
            res_.append(root_.val)
        return res_

    def leaf_node(root_, res_):
        if not root_:
            return
        if not root_.right and not root_.left:
            res_.append(root_.val)
        leaf_node(root_.left, res_)
        leaf_node(root_.right, res_)
        return res_

    if not root:
        return []
    res = [root.val]
    if root.left:
        left_node(root.left, res)
    if root.left or root.right:
        leaf_node(root, res)
    if root.right:
        right_node(root.right, res)
    return res


def main():
    root = TreeNode(1, None, TreeNode(2))
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)

    print(boundary_of_binary_tree(root))


if __name__ == "__main__":
    main()
