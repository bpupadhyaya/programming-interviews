"""
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
A good subarray is a subarray where:
its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:
A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
"""


def check_subarray_sum(nums: list[int], k: int) -> bool:
    mp = {0: -1}
    prefix_sum = 0
    for i, num in enumerate(nums):
        prefix_sum += num
        if k != 0:
            prefix_sum = prefix_sum % k
        if prefix_sum in mp:
            # We know that sum between mp[prefix_sum] + 1 and i is multiple of K, so We don't have to
            # include mp[prefix_sum]
            if i - mp[prefix_sum] > 1:
                return True
        else:
            # if prefix_sum doesn't exist, then add its index, otherwise don't update it, we would always prefer
            # to keep the
            # oldest index, so that we can get length of at least 2
            mp[prefix_sum] = i

    return False


def main():
    nums = [23, 2, 6, 4, 7]
    k = 6
    print(check_subarray_sum(nums, k))


if __name__ == "__main__":
    main()

