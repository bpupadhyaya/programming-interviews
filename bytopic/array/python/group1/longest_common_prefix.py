"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Tag: 20/150
Tag: 14/2927, R13/2936 (overall frequency ranking)
"""


def longest_common_prefix(input_: list[str]) -> str:
    ans = ""
    input_ = sorted(input_)
    first = input_[0]
    last = input_[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]
    return ans


def main():
    input_ = ["flower", "flow", "flight"]
    print(longest_common_prefix(input_))


if __name__ == "__main__":
    main()
