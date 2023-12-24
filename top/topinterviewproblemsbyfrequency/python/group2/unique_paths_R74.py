"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down
or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
1 <= m, n <= 100


Tag: R74/145
"""
import math


def unique_paths_1(m: int, n: int) -> int:
    # Combinatorial
    return math.comb(m+n-2, m-1)


def unique_paths_2(m: int, n: int) -> int:
    # DP - 2D
    dp = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]


def unique_paths_3(m: int, n: int) -> int:
    # DP - 1D
    curr_row = [1] * n
    prev_row = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            curr_row[j] = curr_row[j-1] + prev_row[j]
            curr_row, prev_row = prev_row, curr_row
    return prev_row[-1]


def main():
    m = 3
    n = 2
    print(unique_paths_2(m, n))


if __name__ == "__main__":
    main()


"""
Combinatorial Mathematics (unique_paths_1):
Intuition
The number of unique paths can be seen as the number of ways to choose m−1 downs and n−1 rights, 
regardless of the order. In combinatorial terms, this is equivalent to 
  m+n−2
(       )
  m-1 


Complexity Analysis
Time Complexity: O(m) or O(n) — For calculating the combination.
Space Complexity: O(1)— Constant space.

"""
