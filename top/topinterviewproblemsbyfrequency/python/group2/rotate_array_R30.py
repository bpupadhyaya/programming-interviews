"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Constraints:
1 <= nums.length <= 10^5
-2^{31} <= nums[i] <= 2^{31} - 1
0 <= k <= 10^5

Tag: R30/145
"""


def rotate_1(nums: list[int], k: int) -> None:
    # Run a for loop k times
    # Insert the last element of the list to the start of the list
    # Pop the last element of the list
    for x in range(k):
        nums.insert(0, nums[-1]), nums.pop(-1)


def rotate_2(nums: list[int], k: int) -> None:
    # List slicing method
    k = k % len(nums)  # take care of the case where k >= len(nums)
    nums[:] = nums[-k:] + nums[:-k]


def rotate_3(nums: list[int], k: int) -> None:
    # List replacing method
    k = k % len(nums)
    if len(nums) > 1 and k > 0:
        nums[:k], nums[k:] = nums[-k:], nums[:-k]


def rotate_4(nums: list[int], k: int) -> None:
    # Index assigning method
    k = k % len(nums)
    tmp = nums[-k:]
    for index in range(len(nums) - 1, k-1, -1):
        nums[index] = nums[index-k]
    for index, value in enumerate(tmp):
        nums[index] = value


def rotate_5(nums: list[int], k: int) -> None:
    # Reversed method
    k = k % len(nums)
    if len(nums) > 1 and k > 0:
        nums[:] = reversed(nums)
        nums[:k], nums[k:] = reversed(nums[:k]), reversed(nums[k:])


def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate_5(nums, k)
    print(nums)


if __name__ == "__main__":
    main()
