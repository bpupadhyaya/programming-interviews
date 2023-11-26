"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each
unique element appears at most twice. The relative order of the elements should be kept the same.
Since it is impossible to change the length of the array in some languages, you must instead have the result
be placed in the first part of the array nums. More formally, if there are k elements after removing the
duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave
beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place
with O(1) extra memory.

Example:
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3
respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Tag: 4/150
Tag: 80/2927, R506/2936 (overall frequency ranking)
"""


def remove_duplicates(nums: list[int]) -> int:
    k = 0
    for i in nums:
        if k < 2 or i != nums[k-2]:
            nums[k] = i
            k += 1
    return k


def main():
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(remove_duplicates(nums))


if __name__ == "__main__":
    main()
