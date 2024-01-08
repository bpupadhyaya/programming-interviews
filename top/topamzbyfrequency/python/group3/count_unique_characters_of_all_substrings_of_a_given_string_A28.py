"""
Let's define a function countUniqueChars(s) that returns the number of unique characters in s.
- For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique
characters since they appear only once in s, therefore countUniqueChars(s) = 5.

Given a string s, return the sum of countUniqueChars(t) where t is a substring of s. The test cases are
generated such that the answer fits in a 32-bit integer.
Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

Example:
Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Every substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

Tag: 828/2927 , R614/2935 , R28/50 (amz)
"""
from collections import defaultdict


def unique_letter_string(s: str) -> int:
    last_position = defaultdict(int)  # Used for storing the last position of each character
    contribution = defaultdict(int)  # Used for storing the contribution of each character so far. This will
    # possibly be updated throughout the string traversal

    res = 0

    for i, char in enumerate(s):
        max_possible_substrs_at_idx = i + 1
        contribution[char] = max_possible_substrs_at_idx - last_position[char]

        res += sum(contribution.values())
        last_position[char] = i + 1

    return res


def main():
    s = "ABC"
    print(unique_letter_string(s))


if __name__ == "__main__":
    main()


"""
Complexity: O(N) time, O(1) space

The key ideas behind the solution:
1. The maximum possible substrings that can end at an index are i + 1.
2. The contribution of a character to this substring is (i + 1) - it's last seen position.
3. At each point, sum of all contributions, gives the number of total substrings found so far.
4. The last seen position of char is actually i + 1.

"""