"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Tag: 137/150
Tag: 70/2927, R25/2936 (overall frequency ranking)
"""


def climb_stairs_using_recursion(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return climb_stairs_using_recursion(n - 1) + climb_stairs_using_recursion(n - 2)


def climb_stairs_using_memoization(n: int) -> int:
    memo = {}

    def helper(n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = helper(n-1, memo) + helper(n-2, memo)
        return memo[n]

    return helper(n, memo)


def climb_stairs_using_tabulation(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n+1)
    dp[0] = dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


def climb_stairs_using_space_optimization(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    prev, curr = 1, 1
    for i in range(2, n + 1):
        temp = curr
        curr = prev + curr
        prev = temp
    return curr


def main():
    n = 3
    print(climb_stairs_using_tabulation(n))


if __name__ == "__main__":
    main()
