"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example,
the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1],
a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Tag: 119/150
Tag: 153/2927, R488/2936 (overall frequency ranking)
"""


def find_min(nums: list[int]) -> int:
    ans = nums[0]
    low, high = 0, len(nums) - 1
    if nums[low] < nums[high]:
        return nums[low]
    while low <= high:
        if nums[low] < nums[high]:
            ans = min(ans, nums[low])
            break
        mid = (low + high) // 2
        ans = min(ans, nums[mid])
        if nums[mid] >= nums[low]:
            low = mid + 1
        else:
            high = mid - 1
    return ans


def main():
    nums = [3, 4, 5, 1, 2]
    print(find_min(nums))


if __name__ == "__main__":
    main()
