// Given an array nums of size n, return the majority element.
// The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority
// element always exists in the array.
// Example:
// Input: nums = [2,2,1,1,1,2,2]
// Output: 2
// Tag: 5/150

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
class MajorityElementUsingHashMap {
    public static void main(String...args) {
        int[] nums = {2,2,1,1,1,2,2,8,8,8,8,8};
        System.out.println("Majority element: " + majoritElement(nums));
    }

    static int majoritElement(int[] nums) {
        int n = nums.length;
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }

        Integer keyWithMaxCountValue = Collections.max(map.entrySet(), Map.Entry.comparingByValue()).getKey();

        return keyWithMaxCountValue;
    }
}

// Logic:
// 1. Store number and corresponding count in a hashmap
// 2. Find max value and the corresponding key, this key is the answer

