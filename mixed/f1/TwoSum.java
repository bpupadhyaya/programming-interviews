// Given an array of integer numbers and a target integer number, return indices of the two numbers such that
// they add up to the given target.
// Example :
// Input: [6,3,8,9], target: 11
// Output: [1,2]

import java.util.Map;
import java.util.HashMap;
class TwoSum {
   public static void main(String[] args) {
       int target = 11;
       int[] nums1 = {6,3,8,9};
       int[] nums2 = {8,6,6,3,9,8};
       int[] indices1 = findIndicesTwoSum(nums1, target);
       int[] indices2 = findIndicesTwoSum(nums2, target);
       System.out.println("Indices first set: ");
       System.out.printf("%d, %d",indices1[0], indices1[1]);
       System.out.println();
       System.out.println("Indices second set: ");
       System.out.printf("%d, %d",indices2[0], indices2[1]);
       System.out.println();
   }

   static int[] findIndicesTwoSum(int nums[], int target) {
        int numsLength = nums.length;
        Map<Integer, Integer> map = new HashMap<>();
        int[] result = new int[2];
        for(int i=0; i< numsLength; i++) {
            if(map.containsKey(target-nums[i])) {
                result[1] = i;
                result[0] = map.get(target-nums[i]);
                return result;
            }
            map.put(nums[i], i);
       }
        return result;
   }
}