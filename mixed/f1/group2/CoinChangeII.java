// You are given an integer array coins representing coins of different denominations and an integer amount representing
// a total amount of money.
// Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination
// of the coins, return 0.
// You may assume that you have an infinite number of each kind of coin.
// The answer is guaranteed to fit into a signed 32-bit integer.
// Sample 1:
// Input: amount = 5, coins = [1,2,5]
// Output: 4
// Explanation: there are four ways to make up the amount:
// 5=5
// 5=2+2+1
// 5=2+1+1+1
// 5=1+1+1+1+1
// Soln: Dynamic programming

class CoinChangeII {
    public static void main(String...args) {
        int amount = 5;
        int[] coins = {1,2,5};
        System.out.println("Num. of combinations: " + change(amount, coins));
    }

    static int change(int amount, int[] coins) {
        int[] dp = new int[amount+1];
        dp[0] = 1;

        for (int coin: coins) {
            for (int j = coin; j <= amount; j++) {
                dp[j] += dp[j-coin];
            }
        }
        return dp[amount];
    }
}