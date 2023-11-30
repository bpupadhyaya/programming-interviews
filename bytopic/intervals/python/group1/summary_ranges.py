"""
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each
element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of
the ranges but not in nums.
Each range [a,b] in the list should be output as:
 "a->b" if a != b
 "a" if a == b

Example:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Tag: 48/150
Tag: 228/2927, R295/2936 (overall frequency ranking)
"""


def summary_ranges(nums: list[int]) -> list[str]:
    ranges = []  # [start, end] or [x, y]
    for n in nums:
        if ranges and ranges[-1][1] == n - 1:
            ranges[-1][1] = n
        else:
            ranges.append([n, n])
    return [f'{x}->{y}' if x != y else f'{x}' for x, y in ranges]


def summary_ranges1(nums: list[int]) -> list[str]:
    if not nums:
        return []
    ranges = []
    start_ = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1] + 1:
            if start_ == nums[i-1]:
                ranges.append(str(start_))
            else:
                ranges.append(str(start_) + "->" + str(nums[i-1]))
            start_ = nums[i]

    # Handle the last range
    if start_ == nums[-1]:
        ranges.append(str(start_))
    else:
        ranges.append(str(start_) + "->" + str(nums[-1]))

    return ranges


def main():
    nums = [0, 2, 3, 4, 6, 8, 9]
    print(summary_ranges1(nums))


if __name__ == "__main__":
    main()
