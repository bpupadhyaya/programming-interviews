"""
Given an m x n 2D binary grid 'grid' which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Tag: 200/2927 , R23/2935 , R3/50 (amz)
"""

import collections


def num_island_dfs(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    ans = 0

    def dfs(i, j):
        grid[i][j] = '2'
        for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
            ii, jj = i+di, j+dj
            if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == '1':
                dfs(ii, jj)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                dfs(i, j)
                ans += 1
    return ans


def num_island_bfs(grid: list[list[str]])  -> int:
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                q = collections.deque([(i, j)])
                grid[i][j] = '2'
                while q:
                    x, y = q.popleft()
                    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                        xx, yy = x + dx, y+dy
                        if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == '1':
                            q.append((xx, yy))
                            grid[xx][yy] = '2'
                ans += 1
    return ans


class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.n = n
        self.size = n

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.size -= 1
            self.p[pj] = pi

    def find(self, i):
        if i != self.p[i]:
            self.p[i] = self.find(self.p[i])
        return self.p[i]


def num_island_union_find(grid: list[list[str]])  -> int:
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    d = dict()
    idx = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                d[i, j] = idx
                idx += 1
    uf = UF(idx)
    for i in range(m):
        for j in range(m):
            if grid[i][j] == '1':
                if i > 0 and grid[i-1][j] == '1':
                    uf.union(d[i-1, j], d[i, j])
                if j > 0 and grid[i][j-1] == '1':
                    uf.union(d[i, j-1], d[i, j])
    return uf.size


def main():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print('Number of islands: ', num_island_union_find(grid))


if __name__ == "__main__":
    main()

"""
STEPS:
DFS:
- Iterate over the matrix and DFS at each point whenever a point is land (1)
- Mark visited as 2 to avoid revisit
- Increment ans each time need to do a DFS (original, not recursive)

BFS:
- Iterate over the matrix and BFS at each point whenever a point is land (1)
- Mark visited as 2 to avoid revisit
- Increment ans each time need to do a BFS (original, not recursive)

Union Find:
- Create dictionary d[(i,j)] = idx, give (x,y) an id number, for eaiser union find
- Create a Union Find object with length of number of "1" (say length is n or size)
- Iterate over matrix, from left to right, from top to bottom
    - Union current and left or right, if they are both 1
    - For each union, decrement size
- Return size
"""