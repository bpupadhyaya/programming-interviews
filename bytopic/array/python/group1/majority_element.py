"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority
element always exists in the array.

Example:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Tag: 5/150
Tag: 169/2927, R89/2936 (overall frequency ranking)
"""
from collections import defaultdict


def majority_element_using_sorting(nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    return nums[n//2]


def majority_element_using_hashmap(nums: list[int]) -> int:
    n = len(nums)
    m = defaultdict(int)
    for num in nums:
        m[num] += 1
    n = n // 2
    for key, value in m.items():
        if value > n:
            return key
    return 0


def majority_element_using_moore_voting_algo(nums: list[int]) -> int:
    count = 0
    candidate = 0
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate


def main():
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(majority_element_using_moore_voting_algo(nums))


if __name__ == "__main__":
    main()
