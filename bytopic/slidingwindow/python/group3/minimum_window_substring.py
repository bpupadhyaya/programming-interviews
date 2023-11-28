"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring
of s such that every character in t (including duplicates) is included in the window. If there is no such
substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Tag: 33/150
Tag: 76/2927, R181/2936 (overall frequency ranking)
"""
import collections


def min_window(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""
    need_str = collections.defaultdict(int)
    for ch in t:
        need_str[ch] += 1
    need_cnt = len(t)
    res = (0, float('inf'))
    start = 0
    for end, ch in enumerate(s):
        if need_str[ch] > 0:
            need_cnt -= 1
        need_str[ch] -= 1
        if need_cnt == 0:
            while True:
                tmp = s[start]
                if need_str[tmp] == 0:
                    break
                need_str[tmp] += 1
                start += 1
            if end - start < res[1] - res[0]:
                res = (start, end)
            need_str[s[start]] += 1
            need_cnt += 1
            start += 1
    return '' if res[1] > len(s) else s[res[0]:res[1]+1]


def main():
    s = "ADOBECODEBANC"
    t = "ABC"
    print(min_window(s, t))


if __name__ == "__main__":
    main()
