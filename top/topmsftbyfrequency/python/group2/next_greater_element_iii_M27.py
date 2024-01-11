"""
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n
and is greater in value than n. If no such positive integer exists, return -1.
Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit
in 32-bit integer, return -1.

Example 1:
Input: n = 12
Output: 21

Example 2:
Input: n = 21
Output: -1

Constraints:
1 <= n <= 2^{31} - 1

Tag: M27/50
"""


def next_greater_element(n: int) -> int:
    nums = list(str(n))
    i = len(nums) - 1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i == 0:
        return -1
    j = len(nums) - 1
    while j > i-1 and nums[j] <= nums[i-1]:
        j -= 1
    nums[i-1], nums[j] = nums[j], nums[i-1]
    nums[i:] = nums[i:][::-1]
    res = int(''.join(nums))
    return res if res < 2**31 else -1


def main():
    n = 12
    print(next_greater_element(n))


if __name__ == "__main__":
    main()


"""
Explanation:
Convert the input number n into a list of digits.
Traverse the list from right to left to find the first decreasing digit i-1.
If there is no such digit, the input number is already the largest possible permutation, so return -1.
Traverse the list again from right to left to find the smallest digit j greater than i-1.
Swap i-1 with j.
Reverse the sublist from i to the end of the list to obtain the smallest possible permutation greater than the original
 number.
If the resulting permutation is greater than 2^31 - 1, return -1. Otherwise, return the permutation as an integer.
"""
