"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Tag: 42/150
Tag: 242/2927, R86/2936 (overall frequency ranking)
"""


def is_anagram(s: str, t: str) -> bool:
    count = [0] * 26
    # Count the frequency of characters in string s
    for x in s:
        count[ord(x) - ord('a')] += 1

    # Decrement the frequency of characters in string t
    for x in t:
        count[ord(x) - ord('a')] -= 1

    # Check if any character is non-zero frequency
    for val in count:
        if val != 0:
            return False
    return True


def main():
    s = "anagram"
    t = "nagaram"
    print(is_anagram(s, t))


if __name__ == "__main__":
    main()
