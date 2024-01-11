"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only
have a single space separating the words. Do not include any extra spaces.

Example:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Tag: 21/150
Tag: 151/2927, R319/2936 (overall frequency ranking), M21/50

"""


def reverse_words(s: str) -> str:
    result = []
    temp = ""
    for c in s:
        if c != " ":
            temp += c
        elif temp != "":
            result.append(temp)
            temp = ""
    if temp != "":
        result.append(temp)
    return " ".join(result[::-1])


def main():
    s = "  hello world  "
    print(reverse_words(s))


if __name__ == "__main__":
    main()
