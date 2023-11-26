"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums
except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Tag: 13/150
Tag: 238/2927, R173/2936 (overall frequency ranking)
"""


def product_except_self(nums: list[int]) -> list[int]:
    length = len(nums)
    sol = [1] * length
    pre = 1
    post = 1
    for i in range(length):
        sol[i] *= pre
        pre = pre * nums[i]
        sol[length-i-1] *= post
        post = post * nums[length-i-1]
    return sol


def main():
    nums = [1, 2, 3, 4]
    print(product_except_self(nums))


if __name__ == "__main__":
    main()
