"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Constraints:
1 <= s.length <= 10^5
s[i] is a printable ascii character.

Tag: R63/145
"""


def reverse_string_0(s: list[str]) -> None:
    s.reverse()


def reverse_string(s: list[str]) -> None:
    s[:] = s[::-1]


def reverse_string_1(s: list[str]) -> None:
    size = len(s)
    # Reverse string by mirror image
    for i in range(size // 2):
        s[i], s[-i-1] = s[-i-1], s[i]


def reverse_string_2(s: list[str]) -> None:
    def reverse(l, r, s):
        if l >= r:
            return
        s[l], s[r] = s[r], s[l]
        reverse(l+1, r-1, s)

    reverse(0, len(s)-1, s)


def reverse_string_3(s: list[str]) -> None:
    start = 0
    end = len(s) - 1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start = start + 1
        end = end - 1


def main():
    s = ["h", "e", "l", "l", "o"]
    reverse_string_3(s)
    print(s)


if __name__ == "__main__":
    main()
