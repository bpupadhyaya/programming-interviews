"""
Given an m x n 2D binary grid 'grid' which represents a map of '1's (land) and '0's (water), return the
number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.

Example:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

Tag: R20/145
"""


def num_island(grid: list[list[str]]) -> int:
    def dfs(g, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or g[i][j] == '0':
            return
        g[i][j] = '0'
        dfs(g, i-1, j, m, n)
        dfs(g, i+1, j, m, n)
        dfs(g, i, j-1, m, n)
        dfs(g, i, j+1, m, n)

    if grid is None:
        return 0
    m = len(grid)
    if m == 0:
        return 0
    n = len(grid[0])
    if n == 0:
        return 0
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                ans += 1
                dfs(grid, i, j, m, n)
    return ans


def main():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print(num_island(grid))


if __name__ == "__main__":
    main()


"""
Intuition
Imagine grid as graph with edges from "1" cells to all adjacent (max 4) cells and DFS to find number of 
connected components = Ans

Approach
Iterate through the grid
DFS for each cell with "1" and increment answer counter
Mark cell "0" in dfs calls to mark them visited

Complexity
Time complexity:
O(m*n) where m, n is size of grid
Space complexity:
O(1) not using any space using same input grid to capture visited cells.
"""
