"""
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are
within the inclusive range.
A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of
nums is included in any of the ranges, and each missing number is covered by one of the ranges.

Example:
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]
Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]

Constraints:
-10^9 <= lower <= upper <= 10^9
0 <= nums.length <= 100
lower <= nums[i] <= upper
All the values of nums are unique.

R142/145, F44/50
"""


def find_missing_ranges_0(nums: list[int], lower: int, upper: int) -> list[list[int]]:
    def stringify(a, b):
        if a == b:
            return str(a)
        else:
            return str(a) + "->" + str(b)

    nums = [lower - 1] + nums + [upper + 1]  # trick to avoid edge cases
    ans = []
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] > 1:
            ans.append(stringify(nums[i-1]+1, nums[i]-1))
    return ans


def find_missing_ranges(nums: list[int], lower: int, upper: int) -> list[list[int]]:
    start = lower
    ranges = []

    def add_range(l, r):
        if l == r - 1:
            ranges.append(str(l))
        else:
            ranges.append("{}->{}".format(l, r-1))

    for n in nums:
        if start < n:
            add_range(start, n)
        start = n + 1

    if start <= upper:
        add_range(start, upper + 1)

    return ranges


def main():
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    print(find_missing_ranges_0(nums, lower, upper))


if __name__ == "__main__":
    main()