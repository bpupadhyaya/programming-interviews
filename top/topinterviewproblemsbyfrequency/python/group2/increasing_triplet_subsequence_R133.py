"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k
and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:

1 <= nums.length <= 5 * 10^5
-2^{31} <= nums[i] <= 2^{31} - 1
Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

R133/145
"""
import math


def increasing_triplet(nums: list[int]) -> bool:
    first = second = math.inf
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:  # Now first < num, if num <= second then try to make `second` as small as possible
            second = num
        else:  # now first < second < num
            return True
    return False


def main():
    nums = [2, 1, 5, 0, 4, 6]
    print(increasing_triplet(nums))


if __name__ == "__main__":
    main()


"""
increasing_triplet explanation:
We keep 2 numbers first and second where first < second, and first number must be before second number.
Iterate num in nums:
If num <= first then update the first as minimum as possible, by first = num
Else If num <= second then update second as minimum as possible (since now first < num <= second), by second = num
Else, now first < second < num then we found a valid Increasing Triplet Subsequence, return True.
Otherwise, return False.
Complexity:
Time: O(N)
Space: O(1)

"""
