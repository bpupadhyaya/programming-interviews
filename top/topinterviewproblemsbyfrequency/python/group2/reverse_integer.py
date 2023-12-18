"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = -123
Output: -321

Example 2:
Input: x = 120
Output: 21

Constraints:
-2^{31} <= x <= 2^{31} - 1

Tag: R12/145
"""


def reverse(x: int) -> int:
    rev = int(str(abs(x))[::-1])
    return (-rev if x < 0 else rev) if rev.bit_length() < 32 else 0


def main():
    x = 120
    print(reverse(x))


if __name__ == "__main__":
    main()
