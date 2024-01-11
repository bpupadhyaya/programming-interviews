"""
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
In one move, you can increment n - 1 elements of the array by 1.

Example 1:
Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

Constraints:
n == nums.length
1 <= nums.length <= 10^5
-109 <= nums[i] <= 10^9
The answer is guaranteed to fit in a 32-bit integer.

Tag: M36/50
"""


def min_moves(nums: list[int]) -> int:
    return sum(nums) - (len(nums) * min(nums))


def main():
    nums = [1, 2, 3]
    print(min_moves(nums))


if __name__ == "__main__":
    main()

