"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence
of "abcde" while "aec" is not).

Example:
Input: s = "abc", t = "ahbgdc"
Output: true

Tag: 26/150
Tag: 392/2927, R348/2936 (overall frequency ranking)
"""


def is_subsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


def main():
    s = "abc"
    t = "ahbgdc"
    print(is_subsequence(s, t))


if __name__ == "__main__":
    main()
