// You are given an array prices where prices[i] is the price of a given stock on the ith day.
// Find the maximum profit you can achieve. You may complete at most one transaction.
// Example:
// Input: prices = [3,3,5,0,0,3,1,4]
// Output: 4
// Explanatoin: since only one transaction is allowed, in order to make max. profit, buy on either
// day 4th or 5th (same price) and sell on 8th day: 4 - 0 = 4
//
// Tag: None/150
// Tag: None/2927, RNone/2936 (overall frequency ranking)

class BestTimeToBuyAndSellStockOneTransaction {
    public static void main(String[] args) {
        int[] prices = {3,3,5,0,0,3,1,4};
        System.out.println("Max. profit: " + maxProfit(prices));
    }

    static int maxProfit(int[] prices) {
        int maxEndingHere = 0;
        int maxSoFar = 0;
        for (int i = 1; i < prices.length; i++) {
            maxEndingHere = Math.max(0, maxEndingHere + prices[i] - prices[i-1]);
            maxSoFar = Math.max(maxSoFar, maxEndingHere);
        }

        return maxSoFar;
    }
}

// Soln: Kadane's algo
// Time ~ O(n)
// Space ~ O(1)