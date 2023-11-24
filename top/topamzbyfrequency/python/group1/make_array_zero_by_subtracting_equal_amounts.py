"""
You are given a non-negative integer array nums. In one operation, you must:
- Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
- Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.

Example:
Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].

Tag: 2357/2927 , R606/2935 , R27/50 (amz)
"""


def minimum_operations(nums: list[int]) -> int:
    # Each unique number (except 0) needs one operation.
    return len(set(nums) - {0})


def main():
    nums = [1, 5, 0, 3, 5]
    print(minimum_operations(nums))


if __name__ == "__main__":
    main()
