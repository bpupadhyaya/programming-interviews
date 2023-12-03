"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Tag: 112/150
Tag: 53/2927, R37/2936 (overall frequency ranking)
"""


def max_subarray(nums: list[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray(nums))


if __name__ == "__main__":
    main()
