"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
you can see ordered from top to bottom.

Sample 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Note: visualize to understand

Tag: 82/150
Tag: 199/2927, R549/2936 (overall frequency ranking), fb R23/50
"""
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    queue = deque()
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [root.val]

    result = []
    queue.append(root)
    while queue:
        child_queue = deque()
        prev = -1
        while queue:
            curr = queue.popleft()
            if curr.left is not None:
                child_queue.append(curr.left)
            if curr.right is not None:
                child_queue.append(curr.right)
            prev = curr
        result.append(prev.val)
        queue = child_queue
    return result


def main():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    print(right_side_view(root))


if __name__ == "__main__":
    main()
