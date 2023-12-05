"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
//
Tag: 148/150
Tag: 123/2927, R400/2936 (overall frequency ranking)
"""


def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0
    # Initialize variables for first buy, first sell, second buy, and second sell
    buy1, buy2 = float('inf'), float('inf')
    sell1, sell2 = 0, 0

    # Iterate over prices to update buy adn sell values
    for price in prices:
        # Update first buy and sell values
        buy1 = min(buy1, price)
        sell1 = max(sell1, price - buy1)
        # Update second buy and sell values
        buy2 = min(buy2, price - sell1)
        sell2 = max(sell2, price - buy2)

    return sell2


def main():
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print(max_profit(prices))


if __name__ == "__main__":
    main()
