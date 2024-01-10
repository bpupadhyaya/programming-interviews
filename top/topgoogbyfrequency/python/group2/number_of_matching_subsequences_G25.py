"""
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".

Example 1:
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

Constraints:
1 <= s.length <= 5 * 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.

Tag: G25/50
"""


def num_matching_subseq(s: str, words: list[str]) -> int:
    def sub(st):
        pos = -1
        for char in st:
            pos = s.find(char, pos+1)
            if pos == -1:
                return False
        return True
    return sum(map(sub, words))


def num_matching_subseq1(s: str, words: list[str]) -> int:
    def is_sub(word_):
        index = -1
        for ch in word_:
            index = s.find(ch, index+1)
            if index == -1:
                return False
        return True

    c = 0
    for word in words:
        if is_sub(word):
            c += 1

    return c


def main():
    s = "abcde"
    words = ["a", "bb", "acd", "ace"]
    print(num_matching_subseq1(s, words))


if __name__ == "__main__":
    main()
