"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters
and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Constraints:
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.

Tag: Tag: R52/145
"""


def is_palindrome_1(s: str) -> bool:
    s = [c.lower() for c in s if c.isalnum()]
    return all(s[i] == s[~i] for i in range(len(s) // 2))


def is_palindrome_2(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


def is_palindrome_3(s: str) -> bool:
    s = [char.lower() for char in s if char.isalnum()]
    return s == s[::-1]


def is_palindrome_4(s: str) -> bool:
    l = 0
    r = len(s) - 1
    while l < r:
        while l < r and s[l].isalnum() is False:
            l += 1
        while r > l and s[r].isalnum() is False:
            r -= 1
        if l > r or s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1
    return True


def main():
    s = "A man, a plan, a canal: Panama"
    print(is_palindrome_4(s))


if __name__ == "__main__":
    main()

"""
Two poiner approach:
Intuition
The code aims to determine whether a given string is a palindrome or not. A palindrome is a string that reads the 
same forwards and backwards. The code uses two pointers, l and r, to traverse the string from the beginning and end 
simultaneously. It skips non-alphanumeric characters and compares the corresponding characters at l and r positions. 
If at any point the characters are not equal, the string is not a palindrome. If the pointers meet or cross each 
other, the string is a palindrome.

Approach
Initialize l and r as the left and right pointers.
While l is less than r:
Increment l until it points to an alphanumeric character.
Decrement r until it points to an alphanumeric character.
If l becomes greater than r, return True as the string is a palindrome.
Compare characters at l and r (case-insensitive):
If they are not equal, return False as the string is not a palindrome.
If they are equal, increment l and decrement r.
Return True if the loop completes without finding any mismatch.

Complexity:
Time complexity: O(n)
Space complexity: O(1)
"""
