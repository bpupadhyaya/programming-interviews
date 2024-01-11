"""
You are given a string s consisting only of characters 'a' and 'b'.
You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of
 indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
Return the minimum number of deletions needed to make s balanced.

Example 1:
Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

Example 2:
Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.

Constraints:
1 <= s.length <= 10^5
s[i] is 'a' or 'b'.

Tag: M45/50
"""


def minimum_deletions(s: str) -> int:
    # track the minimum number of deletions to make the current string balanced ending with 'a', 'b'
    end_a, end_b = 0, 0
    for val in s:
        if val == 'a':
            # to end with 'a', nothing to do with previous ending with 'a'
            # to end with 'b', need to delete the current 'a' from previous ending with 'b'
            end_b += 1
        else:
            # to end with 'a', need to delete the current 'b' from previous ending with 'a'
            # to end with 'b', nothing to do, so just pick smaller of end_a, end_b
            end_a, end_b = end_a+1, min(end_a, end_b)
    return min(end_a, end_b)


def main():
    s = "aababbab"
    print(minimum_deletions(s))


if __name__ == "__main__":
    main()
