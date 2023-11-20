// You are given an array prices where prices[i] is the price of a given stock on the ith day.
// Find the maximum profit you can achieve. You may complete at most two transactions.
// Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
// Example:
// Input: prices = [3,3,5,0,0,3,1,4]
// Output: 6
// Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
// Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
//
// Tag: 148/150
// Tag: 123/2927, R400/2936 (overall frequency ranking)

class BestTimeToBuyAndSellStockIII {
    public static void main(String[] args) {
        int[] prices = {3,3,5,0,0,3,1,4};
        System.out.println("Max. profit: " + maxProfit(prices));
    }

    static int maxProfit(int[] prices) {
        if (prices.length == 0)
            return 0;
        int k = 2;
        int dp[][] = new int[k+1][prices.length];
        for (int i = 1; i < dp.length; i++) {
            int maxDiff = -prices[0];
            for (int j = 1; j < dp[0].length; j++) {
                maxDiff = Math.max(maxDiff, dp[i-1][j-1] - prices[j-1]);
                dp[i][j] = Math.max(dp[i][j-1], prices[j] + maxDiff);
            }
        }

        return dp[k][prices.length - 1];
    }
}

// Time ~ O(k * n)
// Space ~ O(k * n)
// k = K transactions, 2 in this case
// n = prices.length