"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Tag: 41/150
Tag: 290/2927, R815/2936 (overall frequency ranking)
"""


def word_pattern(pattern: str, s: str) -> bool:
    words, w_to_p = s.split(' '), dict()

    if len(pattern) != len(words):
        return False
    if len(set(pattern)) != len(set(words)):  # for the case w = ['dog', 'cat'] and p = 'aa'
        return False

    for i in range(len(words)):
        if words[i] not in w_to_p:
            w_to_p[words[i]] = pattern[i]
        elif w_to_p[words[i]] != pattern[i]:
            return False
    return True


def main():
    pattern = "abba"
    s = "dog cat cat dog"
    print(word_pattern(pattern, s))


if __name__ == "__main__":
    main()
