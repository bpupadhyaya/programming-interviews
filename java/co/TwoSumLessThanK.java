// Given an array of integers and integer k, return the maximum sum such that sum is less than k.

import java.util.Arrays;

class TwoSumLessThanK {
    public static void main(String...args) {
        int[] case1 = {55,23,1,24,75,15,54,25};
        int k1 = 70;
        int[] case2 = {50,10,30};
        int k2 = 15;
        System.out.println("Sum: "+twoSumLessThanK(case1, k1));

    }

    private static int twoSumLessThanK(int[] nums, int k) {
        Arrays.sort(nums);
        int left = 0;
        int right = nums.length - 1;
        int result = -1;
        int sum = 0;
        while(left < right) {
            sum = nums[left] + nums[right];
            if ( sum< k) {
                result = Math.max(result, sum);
                left++;
            } else {
                right--;
            }
        }
        return result;
    }
}