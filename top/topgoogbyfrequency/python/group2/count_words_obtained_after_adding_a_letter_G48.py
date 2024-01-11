"""
You are given two 0-indexed arrays of strings startWords and targetWords. Each string consists of lowercase English
 letters only.
For each string in targetWords, check if it is possible to choose a string from startWords and perform a conversion
 operation on it to be equal to that from targetWords.
The conversion operation is described in the following two steps:

Append any lowercase letter that is not present in the string to its end.
For example, if the string is "abc", the letters 'd', 'e', or 'y' can be added to it, but not 'a'. If 'd' is added,
 the resulting string will be "abcd".
Rearrange the letters of the new string in any arbitrary order.
For example, "abcd" can be rearranged to "acbd", "bacd", "cbda", and so on. Note that it can also be rearranged to
 "abcd" itself.
Return the number of strings in targetWords that can be obtained by performing the operations on any string of
 startWords.

Note that you will only be verifying if the string in targetWords can be obtained from a string in startWords by
 performing the operations. The strings in startWords do not actually change during this process.



Example 1:
Input: startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"]
Output: 2
Explanation:
- In order to form targetWords[0] = "tack", we use startWords[1] = "act", append 'k' to it, and rearrange "actk"
 to "tack".
- There is no string in startWords that can be used to obtain targetWords[1] = "act".
  Note that "act" does exist in startWords, but we must append one letter to the string before rearranging it.
- In order to form targetWords[2] = "acti", we use startWords[1] = "act", append 'i' to it, and rearrange "acti"
 to "acti" itself.

1 <= startWords.length, targetWords.length <= 5 * 104
1 <= startWords[i].length, targetWords[j].length <= 26
Each string of startWords and targetWords consists of lowercase English letters only.
No letter occurs more than once in any string of startWords or targetWords.

Tag: G48/50
"""


def word_count(start_words: list[str], target_words: list[str]) -> int:
    d = {}
    for i in start_words:
        x = "".join(sorted(i))
        d[x] = 1

    ans = 0
    for i in target_words:
        i = "".join(sorted(i))
        for j in range(len(i)):
            x = i[:j]+i[j+1:]
            if x in d:
                ans += 1
                break
    return ans


def main():
    start_words = ["ant", "act", "tack"]
    target_words = ["tack", "act", "acti"]
    print(word_count(start_words, target_words))


if __name__ == "__main__":
    main()

