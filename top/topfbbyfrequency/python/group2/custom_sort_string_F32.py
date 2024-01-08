"""
You are given two strings order and s. All the characters of order are unique and were sorted in some custom
order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x
occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

Example:
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda"
are also valid outputs.

Tag: fb R32/50, 791/2927, R618/2936
"""


def custom_sort_string(order: str, s: str) -> str:
    rank = [26]*26

    for i in range(len(order)):
        rank[ord(order[i]) - ord('a')] = i
    return "".join(sorted(list(s), key=lambda x: rank[ord(x) - ord('a')]))


def main():
    order = "cba"
    s = "abcd"
    print("Custom sorted string: ", custom_sort_string(order, s))


if __name__ == "__main__":
    main()

"""
Idea:
*   There can only be 26 characters in the alphabet so if we can create a rank array of size 26 initially all 
    values as 26 rank = [26, 26, . . . . , 26]

*   We can rank all characters by giving them 0-25 Order and all characters that are not in Order string will have 
    their value as 26 so they will be concatenated in the end of sorted string

Time Complexity: O(M) + O(NlogN) ~ O(NlogN)
Space Complexity: O(26) ~ O(1)
"""