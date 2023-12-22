"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a
given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]


Constraints:
0 <= nums.length <= 10^5
-109 <= nums[i] <= 10^9
nums is a non-decreasing array.
-109 <= target <= 109

Tag: R49/145
"""


def search_range_1(nums: list[int], target: int) -> list[int]:
    # Brute force
    first, last = -1, -1
    for i in range(len(nums)):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first, last]


def search_range_2(nums: list[int], target: int) -> list[int]:
    # O (log n) soln
    def search(x):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo
    lo = search(target)
    hi = search(target+1) - 1

    if lo <= hi:
        return [lo, hi]
    return [-1, -1]


def main():
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(search_range_2(nums, target))


if __name__ == "__main__":
    main()


"""
Linear Search (Brute Force):
Initialize two variables, first and last, to -1.
Iterate through the sorted array from left to right.
When you encounter the target element for the first time, set first to the current index.
Continue iterating to find the last occurrence of the target element and update last whenever you encounter it.
Return first and last
Complexity:
Time Complexity: O(n) - In the worst case, you may have to traverse the entire array.
Space Complexity: O(1) - Constant extra space is used.


"""
