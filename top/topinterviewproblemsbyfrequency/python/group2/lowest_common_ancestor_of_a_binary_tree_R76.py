"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as
the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Sample 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Sample 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Note: Visualize to understand. The difference with binary search tree is that binary tree is not sorted, so the
elements on the left are not necessarily less than elements on the right.
Note: program has bug, fix to get correct output.

Tag: R76/145
Tag: 81/150
Tag: 236/2927, R237/2936 (overall frequency ranking), fb R14/50
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
        return root

    lft = lowest_common_ancestor(root.left, p, q)
    rht = lowest_common_ancestor(root.right, p, q)

    if lft and rht:
        return root
    return lft or rht


def main():
    root = TreeNode(3, TreeNode(5), TreeNode(1))
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    res = lowest_common_ancestor(root, root.left, root.right)
    print(res.val)


if __name__ == "__main__":
    main()
