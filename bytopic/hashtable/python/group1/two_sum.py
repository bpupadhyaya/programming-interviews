"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add
up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Tag: 44/150
Tag: 1/2927, R1/2936 (overall frequency ranking)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    num_map = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in num_map:
            return [num_map[complement], i]
        num_map[nums[i]] = i
    return []  # No solution case


def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))


if __name__ == "__main__":
    main()
