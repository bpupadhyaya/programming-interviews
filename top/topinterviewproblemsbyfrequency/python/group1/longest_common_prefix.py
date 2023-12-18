"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Tag: R10/145
"""


def longest_common_prefix(strs: list[str]) -> str:
    ans = ""
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]
    return ans


def main():
    strs = ["flower", "flow", "flight"]
    print(longest_common_prefix(strs))


if __name__ == "__main__":
    main()


"""
Algo:
Initialize an empty string ans to store the common prefix.
Sort the input list v lexicographically. This step is necessary because the common prefix should be common to 
all the strings, so we need to find the common prefix of the first and last string in the sorted list.
Iterate through the characters of the first and last string in the sorted list, stopping at the length of 
the shorter string.
If the current character of the first string is not equal to the current character of the last string, return 
the common prefix found so far.
Otherwise, append the current character to the ans string.
Return the ans string containing the longest common prefix.

Note that the code assumes that the input list v is non-empty, and that all the strings in v have at least one 
character. If either of these assumptions is not true, the code may fail.
"""