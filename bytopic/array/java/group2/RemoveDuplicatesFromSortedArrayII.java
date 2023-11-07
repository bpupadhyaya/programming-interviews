// Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each
// unique element appears at most twice. The relative order of the elements should be kept the same.
//Since it is impossible to change the length of the array in some languages, you must instead have the result
// be placed in the first part of the array nums. More formally, if there are k elements after removing the
// duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave
// beyond the first k elements.
//Return k after placing the final result in the first k slots of nums.
//Do not allocate extra space for another array. You must do this by modifying the input array in-place
// with O(1) extra memory.
// Example:
// Input: nums = [0,0,1,1,1,1,2,3,3]
// Output: 7, nums = [0,0,1,1,2,3,3,_,_]
// Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3
// respectively.
// It does not matter what you leave beyond the returned k (hence they are underscores).
// Tag: 4/150

import java.util.Arrays;
class DuplicatesRemovalFromSortedArrayII {
    public static void main(String...args) {
        int[] nums = {0,0,1,1,1,1,2,3,3,3,4,4,4};
        System.out.println("Number of elements: " + removeDuplicates(nums));
        System.out.println(Arrays.toString(nums));
    }

    static int removeDuplicates(int[] nums) {
        int i = 0;
        for (int n: nums)
            if (i < 2 || n > nums[i-2])
                nums[i++] = n;
        return i;
    }
}

// Intuition: allow 2 duplicates, please it doesn't convert extra numbers to _; they will appear in the output





