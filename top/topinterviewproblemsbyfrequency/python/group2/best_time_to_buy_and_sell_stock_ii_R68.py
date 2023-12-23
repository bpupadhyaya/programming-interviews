"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock
at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Tag: R68/145
Tag: 8/150
Tag: 122/2927, R165/2936 (overall frequency ranking)
"""
from functools import cache


def max_profit_using_bottom_up_dp_and_iteration(prices: list[int]) -> int:
    # It is impossible to sell stock on first day, set -infinity as initial value for cur_hold
    cur_hold, cur_not_hold = -float('inf'), 0
    for stock_price in prices:
        prev_hold, prev_not_hold = cur_hold, cur_not_hold
        # either keep hold, or buy in stock today at stock price
        cur_hold = max(prev_hold, prev_not_hold - stock_price)
        # either keep not-hold, or sell out stock today at stock price
        cur_not_hold = max(prev_not_hold, prev_hold + stock_price)
    # maximum profit must be in not-hold state
    return cur_not_hold
    # Time Complexity: O(n), for single level for loop
    # Space Complexity: O(1), for fixed size of temporary variables


def max_profit_using_top_down_dp_and_recursion(prices: list[int]) -> int:
    @cache
    def trade(day_d):
        if day_d == 0:
            # Hold on day_#0 = buy stock at the price of day_#0
            # Not-hold on day_#0 = doing nothing on day_#0
            return -prices[day_d], 0

        prev_hold, prev_not_hold = trade(day_d - 1)
        hold = max(prev_hold, prev_not_hold - prices[day_d])
        not_hold = max(prev_not_hold, prev_hold + prices[day_d])
        return hold, not_hold
    last_day = len(prices) - 1
    # Max profit must come from not_hold state (i.e., no stock position) on last day
    return trade(last_day)[1]
    # Time Complexity: O(n), for single level for loop
    # Space Complexity: O(n), for 1D DP recursion call depth


def max_profit_using_greedy_container_and_summation(prices: list[int]) -> int:
    price_gain = []
    for idx in range(len(prices) - 1):
        if prices[idx] < prices[idx+1]:
            price_gain.append(prices[idx+1] - prices[idx])
    return sum(price_gain)
    # Time Complexity: O(n), for single level for loop
    # Space Complexity: O(n), for array storage sapce


def max_profit_using_greedy_generator_expression_and_sum(prices: list[int]) -> int:
    return sum((prices[idx+1]-prices[idx]) for idx in range(len(prices)-1) if prices[idx] < prices[idx+1])


def max_profit_using_greedy(prices: list[int]) -> int:
    profit_from_price_gain = 0
    for idx in range(len(prices)-1):
        if prices[idx] < prices[idx+1]:
            profit_from_price_gain += (prices[idx+1] - prices[idx])
    return profit_from_price_gain
    # Time Complexity: O(n), for single level for loop
    # Space Complexity: O(1), for fixed size of temporary variables


def main():
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit_using_greedy(prices))


if __name__ == "__main__":
    main()
