"""
Given a string s and an integer k, return the length of the longest  substring of s that contains at most k distinct
 characters.

Example:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Constraints:
1 <= s.length <= 5 * 10^4
0 <= k <= 50

R130/145
"""
from collections import Counter


def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    freq = Counter()
    window_start = 0
    longest_valid_substring_seen = 0
    for window_end, char in enumerate(s):
        # load up the frequency counter until constraint violation
        freq[char] += 1
        # shrink the window if violates the constraint of more than the number of distinct characters
        # the length of the freq counter represents the number of distinct characters
        while len(freq) > k:
            # get the left char of the window (the char that window_start points to)
            left_char = s[window_start]
            # and decrement it in the counter
            freq[left_char] -= 1
            # we check the length of the frequency counter (which is equivalent to number of distinct chars)
            # we must delete chars that have a zero count, because we no longer have a distinct char in window
            if freq[left_char] == 0:
                del freq[left_char]
            # shrink window here
            window_start += 1
        # valid window at this point, get the size of the window
        # and compare it to the longest valid substring seen so far
        # update longest_valid_substring_seen if we found a new longest valid substring
        window_size = window_end - window_start + 1
        longest_valid_substring_seen = max(longest_valid_substring_seen, window_size)
    return longest_valid_substring_seen


def length_of_longest_substring_k_distinct_1(s: str, k: int) -> int:
    ln = len(s)
    if ln == 0:
        return 0
    # to hold chars from the s so that I know that I have only two distinct characters
    dct = {}
    j = 0
    max_window = 0
    count = 0
    for i in range(ln):
        dct[s[i]] = dct.get(s[i], 0) + 1
        if dct[s[i]] == 1:
            count += 1
        while count > k:
            dct[s[j]] -= 1
            if dct[s[j]] == 0:
                count -= 1
            j += 1
        max_window = max(max_window, i - j + 1)
    return max_window


def main():
    s = "eceba"
    k = 2
    print(length_of_longest_substring_k_distinct(s, k))


if __name__ == "__main__":
    main()

"""
length_of_longest_substring_k_distinct_1 explanation:
# keep a map/dictionary to keep count of different type of characters
# if we add a character and it's count is 1 that means we have added a new char right?
# so we increase the count by 1
# now, we have a limit on count(distinct chars) as k this case
# so we will see if my window has count less than or equal to the 2, if yes, then we will
# find the size of that window.
# otherwise, we will shrink my window
# If we remove a char and if its count becomes 0 that means, we have removed a distinct char right?
# so we will decrease my count by 1
"""