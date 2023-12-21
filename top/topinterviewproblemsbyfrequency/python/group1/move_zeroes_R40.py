"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
elements.
Note that you must do this in-place without making a copy of the array.

Example:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Constraints:
1 <= nums.length <= 10^4
-2^{31} <= nums[i] <= 2^{31} - 1

Follow up: Could you minimize the total number of operations done?

Tag: R40/145
"""


def move_zeroes(nums: list[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
        # Wait while we find a non-zero element to swap with
        if nums[slow] != 0:
            slow += 1


def main():
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    print(nums)


if __name__ == "__main__":
    main()

"""
Complexity:
Time complexity: O(n). Our fast pointer does not visit the same spot twice.
Space complexity: O(1). All operations are made in-place
"""
