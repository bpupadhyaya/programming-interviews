// Given an integer array nums, find a subarraynthat has the largest product, and return the product.
// The test cases are generated so that the answer will fit in a 32-bit integer.
// Sample 1:
// Input: nums = [2,3,-2,4]
// Output: 6
// Explanation: [2,3] has the largest product 6.
// Sample 2:
// Input: nums = [-2,0,-1]
// Output: 0
// Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
// Soln: Two-pointer approach

class MaximumProductSubarray{
    public static void main(String...args) {
        int[] nums = {2,3,-2,4};
        System.out.println("Max product from subarray: " + findMaximumProductSubarray(nums));
    }

    static int findMaximumProductSubarray(int[] nums) {
        int n = nums.length;
        int l = 1, r = 1;
        int ans = nums[0];

        for (int i = 0; i < n; i++) {
            l = l == 0 ? 1 : l;
            r = r == 0 ? 1: r;

            l *= nums[i];
            r *= nums[n-1-i];

            ans = Math.max(ans, Math.max(l, r));
        }

        return ans;
    }
}
