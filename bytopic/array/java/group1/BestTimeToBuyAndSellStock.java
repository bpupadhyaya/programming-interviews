// You are given an array prices where prices[i] is the price of a given stock on the ith day.
// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
// future to sell that stock.
// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
// Example:
// Input: prices = [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
// Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
// Tag: 7/150

class BestTimeToBuyAndSellStock {
    public static void main(String...args) {
        int[] prices = {7,1,5,3,6,4};
        System.out.println("Maximum profit: " + maxProfit(prices));
    }

    static int maxProfit(int[] prices) {
        int lowestPriceTracker = Integer.MAX_VALUE;
        int maxProfitTracker = 0;
        int currentDiffWithLowestPriceTracker = 0;

        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < lowestPriceTracker) {
                lowestPriceTracker = prices[i];
            }
            currentDiffWithLowestPriceTracker = prices[i] - lowestPriceTracker;
            if (maxProfitTracker < currentDiffWithLowestPriceTracker) {
                maxProfitTracker = currentDiffWithLowestPriceTracker;
            }
        }
        return maxProfitTracker;
    }
}

// Logic:
// 1. Track the lowest price.
// 2. Calculate the difference between current price and current lowest price from the past
// 3. Track the max profit
// 4. Return the last value of the max. profit