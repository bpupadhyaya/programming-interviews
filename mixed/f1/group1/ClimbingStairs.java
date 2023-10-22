// You are climbing a staircase. It takes n steps to reach the top.
// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
// Input: n = 3
// Output: 3
// Explanation: There are three ways to climb to the top.
// 1. 1 step + 1 step + 1 step
// 2. 1 step + 2 steps
// 3. 2 steps + 1 step

class ClimbingStairs {
    public static void main(String...args) {
        int n = 5;
         System.out.println("Number of distinct ways: " + findDistinctWays(n));
    }

    static int findDistinctWays(int n) {
        if (n <= 3)
            return n;

        int left = 0;
        int right = 1;
        for (int i = 0; i < n; i++) {
            int temp = right;
            right = left + right;
            left = temp;
        }

        return right;
    }
}