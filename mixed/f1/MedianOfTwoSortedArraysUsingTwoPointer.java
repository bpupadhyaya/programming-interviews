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
// Soln: Two-Pointer
// Time complexity: O(m+n), Space complexity: O(1)

class MedianOfTwoSortedArraysUsingTwoPointer {
    public static void main(String...args) {
        int[] nums1 = {4,5};
        int[] nums2 = {6,7};
        System.out.println("Median: " + findMedianOfTwoSortedArraysUsingTwoPointer(nums1, nums2));
    }

    static double findMedianOfTwoSortedArraysUsingTwoPointer(int[] data1, int[] data2) {
        int m = data1.length;
        int n = data2.length;
        int i = 0, j = 0, m1 = 0, m2 = 0;

        for(int count = 0; count <= (m + n) / 2; count++) {
            m2 = m1;
            if (i != m && j!= n) {
                if (data1[i] > data2[j]) {
                    m1 = data2[j++];
                } else {
                    m1 = data1[i++];
                }
            } else if (i < n) {
                m1 = data1[i++];
            } else {
                m1 = data2[j++];
            }
        }

        if ((m + n) % 2 == 1) {
            return (double) m1;
        } else {
            double medPrep = (double) m1 + (double) m2;
            return medPrep / 2.0;
        }
    }
}