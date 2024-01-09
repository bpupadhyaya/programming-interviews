"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom,
column by column).
If two nodes are in the same row and column, the order should be from left to right.
Sample 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Note: visualize to understand

Tag: fb R7/50
"""
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def vertical_order(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    columns = defaultdict(list)
    q = deque([(root, 0)])
    while q:
        node, x = q.popleft()
        columns[x].append(node.val)
        if node.left:
            q.append((node.left, x-1))
        if node.right:
            q.append((node.right, x+1))

    return [columns[x] for x in range(min(columns), max(columns) + 1)]


def vertical_order1(root: TreeNode) -> list[list[int]]:
    if not root:
        return []

    queue, level_map, res = deque(), defaultdict(list), []
    queue.append((root, 0))

    while queue:
        node, level = queue.popleft()
        level_map[level].append(node.val)
        if node.left:
            queue.append((node.left, level - 1))
        if node.right:
            queue.append((node.right, level + 1))

    for key in sorted(level_map):
        res.append(level_map[key])

    return res


def main():
    root = TreeNode(3, TreeNode(9), TreeNode(20))
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(vertical_order1(root))


if __name__ == "__main__":
    main()
