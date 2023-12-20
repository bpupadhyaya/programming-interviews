"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in
the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Tag: Tag: R5/145
"""


def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0
    max_profit_ = 0
    min_purchase = prices[0]
    for i in range(1, len(prices)):
        max_profit_ = max(max_profit_, prices[i] - min_purchase)
        min_purchase = min(min_purchase, prices[i])
    return max_profit_


def main():
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit(prices))


if __name__ == "__main__":
    main()

"""
Intuition:
We always need to know what is the maxProfit we can make if we sell the stock on i-th day. So, keep track of maxProfit.
There might be a scenario where if stock bought on i-th day is minimum and we sell it on (i + k)th day. So, 
keep track of minPurchase as well.
"""
