"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Tag: 30/150
Tag: 209/2927, R394/2936 (overall frequency ranking)
"""

from sys import maxsize


def min_sub_array_len(target: int, nums: list[int]) -> int:
    res = maxsize
    left, total = 0, 0
    for i in range(len(nums)):
        total += nums[i]
        while total >= target:
            res = min(res, i - left + 1)
            total -= nums[left]
            left += 1
    return res if res != maxsize else 0


def main():
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(min_sub_array_len(target, nums))


if __name__ == "__main__":
    main()
