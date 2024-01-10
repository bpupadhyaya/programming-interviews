"""
You are given an integer array nums of length n and an integer numSlots such that 2 * numSlots >= n. There are
 numSlots slots numbered from 1 to numSlots.
You have to place all n integers into the slots such that each slot contains at most two numbers. The AND sum of
 a given placement is the sum of the bitwise AND of every number with its respective slot number.
For example, the AND sum of placing the numbers [1, 3] into slot 1 and [4, 6] into slot 2 is equal to
 (1 AND 1) + (3 AND 1) + (4 AND 2) + (6 AND 2) = 1 + 1 + 0 + 2 = 4.
Return the maximum possible AND sum of nums given numSlots slots.

Example 1:
Input: nums = [1,2,3,4,5,6], numSlots = 3
Output: 9
Explanation: One possible placement is [1, 4] into slot 1, [2, 6] into slot 2, and [3, 5] into slot 3.
This gives the maximum AND sum of (1 AND 1) + (4 AND 1) + (2 AND 2) + (6 AND 2) + (3 AND 3) + (5 AND 3)
= 1 + 0 + 2 + 2 + 3 + 1 = 9.

Constraints:
n == nums.length
1 <= numSlots <= 9
1 <= n <= 2 * numSlots
1 <= nums[i] <= 15

Tag: G29/50
"""
from functools import cache


def maximum_and_sum(nums: list[int], num_slots: int) -> int:
    @cache
    def fn(k, m):
        """Return max AND sum."""
        if k == len(nums):
            return 0
        ans = 0
        for i in range(num_slots):
            if m & 1 << 2*i == 0 or m & 1 << 2*i+1 == 0:
                if m & 1 << 2*i == 0:
                    mm = m ^ 1 << 2*i
                else:
                    mm = m ^ 1 << 2*i+1
                ans = max(ans, (nums[k] & i+1) + fn(k+1, mm))
        return ans

    return fn(0, 0)


def main():
    nums = [1, 2, 3, 4, 5, 6]
    num_slots = 3
    print(maximum_and_sum(nums, num_slots))


if __name__ == "__main__":
    main()
