// Given an array of stock prices, find maximum profit. If maximum profit cannot be found return 0.
// If a[] is an array representing stock prirce, a[i] represents stock on the ith day.
// Sample input: a = [10, 5, 6, 25, 1], sample output: 20
// Sample input: a = [250, 200, 100, 90], sample output: 0
// Soln: Time complexity: O(n), space complexity: O(1)

class BuySellStock {
    public static void main(String[] args) {
        int[] prices1 = {10, 5, 6, 25, 1};
        int[] prices2 = {250, 200, 100, 90};
        System.out.println("Max profit 1: " + findMaxProfit(prices1));
        System.out.println("Max profit 21: " + findMaxProfit(prices2));
    }

    private static int findMaxProfit(int[] priceArray) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int i = 0; i < priceArray.length; i++) {
             if (priceArray[i] < minPrice)
                 minPrice = priceArray[i];

             if (priceArray[i] -  minPrice > maxProfit)
                 maxProfit = priceArray[i] - minPrice;
        }

        return maxProfit;
    }
}
