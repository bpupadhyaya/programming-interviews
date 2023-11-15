// You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing
// the number of elements in nums1 and nums2 respectively.
// Merge nums1 and nums2 into a single array sorted in non-decreasing order.
// The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate
// this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
// Example 1:
// Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
// Output: [1,2,2,3,5,6]
// Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
// The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
// Soln: two pointer
// Time complexity ~ O(m+n)
// Space complexity ~ O(1)
//
// Tag: 1/150
// Tag: 88/2927, R9/2936 (overall frequency ranking)

class MergeSortedArrayTwoPointer {
    public static void main(String...args) {
        int[] nums1 = {4,5,8,0,0,0,0};
        int m = 3;
        int[] nums2 = {6,7,8,9};
        int n = 4;
        merge(nums1, m, nums2, n);
        for (int i = 0; i < nums1.length; i++) {
            System.out.print(nums1[i] + ",");
        }
        System.out.println();

    }

    static void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;
        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }
    }
}

// Solution idea:
// The main idea behind multiple pointers is that we start from the highest elements in both the array.
// Compare the highest elements in both the arrays; whichever is higher, copy that to the max. available index
// in nums1. Next, compare two highest available elements again and copy the greater one to the next max. available index
// in nums1. Repeat this process. Our lower bound is index of both nums1 and nums2 should not be less than 0.
// Less than 0 index is not available and that will resutl an error. That is the check we have in the above code:
// while and if LOCs.