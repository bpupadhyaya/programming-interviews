"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible
palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.

R101/145
"""
import collections
from functools import cache


def partition(s: str) -> list[list[str]]:
    n = len(s)
    dp = [[] for _ in range(n+1)]
    dp[n] = [[]]
    for begin in range(n-1, -1, -1):
        for end in range(begin+1, n+1):
            candidate = s[begin:end]
            if candidate == candidate[::-1]:
                for each in dp[end]:
                    new_each = [candidate]
                    new_each.extend(each)
                    dp[begin].append(new_each)
    return dp[0]


@cache   # the memory trick can save some time
def partition_1_python3(s: str) -> list[list[str]]:
    if not s:
        return [[]]
    ans = []
    for i in range(1, len(s) + 1):
        if s[:i] == s[:i][::-1]:  # prefix is a palindrome
            for suf in partition(s[i:]):  # process suffix recursively
                ans.append([s[:i]] + suf)
    return ans


def partition_1_python2(s: str) -> list[list[str]]:
    # Needs debugging, wrong output
    memory = collections.defaultdict(list)

    def partition_(s):
        if not s:
            return [[]]
        if s in memory:
            return memory[s]  # the memory trick can save some time
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in partition_(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        memory[s] = ans
        return ans


def main():
    s = "aab"
    print(partition_1_python2(s))


if __name__ == "__main__":
    main()

"""
partition_1 explanation:
Approach:
Find answer recursively and memory trick can save some time
traverse and check every prefix s[:i] of s
if prefix s[:i] is a palindrome, then process the left suffix s[i:] recursively
since the suffix s[i:] may repeat, the memory trick can save some time

Complexity:
Time  Complexity: O(N * (2 ^ N))
Space Complexity: O(N * (2 ^ N))

"""