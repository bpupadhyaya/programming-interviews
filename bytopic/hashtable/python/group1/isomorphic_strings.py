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


def is_isomorphic_one_liner(s: str, t: str) -> bool:
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


def is_isomorphic_using_hashmap(s: str, t: str) -> bool:
    dic1, dic2 = {}, {}
    for s1, t1 in zip(s, t):
        if (s1 in dic1 and dic1[s1] != t1) or (t1 in dic2 and dic2[t1] != s1):
            return False
        dic1[s1] = t1
        dic2[t1] = s1
    return True


def main():
    s = "egg"
    t = "add"
    print(is_isomorphic_using_hashmap(s, t))


if __name__ == "__main__":
    main()
