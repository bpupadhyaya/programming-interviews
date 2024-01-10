"""
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are
 also given an integer startValue representing the value of the start node s, and a different integer destValue
  representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path
 as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

Example 1:
Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Note: Visualize to understand

Constraints:
The number of nodes in the tree is n.
2 <= n <= 10^5
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue

Note: debug and find out why output is not printing for get_directions, fix error for get_directions1

Tag: G19/50
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_directions(root: TreeNode, start_value: int, dest_value: int) -> str:
    def find(n: TreeNode, val: int, path: list[str]) -> bool:
        if n.val == val:
            return True
        if n.left and find(n.left, val, path):
            path += "L"
        elif n.right and find(n.right, val, path):
            path += "R"
        return path
    s, d = [], []
    find(root, start_value, s)
    find(root, dest_value, d)
    while len(s) and len(d) and s[-1] == d[-1]:
        s.pop()
        d.pop()
    return "".join("U" * len(s)) + "".join(reversed(d))


def get_directions1(root: TreeNode, start_value: int, dest_value: int) -> str:
    def lca(node):
        """Return lowest common ancestor of start and dest nodes."""
        if not node or node.val in (start_value, dest_value):
            return node
        left, right = lca(node.left), lca(node.right)
        return node if left and right else left or right

    root = lca(root)  # only this sub-tree matters

    ps = pd = ""
    stack = [(root, "")]
    while stack:
        node, path = stack.pop()
        if node.val == start_value:
            ps = path
        if node.val == dest_value:
            pd = path
        if node.left:
            stack.append((node.left, path + "L"))
        if node.right:
            stack.append((node.right, path + "R"))
    return "U"*len(ps) + pd


def main():
    root1 = [5, 1, 2, 3, None, 6, 4]
    root = TreeNode(5, TreeNode(1), TreeNode(2))
    root.left.right = None
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(4)
    # start_value = root.left.left
    # dest_value = root.right.left
    print(get_directions1(root, root.left.left, root.right.left))


if __name__ == "__main__":
    main()
