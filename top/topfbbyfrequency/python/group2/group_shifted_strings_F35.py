"""
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings 'strings', group all strings[i] that belong to the same shifting sequence. You may
return the answer in any order.

Example 1:
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
Example 2:

Input: strings = ["a"]
Output: [["a"]]

Constraints:
1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.

"""
import collections


def group_strings(strings: list[str]) -> list[list[str]]:
    groups = collections.defaultdict(list)
    for s in strings:
        pattern = ()
        for i in range(1, len(s)):
            pattern = pattern + ((ord(s[i]) - ord(s[i-1]) + 26) % 26,)
        groups[pattern].append(s)
    return groups.values()


def main():
    strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    print(group_strings(strings))


if __name__ == "__main__":
    main()
