"""
You are given a string s and an array of strings words. All the strings of words are of the same length.
A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.
For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are
all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any
permutation of words.
Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

Example:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.

Tag: 32/150
Tag: 30/2927, R468/2936 (overall frequency ranking)
"""
from collections import Counter, defaultdict


def find_substring(s: str, words: list[str]) -> list[int]:
    """
    Time:   O(n*k), n = length of s, k = length of each word
    Memory: O(m*k), m = length of words, k = length of each word
    """
    length = len(words[0])
    word_count = Counter(words)
    indices = []
    for i in range(length):
        start = i
        window = defaultdict(int)
        words_used = 0
        for j in range(i, len(s) - length + 1, length):
            word = s[j:j + length]
            if word not in word_count:
                start = j + length
                window = defaultdict(int)
                words_used = 0
                continue
            words_used += 1
            window[word] += 1
            while window[word] > word_count[word]:
                window[s[start: start + length]] -= 1
                start += length
                words_used -= 1
            if words_used == len(words):
                indices.append(start)
    return indices


def main():
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(find_substring(s, words))


if __name__ == "__main__":
    main()
