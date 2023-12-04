"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position
of a given target value. If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Sample 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Soln: Time complexity: O(log(n)), space complexity: O(1)

Tag: 118/150
Tag: 34/2927, R114/2936 (overall frequency ranking)
"""


def search_range(nums: list[int], target: int) -> list[int]:
    def binary_search(nums, target, is_searching_left):
        left = 0
        right = len(nums) - 1
        idx = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right =  mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                idx = mid
                if is_searching_left:
                    right = mid - 1
                else:
                    left = mid + 1
        return idx

    left = binary_search(nums, target, True)
    right = binary_search(nums, target, False)

    return [left, right]


def main():
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(search_range(nums, target))


if __name__ == "__main__":
    main()
