"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer
should be set to NULL.

Initially, all next pointers are set to NULL.

Example:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to
point to its next right node, just like in Figure B. The serialized output is in level order as connected by the
next pointers, with '#' signifying the end of each level.

Constraints:
The number of nodes in the tree is in the range [0, 2^{12} - 1].
-1000 <= Node.val <= 1000

Follow-up:
You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra

R126/145
"""
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect_dfs(root: 'Optional[Node]') -> 'Optional[Node]':
    def dfs(root):
        if root is None or root.left is None:
            return
        root.left.next = root.right
        if root.next is not None:
            root.right.next = root.next.left
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return root


def connect_bfs(root: 'Optional[Node]') -> 'Optional[Node]':
    if root is None:
        return None
    q = deque([root])
    while q:
        size = len(q)
        while size > 0:
            node = q.popleft()
            if size > 1:
                node.next = q[0]
            size -= 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return root


def main():
    root = Node(1, Node(2), Node(3), None)
    root.left.next = root.right
    root.right.next = None
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.next = root.left.right
    root.right.left = Node(6)
    root.left.right.next = root.right.left
    root.right.right = Node(7)
    root.right.left.next = root.right.right

    res = connect_bfs(root)
    print(res.val, res.left.val, res.left.next.val, root.left.left.val, root.left.left.next.val, root.right.left.val,
          root.right.left.next.val)


if __name__ == "__main__":
    main()
