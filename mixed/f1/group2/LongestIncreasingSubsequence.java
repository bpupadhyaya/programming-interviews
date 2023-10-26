// Given an integer array nums, return the length of the longest strictly increasing subsequence.
// Sample 1:
// Input: nums = [10,9,2,5,3,7,101,18]
// Output: 4
// Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

class LongestIncreasingSubsequence {
    public static void main(String...args) {
        int[] nums = {10,9,2,5,3,7,101,18};
        System.out.println("Length of LIS: " + lengthofLIS(nums));
    }

    static int lengthofLIS(int[] nums) {
        int[] tails = new int[nums.length];
        int size = 0;
        for (int x: nums) {
            int i = 0, j = size;
            while (i != j) {
                int m = (i + j) / 2;
                if (tails[m] < x)
                    i =  m + 1;
                else j = m;
            }
            tails[i] = x;
            if (i == size) ++size;
        }
        return size;
    }
}