// Given an array nums of size n, return the majority element.
// The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority
// element always exists in the array.
// Example:
// Input: nums = [2,2,1,1,1,2,2]
// Output: 2
//
// Tag: 5/150
// Tag: 169/2927, R89/2936 (overall frequency ranking)
// Note: This logic seems flawed, debug and fix it.

import java.util.Arrays;
class MajorityElement {
    public static void main(String...args) {
        int[] nums = {2,2,1,1,1,2,2,8,8,8,8,8,8};
        System.out.println("Majority element: " + majoritElement(nums));
    }

    static int majoritElement(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        return nums[n/2];
    }
}

// Intuition:
// The intuition behind this approach is that if an element occurs more than n/2 times in the array
// (where n is the size of the array), it will always occupy the middle position when the array is sorted.
// Therefore, we can sort the array and return the element at index n/2.
//
// Explanation:
// 1. The code begins by sorting the array nums in non-decreasing order using the sort function from the C++ Standard
// Library. This rearranges the elements such that identical elements are grouped together.
// 2. Once the array is sorted, the majority element will always be present at index n/2, where n is the size of the array.
// -This is because the majority element occurs more than n/2 times, and when the array is sorted, it will occupy the
// middle position.
// 3. The code returns the element at index n/2 as the majority element.
//
// The time complexity of this approach is O(n log n) since sorting an array of size n takes O(n log n) time.