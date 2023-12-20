"""
Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Tag: R8/145
"""


def length_of_longest_substring(s: str) -> int:
    n = len(s)
    max_length = 0
    char_index = [-1] * 128
    left = 0

    for right in range(n):
        if char_index[ord(s[right])] >= left:
            left = char_index[ord(s[right])] + 1
        char_index[ord(s[right])] = right
        max_length = max(max_length, right - left + 1)
    return max_length


def main():
    s = "pwwkew"
    print(length_of_longest_substring(s))


if __name__ == "__main__":
    main()

"""
Algo:
We iterate through the string using the right pointer.
We check if the current character has occurred within the current substring by comparing its index in charIndex 
with left.
If the character has occurred, we move the left pointer to the next position after the last occurrence of the character.
We update the index of the current character in charIndex.
At each step, we update the maxLength by calculating the length of the current substring.
We continue the iteration until reaching the end of the string.
Finally, we return the maxLength as the length of the longest substring without repeating characters.

"""
