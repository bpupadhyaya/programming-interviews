"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word
is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Tag: 140/2927 , R331/2935 , R12/50 (amz)
"""

from collections import defaultdict


def word_break(s: str, word_dict: list[str]) -> list[str]:
    def fun(s, dc, memo):
        if s in memo:
            return memo[s]
        ans = []
        if dc[s] == 1:
            ans = [s]
        for i in range(1, len(s)):
            if dc[s[:i]] == 1:
                a = fun(s[i:], dc, memo)
                for x in a:
                    ans.append(s[:i] + " " + x)
        memo[s] = ans
        return ans

    dc = defaultdict(lambda:0)
    for a in word_dict:
        dc[a] = 1
    return fun(s, dc, {})


def main():
    s = "catsanddog"
    word_dict = ["cat", "cats", "and", "sand", "dog"]
    print(word_break(s, word_dict))


if __name__ == "__main__":
    main()
