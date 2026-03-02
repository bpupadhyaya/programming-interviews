"""
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Sample 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Note: visualize to understand
It is row level traversal starting from first row, which is root node.
Note: some output is missing, debug and find out.

Tag: R112/145
Tag: 84/150
Tag: 102/2927, R516/2936 (overall frequency ranking)
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    list1 = []
    q = deque()
    q.append(root)
    while q:
        level = []
        for i in range(len(q)):
            poping = q.popleft()
            if poping:
                level.append(poping.val)
                q.append(poping.left)
                q.append(poping.right)
        if level:
            list1.append(level)
    return list1


def level_order_ai_gemini(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])  # Start with the root in the queue

    while queue:
        level_size = len(queue)  # Snapshots the number of nodes at this level
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            # Only add children if they actually exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


def main():
    root = TreeNode(3, TreeNode(9), TreeNode(20))
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(level_order_ai_gemini(root))


if __name__ == "__main__":
    main()
