"""
The appeal of a string is the number of distinct characters found in the string.
- For example, the appeal of "abbca" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.

Given a string s, return the total appeal of all of its substrings.
A substring is a contiguous sequence of characters within a string.

Example:
Input: s = "code"
Output: 20
Explanation: The following are the substrings of "code":
- Substrings of length 1: "c", "o", "d", "e" have an appeal of 1, 1, 1, and 1 respectively. The sum is 4.
- Substrings of length 2: "co", "od", "de" have an appeal of 2, 2, and 2 respectively. The sum is 6.
- Substrings of length 3: "cod", "ode" have an appeal of 3 and 3 respectively. The sum is 6.
- Substrings of length 4: "code" has an appeal of 4. The sum is 4.
The total sum is 4 + 6 + 6 + 4 = 20.

Tag: 2262/2927 , R1857/2935 , R45/50 (amz)
"""
from collections import defaultdict


def appeal_sum(s: str) -> int:
    res, cur, prev = 0, 0, defaultdict(lambda: -1)  # lambda: -1 defines an anonymous function that takes
    # no arguments and returns the value -1.
    for i, ch in enumerate(s):
        cur += i - prev[ch]
        prev[ch] = i
        res += cur
    return res


def main():
    s = "code"
    print(appeal_sum(s))


if __name__ == "__main__":
    main()
