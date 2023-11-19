// Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
// The overall run time complexity should be O(log (m+n)).
// Example:
// Input: nums1 = [1,2], nums2 = [3,4]
// Output: 2.50000
// Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
//
// Tag: 120/150
// Tag: 4/2927, R14/2936 (overall frequency ranking)

class MedianOfTwoSortedArrays {
    public static void main(String[] args) {
        int[] nums1 = {1, 2};
        int[] nums2 = {3, 4};
        System.out.println("Median...: " + findMedianSortedArrays(nums1, nums2));
    }

    static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n1 = nums1.length, n2 = nums2.length;

        // Ensure nums1 is the smaller array for simplicity
        if (n1 > n2)
            return findMedianSortedArrays(nums2, nums1);

        int n = n1 + n2;
        int left = (n1 + n2 + 1) / 2; // Calculate the left partition size
        int low = 0, high = n1;

        while (low <= high) {
            int mid1 = (low + high) >> 1; // Calculate mid index for nums1
            int mid2 = left - mid1; // Calculate mid index for nums2

            int l1 = Integer.MIN_VALUE, l2 = Integer.MIN_VALUE;
            int r1 = Integer.MAX_VALUE, r2 = Integer.MAX_VALUE;

            // Determine values of l1, l2, r1, and r2
            if (mid1 < n1)
                r1 = nums1[mid1];
            if (mid2 < n2)
                r2 = nums2[mid2];
            if (mid1 - 1 >= 0)
                l1 = nums1[mid1 - 1];
            if (mid2 -1 >= 0)
                l2 = nums2[mid1 - 1];

            if (l1 <= r2 && l2 <= r1) {
                // The partition is correct, we found the median
                if (n % 2 == 1)
                    return Math.max(l1, l2);
                else
                    return ((double) (Math.max(l1, l2) + Math.min(r1, r2))) / 2.0;
            } else if (l1 > l2) {
                // Move toard the left side of nums1
                high = mid1 - 1;
            } else {
                // Move towards the right side of nums1
                low = mid1 + 1;
            }
        }

        return 0; // If the control reaches here, the input arrays were not sorted.
    }
}

// Method: Binary Search
// - Use binary search to partition the smaller of the two input arrays into two parts.
// - Find the partition of the larger array such that the sum of elements on the left side of the partition in both
// arrays is half of the total elements.
// - Check if this partition is valid by verifying if the largest number on the left side is smaller than the smallest
// number on the right side.
// - If the partition is valid, calculate and return the median.
// Time Complexity ~ O(logm/logn)
// Space Complexity ~O(1)