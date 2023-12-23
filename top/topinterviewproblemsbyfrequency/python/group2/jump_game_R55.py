"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in
the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it
impossible to reach the last index.

Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5

Tag: R55/145
"""


def can_jump(nums: list[int]) -> bool:
    # Take curr variable to keep the current maximum jump
    curr = nums[0]
    # Traverse all the elements through the loop
    for i in range(1, len(nums)):
        # If the current index 'i' is less than current maximum jump 'curr'
        # It means there is no way to jump to current index
        # So we should return false
        if curr == 0:
            return False
        curr -= 1
        # Update the current maximum jump
        curr = max(curr, nums[i])  # It is possible to reach the end of teh array
    return True


def main():
    nums = [2, 3, 1, 1, 4]
    print(can_jump(nums))


if __name__ == "__main__":
    main()
