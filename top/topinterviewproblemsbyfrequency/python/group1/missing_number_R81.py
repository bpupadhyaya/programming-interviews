"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is
missing from the array.

Example:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the
range since it does not appear in nums.

Constraints:
n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

R81/145
"""
from functools import reduce


def missing_number(nums: list[int]) -> int:
    # We can find the sum of first n numbers using Gauss formula.
    # (n * (n+1))/2 where `n` is the length of input `nums`.
    # Then just subtract this with the sum of input nums to find the missing number.
    return (len(nums) * (len(nums) + 1)) // 2 - sum(nums)


def missing_number_1(nums: list[int]) -> int:
    return reduce(lambda x,y: x ^ y, list(range(len(nums) + 1)) + nums)


def main():
    nums = [3, 0, 1]
    print(missing_number_1(nums))


if __name__ == "__main__":
    main()


"""
Bit manipulation:
In this approach, we will concat the input nums with the sequence of numbers from [0, n]. Then we would perform 
the reduce operation using an xor operator. The xor operation cancels the same elements in the list. So after the
reduce operation, we would be left only with the missing number
Complexity:
Time - O(n)
Space - O(1) 
"""
