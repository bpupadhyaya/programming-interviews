// You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within
// the inclusive range.
// A number x is considered missing if x is in the range [lower, upper] and x is not in nums.
// Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is
// included in any of the ranges, and each missing number is covered by one of the ranges.
// Sample 1:
// Input: nums = [0,1,3,50,75], lower = 0, upper = 99
// Output: [[2,2],[4,49],[51,74],[76,99]]
// Explanation: The ranges are:
// [2,2]
// [4,49]
// [51,74]
// [76,99]
// Sample 2:
// Input: nums = [-1], lower = -1, upper = -1
// Output: []
// Explanation: There are no missing ranges since there are no missing numbers.

import java.util.ArrayList;
import java.util.List;
class MissingRanges {
    public static void main(String...args) {
        int[] nums = {0,1,3,50,75};
        int lower = 0;
        int upper = 99;
        List<String> missingRanges = findMissingRanges(nums, lower, upper);
        for (String range: missingRanges) {
            System.out.print(range + ",");
        }
        System.out.println();
    }

    static List<String> findMissingRanges(int[] nums, int lower, int upper) {
        List<String> result = new ArrayList<>();
        int next = lower;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < next)
                continue;
            if (nums[i] == next) {
                next++;
                continue;
            }
            result.add(getRange(next, nums[i] - 1));
            next = nums[i] + 1;
        }
        if (next <= upper)
            result.add(getRange(next, upper));

        return result;
    }

    private static String getRange(int n1, int n2) {
        return (n1 == n2) ? String.valueOf(n1) : String.format("[%d,%d]", n1, n2);
    }
}