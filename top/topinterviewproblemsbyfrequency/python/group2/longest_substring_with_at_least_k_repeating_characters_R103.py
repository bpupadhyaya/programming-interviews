"""
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of
each character in this substring is greater than or equal to k.

if no such substring exists, return 0.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Constraints:
1 <= s.length <= 10^4
s consists of only lowercase English letters.
1 <= k <= 10^5

R103/145
"""
import collections


def longest_substring(s: str, k: int) -> int:
    cnt = collections.Counter(s)
    st = 0
    max_st = 0
    for i, c in enumerate(s):
        if cnt[c] < k:
            max_st = max(max_st, longest_substring(s[st:i], k))
            st = i + 1
    return len(s) if st == 0 else max(max_st, longest_substring(s[st:], k))


def longest_substring_1(s: str, k: int) -> int:
    # Divide and conquer
    if len(s) < k:
        return 0
    c = collections.Counter(s)
    st = 0
    for p, v in enumerate(s):
        if c[v] < k:
            return max(longest_substring_1(s[st:p], k), longest_substring_1(s[p+1:], k))
    return len(s)


def main():
    s = "ababbc"
    k = 2
    print(longest_substring_1(s, k))


if __name__ == "__main__":
    main()
