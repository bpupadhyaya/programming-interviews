"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once.

Example:
Input: s = "anagram", t = "nagaram"
Output: true

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

Tag: R42/145
"""
from collections import Counter


def is_anagram_using_sorting(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def is_anagram_using_hashtable(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in t:
        if char_count.get(char, 0) == 0:
            return False
        char_count[char] -= 1
    return True


def is_anagram_using_char_array(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    char_count_s = [0] * 26
    char_count_t = [0] * 26
    for char in s:
        char_count_s[ord(char) - ord('a')] += 1
    for char in t:
        char_count_t[ord(char) - ord('a')] += 1
    return char_count_s == char_count_t


def is_anagram_using_counter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


def main():
    s = "anagram"
    t = "nagaram"
    print(is_anagram_using_counter(s, t))


if __name__ == "__main__":
    main()

"""
Sorting:
Sort both strings.
Compare the sorted strings to check if they are equal.
Complexity:
Time Complexity: O(n log n) - Due to the sorting operation.
Space Complexity: O(1) - No extra space used other than the input strings.

Hash Table:
Create a hash table (dictionary) to store the frequency of characters in the first string.
Iterate through the second string and decrement the corresponding frequency in the hash table.
If the hash table becomes empty, the strings are anagrams.
Complexity:
Time Complexity: O(n) - Iterate through both strings.
Space Complexity: O(n) - Space required for the hash table.

Character Array:
Create two arrays of size 26 to represent the count of each character in the alphabet for both strings.
Iterate through both strings, updating the count in the arrays.
Compare the arrays to check if they are equal.
Complexity
Time Complexity: O(n) - Iterate through both strings.
Space Complexity: O(1) - Fixed-size character arrays.

Counter:
Use the Counter class from the collections module to get character counts for both strings.
Compare the Counters to check if they are equal.
Complexity
Time Complexity: O(n) - The Counter class internally iterates through the strings.
Space Complexity: O(n) - Space required for the Counters.

"""
