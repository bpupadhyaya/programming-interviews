"""
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and
smallest element in the subarray.
Return the sum of all subarray ranges of nums.
A subarray is a contiguous non-empty sequence of elements within an array.

Example:
Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

Tag: 2104/2927 , R905/2935 , R32/50 (amz)
"""
from operator import lt, gt


def sub_array_ranges(nums: list[int]) -> int:
    def fn(op):
        ans = 0
        stack = []
        for i in range(len(nums) + 1):
            while stack and (i == len(nums) or op(nums[stack[-1]], nums[i])):
                mid = stack.pop()
                ii = stack[-1] if stack else - 1
                ans += nums[mid] * (i - mid) * (mid - ii)
            stack.append(i)
        return ans

    return fn(lt) - fn(gt)


def main():
    nums = [1, 2, 3]
    print(sub_array_ranges(nums))


if __name__ == "__main__":
    main()
