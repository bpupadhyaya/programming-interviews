// Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the
// array such that nums[i] == nums[j] and abs(i - j) <= k.
// Example 1:
// Input: nums = [1,2,3,1], k = 3
// Output: true
// Example 2:
// Input: nums = [1,2,3,1,2,3], k = 2
// Output: false
// Tag: 46/150

import java.util.HashSet;
import java.util.Set;
class ContainsDuplicateII {
    public static void main(String[] args) {
        int[] nums = {1,2,3,1};
        int k = 3;
        System.out.println("Duplicate exists within given range? " + containsNearbyDuplicate(nums, k));
    }

    static boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (i > k) set.remove(nums[i-k-1]); // Removing numbers out of indices range
            if (!set.add(nums[i])) return true; // Not able to add because of duplicate
        }
        return false;
    }
}