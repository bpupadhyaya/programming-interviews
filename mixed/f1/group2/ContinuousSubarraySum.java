// Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
// A good subarray is a subarray where:
// its length is at least two, and
// the sum of the elements of the subarray is a multiple of k.
// Note that:
// A subarray is a contiguous part of the array.
// An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
// Sample 1:
// Input: nums = [23,2,6,4,7], k = 6
// Output: true
// Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
// 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
// Tag: fb R29/50

import java.util.HashMap;
import java.util.Map;
class ContinuousSubarraySum {
    public static void main(String...args) {
        int[] nums = {23,2,6,4,7};
        int k = 6;
        System.out.println("Sub array sum exists? " + checkSubarraySum(nums, k));
    }
    static boolean checkSubarraySum(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            sum %= k;
            if (sum == 0 && i > 0) {
                return true;
            }
            if (map.containsKey(sum) && i - map.get(sum) > 1) {
                return true;
            }
            if (!map.containsKey(sum)) {
                map.put(sum, i);
            }
        }
        return false;
    }
}