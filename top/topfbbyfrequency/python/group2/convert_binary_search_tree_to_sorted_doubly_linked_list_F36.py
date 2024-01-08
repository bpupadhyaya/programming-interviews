"""
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a
doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element,
and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should
point to its predecessor, and the right pointer should point to its successor. You should return the pointer
 to the smallest element of the linked list.

Example:
Input: root = [4,2,5,1,3]
Output: [1,2,3,4,5]

Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship,
while the dashed line means the predecessor relationship.

Tag: fb R36/50, 426/2927, R746/2936
"""


from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_doubly_list(root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
        return
    sentinel = Node(0)

    def dfs(node, pred):
        if not node.left and not node.right:
            pred.right = node
            node.left = pred
            pred = pred.right
            return pred

        if node.left:
            pred = dfs(node.left, pred)

        pred.right = node
        node.left = pred
        pred = node

        if node.right:
            pred = dfs(node.right, pred)

        return pred

    last_value = dfs(root, sentinel)

    head = sentinel.right
    last_value.right = head
    head.left = last_value

    return head


def main():
    root = Node(4, Node(2), Node(5))
    root.left.left = Node(1)
    root.left.right = Node(3)

    result = tree_to_doubly_list(root)
    print('Result: ',
          result.val, result.right.val, result.right.right.val,
          result.right.right.right.val, result.right.right.right.right.val)


if __name__ == "__main__":
    main()
