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

Tag: R18/145
"""


def climb_stairs_using_space_optimization(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    prev, curr = 1, 1
    for i in range(2, n + 1):
        temp = curr
        curr = prev + curr
        prev = temp
    return curr


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


def climb_stairs_using_tabulation_or_dp(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n+1)
    dp[0] = dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


def main():
    n = 3
    print(climb_stairs_using_space_optimization(n))


if __name__ == "__main__":
    main()


"""
Recursive approach:
Explanation: The recursive solution uses the concept of Fibonacci numbers to solve the problem. It calculates 
the number of ways to climb the stairs by recursively calling the climbStairs function for (n-1) and (n-2) steps. 
However, this solution has exponential time complexity (O(2^n)) due to redundant calculations.

Memoization:
Explanation: The memoization solution improves the recursive solution by introducing memoization, which avoids 
redundant calculations. We use an unordered map (memo) to store the already computed results for each step n. 
Before making a recursive call, we check if the result for the given n exists in the memo. If it does, we return 
the stored value; otherwise, we compute the result recursively and store it in the memo for future reference.

Tabulation/dp:
 The tabulation solution eliminates recursion and uses a bottom-up approach to solve the problem iteratively. 
 It creates a DP table (dp) of size n+1 to store the number of ways to reach each step. The base 
 cases (0 and 1 steps) are initialized to 1 since there is only one way to reach them. Then, it iterates 
 from 2 to n, filling in the DP table by summing up the values for the previous two steps. Finally, it 
 returns the value in the last cell of the DP table, which represents the total number of ways to reach the top.
 
 Space optimization:
 The space-optimized solution further reduces the space complexity by using only two variables (prev and curr) 
 instead of an entire DP table. It initializes prev and curr to 1 since there is only one way to reach the base 
 cases (0 and 1 steps). Then, in each iteration, it updates prev and curr by shifting their values. curr becomes 
 the sum of the previous two values, and prev stores the previous value of curr.
"""