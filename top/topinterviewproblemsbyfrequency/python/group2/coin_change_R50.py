"""
You are given an integer array coins representing coins of different denominations and an integer amount
representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot
be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2^{31} - 1
0 <= amount <= 10^4

Tag: R50/145
"""
import math


def coin_change_1(coins: list[int], amount: int) -> int:
    # Bottom up DP (tabulation)
    dp = [math.inf] * (amount+1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount+1):
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin]+1)
    return -1 if dp[-1] == math.inf else dp[-1]


def coin_change_2(coins: list[int], amount: int) -> int:
    # Top down DP (memoization)
    def coin_change_inner(rem, cache):
        if rem < 0:
            return math.inf
        if rem == 0:
            return 0
        if rem in cache:
            return cache[rem]
        cache[rem] = min(coin_change_inner(rem-x, cache) + 1 for x in coins)
        return cache[rem]
    ans = coin_change_inner(amount, {})
    return -1 if ans == math.inf else ans


def main():
    coins = [1, 2, 5]
    amount = 11
    print(coin_change_2(coins, amount))


if __name__ == "__main__":
    main()
