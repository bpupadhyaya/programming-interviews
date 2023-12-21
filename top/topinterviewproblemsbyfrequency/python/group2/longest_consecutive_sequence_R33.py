"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

Tag: R33/145
"""


def longest_consecutive(nums: list[int]) -> int:
    longest = 0
    num_set = set(nums)

    for n in num_set:
        if n-1 not in num_set:
            length = 1
            while n + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest


def main():
    nums = [100, 4, 200, 1, 3, 2]
    print(longest_consecutive(nums))


if __name__ == "__main__":
    main()
