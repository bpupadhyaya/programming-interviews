"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Tag: 19/150
Tag: 58/2927, R712/2936 (overall frequency ranking)
"""


def length_of_last_word(s: str) -> int:
    length = 0
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    return length


def length_of_last_word_1(s: str) -> int:
    return len(s.strip().split(" ")[-1])


def main():
    s = "   fly me   to   the moon  "
    print(length_of_last_word(s))


if __name__ == "__main__":
    main()
