// Given an integer array nums and an integer k, return the kth largest element in the array.
// Note that it is the kth largest element in the sorted order, not the kth distinct element.
// Can you solve it without sorting?
// Sample 1:
// Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
// Output: 4
//
// Tag: 121/150
// Tag: 215/2927, R24/2936 (overall frequency ranking), fb R2/50

import java.util.Random;
class KthLargestElementInAnArray {
    public static void main(String[] args) {
        int[] nums = {3,2,3,1,2,4,5,5,6};
        int k = 4;
        System.out.println("Kth largest: " + findKthLargest(nums, k));

    }

    static int findKthLargest(int[] nums, int k) {
        return quickSelect(nums, 0, nums.length - 1, nums.length - k);
    }

    private static int quickSelect(int[] nums, int left, int right, int k) {
        if (left == right)
            return nums[left];
        int pIndex = new Random().nextInt(right - left + 1) + left;
        pIndex = partition(nums, left, right, pIndex);

        if (pIndex == k)
            return nums[k];
        else if (pIndex < k)
            return quickSelect(nums, pIndex + 1, right, k);

        return quickSelect(nums, left, pIndex - 1, k);
    }

    private static int partition(int[] nums, int left, int right, int pIndex) {
        int pivot = nums[pIndex];
        swap(nums, pIndex, right);
        pIndex = left;

        for (int i = left; i <= right; i++)
            if (nums[i] <= pivot)
                swap(nums, i, pIndex++);

        return pIndex - 1;
    }

    private static void swap(int[] nums, int x, int y) {
        int temp = nums[x];
        nums[x] = nums[y];
        nums[y] = temp;
    }
}