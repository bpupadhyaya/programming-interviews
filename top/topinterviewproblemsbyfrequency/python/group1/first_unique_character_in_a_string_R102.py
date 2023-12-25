"""
First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example:
Input: s = "lovelyday"
Output: 1

Constraints:
1 <= s.length <= 10^5
s consists of only lowercase English letters.

R102/145
"""
import collections


def first_unique_char(s: str) -> int:
    hset = collections.Counter(s)
    for idx in range(len(s)):
        # If the count is equal to 1, it is the first distinct character in the list.
        if hset[s[idx]] == 1:
            return idx
    return -1


def first_unique_char_0(s: str) -> int:
    for i, c in enumerate(s):
        if s.count(c) == 1:
            return i
            break
    return -1


def first_unique_char_0_1(s: str) -> int:
    dic = {}
    seen = set()
    for i, c in enumerate(s):
        if c not in seen:
            dic[c] = i
            seen.add(c)
        elif c in dic:
            del dic[c]
    return min(dic.values()) if dic else -1


def first_unique_iterative(s: str) -> int:
    for i in range(len(s)):
        if s[i] not in s[:i] and s[i] not in s[i+1:]:
            return i
    return -1


def first_unique_inefficient(s: str) -> int:
    frequency = {}
    for char in s:
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] = frequency[char] + 1
    for index in range(len(s)):
        if frequency[s[index]] == 1:
            return index
    return -1


def main():
    s = "lovelyday"
    print(first_unique_inefficient(s))


if __name__ == "__main__":
    main()
