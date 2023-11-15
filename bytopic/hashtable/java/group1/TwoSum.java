// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.
// Example:
// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
//
// Tag: 44/150
// Tag: 1/2927, R1/2936 (overall frequency ranking)

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
class TwoSum {
    public static void main(String[] args) {
        int[] nums = {2,7,11,15};
        int target = 9;
        int[] indices = twoSum(nums, target);
        System.out.println("Indices: " + Arrays.toString(indices));
    }

    static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if (numMap.containsKey(complement)) {
                return new int[]{numMap.get(complement), i}; // Found the solution
            }
            numMap.put(nums[i], i); // Keep adding into the hashmap.
        }

        return new int[]{}; // No solution
    }
}