"""
You are given a 0-indexed string s that you must perform k replacement operations on. The replacement operations
are given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.
To complete the ith replacement operation:
Check if the substring sources[i] occurs at index indices[i] in the original string s.
If it does not occur, do nothing.
Otherwise if it does occur, replace that substring with targets[i].
For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this
 replacement will be "eeecd".
All replacement operations must occur simultaneously, meaning the replacement operations should not affect the
 indexing of each other. The testcases will be generated such that the replacements will not overlap.
For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not be generated because
 the "ab" and "bc" replacements overlap.
Return the resulting string after performing all replacement operations on s.

A substring is a contiguous sequence of characters in a string.

Example:
Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
Output: "eeebffff"
Explanation:
"a" occurs at index 0 in s, so we replace it with "eee".
"cd" occurs at index 2 in s, so we replace it with "ffff".

Tag: G31/50
"""


def find_replace_string(s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
    lookup = {i: (src, tgt) for i, src, tgt in zip(indices, sources, targets)}
    i, result = 0, ""
    while i < len(s):
        if i in lookup and s[i:].startswith(lookup[i][0]):
            result += lookup[i][1]
            i += len(lookup[i][0])
        else:
            result += s[i]
            i += 1
    return result


def main():
    s = "abcd"
    indices = [0, 2]
    sources = ["a", "cd"]
    targets = ["eee", "ffff"]
    print(find_replace_string(s, indices, sources, targets))


if __name__ == "__main__":
    main()
