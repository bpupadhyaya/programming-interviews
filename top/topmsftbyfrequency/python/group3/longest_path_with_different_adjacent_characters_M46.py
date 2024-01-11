"""
You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes
 numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the
  parent of node i. Since node 0 is the root, parent[0] == -1.
You are also given a string s of length n, where s[i] is the character assigned to node i.
Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same
 character assigned to them.

Example:
Input: parent = [-1,0,0,1,1,2], s = "abacbe"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters in the tree is the
 path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions.

Constraints:
n == parent.length == s.length
1 <= n <= 10^5
0 <= parent[i] <= n - 1 for all i >= 1
parent[0] == -1
parent represents a valid tree.
s consists of only lowercase English letters.

Tag: M46/50
"""


def longest_path(parent: list[int], s: str) -> int:
    t = {}
    for i in range(1, len(parent)):
        if parent[i] not in t:
            t[parent[i]] = [i]
        else:
            t[parent[i]].append(i)

    ans = 1

    def fun(i):
        nonlocal ans
        if i not in t:
            return 1
        res = 1
        for j in t[i]:
            length = fun(j)
            if s[i] != s[j]:
                ans = max(ans, length+res)
                res = max(res, length+1)
        return res

    fun(0)
    return ans


def main():
    parent = [-1, 0, 0, 1, 1, 2]
    s = "abacbe"
    print(longest_path(parent, s))


if __name__ == "__main__":
    main()
