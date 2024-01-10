"""
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of
 points you can get from the matrix.
To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to
 your score.
However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For
 every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2)
  will subtract abs(c1 - c2) from your score.
Return the maximum number of points you can achieve.

abs(x) is defined as:
x for x >= 0.
-x for x < 0.

Example:
Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.

Constraints:
m == points.length
n == points[r].length
1 <= m, n <= 10^5
1 <= m * n <= 10^5
0 <= points[r][c] <= 10^5

Tag: G32/50
"""


def max_points(points: list[list[int]]) -> int:
    m, n = len(points), len(points[0])

    dp = points[0]

    left = [0] * n  # left side contribution
    right = [0] * n  # right side contribution

    for r in range(1, m):
        for c in range(n):
            if c == 0:
                left[c] = dp[c]
            else:
                left[c] = max(left[c - 1] - 1, dp[c])

        for c in range(n - 1, -1, -1):
            if c == n-1:
                right[c] = dp[c]
            else:
                right[c] = max(right[c + 1] - 1, dp[c])

        for c in range(n):
            dp[c] = points[r][c] + max(left[c], right[c])

    return max(dp)


def main():
    points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
    print(max_points(points))


if __name__ == "__main__":
    main()
