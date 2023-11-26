"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Tag: 6/150
Tag: 189/2927, R54/2936 (overall frequency ranking)
"""


def rotate(nums: list[int], k: int) -> None:
    length = len(nums)
    if length == k:
        return
    k = k % length  # the case when k > length
    nums.reverse()
    for i in range(k//2):
        nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
    for i in range(k, (length+k)//2):
        nums[i], nums[length-1-i+k] = nums[length-1-i+k], nums[i]


def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate(nums, k)
    print(nums)


if __name__ == "__main__":
    main()
