"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of
the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

Example:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

R111/145
"""


def num_decodings(s: str) -> int:
    if s == "0":
        return 0
    dp_2 = 1
    dp_1 = int(s[-1] != "0")
    i = len(s) - 2
    while i >= 0:
        if s[i] == "0":
            dp_0 = 0
        else:
            dp_0 = dp_1
            if s[i] == "1" or (s[i] == "2" and int(s[i + 1]) < 7):
                dp_0 += dp_2
        i -= 1
        dp_0, dp_1, dp_2 = 0, dp_0, dp_1
    return dp_1


def main():
    s = "226"
    print(num_decodings(s))


if __name__ == "__main__":
    main()

"""
Complexity:
Time: O(N)
Space: O(1)
"""
