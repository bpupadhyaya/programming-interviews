// Given an array of stock prices, find maximum profit. If maximum profit cannot be found return 0.
// If a[] is an array representing stock prirce, a[i] represents stock on the ith day.
// Rules: can hold only one stock in a day; can buy and sell only twice for a given duration.
// Sample input: a = [10, 5, 6, 25, 1, 10], sample output: 20 + 9 = 29
// Sample input: a = [250, 200, 100, 90], sample output: 0
// Soln: Time complexity: O(n), space complexity: O(n)

class BuySellStock {
    public static void main(String[] args) {
        int[] prices1 = {10, 5, 6, 25, 1, 10};
        int[] prices2 = {250, 200, 100, 90};
        int[] prices3 = {1, 5, 5, 21,5,55,6,56};
        System.out.println("Max profit 1: " + findMaxProfit(prices1));
        System.out.println("Max profit 2: " + findMaxProfit(prices2));
        // TODO need to fix
        System.out.println("Max profit 3: " + findMaxProfit(prices3));
    }

    private static int findMaxProfit(int[] priceArray) {
        int t1Cost = Integer.MAX_VALUE;
        int t2Cost = Integer.MAX_VALUE;
        int t1Profit = 0;
        int t2Profit = 0;

        for (int i = 0; i < priceArray.length; ++i) {
            t1Cost = Math.min(t1Cost, priceArray[i]);
            t1Profit = Math.max(t1Profit, priceArray[i] - t1Cost);

            t2Cost = Math.min(t2Cost, priceArray[i] - t1Profit);
            t2Profit = Math.max(t2Profit, priceArray[i] - t2Cost);
        }

        return t2Profit;
    }

}