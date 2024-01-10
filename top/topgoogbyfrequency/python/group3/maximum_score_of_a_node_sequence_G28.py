"""
There is an undirected graph with n nodes, numbered from 0 to n - 1.
You are given a 0-indexed integer array scores of length n where scores[i] denotes the score of node i. You are
also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting
 nodes ai and bi.
A node sequence is valid if it meets the following conditions:
There is an edge connecting every pair of adjacent nodes in the sequence.
No node appears more than once in the sequence.
The score of a node sequence is defined as the sum of the scores of the nodes in the sequence.
Return the maximum score of a valid node sequence with a length of 4. If no such sequence exists, return -1.

Example:
Input: scores = [5,2,9,8,4], edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
Output: 24
Explanation: The figure above shows the graph and the chosen node sequence [0,1,2,3].
The score of the node sequence is 5 + 2 + 9 + 8 = 24.
It can be shown that no other node sequence has a score of more than 24.
Note that the sequences [3,1,2,0] and [1,0,2,3] are also valid and have a score of 24.
The sequence [0,3,2,4] is not valid since no edge connects nodes 0 and 3.

Constraints:
n == scores.length
4 <= n <= 5 * 10^4
1 <= scores[i] <= 108
0 <= edges.length <= 5 * 10^4
edges[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
There are no duplicate edges.

Tag: G28/50
"""
from collections import defaultdict
from heapq import nlargest, heappush, heappop


def maximum_score(scores: list[int], edges: list[list[int]]) -> int:
    # Note: incorrect output, debug and fix
    n = len(scores)
    G = [[] for i in range(n)]
    for i, j in edges:
        G[i].append([scores[j], j])
        G[j].append([scores[i], i])
    for i in range(n):
        G[i] = nlargest(3, G[i])

    res = -1
    for i, j in edges:
        for vii, ii in G[i]:
            for vjj, jj in G[j]:
                if ii != jj and ii != j and j != ii:
                    res = max(res, vii + vjj + scores[i] + scores[j])
    return res


def maximum_score1(scores: list[int], edges: list[list[int]]) -> int:
    g = defaultdict(list)
    for a, b in edges:
        heappush(g[a], (scores[b], b))
        if len(g[a]) > 3:
            heappop(g[a])
        heappush(g[b], (scores[a], a))
        if len(g[b]) > 3:
            heappop(g[b])

    ans = -1
    for a, b in edges:
        for s1, n1 in g[a]:
            if n1 == b:
                continue
            for s2, n2 in g[b]:
                if n2 == n1 or n2 == a:
                    continue
                ans = max(ans, scores[a] + scores[b] + s1 + s2)
    return ans


def main():
    scores = [5, 2, 9, 8, 4]
    edges = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
    print(maximum_score1(scores, edges))


if __name__ == "__main__":
    main()

"""
Explanation:
Intuition
We don't need to check all possible sequences,
but only some big nodes.


Explanation
For each edge (i, j) in edges,
we find a neighbour ii of node i,
we find a neighbour jj of node i,
If ii, i, j,jj has no duplicate, then that's a valid sequence.

Ad the intuition mentioned,
we don't have to enumerate all neighbours,
but only some nodes with big value.

But how many is enough?
I'll say 3.
For example, we have ii, i, j now,
we can enumerate 3 of node j biggest neighbour,
there must be at least one node different node ii and node i.

So we need to iterate all edges (i, j),
for each node we keep at most 3 biggest neighbour, which this can be done in O(3) or O(log3).


Complexity
Time O(n + m)
Space O(n + m)
"""