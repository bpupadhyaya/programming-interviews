"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes
 with a value greater than X.
Return the number of good nodes in the binary tree.

Example:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Constraints:
The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].


Tag: M49/50
"""
from collections import deque
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def good_nodes(root: TreeNode) -> int:
    def solve(root_, val):
        if root_:
            k = solve(root_.left, max(val, root_.val)) + solve(root_.right, max(val, root_.val))
            if root_.val >= val:
                k += 1
            return k
        return 0
    return solve(root, root.val)


def good_nodes1(root: TreeNode) -> int:
    ans = 0
    q = deque()

    q.append((root, -inf))
    """ perform bfs  with track of max_val till perant node """

    while q:
        node, max_val = q.popleft()
        """ if curr node has max or eqvalue till current max """
        if node.val >= max_val:
            ans += 1

        if node.left:    # new max update
            q.append((node.left, max(max_val, node.val)))

        if node.right:
            q.append((node.right, max(max_val, node.val)))

    return ans


def main():
    root = TreeNode(3, TreeNode(1), TreeNode(4))
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)

    print(good_nodes1(root))


if __name__ == "__main__":
    main()
