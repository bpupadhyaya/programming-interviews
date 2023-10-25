// Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the
// array such that nums[i] == nums[j] and abs(i - j) <= k.
// Sample 1:
// Input: nums = [1,2,3,1], k = 3
// Output: true

import java.util.HashSet;
class ContainsDuplicateII {
    public static void main(String...args) {
        int nums[] = {1,2,3,1};
        int k = 3;
        System.out.println("Contains duplicate? " + containsDuplicate(nums, k));
    }

    static boolean containsDuplicate(int[] nums, int k) {
        if (nums == null || nums.length < 2 || k == 0)
            return false;
        int i = 0;
        HashSet<Integer> hset = new HashSet<Integer>();
        for (int j = 0; j < nums.length; j++) {
            if (!hset.add(nums[j])) {
                return true;
            }
            if (hset.size() >= k+1) {
                hset.remove(nums[i++]);
            }
        }
        return false;
    }
}