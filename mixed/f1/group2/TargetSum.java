// You are given an integer array nums and an integer target.
// You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and
// then concatenate all the integers.
// For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
// Return the number of different expressions that you can build, which evaluates to target.
// Sample 1:
// Input: nums = [1,1,1,1,1], target = 3
// Output: 5
// Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
// -1 + 1 + 1 + 1 + 1 = 3
// +1 - 1 + 1 + 1 + 1 = 3
// +1 + 1 - 1 + 1 + 1 = 3
// +1 + 1 + 1 - 1 + 1 = 3
// +1 + 1 + 1 + 1 - 1 = 3

class TargetSum {
    public static void main(String...args) {
        int nums[] = {1,1,1,1,1};
        int target = 3;
        System.out.println("Number of ways: " + findTargetSumWays(nums, target));
    }

    static int findTargetSumWays(int[] nums, int target) {
        int sum = 0;
        for (int x: nums)
            sum += x;
        if ((sum - target) % 2 == 1 || (target > sum))
            return 0;
        int n = nums.length;
        int s2 = (sum - target) / 2;
        int[][] t = new int[n+1][s2+1];
        t[0][0] = 1;

        for (int i = 1; i < n + 1; i++) {
            for (int j = 0; j < s2 + 1; j++) {
                if (nums[i-1] <= j)
                    t[i][j] = t[i-1][j] + t[i-1][j - nums[i-1]];
                else t[i][j] = t[i-1][j];
            }
        }
        return t[n][s2];
    }
}

