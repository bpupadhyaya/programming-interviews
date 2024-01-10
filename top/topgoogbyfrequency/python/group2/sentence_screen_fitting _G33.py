"""
Given a rows x cols screen and a sentence represented as a list of strings, return the number of times the given
 sentence can be fitted on the screen.
The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space
 must separate two consecutive words in a line.

Example 1:
Input: sentence = ["hello","world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.

Constraints:
1 <= sentence.length <= 100
1 <= sentence[i].length <= 10
sentence[i] consists of lowercase English letters.
1 <= rows, cols <= 2 * 10^4
"""
from bisect import bisect_right


def words_typing(sentence: list[str], rows: int, cols: int) -> int:
    prefix = [0]
    for x in sentence:
        prefix.append(prefix[-1] + len(x) + 1)

    ans = j = 0
    for i in range(rows):
        n = prefix[-1] - prefix[j]
        if n > cols+1:
            j = bisect_right(prefix, prefix[j]+cols+1)-1
        elif n <= cols+1:
            q, r = divmod(cols+1-n, prefix[-1])
            ans += 1+q
            j = bisect_right(prefix, r)-1
    return ans


def main():
    sentence = ["hello", "world"]
    rows = 2
    cols = 8
    print(words_typing(sentence, rows, cols))


if __name__ == "__main__":
    main()
