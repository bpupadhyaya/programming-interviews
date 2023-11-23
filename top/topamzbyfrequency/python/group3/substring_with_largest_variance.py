"""
The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters
present in the string. Note the two characters may or may not be the same.
Given a string s consisting of lowercase English letters only, return the largest variance possible among all
substrings of s.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "aababbb"
Output: 3
Explanation:
All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.

Example 2:
Input: s = "abcde"
Output: 0
Explanation:
No letter occurs more than once in s, so the variance of every substring is 0.

Tag: 2272/2927 , R139/2935 , R11/50 (amz)
"""


def largest_variance(s: str) -> int:
    count1 = 0
    count2 = 0
    max_variance = 0

    # Create distinct list of character pairs
    pairs = [(l1, l2) for l1 in set(s) for l2 in set(s) if l1 != l2]

    # Run once for original string order, then again for reverse string order
    for nums in range(2):
        for pair in pairs:
            count1 = count2 = 0
            for letter in s:
                # No reason to process letters that aren't part of the current pair
                if letter not in pair:
                    continue
                if letter == pair[0]:
                    count1 += 1
                elif letter == pair[1]:
                    count2 += 1
                if count1 < count2:
                    count1 = count2 = 0
                elif count1 > 0 and count2 > 0:
                    max_variance = max(max_variance, count1 - count2)

        # Reverse the string for the second time around
        s = s[::-1]

    return max_variance


def main():
    s = "aababbb"
    print(largest_variance(s))


if __name__ == "__main__":
    main()