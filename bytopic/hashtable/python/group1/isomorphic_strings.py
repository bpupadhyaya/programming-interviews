"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
Example 2:
Input: s = "foo", t = "bar"
Output: false
Example 3:
Input: s = "paper", t = "title"
Output: true

Tag: 40/150
Tag: 205/2927, R438/2936 (overall frequency ranking)
"""


def is_isomorphic(s: str, t: str) -> bool:
    map1 = []
    map2 = []
    for idx in s:
        map1.append(s.index(idx))
    for idx in t:
        map2.append(t.index(idx))
    if map1 == map2:
        return True
    return False


def main():
    s = "egg"
    t = "add"
    print(is_isomorphic(s, t))


if __name__ == "__main__":
    main()
