"""
Given a string s, return the longest palindromic substring in s.

Example:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Tag: Tag: R4/145
"""


def longest_palindrome(s: str) -> str:
    if len(s) <= 1:
        return s

    def expand_from_center(left, right):
        while left >= 0 and right <= len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1: right]
    max_str = s[0]

    for i in range(len(s) - 1):
        # For odd length palindrome, we will consider the current character as the center and expand around it.
        odd = expand_from_center(i, i)
        # For even length palindrome, we will consider the current character and the next character as the center and
        # expand around it.
        even = expand_from_center(i, i+1)

        if len(odd) > len(max_str):
            max_str = odd
        if len(even) > len(max_str):
            max_str = even

    return max_str


def main():
    s = "babad"
    print(longest_palindrome(s))


if __name__ == "__main__":
    main()


"""
Brief note: The algo checks for every character position and every position in between characters.
Analysis :
To enumerate all palindromic substrings of a given string, we first expand a given string at each possible 
starting position of a palindrome and also at each possible ending position of a palindrome and keep track of the 
length of the longest palindrome we found so far.

Approach:
We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, 
and there are only 2n - 1 such centers.
You might be asking why there are 2n - 1 but not n centers? The reason is the center of a palindrome can be 
in between two letters. Such palindromes have even number of letters (such as "abba") and its center are between 
the two 'b's.'
Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).

Algorithm :
At starting we have max_str = s[0] and max_len = 1 as every single character is a palindrome.
Now, we will iterate over the string and for every character we will expand around its center.
For odd length palindrome, we will consider the current character as the center and expand around it.
For even length palindrome, we will consider the current character and the next character as the center and 
expand around it.
We will keep track of the maximum length and the maximum substring.
Print the maximum substring.

Complexity Analysis:
Time complexity : O(n^2). Since expanding a palindrome around its center could take O(n) time, the overall 
complexity is O(n^2).

Space complexity : O(1).
"""