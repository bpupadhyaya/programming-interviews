// Category: group3
// Given two sorted arrays, return the median of the two sorted arrays.
// The overall run time complexity should be O(log(m+n)), where m is the
// size of first and n is the size of the second array
// Sample: Input: nums1 = [1,4], nums2 = [3]
// Output: 2
// Explanation: merged array = [1,3,4] and the median is 3.
// Sample 2: Input: nums1 = [4,5], nums2 = [6,7]
// Output:
// Explanation: merged array = [4,5,6,7] and the median is (5+6)/2 = 5.5
// Soln: Brute Forrce - Merge and Sort

import java.util.Arrays;
class MedianOfTwoSortedArrays {
    public static void main(String...args) {
        int[] nums1 = {4,5};
        int[] nums2 = {6,7};
        System.out.println("Median: "+findMedianOfTwoSortedArrays(nums1,nums2));
    }

    static double findMedianOfTwoSortedArrays(int[] data1, int[] data2) {
        int m = data1.length;
        int n = data2.length;

        // Merge the two arrays into a single array
        int[] merged = new int[m+n];
        int k = 0;
        for(int i = 0; i < m; i++) {
            merged[k++] = data1[i];
        }
        for(int i = 0; i < n; i++) {
            merged[k++] = data2[i];
        }

        // Sort the merged array
        Arrays.sort(merged);

        int mergedLength = merged.length;

        if(mergedLength % 2 == 1) // odd number of elements: return the middle element as the median
            return (double) merged[mergedLength/2];
        else {
            // even number of elements: calculate the average of two middle elements as the median
            int middle1 = merged[mergedLength / 2 - 1];
            int middle2 = merged[mergedLength / 2];

            return ((double) middle1 + (double) middle2) / 2.0;
        }
    }
}
