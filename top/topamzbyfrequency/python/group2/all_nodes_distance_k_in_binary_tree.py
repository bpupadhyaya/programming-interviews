"""
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values
of all nodes that have a distance k from the target node.
You can return the answer in any order.

Example:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Tag: 863/2927 , R317/2935 , R15/50 (amz)
"""
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def distance_k(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    ans = []
    parent = {}
    queue = deque()
    queue.append(root)

    while queue:
        size = len(queue)
        for _ in range(size):
            top = queue.popleft()

            if top.left:
                parent[top.left.val] = top
                queue.append(top.left)

            if top.right:
                parent[top.right.val] = top
                queue.append(top.right)

    visited = {}
    queue.append(target)
    while k > 0 and queue:
        size = len(queue)

        for _ in range(size):
            top = queue.popleft()

            visited[top.val] = 1

            if top.left and top.left.val not in visited:
                queue.append(top.left)

            if top.right and top.right.val not in visited:
                queue.append(top.right)

            if top.val in parent and parent[top.val].val not in visited:
                queue.append(parent[top.val])

        k -= 1

    while queue:
        ans.append(queue.popleft().val)

    return ans


def main():
    root = TreeNode(3)
    target = TreeNode(5)
    root.left, root.right = target, TreeNode(1)
    root.left.left, root.left.right = TreeNode(6), TreeNode(2)
    root.right.left, root.right.right = TreeNode(0), TreeNode(8)
    root.left.right.left, root.left.right.right = TreeNode(7), TreeNode(4)

    k = 2

    print(distance_k(root, target, k))


if __name__ == "__main__":
    main()
