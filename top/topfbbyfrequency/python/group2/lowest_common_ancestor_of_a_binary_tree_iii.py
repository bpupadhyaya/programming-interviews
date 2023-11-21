"""
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is
the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

Example:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Note: visualize to understand

Tag: fb R22/50, 1650/2927, R396/2936
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def lowest_common_ancestor(p: 'Node', q: 'Node') -> Node:
    path = set()
    while p:
        path.add(p)
        p = p.parent
    while q not in path:
        q = q.parent

    return q


def main():
    root = Node(3)
    root.left, root.right = Node(5), Node(1)
    root.left.parent, root.right.parent = root, root
    root.left.left, root.left.right = Node(6), Node(2)
    root.left.left.parent, root.left.right.parent = root.left, root.left
    root.left.right.left, root.left.right.right = Node(7), Node(4)
    root.left.right.left.parent, root.left.right.right.parent = root.left.right, root.left.right
    root.left.left.left, root.left.left.right = None, None
    root.right.left, root.right.right = Node(0), Node(8)
    root.right.left.parent, root.right.right.parent = root.right, root.right

    lca = lowest_common_ancestor(root.left, root.right)
    print(lca.val)


if __name__ == "__main__":
    main()
