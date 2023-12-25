"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some
integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:
1 <= n <= 10^4


R80/145
"""


def num_squares(n: int) -> int:
    # Recursive
    if n == 0:
        return 0
    if n < 0:
        return float('-inf')
    mini = n
    i = 1
    while i * i <= n:
        mini = min(mini, num_squares(n - (i*i)))
        i += 1
    return mini + 1


def num_squares_1(n: int) -> int:
    # Memoization
    # Needs debugging
    memo = [-1] * (n+1)

    def solve(n):
        if n == 0:
            return 0
        if n < 0:
            return float('inf ')
        if memo[n] != -1:
            return memo[n]
        mini = n
        i = 1
        while i*i <= n:
            mini = min(mini, solve(n - (i*i)))
            i += 1
        memo[n] = mini + 1
        return memo[n]

    solve(n)


def main():
    n = 12
    print(num_squares(n))


if __name__ == "__main__":
    main()
