"""
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has
 unique characters.
Return the maximum possible length of s.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing
 the order of the remaining elements.

Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Constraints:
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.

Tag: M40/50
"""


def max_length(arr: list[str]) -> int:
    uniq_elements = ['']
    maximum = 0
    for i in range(len(arr)):
        sz = len(uniq_elements)
        for j in range(sz):
            x = arr[i]+uniq_elements[j]
            if len(x) == len(set(x)):
                uniq_elements.append(x)
                maximum = max(maximum, len(x))
    return maximum


def main():
    arr = ["un", "iq", "ue"]
    print(max_length(arr))


if __name__ == "__main__":
    main()
