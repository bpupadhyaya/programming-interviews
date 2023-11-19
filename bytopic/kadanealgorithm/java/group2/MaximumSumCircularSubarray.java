// Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
// A circular array means the end of the array connects to the beginning of the array. Formally, the next element of
// nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
// A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i],
// nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
//
// Input: nums = [5,-3,5]
// Output: 10
// Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
// Tag: 113/150
// Tag: 918/2927, R949/2936 (overall frequency ranking)

class MaximumSumCircularSubarray {
    public static void main(String...args) {
        int[] nums = {5, -3, 5};
        System.out.println("Max. subarray sum: " + maxSubarraySumCircular(nums));
    }

    static int maxSubarraySumCircular(int[] nums) {
        // Keep track of the total sum of the array
        int acc = 0;
        // Keep track of the maximum sum subarray using kadane's algorithm
        int max1 = kadane(nums);
        // Iterate through the array and negate each element
        for (int i = 0; i < nums.length; i++) {
            acc += nums[i];
            nums[i] = - nums[i];
        }
        // Keep track of the minimum sum subarray using kadane's algorithm
        int min = kadane(nums);
        // Keep track of the maximum sum subarray that can be formed by wrapping around the array
        int max2 = acc + min;
        // If the maximum sum subarray that can be formed by wrapping around the array is zero, return the maximum
        // sum subarray using kadane's algorithm
        if (max2 == 0) return max1;
        // Return the maximum of the two maximum sum subarrays
        return Math.max(max1, max2);
    }

    // Method to calculate the maximum sum subarray using kadane's algorithm
    static int kadane(int[] nums) {
        // Keep track of the maximum sum subarray ending at current index
        int maxSum = nums[0];
        // Keep track of the overall maximum sum subarray
        int max = nums[0];
        // Iterate through the array starting from the second element
        for (int i = 1; i < nums.length; i++) {
            // Update the maximum sum subarray ending at current index
            // by taking the maximum between the current element and the sum of the current element and the maximum sum
            // subarray ending at the previous index
            maxSum = Math.max(maxSum + nums[i], nums[i]);
            // Update the overall maximum sum subarray by taking the maximum between the current maximum sum subarray
            // ending at current index and the overall maximum sum subarray
            max = Math.max(max, maxSum);
        }
        return max;
    }
}
