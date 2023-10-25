// Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
// Sample 1:
// Input: nums = [3,2,3]
// Output: [3]
// Sample 2:
// Input: nums = [1]
// Output: [1]
// Sample 3:
// Input: nums = [1,2]
// Output: [1,2]

import java.util.ArrayList;
import java.util.List;
class MajorityElementII {
    public static void main(String...args) {
        int[] nums = {3,2,3};
        List<Integer> majElements = majorityElement(nums);
        System.out.println("Majorityu elements: " + majElements);
    }

    static List<Integer> majorityElement(int[] nums) {
        int count1 = 0, count2 = 0;
        int candidate1 = 0, candidate2 = 0;

        for (int i = 0; i < nums.length; i++) {
            if (count1 == 0 && nums[i] != candidate2) {
                count1 = 1;
                candidate1 = nums[i];
            } else if (count2 == 0 && nums[i] != candidate1) {
                count2 = 1;
                candidate2 = nums[i];
            } else if (candidate1 == nums[i]) {
                count1++;
            } else if (candidate2 == nums[i]) {
                count2++;
            } else {
                count1--;
                count2--;
            }
        }

        List<Integer> result = new ArrayList<>();
        int threshold = nums.length / 3;

        count1 = 0;
        count2 = 0;
        for (int i = 0; i < nums.length; i++) {
            if (candidate1 == nums[i]) {
                count1++;
            } else if (candidate2 == nums[i]) {
                count2++;
            }
        }

        if (count1 > threshold) {
            result.add(candidate1);
        }
        if (count2 > threshold) {
            result.add(candidate2);
        }

        return result;
    }
}
