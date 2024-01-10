"""
Two strings, X and Y, are considered similar if either they are identical or we can make them equivalent by swapping
 at most two letters (in distinct positions) within the string X.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but
 "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars"
and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in
 the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How
many groups are there?


Example 1:
Input: strs = ["tars","rats","arts","star"]
Output: 2

Constraints:
1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.
"""


class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        if self.par[node] != node:
            self.par[node] = self.find(self.par[node])
        return self.par[node]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if self.rank[px] > self.rank[py]:  # py to px
            self.rank[px] += self.rank[py]
            self.par[py] = px
        else:  # px to py
            self.rank[py] += self.rank[px]
            self.par[px] = py


def num_similar_groups(strs: list[str]) -> int:
    ls = len(strs)
    dsu = DSU(ls)

    for i in range(ls):

        for j in range(i + 1, ls):
            if dsu.par[i] == dsu.par[j]:  # same group
                continue

            diff = 0
            for k in range(len(strs[0])):
                if strs[i][k] != strs[j][k]:
                    diff += 1
                    if diff > 2:  # not same group
                        break
            if diff <= 2:
                dsu.union(i, j)

    for i in range(ls):
        dsu.find(i)

    return len(set(dsu.par))


def main():
    strs = ["tars", "rats", "arts", "star"]
    print(num_similar_groups(strs))


if __name__ == "__main__":
    main()

"""
Note from internet:
Intuition
The word "group" in description -> think about DSU is good intuition.

Optimize:
skip checking if you know 2 strings are already in the same group
if >2 letter differences are found between 2 strings, stop checking because they are not the same group

"""
