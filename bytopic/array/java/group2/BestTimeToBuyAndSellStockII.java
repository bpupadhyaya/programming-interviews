// You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
// On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock
// at any time. However, you can buy it then immediately sell it on the same day.
// Find and return the maximum profit you can achieve.
// Example:
// Input: prices = [7,1,5,3,6,4]
// Output: 7
// Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
// Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
// Total profit is 4 + 3 = 7.
// Tag: 8/150

class BestTimeToBuyAndSellStockII {
    public static void main(String...args) {
        int[] prices= {7,1,5,3,6,4};
        System.out.println("Max profit: " + maxProfit(prices));
    }

    static int maxProfit(int[] prices) {
        // Selling stock on the first day is not allowed so set max available negative value as a reference point.
        int currentHold = -Integer.MAX_VALUE;
        int currentNotHold = 0;

        for (int stockPrice: prices) {
            int prevHold = currentHold;
            int prevNotHold = currentNotHold;

            // Either keep curretHold or buy stock today at stock price
            currentHold = Math.max(prevHold, prevNotHold - stockPrice);

            // Either keep notHold or sell stock today at stock price
            currentNotHold = Math.max(prevNotHold, prevHold + stockPrice);
        }
        // Max. profit should be in latest currentNotHold.
        return currentNotHold;
    }
}