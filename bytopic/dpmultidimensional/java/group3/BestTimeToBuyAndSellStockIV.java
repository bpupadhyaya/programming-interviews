// You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
// Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times
// and sell at most k times.
// Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
// Example:
// Input: k = 2, prices = [3,2,6,5,0,3]
// Output: 7
// Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0)
// and sell on day 6 (price = 3), profit = 3-0 = 3.
//
// Tag: 149/150
// Tag: 188/2927, R508/2936 (overall frequency ranking)

class BestTimeToBuyAndSellStockIV {
    public static void main(String[] args) {
        int k = 2;
        int[] prices = {3,2,6,5,0,3};
        System.out.println("Max profit: " + maxProfit(k, prices));
    }

    static int maxProfit(int k, int[] prices) {
        if (k >= prices.length / 2)
            return maxProfit(prices);   // This is to avoid Memory Limit Exceeded... In other words,
                                        // we can make infinite transactions. Using variant presented in Infinite
                                        // number of transactions case.
        int dp[][] = new int[k+1][prices.length];
        for (int i = 1; i < dp.length; i++) {
            int maxDiff = -prices[0];
            for (int j = 1; j < dp[0].length; j++) {
                maxDiff = Math.max(maxDiff, dp[i-1][j-1] - prices[j-1]);
                dp[i][j] = Math.max(dp[i][j-1], prices[j] + maxDiff);
            }
        }

        return dp[k][prices.length -1];
    }

    private static int maxProfit(int[] prices) {
        int profit = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            if (prices[i+1] > prices[i]) {
                profit += prices[i+1] - prices[i];
            }
        }

        return profit;
    }
}