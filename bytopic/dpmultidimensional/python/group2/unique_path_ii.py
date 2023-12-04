"""
You are given an m x n integer array grid. There is a robot initially located at the top-left
corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot
include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 10^9.

Sample 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Note: Visualize to understand
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Tag: 144/150
Tag: 63/2927, R308/2936 (overall frequency ranking)
"""


def unique_paths_with_obstacles(obstacle_grid: list[list[int]]) -> int:
    if not obstacle_grid or not obstacle_grid[0] or obstacle_grid[0][0] == 1:
        return 0
    m, n = len(obstacle_grid), len(obstacle_grid[0])

    prev = [0] * n
    curr = [0] * n
    prev[0] = 1

    for i in range(m):
        curr[0] = 0 if obstacle_grid[i][0] == 1 else prev[0]
        for j in range(1, n):
            curr[j] = 0 if obstacle_grid[i][j] == 1 else curr[j-1] + prev[j]
            prev[:] = curr
    return prev[n-1]


def main():
    obstacle_grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(unique_paths_with_obstacles(obstacle_grid))


if __name__ == "__main__":
    main()
