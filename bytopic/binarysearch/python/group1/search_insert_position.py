"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Tag: 114/150
Tag: 35/2927, R434/2936 (overall frequency ranking)
"""


def search_insert(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while right >= left:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return left


def main():
    nums = [1, 3, 5, 6]
    target = 5
    print(search_insert(nums, target))


if __name__ == "__main__":
    main()
