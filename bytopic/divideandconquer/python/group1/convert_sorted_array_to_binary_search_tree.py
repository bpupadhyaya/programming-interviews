"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced binary search tree.

Example:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted.

Tag: 108/150
Tag: 108/2927, R978/2936 (overall frequency ranking)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(nums: list[int]) -> Optional[TreeNode]:
    if len(nums) == 0:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])

    return root


def main():
    nums = [-10, -3, 0, 5, 9]
    res = sorted_array_to_bst(nums)
    print(res.val, res.left.val, res.right.val, res.left.left.val, res.right.left.val)


if __name__ == "__main__":
    main()
