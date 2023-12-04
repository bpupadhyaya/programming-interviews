"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes
the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Note: Visualize to understand

Tag: 143/150
Tag: 64/2927, R375/2936 (overall frequency ranking)
"""


def min_path_sum(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]


def main():
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(min_path_sum(grid))


if __name__ == "__main__":
    main()
