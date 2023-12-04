"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Sample 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Tag: 141/150
Tag: 300/2927, R99/2936 (overall frequency ranking)
"""
from bisect import bisect_left


def length_of_lis(nums: list[int]) -> int:
    arr = [nums.pop(0)]
    for n in nums:
        if n > arr[-1]:
            arr.append(n)
        else:
            arr[bisect_left(arr, n)] = n
    return len(arr)


def main():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(length_of_lis(nums))


if __name__ == "__main__":
    main()
