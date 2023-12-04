"""
You are given an integer array coins representing coins of different denominations and an integer amount
representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by
any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Tag: 140/150
Tag: 322/2927, R115/2936 (overall frequency ranking)
"""


def coin_change(coins: list[int], amount: int) -> int:
    min_coins = [amount+1] * (amount + 1)
    min_coins[0] = 0

    for i in range(amount + 1):
        for coin in coins:
            if coin <= i:
                min_coins[i] = min(min_coins[i], min_coins[i-coin] + 1)
    if min_coins[amount] == amount + 1:
        return -1

    return min_coins[amount]


def main():
    coins = [1, 2, 5]
    amount = 11
    print(coin_change(coins, amount))


if __name__ == "__main__":
    main()
