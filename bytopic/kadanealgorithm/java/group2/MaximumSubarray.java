// Given an integer array nums, find the subarray with the largest sum, and return its sum.
// Example:
// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: The subarray [4,-1,2,1] has the largest sum 6.
//
// Tag: 112/150
// Tag: 53/2927, R37/2936 (overall frequency ranking)

class MaximumSubarray {
    public static void main(String[] args) {
        int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
        System.out.println("Largest sum from subarray: " + maxSubArray(nums));
    }

    static int maxSubArray(int[] nums) {
        int n = nums.length;
        int max = Integer.MIN_VALUE, sum = 0;

        for (int i = 0; i < n; i++) {
            sum += nums[i];
            max = Math.max(sum, max);

            if (sum < 0)
                sum = 0;
        }
        return max;
    }
}

