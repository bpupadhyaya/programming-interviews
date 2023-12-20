"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if
every element is distinct.

Example:
Input: nums = [1,2,3,1]
Output: true

Tag: R28/145
"""


def contains_duplicate_using_hashset(nums: list[int]) -> bool:
    # Time complexity: O(n)
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def contains_duplicate_using_hashmap(nums: list[int]) -> bool:
    # Time complexity: O(n)
    seen = {}
    for num in nums:
        if num in seen and seen[num] >= 1:
            return True
        seen[num] = seen.get(num, 0) + 1
    return False


def contains_duplicate_using_sorting(nums: list[int]) -> bool:
    # Time complexity: O(n log n)
    nums.sort()
    n = len(nums)
    for i in range(1, n):
        if nums[i] == nums[i-1]:
            return True
    return False


def contains_duplicate_using_brute_force(nums: list[int]) -> bool:
    # Time complexity: O(n^2)
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                return True
    return False


def main():
    nums = [1, 2, 3, 1]
    print(contains_duplicate_using_brute_force(nums))


if __name__ == "__main__":
    main()

