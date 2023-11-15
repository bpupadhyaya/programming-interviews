// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
// You must write an algorithm that runs in O(n) time.
// Example:
// Input: nums = [100,4,200,1,3,2]
// Output: 4
// Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
//
// Tag 47/150
// Tag: 128/2927, R57/2936 (overall frequency ranking)

import java.util.HashSet;
import java.util.Set;
class LongestConsecutiveSequence {
    public static void main(String...args) {
        int[] nums = {100,4,200,1,3,2};
        System.out.println("Longest consecutive sequence: " + longestConsecutive(nums));
    }

    static int longestConsecutive(int[] nums) {
        // S1: Handle the base case, the array is empty
        if (nums.length == 0) return 0;

        Set<Integer> set = new HashSet<>();

        // S2: Insert all the elements of 'nums' into the hash set 'set'
        for (int num: nums) {
            set.add(num);
        }

        int count = 1; // Initialize a counter for the current consecutive sequence length.
        int longest = 0; // Initialize a variable to store the maximum consecutive sequence length.

        // S3: Iterate through the element of 'nums'.
        for (int num: nums) {
            // S4: If the current element 'num' is the start of a sequence (no 'num-1' in 'set'),
            if (!set.contains(num-1)) {
                int x = num; // Update 'x' to the current element 'num'.
                count = 1;
                // S5: While consecutive elements exist in 'set', increment 'count' and 'x'.
                while (set.contains(x+1)) {
                    count++;
                    x = x + 1;
                }
            }

            // S6: Update 'longest' with the maximum of 'longest' and 'count'.
            longest = Math.max(longest, count);
        }

        // S7: Return 'longst' as the result.
        return longest;
    }
}

// Complexity:
//Time complexity ~ O(n)
// Space complexity ~ O(n)