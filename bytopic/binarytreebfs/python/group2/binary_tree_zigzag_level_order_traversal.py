"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes'
values. (i.e., from left to right, then right to left for the next level and alternate between).

Sample 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Note: visualize to understand
It is row level traversal starting from first row, which is root node. First left to right, then right to
left and again left to right and so on.

Tag: 85/150
Tag: 103/2927, R697/2936 (overall frequency ranking)
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return[]
    res = []
    queue = deque([root])
    even_level = False
    while queue:
        n = len(queue)
        level = deque()
        for _ in range(n):
            node = queue.popleft()
            if even_level:
                level.appendleft(node.val)
            else:
                level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(list(level))
        even_level = not even_level
    return res


def main():
    root = TreeNode(3, TreeNode(9), TreeNode(20))
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(zigzag_level_order(root))


if __name__ == "__main__":
    main()
