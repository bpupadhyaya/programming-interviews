"""
Given an integer array nums where every element appears three times except for one, which appears exactly once.
Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example:
Input: nums = [0,1,0,1,0,1,99]
Output: 99

Tag: 129/150
Tag: 137/2927, R186/2936 (overall frequency ranking)
"""


def single_number(nums: list[int]) -> int:
    ans = 0
    for i in range(32):
        bit_sum = 0
        for num in nums:
            # Convert the number to two's complement representation to handle large test case
            if num < 0:
                num = num & (2**32-1)
            bit_sum += (num >> i) & 1
        bit_sum %= 3
        ans |= bit_sum << i
    # Convert the result back to two's complement representation if it's negative
    if ans >= 2**31:
        ans -= 2**32
    return ans


def single_number_1(nums: list[int]) -> int:
    ones = 0
    twos = 0

    for num in nums:
        ones ^= (num & ~twos)
        twos ^= (num & ~ones)
    return ones


def main():
    nums = [0, 1, 0, 1, 0, 1, 99]
    print(single_number_1(nums))


if __name__ == "__main__":
    main()
