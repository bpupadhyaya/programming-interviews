"""
There is a function signFunc(x) that returns:
1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).

Example 1:
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1

Constraints:
1 <= nums.length <= 1000
-100 <= nums[i] <= 100

Tag: F41/50
"""


def array_sign(nums: list[int]) -> int:
    ans = 1
    for x in nums:
        if x == 0:
            return 0
        if x < 0:
            ans *= -1
    return ans


def main():
    nums = [-1, -2, -3, -4, 3, 2, 1]
    print(array_sign(nums))


if __name__ == "__main__":
    main()
