"""
Given a list of strings dict where all the strings are of the same length.
Return true if there are 2 strings that only differ by 1 character in the same index, otherwise return false.

Example 1:
Input: dict = ["abcd","acbd", "aacd"]
Output: true
Explanation: Strings "abcd" and "aacd" differ only by one character in the index 1.

Example 2:
Input: dict = ["ab","cd","yz"]
Output: false

Example 3:
Input: dict = ["abcd","cccc","abyd","abab"]
Output: true

Constraints:
The number of characters in dict <= 105
dict[i].length == dict[j].length
dict[i] should be unique.
dict[i] contains only lowercase English letters.

Follow up: Could you solve this problem in O(n * m) where n is the length of dict and m is the length of each string.

Tag: G42/50
"""


def differ_by_one(dict_: list[str]) -> bool:
    # Complexity: O(m^2 n)
    seen = set()
    for word in dict_:
        for i in range(len(word)):
            key = word[:i] + "*" + word[i+1:]
            if key in seen:
                return True
            seen.add(key)
    return False


def differ_by_one1(dict_: list[str]) -> bool:
    # Complexity: O(mn)
    MOD = 1_000_000_007
    hs = []
    for word in dict_:
        val = 0
        for ch in word:
            val = (26*val + ord(ch) - 97) % MOD
        hs.append(val)

    mult = 1
    for j in reversed(range(len(dict_[0]))):
        seen = {}
        for i, w in enumerate(dict_):
            val = (hs[i] - (ord(w[j]) - 97) * mult) % MOD
            if val in seen:
                for ww in seen[val]:
                    if sum(x != xx for x, xx in zip(w, ww)) == 1:
                        return True
            seen.setdefault(val, []).append(w)
        mult = 26 * mult % MOD
    return False


def main():
    dict_ = ["abcd", "cccc", "abyd", "abab"]
    print(differ_by_one(dict_))


if __name__ == "__main__":
    main()
