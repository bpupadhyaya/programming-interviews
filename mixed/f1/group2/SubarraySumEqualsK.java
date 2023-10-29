// Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
// A subarray is a contiguous non-empty sequence of elements within an array.
// Input: nums = [1,1,1], k = 2
// Output: 2

import java.util.HashMap;
import java.util.Map;
class SubarraySumEqualsK {
    public static void main(String...args) {
        int[] nums = {1,1,1,1,3,2,2};
        int k = 4;

        System.out.println("Total nubmer of subarray whose sum equals to k: " + subarraySum(nums, k));
    }

    static int subarraySum(int[] nums, int k) {
        int count = 0, sum = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0,1);

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (map.containsKey(sum - k))
                count += map.get(sum - k);
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }

        return count;
    }
}