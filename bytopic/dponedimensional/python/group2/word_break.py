"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a
space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Sample 1:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Soln: dynamic programming

Tag: 139/150
Tag: 139/2927, R121/2936 (overall frequency ranking)
Note: Wrong output, debug and fix it.
"""


def word_break(s: str, word_dict: list[str]) -> bool:
    dp = [True] + [False] * len(s)

    for i in range(1, len(s) + 1):
        for w in word_dict:
            if i - len(w) >= 0 and dp[i - len(w)] and s[:i].endswith(w):
                dp[i] = True
                break
    return dp[-1]


def main():
    s = "applepenapple",
    word_dict = ["apple", "pen"]
    print(word_break(s, word_dict))


if __name__ == "__main__":
    main()
