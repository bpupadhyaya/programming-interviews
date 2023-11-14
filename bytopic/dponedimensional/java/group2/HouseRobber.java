// You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
// the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
// it will automatically contact the police if two adjacent houses were broken into on the same night.
// Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
// rob tonight without alerting the police.
// Sample 1:
// Input: nums = [2,7,9,3,1]
// Output: 12
// Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
// Total amount you can rob = 2 + 9 + 1 = 12.
//
// Tag: 138/150
// Tag: 198/2927, R164/2936 (overall frequency ranking)

import java.util.HashMap;
class HouseRobber {
    public static void main(String...args) {
        int[] nums = {2,7,9,3,1};
        System.out.println("Max robbed: " + rob(nums));
    }

    static int rob(int[] nums) {
        return helper(nums, 0, new HashMap<Integer, Integer>());
    }

    static int helper(int[] nums, int i, HashMap<Integer, Integer> memo) {
        if (memo.containsKey(i)) {
            return memo.get(i);
        }
        if (i >= nums.length) {
            return 0;
        }

        int notTake = 0;
        int take = nums[i] + helper(nums, i+2, memo);
        if (i < nums.length -1)
            notTake = nums[i+1] + helper(nums, i+3, memo);
        memo.put(i, Math.max(take, notTake));

        return memo.get(i);
    }
}