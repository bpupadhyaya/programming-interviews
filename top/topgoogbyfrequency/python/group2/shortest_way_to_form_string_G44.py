"""
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence
 of "abcde" while "aec" is not).
Given two strings source and target, return the minimum number of subsequences of source such that their concatenation
 equals target. If the task is impossible, return -1.



Example 1:
Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

Constraints:
1 <= source.length, target.length <= 1000
source and target consist of lowercase English letters.

Tag: G44/50
"""


def shortest_way(source: str, target: str) -> int:
    i, minimum = 0, 1

    for c in target:
        # Get leftmost char after previously matched index
        i = source.find(c, i)
        # If not found
        if i == -1:
            # Get leftmost char from beginning of string and increase number of concatenated string
            i = source.find(c)
            minimum += 1
            # if not found, then target can't be formed. Return -1
            if i == -1:
                return i
        i += 1

    return minimum


def shortest_way1(source: str, target: str) -> int:
    for t in target:
        if t not in source:
            return -1

    result = 1
    i, j = 0, 0

    while i < len(target):
        if j >= len(source):
            j = 0
            result += 1
        if target[i] == source[j]:
            i += 1
        j += 1

    return result


def main():
    source = "abc"
    target = "abcbc"
    print(shortest_way1(source, target))


if __name__ == "__main__":
    main()
