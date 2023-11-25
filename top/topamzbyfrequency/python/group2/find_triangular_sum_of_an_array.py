"""
You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:
1. Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums
of length n - 1.
2. For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes
modulo operator.
3. Replace the array nums with newNums.
4. Repeat the entire process starting from step 1.

Return the triangular sum of nums.

Example:
Input: nums = [1,2,3,4,5]
Output: 8
Explanation:
Process diagram:
1   2   3   4   5
  3   5   7   9
    8   2   6
      0   8
        8
The above diagram (note: arrows are missing, e.g. 1 and 2 in the first row point to 3 in the second row, 2 and 3 in the
first row point to 5 in the second row, and the pattern follows for all numbers) depicts the process
from which we obtain the triangular sum of the array.

Tag: 2221/2927 , R1904/2935 , R46/50 (amz)
"""
from math import comb


def triangualr_sum_using_comb(nums: list[int]) -> int:
    return sum(n * comb(len(nums) - 1, i) for i, n, in enumerate(nums)) % 10


def triangualr_sum_using_ncr(nums: list[int]) -> int:
    res, ncr, n = 0, 1, len(nums) - 1
    for r, num in enumerate(nums):
        res = (res + num * ncr) % 10
        ncr = ncr * (n - r) // (r + 1)
    return res


def main():
    nums = [1, 2, 3, 4, 5]
    print(triangualr_sum_using_ncr(nums))


if __name__ == '__main__':
    main()
