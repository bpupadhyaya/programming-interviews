"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element
in the array represents your maximum jump length at that position.
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

Tag: 9/150
Tag: 55/2927, R30/2936 (overall frequency ranking)
"""


def can_jump(nums: list[int]) -> bool:
    curr = nums[0]
    for i in range(1, len(nums)):
        if curr == 0:
            return False
        curr -= 1
        curr = max(curr, nums[i])
    return True


def main():
    nums = [2, 3, 1, 1, 4]
    print(can_jump(nums))


if __name__ == "__main__":
    main()
