"""
You are given an array words of size n consisting of non-empty strings.
We define the score of a string word as the number of strings words[i] such that word is a prefix of words[i].
For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of
both "ab" and "abc".
Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].
Note that a string is considered as a prefix of itself.

Example 1:
Input: words = ["abc","ab","bc","b"]
Output: [5,4,3,2]
Explanation: The answer for each string is the following:
- "abc" has 3 prefixes: "a", "ab", and "abc".
- There are 2 strings with the prefix "a", 2 strings with the prefix "ab", and 1 string with the prefix "abc".
The total is answer[0] = 2 + 2 + 1 = 5.
- "ab" has 2 prefixes: "a" and "ab".
- There are 2 strings with the prefix "a", and 2 strings with the prefix "ab".
The total is answer[1] = 2 + 2 = 4.
- "bc" has 2 prefixes: "b" and "bc".
- There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
The total is answer[2] = 2 + 1 = 3.
- "b" has 1 prefix: "b".
- There are 2 strings with the prefix "b".
The total is answer[3] = 2.

Example 2:
Input: words = ["abcd"]
Output: [4]
Explanation:
"abcd" has 4 prefixes: "a", "ab", "abc", and "abcd".
Each prefix has a score of one, so the total is answer[0] = 1 + 1 + 1 + 1 = 4.


Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists of lowercase English letters.

Tag: G46/50
"""


def sum_prefix_scores(words: list[str]) -> list[int]:
    d = dict()
    for i in words:
        s = ""
        for j in range(len(i)):
            s += i[j]
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
    l = []
    for i in words:
        c = 0
        s = ""
        for j in range(len(i)):
            s += i[j]
            c += d[s]
        l.append(c)
    return l


def sum_prefix_scores1(words: list[str]) -> list[int]:
    ws = dict()

    for word in words:
        buffer = ""
        for c in word:
            buffer += c
            if buffer not in ws:
                ws[buffer] = 0
            ws[buffer] += 1

    counts = [0] * len(words)
    for i, word in enumerate(words):
        buffer = ""
        for c in word:
            buffer += c
            if buffer in ws:
                counts[i] += ws[buffer]
    return counts


def main():
    words = ["abc", "ab", "bc", "b"]
    print(sum_prefix_scores1(words))


if __name__ == "__main__":
    main()
