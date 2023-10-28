// Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
// Sample 1:
// Input: nums = [0,1,0]
// Output: 2
// Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

class ContiguousArray {
    public static void main(String...args) {
        int[] nums = {0,1,0};
        System.out.println("Max length of cont...: " + findMaxLength(nums));
    }

    static int findMaxLength(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            int zeros = 0, ones = 0;
            for (int j = i; j < nums.length; j++) {
                if (nums[j] == 0) {
                    zeros++;
                } else {
                    ones++;
                }
                if (zeros == ones) {
                    count = Math.max(count, j - i + 1);
                }
            }
        }

        return count;
    }
}