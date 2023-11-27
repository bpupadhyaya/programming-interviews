"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters
include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Tag: 25/150
Tag: 125/2927, R117/2936 (overall frequency ranking), fb R9/50
"""


def is_palindrome(s: str) -> bool:
    s = [i for i in s.lower() if i.isalnum()]
    return s == s[::-1]


def is_palindrome_two_pointer(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        a, b = s[i].lower(), s[j].lower()
        if a.isalnum() and b.isalnum():
            if a != b:
                return False
            else:
                i, j = i + 1, j - 1
                continue
        i, j = i + (not a.isalnum()), j - (not b.isalnum())
    return True


def main():
    s = "A man, a plan, a canal: Panama"
    print(is_palindrome_two_pointer(s))


if __name__ == "__main__":
    main()
