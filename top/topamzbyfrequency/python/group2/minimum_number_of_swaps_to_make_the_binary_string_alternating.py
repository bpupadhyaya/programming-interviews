"""
Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is impossible.

The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and "1010"
are alternating, while the string "0100" is not.
Any two characters may be swapped, even if they are not adjacent.

Example 1:
Input: s = "111000"
Output: 1
Explanation: Swap positions 1 and 4: "111000" -> "101010"
The string is now alternating.

Example 2:
Input: s = "010"
Output: 0
Explanation: The string is already alternating, no swaps are needed.

Example 3:
Input: s = "1110"
Output: -1

Tag: 1864/2927 , R2389/2935 , R47/50 (amz)
"""


def min_swaps(s: str) -> int:
    ones = s.count("1")
    zeros = len(s) - ones
    if abs(ones - zeros) > 1:
        return -1  # impossible

    def fn(x):
        ans = 0
        for c in s:
            if c != x:
                ans += 1
            x = "1" if x == "0" else "0"
        return ans // 2

    if ones > zeros:
        return fn("1")
    elif ones < zeros:
        return fn("0")
    else:
        return min(fn("0"), fn("1"))


def main():
    s = "111000"
    print(min_swaps(s))


if __name__ == "__main__":
    main()
