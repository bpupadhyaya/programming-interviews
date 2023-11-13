// You are given a sorted unique integer array nums.
// A range [a,b] is the set of all integers from a to b (inclusive).
// Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each
// element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of
// the ranges but not in nums.
// Each range [a,b] in the list should be output as:
//"a->b" if a != b
//"a" if a == b
// Example:
// Input: nums = [0,2,3,4,6,8,9]
// Output: ["0","2->4","6","8->9"]
// Explanation: The ranges are:
// [0,0] --> "0"
// [2,4] --> "2->4"
// [6,6] --> "6"
// [8,9] --> "8->9"
// Tag: 48/150

import java.util.ArrayList;
import java.util.List;
class SummaryRanges {
    public static void main(String...args) {
        int[] nums = {0,2,3,4,6,8,9};
        System.out.println("Summary ranges: " + summaryRanges(nums));
    }

    static List<String> summaryRanges(int[] nums) {
        List<String>  summaryRanges = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            int start = nums[i];
            while (i+1 < nums.length && nums[i]+1 == nums[i+1])
                i++;

            if (start != nums[i]) {
                summaryRanges.add("" + start + "->" + nums[i]);
            } else {
                summaryRanges.add("" + start);
            }
        }

        return summaryRanges;
    }
}