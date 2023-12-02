"""
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will
fit in a 32-bit integer.
A leaf node is a node with no children.

Sample 1:
Input: root = [4,9,0,5,1]
Note: visualize to understand : hint: 4 in the first row, 9, 0 in the second row, 5, 1 in the third row.
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

Tag: 77/150
Tag: 129/2927, R892/2936 (overall frequency ranking)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_numbers(root: Optional[TreeNode]) -> int:
    my_list = []

    def dfs(root, s):
        if root is None:
            pass
        elif root.left is None and root.right is None:
            s += str(root.val)
            my_list.append(s)
        else:
            s += str(root.val)
            s1 = s[::]
            dfs(root.left, s)
            dfs(root.right, s1)
    dfs(root, "")
    ans = 0
    for i in my_list:
        ans += int(i)
    return ans


def main():
    root = TreeNode(4, TreeNode(9), TreeNode(0))
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)

    print(sum_numbers(root))


if __name__ == "__main__":
    main()
