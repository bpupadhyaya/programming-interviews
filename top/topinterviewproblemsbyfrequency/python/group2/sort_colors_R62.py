"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

Tag: R62/145
"""
from collections import Counter


def sort_colors(nums: list[int]) -> None:
    red, white, blue = 0, 0, len(nums) - 1
    while white <= blue:
        if nums[white] == 0:
            nums[white], nums[red] = nums[red], nums[white]
            red += 1
            white += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1


def sort_colors_1(nums: list[int]) -> None:
    prefix = Counter(nums)
    for i in range(prefix[0]):
        nums[i] = 0
    prefix[1] += prefix[0]
    for i in range(prefix[0], prefix[1]):
        nums[i] = 1
    prefix[2] += prefix[1]
    for i in range(prefix[1], prefix[2]):
        nums[i] = 2


def sort_colors_2(nums: list[int]) -> None:
    a, b = nums.count(0), nums.count(1)
    for i in range(len(nums)):
        if a != 0:
            nums[i] = 0
            a -= 1
        elif b != 0:
            nums[i] = 1
            b -= 1
        else:
            nums[i] = 2


def main():
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors_2(nums)
    print(nums)


if __name__ == "__main__":
    main()


"""
sort_colors_1 explanation:
Intuition
Let's briefly explain, what the problem is:

there a list of nums, it consists only with 0, 1's and 2's
our goal is to sort nums in ascending order in-place
The simplest approach we could use is to apply built-in sorting methods, but they're not allowed.

So, what if we count frequencies of integers? We will get a frequency map.
Since we know, that all of the integers must be sorted like [0,0,1,2] we will map frequency of each integer to a 
particular index with using intervals.

Approach
declare prefix array to map frequencies to a particular integer
iterate over nums and build prefix
iterate over each interval from map and add to prefix the last frequency for integers 1 and 2
Complexity
Time complexity: O(N), since we iterate over nums

Space complexity: O(1), we don't allocate extra space, except prefix, but it stores only constant amount of integers, 
while having a maximum size as 3

"""

