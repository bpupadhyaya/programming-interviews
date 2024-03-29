"""
An original string, consisting of lowercase English letters, can be encoded by the following steps:

- Arbitrarily split it into a sequence of some number of non-empty substrings.
- Arbitrarily choose some elements (possibly none) of the sequence, and replace each with its length
 (as a numeric string).
- Concatenate the sequence as the encoded string.

For example, one way to encode an original string "abcdefghijklmnop" might be:

- Split it as a sequence: ["ab", "cdefghijklmn", "o", "p"].
- Choose the second and third elements to be replaced by their lengths, respectively. The sequence
becomes ["ab", "12", "1", "p"].
- Concatenate the elements of the sequence to get the encoded string: "ab121p".
Given two encoded strings s1 and s2, consisting of lowercase English letters and digits 1-9 (inclusive),
return true if there exists an original string that could be encoded as both s1 and s2. Otherwise, return false.

Note: The test cases are generated such that the number of consecutive digits in s1 and s2 does not exceed 3.

Example 1:
Input: s1 = "internationalization", s2 = "i18n"
Output: true
Explanation: It is possible that "internationalization" was the original string.
- "internationalization"
  -> Split:       ["internationalization"]
  -> Do not replace any element
  -> Concatenate:  "internationalization", which is s1.
- "internationalization"
  -> Split:       ["i", "nternationalizatio", "n"]
  -> Replace:     ["i", "18",                 "n"]
  -> Concatenate:  "i18n", which is s2

Example 2:
Input: s1 = "a5b", s2 = "c5b"
Output: false
Explanation: It is impossible.
- The original string encoded as s1 must start with the letter 'a'.
- The original string encoded as s2 must start with the letter 'c'.

Tag: fb R45/50, 2060/2927, R1365/2936

"""


def possibly_equals(s1: str, s2: str) -> bool:
    def inner_1(s):
        ans = {int(s)}
        for i in range(1, len(s)):
            ans |= {x+y for x in inner_1(s[:i]) for y in inner_1(s[i:])}
        return ans

    def inner_2(i, j, diff):
        if i == len(s1) and j == len(s2):
            return diff == 0
        if i < len(s1) and s1[i].isdigit():
            ii = i
            while ii < len(s1) and s1[ii].isdigit():
                ii += 1
            for x in inner_1(s1[i:ii]):
                if inner_2(ii, j, diff-x):
                    return True
        elif j < len(s2) and s2[j].isdigit():
            jj = j
            while jj < len(s2) and s2[jj].isdigit():
                jj += 1
                for x in inner_1(s2[j:jj]):
                    if inner_2(i, jj, diff+x):
                        return True
        elif diff == 0:
            if i < len(s1) and j < len(s2) and s1[i] == s2[j]:
                return inner_2(i+1, j+1, 0)
        elif diff > 0:
            if i < len(s1):
                return inner_2(i+1, j, diff-1)
        else:
            if j < len(s2):
                return inner_2(i, j+1, diff+1)
        return False

    return inner_2(0, 0, 0)


def main():
    s1 = "internationalization"
    s2 = "i18n"
    print('Possibly equal? ', possibly_equals(s1, s2))


if __name__ == "__main__":
    main()


