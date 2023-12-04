"""
Given a string, return the longest palindromic substring.

Sample 1:
Input: s = "xyxyz"
Output: "xyx", also "yxy"

Tag: 145/150
Tag: 5/2927, R5/2936 (overall frequency ranking)
"""


def longest_palindrome_dp(s: str) -> str:
    if len(s) <= 1:
        return s
    max_len = 1
    max_str = s[0]
    dp = [[False for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
        for j in range(i):
            if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                dp[j][i] = True
                if i-j+1 > max_len:
                    max_len = i-j+1
                    max_str = s[j:i+1]
    return max_str


def longest_palindrome_recursive_time_limit_exceeded(s: str) -> str:
    if s == s[::-1]:
        return s
    left = longest_palindrome_recursive_time_limit_exceeded(s[1:])
    right = longest_palindrome_recursive_time_limit_exceeded(s[:-1])

    if len(left) > len(right):
        return left
    else:
        return right


def main():
    s = "xyxyz"
    print(longest_palindrome_recursive_time_limit_exceeded(s))


if __name__ == "__main__":
    main()

