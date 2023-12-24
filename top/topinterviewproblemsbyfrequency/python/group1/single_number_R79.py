"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example:
Input: nums = [4,1,2,1,2]
Output: 4

Tag: R79/145
Tag: 128/150
Tag: 136/2927, R244/2936 (overall frequency ranking)
"""
import functools


def single_number_1(nums: list[int]) -> int:
    return functools.reduce(lambda x, y: x ^ y, nums, 0)


def single_number(nums: list[int]) -> int:
    unique_num = 0
    for idx in nums:
        unique_num ^= idx
    return unique_num


def main():
    nums = [4, 1, 2, 1, 2]
    print(single_number_1(nums))


if __name__ == "__main__":
    main()
