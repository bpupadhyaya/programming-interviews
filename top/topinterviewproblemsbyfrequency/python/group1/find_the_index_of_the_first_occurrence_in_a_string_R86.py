"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.

Example:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Tag: R86/145
Tag: 23/150
Tag: 28/2927, R294/2936 (overall frequency ranking)
"""


def str_str(haystack: str, needle: str) -> int:
    if needle == haystack:
        return 0
    i = 0
    j = len(needle)
    while j <= len(haystack):
        current_needle = haystack[i:j]
        if current_needle == needle:
            return i
        i += 1
        j += 1
    return -1


def main():
    haystack = "sadbutsad"
    needle = "sad"
    print(str_str(haystack, needle))


if __name__ == "__main__":
    main()
