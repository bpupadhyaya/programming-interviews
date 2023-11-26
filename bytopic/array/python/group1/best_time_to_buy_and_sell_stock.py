"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Tag: 7/150
Tag: 121/2927, R6/2936 (overall frequency ranking)
"""


def max_profit(prices: list[int]) -> int:
    min_price = prices[0]
    max_profit_ = 0
    for price in prices[1:]:
        max_profit_ = max(max_profit_, price - min_price)
        min_price = min(min_price, price)
    return max_profit_


def main():
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit(prices))


if __name__ == "__main__":
    main()
