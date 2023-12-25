"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or
move outside the boundary (i.e., wrap-around is not allowed).

Example:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 2^{31} - 1

R99/145
"""


def longest_increasing_path(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for i in range(rows)]

    def dfs(i, j):
        if not dp[i][j]:
            val = matrix[i][j]
            dp[i][j] = 1 + max(
                dfs(i-1, j) if i and val > matrix[i-1][j] else 0,
                dfs(i+1, j) if i < rows - 1 and val > matrix[i+1][j] else 0,
                dfs(i, j-1) if j and val > matrix[i][j-1] else 0,
                dfs(i, j+1) if j < cols - 1 and val > matrix[i][j+1] else 0
            )
        return dp[i][j]
    for r in range(rows):
        for c in range(cols):
            dfs(r, c)
    return max(max(x) for x in dp)


def longest_increasing_path_1(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    memo = [[0]*n for _ in range(m)]   # memoization matrix to store the length of the longest increasing path
    # starting from each cell
    res = 0   # maximum length of the increasing path found so far

    # DFS function to find the length of the longest increasing path starting from the current cell
    def dfs(i, j):
        if memo[i][j]:
            return memo[i][j]
        path = 1   # length of the increasing path starting from the current cell
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:   # explore all four directions (right, left, down, up)
            if 0 <= i+x < m and 0 <= j+y < n and matrix[i+x][j+y] > matrix[i][j]:   # if the neighbor has a
                # greater value, move to it
                path = max(path, 1 + dfs(i+x, j+y))   # update the length of the increasing path
        memo[i][j] = path   # memoize the length of the increasing path starting from the current cell
        return path

    for i in range(m):
        for j in range(n):
            res = max(res, dfs(i, j))   # update the maximum length of the increasing path found so far
    return res


def main():
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    print(longest_increasing_path_1(matrix))


if __name__ == "__main__":
    main()

"""
longest_increasing_path_1 explanation:
The problem can be solved by performing a depth-first search (DFS) on each cell of the matrix and keeping track of 
the longest increasing path found so far. We start the search from each cell of the matrix and for each cell, 
we move in all four directions (left, right, up, and down) to find the increasing path. We use memoization to store
 the length of the longest increasing path starting from each cell to avoid recomputing it.

Step-by-step algorithm:

Create a memoization matrix of the same size as the input matrix to store the length of the longest increasing path 
starting from each cell.
For each cell in the matrix, perform a DFS to find the length of the longest increasing path starting from that cell.
During the DFS, for each unvisited neighbor of the current cell that has a greater value, perform a DFS on that 
neighbor and update the memoization matrix with the length of the longest increasing path starting from that neighbor.
If we have already computed the length of the longest increasing path starting from a neighbor, we can use that 
value from the memoization matrix instead of recomputing it.
During the DFS, keep track of the maximum length of the increasing path found so far and return it as the result.
Time Complexity: O(mn), where m and n are the dimensions of the matrix, as we perform a DFS starting from each 
cell of the matrix, and each cell is visited only once.

Space Complexity: O(mn), for the memoization matrix used to store the length of the longest increasing path 
starting from each cell.
"""