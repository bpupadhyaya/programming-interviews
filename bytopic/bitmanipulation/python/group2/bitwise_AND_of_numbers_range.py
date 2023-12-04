"""
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers
in this range, inclusive.

Example:
Input: left = 5, right = 7
Output: 4

Tag: 130/150
Tag: 201/2927, R2106/2936 (overall frequency ranking)
"""


def range_bitwise_and(left: int, right: int) -> int:
    while right > left:
        right = right & right - 1  # Clear the least significant bit of right
    return right & left  # Return the bitwise AND of the modified right and left


def range_bitwise_and_1(left: int, right: int) -> int:
    shift = 0
    while left < right:
        # Right shift the left limit by 1 bit.
        left >>= 1
        # Right shift the right limit by 1 bit.
        right >>= 1
        # Increment the 'shift' variable by 1.
        shift += 1
        # Left shift the left limit by 'shift' bits and return the result.
    return left << shift


def main():
    left = 5
    right = 7
    print(range_bitwise_and_1(left, right))


if __name__ == "__main__":
    main()
