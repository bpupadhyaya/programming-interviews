"""
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the
 string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Example:
Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Constraints:
1 <= s.length <= 10^5
s contains only lowercase English letters.

Tag: M8/50
"""
from collections import Counter


def min_deletions(s: str) -> int:
    chars = Counter(s)

    freq_set = set()
    count = 0

    for freq in chars.values():
        while freq > 0 and freq in freq_set:
            freq -= 1
            count += 1

        freq_set.add(freq)

    return count


def min_deletions1(s: str) -> int:
    freq = [0] * 26  # Create a list to store character frequencies
    for c in s:
        freq[ord(c) - ord('a')] += 1  # Count the frequency of each character

    freq.sort()  # Sort frequencies in ascending order
    del_count = 0  # Initialize the deletion count

    for i in range(24, -1, -1):
        if freq[i] == 0:
            break  # No more characters with this frequency

        if freq[i] >= freq[i + 1]:
            prev = freq[i]
            freq[i] = max(0, freq[i + 1] - 1)
            del_count += prev - freq[i]  # Update the deletion count

    return del_count  # Return the minimum deletions required


def main():
    s = "aaabbbcc"
    print(min_deletions1(s))


if __name__ == "__main__":
    main()
