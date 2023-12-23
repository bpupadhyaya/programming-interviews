"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.

Sample 1:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Tag: R60/145
Tag: 138/150
Tag: 198/2927, R164/2936 (overall frequency ranking)
"""


def rob(nums: list[int]) -> int:
    bag = (0, 0)
    for house in nums:
        bag = (bag[1], max(bag[0] + house, bag[1]))
    return bag[1]


def rob_using_dp_bottom_up(nums: list[int]) -> int:
    if len(nums) < 3:
        # Base case
        return max(nums)
    # mm memory stores maximum money until last two points
    mm = nums[0], max(nums[0], nums[1])
    # Iterate mm until we get the max money in the last house
    for i in range(2, len(nums)):
        # Only store last two points to save memory
        mm = mm[1], max(nums[i]+mm[0], mm[1])
    return mm[1]


def main():
    nums = [2, 7, 9, 3, 1]
    print(rob(nums))


if __name__ == "__main__":
    main()
