"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the
letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "aa", magazine = "aab"
Output: true
Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Tag: 39/150
Tag: 383/2927, R502/2936 (overall frequency ranking)
"""
from collections import Counter


def can_construct(ransom_note: str, magazine: str) -> bool:
    st1, st2 = Counter(ransom_note), Counter(magazine)
    if st1 & st2 == st1:
        return True
    return False


def main():
    ransom_note = "aa"
    magazine = "ab"
    print(can_construct(ransom_note, magazine))


if __name__ == "__main__":
    main()
