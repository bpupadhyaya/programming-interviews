// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that
// i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
// Notice that the solution set must not contain duplicate triplets.
// Sample 1:
// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Explanation:
// nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
// nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
// nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
// The distinct triplets are [-1,0,1] and [-1,-1,2].
// Notice that the order of the output and the order of the triplets does not matter.

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
class ThreeSum {
    public static void main(String...args) {
        int[] nums = {-1,0,1,2,-1,-4};
        List<List<Integer>> result = findThreeSum(nums);
        System.out.println("Three sums: ");
        for (List<Integer> res: result)
            System.out.println("Combination: " + res);

        System.out.println();

    }

    static List<List<Integer>> findThreeSum(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        Arrays.sort(nums);

        for(int i = 0; i < nums.length - 2; i++) {
            // Skip duplicate elements for i
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }

            int j = i + 1;
            int k = nums.length - 1;

            while(j < k) {
                int sum = nums[i] + nums[j] + nums[k];

                if (sum == 0) {
                    // Found a triplet with 0 sum
                    ans.add(Arrays.asList(nums[i], nums[j], nums[k]));

                    // Skip duplicate elements for j
                    while(j < k && nums[j] == nums[j+1]) {
                        j++;
                    }

                    // Skip duplicate elements for k
                    while(j < k && nums[k] == nums[k-1]) {
                        k--;
                    }

                    // Move the pointers
                    j++;
                    k--;
                } else if (sum < 0) {
                    // Sum is less than 0, increment j to increase the sum
                    j++;
                } else {
                    // Sum is greater than 0, decrement k to decrease the sum
                    k--;
                }
            }
        }
        return ans;
    }
}