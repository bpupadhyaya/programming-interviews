"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

R77/145, M19/50
"""


def is_match(s: str, p: str) -> bool:
    i, j = len(s) - 1, len(p) - 1

    def backtrack(cache, s, p, i, j):
        key = (i, j)
        if key in cache:
            return cache[key]

        if i == -1 and j == -1:
            cache[key] = True
            return True

        if i != -1 and j == -1:
            cache[key] = False
            return cache[key]

        if i == -1 and p[j] == '*':
            k = j
            while k != -1 and p[k] == '*':
                k -= 2
            if k == -1:
                cache[key] = True
                return cache[key]

            cache[key] = False
            return cache[key]

        if i == -1 and p[j] != '*':
            cache[key] = False
            return cache[key]

        if p[j] == '*':
            if backtrack(cache, s, p, i, j-2):
                cache[key] = True
                return cache[key]

            if p[j-1] == s[j] or p[j-1] == '.':
                if backtrack(cache, s, p, i-1, j):
                    cache[key] = True
                    return cache[key]

        if p[j] == '.' or s[i] == p[j]:
            if backtrack(cache, s, p, i-1, j-1):
                cache[key] = True
                return cache[key]

        cache[key] = False
        return cache[key]

    return backtrack({}, s, p, i, j)


def is_match_1(s: str, p: str) -> bool:
    s, p = ' ' + s, ' ' + p
    len_s, len_p = len(s), len(p)
    dp = [[0]*len_p for i in range(len_s)]
    dp[0][0] = 1

    for j in range(1, len_p):
        if p[j] == '*':
            dp[0][j] = dp[0][j-2]

    for i in range(1, len_s):
        for j in range(1, len_p):
            if p[j] in {s[i], '.'}:
                dp[i][j] = dp[i-1][j-1]
            elif p[j] == '*':
                dp[i][j] = dp[i][j-2] or int(dp[i-1][j] and p[j-1] in {s[i], '.'})

    return bool(dp[-1][-1])


def main():
    s = "aa"
    p = "a*"
    print(is_match_1(s, p))


if __name__ == "__main__":
    main()
