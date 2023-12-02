"""
Given a binary tree

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
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to
its next right node, just like in Figure B. The serialized output is in level order as connected by the
next pointers, with '#' signifying the end of each level.
Note: Visualize to understand (the element horizontally right is the next pointer in visualization, # is null)

Tag: 74/150
Tag: 117/2927, R1731/2936 (overall frequency ranking)
Note: Might need to analyze this implementation: without adding next as a part of input preparation
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Node') -> 'Node':
    if not root:
        return None
    dummy = Node(-999)
    head = root

    while head:
        curr = head
        prev = dummy
        while curr:
            if curr.left:
                prev.next = curr.left
                prev = prev.next
            if curr.right:
                prev.next = curr.right
                prev = prev.next
            curr = curr.next
        head = dummy.next
        dummy.next = None
    return root


def main():
    input_root = Node(1, Node(2), Node(3))
    input_root.left.left = Node(4)
    input_root.left.right = Node(5)
    input_root.right = Node(3)
    input_root.right.right = Node(7)

    input_root.next = None
    input_root.left.next = input_root.right
    input_root.left.left.next = input_root.left.right
    input_root.left.right.next = input_root.right.right
    input_root.right.next = None
    input_root.right.right.next = None

    root = connect(input_root)
    print(root.val, root.next is None, root.left.val, root.left.next.val, root.right.next is None,
          root.left.left.val, root.left.left.next.val, root.left.right.next.val, root.right.right.next is None)


if __name__ == "__main__":
    main()
