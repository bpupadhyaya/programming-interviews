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
// Soln: Binary Search
// Time complexity: O(logn/logm), Space complexity: O(1)

class MedianOfTwoSortedArraysUsingBinarySearch {
    public static void main(String...args) {
        int[] nums1 = {4,5};
        int[] nums2 = {6,7};
        System.out.println("Median: " + findMedianOfTwoSortedArraysUsingBinarySearch(nums1, nums2));
    }

    static double findMedianOfTwoSortedArraysUsingBinarySearch(int[] data1, int[] data2) {
        int n1 = data1.length;
        int n2 = data2.length;

        // Ensure data1 is the smaller array for simplicity
        if (n1 > n2)
            return findMedianOfTwoSortedArraysUsingBinarySearch(data2, data1);

        int n = n1 + n2;
        int left = (n1 + n2 + 1) / 2; // Calculate the left partition size
        int low  = 0, high = n1;

        while (low <= high) {
            int mid1 = (low + high) >> 1; // Calculate mid index for nums1
            int mid2 = left - mid1; // Calculate mid index for nums2

            int l1 = Integer.MIN_VALUE;
            int l2 = Integer.MIN_VALUE;
            int r1 = Integer.MAX_VALUE;
            int r2 = Integer.MAX_VALUE;

            // Determine values of l1, l2, r1, and r2
            if (mid1 < n1)
                r1 = data1[mid1];
            if (mid2 < n2)
                r2 = data2[mid2];
            if (mid1 - 1 >= 0)
                l1 = data1[mid1 - 1];
            if (mid2 - 1 >= 0)
                l2 = data2[mid2 - 1];

            if (l1 <= r2 && l2 <= r1) {
                // The partition is correct, we found the median
                if (n % 2 == 1)
                    return Math.max(l1, l2);
                else
                    return ((double) (Math.max(l1, l2) + Math.min(r1, r2))) / 2.0;
            } else if (l1 > r2) {
                // Move towards the left side of the data1
                high = mid1 - 1;
            } else {
                // Move towards the right side of the data1
                low = mid1 + 1;
            }
        }

        return 0; // If the execution reaches here, the input arrays were not sorted.
    }
}