// You are given an array prices where prices[i] is the price of a given stock on the ith day.
// Find the maximum profit you can achieve. You may complete infinite number of transactions.
// Example:
// Input: prices = [3,3,5,0,0,3,1,4]
// Output: 8
// Explanation: Buy on day 2 and sell on day 3: 5-3 = 2; buy on day 5 and sell on day 6: 3-0 = 3;
// buy on day 7 and sell on day 8: 4-1 = 3; total 2+3+3 = 8
//
// Tag: None/150
// Tag: None/2927, RNone/2936 (overall frequency ranking)

class BestTimeToBuyAndSellStockInfiniteTransactions {
    public static void main(String[] args) {
        int[] prices = {3,3,5,0,0,3,1,4};
        System.out.println("Max. profit: " + maxProfit(prices));
    }

    static int maxProfit(int[] prices) {
        int profit = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            if (prices[i+1] > prices[i]) {
                profit += prices[i+1] - prices[i];
            }
        }

        return profit;
    }
}

// Time ~ O(n)
// Space ~ O(1)