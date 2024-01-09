"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.

Sample 1:
Input: grid = [
 ["1","1","0","0","0"],
 ["1","1","0","0","0"],
 ["0","0","1","0","0"],
 ["0","0","0","1","1"]
]
Output: 3

Tag: 89/150
Tag: 200/2927, R23/2936 (overall frequency ranking)
"""


def num_islands(grid: list[list[str]]) -> int:
    count = 0

    def dfs(grid_, i, j):
        grid_[i][j] = 0
        for dr, dc in (1, 0), (-1, 0), (0, -1), (0, 1):
            r = i + dr
            c = j + dc
            if 0 <= r < len(grid_) and 0 <= c < len(grid_[0]) and grid_[r][c] == '1':
                dfs(grid_, r, c)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                # print(i, j)
                dfs(grid, i, j)
                count += 1
    return count


def main():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(num_islands(grid))


if __name__ == "__main__":
    main()
